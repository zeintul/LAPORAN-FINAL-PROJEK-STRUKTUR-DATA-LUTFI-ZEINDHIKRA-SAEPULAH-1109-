import csv
import os
from datetime import datetime

datacsv = "keuangan.csv"

if not os.path.exists(datacsv):
    with open(datacsv, "w", newline="") as f:
        tulis = csv.writer(f)
        tulis.writerow(["ID", "Tanggal", "Tipe", "Kategori", "Nominal", "Catatan"])

def tulis():
    with open(datacsv, "a", newline="") as f:
        tulis = csv.writer(f)
        idbaru = sum(1 for _ in open(datacsv))
        tanggal = datetime.now().strftime("%d-%m-%Y")
        tipe = input("Tipe (Pemasukan/Pengeluaran): ")
        kategori = input("Kategori: ")
        nominal = input("Nominal: ")
        catatan = input("Catatan: ")
        tulis.writerow([idbaru, tanggal, tipe, kategori, nominal, catatan])
        print("✅ Data masuk!")

def hapus():
    idhapus = input("ID yang mau dihapus: ")
    semuadata = []
    with open(datacsv, "r") as f:
        baca = csv.reader(f)
        semuadata = [baris for baris in baca if baris[0] != idhapus or baris[0] == "ID"]
    with open(datacsv, "w", newline="") as f:
        tulis = csv.writer(f)
        tulis.writerows(semuadata)
    print("🗑️ Data dihapus.")

def ubah():
    idubah = input("ID yang mau diubah: ")
    semuadata = []
    with open(datacsv, "r") as f:
        baca = csv.reader(f)
        for baris in baca:
            if baris[0] == idubah and baris[0] != "ID":
                print("📝 Tekan ENTER kalo gak mau ubah.")
                baris[1] = datetime.now().strftime("%d-%m-%Y")
                baris[2] = input(f"Tipe [{baris[2]}]: ") or baris[2]
                baris[3] = input(f"Kategori [{baris[3]}]: ") or baris[3]
                baris[4] = input(f"Nominal [{baris[4]}]: ") or baris[4]
                baris[5] = input(f"Catatan [{baris[5]}]: ") or baris[5]
            semuadata.append(baris)
    with open(datacsv, "w", newline="") as f:
        tulis = csv.writer(f)
        tulis.writerows(semuadata)
    print("✅ Data diubah.")

def lihat():
    pemasukan = 0
    pengeluaran = 0

    with open(datacsv, "r") as f:
        baca = csv.reader(f)
        header = next(baca)
        kosong = True

        print("\n=== DATA TRANSAKSI ===")
        print(f"{header[0]:<5} {header[1]:<12} {header[2]:<12} {header[3]:<12} {header[4]:<10} {header[5]}")
        print("-" * 60)

        for baris in baca:
            print(f"{baris[0]:<5} {baris[1]:<12} {baris[2]:<12} {baris[3]:<12} {baris[4]:<10} {baris[5]}")
            kosong = False
            try:
                nominal = int(baris[4])
                if baris[2].lower() == "pemasukan":
                    pemasukan += nominal
                elif baris[2].lower() == "pengeluaran":
                    pengeluaran += nominal
            except:
                pass

    if kosong:
        print("📭 Belum ada catatan.")
    else:
        sisa = pemasukan - pengeluaran
        print("\n=== RINGKASAN ===")
        print(f"Total Pemasukan   : Rp {pemasukan}")
        print(f"Total Pengeluaran : Rp {pengeluaran}")
        print(f"Sisa Uang         : Rp {sisa}")

def rekapperkategori():
    kategori_map = {}
    with open(datacsv, "r") as f:
        baca = csv.reader(f)
        next(baca)
        for baris in baca:
            kategori = baris[3]
            try:
                nominal = int(baris[4])
            except:
                continue
            if kategori not in kategori_map:
                kategori_map[kategori] = 0
            kategori_map[kategori] += nominal
    print("\n=== REKAP KATEGORI ===")
    for kategori, total in kategori_map.items():
        print(f"{kategori:<15} : Rp {total}")

def menu():
    while True:
        print("\n=== MENU KEUANGAN ===")
        print("1. Tulis")
        print("2. Hapus")
        print("3. Ubah")
        print("4. Lihat")
        print("5. Rekap per Kategori")
        print("6. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1": tulis()
        elif pilih == "2": hapus()
        elif pilih == "3": ubah()
        elif pilih == "4": lihat()
        elif pilih == "6":
            print("👋 Sampai jumpa bro!")
            break
        elif pilih == "5": rekapperkategori()
        else:
            print("❌ Pilihan gak valid")

menu()
