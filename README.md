Sistema de Matrículas (Django, MySQL)

Sobre o projeto:
    Esse projeto foi feito com o objetivo de praticar Django.
    A ideia é ter um controle básico de alunos, professores, cursos e matrículas,
    usando o Django Admin como interface principal.
    Não é um sistema completo, mas aborda várias partes importantes do framework.

Funcionalidades:
    Cadastro de alunos
    Cadastro de professores
    Cadastro de cursos
    Matrícula de alunos em cursos
    Impede que um aluno se matricule duas vezes no mesmo curso
    Controle de status da matrícula (ativo, trancado, concluído)

Durante o desenvolvimento aprendi e pratiquei:
    Criação de models no Django
    Uso de ForeignKey e related_name
    Criação de regras de negócio usando clean()
    Uso de constraints para garantir dados únicos
    Customização do Django Admin
    Migrações e organização do projeto em apps

Tecnologias usadas:
    Python
    Django
    MySQL
    mysqlclient

Como executar o projeto:
    1. Clone o repositório
    2. Crie um ambiente virtual
    3. Instale as dependências (requirements.txt)
    4. Crie um banco de dados MySQL
    5. Rode as migrações
    6. Crie um superuser
    7. Inicie o servidor e acesse o Django Admin

Observações:
    Esse projeto foi feito com foco em aprendizado e prática.
    A interface é baseada no Django Admin e não possui frontend próprio.