
import pyrebase

class FirebaseFlaskConfig:
    firebaseConfig = {
        "apiKey": "",
        "authDomain": "",
        "databaseURL": "",
        "projectId": "",
        "storageBucket": "",
        "messagingSenderId": "",
        "appId": ""
        }
    
    def __init__(self):
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)

    def getFirebaseDatabase(self):
        db= self.firebase.database()
        return db
    
    def getFirebaseAuth(self):
        return self.firebase.auth()



#Push Data
# data={"age":20, "address":["new york", "los angeles"]}
# print(db.push(data)) #unique key is generated

# #Create paths using child
# #data={"name":"Jane", "age":20}
# #db.child("Branch").child("Employees").push(data)

# #Create your own key
# data={"age":20, "address":["new york", "los angeles"]}
# db.child("John").set(data)

# #Create your own key + paths with child
# data={"name":"John", "age":20, "address":["new york", "los angeles"]}
# db.child("Branch").child("Employee").child("male employees").child("John's info").set(data)
