# Sistema de Gestão de Tarefas

## Descrição
Este é um sistema simples de gestão de tarefas onde os usuários podem criar, visualizar, atualizar e excluir tarefas.

## Pré-requisitos
Certifique-se de ter o Python 3.9 ou superior instalado em seu sistema. Além disso, instale o Docker e Docker Compose para containerizar a aplicação.

## Instalação
Para instalar o projeto, siga os seguintes passos:

```bash
git clone https://github.com/Eduardo-Silva-dev/Gestao_Tarefas.git
cd Gestao_Tarefas

# Crie e ative um ambiente virtual
python3 -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Configure o banco de dados
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

# Execute a aplicação
python app.py
```

## Usando Docker
Para executar a aplicação usando Docker, siga os seguintes passos:

```bash
# Construa a imagem Docker
docker build -t task-manager .

# Inicie os contêineres usando Docker Compose
docker-compose up
```

##### A aplicação estará disponível em http://localhost:5000.

## Documentação da API
| URL                                                 | Metodo       | Descrição                           |
|:----------------------------------------------------| :--------- | :---------------------------------- |
| `http://localhost:5000/tasks` | `POST` | Criar uma nova tarefa |
| `http://localhost:5000/tasks`  | `GET` | 	Listar todas as tarefas |
| `http://localhost:5000/tasks/<int:id>` | `PUT` | Atualizar uma tarefa existente |
| `http://localhost:5000/tasks/<int:id>/complete`  | `PUT` | Marcar uma tarefa como concluída |
| `http://localhost:5000/tasks/<int:id>` | `DELETE` | Excluir uma tarefa |''

## Observações
- Certifique-se de que todas as portas necessárias estejam livres antes de iniciar a aplicação com Docker.
- Verifique se todas as dependências foram instaladas corretamente antes de executar a aplicação.
