from rest_framework import serializers

from users.models import CustomUser, Shop, Favorite, Offer, HomeMessage, Support


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['password', 'phone']
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, **kwargs):
        user = CustomUser(phone=self.validated_data['phone'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone', 'expire_date']


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()

    class Meta:
        model = Favorite
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()
    is_favorite = serializers.SerializerMethodField('get_fav')

    def get_fav(self, data):
        fav = Favorite.objects.filter(user=self.context.get('user'),
                                      offer=data)
        return True if fav.count() > 0 else False

    class Meta:
        model = Offer
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeMessage
        fields = '__all__'


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'
