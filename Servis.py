OgrenciSayisi = 1000

KoltukSayisi = 26

ServisSayisi = OgrenciSayisi//KoltukSayisi
KalanOgrenciSayisi = OgrenciSayisi%KoltukSayisi

BosKoltuk = 26-KalanOgrenciSayisi

if KalanOgrenciSayisi>0 and KalanOgrenciSayisi<=KoltukSayisi:
   ServisSayisi=ServisSayisi+1
  

print("Servis Sayısı: ",ServisSayisi)
print(f"Tüm servis araçları dolmadı, {BosKoltuk} kadar boş koltuk mevcut")
   