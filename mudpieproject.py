import pyodbc as pyo
print (" ")
print ("Updated on 27-Jun-20240Thu ")
print ("Version:  Mackenzie Mackenzie")
print (" ")
print ("Original Version is From Mackenzie Mackenzie ")
print (" ")
print ("opening ..")
cnn_string=(
               r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
               r'DBQ=G:\DOB\DateOfBirthMDB.mdb'
              )
cnn = pyo.connect(cnn_string)
cursor = cnn.cursor()
# sql = (
#        r"Insert into Table01_DateOfBirth (NickName, DateOfBirth) Values "
#        r" ()
#       )

# cursor.execute(sql)
# cursor.commit()

sql = "select * from Table01_DateOfBirth"
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)
print("success...")
cursor.close()
cnn.close()
print("connection closed.")    
