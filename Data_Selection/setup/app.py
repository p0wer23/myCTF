from flask import Flask, request
import mysql.connector, hashlib

app = Flask(__name__)

# MySQL config
mysql_host = "127.0.0.1"
mysql_user = "Cybercon"
mysql_password = "G4m30f1if3"
mysql_db = "Cybercon"

def authenticate_user(username, password):
    try:
        conn = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            database=mysql_db
        )

        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result  
    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)
        return None

@app.route('/login', methods=['POST'])
def handle_request():
    try:
        username = request.form['username']
        password = hashlib.md5(request.form['password'].encode()).hexdigest()
        user_data = authenticate_user(username, password)

        if user_data:
            return "cybercon{P4r4m3t3r_p011uti0n}"  
        else:
            return "Invalid credentials"  
    except:
        return "internal error happened"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
