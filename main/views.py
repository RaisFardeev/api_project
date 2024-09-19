from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status
from main.models import Product
from main.serializers import ProductSerializer


def main_page(request: HttpRequest) -> HttpResponse:
    """
    Главная страница
    :param request: Объект HTTP-запроса
    :return: HTTP-ответ с рендером шаблона main_page.html
    """
    return render(request, 'main_page.html')


@api_view(['GET'])
def product_list(request: Request) -> Response:
    """
    Вывод всех продуктов
    :param request: Объект DRF запроса
    :return: JSON response содержащий список продуктов.
    """
    products = Product.objects.all()
    serializer: Serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def product_create(request: Request) -> Response:
    """
    Создание нового продукта
    :param request: Объект DRF запроса содержащий информацию о продукте
    :return: JSON response содержащий информацию о продукте или ошибки при валидации.
    """
    serializer: Serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
