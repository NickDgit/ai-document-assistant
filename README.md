# 🤖 AI Smart Assistant (RAG Lite)

A lightweight, high-performance Document Intelligence tool built with **Streamlit** and **Groq Cloud**. This application allows users to summarize complex PDF documents and "chat" with their data in real-time.

🚀 **Features**
- **Instant Summarization:** Powered by **Llama 3.1 8B** via Groq API for lightning-fast Greek & English summaries.
- **Document Q&A:** Interactive Chat interface to ask specific questions about your uploaded PDFs.
- **Smart UI:** Adjustable detail levels (Short, Normal, Detailed) and a professional sidebar layout.
- **PDF & Text Support:** Handles both file uploads and direct text input.
- **Export Ready:** Download your summaries as `.txt` files with one click.

🛠️ **Tech Stack**
- **Framework:** Streamlit (Frontend & State Management)
- **LLM:** Llama 3.1 8B (Groq)
- **Orchestration:** LangChain
- **PDF Engine:** PyPDF2
- **Environment:** Python 3.12+

⚙️ **Setup**

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/ai-summarizer.git](https://github.com/your-username/ai-summarizer.git)
   cd ai-summarizer
   ```
2.  **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure Environment:**
Create a .env file in the root directory and add your Groq API Key:
   ```bash
   GROQ_API_KEY=your_key_here
   ```
4**Run the Application:**
   ```bash
   streamlit run main.py
   ```   
