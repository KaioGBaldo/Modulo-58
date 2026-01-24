from django.test import TestCase
from .models import Produto, Categoria

class LojaIntegridadeTestCase(TestCase):

    def setUp(self):
        # Prepara uma categoria para os testes de produto
        self.categoria = Categoria.objects.create(nome="Eletrônicos")

    def test_criacao_categoria(self):
        """Verifica se a categoria é salva corretamente"""
        self.assertEqual(Categoria.objects.count(), 1)
        self.assertEqual(self.categoria.nome, "Eletrônicos")

    def test_integridade_produto_e_relacionamento(self):
        """Verifica a criação de produto e sua ligação com categoria"""
        produto = Produto.objects.create(
            nome="Smartphone",
            descricao="Um celular moderno",
            preco=2500.50,
            estoque=10,
            categoria=self.categoria
        )
        
        # Verifica se o produto foi salvo
        self.assertEqual(Produto.objects.count(), 1)
        # Verifica se o relacionamento (ForeignKey) está funcionando
        self.assertEqual(produto.categoria.nome, "Eletrônicos")
        # Verifica se o preço foi salvo com a precisão correta
        self.assertEqual(float(produto.preco), 2500.50)

    def test_constraint_unique_categoria(self):
        """Verifica se o banco impede categorias com nomes duplicados"""
        with self.assertRaises(Exception):
            Categoria.objects.create(nome="Eletrônicos") # Já existe no setUp
