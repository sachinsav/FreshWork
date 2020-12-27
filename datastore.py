import pickle
import os
import json

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

    def create(self,key="name3",val={"a":5}):
        if key in self.data:
            raise Exception("given key is already exists")
        else:
            val = json.dumps(val)
            self.data[key] = val

    def read(self,key):
        return self.data.get(key)
    def delete(self,key):
        if key not in self.data:
            raise Exception("given key does not exists")
        return self.data.pop(key)
        

db = datastore()
# db.create()
# db.commit()
print(db.getdata())
print(db.read("name3"))
db.delete("name3")
# db.commit()