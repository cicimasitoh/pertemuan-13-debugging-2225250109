# Pertemuan 13 Debugging dan Testing
Nama: Cici Masitoh
NIM: 2225250109
Kelas: 3B

## Kasus
Melakukan investigasi, identifikasi, dan perbaikan bug logika (logical error) pada program pengolahan data nilai mahasiswa yang mencakup fungsi perhitungan rata-rata, penentuan status kelulusan, dan pencarian nilai tertinggi.

## Test Case
| ID | Target | Input | Expected | Actual Awal | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| T1 | rata-rata | `[80, 60, 90, 70]` | `75.0` | `60.0` | PASS |
| T2 | rata-rata | `[100, 80]` | `90.0` | `36.0` | PASS |
| T3 | status | `60` | `Lulus` | `Tidak lulus` | PASS |
| T4 | status | `59` | `Tidak lulus` | `Tidak lulus` | PASS |
| T5 | tertinggi | `[80, 60, 90, 70]` | `90` | `0` | PASS |

## Bug Report
1. **Bug Rata-rata**: Pembagi menggunakan angka statis `5` alih-alih panjang data `len(nilai)`. Perbaikan: Mengganti pembagi dengan `len(nilai)`[cite: 41, 46].
2. **Bug Status Kelulusan**: Menggunakan operator `> 60` sehingga nilai `60` persis gagal lulus. Perbaikan: Mengubah operator menjadi `>= 60`[cite: 40, 42, 46].
3. **Bug Nilai Tertinggi**: Inisialisasi awal `0` dengan kondisi `x < tertinggi` menyebabkan hasil salah. Perbaikan: Menginisialisasi dengan elemen pertama list dan mengubah arah operator perbandingan menjadi `>`[cite: 42, 46, 47].

## Retest
Seluruh test case (T1 sampai T5) dijalankan ulang setelah perbaikan dan memberikan status **PASS** tanpa adanya regresi pada bagian program lainnya[cite: 46].

## Cara Menjalankan
```bash
python3 praktik/praktik_4_debugging.py