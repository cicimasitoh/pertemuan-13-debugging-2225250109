def hitung_rata_rata(data):
    # Kasus bug logika pembagi statis
    total = sum(data)
    return total / 5

print("Rata-rata:", hitung_rata_rata([80, 90, 70]))