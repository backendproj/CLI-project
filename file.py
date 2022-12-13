from pathlib import Path
print("Assalomu alekum!")
def papkaga_kirish(kirish):
        print(Path.home() /"Desktop"/kirish)
def papka_yaratish(papka):
    try:
            desk = Path.home() /"Desktop"/papka
            desk.mkdir()
    except FileExistsError:
        print("Papka allaqachon yaratilgan!")
def file_yaratish(file):
    try:
            ds = Path.home() / "Desktop"/file
            ds.touch()
    except FileExistsError:
        print("File allaqachon yaratilgan!")
def ozgartirish(old_papka,new_papka,file):
    desktop = Path.home() / "Desktop"
    new = desktop /old_papka /file
    old = desktop / new_papka / file
    new.replace(old)
def ochirish(delate_papka):
        delate = Path.home() / "Desktop" / delate_papka
        delate.rmdir()