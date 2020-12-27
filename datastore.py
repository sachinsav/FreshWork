import pickle

class datastore:
    def __init__(self,filepath="D"):
        self.filepath = filepath+":\\datastore"
        self.data = {}

    def load(self):
        dbfile = open(self.filepath,'rb')
        self.data = pickle.load(dbfile)
        print(self.data)

    def append(self):
        dbfile = open(self.filepath, 'ab') 
        pickle.dump(self.data,dbfile)

    def create(self,key="name",val="sachin"):
        self.data[key] = val
        self.append()
        

db = datastore()
db.create()
db.load()