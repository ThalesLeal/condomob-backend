

# Condomob Backend
Este é o backend do projeto Condomob, desenvolvido em Django REST Framework.

## Instalação e Configuração

Siga os passos abaixo para configurar e executar este projeto no seu ambiente local:

# Requisitos
Certifique-se de ter os seguintes requisitos instalados antes de prosseguir:

Python (versão 3.8)
Pip (gerenciador de pacotes do Python)
Ambiente virtual (recomendado)
Instalação
Clone o repositório: git clone https://github.com/seu-usuario/condomob-backend.git cd condomob-backend


### Passo 1: Crie um Ambiente Virtual

Recomendamos o uso de um ambiente virtual para isolar as dependências do projeto. Execute os seguintes comandos para criar e ativar um ambiente virtual:

\`\`\`

# Instale o virtualenv
pip install virtualenv

# Crie um ambiente virtual (substitua 'venv' pelo nome que você desejar)
 python -m venv env

# Ativo o ambiente virtual
source venv/bin/activate 
# no Windows use venv\Scripts\activate

\`\`\`

### Passo 2: Instale as Dependências Python

Com o ambiente virtual ativado, você pode instalar as dependências Python listadas no arquivo requirements.txt usando o pip:

\`\`\`
pip install -r requirements.txt
\`\`\`

\`\`\`
#Configuração
Configurar Variáveis de Ambiente: (Já subi com o .env para facilitar)

#Aplicar Migrações do Banco de Dados: python manage.py migrate

#Executando o Servidor de Desenvolvimento
Para iniciar o servidor de desenvolvimento do Django: python manage.py runserver

#OBS.: A anexação do arquivo depende do front-end que esta em outro repositorio
\`\`\`
