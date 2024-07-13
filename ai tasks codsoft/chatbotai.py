def chatbot_response(user_input):
    user_input = user_input.lower()

    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    
    elif "your name" in user_input:
        return "I'm ChatGPT, your friendly chatbot!"

    
    elif "weather" in user_input:
        return "I'm not sure about the weather right now, but you can check a weather website for the latest updates!"

    
    elif "time" in user_input:
        return "I don't have real-time capabilities, but you can check the clock on your device."


    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
