print('''Asalomalekum !
quidagi berilgan xizmatlarni tanglang 
1 Roixatdan otish 
2 Tekshirish 
3 Fayllar blan ishlash
''')
num = int(input("Raqamni kriting : "))

if num == 1 :
    import base
elif num == 2:
    import form3
elif num == 3 :
    print('''
    Siz bu tizim orqali kompiyuteringizdagi faylarni kochirish ,
    ochirish, ozgartirish va h.k.z larni qlshingiz mumkun

    Faylga kirish uchun : K
    Fayl yaratish uchun: Y
    Papka yaratish uchun: P
    Faylni boshqa faylga ozgartirish uchun : O
    komandalarni kriting 
    ''')
    comand = input("komandni kriting : ")

