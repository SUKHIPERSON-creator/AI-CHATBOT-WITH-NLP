import nltk as nl
#download natural language tool kit from command prompt or terminal
import random as ran
#generate random choices
from nltk.stem import WordNetLemmatizer
#its is a use for making helps reduce words
from nltk.tokenize import word_tokenize
#Splits sentences into words/tokens
nl.download ('punkt')
#Required for word_tokenize()
nl.download ('wordnet')
#Lemma is a language
#Required for wordnet lemmatizer
nl.download ('omw-1.4')
#omw= open multi words
# required for support lemma
lemmatizer = WordNetLemmatizer()#it is use to reduce 
#what user want
intents= {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "see you", "goodbye", "take care"],
    "thanks": ["thanks", "thank you", "thx"],
    "name": ["what is your name", "who are you", "tell your name"],
    "age": ["how old are you", "your age"],
    "weather": ["how is the weather", "weather today", "is it raining"]
}
responses ={
    "greeting": ["Hello!", "Hi there!", "Hey!", "Nice to meet you!"],
    "goodbye": ["Goodbye!", "See you soon!", "Take care!", "Bye!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "name": ["I'm ChatBot!", "My name is helper."],
    "age": ["MAI AMAR HU .", "I'm timeless!"],
    "weather": ["I'm not connected to the internet, so I don't know!"]
    
}
#Preprocess
def preprocess(sen):
    # to clean and prepare for user input
    tokens = word_tokenize(sen.lower())  # Tokenize and lowercase
    #better for understanding(LOWER CASE)
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens
# Step 4: Match user input to intent (what is user input)
def match_intents(User_input):
    #take user input
    processed_input = preprocess(User_input)
    #process user input and preprocess data
    
    for intent,patterns in intents.items():
        for pattern in patterns:
            processed_pattern =preprocess(pattern)
            #pick words from list 
            if all(word in processed_input for word in processed_pattern):
                return intent
              # If no match is found, return "unknown"
    return "unknown"

# 8. Chat Loop
print("Chatbot: Hello! Ask me something. Type 'exit' to stop.")

while True:
    # Take input from user
    user_input = input("You: ")
    
    # Exit condition
    if user_input.lower() == "exit":
        print("Chatbot: Bye! ")
        break

    # Detect intent of user message
    intent = match_intents(user_input)

    # Find response from intent
    response = ran.choice(responses.get(intent, "Sorry, I didn't understand that."))
    
    # Print response
    print("Chatbot:", response)
        

