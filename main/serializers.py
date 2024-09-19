from rest_framework import serializers
from main.models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Product.
    Позволяет валидировать цену и название.
    """
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, value: int or float) -> int or float:
        """
        Проверка поля цена
        :param value: Цена продукта
        :raise: serializers.ValidationError, если цена неположительна
        :return: Цена продукта
        """
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть положительной.")
        return value

    def validate_name(self, value :str) -> str:
        """
        Проверка поля название на наличие символов
        :param value: Название продукта
        :raise: serializers.ValidationError, если название пустое
        :return: Название продукта
        """
        if not value.strip():
            raise serializers.ValidationError("Название не должно быть пустым.")
        return value