'''
Launches a Gradio interface for Google Gemini Pro.
'''
import gradio as gr
from gemini import (
    generate_text,
    generate_multimodal_text,
    start_chat_session,
    continue_chat_session,
)

with gr.Blocks() as demo:
    gr.Markdown("""# Gradio Interface for Google Gemini Pro""")

    # Text Generation
    with gr.Tab(label="Text Generation"):
        gr.Interface(generate_text, inputs="text", outputs="text")

    # Multimodal Generation
    with gr.Tab(label="Multimodal Generation"):
        gr.Interface(
            generate_multimodal_text,
            inputs=["text", gr.Image(type="filepath")],
            outputs="text",
        )

    # Chatbot
    with gr.Tab(label="Chatbot"):
        chat = start_chat_session()

        chatbot = gr.Chatbot()
        message = gr.Textbox()
        clear = gr.ClearButton([message, chatbot])

        def respond(message, chat_history):
            user_message = message
            bot_message = continue_chat_session(chat, user_message)
            chat_history.append((user_message, bot_message))
            return "", chat_history

        message.submit(respond, [message, chatbot], [message, chatbot])


demo.launch()
