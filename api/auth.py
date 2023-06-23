from flask import request, jsonify
from api.config import app, mysql
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from utils.verifyemail import verifyEmail, decode_auth_token, encode_auth_token


@app.route('/auth/signin', methods = ['POST', 'GET'])
def login():
    if (
        request.method == "POST"
        and "email" in request.form
        and "password" in request.form
    ):  
        email = request.form["email"]
        password = request.form["password"]
        sqlRead = "SELECT * FROM Users WHERE email = %s"
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(sqlRead, (email,))
            results = cursor.fetchall()
            if len(results) > 1:
                return jsonify({"message": "Double users"})
            elif len(results) == 0:
                return jsonify({"message": "User not exist"})
            elif results:
                userData = results[0]
                passwd = userData[4]
                status = userData[5]
                if status == 0:
                  return jsonify({"message": "User not verified. Signup again!"})
                data = {
                    "email": userData[1],
                    "firstName": userData[2],
                    "lastName": userData[3],
                }
                if passwd and check_password_hash(passwd, password) == True:
                    token = encode_auth_token(userData[1])
                    return jsonify({"token": token,"data":data, "message": "success signin"})
                return jsonify({"message": "password is incorrect"})
            else:
                return jsonify({"message": "user not exist"})
        except Exception as e:
            print("Database connection failed due to {}".format(e))
            return jsonify({"message": "signin failed"})
    
@app.route('/auth/signup', methods = ['POST', 'GET'])
def register():
    if (
        request.method == "POST"
        and "email" in request.form
        and "password" in request.form
    ):
        email = request.form["email"]
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        password = generate_password_hash(request.form["password"])
        sqlRead = "SELECT * FROM Users WHERE email = %s"
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(sqlRead, (email,))
            results = cursor.fetchall()
            print(results)
            cursor.close()
            if len(results) > 0:
              if results[0][5] == 0:
                verifyEmail(email, firstName)
                return jsonify({"message": "User already registered. Confirm your Email"})
              else:
                return jsonify({"message": "User already registered."})
            else:
                sqlRegister = "INSERT INTO `Users` (`email`, `firstName`, `lastName`, `password`, `status`) VALUES (%s, %s,%s, %s,%s)"
                cursor = mysql.connection.cursor()
                cursor.execute(
                    sqlRegister,
                    (
                        email,
                        firstName,
                        lastName,
                        password,
                        0
                    ),
                )
                mysql.connection.commit()
                cursor.close()
                
                verifyEmail(email, firstName)
                return jsonify({"message": "Signup successed. Pleae confirm your email"})
        except Exception as e:
            print(e)
            return jsonify({"message": "Server Error"})
    else:
        return jsonify({"message": "Missing fields"})
    
@app.route("/auth/validateToken", methods=["POST"])
def validateToken():
  if (
        request.method == "POST"
        and "token" in request.form
    ):
    token = request.form['token']
    if (token is not None):
        result = decode_auth_token(token)
        if result == '200':
          return jsonify({'message':'success'})
        else: 
          return jsonify({'message':'error'})
    else:
        return jsonify({'message':'error'})