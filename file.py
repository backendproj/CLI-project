from pathlib import Path
print("Assalomu alekum!")
def papkaga_kirish(kirish):
        print(Path.home() /"Desktop"/kirish)
        print(f"{kirish} ga kirildi!")
def papka_yaratish(papka):
    try:
        desk = Path.home() /"Desktop"/papka
        desk.mkdir()
        print(f"{papka} nomli papka yaratildi!")
    except FileExistsError:
        print("Papka allaqachon yaratilgan!")
def file_yaratish(file):
    try:
            ds = Path.home() / "Desktop"/file
            ds.touch()
            print(f"{file} nomli file yaratildi!")
    except FileExistsError:
        print("File allaqachon yaratilgan!")
def ozgartirish(old_papka,new_papka,file):
    try:
        desktop = Path.home() / "Desktop"
        new = desktop /old_papka /file
        old = desktop / new_papka / file
        new.replace(old)
        print(f"{old_papka} papkadagi {file} file {new_papka} papkasiga ko`chirildi!")
    except FileNotFoundError:
        print("File o`zgartirib bo`lingan")
def ochirish(delate_papka):
        try:
                delate = Path.home() / "Desktop" / delate_papka
                delate.rmdir()
                print(f"{delate_papka} nomli papka o`chrildi")
        except FileNotFoundError:
                print("Papka o`chirilib bo`lingan!")
print(ozgartirish("A","B","main.py"))