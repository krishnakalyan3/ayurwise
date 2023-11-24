#!/usr/bin/env python

import chainlit as cl
import os

DATABASE_PATH = os.environ.get("DATABASE_PATH")
print(DATABASE_PATH)

@cl.password_auth_callback
def auth_callback(username: str, password: str):
  # Fetch the user matching username from your database
  # and compare the hashed password with the value stored in the database
  if (username, password) == ("admin", "admin"):
    return cl.AppUser(username="admin", role="ADMIN", provider="credentials")
  else:
    return None

@cl.set_chat_profiles
async def chat_profile():
    return [
        cl.ChatProfile(
            name="Ayurveda",
            markdown_description="The underlying LLM model is **GPT-3.5**.",
            icon="https://picsum.photos/200",
        ),
        cl.ChatProfile(
            name="Yoga",
            markdown_description="The underlying LLM model is **GPT-4**.",
            icon="https://picsum.photos/250",
        )
    ]

@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: cl.Message):
    """
    This function is called every time a user inputs a message in the UI.
    It sends back an intermediate response from Tool 1, followed by the final answer.

    Args:
        message: The user's message.

    Returns:
        None.
    """


    # Send the final answer.
    await cl.Message(content=f"This is the final answer").send()