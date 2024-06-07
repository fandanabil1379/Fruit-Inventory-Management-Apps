def inputBuah(nama, stock, harga):
    """Fungsi meminta user untuk input jumlah buah 
    dan menghitung harganya.

    Args:
        nama (String): Nama buah yang akan dibeli
        stock (Integer): Stock buah yang akan dibeli
        harga (Integer): Harga buah per kg

    Returns:
        nBuah (Integer): Jumlah buah yang dipesan 
        hargaBuah (Integer): Total harga buah
    """
    while True:
        # Input jumlah buah
        nBuah = int(input(f'Masukkan jumlah {nama}: '))

        # Membandingkan antara jumlah permintaan dengan stock
        if nBuah > stock:
            print(f'Jumlah terlalu banyak, stock tersisa {stock} buah')
            continue

        # Berhenti minta input, ketika jumlah permintaan terpenuhi
        break

    # Hitung total harga untuk buah tersebut
    hargaBuah = nBuah * harga

    return nBuah, hargaBuah