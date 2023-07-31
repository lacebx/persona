import openai
import requests
import json

# Set up OpenAI API credentials
openai.api_key = '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'

# Define persona prompt (same as before)
persona_prompt = "Imagine you are Lisa, a highly advanced AI assistant specifically built to cater to the needs of students..."

# Load the conversation history from a file (or create an empty list)
def load_conversation_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            conversation = json.load(file)
    except FileNotFoundError:
        conversation = []
    return conversation

# Function to send a user message and receive an assistant response
def chat(message):
    conversation.append({'role': 'user', 'content': message})

    # Truncate the conversation history to fit within the token limit
    while len(json.dumps(conversation)) > 4096:
        conversation.pop(0)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    conversation.append({'role': 'assistant', 'content': response['choices'][0]['message']['content']})
    return response['choices'][0]['message']['content']

# Start the interactive conversation
conversation = load_conversation_from_file('conversation_history.json')

# Append the persona prompt if the conversation is empty or has been truncated
if not conversation or conversation[0]['content'] != persona_prompt:
    conversation = [{'role': 'system', 'content': persona_prompt}]

# Example usage
while True:
    user_input = input("User: ")
    response = chat(user_input)
    print("Lisa:", response)

    # Append the new conversation to the conversation history
    conversation.append({'role': 'user', 'content': user_input})
    conversation.append({'role': 'assistant', 'content': response})

    # Save the updated conversation history to the file
    with open('conversation_history.json', 'w') as file:
        json.dump(conversation, file)
