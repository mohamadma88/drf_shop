from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer
from .pagination import StandardResultsSetPagination
from django.db.models import Q

class ArticleList(APIView, StandardResultsSetPagination):

    def get(self, request):
        queryset = Article.objects.all()
        result = self.paginate_queryset(queryset, request)
        serializer = ArticleSerializer(instance=result, many=True)
        return self.get_paginated_response(serializer.data)


class AddArticle(APIView):
    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser,)

    def get(self, request, slug):
        obj = Article.objects.get(slug=slug)
        serializer = ArticleSerializer(instance=obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SearchProduct(APIView, StandardResultsSetPagination):

    def get(self, request):
        q = Article.objects.get('q')
        queryset = Article.objects.filter(Q(title=q))
        result = self.paginate_queryset(queryset, request)
        serializer = ArticleSerializer(instance=result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
