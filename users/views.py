import json

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from article.models import Article
from article.serializers import ArticleSerializer
from users.models import CustomUser, OTP, Shop, Favorite, Offer, HomeMessage
import requests

from users.serializers import CustomUserSerializer, ShopSerializer, OfferSerializer, MessageSerializer, \
    RegistrationSerializer


def send_otp(otp, phone):
    pass
    # api_url = "https://api2.ippanel.com/api/v1/sms/pattern/normal/send"
    #
    # headers = {
    #     'Content-Type': 'application/json',
    #     'apikey': 'M-o-KUXHu_VfZgtr6dzrptzXjq0GFeZcoT5pV2PCc34='
    # }
    #
    # body = {
    #     "recipient": phone,
    #     "sender": "3000505",
    #     # "time": "2025-03-21T09:12:50.824Z",
    #     "code": "snad47rjhgnpalm",
    #     "variable": {
    #         "code": otp
    #     }
    # }
    # response = requests.post(api_url, headers=headers, data=json.dumps(body))
    # print(response)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    try:
        user = CustomUser.objects.get(phone=request.data['phone'])

        if user.check_password(request.POST.get('password')):
            user.is_active = True
            user.save()

            token, created = Token.objects.get_or_create(user=user)

            # otp = OTP(user=user)
            # otp.save()
            # send_otp(otp.code, user.phone)

            return Response({
                'token': token.key,
                'exist': True
            }, status=200)
        else:
            return Response({
                'message': 'رمز ورود اشتباه است'
            }, status=403)

    except CustomUser.DoesNotExist:
        user_serializer = RegistrationSerializer(data=request.data)

        if user_serializer.is_valid():
            user = user_serializer.save()

            user.is_active = True
            user.save()

            # otp = OTP(user=user)
            # otp.save()
            # send_otp(otp.code, user.phone)

            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'token': token.key,
                'exist': False
            })

        else:
            return Response(user_serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def check_otp(request):
    otp = OTP.objects.filter(user__phone=request.data['phone']).last()
    if otp.code == request.data['code']:
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_shops(request):
    shops = Shop.objects.filter(is_active=True)
    if 'sort' in request.data:
        if request.data['sort'] == 'score':
            shops = shops.order_by('-score')
        elif request.data['sort'] == 'date':
            shops = shops.order_by('-created_at')

    if 'search' in request.data:
        shops = shops.filter(name__contains=request.data['search'])

    return Response(ShopSerializer(shops, many=True).data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_favorite(request):
    try:
        fav = Favorite.objects.get(offer_id=request.data['offer'],
                                   user=request.user)
        fav.delete()
    except Favorite.DoesNotExist:
        fav = Favorite(offer_id=request.data['offer'],
                       user=request.user)
        fav.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_offers(request):
    offers = Offer.objects.filter(is_active=True,
                                  shop__is_active=True)
    if 'search' in request.data:
        offers = offers.filter(title__contains=request.data['search'])
    if 'shop' in request.data:
        offers = offers.filter(shop_id=request.data['shop'])

    if 'favorite' in request.data:
        offers = offers.filter(favorite__user=request.user,
                               is_active=True)

    if 'sort' in request.data:
        if request.data['sort'] == 'discount':
            offers = offers.order_by('-discount')
        elif request.data['sort'] == 'date':
            offers = offers.order_by('-created_at')

    try:
        user = CustomUser.objects.get(id=request.user.id)
    except:
        user = CustomUser.objects.all().first()
    return Response(OfferSerializer(offers, many=True,
                                    context={'user': user}).data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def splash(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_home(request):
    home_articles = Article.objects.filter(is_active=True,
                                           is_special=True).order_by('-created_at')
    message = HomeMessage.objects.filter(is_active=True).order_by('-created_at').last()
    data = {
        'articles': ArticleSerializer(home_articles, many=True).data,
        'message': MessageSerializer(message).data
    }
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = CustomUser.objects.get(id=request.user.id)
    return Response(CustomUserSerializer(user).data, status=status.HTTP_200_OK)
