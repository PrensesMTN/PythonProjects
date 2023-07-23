print("""
    1400 yıl önce savaşmayı çok seven Krala SATRANÇ
        öğreten Yüce Bilge şunu talep eder;
 
 "Kralım sizden çok fazla şey istemem buğday verseniz
yeter. Bakın bu satranç tahtası 64 kare. Birinci kareye bir
buğday ikincisine 2, üçüncü kareye 4, dördüncü kareye 8
 ve sonrasında hep böyle iki misli olacak şekilde her kareyi
  doldurmaya yetecek kadar buğday yeter" demiş. 
""")

bugday=1 

for i in range(64):
    bugday=i*2
    print(i,"."," Gün için",bugday)


print(f"64. Günün sonunda {bugday} kadar bugday gerek.")