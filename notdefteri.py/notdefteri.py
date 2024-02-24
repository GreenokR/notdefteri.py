def create_note():
    """
    Yeni bir not oluşturur.
    """
    note_title = input("Not başlığını girin: ")
    note_content = input("Not içeriğini girin: ")
    with open(f"{note_title}.txt", "w") as note_file:
        note_file.write(note_content)
    print("Not başarıyla oluşturuldu.")

def view_note():
    """
    Var olan bir notu görüntüler.
    """
    note_title = input("Görüntülemek istediğiniz notun başlığını girin: ")
    try:
        with open(f"{note_title}.txt", "r") as note_file:
            note_content = note_file.read()
            print(f"{note_title}:\n{note_content}")
    except FileNotFoundError:
        print("Belirtilen not bulunamadı.")

def delete_note():
    """
    Var olan bir notu siler.
    """
    note_title = input("Silmek istediğiniz notun başlığını girin: ")
    try:
        import os
        os.remove(f"{note_title}.txt")
        print(f"{note_title} başlıklı not başarıyla silindi.")
    except FileNotFoundError:
        print("Belirtilen not bulunamadı.")

def main():
    """
    Ana iş mantığını yürütür.
    """
    print("1. Not Oluştur")
    print("2. Not Görüntüle")
    print("3. Not Sil")

    choice = input("Lütfen seçim yapın (1/2/3): ")

    if choice == '1':
        create_note()
    elif choice == '2':
        view_note()
    elif choice == '3':
        delete_note()
    else:
        print("Geçersiz giriş.")

if __name__ == "__main__":
    main()
