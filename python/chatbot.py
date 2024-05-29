import random

# Define responses for different user inputs
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm fine, thanks for asking.", "I'm good, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"],
    "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm still learning!"]
}

def respond(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])

def main():
    print("Welcome to the Basic Chatbot!")
    print("You can start chatting. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print(respond(user_input))
            break
        else:
            print("Chatbot:", respond(user_input))

if __name__ == "__main__":
    main()
