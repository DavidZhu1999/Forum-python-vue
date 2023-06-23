from flask import request, Blueprint, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
from model.usermodel import *
from model.extensions import mail
import random

app_user = Blueprint('app_user', __name__, url_prefix='/user')

CORS(app_user, supports_credentials=True)


@app_user.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    print(username, email, password)
    searchusername = exist_user_username(username)
    searchemail = exist_user_email(email)
    if not searchemail and not searchusername:
        code_list = []
        for i in range(2):
            random_number = random.randint(0, 9)
            a = random.randint(65, 90)
            b = random.randint(97, 122)
            random_uppercase_letter = chr(a)
            random_lowercase_letter = chr(b)
            code_list.append(str(random_number))
            code_list.append(random_uppercase_letter)
            code_list.append(random_lowercase_letter)
        verification_code = ''.join(code_list)
        print(verification_code)
        msg = Message(subject="helloworld",
                      sender='3588034273@qq.com',
                      recipients=[f'{email}'])
        msg.body = f'{verification_code}'
        mail.send(msg)
        insert_verifycode(email, verification_code)
        print("success")
        return jsonify({"status": '1', "message": "please go to find verifycode from email"})
    if searchusername:
        return jsonify({"status": '0', "message": "username has been used"})
    if searchemail:
        return jsonify({"status": '-1', "message": "email has been used"})


@app_user.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    code = check_user(email, password)
    username = return_username(email)
    returnusername = username[0][0]
    print(code)
    if code == -1:
        return jsonify({"status": code, "message": "email or password error"})
    if code == 1:
        return jsonify({"status": code, "message": "login success", "data": returnusername})


@app_user.route('/emailverify', methods=['POST'])
def emailverify():
    data = request.get_json()
    verifycode = data['verifycode']
    username = data['username']
    password = data['password']
    email = data['email']
    searchverifycode = search_verifycode(email)
    print(searchverifycode[0][0])
    print(verifycode)
    if searchverifycode[0][0] == verifycode:
        if time.time() - float(searchverifycode[0][1]) <= 60 * 30:
            insert_user(username, email, password)
            delete_verifycode(email)
            return jsonify({"status": '1', "message": "register success"})
        else:
            return jsonify({"status": '-1', "message": "verifycode expired"})
    return jsonify({"status": '0', "message": "register error"})

# @app_user.route('/return_user', methods=['POST'])
# def return_user():
#     data = request.get_json()
#     email = data['email']
#     print(email)
#     username = return_username(email)
#     print(username)
#     returnusername = username[0][0]
#     print(returnusername)
#     return jsonify({"status": '1', "data":returnusername})

@app_user.route('/getemail', methods=["POST"])
def getemail():
    data = request.get_json()
    username = data['username']
    email = return_email(username)
    return jsonify({"status":'1',"email":email})

@app_user.route('/changepassword', methods=["POST"])
def changepassword():
    data = request.get_json()
    email = data['email']
    searchemail = exist_user_email(email)
    if searchemail:
        code_list = []
        for i in range(2):
            random_number = random.randint(0, 9)
            a = random.randint(65, 90)
            b = random.randint(97, 122)
            random_uppercase_letter = chr(a)
            random_lowercase_letter = chr(b)
            code_list.append(str(random_number))
            code_list.append(random_uppercase_letter)
            code_list.append(random_lowercase_letter)
        verification_code = ''.join(code_list)
        print(verification_code)
        msg = Message(subject="helloworld",
                      sender='3588034273@qq.com',
                      recipients=[f'{email}'])
        msg.body = f'{verification_code}'
        mail.send(msg)
        insert_verifycode(email, verification_code)
        print("success")
        return jsonify({"status": '1', "message": "please go to find verifycode from email"})
    return jsonify({"status": '0', "message":"email input error"})

@app_user.route('/changepasswordverifycode', methods=["POST"])
def changepasswordverifycode():
    data = request.get_json()
    email = data['email']
    verifycode = data['verifycode']
    password = data['password']
    searchverifycode = search_verifycode(email)
    print(searchverifycode[0][0])
    if verifycode == searchverifycode[0][0]:
        change_password(email,password)
        return jsonify({"status": '1', "message":"change password success"})
    return jsonify({"status": '0', "message":"error"})