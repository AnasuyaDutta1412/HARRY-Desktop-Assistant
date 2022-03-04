import mysql.connector as my
mydb = my.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="harry"
    )
def insertindb(t,d):
    
    cursor = mydb.cursor()
    sql ="insert into WIKI values(%s,%s)"
    cursor.execute(sql,(t,d))
    mydb.commit()

def getdata(t):
    cursor = mydb.cursor()
    sql = "select des from WIKI where Topic = '{}'".format(t)
    cursor.execute(sql)
    data = cursor.fetchall()
    if len(data) == 0:
        return "No data found"
    else:
        b = str(data[0])
        b = b.replace("(", "")
        b = b.replace(")", "")
        b = b.replace("\"", "")
        return b