#!/usr/bin/env python3
"""
Script de teste para verificar a conexão com Google Sheets
"""

import gspread
import streamlit as st

# ID da planilha extraído da URL
SPREADSHEET_ID = "196mkyj8XPLouscoiJqmarCJ4H5N7ANnAhmH6V-uXSlw"

def test_connection():
    try:
        # Tentar carregar do arquivo JSON primeiro
        try:
            import json
            with open('service_account.json', 'r') as f:
                creds = json.load(f)
            print("Carregando credenciais do arquivo JSON")
        except:
            # Se não conseguir, usar o secrets
            creds = dict(st.secrets["gcp_service_account"])
            print("Carregando credenciais do secrets.toml")
        
        print(f"Service Account: {creds.get('client_email')}")
        
        # Conectar ao Google Sheets
        gc = gspread.service_account_from_dict(creds)
        print("Conectado ao Google Sheets API")
        
        # Tentar abrir a planilha
        sh = gc.open_by_key(SPREADSHEET_ID)
        print(f"Planilha aberta: {sh.title}")
        
        # Listar abas
        ws_list = sh.worksheets()
        print(f"Abas encontradas: {len(ws_list)}")
        for ws in ws_list:
            print(f"   - {ws.title}")
            
        # Testar leitura de uma aba
        if ws_list:
            ws = ws_list[0]
            values = ws.get_all_values()
            print(f"Primeira aba '{ws.title}': {len(values)} linhas")
            if values:
                print(f"   Primeiras colunas: {values[0][:5]}")  # Primeiras 5 colunas do cabeçalho
        
        return True
        
    except Exception as e:
        print(f"Erro: {e}")
        return False

if __name__ == "__main__":
    print("Testando conexao com Google Sheets...")
    print(f"ID da planilha: {SPREADSHEET_ID}")
    print("-" * 50)
    
    success = test_connection()
    
    print("-" * 50)
    if success:
        print("Teste bem-sucedido!")
    else:
        print("Teste falhou!")
