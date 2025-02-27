from http.cookiejar import debug

from flask import Flask,jsonify,request
from config import Config
from models import db,Registration

app=Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/home', methods=['GET'])
def home_func():
    return "Hello world!this is my sample flask project"

@app.route('/register',methods=['POST'])

def register_func():
 data=request.get_json(silent=True)
 if data:
    print(data)
    username_from_user=data.get('username')
    password_from_user=data.get('password')

    user=Registration.query.filter_by(username=username_from_user).first()
    print("******",user)
    if user:
            return jsonify(msg=f"user with {username_from_user} already exists")
    usr_to_insert_db = Registration(username=username_from_user,password=password_from_user)

    db.session.add(usr_to_insert_db)
    db.session.commit()
    return jsonify(msg=f"user with username {username_from_user} successfully registered")
 return jsonify(msg=f"please provide username and password")

@app.route('/login',methods=['POST'])
def login_func():
    data=request.get_json(silent=True)
    if data:
        username_from_user=data.get('username')
        password_from_user=data.get('password')
        user=Registration.query.filter_by(username=username_from_user,password=password_from_user).first()
        print("==== user",user)
        if user:
            return jsonify(msg="user logged in")
        return jsonify(msg="provide valid credentials")

if __name__ == '__main__':
     app.run(debug==True)
     #app.run(debug=True, port=5000)
