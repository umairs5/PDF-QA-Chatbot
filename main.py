# main.py

import gradio as gr
from utils import setup_astra_vectorstore, process_pdf, get_llm

# Global objects
llm = get_llm()
vectorstore = None  # will be assigned after PDF upload


def upload_pdf(pdf_path):
    global vectorstore
    chunks = process_pdf(pdf_path)

    # Reset and set up new vector store
    vectorstore = setup_astra_vectorstore(reset=True)
    vectorstore.add_texts(chunks)

    return "✅ PDF uploaded and processed. You can now ask questions."


def ask_question(query):
    global vectorstore
    if not vectorstore:
        return "❌ Please upload a PDF first."

    result = vectorstore.similarity_search_with_score(query, k=3)
    docs = [doc.page_content for doc, _ in result]

    context = "\n".join(docs)
    full_prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"

    response = llm.invoke(full_prompt)
    return response.content


# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 📄 PDF QA Chatbot with Groq & Astra DB")
    pdf_input = gr.File(label="Upload your PDF", type="filepath", file_types=[".pdf"])
    upload_button = gr.Button("Upload and Process")
    status = gr.Textbox(label="Status", interactive=False)

    with gr.Row():
        query_input = gr.Textbox(label="Ask a Question")
        ask_button = gr.Button("Ask")

    answer_output = gr.Textbox(label="Answer")

    upload_button.click(upload_pdf, inputs=pdf_input, outputs=status)
    ask_button.click(ask_question, inputs=query_input, outputs=answer_output)

# Launch app
if __name__ == "__main__":
    demo.launch()
