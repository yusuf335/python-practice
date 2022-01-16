import random
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('D:/key/hand-on-989cf-firebase-adminsdk-9k5vo-27e299092b.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hand-on-989cf-default-rtdb.firebaseio.com'
})

Count = 0

while True:
    Count += 1
    print(Count)
    ref = db.reference('data')

    data = {"Count": Count, "turbidity": random.randint(0, 10), "ph": random.randint(0, 14),
            "temp": random.randint(0, 40), "time": int(time.time())}

    ref.child('HTTP').set(data)

