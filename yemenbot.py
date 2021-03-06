from chatterbot import ChatBot

yemenchatbot = ChatBot(
    'YemenBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

from chatterbot.trainers import ListTrainer

trainer = ListTrainer(yemenchatbot)

training_data_quesans = open('training_data/YemenBot_QA.txt').read().splitlines()
training_data_personal = open('training_data/YemenBot_PQ.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer.train(training_data)

from chatterbot.trainers import ChatterBotCorpusTrainer

trainer_corpus = ChatterBotCorpusTrainer(yemenchatbot)

trainer_corpus.train(
    'chatterbot.corpus.english'
)
