import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from PyPDF2 import PdfReader

# Φόρτωση ρυθμίσεων
load_dotenv()

# Ρύθμιση Σελίδας
st.set_page_config(page_title="AI Smart Summarizer", page_icon="🤖", layout="wide")

# --- SIDEBAR (Όπως στην εικόνα σου) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2811/2811194.png", width=100)
    st.title("Ρυθμίσεις")
    option = st.radio("Επίλεξε πηγή:", ("PDF Αρχείο", "Κείμενο (Copy-Paste)"))

    st.divider()
    summary_type = st.select_slider(
        "Λεπτομέρεια Περίληψης:",
        options=["Σύντομη", "Κανονική", "Αναλυτική"]
    )
    st.info("Χρησιμοποιεί το μοντέλο Llama 3.1 μέσω Groq API.")

# --- ΚΥΡΙΟ ΜΕΡΟΣ ---
st.title("🤖 AI Smart Assistant")
st.markdown(f"### Ανάλυση από: **{option}**")

# Ρύθμιση του AI
llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0)


def ai_call(text, system_prompt, user_input):
    """Γενική συνάρτηση για κλήση στο AI"""
    limited_text = text[:15000]
    prompt = ChatPromptTemplate.from_template(system_prompt)
    chain = prompt | llm
    return chain.invoke({"context": limited_text, "question": user_input}).content


# --- ΕΞΑΓΩΓΗ ΚΕΙΜΕΝΟΥ ---
document_text = ""

if option == "PDF Αρχείο":
    uploaded_file = st.file_uploader("Ανέβασε το PDF σου", type="pdf")
    if uploaded_file:
        pdf_reader = PdfReader(uploaded_file)
        document_text = " ".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        st.success("Το έγγραφο φορτώθηκε!")

elif option == "Κείμενο (Copy-Paste)":
    document_text = st.text_area("Επικόλλησε το κείμενο εδώ:", height=200)

# --- ΛΕΙΤΟΥΡΓΙΕΣ (Μόνο αν υπάρχει κείμενο) ---
if document_text:
    col1, col2 = st.columns([1, 1])  # Χωρισμός σε δύο στήλες για Περίληψη και Chat

    with col1:
        st.subheader("📝 Περίληψη")
        if st.button("🚀 Δημιουργία Περίληψης"):
            with st.spinner("Αναλύω..."):
                sys_p = f"Κάνε μια {summary_type} περίληψη στα Ελληνικά με bullet points για το παρακάτω κείμενο:\n\n{{context}}"
                summary = ai_call(document_text, sys_p, "")
                st.markdown(summary)
                st.download_button("📥 Λήψη Περίληψης", summary, file_name="summary.txt")

    with col2:
        st.subheader("💬 Chat με το Έγγραφο")
        user_question = st.text_input("Κάνε μια ερώτηση:")
        if user_question:
            with st.spinner("Σκέφτομαι..."):
                sys_p = """
                Χρησιμοποίησε το κείμενο για να απαντήσεις στην ερώτηση. 
                Απάντησε μόνο βάσει του κειμένου.
                Context: {context}
                Ερώτηση: {question}
                """
                answer = ai_call(document_text, sys_p, user_question)
                st.info(answer)

else:
    st.info("Παρακαλώ ανέβασε ένα αρχείο ή βάλε κείμενο για να ξεκινήσεις.")