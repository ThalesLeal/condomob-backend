# Condomob-backend

## Instalação e Configuração

Siga os passos abaixo para configurar e executar este projeto no seu ambiente local:

### Passo 1: Clone o repositório
git clone https://github.com/seu-usuario/condomob-backend.git cd condomob-backend

#### Passo 2: Crie um Ambiente Virtual

Recomendamos o uso de um ambiente virtual para isolar as dependências do projeto. Execute os seguintes comandos para criar e ativar um ambiente virtual:

```bash
# Instale o virtualenv, se ainda não estiver instalado
pip install virtualenv

# Crie um ambiente virtual (substitua 'venv' pelo nome que você desejar)
 python -m venv env


# Ative o ambiente virtual
source env/bin/activate
```

#### Passo 3: Instale as Dependências Python

Com o ambiente virtual ativado, você pode instalar as dependências Python listadas no arquivo requirements.txt usando o pip:

```bash
pip install -r requirements.txt
```

###### observações

Configuração
Configurar Variáveis de Ambiente: (Já subi com o .env para facilitar)

Aplicar Migrações do Banco de Dados: python manage.py migrate

Executando o Servidor de Desenvolvimento
Para iniciar o servidor de desenvolvimento do Django: python manage.py runserver

A anexação do arquivo depende do front-end que esta em outro repositorio
