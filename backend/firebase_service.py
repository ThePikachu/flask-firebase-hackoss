import firebase_admin
from firebase_admin import credentials, firestore

API_KEY_PATH = "firebase-api-key.json"

class FirebaseService:
    def __init__(self):

            self.__cred = firebase_admin.credentials.Certificate(API_KEY_PATH)

            firebase_admin.initialize_app(
                    credential=self.__cred,
                    options={
                        'databaseURL': 'https://firebase-flask-1.firebaseio.com',
                    })

            self.__firestore = firestore.client()

    def get_firestore(self):
        return self.__firestore