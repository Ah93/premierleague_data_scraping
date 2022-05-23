import pymysql
import mysql.connector

connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='Pl_data',
    port=3306
)


def insertScrapedPLData(PlDataToInsert):
    try:
        mySql_insert_query = """INSERT INTO pldata (team, Pld, Pts, GD, W, D, L, A, F, season) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

        cursor = connection.cursor()
        cursor.executemany(mySql_insert_query, PlDataToInsert)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into pldata table")

    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    # finally:
    #     connection.close()