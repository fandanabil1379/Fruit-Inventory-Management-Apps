from tabulate import tabulate

def string_validation(title):
    """Fungsi untuk validasi tipe data string

    Args:
        title (String): Pesan yang akan ditampilkan pada layar

    Returns:
        String: Nilai yang diinputkan
    """
    while True:
        teks = input(title)
        if teks.isalpha() == True:
            break
        else:
            print('Silahkan inputkan hanya teks')
    return teks.capitalize()

def integer_validation(title, minval=0, maxval=100):
    """Fungsi untuk validasi bilangan bulat

    Args:
        title (String): Pesan yang akan ditampilkan pada layar
        minval (int, optional): Batas bawah. Defaults to 0.
        maxval (int, optional): Batas atas. Defaults to 100.

    Returns:
        Int: Nilai yang diinputkan
    """
    while True:
        num = input(title)
        try:
            num = int(num)
            if num > minval or num < maxval:
                break
            else:
                print('Angka yang anda masukkan di luar rentang')
        except:
            print('Yang anda inputkan bukan bilangan')
    return num

def show(database, header=['index', 'stock', 'name', 'price']):
    """Fungsi untuk menampilkan data dalam format tabel

    Args:
        database (list): Data persediaan buah
        header (list, optional): Nama kolom. Defaults to ['index', 'stock', 'name', 'price'].
    """
    # Menampilkan data dalam format tabulasi
    print(tabulate(database, headers=header, tablefmt='grid'))

def add(database):
    """Fungsi untuk menambahkan data ke dalam database

    Args:
        database (list): Data persediaan buah
    """
    # Meminta input data buah yang baru
    name = string_validation(title='Masukkan Nama Buah: ')
    stock = integer_validation(
        title='Masukkan Stock Buah: ',
        minval=0
    )
    price = integer_validation(
        title='Masukkan Harga Buah: ',
        minval=0,
        maxval=100000
    )

    # Menambahkan data ke database
    for id, buah in enumerate(database):
        if name in buah:
            database[id] = [id, name, stock, price]
            break
    else:
        database.append([id+1, name, stock, price])

    # Menampilkan database ter-update
    show(database)

def delete(database):
    """Fungsi untuk menghapus data dari database

    Args:
        database (list): Data persediaan buah
    """
    # Menampilkan database terbaru
    show(database)

    # Meminta user input indeks yang akan dihapus
    idx = integer_validation(
        title='Masukkan indeks buah yang ingin dihapus: ',
        maxval=len(database)
    )

    # Melakukan proses penghapusan sesuai indeks buah
    for id in range(len(database)):
        if id == idx:
            del database[idx]
    else:
        print('Buah yang Anda cari tidak ada')

    # Memperbarui indeks buah
    for id, buah in enumerate(database):
        if id != buah[0]:
            database[id][0] = id

    # Menampilkan database terbaru
    show(database)