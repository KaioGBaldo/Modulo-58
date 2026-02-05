# 🏛️ Django Data Modeling - Relacionamentos e Normalização

Este projeto foca na estruturação avançada de bancos de dados relacionais utilizando o ORM do Django. O objetivo principal foi implementar a normalização de dados, separando categorias e produtos para garantir a integridade e a escalabilidade da aplicação.

---

# 📝 Resumo (Resume)
Neste projeto, apliquei conceitos fundamentais de engenharia de dados no Back-End. Estruturei um relacionamento **Many-to-One** (Muitos-para-Um) entre `Produto` e `Categoria`, utilizando chaves estrangeiras (`ForeignKey`). A implementação conta com o parâmetro `related_name='produtos'`, que otimiza o acesso reverso aos dados, e o comportamento `on_delete=models.CASCADE` para manter a consistência referencial. Além disso, utilizei campos de validação como `unique=True` para categorias e `DecimalField` para garantir a precisão matemática em valores monetários, essencial para sistemas de e-commerce e gestão.



## 🚀 Tecnologias e Ferramentas (Tech Stack)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

## 📋 Funcionalidades em Destaque
* **Normalização de Banco de Dados:** Separação de atributos repetitivos em tabelas distintas, reduzindo a redundância e facilitando a manutenção.
* **Relacionamento Reverso (`related_name`):** Configuração que permite acessar todos os produtos vinculados a uma categoria diretamente pelo objeto da categoria.
* **Integridade Referencial:** Uso de `on_delete=models.CASCADE` para garantir que a remoção de uma categoria gerencie automaticamente os produtos órfãos.
* **Tipagem Monetária de Alta Precisão:** Implementação de `DecimalField` para evitar os erros de ponto flutuante comuns em tipos `float`.
* **Auditoria de Dados:** Uso de `DateTimeField(auto_now_add=True)` para rastreio automático do momento de inserção de cada produto.
* **UX Administrativa:** Sobrescrita do método `__str__` para garantir que os objetos sejam identificáveis por nome humano no Django Admin e logs.



---

# 👨‍💻 Sobre mim (About Me)
Olá, meu nome é **Kaio**, tenho 22 anos. Como meu foco principal é o **Back-End com Python**, dominar a modelagem relacional é o que me permite construir sistemas inteligentes. Entender como as tabelas se conectam é fundamental para criar APIs rápidas e seguras. Minha base em Front-End me ajuda a visualizar como esses dados serão exibidos, mas é no Back-End, desenhando esses modelos, que eu garanto que a regra de negócio do mundo real seja replicada com perfeição no código.

### Entre em contato (Contact me)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=092E20)](https://linkedin.com/in/kaio-grativol-baldo-071a74150/)
[![Instagram](https://img.shields.io/badge/Instagram-000?style=for-the-badge&logo=instagram&logoColor=092E20)](https://www.instagram.com/kaiull__/)
[![GitHub](https://img.shields.io/badge/Github-000?style=for-the-badge&logo=github&logoColor=092E20)](https://github.com/SeuUsuarioAqui)

---
*Projeto desenvolvido para consolidar conhecimentos em normalização de dados e relacionamentos avançados no Django ORM.*
