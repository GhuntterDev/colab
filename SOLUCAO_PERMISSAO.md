# 🔐 SOLUÇÃO: Erro de Permissão no Google Sheets

## ❌ Problema Identificado
**Erro**: `PermissionError` - A service account não tem permissão para acessar a planilha.

**Service Account**: `ghuntter@uplifted-water-472222-k7.iam.gserviceaccount.com`
**Planilha**: https://docs.google.com/spreadsheets/d/196mkyj8XPLouscoiJqmarCJ4H5N7ANnAhmH6V-uXSlw/edit

## ✅ SOLUÇÃO

### 1. Compartilhar a Planilha

1. **Abra a planilha** no Google Sheets:
   - URL: https://docs.google.com/spreadsheets/d/196mkyj8XPLouscoiJqmarCJ4H5N7ANnAhmH6V-uXSlw/edit

2. **Clique no botão "Compartilhar"** (canto superior direito)

3. **Adicione o email da service account**:
   ```
   ghuntter@uplifted-water-472222-k7.iam.gserviceaccount.com
   ```

4. **Defina a permissão**:
   - ✅ **Editor** (recomendado) ou **Leitor**
   - ❌ **Não marque** "Notificar pessoas"

5. **Clique em "Enviar"**

### 2. Verificar se Funcionou

Após compartilhar, execute o teste:

```bash
cd "C:\Users\Ghuntter\Documents\PROGRAMAS\COLABORADORES"
python check_permissions.py
```

### 3. Se Ainda Não Funcionar

#### Opção A: Verificar Service Account no Google Cloud Console

1. Acesse: https://console.cloud.google.com/
2. Vá para **IAM & Admin > Service Accounts**
3. Verifique se `ghuntter@uplifted-water-472222-k7.iam.gserviceaccount.com` está ativa
4. Se necessário, gere uma nova chave JSON

#### Opção B: Usar uma Nova Service Account

1. No Google Cloud Console, crie uma nova service account
2. Baixe o arquivo JSON de credenciais
3. Substitua o arquivo `service_account.json`
4. Compartilhe a planilha com o novo email

#### Opção C: Verificar se a Planilha Existe

1. Confirme se a planilha está acessível pelo seu usuário Google
2. Verifique se não há restrições de domínio
3. Teste acessar a planilha em modo anônimo

## 🧪 Teste Final

Após resolver o problema de permissão:

```bash
cd "C:\Users\Ghuntter\Documents\PROGRAMAS\COLABORADORES"
streamlit run colab.py
```

A aplicação deve carregar os dados do Google Sheets sem erros.

## 📞 Precisa de Ajuda?

Se o problema persistir:
1. Verifique se você tem acesso à planilha
2. Confirme se a service account está ativa
3. Tente criar uma nova service account
4. Verifique se não há restrições de firewall/proxy

