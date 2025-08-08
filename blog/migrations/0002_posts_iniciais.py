from django.db import migrations

def criar_posts_iniciais(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Post.objects.create(
        titulo="Introdução ao Django",
        conteudo=(
            "Django é um framework web de alto nível escrito em Python, "
            "que incentiva o desenvolvimento rápido e o design limpo e pragmático. "
            "Ele segue o padrão MVT (Model-View-Template) e vem com uma série de "
            "funcionalidades integradas como autenticação, painel admin e ORM."
        )
    )
    Post.objects.create(
        titulo="Introdução ao Flask",
        conteudo=(
            "Flask é um microframework em Python focado em simplicidade e flexibilidade. "
            "Diferente do Django, ele é minimalista e deixa o desenvolvedor escolher "
            "bibliotecas adicionais para lidar com formulários, autenticação, etc."
        )
    )
    Post.objects.create(
        titulo="Django vs Flask",
        conteudo=(
            "Django é mais completo, ideal para aplicações grandes e estruturadas, "
            "enquanto Flask oferece mais liberdade e é ótimo para APIs pequenas "
            "ou protótipos rápidos. A escolha depende do tipo de projeto."
        )
    )

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(criar_posts_iniciais),
    ]
