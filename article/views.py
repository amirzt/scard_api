from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from article.models import Article
from article.serializers import ArticleSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def get_articles(request):
    articles = Article.objects.filter(is_active=True).order_by('-created_at')
    if 'special' in request.data:
        articles = articles.filter(is_special=True)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
