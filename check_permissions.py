#!/usr/bin/env python3
"""
Script para verificar permissões da planilha
"""

import gspread
import json

# ID da planilha extraído da URL
SPREADSHEET_ID = "196mkyj8XPLouscoiJqmarCJ4H5N7ANnAhmH6V-uXSlw"

def check_permissions():
    try:
        # Carregar credenciais do arquivo JSON
        with open('service_account.json', 'r') as f:
            creds = json.load(f)
        
        print(f"Service Account: {creds.get('client_email')}")
        
        # Conectar ao Google Sheets
        gc = gspread.service_account_from_dict(creds)
        print("Conectado ao Google Sheets API")
        
        # Tentar abrir a planilha
        try:
            sh = gc.open_by_key(SPREADSHEET_ID)
            print(f"SUCESSO: Planilha aberta: {sh.title}")
            
            # Listar abas
            ws_list = sh.worksheets()
            print(f"Abas encontradas: {len(ws_list)}")
            for ws in ws_list:
                print(f"   - {ws.title}")
                
            return True
            
        except Exception as e:
            error_msg = str(e)
            print(f"ERRO ao abrir planilha: {error_msg}")
            print(f"Tipo do erro: {type(e).__name__}")
            
            # Verificar se é erro de permissão
            if "403" in error_msg:
                print("\nPROBLEMA DE PERMISSAO:")
                print("A planilha nao esta compartilhada com a service account")
                print(f"Compartilhe a planilha com: {creds.get('client_email')}")
                print("Permissao necessaria: Editor ou Leitor")
            elif "404" in error_msg:
                print("\nPROBLEMA DE ID:")
                print("Planilha nao encontrada. Verifique o ID da planilha")
            elif not error_msg:
                print("\nERRO VAZIO - Possivel problema de conexao ou credenciais")
                print("Verifique:")
                print("1. Se a service account esta ativa")
                print("2. Se as credenciais estao corretas")
                print("3. Se a planilha existe")
            else:
                print(f"\nOUTRO ERRO: {error_msg}")
                
            return False
        
    except Exception as e:
        print(f"Erro geral: {e}")
        return False

if __name__ == "__main__":
    print("Verificando permissoes da planilha...")
    print(f"ID da planilha: {SPREADSHEET_ID}")
    print("-" * 60)
    
    success = check_permissions()
    
    print("-" * 60)
    if success:
        print("Teste bem-sucedido!")
    else:
        print("Teste falhou - verifique as instrucoes acima")
