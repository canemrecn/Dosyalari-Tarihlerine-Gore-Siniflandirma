import os
from datetime import datetime
def duzele():
# Kullanıcıdan düzenlenecek klasör adını alır
    klasor = input("Düzenlenecek Klasör: ")
    dosyalar = []
# Dosya listesini tutmak için boş bir liste oluşturulur
    tarihler = []
# Tarihleri tutmak için boş bir liste oluşturulur
    def list_dir():
# Klasördeki dosyaları listeler ve dosya listesine ekler
        for dosya in os.listdir(klasor):
            if os.path.isdir(os.path.join(klasor, dosya)):
                continue
# Klasörleri geçer, dosyalara odaklanır
            if dosya.startswith("."):
                continue
# Gizli dosyaları geçer
            else:
                dosyalar.append(dosya)
    list_dir()
# Dosya listesini oluşturur
    for dosya in dosyalar:
        tarih_damgasi = os.stat(os.path.join(klasor, dosya)).st_mtime
        tarih = datetime.fromtimestamp(tarih_damgasi).strftime("%d-%m-%Y")
        if tarih in tarihler:
            continue
# Aynı tarih zaten işlenmişse atlar
        else:
            os.mkdir(os.path.join(klasor, tarih))
# Yeni tarih klasörü oluşturur

    for dosya in dosyalar:
        tarih_damgasi = os.stat(os.path.join(klasor, dosya)).st_mtime
        tarih = datetime.fromtimestamp(tarih_damgasi).strftime("%d-%m-%Y")
        os.rename(os.path.join(klasor, dosya), os.path.join(klasor, tarih, dosya))
# Dosyaları yeni tarih klasörüne taşır
if __name__ == "__main__":
    duzele()
