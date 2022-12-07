# Otabek


text = '''Xush kelibsiz Xurmatli mijoz!

Biz

register
login
check
fayl xizmatlari

'''
print(text)
ask = input("Xizmat turi: ")
if ask.lower() == "register":
    email = input("Email: ")
    login = input("Login: ")
    parol = input("Parol: ")
elif ask.lower() == "login":
    login = input("Login: ")
    parol = input("Parol: ")
elif ask.lower() == "check":
    user = input("Kimni izlayabsiz: ")
else:
    pass