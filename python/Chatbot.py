import nltk
from nltk.chat.util import Chat, reflections

# Pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by OpenAI.",]
    ],
    [
        r"how are you ?",
        ["I'm good, thank you!", "I'm doing well, and you?",]
    ],
]

# Create Chat Bot
chatbot = Chat(pairs, reflections)

# Start Chat
print("Hello! I am your chatbot. Type 'quit' to exit.")
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    print(chatbot.respond(user_input))
