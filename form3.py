print('''siz bu tizim orqali siz oziz xoxlagan odam xaqida malumot olishingiz mumkun
1 F.I.SH
2 email
3 tel_raqam
''')

from sqlite3 import connect
test = connect('USERS.db')
cursor = test.cursor()
print(cursor.fetchall())
num = int(input("Raqamni kriting :  "))
if num ==1 :
    fish = input(("F.I.SH ni krting: "))
    cursor.execute('''
        SELECT * FROM users;
    ''')
    
    all = cursor.fetchall()
    if fish  in all[0]:
            p = cursor.execute('''
        SELECT * FROM users WHERE FISH="Bakhodirov Mirafzal"
    ''')    
            print(p)
            # print(all)
            print("Siz 1 orqali F.I.SH ni qoldrdingiz mana uning malumotlari :  ")
            print(f'''
        F.I.SH :{all[0][0]}
        email: {all[0][1]}
        tel nomer: {all[0][2]}
        
        ''')
    else:
            print('''Siz kritgan parametrda xatolik bor :
        Yana urinish uchun: Y
        Boshqa xizmatdan foydalanish uchun : B

        Kommandani kriting :
        ''')
elif num==2:
    email = input("Email ni kriting : ")
    cursor.execute('''
        SELECT * FROM users;
    ''')
    all = cursor.fetchall()
    if email  in all[0]:
            print("Siz 1 orqali F.I.SH ni qoldrdingiz mana uning malumotlari :  ")
            print(f'''
        F.I.SH :{all[0][0]}
        email: {all[0][1]}
        tel nomer: {all[0][2]}
        
        ''')
    else:
            print('''Siz kritgan parametrda xatolik bor :
        Yana urinish uchun: Y
        Boshqa xizmatdan foydalanish uchun : B

        Kommandani kriting :
        ''')
elif num==3:
    tel = int(input("Telefon  raqamni kriting :  "))
    cursor.execute('''
        SELECT * FROM users;
    ''')
    all = cursor.fetchall()
    if tel  in all[0]:
            print("Siz 1 orqali F.I.SH ni qoldrdingiz mana uning malumotlari :  ")
            print(f'''
        F.I.SH :{all[0][0]}
        email: {all[0][1]}
        tel nomer: {all[0][2]}
        
        ''')
    else:
            print('''Siz kritgan parametrda xatolik bor :
        Yana urinish uchun: Y
        Boshqa xizmatdan foydalanish uchun : B

        Kommandani kriting :
        ''')
else :
    print("Komandani togri kriting3!")
    
        
