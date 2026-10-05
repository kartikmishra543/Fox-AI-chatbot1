from chatbot import get_response

print("Foxsquare AI Chatbot")
print("Type 'exit' to close the chatbot.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    answer = get_response(question)
    print("Bot:", answer)