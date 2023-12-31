from pathlib import Path
from typing import Optional
import typer
from gemini import generate_text, generate_multimodal_text, start_chat_session, continue_chat_session

app = typer.Typer()

@app.command()
def text_generation(prompt: str):
    """ Generates text from a prompt using the Gemini Pro model.
    Args:
        prompt (str): The prompt to generate text from.
    """
    styled_prompt = typer.style(f"Prompt: {prompt}\n", fg=typer.colors.GREEN)
    typer.echo(styled_prompt)
    
    styled_response = typer.style(f"Model: {generate_text(prompt)}", fg=typer.colors.BRIGHT_CYAN)
    typer.echo(styled_response)

@app.command()
def multimodal_generation(prompt: Optional[str] = None, image: Path = None):
    """ Generates text from a prompt and image using the Gemini Pro Vision model.
    Args:
        prompt (str): The prompt to generate text from.
        image (Path): The image to generate text from.
    """
    if prompt is not None:
        styled_prompt = typer.style(f"Prompt: {prompt}\n", fg=typer.colors.GREEN)
        typer.echo(styled_prompt)
    
    styled_response = typer.style(f"Model: {generate_multimodal_text(prompt, image)}", fg=typer.colors.BRIGHT_CYAN)
    typer.echo(styled_response)

@app.command()
def chatbot():
    """ Starts a chat session using the Gemini Pro model.
        Type EXIT to exit the chat session.
    """
    typer.echo("Starting chat session...\n")
    chat = start_chat_session()

    typer.echo("Type EXIT to exit the chat session.\n")

    while True:
        prompt_text = typer.style("You: ", fg=typer.colors.GREEN)
        prompt = typer.prompt(prompt_text)
        typer.echo("\n")

        if prompt == "EXIT":
            break
        styled_response = typer.style(f"Model: \n {continue_chat_session(chat, prompt)}", fg=typer.colors.BRIGHT_CYAN)
        typer.echo(styled_response)
        typer.echo("\n")

if __name__ == "__main__":
    app()