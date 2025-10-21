# mobile_utils.py — Utilitários para otimização mobile
import streamlit as st
import streamlit.components.v1 as components

def detect_mobile():
    """Detecta se o usuário está em um dispositivo móvel"""
    try:
        # Verificar se há informações sobre o user agent
        if hasattr(st, 'session_state') and 'mobile_detected' in st.session_state:
            return st.session_state.mobile_detected
        
        # JavaScript para detectar mobile
        mobile_js = """
        <script>
        function isMobile() {
            return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ||
                   window.innerWidth <= 768;
        }
        window.parent.postMessage({type: 'mobile_detection', isMobile: isMobile()}, '*');
        </script>
        """
        
        # Usar componente para executar JavaScript
        components.html(mobile_js, height=0)
        
        return False  # Default para desktop
    except:
        return False

def get_mobile_config():
    """Retorna configurações específicas para mobile"""
    return {
        'sidebar_collapsed': True,
        'columns_single': True,
        'compact_mode': True,
        'hide_metrics': False,
        'simplified_filters': True
    }

def apply_mobile_styles():
    """Aplica estilos CSS específicos para mobile"""
    mobile_css = """
    <style>
    /* Mobile optimizations */
    @media (max-width: 768px) {
        /* Sidebar mais compacta */
        .css-1d391kg {
            width: 200px !important;
        }
        
        /* Métricas em coluna única */
        .metric-container {
            margin-bottom: 10px;
        }
        
        /* Botões maiores para touch */
        .stButton > button {
            min-height: 44px;
            font-size: 16px;
        }
        
        /* Inputs maiores */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > select {
            min-height: 44px;
            font-size: 16px;
        }
        
        /* Tabelas responsivas */
        .dataframe {
            font-size: 12px;
        }
        
        /* Espaçamento otimizado */
        .main .block-container {
            padding: 1rem;
        }
        
        /* Headers menores */
        h1 { font-size: 1.5rem; }
        h2 { font-size: 1.3rem; }
        h3 { font-size: 1.1rem; }
    }
    
    /* Melhorias gerais para touch */
    .stButton > button:hover {
        transform: none;
    }
    
    /* Scroll suave */
    html {
        scroll-behavior: smooth;
    }
    </style>
    """
    
    st.markdown(mobile_css, unsafe_allow_html=True)

def create_mobile_metrics(data, cols=2):
    """Cria métricas otimizadas para mobile"""
    if cols == 1:
        # Uma coluna para mobile
        st.metric("Avaliações", int(data.shape[0]))
        st.metric("Média Velocidade", round(data["Velocidade"].mean() if len(data) else 0, 2))
        st.metric("Média Atendimento", round(data["Atendimento"].mean() if len(data) else 0, 2))
        st.metric("Média Qualidade", round(data["Qualidade"].mean() if len(data) else 0, 2))
        st.metric("Média Ajuda", round(data["Ajuda"].mean() if len(data) else 0, 2))
    else:
        # Layout original para desktop
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.metric("Avaliações (linhas)", int(data.shape[0]))
        with col2: st.metric("Média Velocidade", round(data["Velocidade"].mean() if len(data) else 0, 2))
        with col3: st.metric("Média Atendimento", round(data["Atendimento"].mean() if len(data) else 0, 2))
        with col4: st.metric("Média Qualidade", round(data["Qualidade"].mean() if len(data) else 0, 2))
        with col5: st.metric("Média Ajuda", round(data["Ajuda"].mean() if len(data) else 0, 2))

def create_mobile_filters(current_user):
    """Cria filtros otimizados para mobile"""
    st.sidebar.markdown("### 📱 Filtros")
    
    # Filtros essenciais primeiro
    with st.sidebar.expander("📅 Data", expanded=True):
        # Implementar filtro de data simplificado
        pass
    
    with st.sidebar.expander("🏢 Setor", expanded=False):
        # Implementar filtro de setor
        pass
    
    # Filtros avançados colapsados
    with st.sidebar.expander("⚙️ Avançado", expanded=False):
        # Filtros adicionais
        pass

def optimize_dataframe_for_mobile(df, max_rows=100):
    """Otimiza dataframe para visualização mobile"""
    if len(df) > max_rows:
        st.warning(f"⚠️ Mostrando apenas {max_rows} de {len(df)} registros para melhor visualização mobile")
        return df.head(max_rows)
    return df
