# Sistem Monitoring Kesehatan Sederhana 🩺

Repositori ini berisi kode tugas praktikum Pemrograman Berorientasi Objek (OOP) menggunakan bahasa Python. Program ini merupakan simulasi sederhana untuk menganalisis dan mengevaluasi data rekam medis detak jantung (BPM) pasien secara otomatis.

## 🚀 Deskripsi Project

Program ini membaca kumpulan data rekam medis dari struktur data *Dictionary* (format menyerupai JSON), lalu mengevaluasi setiap nilai detak jantung (BPM) menggunakan sebuah fungsi khusus. Jika nilai BPM di atas 100, program akan memberikan status peringatan **Takikardia**. Jika tidak, statusnya adalah **Normal**.

## 🧠 Konsep yang Diterapkan

* **Struktur Data (Dictionary & List):** Mengelola kumpulan data secara rapi menggunakan *key* dan *value*.
* **Modularisasi (Function):** Membungkus logika pengecekan kesehatan ke dalam fungsi `kondisi_jantung()` agar *reusable* (bisa digunakan berulang kali).
* **Iterasi (Looping):** Menggunakan perulangan `for` untuk menyisir dan memproses data masif secara efisien.
* **F-String Formatting:** Menyusun *output* teks dan variabel secara dinamis agar lebih mudah dibaca.

## 💻 Teknologi

* **Bahasa Pemrograman:** Python 3.x

## 📋 Cara Menjalankan Program

1.  Pastikan Python sudah terinstal di perangkatmu.
2.  *Clone* repositori ini atau *download* file Python-nya (misalnya bernama `main.py`).
3.  Buka terminal/CMD di dalam folder project.
4.  Jalankan perintah berikut:
    ```bash
    python main.py
    ```

## 📊 Contoh Output

Ketika program dijalankan, hasil analisis yang ditampilkan di terminal akan tampak seperti ini:

```text
Data ke-1: 70 BPM -> Kondisi: Normal
Data ke-2: 110 BPM -> Peringatan: Takikardia (Detak Tinggi)
Data ke-3: 65 BPM -> Kondisi: Normal
Data ke-4: 120 BPM -> Peringatan: Takikardia (Detak Tinggi)
Data ke-5: 80 BPM -> Kondisi: Normal
Data ke-6: 140 BPM -> Peringatan: Takikardia (Detak Tinggi)
Data ke-7: 75 BPM -> Kondisi: Normal
