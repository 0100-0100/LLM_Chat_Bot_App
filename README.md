# LLM_Chat_Bot_App
This repository is the final project for the Udemy Course: The Local LLM Crash Course - Build an AI Chatbot in 2 hours!

On this course we understood a minimal python stack for creating a chatbot with the use of hugging face's text models and chainlit a Python framework for the web application front-end for conversation interactions with an LLM similar to OpenAI's UI for ChatGPT locally.

## Screenshot of the application's UI running locally.
![UI_Screenshot](https://github.com/0100-0100/LLM_Chat_Bot_App/blob/main/static/img/Example.PNG "UI Screenshot")

## Basic Actions.
You can write on the message input on of the following commands
### Model Selection
| Chat Command | Description                                                                                                                                            |
| :----------: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| use orca     | Use the model [zoltanctoth/orca_mini_3B-GGUF](https://huggingface.co/zoltanctoth/orca_mini_3B-GGUF "Hugging Face Orca 3B Model.")                      |
| use llama2   | Use the model [TheBloke/Llama-2-7B-Chat-GGUF](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF "Hugging Face Llama 2 7B.")                         |
| ~use llama3~ | Use the model [SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF "Hugging Face Llama 2 7B.") |
By default on first run the program will attempt the download of the model Orca Mini 3B GGUF if it is not already on cache and use the cached version on sub sequent runs.
Executing any of the commands above on the chat will change the LLM used for the current session.

Use *llama3* will attempt to use the SanctumAI Llama 3.1 8B model but in all the testing I did I was unable to run this project with the use of this las model.
**I tried my best to use Llama 3.1 but was unable to make it run with ctransformers on my local compputer :c**
---
### Extra Actions
| Chat Command      | Description                             |
| :---------------: | --------------------------------------- |
| forget everything | Reset the current session's chat memory |
| show history      | Show the current session's chat memory  |

## Installation:
### Install by running the ./install script or running the following commands:
```bash
python3 -m venv .venv
if [ $? -ne 0 ]; then
    echo 'Error while creating virtual environment with python3 -m venv .venv'
    exit
fi
source .venv/bin/activate
pip3 install -r requirements.txt
```

## Executing project:
### Run the project locally by running the ./run.sh script or running the command:
```bash
chainlit run ___/app.py -w
```

Many improvements can be added to the whole project but is intended to be a base for new projects that need to have chatbot like interactions with the user.
