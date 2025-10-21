# 🔐 Como Configurar as Credenciais do Google Sheets

## Problema Atual
O erro "Seção [gcp_service_account] não encontrada em .streamlit/secrets.toml" indica que as credenciais não estão configuradas corretamente.

## Solução

### 1. Obter o Arquivo de Credenciais do Google Cloud

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Vá para **IAM & Admin > Service Accounts**
3. Encontre sua service account `colab-27@uplifted-water-472222-k7.iam.gserviceaccount.com`
4. Clique em **Actions > Manage Keys**
5. Clique em **Add Key > Create new key**
6. Escolha **JSON** e baixe o arquivo

### 2. Configurar o arquivo secrets.toml

Abra o arquivo `.streamlit/secrets.toml` e substitua os valores:

```toml
[gcp_service_account]
type = "service_account"
project_id = "uplifted-water-472222-k7"
private_key_id = "COLE_AQUI_O_private_key_id_DO_JSON"
private_key = '''-----BEGIN PRIVATE KEY-----
COLE_AQUI_A_CHAVE_PRIVADA_COMPLETA_DO_JSON
-----END PRIVATE KEY-----'''
client_email = "colab-27@uplifted-water-472222-k7.iam.gserviceaccount.com"
client_id = "110235144704036821022"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/colab-27%40uplifted-water-472222-k7.iam.gserviceaccount.com"
universe_domain = "googleapis.com"
```

### 3. Copiar os Valores do JSON

No arquivo JSON baixado, copie:

- **`private_key_id`** → substitua "COLE_AQUI_O_private_key_id_DO_JSON"
- **`private_key`** → substitua toda a chave privada (mantenha as quebras de linha)

### 4. Exemplo de Como Ficar

```toml
[gcp_service_account]
type = "service_account"
project_id = "uplifted-water-472222-k7"
private_key_id = "abc123def456ghi789"
private_key = '''-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDHfNQV5Tfmg27m
NeZwg+J8/8Zm4zuOk8UQDzgUNa1uAmRyasGz2XKLZjETQfcp9XfO4+ZinUwhw2Ir
... (toda a chave privada aqui)
-----END PRIVATE KEY-----'''
client_email = "colab-27@uplifted-water-472222-k7.iam.gserviceaccount.com"
client_id = "110235144704036821022"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/colab-27%40uplifted-water-472222-k7.iam.gserviceaccount.com"
universe_domain = "googleapis.com"
```

### 5. Compartilhar a Planilha

Não esqueça de compartilhar sua planilha do Google Sheets com a service account:

1. Abra a planilha: https://docs.google.com/spreadsheets/d/196mkyj8XPLouscoiJqmarCJ4H5N7ANnAhmH6V-uXSlw/edit
2. Clique em **Compartilhar**
3. Adicione o email: `colab-27@uplifted-water-472222-k7.iam.gserviceaccount.com`
4. Dê permissão de **Editor**

### 6. Testar

Após configurar, execute:

```bash
streamlit run colab.py
```

## ⚠️ Importante

- **NUNCA** commite o arquivo `secrets.toml` com credenciais reais
- O arquivo está protegido pelo `.gitignore`
- Use sempre o arquivo de exemplo para referência

