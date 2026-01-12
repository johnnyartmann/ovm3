import streamlit as st

def render_custom_header():
    """
    Renderiza o cabeçalho fixo customizado no topo da página.

    Layout:
    1. Botões de navegação (usando botões Streamlit nativos)
    2. Cards de resumo (Filtros atuais)
    3. Expander para detalhes de municípios (quando necessário)
    """

    # --- CSS PARA HEADER FIXO ---
    header_style = """
    <style>
        /* RESET & Compatibilidade */
        header[data-testid="stHeader"] {
            visibility: visible !important;
            background: transparent !important;
            box-shadow: none !important;
            z-index: 1000005 !important;
            pointer-events: none;
        }

        header[data-testid="stHeader"] > div {
            background: transparent !important;
        }

        [data-testid="stSidebarCollapsedControl"] button,
        [data-testid="stToolbar"] button,
        header[data-testid="stHeader"] button {
            pointer-events: auto !important;
            color: white !important;
            fill: white !important;
        }

        [data-testid="stSidebarCollapsedControl"] {
            display: block !important;
            pointer-events: auto !important;
            color: white !important;
        }

        footer { visibility: hidden; }

        /* HEADER FIXO PRINCIPAL */
        .fixed-header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            background: white;
            z-index: 999999;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border-bottom: 1px solid rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            padding: 0;
            font-family: "Inter", "Source Sans Pro", sans-serif;
            color: #333;
            overflow: hidden;
        }

        /* LINHAS DO HEADER */
        .header-nav-row {
            display: flex;
            align-items: center;
            justify-content: flex-start;
            padding: 1rem 2rem;
            gap: 0.75rem;
            border-bottom: 1px solid rgba(0,0,0,0.06);
            flex-wrap: nowrap;
            background: white;
            min-height: 70px;
        }

        .header-info-row {
            display: flex;
            align-items: center;
            padding: 1rem 2rem;
            gap: 1.5rem;
            flex-wrap: wrap;
            background: linear-gradient(135deg, #f5f7fa 0%, #e9ecef 100%);
            min-height: 90px;
        }

        /* CONTAINER DOS BOTÕES STREAMLIT */
        #header-tabs-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            background: white;
            z-index: 999999;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border-bottom: 1px solid rgba(0,0,0,0.06);
            padding: 1rem 2rem;
            display: flex !important;
            gap: 0.75rem;
            align-items: center;
            min-height: 70px;
        }

        /* Estiliza os botões Streamlit dentro do container */
        #header-tabs-container button[data-testid="baseButton-secondary"] {
            color: #666 !important;
            font-weight: 500;
            padding: 0.6rem 1.2rem !important;
            border-radius: 8px !important;
            transition: all 0.25s ease;
            font-size: 13px !important;
            white-space: nowrap;
            border: 1px solid #e0e0e0 !important;
            background: white !important;
            cursor: pointer;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
            height: 40px !important;
            min-width: fit-content;
        }

        #header-tabs-container button[data-testid="baseButton-secondary"]:hover {
            color: #8e24aa !important;
            background: #f9f5ff !important;
            border-color: #dfc8e8 !important;
            box-shadow: 0 2px 6px rgba(142, 36, 170, 0.15) !important;
            transform: translateY(-1px);
        }

        /* Botão ativo (marcado quando está selecionado) */
        #header-tabs-container button[data-testid="baseButton-secondary"][kind="primary"],
        #header-tabs-container button[data-testid="baseButton-secondary"].active {
            background: linear-gradient(135deg, #8e24aa 0%, #ab47bc 100%) !important;
            color: white !important;
            font-weight: 700 !important;
            box-shadow: 0 4px 12px rgba(142, 36, 170, 0.35) !important;
            border-color: #8e24aa !important;
        }

        /* CARDS DE INFO */
        .info-container {
            display: flex;
            gap: 2rem;
            width: 100%;
            justify-content: flex-start;
            align-items: center;
            flex-wrap: nowrap;
            overflow-x: auto;
            padding-right: 1rem;
        }

        .info-container::-webkit-scrollbar {
            height: 4px;
        }

        .info-container::-webkit-scrollbar-track {
            background: transparent;
        }

        .info-container::-webkit-scrollbar-thumb {
            background: rgba(142, 36, 170, 0.2);
            border-radius: 2px;
        }

        .info-card {
            display: flex;
            flex-direction: column;
            justify-content: center;
            border-left: 4px solid #8e24aa;
            padding-left: 1rem;
            flex: 0 0 auto;
            min-width: 180px;
        }

        .info-card h5 {
            margin: 0;
            color: #999;
            font-size: 10px;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 0.5px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .info-card p {
            margin: 4px 0 0 0;
            color: #4a148c;
            font-weight: 700;
            font-size: 15px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            line-height: 1.2;
        }

        .info-card span {
            font-size: 12px;
            color: #999;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            margin-top: 2px;
        }

        /* EXPANDER HTML NO HEADER */
        .header-expander {
            margin-top: 0.5rem;
            padding: 0.75rem 1rem;
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .header-expander:hover {
            background: #f9f5ff;
            border-color: #dfc8e8;
            box-shadow: 0 2px 6px rgba(142, 36, 170, 0.15);
        }

        .header-expander summary {
            font-weight: 600;
            color: #8e24aa;
            font-size: 13px;
            outline: none;
            user-select: none;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .header-expander summary::-webkit-details-marker {
            color: #8e24aa;
        }

        .header-expander[open] summary {
            color: #6a1b9a;
            margin-bottom: 0.5rem;
        }

        .expander-content {
            font-size: 12px;
            color: #666;
            line-height: 1.5;
            border-top: 1px solid #e0e0e0;
            padding-top: 0.5rem;
        }

        .expander-content p {
            margin: 0.3rem 0;
            word-break: break-word;
        }

        .expander-content strong {
            color: #4a148c;
            font-weight: 700;
        }

        /* AJUSTES DE LAYOUT PRINCIPAL */
        .block-container {
            padding-top: 180px !important;
            margin-top: 0 !important;
        }

        section[data-testid="stSidebar"] {
            top: 0;
            z-index: 999998;
        }

        /* RESPONSIVIDADE */
        @media (max-width: 1200px) {
            #header-tabs-container {
                padding: 0.75rem 1.5rem;
                gap: 0.5rem;
                min-height: 65px;
            }

            #header-tabs-container button[data-testid="baseButton-secondary"] {
                padding: 0.5rem 1rem !important;
                font-size: 12px !important;
                height: 36px !important;
            }

            .header-info-row {
                padding: 0.75rem 1.5rem;
                gap: 1rem;
                min-height: 85px;
            }

            .info-card {
                min-width: 150px;
            }

            .info-container {
                gap: 1.5rem;
            }

            .block-container {
                padding-top: 160px !important;
            }
        }

        @media (max-width: 900px) {
            #header-tabs-container {
                padding: 0.75rem 1rem;
                gap: 0.3rem;
                min-height: 60px;
            }

            #header-tabs-container button[data-testid="baseButton-secondary"] {
                padding: 0.4rem 0.8rem !important;
                font-size: 11px !important;
                height: 34px !important;
            }

            .info-container {
                gap: 1rem;
            }

            .header-info-row {
                padding: 0.75rem 1rem;
                gap: 0.75rem;
                min-height: auto;
                display: flex;
                flex-wrap: wrap;
            }

            .info-card {
                min-width: 140px;
                border-left-width: 3px;
                padding-left: 0.75rem;
            }

            .block-container {
                padding-top: 150px !important;
            }
        }

        @media (max-width: 600px) {
            #header-tabs-container {
                padding: 0.5rem;
                gap: 0.2rem;
                min-height: 55px;
            }

            #header-tabs-container button[data-testid="baseButton-secondary"] {
                padding: 0.3rem 0.5rem !important;
                font-size: 10px !important;
                height: 32px !important;
            }

            .header-info-row {
                display: none;
            }

            .block-container {
                padding-top: 70px !important;
            }
        }
    </style>
    """

    # --- INJETAR CSS ---
    st.markdown(header_style, unsafe_allow_html=True)

    # --- CONSTRUIR INFO CARDS HTML ---
    def build_info_html():
        """Constrói os cards de informação dos filtros"""
        if 'data_inicial' not in st.session_state or 'df_geral_filtrado' not in st.session_state:
            return ""

        data_ini = st.session_state.data_inicial
        data_fim = st.session_state.data_final
        dias_totais = (data_fim - data_ini).days

        mesos_no_filtro = st.session_state.df_geral_filtrado['mesoregiao'].unique()
        mesos_reais = [m for m in mesos_no_filtro if m != 'Não informado']
        qtd_mesos = len(mesos_reais)

        if qtd_mesos >= 6:
            texto_meso = "Todo o Estado (SC)"
            detalhe_meso = None
        elif qtd_mesos <= 2:
            texto_meso = ", ".join(mesos_reais[:2])
            detalhe_meso = ", ".join(sorted(mesos_reais))
        else:
            texto_meso = f"{qtd_mesos} Mesorregiões"
            detalhe_meso = None

        muns_selecionados = st.session_state.df_geral_filtrado['municipio'].unique()
        qtd_mun = len(muns_selecionados)

        if qtd_mun >= 293:
            texto_mun = "Todos os 295 Municípios"
            mostrar_expander_mun = False
        elif qtd_mun == 1:
            texto_mun = muns_selecionados[0]
            mostrar_expander_mun = False
        else:
            texto_mun = f"{qtd_mun} Municípios"
            mostrar_expander_mun = qtd_mun > 3

        # Monta HTML do expander se necessário
        expander_html = ""
        if mostrar_expander_mun or detalhe_meso:
            lista_mun = ", ".join(sorted(muns_selecionados)) if mostrar_expander_mun else ""
            expander_html = f'<details class="header-expander"><summary>🔎 Ver localidades selecionadas</summary><div class="expander-content">{"<p><strong>Mesorregiões:</strong> " + detalhe_meso + "</p>" if detalhe_meso else ""}{"<p><strong>Municípios:</strong> " + lista_mun + "</p>" if mostrar_expander_mun else ""}</div></details>'

        info_html = f'<div class="header-info-row"><div class="info-container"><div class="info-card"><h5>📅 Período</h5><p>{data_ini.strftime("%d/%m/%Y")} - {data_fim.strftime("%d/%m/%Y")}</p><span>{dias_totais} dias</span></div><div class="info-card"><h5>🗺️ Abrangência</h5><p>{texto_meso}</p><span>Mesorregiões</span></div><div class="info-card"><h5>📍 Municípios</h5><p>{texto_mun}</p><span>Selecionados</span></div></div>{expander_html}</div>'
        return info_html

    # Renderiza os cards de info
    info_html = build_info_html()
    if info_html:
        st.markdown(f'<div style="position: fixed; top: 70px; left: 0; width: 100vw; z-index: 999998;">{info_html}</div>', unsafe_allow_html=True)


def render_tab_buttons():
    """
    Renderiza os botões de navegação das abas usando botões Streamlit nativos.
    Estes botões serão posicionados no header fixo via CSS.
    """

    # Callbacks para mudar de aba
    def mudar_aba(nome_aba):
        st.session_state.active_tab = nome_aba

    # Container com ID específico para o CSS posicionar
    st.markdown('<div id="header-tabs-container">', unsafe_allow_html=True)

    # Cria os botões em colunas
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        tipo = "primary" if st.session_state.get('active_tab') == "Análise Geral" else "secondary"
        st.button(
            "📊 Análise Geral",
            key="btn_analise_geral",
            on_click=mudar_aba,
            args=("Análise Geral",),
            type=tipo,
            use_container_width=True
        )

    with col2:
        tipo = "primary" if st.session_state.get('active_tab') == "Análise de Feminicídios" else "secondary"
        st.button(
            "🚨 Análise de Feminicídios",
            key="btn_feminicidios",
            on_click=mudar_aba,
            args=("Análise de Feminicídios",),
            type=tipo,
            use_container_width=True
        )

    with col3:
        tipo = "primary" if st.session_state.get('active_tab') == "Metodologia e Glossário" else "secondary"
        st.button(
            "📖 Metodologia e Glossário",
            key="btn_metodologia",
            on_click=mudar_aba,
            args=("Metodologia e Glossário",),
            type=tipo,
            use_container_width=True
        )

    with col4:
        tipo = "primary" if st.session_state.get('active_tab') == "Download de Dados" else "secondary"
        st.button(
            "📥 Download de Dados",
            key="btn_download",
            on_click=mudar_aba,
            args=("Download de Dados",),
            type=tipo,
            use_container_width=True
        )

    st.markdown('</div>', unsafe_allow_html=True)
