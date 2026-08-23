import streamlit as st
import requests

# Configurare interfață site
st.set_page_config(page_title="Generator Reclame AIDA", page_icon="✍️", layout="centered")

st.title("✍️ Generator de Reclame Facebook (Formula AIDA)")
st.write("Introdu numele produsului tău și AI-ul va genera o reclamă optimizată pentru vânzări.")


GEMINI_API_KEY = "AQ.Ab8RN6KVXXXBWGZcEeY52Hv7YYPC63YwlrSlC2ZbWrUWy9C8eA"






with st.sidebar:
    st.header("🔑 Configurare")
    st.success("Sistemul AI este conectat și activat automat!")
    st.markdown("---")
    st.caption("Conexiune Directă Automatizată & Streamlit")

# Căsuțele de input
produs = st.text_input("Numele produsului sau serviciului tău:", placeholder="Ex: Curs de programare pentru începători")
detalii = st.text_area("Scurtă descriere / Beneficii cheie:", placeholder="Ex: Înveți Python de la zero în 4 săptămâni, mentorat inclus, 100% online.")

# Butonul care pornește generarea
if st.button("Generează Reclama 🚀"):
    if not produs:
        st.warning("Te rog să introduci numele produsului!")
    else:
        with st.spinner("AI-ul scrie reclama acum..."):
            url = f"https://googleapis.com{api_key}"
            
            prompt = f"""
            Acționează ca un copywriter de top, expert în reclame de Facebook Conversion.
            Scrie o reclamă extrem de convingătoare pentru următorul produs: "{produs}".
            Detalii produs: "{detalii}".
            
            Folosește structura psihologică AIDA și marchează clar fiecare secțiune în text:
            - **Attention (Atenție):** Un cârlig (hook) puternic care oprește scroll-ul.
            - **Interest (Interes):** Prezintă problema și de ce acest produs este soluția.
            - **Desire (Dorință):** Scoate în evidență beneficiile majore și transformarea oferită.
            - **Action (Acțiune):** Un îndemn la acțiune (CTA) clar și direct.
            
            Adaugă emoji-uri potrivite și folosește un ton persuasiv, dar natural.
            """
            
            headers = {'Content-Type': 'application/json'}
            data = {"contents": [{"parts": [{"text": prompt}]}]}
            
            try:
                response = requests.post(url, headers=headers, json=data)
                res_json = response.json()
                
                text_generat = res_json['candidates']['content']['parts']['text']
                st.success("Reclama ta este gata!")
                st.markdown("### 📋 Textul generat pentru reclama ta:")
                st.write(text_generat)
                
            except Exception as e:
                st.error("A apărut o problemă pe serverul central Google. Te rugăm să apeși din nou pe buton!")
