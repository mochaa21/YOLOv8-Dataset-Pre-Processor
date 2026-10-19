# author: Aby Ashera

import datetime

file_kotor = ["jalan_aspal1.jpg", "laporan_kwu.pdf", "lubang_besar.jpg", "virus.exe", "retak_rambut.jpg", "catatan.txt"]
file_bersih = [i for i in file_kotor if i.endswith(".jpg")]
print((f"[{datetime.datetime.now()}] - Pembersihan Direktori Selesai.."))
print(f"Dataset YOLOv8 Siap: {file_bersih}")