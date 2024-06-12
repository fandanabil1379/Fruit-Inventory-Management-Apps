import mylib

daftarBuah = {
    'Apel': [0, 'Apel', 20, 10000],
    'Jeruk': [1, 'Jeruk', 15, 15000],
    'Anggur': [2, 'Anggur', 20, 20000]
}

def main():
    listMenu = '''
Selamat Datang di Pasar Buah!'

List Menu:
1. Show
2. Add
3. Delete
4. Buy 
5. Exit
'''
    while True:
        # Menampilkan tampilan utama
        print(listMenu)

        # Meminta input nomor sesuai pilihan menu
        option = input("Masukkan angka sesuai menu: ")

        # Menjalankan fungsi sesuai pilihan menu
        if option == '1':
            mylib.show(daftarBuah)
        elif option == '2':
            mylib.add(daftarBuah)
        elif option == '3':
            mylib.delete(daftarBuah)
        elif option == '4':
            mylib.buy(daftarBuah)
        elif option == '5':
            break
        else:
            print('Input ada salah. Silahkan input ulang!')

# Menjalankan program utama
main()