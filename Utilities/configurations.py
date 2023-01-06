import configparser
import mysql.connector
from mysql.connector import Error

def getconfig():
    config=configparser.ConfigParser()
    config.read("C:\\Users\\VARUN\Desktop\\Varun_Personal\\API_BDDAutomation_2022\\Utilities\\properties.ini")
    return config


# store db details in dict format and get key values from properties.ini
connect_config = {
    'user': getconfig()['SQL']['user'],
    'password': getconfig()['SQL']['password'],
    'database': getconfig()['SQL']['database'],
    'host': getconfig()['SQL']['host']
}


# db connection function
def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config) # keyword args as its dict format
        if conn.is_connected():
            print("DB Connected")
            return conn
    except Error as e:
        print(e)

# getQuery method to fetch records from table and pass it to payload
def getQuery(query):
    conn=getConnection()
    cursor=conn.cursor()
    cursor.execute(query)
    row=cursor.fetchone()
    conn.commit()
    conn.close()
    return row


# get access token for authentication
def getAccessToken():
    return "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"
