import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION (Iwe juu kabisa)
# ==========================================
st.set_page_config(
    page_title="Subalo High School",
    page_icon="🎓",
    layout="centered",  # Hugawa content katikati
    initial_sidebar_state="collapsed",  # Huficha sidebar kwenye simu
)

# ==========================================
# 2. MOBILE-FIRST CSS CUSTOM STYLING
# ==========================================
st.markdown(
    """
    <style>
    /* Kupunguza nafasi na kuweka muonekano wa simu (Mobile View) */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 480px; /* Inafanya app ionekane kama ya simu hata kwenye PC */
        margin: auto;
    }
    
    /* Kufanya vitufe viwe vikubwa na vyepesi kubonyeza kwa kidole */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
        background-color: #2e7d32;
        color: white;
    }

    /* Kuficha header, footer na menu zisizo za lazima */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Kuboresha muonekano wa Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        border-radius: 8px 8px 0px 0px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# 3. NAVIGATION (Bottom/Top Tabs for Mobile)
# ==========================================
tab_login, tab_register, tab_info = st.tabs(
    ["🔑 Login", "📝 Usajili", "ℹ️ Taarifa"]
)

# ------------------------------------------
# TAB 1: LOGIN / INGIA
# ------------------------------------------
with tab_login:
    with st.container(border=True):
        st.markdown(
            "<h2 style='text-align: center;'>STUDENTS REGISTRATION SYSTEM</h2>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h4 style='text-align: center; color: #555;'>SUBALO HIGH SCHOOL</h4>",
            unsafe_allow_html=True,
        )

        st.write("")  # Nafasi

        username = st.text_input("Jina la Mtumiaji (Username)")
        password = st.text_input("Nenosiri (Password)", type="password")

        st.write("")

        if st.button("INGIA (LOGIN)"):
            if username and password:
                st.success(f"Karibu, {username}!")
            else:
                st.error("Tafadhali ingiza username na password.")

# ------------------------------------------
# TAB 2: FOMU YA USAJILI
# ------------------------------------------
with tab_register:
    with st.container(border=True):
        st.subheader("Usajili wa Mwanafunzi Mpya")

        full_name = st.text_input("Jina Kamili la Mwanafunzi")
        gender = st.selectbox("Jinsi", ["Chagua...", "Mwanaume", "Mwanamke"])
        combination = st.selectbox(
            "Tahasusi (Combination)",
            ["Chagua...", "PCM", "PCB", "CBG", "HGL", "HGK", "EGM"],
        )
        parent_phone = st.text_input("Namba ya Simu ya Mzazi/Mlezi")

        st.write("")

        if st.button("HIFADHI TAARIFA"):
            if full_name and gender != "Chagua...":
                st.success(
                    f"Taarifa za mwanafunzi {full_name} zimehifadhiwa kikamilifu!"
                )
            else:
                st.warning("Tafadhali jaza taarifa zote zinazohitajika.")

# ------------------------------------------
# TAB 3: TAARIFA NA MSAADA
# ------------------------------------------
with tab_info:
    with st.container(border=True):
        st.subheader("Msaada & Mawasiliano")
        st.write("Mfumo wa Usajili - Subalo High School")
        st.info("Kama unakumbana na changamoto yoyote, wasiliana na Admin.")