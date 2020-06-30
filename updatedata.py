import pyrebase

firebaseConfig={"apiKey": "AIzaSyBPhwfUTQqOwKq2xH9087gHEslqEQTSNro",
    "authDomain": "pyrebaserealtimedbdemo.firebaseapp.com",
    "databaseURL": "https://pyrebaserealtimedbdemo.firebaseio.com",
    "projectId": "pyrebaserealtimedbdemo",
    "storageBucket": "pyrebaserealtimedbdemo.appspot.com",
    "messagingSenderId": "843349173643",
    "appId": "1:843349173643:web:90ff345ff844aa89d5fb8e",
    "measurementId": "G-DT093HRL5R"}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

#Update data with known path
db.child("todolistA").child("monday").child("paper").update({"deadline":"1pm"})

#Multi-location update data
data={"todolistA/monday/paper":{"details":"v2"}, "todolistA/tuesday/filmvideo":{"deadline":"7pm"}}
db.update(data)

#Update data with unknown key
monday_tasks=db.child("todolistB").child("monday").get()
for task in monday_tasks.each():
    if(task.val()['name']=="paper"):
        key=task.key()
db.child("todolistB").child("monday").child(key).update({"deadline":"1pm"})
