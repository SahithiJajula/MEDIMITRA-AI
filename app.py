import streamlit as st

st.set_page_config(
    page_title="MediMitra AI", page_icon="🏥", layout="centered"
)

# Initialize language state
if "language" not in st.session_state:
    st.session_state.language = None

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Localization dictionary for UI texts
ui_texts = {
    "English": {
        "title": "🏥 MediMitra AI",
        "caption": "Regional Language Voice & Text Healthcare Triage | GNITS",
        "selected_lang": "Selected Language:",
        "change_btn": "Change Language",
        "whatsapp_header": "📲 Connect via WhatsApp",
        "whatsapp_link": "👉 [Click here to open WhatsApp Chat](https://wa.me/919876543210?text=Namaste%20MediMitra%20AI)",
        "prompt": "Describe your symptoms (e.g., severe fever)...",
        "triage": "🚨 **Triage Level: Moderate Risk**\n\n**Advice:** Stay hydrated, take rest, and monitor body temperature.\n\n📍 **Nearby Doctors & Health Centers:**\n1. Dr. Sharma Clinic - 1.2 km away\n2. Primary Health Center - 2.5 km away",
    },
    "Hindi": {
        "title": "🏥 मेडिमित्र AI",
        "caption": "क्षेत्रीय भाषा आवाज और पाठ स्वास्थ्य ट्राइएज | जीएनआईटीएस",
        "selected_lang": "चयनित भाषा:",
        "change_btn": "भाषा बदलें",
        "whatsapp_header": "📲 व्हाट्सएप के माध्यम से जुड़ें",
        "whatsapp_link": "👉 [व्हाट्सएप चैट खोलने के लिए यहाँ क्लिक करें](https://wa.me/919876543210?text=Namaste%20MediMitra%20AI)",
        "prompt": "अपने लक्षणों का वर्णन करें (उदा. तेज़ बुखार)...",
        "triage": "🚨 **ट्राइएज स्तर: मध्यम जोखिम**\n\n**सलाह:** पर्याप्त पानी पिएं, आराम करें और शरीर के तापमान की निगरानी करें।\n\n📍 **निकटतम डॉक्टर और स्वास्थ्य केंद्र:**\n1. डॉ. शर्मा क्लिनिक - 1.2 किमी दूर\n2. प्राथमिक स्वास्थ्य केंद्र - 2.5 किमी दूर",
    },
    "Telugu": {
        "title": "🏥 మెడిమిత్ర AI",
        "caption": "ప్రాంతీయ భాష వాయిస్ & టెక్స్ట్ హెల్త్‌కేర్ ట్రయేజ్ | GNITS",
        "selected_lang": "ఎంచుకున్న భాష:",
        "change_btn": "భాషను మార్చండి",
        "whatsapp_header": "📲 వాట్సాప్ ద్వారా కనెక్ట్ అవ్వండి",
        "whatsapp_link": "👉 [వాట్సాప్ చాట్ తెరవడానికి ఇక్కడ క్లిక్ చేయండి](https://wa.me/919876543210?text=Namaste%20MediMitra%20AI)",
        "prompt": "మీ ఆరోగ్య లక్షణాలను తెలియజేయండి (ఉదా. తీవ్రమైన జ్వరం)...",
        "triage": "🚨 **ట్రయేజ్ స్థాయి: మధ్యస్థ ప్రమాదం**\n\n**సలహా:** తగినంత నీరు తాగి, విశ్రాంతి తీసుకోండి మరియు శరీర ఉష్ణోగ్రతను పర్యవేక్షించండి.\n\n📍 **సమీపంలోని వైద్యులు & ఆరోగ్య కేంద్రాలు:**\n1. డాక్టర్ శర్మ క్లినిక్ - 1.2 కి.మీ దూరంలో\n2. ప్రాథమిక ఆరోగ్య కేంద్రం - 2.5 కి.మీ దూరంలో",
    },
}

# Step 1: Language Selection Prompt if not chosen yet
if st.session_state.language is None:
    st.title("🏥 MediMitra AI")
    st.caption("Regional Language Voice & Text Healthcare Triage | GNITS")
    
    st.info("🙏 **Namaste! Welcome to MediMitra AI.**")
    st.subheader(
        "Please select your preferred language to continue / कृपया अपनी भाषा चुनें / దయచేసి మీ భాషను ఎంచుకోండి:"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("English 🇬🇧", use_container_width=True):
            st.session_state.language = "English"
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": "Namaste! I am MediMitra AI. Please describe your health symptoms or concerns.",
                }
            )
            st.rerun()

    with col2:
        if st.button("हिंदी 🇮🇳", use_container_width=True):
            st.session_state.language = "Hindi"
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": "नमस्ते! मैं मेडिमित्र AI हूँ। कृपया अपने स्वास्थ्य लक्षणों या समस्याओं के बारे में बताएं।",
                }
            )
            st.rerun()

    with col3:
        if st.button("తెలుగు 🇮🇳", use_container_width=True):
            st.session_state.language = "Telugu"
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": "నమస్కారం! నేను మెడిమిత్ర AI. దయచేసి మీ ఆరోగ్య సమస్యలు లేదా లక్షణాలను తెలియజేయండి.",
                }
            )
            st.rerun()

# Step 2: Main Chat Interface after language selection
else:
    current_lang = st.session_state.language
    text = ui_texts[current_lang]

    # Render translated header elements
    st.title(text["title"])
    st.caption(text["caption"])

    # Top status bar showing selected language with localized reset option
    col_lang, col_reset = st.columns([3, 1])
    with col_lang:
        st.write(f"🌐 **{text['selected_lang']}** {current_lang}")
    with col_reset:
        if st.button(text["change_btn"], type="secondary"):
            st.session_state.language = None
            st.session_state.messages = []
            st.rerun()

    st.divider()

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input box with translated placeholder
    if user_input := st.chat_input(text["prompt"]):
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Display localized assistant reply
        bot_reply = text["triage"]
        with st.chat_message("assistant"):
            st.markdown(bot_reply)
        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply}
        )

    st.divider()
    st.markdown(f"### {text['whatsapp_header']}")
    st.markdown(text["whatsapp_link"])
