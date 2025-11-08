
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
    "Sen deneyimli bir astroloji uzmanısın. "
    "Doğum haritası bilgilerini (gezegen konumları, evler, açılar vb.) alır ve "
    "bunları insanın kişiliği, duyguları, ilişkileri ve kariyer yönüyle ilişkilendirerek açıklar. "
    "Sade ve doğal Türkçe ile konuş. "
    "Karmaşık astroloji terimlerini açıkla, HTML veya kod kullanma."
    "kullanıcı selam verdiğinde selam ver ve doğum haritanı benimle paylaşır mısın de"
    "kullanıcı haritasını paylaştıktan sonra cevabın en son kısmında aşk,iş yada ekonomik olarak hayatının nasıl olduğunu analiz edebilirim diye öneride bulun eğer analiz istersex  verilen haritaya göre yorum yap "

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

