def keywordArgument(nama='', umur='', jk=''):
    "Fungsi yang mempunyai nilai default pada parameternya."
    print("Nama : ", nama)
    print("umur : ", umur)
    print("JK   : ", jk)
    return


def main():
    "Pemanggilan fungsi keywordArgument dengan nilai parameter default"
    print("Nilai Default dari fungsi")
    keywordArgument()

    print("==============")
    "Pemanggilan fungsi keywordArgument dengan menimpa nilai parameter defaultnya"
    "Saat pemanggilan fungsi keywordArgument(), posisi argument bisa tidak berurutan asalkan nama parameternya sama."
    print("Nilai baru yang dikirimkan sebagai parameter")
    keywordArgument(jk='L', nama='Andrea', umur='21')


if __name__ == '__main__':
    main()
