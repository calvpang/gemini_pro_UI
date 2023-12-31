# Gemini Pro Interface

This repository contains code that will allow you to interact with Gemini Pro via Command Line Interface or Gradio.

## Pre-requisites
To begin, generate an Google Vertex AI API Key via [Google Maker Suite](https://makersuite.google.com/app/apikey) and store it in `src/config.yaml` as follows.

```
VERTEX_API_KEY: "INSERT KEY HERE"
```

## Environment Setup
Simply install [miniforge](https://github.com/conda-forge/miniforge), navigate to this repository and run the following command in Terminal.
```
conda env create -f environment.yml
```

## Usage
### CLI
Typer has be used to develop the CLI. You can view the help documentation as follows.
```
python src/main.py --help
```

### Gradio
To start the Gradio interface, simply run the following.
```
python src/webui.py
```