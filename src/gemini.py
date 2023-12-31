""" Module for Gemini API calls."""

from pathlib import Path
from typing import Optional
import yaml
import google.generativeai as genai
import PIL.Image

# Load the configuration file
with open(Path("src/config.yaml"), encoding="utf-8") as file:
    config = yaml.safe_load(file.read())

# Setup Gemini API Credentials
genai.configure(api_key=config.get("VERTEX_API_KEY"))


# Gemini Pro Text Generation
def generate_text(prompt: str):
    """Generates text from a prompt using the Gemini Pro model.
    Args:
        prompt (str): The prompt to generate text from.
    Returns:
        str: The generated text.
    """
    model = genai.GenerativeModel("gemini-pro")

    response = model.generate_content(prompt)
    return response.text


# Gemini Pro Vision Multimodal Generation
def generate_multimodal_text(prompt: Optional[str] = None, image: Path = None):
    """Generates text from a prompt and image using the Gemini Pro Vision model.
    Args:
        prompt (str): The prompt to generate text from.
        image (Path): The image to generate text from.
    Returns:
        str: The generated text.
    """
    model = genai.GenerativeModel("gemini-pro-vision")

    if image is not None:
        img = PIL.Image.open(image)

    if prompt is None and image is not None:  # Case 1: Passing only an image
        response = model.generate_content(img)
    elif prompt is not None and image is None:  # Case 2: Passing only text
        raise ValueError("Please provide an image or choose a different model.")
    else:  # Case 3: Passing both text and image
        response = model.generate_content([prompt, img])
        response.resolve()
    return response.text


# Gemini Pro Chat
def start_chat_session():
    """Starts a chat session using the Gemini Pro model.
    Returns:
        chat (Chat): The chat session.
    """
    model = genai.GenerativeModel("gemini-pro")
    return model.start_chat(history=[])


def continue_chat_session(chat, prompt):
    """Continues a chat session using the Gemini Pro model.
    Args:
        chat (Chat): The instantiated chat session.
        prompt (str): The prompt to generate text from.
    Returns:
        str: The generated text.
    """
    response = chat.send_message(prompt)
    return response.text


def review_chat_history(chat):
    """Reviews the chat history of a chat session.
    Args:
        chat (Chat): The instantiated chat session.
    """
    for message in chat.history:
        print(f"{message.role}: {message.parts[0].text}\n")
