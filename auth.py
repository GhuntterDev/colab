# auth.py — Sistema de Autenticação
import bcrypt
import streamlit as st
from typing import Dict, List, Optional, Tuple

# Usuários administrativos (acesso a todas as lojas)
ADMIN_USERS = {
    "GhtDev": {
        "password_hash": "$2b$12$OnIkl662ci5vz6qLSgoX1.hxXMAUs6H9c/EYhbLubDCmaqBEzT0pq",  # 18111997
        "role": "admin",
        "name": "GhtDev",
        "access_level": "all_stores"
    },
    "Monitoramento": {
        "password_hash": "$2b$12$4Db7oIeIU9Scj4f8XtMkjelAs0Q4S5iezRKA5CteWWEAruuPAIEVy",  # Monitoramento
        "role": "admin", 
        "name": "Monitoramento",
        "access_level": "all_stores"
    }
}

# Usuários de loja (acesso restrito às próprias lojas)
STORE_USERS = {
    "Carioca": {
        "password_hash": "$2b$12$Na7gsSgxP2sv6Zz0SJYdfeniqNiedmpb./6hGbBu7fOlcsjWBX3hq",  # loja123
        "role": "store",
        "name": "Carioca",
        "access_level": "Carioca"
    },
    "Santa Cruz": {
        "password_hash": "$2b$12$Na7gsSgxP2sv6Zz0SJYdfeniqNiedmpb./6hGbBu7fOlcsjWBX3hq",  # loja123
        "role": "store",
        "name": "Santa Cruz", 
        "access_level": "Santa Cruz"
    },
    "Mesquita": {
        "password_hash": "$2b$12$Na7gsSgxP2sv6Zz0SJYdfeniqNiedmpb./6hGbBu7fOlcsjWBX3hq",  # loja123
        "role": "store",
        "name": "Mesquita",
        "access_level": "Mesquita"
    },
    "Nilópolis": {
        "password_hash": "$2b$12$Na7gsSgxP2sv6Zz0SJYdfeniqNiedmpb./6hGbBu7fOlcsjWBX3hq",  # loja123
        "role": "store",
        "name": "Nilópolis",
        "access_level": "Nilópolis"
    },
    "Madureira": {
        "password_hash": "$2b$12$Na7gsSgxP2sv6Zz0SJYdfeniqNiedmpb./6hGbBu7fOlcsjWBX3hq",  # loja123
        "role": "store",
        "name": "Madureira",
        "access_level": "Madureira"
    },
    "Bonsucesso": {
        "password_hash": "$2b$12$Na7gsSgxP2sv6Zz0SJYdfeniqNiedmpb./6hGbBu7fOlcsjWBX3hq",  # loja123
        "role": "store",
        "name": "Bonsucesso",
        "access_level": "Bonsucesso"
    },
    "Taboão": {
        "password_hash": "$2b$12$Na7gsSgxP2sv6Zz0SJYdfeniqNiedmpb./6hGbBu7fOlcsjWBX3hq",  # loja123
        "role": "store",
        "name": "Taboão",
        "access_level": "Taboão"
    },
    "São Bernardo": {
        "password_hash": "$2b$12$Na7gsSgxP2sv6Zz0SJYdfeniqNiedmpb./6hGbBu7fOlcsjWBX3hq",  # loja123
        "role": "store",
        "name": "São Bernardo",
        "access_level": "São Bernardo"
    },
    "Santo André": {
        "password_hash": "$2b$12$Na7gsSgxP2sv6Zz0SJYdfeniqNiedmpb./6hGbBu7fOlcsjWBX3hq",  # loja123
        "role": "store",
        "name": "Santo André",
        "access_level": "Santo André"
    },
    "Mauá": {
        "password_hash": "$2b$12$Na7gsSgxP2sv6Zz0SJYdfeniqNiedmpb./6hGbBu7fOlcsjWBX3hq",  # loja123
        "role": "store",
        "name": "Mauá",
        "access_level": "Mauá"
    },
    "MDC São Mateus": {
        "password_hash": "$2b$12$Na7gsSgxP2sv6Zz0SJYdfeniqNiedmpb./6hGbBu7fOlcsjWBX3hq",  # loja123
        "role": "store",
        "name": "MDC São Mateus",
        "access_level": "MDC São Mateus"
    },
    "CDM São Mateus": {
        "password_hash": "$2b$12$Na7gsSgxP2sv6Zz0SJYdfeniqNiedmpb./6hGbBu7fOlcsjWBX3hq",  # loja123
        "role": "store",
        "name": "CDM São Mateus",
        "access_level": "CDM São Mateus"
    }
}

def hash_password(password: str) -> str:
    """Gera hash da senha usando bcrypt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """Verifica se a senha corresponde ao hash"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def authenticate_user(username: str, password: str) -> Optional[Dict]:
    """Autentica usuário e retorna dados do usuário se válido"""
    # Verificar usuários administrativos
    if username in ADMIN_USERS:
        user_data = ADMIN_USERS[username]
        if verify_password(password, user_data["password_hash"]):
            return user_data
    
    # Verificar usuários de loja
    if username in STORE_USERS:
        user_data = STORE_USERS[username]
        if verify_password(password, user_data["password_hash"]):
            return user_data
    
    return None

def get_user_stores(user_data: Dict) -> List[str]:
    """Retorna lista de lojas que o usuário pode acessar"""
    if user_data["role"] == "admin":
        return []  # Lista vazia significa acesso a todas as lojas
    else:
        return [user_data["access_level"]]

def is_authenticated() -> bool:
    """Verifica se o usuário está autenticado"""
    return "authenticated" in st.session_state and st.session_state.authenticated

def get_current_user() -> Optional[Dict]:
    """Retorna dados do usuário atual"""
    if is_authenticated():
        return st.session_state.get("user_data")
    return None

def login_user(user_data: Dict):
    """Define usuário como autenticado"""
    st.session_state.authenticated = True
    st.session_state.user_data = user_data

def logout_user():
    """Remove autenticação do usuário"""
    if "authenticated" in st.session_state:
        del st.session_state.authenticated
    if "user_data" in st.session_state:
        del st.session_state.user_data

def show_login_form():
    """Exibe formulário de login"""
    st.title("🔐 Login - Avaliação de Colaboradores")
    
    with st.form("login_form"):
        st.markdown("### Entre com suas credenciais")
        
        username = st.text_input("Usuário", placeholder="Digite seu usuário")
        password = st.text_input("Senha", type="password", placeholder="Digite sua senha")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            login_button = st.form_submit_button("Entrar", use_container_width=True)
        with col2:
            if st.form_submit_button("Limpar", use_container_width=True):
                st.rerun()
        
        if login_button:
            if not username or not password:
                st.error("⚠️ Por favor, preencha todos os campos")
                return False
            
            user_data = authenticate_user(username, password)
            if user_data:
                login_user(user_data)
                st.success(f"✅ Login realizado com sucesso! Bem-vindo, {user_data['name']}")
                st.rerun()
            else:
                st.error("❌ Usuário ou senha incorretos")
                return False
    
    # Informações sobre os usuários disponíveis
    with st.expander("ℹ️ Usuários disponíveis"):
        st.markdown("""
        **Usuários Administrativos (acesso a todas as lojas):**
        - GhtDev
        - Monitoramento
        
        **Usuários de Loja (acesso restrito):**
        - Carioca, Santa Cruz, Mesquita, Nilópolis, Madureira, Bonsucesso
        - Taboão, São Bernardo, Santo André, Mauá, MDC São Mateus, CDM São Mateus
        """)

def show_logout_button():
    """Exibe botão de logout na sidebar"""
    if is_authenticated():
        user_data = get_current_user()
        st.sidebar.markdown("---")
        st.sidebar.markdown(f"**Usuário:** {user_data['name']}")
        st.sidebar.markdown(f"**Tipo:** {'Administrador' if user_data['role'] == 'admin' else 'Loja'}")
        
        if st.sidebar.button("🚪 Sair", use_container_width=True):
            logout_user()
            st.rerun()

def filter_data_by_user_access(data, user_data):
    """Filtra dados baseado no acesso do usuário"""
    if user_data["role"] == "admin":
        return data  # Administradores veem tudo
    else:
        # Usuários de loja veem apenas sua loja
        store_name = user_data["access_level"]
        return data[data["Loja"] == store_name]
