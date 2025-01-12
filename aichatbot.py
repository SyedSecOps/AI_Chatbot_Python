import random
from datetime import datetime

# Simple Rule-Based Chatbot Using Dictionary with Enhancements

def chatbot():
    print("Chatbot: Hello! I am your assistant. Type 'bye' to exit.")
    
    # Predefined responses stored in a dictionary
    responses = {
        "hello": ["Hi there! How can I help you?", "Hello! What's up?", "Hey! How can I assist you today?"],
        "hi": ["Hello!", "Hey there!", "Hi! How can I help you?"],
        "how are you": ["I'm just a program, but I'm doing great! How about you?", "I'm doing well, thank you! How are you?"],
        "your name": "I'm just a simple chatbot. You can call me Assistant.",
        "time": lambda: f"The current time is {datetime.now().strftime('%H:%M:%S')}.",
        "weather": "I'm not connected to the internet, but I hope it's sunny!",
        "bye": "Goodbye! Have a great day!",
        "help": "You can ask me about the time, weather, how I'm doing, or just chat with me!",
        "favorite color": "I don't have a favorite color, but I think blue is nice!",
        "what is your purpose": "I am here to assist you with information and have a friendly conversation!",
        "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
        "are you human": "No, I'm a chatbot, a simple program created to assist you.",
        "thank you": ["You're welcome!", "Happy to help!", "Glad I could assist you!"],
        "how old are you": "I don't age, but I was created recently to help you out!"
    }
    
    # Track the user's name for personalization
    user_name = None
    
    while True:
        user_input = input("You: ").lower()  # Convert user input to lowercase
        
        # Exit condition
        if user_input == "bye":
            print(f"Chatbot: {responses['bye']}")
            break
        
        # Personalized greeting if user name is known
        elif user_name and "your name" in user_input:
            print(f"Chatbot: My name is Assistant. But you can call me whatever you like, {user_name}!")
        
        # Asking for user name and storing it
        elif "my name is" in user_input:
            user_name = user_input.split("is")[-1].strip()
            print(f"Chatbot: Nice to meet you, {user_name}!")
        
        # Check for exact matches or fuzzy matching in the dictionary
        elif any(keyword in user_input for keyword in responses.keys()):
            # Handle multiple responses for a keyword
            for key, value in responses.items():
                if key in user_input:
                    if isinstance(value, list):  # Multiple responses
                        print(f"Chatbot: {random.choice(value)}")
                    else:  # Single response
                        print(f"Chatbot: {value() if callable(value) else value}")
                    break

        # Default response if no match is found
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you try asking something else?")
            
# Run the chatbot
chatbot()
