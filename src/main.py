import mylib

daftarBuah = [
    [0, 'Apel', 20, 10000],
    [1, 'Jeruk', 15, 15000],
    [2, 'Anggur', 25, 20000]
]

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

        # Meminta input menu yang di pilih
        option = input("Masukkan angka sesuai menu: ")

        # Menjalankan fungsi sesuai input
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

main()