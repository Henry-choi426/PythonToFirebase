''' 
pyrebase : https://github.com/thisbejim/Pyrebase
오류 발생 시 : https://m.blog.naver.com/vvv1ct0r/220930787642
'''

from pyrebase import pyrebase
import json

with open("auth.json") as f:
    # FB 설정파일이 담김
    config = json.load(f)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

signin = {"password":"1234","username":"henry"}
db.child("users").child('abcd').set(signin)