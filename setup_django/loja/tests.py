import pytest
from .models import Produto

@pytest.mark.django_db
def test_criacao_produto():
    # Testa se o modelo consegue salvar um objeto corretamente
    produto = Produto.objects.create(
        nome="Teclado Mecânico",
        descricao="Teclado RGB switch blue",
        preco=250.00
    )
    
    assert Produto.objects.count() == 1
    assert produto.nome == "Teclado Mecânico"
