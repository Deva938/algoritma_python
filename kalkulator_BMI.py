berat = int(input("Masukan Berat badan: "))
tinggi = float(input("Masukan Tinggi Badan: "))
bmi = berat / tinggi;

if bmi > 30: 
    kategori = "obesitas (konsultasi dokter)"
elif bmi >= 25:
    kategori = "gemuk (perlu olahraga lebih)"
elif bmi >= 18.5:
    kategori = "normal (pertahankan gaya hidup sehat)"
else:
    kategori = "kurus (Perlu tambah berat badan)" 

print("BMI :", bmi)
print("Kategori :", kategori)