from rest_framework.serializers import ModelSerializer
from mainapp.models import Category, Books, Author


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
