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
        minval (int, optional): Nilai minimal. Defaults to 0.
        maxval (int, optional): Nilai maksimal. Defaults to 100.

    Returns:
        Int: Nilai yang diinputkan
    """
    while True:
        num = input(title)
        try:
            num = int(num)
            if num >= minval and num <= maxval:
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

    # Menampilkan database
    show(database)

def delete(database):
    """Fungsi untuk menghapus data dari database

    Args:
        database (list): Data persediaan buah
    """
    # Menampilkan database
    show(database)

    # Meminta user untuk input indeks buah yang akan dihapus
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

    # Memperbarui urutan indeks buah
    for id, buah in enumerate(database):
        if id != buah[0]:
            database[id][0] = id

    # Menampilkan database
    show(database)

def buy(database):
    # Menyalin database ke dalam penyimpanan sementara
    databaseTemp = database.copy()
    
    # Definisi variabel untuk menyimpan belanjaan
    keranjang = []

    # Proses pembelian
    reorder = None
    while reorder != 'No':
        # Menampilkan database
        show(databaseTemp)

        # Meminta input untuk indeks dan jumlah buah yang ingin dibeli
        id = integer_validation(
            title='Silahkan masukkan indeks buah: ',
            minval=0,
            maxval=len(databaseTemp)-1
            )
        stock = integer_validation(
            title='Silahkan masukkan jumlah buah: ',
            minval=0,
            maxval=databaseTemp[id][2]
            )
        
        # Menambahkan ke dalam keranjang belanja
        keranjang.append([databaseTemp[id][1], stock, databaseTemp[id][3]])

        # Menampilkan keranjang belanja
        show(database=keranjang, header=['Nama', 'Qty', 'Harga'])

        # Konfirmasi reorder
        while True:
            status = string_validation('Mau beli yang lain?: ').lower()
            if status in ['yes', 'y', 'ya']:
                reorder = 'Yes'
            elif status in ['no', 'n', 'tidak']:
                reorder = 'No'
            break

        # Update stock sementara
        databaseTemp[id][2] -= stock

    # Menghitung total harga
    total = 0
    for id, item in enumerate(keranjang):
        # Hitung total harga per buah
        totalHargaBuah = item[1] * item[2]

        # Input total harga ke keranjang
        keranjang[id].append(totalHargaBuah)

        # Sum seluruh harga
        total += totalHargaBuah

    # Menampilkan keranjang belanja
    show(database=keranjang, header=['Nama', 'Qty', 'Harga', 'Total Harga'])

    # Menampilkan uang yang harus dibayar
    print(f'Uang yang harus Anda bayarkan adalah Rp.{total}')

    # Proses pembayaran
    pembayaran(total)

    # Update database
    database = databaseTemp.copy()

def pembayaran(totalHarga):
    while True:
        # Input jumlah uang
        bayar = int(input('Silahkan masukkan uang Anda: '))

        # Hitung selisih antara bayar dengan total
        selisih = totalHarga - bayar

        # Bandingkan antara uang dengan total harga
        if selisih > 0: 
            print(f'Uang Anda kurang sebesar Rp.{selisih}')
            continue
        
        # Ucapkan terima kasih ketika selesai pembayaran
        else:
            print(f'''Terimakasih. Uang kembalian Anda: {abs(selisih)}''')
            break