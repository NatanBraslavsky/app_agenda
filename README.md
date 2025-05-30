# 🔎Projeto Agenda de Contatos
Ultimamente tenho focado grande parte do meu tempo nos meus estudos em Python e procurando entender melhor o framework Django. Esse projeto faz parte de um curso que venho me dedicando a um tempo e me ajudou a entender conceitos importantes do framework.

# 🧠Funcionalidades

✅ Cadastro, visualização, edição, remoção e busca de contatos<br>
✅ Fotos de perfil, com tratamento de imagens utilizando a biblioteca Pillow<br>
✅ Contatos fictícios para testes, com uso do pacote Faker<br>
✅ Controle de acesso: apenas usuários autenticados têm permissão para gerenciar seus próprios contatos

# 🛠️Tecnologias:

•Frontend: html, css - Estrutura do projeto<br><br>
•Backend: Python - Linguagem usada na lógica do sistema e construção das funcionalidades<br><br>
•Framework: Django – Utilizado para gerenciar rotas, templates, banco de dados, autenticação e estrutura geral do projeto<br><br>
•Manipulação de Imagens: Pillow – Biblioteca utilizada para lidar com o upload e o processamento de fotos de perfil<br><br>
•Geração de Dados Fictícios: Faker – Usado para criar contatos de teste automaticamente<br><br>
•Versionamento: git | github - Versionamento e colaboração<br><br>

<h2>
    ⚙ Como rodar o projeto
</h2>

1. Clone o repositório:

```git clone https://github.com/natanbraslavsky/app_agenda.git```


2. Instale as dependências:

```pip install -r requirements.txt```



3. Aplique as migrações:

```python manage.py migrate```


(Opcional) Gere dados de teste:


```python utils/create_contacts.py```


4. Inicie o servidor de desenvolvimento:

```python manage.py runserver```


5. Acesse no navegador:


```http://127.0.0.1:8000/```
