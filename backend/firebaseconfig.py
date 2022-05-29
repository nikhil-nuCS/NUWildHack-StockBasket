
import pyrebase

class FirebaseFlaskConfig:
    firebaseConfig = {
        "apiKey": "AIzaSyC5aFHgfudn6WnY4YPIOiKd6VXy56YahDo",
        "authDomain": "stockbasket-2201.firebaseapp.com",
        "databaseURL": "https://stockbasket-2201-default-rtdb.firebaseio.com",
        "projectId": "stockbasket-2201",
        "storageBucket": "stockbasket-2201.appspot.com",
        "messagingSenderId": "33605817709",
        "appId": "1:33605817709:web:ed3f7f196cac05b87bb664"
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
