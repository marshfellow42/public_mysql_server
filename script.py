import mysql.connector

mydb = mysql.connector.connect(
    host="2.tcp.ngrok.io",
    port=16531,
    user="myuser",
    password="mypassword",
    database="mydatabase",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE IF NOT EXISTS TESTE (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome TEXT
);""")

mydb.commit()

print("TESTE foi criado")

mycursor.close()
mydb.close()