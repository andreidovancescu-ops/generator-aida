import streamlit as st
import google.generativeai as genai

# Configurare interfață site
st.set_page_config(page_title="Generator Reclame AIDA", page_icon="✍️", layout="centered")

st.title("✍️ Generator de Reclame Facebook (Formula AIDA)")
st.write("Introdu numele produsului tău și AI-ul va genera o reclamă optimizată pentru vânzări.")

# Secțiune pentru introducerea cheii API în mod securizat
with st.sidebar:
    st.header("🔑 Configurare")
    api_key = st.text_input("Introdu Cheia API Gemini:", type="password", help="Poți obține o cheie gratuită din Google AI Studio")
    st.markdown("---")
    st.caption("Creat cu Google Gemini 3.7 Flash & Streamlit")

# Căsuța unde utilizatorul introduce produsul
produs = st.text_input("Numele produsului sau serviciului tău:", placeholder="Ex: Curs de programare pentru începători")
detalii = st.text_area("Scurtă descriere / Beneficii cheie:", placeholder="Ex: Înveți Python de la zero în 4 săptămâni, mentorat inclus, 100% online.")

# Butonul care pornește generarea
if st.button("Generează Reclama 🚀"):
    if not api_key:
        st.error("Te rog să introduci cheia API Gemini în meniul din stânga (Sidebar) pentru a putea genera textul!")
    elif not produs:
        st.warning("Te rog să introduci numele produsului!")
    else:
        with st.spinner("AI-ul scrie reclama acum..."):
            try:
                # Conectare la API-ul Google Gemini
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("gemini-2.5-flash") # Folosește modelul stabil de rulare
                
                # Promptul intern de copywriting
                prompt = f"""
                Acționează ca un copywriter de top, expert în reclame de Facebook Conversion.
                Scrie o reclamă extrem de convingătoare pentru următorul produs: "{produs}".
                Detalii produs: "{detalii}".
                
                Folosește structura psihologică AIDA și marchează clar fiecare secțiune în text:
                - **Attention (Atenție):** Un cârlig (hook) puternic care oprește scroll-ul.
                - **Interest (Interes):** Prezintă problema și de ce acest produs este soluția.
                - **Desire (Dorință):** Scoate în evidență beneficiile majore și transformarea oferită.
                - **Action (Acțiune):** Un îndemn la acțiune (CTA) clar și direct (ex: Apasă pe link).
                
                Adaugă emoji-uri potrivite pentru lizibilitate și folosește un ton persuasiv, dar natural (nu robotizat).
                """
                
                # Generare răspuns
                response = model.generate_content(prompt)
                
                # Afișare rezultat pe site
                st.success("Reclama ta este gata!")
                st.markdown("### 📋 Textul generat pentru reclama ta:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"A apărut o eroare la conectarea cu AI-ul: {e}")

