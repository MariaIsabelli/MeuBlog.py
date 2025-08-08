# 📝 Projeto Blog - Django

Este projeto foi desenvolvido como parte da **Unidade 3** da disciplina, com o objetivo de praticar os conceitos de **Programação Orientada a Objetos (POO)** aplicados ao framework **Django**.

O sistema consiste em um **blog simples**, que permite criar, visualizar, editar e excluir postagens, explorando os principais fundamentos do Django aprendidos em aula.

---

## 📚 Conteúdo Abordado

Durante o desenvolvimento do projeto, foram aplicados os seguintes conceitos e recursos:

- **POO no Python** (classes, herança, encapsulamento, polimorfismo)
- Estrutura de um projeto Django
- Configuração do ambiente e servidor de desenvolvimento
- Criação de apps dentro do projeto
- Definição de **models** para representar os dados
- Criação de **views** e **templates**
- Uso do **Django ORM** para manipulação do banco de dados
- URLs e roteamento
- Admin do Django para gerenciamento de conteúdo
- Integração HTML + CSS para estilização básica

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.x**
- **Django 4.x**
- SQLite (banco de dados padrão do Django)
- HTML5, CSS3 e Bootstrap (opcional)
- Git & GitHub para versionamento

---

## 🚀 Como Executar o Projeto

1. **Clone este repositório**
   git clone https://github.com/usuario/nome-do-repositorio.git
   cd nome-do-repositorio
2. **Crie e ative um ambiente virtual**
    python -m venv venv
    source venv/bin/activate   # Linux / Mac
    venv\Scripts\activate      # Windows
3. **Instale as dependências**
    pip install -r requirements.txt
4. **Execute as migrações do banco de dados**
    python manage.py migrate
5. **Crie um superusuário (para acessar o admin)**
    python manage.py createsuperuser
6. **Inicie o servidor de desenvolvimento**
    python manage.py runserver
7. **Acesse no navegador**
    Blog: http://127.0.0.1:8000/
    Django Admin: http://127.0.0.1:8000/admin/

## 🛠 Funcionalidades Implementadas
- Listagem de postagens.

- Visualização detalhada de cada postagem.

- CRUD de postagens (Create, Read, Update, Delete).

