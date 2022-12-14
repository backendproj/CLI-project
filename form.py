from sqlite3 import connect

FISH = (input("F.I.SH. ni kriting: "))
email = (input("Email ni kriting : "))
tel = int(input("Telefon raqamingizni ktiting : "))


with connect("USERS.db") as test:
    cursor = test.cursor()
    cursor.execute(f"INSERT INTO users VALUES('{FISH}','{email}','{tel}')") 
    cursor.execute('''
        SELECT * FROM users;
    
    ''')
print("Tabriklayman siz roixatdan muvofaqiyatli otdingiz....")
import form3

