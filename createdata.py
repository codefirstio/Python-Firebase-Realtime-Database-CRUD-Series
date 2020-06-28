import pyrebase

#Initialize Firebase
firebaseConfig={"apiKey": "AIzaSyDm2HeGl3bApix5KsbhI8NOjdwXkhNTaJM",
    "authDomain": "trialauth-7eea1.firebaseapp.com",
    "databaseURL": "https://trialauth-7eea1.firebaseio.com",
    "projectId": "trialauth-7eea1",
    "storageBucket": "trialauth-7eea1.appspot.com",
    "messagingSenderId": "441088628124",
    "appId": "1:441088628124:web:6fc6142f0e28275e2f2459",
    "measurementId": "G-NKL8XN36NX"}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

#Push Data
data={"age":20, "address":["new york", "los angeles"]}
print(db.push(data)) #unique key is generated

#Create paths using child
#data={"name":"Jane", "age":20}
#db.child("Branch").child("Employees").push(data)

#Create your own key
data={"age":20, "address":["new york", "los angeles"]}
db.child("John").set(data)

#Create your own key + paths with child
data={"name":"John", "age":20, "address":["new york", "los angeles"]}
db.child("Branch").child("Employee").child("male employees").child("John's info").set(data)



