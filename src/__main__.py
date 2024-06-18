import os
import sys
import csv
import mylib

def clear_screen():
    """
    A function to clean the user interface
    """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def initialize_db():
    """
    A function to initialize the database 

    Returns:
        dict: Fruit database
    """
    with open(PATH, 'r') as file:
        # Membuat objek reader
        reader = csv.reader(file, delimiter=";")
        # Inisialisasi database kosong
        database = {}
        # Mengisi data ke dalam database
        for row in reader:
            idx, name, stock, price = row
            database.update({name: [int(idx), name, int(stock), int(price)]})

    return database

def main():
    global database

    while True:
        # Menampilkan tampilan utama
        print('''
Selamat Datang di Pasar Buah!

    List Menu:
    1. Show
    2. Add
    3. Delete
    4. Buy 
    5. Exit
''')
        # Meminta input nomor sesuai pilihan menu
        option = mylib.integer_validation("Masukkan angka sesuai menu: ")

        # Menjalankan fungsi sesuai pilihan menu
        if option == 1:
            mylib.show(database)
        elif option == 2:
            mylib.add(database)
        elif option == 3:
            mylib.delete(database)
        elif option == 4:
            mylib.buy(database)
        elif option == 5:
            break
        else:
            print('Inputkan hanya angka 1-5!')

        # Menjaga agar database selalu diperbarui
        with open(PATH, 'w') as file:
            # Membuat objek writer
            writer = csv.writer(file, delimiter=";")
            # Menulis data ke dalam file csv
            writer.writerows(database.values())

if __name__ == "__main__":
    # Membersihkan tampilan user
    clear_screen()

     # Mengatur letak file database
    if getattr(sys, 'frozen', False):
        PATH = sys._MEIPASS
        PATH = os.path.join(PATH, 'data/db.csv') 
    else:
        PATH = os.getcwd()
        PATH = os.path.join(PATH, 'data/db.csv') 

    # Inisialisasi database
    database = initialize_db()

    # Menjalankan menu utama
    main()
    