from pymongo import MongoClient

class MongoDB:

    def __init__(self):
        client = MongoClient("mongodb+srv://luishhuttener:M3fnIB6rlz2WzyMD@datasetlibrasyoutube.7mnoo.mongodb.net/?retryWrites=true&w=majority&appName=DatasetLibrasYoutube")
        self.db = client.get_database('LibrasDB')
    
    def connect_collection(self, collection = 'channels'):
        return self.db.get_collection(collection)
    