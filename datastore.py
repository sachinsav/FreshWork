import pickle
import os
import json
from threading import Thread
from time import sleep

class datastore(Thread):
    def __init__(self,path="D:/datastore"):
        super(datastore, self).__init__()
        filepath = os.path.join(path, 'datastore')
        if not os.path.exists(path):
            os.makedirs(path)
        self.filepath = filepath
        self.data = self.loadData()
        self.start()
        
        
    def loadData(self): 
        try:
            dbfile = open(self.filepath, 'rb')      
            data = pickle.load(dbfile) 
            dbfile.close()
            return data
        except Exception as e:
            print(e)
            return {}
        
    def run(self):
        while True:
            for key in self.data:
                if self.data[key]["ttl"] > -1:
                    self.data[key]["ttl"] -= 1
            self.commit()
            sleep(1)
        
    def getAlldata(self):
        return self.data
    def getdata(self):
        newData = {}
        for key,val in self.data.items():
            if val["ttl"]!=-1:
                newData[key] = val
        return newData

    def commit(self):
        try:
            dbfile = open(self.filepath, 'wb')
            pickle.dump(self.data,dbfile)
            dbfile.close()
        except Exception as e:
            print(e)

    def create(self,key="name5",val={"ab":5},ttl=-2):
        if key in self.data:
            raise Exception("given key is already exists")
        else:
            val["ttl"] = ttl
            val = self.getJsonVal(val)
            val = json.loads(val)
            self.data[key] = val
        self.commit()

    def readByKey(self,key):
        val = self.data.get(key)
        if not val:
            raise Exception("Given key is not present")
        if val["ttl"]!=-1:
            return json.dumps(val)

    def delete(self,key):
        val = self.data.get(key)
        if not val:
            raise Exception("Given key is not present")
        if val["ttl"]!=-1:
            return self.data.pop(key)
        self.commit()

    def getJsonVal(self,val={"ab":5,"ttl":3}):
        return json.dumps(val)
