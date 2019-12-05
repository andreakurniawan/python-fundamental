def main():
    daftarIsi = [1, 2, 3, 4]
    print("List di luar fungsi : ", daftarIsi)

    rubahIsi(daftarIsi)


def rubahIsi(daftarIsi):
    daftarIsi = [10, 20, 30, 40]

    print("List di dalam fungsi : ", daftarIsi)
    return


if __name__ == '__main__':
    main()
