from datastore import datastore
from time import sleep

db = datastore()


print(db.getdata())
sleep(6)
print(db.getdata())


