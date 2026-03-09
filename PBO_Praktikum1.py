data = {
    "rekam_medis": [
        {"id": 1, "bpm": 70}, {"id": 2, "bpm": 110}, {"id": 3, "bpm": 65},
        {"id": 4, "bpm": 120}, {"id": 5, "bpm": 80}, {"id": 6, "bpm": 140}, {"id": 7, "bpm": 75}
    ]
}

def kondisi_jantung(nilai): 
    if nilai > 100: 
        return "Peringatan: Takikardia (Detak Tinggi)" 
    else :
        return "Kondisi: Normal" 

x = 1
for i in data["rekam_medis"]:
    nilai_bpm = i["bpm"]
    status = kondisi_jantung(nilai_bpm)
    print(f"Data ke-{x}: {nilai_bpm} BPM -> {status}")
    x += 1