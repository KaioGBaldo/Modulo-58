import pytest
import factory
from loja.models import Product

# Definindo a Factory
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = 'Teclado Mecânico'
    description = 'Teclado RGB com switches blue'
    price = 250.00
    active = True

# O decorator @pytest.mark.django_db permite acessar o banco de dados de teste
@pytest.mark.django_db
def test_create_product():
    product = ProductFactory() # Cria um produto usando a factory
    assert product.title == 'Teclado Mecânico'
    assert Product.objects.count() == 1
