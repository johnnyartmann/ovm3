"""
Módulo para renderizar os botões de navegação das abas.
Os botões são renderizados de forma oculta (invisível) e são clicados
programaticamente via JavaScript pelos botões visuais do header.
"""
import streamlit as st


def render_hidden_tab_buttons():
    """
    Renderiza os botões de navegação das abas de forma oculta.

    Estes botões são escondidos visualmente via CSS, mas mantêm sua funcionalidade
    para serem clicados pelo JavaScript do header customizado.

    Abas disponíveis:
    - Análise Geral
    - Análise de Feminicídios
    - Metodologia e Glossário
    - Download de Dados
    """

    # CSS para esconder completamente os botões Streamlit
    # Eles ficam invisíveis mas funcionais para o JavaScript
    st.markdown("""
    <style>
        /* Esconde TODOS os botões secundários Streamlit da área principal */
        /* (o header usa botões HTML customizados, não afetados por isto) */
        section.main button[data-testid="baseButton-secondary"] {
            position: absolute !important;
            left: -9999px !important;
            top: -9999px !important;
            width: 1px !important;
            height: 1px !important;
            overflow: hidden !important;
            opacity: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
            pointer-events: auto !important; /* Mantém clicável para JS */
        }

        /* Esconde também os containers dos botões */
        section.main .stButton {
            position: absolute !important;
            left: -9999px !important;
            width: 1px !important;
            height: 1px !important;
            overflow: hidden !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        /* Esconde linhas de colunas que contêm os botões */
        section.main .stHorizontalBlock {
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Botões mantidos apenas para funcionalidade (completamente invisíveis)
    # O JavaScript do header.py vai clicar nestes botões quando o usuário
    # clicar nos botões visuais do header
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📊 Análise Geral", key="btn_ag"):
            st.session_state.active_tab = "Análise Geral"
            st.rerun()

    with col2:
        if st.button("🚨 Análise de Feminicídios", key="btn_af"):
            st.session_state.active_tab = "Análise de Feminicídios"
            st.rerun()

    with col3:
        if st.button("📖 Metodologia e Glossário", key="btn_mg"):
            st.session_state.active_tab = "Metodologia e Glossário"
            st.rerun()

    with col4:
        if st.button("📥 Download de Dados", key="btn_dd"):
            st.session_state.active_tab = "Download de Dados"
            st.rerun()
