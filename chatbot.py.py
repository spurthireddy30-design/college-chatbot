print("*" * 40)
print("*" + " " * 38 + "*")
print("*" + "  Welcome to CollegeBot!".center(38) + "*")
print("*" + "  Your college assistant!".center(38) + "*")
print("*" + " " * 38 + "*")
print("*" * 40)
print()
print("Ask me about internships, CGPA, skills,")
print("NPTEL and more! Type 'bye' to exit.")
print()
chat_log = open("chat_history.txt", "w")
print("Welcome to CollegeBot!")

while True:
    message = input("Write a message... ").lower()
    
    if message == "hello":
        reply="CollegeBot: Hey! How can I help you?"
        print(reply)
        chat_log.write("You: " + message + "\n")
        chat_log.write(reply + "\n")
    elif message == "what is nptel":
        reply="CollegeBot: NPTEL is a free platform by IITs! Great for certifications!"
        print(reply)
        chat_log.write("You: " + message + "\n")
        chat_log.write(reply + "\n")
    elif message == "how to get internship":
        reply="CollegeBot: Build projects, get certifications and apply on Internshala!"
        print(reply)
        chat_log.write("You: " + message + "\n")
        chat_log.write(reply + "\n")
    elif message == "what skills should i learn":
        reply="CollegeBot: Learn Python, Full Stack Development and AI/ML — very high demand!"
        print(reply)
        chat_log.write("You: " + message + "\n")
        chat_log.write(reply + "\n")
    elif message == "how to improve cgpa":
        reply="CollegeBot: Attend classes, practice previous papers and study consistently!"
        print(reply)
        chat_log.write("You: " + message + "\n")
        chat_log.write(reply + "\n")
    elif message == "how much cgpa required to get a good job":
        reply="CollegeBot: 9+ cgpa looks decent,not only cgpa but skills matter more nowadays."
        print(reply)
        chat_log.write("You: " + message + "\n")
        chat_log.write(reply + "\n")
    elif message == "bye" or message=="byee":
        reply="CollegeBot: Goodbye!"
        print(reply)
        chat_log.write("You: " + message + "\n")
        chat_log.write(reply + "\n")
        break
    else:
        print("CollegeBot: I don't know that yet!")