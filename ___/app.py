"""LLM Crash Course"""
import chainlit as cl
from typing import List
from classes import Model


def get_prompt(instruction: str, history: List[str] = []) -> str:
    system = "You are the best code assistant, with a deep understanding of programming languages as well as OOP and design patterns, Always answer as helpfully as possible. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."
    prompt = f"### System:\n{system}\n\n### User:\n"
    if Model().model == 'llama2':
        prompt = f"[INST] <<SYS>>\n{system}\n<</SYS>>\n"

    if len(history) > 0:
        prompt += f"Here's our conversation history:\n{''.join(history)}\n"

    if Model().model == 'llama2':
        prompt += f"{instruction}[/INST]"
    else:
        prompt += f"{instruction}\n\n### Response:\n"
    return prompt


@cl.on_message
async def on_message(message: cl.Message):
    in_message = message.content
    if in_message == 'forget everything':
        cl.user_session.set('message_history', [])
        await cl.Message("Uh oh, I've just forgotten our conversation history").send()
        return

    # 'use MODEL' command.
    models = tuple(Model().options.keys())
    if in_message.endswith(models) and len(message.content) <= 10:
        Model().set_llm(in_message.split('use ')[1])
        await cl.Message(in_message.split('use ')[1]).send()
        return

    # Show Conversation History command.
    if in_message == 'show history':
        await cl.Message(''.join(cl.user_session.get('message_history'))).send()
        return

    llm = Model().get_llm()
    message_history = cl.user_session.get('message_history')
    msg = cl.Message(content='')
    await msg.send()

    prompt = get_prompt(message.content, message_history)
    response = ''
    for word in llm(prompt, stream=True):
        await msg.stream_token(word)
        response += word
    await msg.update()
    message_history.append(response)


@cl.on_chat_start
def on_chat_start():
    cl.user_session.set('message_history', [])
    Model()
