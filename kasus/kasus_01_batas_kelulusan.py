def status_lulus(nilai):
    # Kasus bug batas (nilai 60 belum tentu lulus jika operator salah)
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"

print("Status 60:", status_lulus(60))