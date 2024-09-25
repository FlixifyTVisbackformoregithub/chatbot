from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Define your chatbot
chatbot = ChatBot('ChatBotName')

# Train the chatbot based on the English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

def get_response(message):
    return chatbot.get_response(message)
