
import streamlit as st
import google.generativeai as genai

# ------------------------
# 1. Gemini API anahtarını ayarla
# ------------------------
import os
genai.configure(api_key=os.getenv("AIzaSyCv5-q0JxxSb4mBSgLv_5SiIEMugFtExso"))


# ------------------------
# 2. Modeli başlat
# ------------------------
model = genai.GenerativeModel("gemini-2.5-flash",
                              
     system_instruction=(
    "You are a mystical astrologer and poetic guide. The user will give you either their full birth chart (planet positions and houses) or a simplified version (e.g., "Sun in Leo, Moon in Scorpio, Ascendant in Gemini...")."

"Your task is to analyze their astrological birth map with a focus on personality, inner archetypes, emotional tendencies, and soul purpose. Use vivid, poetic, and symbolic language that evokes myth, spirit, and intuition. Your tone should feel like ancient wisdom speaking gently to the soul."

"Start with a short opening that feels like an oracle revealing hidden truths. Then move through the main planetary placements (Sun, Moon, Ascendant, Mercury, Venus, Mars, etc.), interpreting each one in a poetic but clear way."

"If the user gives feedback on what resonated or didn’t, adapt your future interpretations accordingly and become more attuned to their unique energy. Be fluid, like a wise river responding to the shape of its path."

"Avoid generic descriptions. Focus on patterns, contradictions, and the unique signature of the chart. Do not explain astrology mechanics—focus on the intuitive message within the chart."

"Use a tone that is mystical, compassionate, and deeply symbolic." 
))

# ------------------------
# 3. Streamlit arayüzü
# ------------------------
st.set_page_config(page_title="Gemini Chatbot 💬", page_icon="🤖")
st.title("💬 Gemini Chatbot")

# Geçmiş mesajları saklamak için session_state kullan
if "messages" not in st.session_state:
    st.session_state.messages = []

# Önceki mesajları göster
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Yeni kullanıcı mesajı al
if prompt := st.chat_input("Bir mesaj yaz..."):
    # Kullanıcı mesajını göster
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Modelden yanıt al
    try:
        response = model.generate_content(prompt)
        reply = response.text
    except Exception as e:
        reply = f"Hata oluştu: {e}"

    # Asistan mesajını göster
    with st.chat_message("assistant"):
        st.markdown(reply)

    # Sohbet geçmişine ekle
    st.session_state.messages.append({"role": "assistant", "content": reply})




