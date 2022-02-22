from django.views.generic import ListView
from mainapp.models import Category, Books, Author
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from mainapp.serializers import CategorySerializer, AuthorSerializer, BooksSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BooksViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


