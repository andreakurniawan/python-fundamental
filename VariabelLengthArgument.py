def vLengthArgument(*args):
    "Fungsi ini memiliki jumlah argument yang relatif tergantung dari banyak parameter yang dikirim saat proses pemanggilan fungsi."
    print(*args)
    return


def main():

    # Pemanggilan fungsi vLengthArgument() dengan 1 parameter
    vLengthArgument("Hai1")
    print("---")

    # Pemanggilan fungsi vlengthArgument() dengan 2 parameter
    vLengthArgument("Hai1", "Hai2")
    print("---")

    # Pemanggilan fungsi vLengthArgument() dengan 3 parameter
    vLengthArgument("Hai1", "Hai2", "Hai3")

    # dst


if __name__ == '__main__':
    main()
