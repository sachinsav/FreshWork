import pickle
import os
class datastore:
    def __init__(self,path="D:/datastore"):
        filepath = os.path.join(path, 'datastore')
        if not os.path.exists(path):
            os.makedirs(path)
        self.filepath = filepath
        self.data = self.loadData()
        
        
    def loadData(self): 
        try:
            dbfile = open(self.filepath, 'rb')      
            data = pickle.load(dbfile) 
            dbfile.close()
            return data
        except:
            return {}

    def getdata(self):
        return self.data

    def commit(self):
        try:
            dbfile = open(self.filepath, 'wb')
            pickle.dump(self.data,dbfile)
            dbfile.close()
        except:
            pass

    def create(self,key="name2",val="sachin"):
        self.data[key] = val
        

db = datastore()
# db.create()
# db.commit()
print(db.getdata())
