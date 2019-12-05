def argumentWajib(param1):
    "Fungsi ini merupakan contoh dari Required Argument. Fungsi yang wajib memiliki parameter saat pemanggilannya !"
    print(str)
    return


def main():
    "Fungsi utama"
    # Memanggil fungsi argumentWajib
    # argumentWajib()  # Akan menampilkan pesan error
    argumentWajib(10)


if __name__ == '__main__':
    main()
