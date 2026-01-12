import streamlit as st

def render_custom_header():
    """
    Renderiza o cabeçalho fixo customizado com informações dos filtros.

    Layout:
    - Cards de resumo dos filtros ativos (Período, Abrangência, Municípios)
    - Expander para detalhes quando necessário
    """

    # --- CSS PROFISSIONAL PARA HEADER ---
    header_style = """
    <style>
        /* RESET & Compatibilidade Streamlit */
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

        /* CONTAINER DOS BOTÕES STREAMLIT NO TOPO */
        #header-tabs-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            background: linear-gradient(to right, #ffffff 0%, #fafafa 100%);
            z-index: 999999;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
            border-bottom: 1px solid #e8e8e8;
            padding: 0.875rem 2rem;
            display: flex !important;
            gap: 0.75rem;
            align-items: center;
            min-height: 68px;
        }

        /* Estilização dos botões Streamlit */
        #header-tabs-container button[data-testid="baseButton-secondary"],
        #header-tabs-container button[data-testid="baseButton-primary"] {
            font-weight: 500 !important;
            padding: 0.625rem 1.25rem !important;
            border-radius: 10px !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            font-size: 13.5px !important;
            white-space: nowrap;
            border: 1.5px solid #e5e5e5 !important;
            background: white !important;
            color: #555 !important;
            cursor: pointer;
            box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
            height: 42px !important;
            min-width: fit-content;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
        }

        #header-tabs-container button[data-testid="baseButton-secondary"]:hover {
            color: #8e24aa !important;
            background: linear-gradient(135deg, #faf5ff 0%, #f3e5f5 100%) !important;
            border-color: #ce93d8 !important;
            box-shadow: 0 3px 10px rgba(142, 36, 170, 0.2) !important;
            transform: translateY(-2px);
        }

        /* Botão ativo (primary) */
        #header-tabs-container button[data-testid="baseButton-primary"] {
            background: linear-gradient(135deg, #8e24aa 0%, #ab47bc 100%) !important;
            color: white !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 14px rgba(142, 36, 170, 0.4) !important;
            border-color: #8e24aa !important;
        }

        #header-tabs-container button[data-testid="baseButton-primary"]:hover {
            background: linear-gradient(135deg, #7b1fa2 0%, #9c27b0 100%) !important;
            box-shadow: 0 6px 20px rgba(142, 36, 170, 0.5) !important;
            transform: translateY(-2px);
        }

        /* HEADER DE INFORMAÇÕES (abaixo dos botões) */
        .info-header-container {
            position: fixed;
            top: 68px;
            left: 0;
            width: 100vw;
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 50%, #f5f7fa 100%);
            z-index: 999998;
            padding: 1.25rem 2rem 1.5rem 2rem;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
            border-bottom: 1px solid rgba(142, 36, 170, 0.12);
        }

        /* Container dos cards */
        .info-cards-wrapper {
            display: flex;
            gap: 1.75rem;
            align-items: stretch;
            flex-wrap: wrap;
            max-width: 1400px;
            margin: 0 auto;
        }

        /* Card individual */
        .info-card {
            display: flex;
            flex-direction: column;
            justify-content: center;
            background: white;
            padding: 1.125rem 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06), 0 1px 3px rgba(0, 0, 0, 0.03);
            border: 1px solid rgba(142, 36, 170, 0.08);
            border-left: 4px solid #8e24aa;
            flex: 1 1 220px;
            min-width: 200px;
            max-width: 320px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }

        .info-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(142, 36, 170, 0.02) 0%, transparent 100%);
            pointer-events: none;
        }

        .info-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(142, 36, 170, 0.15), 0 3px 8px rgba(0, 0, 0, 0.08);
            border-left-width: 5px;
        }

        /* Título do card */
        .info-card-title {
            margin: 0 0 0.5rem 0;
            color: #7a7a7a;
            font-size: 10.5px;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 1px;
            display: flex;
            align-items: center;
            gap: 0.375rem;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        /* Valor principal do card */
        .info-card-value {
            margin: 0;
            color: #4a148c;
            font-weight: 700;
            font-size: 17px;
            line-height: 1.3;
            margin-bottom: 0.25rem;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        /* Subtexto do card */
        .info-card-subtitle {
            font-size: 12px;
            color: #9e9e9e;
            margin: 0;
            font-weight: 500;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        /* EXPANDER ELEGANTE */
        .header-expander {
            margin-top: 1rem;
            padding: 0.875rem 1.25rem;
            background: white;
            border: 1px solid rgba(142, 36, 170, 0.15);
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
            max-width: 1400px;
            margin-left: auto;
            margin-right: auto;
        }

        .header-expander:hover {
            background: linear-gradient(135deg, #faf5ff 0%, #f3e5f5 100%);
            border-color: #ce93d8;
            box-shadow: 0 4px 12px rgba(142, 36, 170, 0.12);
            transform: translateY(-1px);
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
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        .header-expander summary::-webkit-details-marker {
            color: #8e24aa;
        }

        .header-expander[open] {
            box-shadow: 0 6px 16px rgba(142, 36, 170, 0.15);
        }

        .header-expander[open] summary {
            color: #7b1fa2;
            margin-bottom: 0.75rem;
            padding-bottom: 0.75rem;
            border-bottom: 1px solid rgba(142, 36, 170, 0.15);
        }

        .expander-content {
            font-size: 12.5px;
            color: #555;
            line-height: 1.6;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        .expander-content p {
            margin: 0.5rem 0;
            word-break: break-word;
        }

        .expander-content strong {
            color: #6a1b9a;
            font-weight: 700;
        }

        /* AJUSTES DE LAYOUT PRINCIPAL */
        .block-container {
            padding-top: 195px !important;
            margin-top: 0 !important;
        }

        section[data-testid="stSidebar"] {
            top: 0;
            z-index: 999997;
        }

        /* RESPONSIVIDADE PROFISSIONAL */
        @media (max-width: 1200px) {
            #header-tabs-container {
                padding: 0.75rem 1.5rem;
                gap: 0.6rem;
                min-height: 64px;
            }

            #header-tabs-container button {
                padding: 0.5rem 1rem !important;
                font-size: 12.5px !important;
                height: 38px !important;
            }

            .info-header-container {
                top: 64px;
                padding: 1rem 1.5rem 1.25rem 1.5rem;
            }

            .info-cards-wrapper {
                gap: 1.25rem;
            }

            .info-card {
                flex: 1 1 180px;
                min-width: 180px;
                padding: 1rem 1.25rem;
            }

            .block-container {
                padding-top: 180px !important;
            }
        }

        @media (max-width: 900px) {
            #header-tabs-container {
                padding: 0.625rem 1rem;
                gap: 0.4rem;
                min-height: 60px;
            }

            #header-tabs-container button {
                padding: 0.4rem 0.8rem !important;
                font-size: 11.5px !important;
                height: 36px !important;
            }

            .info-header-container {
                top: 60px;
                padding: 0.875rem 1rem 1rem 1rem;
            }

            .info-cards-wrapper {
                gap: 1rem;
            }

            .info-card {
                flex: 1 1 160px;
                min-width: 160px;
                padding: 0.875rem 1rem;
            }

            .info-card-value {
                font-size: 15px;
            }

            .block-container {
                padding-top: 165px !important;
            }
        }

        @media (max-width: 600px) {
            #header-tabs-container {
                padding: 0.5rem;
                gap: 0.25rem;
                min-height: 56px;
            }

            #header-tabs-container button {
                padding: 0.35rem 0.6rem !important;
                font-size: 10px !important;
                height: 32px !important;
            }

            .info-header-container {
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

    # --- CONSTRUIR HTML DAS INFORMAÇÕES ---
    def build_info_html():
        """Constrói os cards de informação dos filtros com design profissional"""
        if 'data_inicial' not in st.session_state or 'df_geral_filtrado' not in st.session_state:
            return ""

        data_ini = st.session_state.data_inicial
        data_fim = st.session_state.data_final
        dias_totais = (data_fim - data_ini).days

        # Análise das mesorregiões
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

        # Análise dos municípios
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

        # Construir cards
        cards_html = f"""
        <div class="info-cards-wrapper">
            <div class="info-card">
                <div class="info-card-title">📅 PERÍODO</div>
                <div class="info-card-value">{data_ini.strftime("%d/%m/%Y")} - {data_fim.strftime("%d/%m/%Y")}</div>
                <div class="info-card-subtitle">{dias_totais:,} dias selecionados</div>
            </div>

            <div class="info-card">
                <div class="info-card-title">🗺️ ABRANGÊNCIA</div>
                <div class="info-card-value">{texto_meso}</div>
                <div class="info-card-subtitle">Mesorregiões</div>
            </div>

            <div class="info-card">
                <div class="info-card-title">📍 MUNICÍPIOS</div>
                <div class="info-card-value">{texto_mun}</div>
                <div class="info-card-subtitle">Selecionados para análise</div>
            </div>
        </div>
        """

        # Adicionar expander se necessário
        expander_html = ""
        if mostrar_expander_mun or detalhe_meso:
            lista_mun = ", ".join(sorted(muns_selecionados)) if mostrar_expander_mun else ""

            detalhes_content = ""
            if detalhe_meso:
                detalhes_content += f"<p><strong>Mesorregiões:</strong> {detalhe_meso}</p>"
            if mostrar_expander_mun:
                detalhes_content += f"<p><strong>Municípios:</strong> {lista_mun}</p>"

            expander_html = f"""
            <details class="header-expander">
                <summary>🔎 Ver detalhes das localidades selecionadas</summary>
                <div class="expander-content">{detalhes_content}</div>
            </details>
            """

        # HTML completo
        full_html = f"""
        <div class="info-header-container">
            {cards_html}
            {expander_html}
        </div>
        """

        return full_html

    # Renderizar informações
    info_html = build_info_html()
    if info_html:
        st.markdown(info_html, unsafe_allow_html=True)


def render_tab_buttons():
    """
    Renderiza os botões de navegação das abas usando botões Streamlit nativos.
    Estes botões serão posicionados no header fixo via CSS.
    """

    # Callback para mudar de aba
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
