from rest_framework import serializers
from demo_app.models import Article, Author


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fileds = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        # author = AuthorSerializer()
        model = Article
        fields = '__all__'
