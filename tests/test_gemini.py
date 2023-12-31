""" Unit tests for gemini.py """
from pathlib import Path
import pytest

from src.gemini import (
    generate_text,
    generate_multimodal_text,
    start_chat_session,
    continue_chat_session,
)


# generate_text() Unit
def test_generate_text(prompt="Hello World"):
    """Test generate_text() function"""
    assert len(generate_text(prompt)) > 0


# generate_multimodal_text() Unit
def test_generate_multimodal_text_case_1(
    prompt="None", image=Path("src/AdobeStock_213269596.jpeg")
):
    """Test generate_multimodal_text() function - Case 1:
    Passing only an image
    """
    assert len(generate_multimodal_text(prompt, image)) > 0


def test_generate_multimodal_text_case_2(prompt="Hello World", image=None):
    """Test generate_multimodal_text() function - Case 2:
    Passing only text
    """
    with pytest.raises(ValueError):
        generate_multimodal_text(prompt, image)


def test_generate_multimodal_text_case_3(
    prompt="Explain this image", image=Path("src/AdobeStock_213269596.jpeg")
):
    """Test generate_multimodal_text() function - Case 3:
    Passing both text and image
    """
    assert len(generate_multimodal_text(prompt, image)) > 0


# chat_session() Unit
def test_start_chat_session():
    """Test start_chat_session() functions"""
    chat = start_chat_session()
    assert len(continue_chat_session(chat, "Hello, how are you?")) > 0
    assert len(continue_chat_session(chat, "What is your name?")) > 0
    assert len(chat.history) == 4
