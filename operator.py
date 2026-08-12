# Contoh menggabungkan operator logika dan operator perbandingan
akhlak = 30
nilai = input("Masukkan nilai anda: ")
alpa = 5
izin = 10

# Menggunakan operator aritmatika
nilai_akhir = akhlak + int(nilai)
print("Nilai akhir anda adalah:", nilai_akhir)
jumlah_total = alpa + izin
print("Jumlah total alpa dan izin anda adalah:", jumlah_total)

#lulus jika nilai akhir lebih besar dari 70 dan jumlah total alpa dan izin lebih kecil dari 20
lulus = nilai_akhir >= 70 and jumlah_total < 20 or nilai_akhir >= 80 and jumlah_total < 30
print("Apakah anda lulus?", lulus)

