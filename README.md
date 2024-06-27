# sisvap
Sistema de veículos apreendidos

## Instalação e Configuração

Siga os passos abaixo para configurar e executar este projeto no seu ambiente local:

### Passo 1: Crie um Ambiente Virtual

Recomendamos o uso de um ambiente virtual para isolar as dependências do projeto. Execute os seguintes comandos para criar e ativar um ambiente virtual:

```bash
# Instale o virtualenv, se ainda não estiver instalado
pip install virtualenv

# Crie um ambiente virtual (substitua 'venv' pelo nome que você desejar)
virtualenv venv

# Ative o ambiente virtual
source venv/bin/activate
```

#### Passo 2: Instale as Dependências Python

Com o ambiente virtual ativado, você pode instalar as dependências Python listadas no arquivo requirements.txt usando o pip:

```bash
pip install -r requirements.txt
```

##### Passo 3: Instale as Dependências do Sistema

Para compilar o projeto, você precisará das seguintes dependências do sistema:

libsasl2-dev
libldap2-dev

Você pode instalá-las em sistemas baseados em Debian/Ubuntu com o seguinte comando:

```bash
sudo apt-get install libsasl2-dev libldap2-dev
```
