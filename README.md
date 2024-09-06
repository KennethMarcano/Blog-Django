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


Criei os templates para mostrar a lista de posts, un post em especifico com seus comentarios e para editar os posts e comentarios,  estilizei os template com css y usei um pouco de js para mudar alungs atributos.

Parece na sequencia mas na verdade trabalhei en tudo quase que ao mesmo tempo, um dependia do outro entao primeiro fiz para mostrar a rota principal onde ficam os posts e partindo disso fiz o resto como editar um post, ver um post em especifico com seus comentarios.

Depois de conferir que as funcionalidades estavam prontas, fiz os testes, onde tive que pesquisar tambem mas despois de entender 2 exemplos consegui desenvolver os testes.
