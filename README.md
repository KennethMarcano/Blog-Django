# Documentacao

## Requisitos

Precisa instalar:

- Python 3.10.12
- pip 22.0.2
- Django 5.1

## Passos

1) Clona o repositorio:

```
git clone https://github.com/KennethMarcano/Blog-Django.git
```

2) Abre o diretorio clonado no terminal e instala as dependencias:

```
pip install -r requirements.txt
```

3) Faz as migrações: 
```
python3 manage.py migrate  
```
4) Executa o servidor:

```
python3 manage.py runserver
```

5) Para os testes:

```
python3 manage.py test
```

# Desenvolvimento do projeto

Para desenvolver o projeto primeiro foi necessario familiarizarme com Django, porque só tinha programado em python mas nunca usei Django, comecei lendo a documentação oficial e forums em internet para ter uma introdução clara aos fundamentos da framework, como a configurção do projeto, crear models, views e templates.

Comecei com o basico, conferindo o que precisava instalar, neste caso tive que instalar django o python3 já estava instalado no notebook.

Primeiro criei o projeto com:
```
django-admin startproject
```

Na sequencia criei a aplicação 'blog' com:
```
python3 manage.py startapp
```

Depois seguendo os forum e a documentaçao criei os models para los Posts e comentarios e fiz as migrações.

Apos isso fiz as views para logica da aplicação, nesta parte tive que ler muito, ver videos e ate usar ChatGPT, nessa parte mexe durante todo o desenvolvimento da app.

Fiz tambem os formularios para criar ou editar os post e comentarios.

Configurei as rotas da app no arquivo urls.py.

Criei os templates para mostrar a lista de posts, un post em especifico com seus comentarios e para editar os posts e comentarios,  estilizei os template com css y usei um pouco de js para mudar alungs atributos.

Parece na sequencia mas na verdade trabalhei en tudo quase que ao mesmo tempo, um dependia do outro entao primeiro fiz para mostrar a rota principal onde ficam os posts e partindo disso fiz o resto como editar um post, ver um post em especifico com seus comentarios.

Depois de conferir que as funcionalidades estavam prontas, fiz os testes, onde tive que pesquisar tambem mas despois de entender 2 exemplos consegui desenvolver os testes.