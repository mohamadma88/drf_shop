from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView, Response
from .models import Product
from .serializers import ProductSerializer
from .pagination import StandardResultsSetPagination
from rest_framework.parsers import MultiPartParser


class ProductView(APIView, StandardResultsSetPagination):
    serializer_class = ProductSerializer

    def get(self, request):
        queryset = Product.objects.all()
        result = self.paginate_queryset(queryset, request)
        serializer = ProductSerializer(instance=result, many=True)
        return self.get_paginated_response(serializer.data)


class AddProduct(APIView):
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailProduct(APIView):
    serializer_class = ProductSerializer

    def get(self, request, pk):
        instance = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SearchProduct(APIView,StandardResultsSetPagination):

    def get(self, request):
        q = Product.objects.get('q')
        queryset = Product.objects.filter(Q(title=q))
        result = self.paginate_queryset(queryset,request)
        serializer = ProductSerializer(instance=result,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

