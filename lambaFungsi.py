"Anonymous Function"
jumlah = lambda nilai1, nilai2: nilai1 + nilai2
print("Jumlah = ", jumlah(10,10))

print("\n")


"Lingkup Variabel"
"Secara Umum lingkup variabel dibagi menjadi 2, yaitu variabel local (dalam suatu fungsi), dan variabel global (variabel yang disimpan di luar fungsi)"

nilai = 0   # variabel global

def angka(arg):
    # Gunakan keyword 'global' di depan variabel, untuk menjadikan variabel local menjadi variabel global.
    nilai = arg  # variabel local, terhadap fungsi angka()
    return nilai


var_local = angka(100)
print("variabel global :", nilai)
print("Variabel Lokal :", var_local)



