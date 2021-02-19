# Authentication of database
import firebase_admin
from firebase_admin import credentials, firestore
databaseURL = {
# Url of your database
     'databaseURL': "https://console.firebase.google.com/u/0/project/wallpaperapp-4f6de/firestore/data~2Fads%3F~2F1"
}
cred = credentials.Certificate('/content/serviceAccountKey.json')
firebase_admin.initialize_app(cred, databaseURL)

db = firestore.client()  # this connects to our Firestore database
collection = db.collection('earnMoneyUser')  # opens 'earnMoneyUser' collection

print(collection.stream())
