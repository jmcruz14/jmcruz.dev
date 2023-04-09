import psycopg2
import pandas as pd

def getdblocation():
    db = psycopg2.connect(
        host = 'localhost',
        database = 'IE172-database',
        user = 'postgres',
        port = 5432,
        password = PASSWORD_HERE
    )
    return db

def modifydatabase(sql, values):
    db = getdblocation()

    # We create a cursor object
    # Cursor - a mechanism used to manipulate db objects on a per-row basis 
    # # In this case, a cursor is used to add/edit each row
    cursor = db.cursor()

    # Execute the sql code with the cursor value
    cursor.execute(sql, values)

    # Make the changes to the db persistent
    db.commit()

    # Close the connection (so nobody else can use it)
    db.close()

def querydatafromdatabase(sql, values, dfcolumns):

    db = getdblocation()
    cur = db.cursor()
    cur.execute(sql, values) #Calls the table of the database
    rows = pd.DataFrame(cur.fetchall(), columns=dfcolumns)
    db.close()
    return rows
