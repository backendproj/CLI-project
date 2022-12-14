# import form
import base
from sqlite3 import connect
test = connect('USERS.db')
cursor = test.cursor()

emaill = input("Emailingizni kriting :  ")

cursor.execute('''
    SELECT email FROM users;
''')

n = cursor.fetchall()
if emaill in n[0]:
    import form2
else :
    print("iltmos quidagi malumotarni togri kriting va jonatishdan oldn tekshirib koring !")
    import form
    


