import datetime as dt

print("---Program mencari usia anda sekarang---")
tanggal = int(input("Masukkan tanggal \t: "))
bulan = int(input("Masukkan  \t\t: "))
tahun = int(input("Masukkan tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir kamu adalah {tanggal_lahir}")
print(f"Hari-nya adalah {tanggal_lahir:%A}")
print(f"Bulan-nya adalah {tanggal_lahir:%B}")


hari_ini = dt.date.today()
print("Hari ini tanggal:", hari_ini)

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Umur anda sekarang: {umur_tahun} tahun, {umur_bulan_sisa} bulan")
