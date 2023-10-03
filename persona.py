
    # Save the updated conversation history to the file
    with open('conversation_history.json', 'w') as file:
        json.dump(conversation, file)