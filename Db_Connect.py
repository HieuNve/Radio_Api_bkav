import json

import mysql


def getConnect():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="21102001",
        auth_plugin='mysql_native_password'
    )
    return db


