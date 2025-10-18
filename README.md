# Sistema de Avaliação de Colaboradores

Sistema web para análise e avaliação de colaboradores usando dados do Google Sheets.

## Funcionalidades

- 📊 **Dashboard interativo** com métricas de avaliação
- 📈 **Análise por colaborador, setor, loja e região**
- 🕐 **Análise temporal** por hora do dia
- 📋 **Relatórios exportáveis** em Excel
- 🏪 **Suporte a múltiplas lojas** (RJ e SP)
- 👥 **Ranking de avaliadores**

## Configuração

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar credenciais do Google Sheets

**📋 Instruções detalhadas**: Consulte o arquivo `CONFIGURAR_CREDENCIAIS.md`

1. **Baixe o arquivo JSON** de credenciais do Google Cloud Console
2. **Crie o arquivo** `.streamlit/secrets.toml` com suas credenciais:

```toml
[gcp_service_account]
type = "service_account"
project_id = "seu-projeto"
private_key_id = "sua-chave-privada-id"
private_key = '''-----BEGIN PRIVATE KEY-----
SUA_CHAVE_PRIVADA_COMPLETA_AQUI
-----END PRIVATE KEY-----'''
client_email = "sua-service-account@seu-projeto.iam.gserviceaccount.com"
client_id = "seu-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/sua-service-account%40seu-projeto.iam.gserviceaccount.com"
universe_domain = "googleapis.com"
```

3. **Compartilhe a planilha** com a service account (permissão de Editor)

### 3. Executar a aplicação

```bash
streamlit run colab.py
```

## Estrutura dos Dados

O sistema espera dados no Google Sheets com a seguinte estrutura:

| Coluna | Descrição |
|--------|-----------|
| A | Data |
| B | Setor |
| C | Colaborador |
| D | Velocidade |
| F | Atendimento |
| H | Qualidade |
| J | Ajuda |
| M | Avaliador |

## Mapeamento de Regiões

### Rio de Janeiro (RJ)
- Carioca
- Santa Cruz
- Mesquita
- Nilópolis
- Madureira
- Bonsucesso

### São Paulo (SP)
- Taboão
- São Bernardo
- Santo André
- Mauá
- MDC São Mateus
- CDM São Mateus

## Funcionalidades Principais

### Filtros Disponíveis
- 📅 **Período**: Filtro por data
- 🗺️ **Região**: RJ, SP ou todas
- 🏪 **Loja**: Filtro por loja específica
- 📋 **Setor**: Filtro por setor
- 🕐 **Horário**: Filtro por faixa de hora

### Relatórios
- 📊 **Resumo por Pessoa**: Performance individual
- 🏬 **Resumo por Setor**: Performance por setor
- 🏪 **Resumo por Loja**: Performance por loja
- 🗺️ **Resumo por Região**: Performance por região
- 👥 **Ranking de Avaliadores**: Quem mais avalia
- ⏰ **Volume por Hora**: Análise temporal

### Exportação
- 📄 **Excel**: Relatório completo com uma aba por loja
- 📋 **CSV**: Dados filtrados para análise externa

## Tecnologias Utilizadas

- **Streamlit**: Interface web
- **Pandas**: Manipulação de dados
- **Google Sheets API**: Integração com planilhas
- **Altair**: Visualizações
- **XlsxWriter/OpenPyxl**: Exportação Excel
