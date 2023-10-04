print("Merhaba yarışmacı isminiz nedir?")
name=input()
print("Hoşgeldin " + name)
print("10 canın var yani 10 yanlış yapma hakkın eğer 10 tane yanlış yaparsan ölürsün ve oyun senin için biter yarışmacı")
dogrucevap="python"
can=10
tahmin_str=""

while can>0:

	kalanKelime=0

	for harf in dogrucevap:
		if harf in tahmin_str:
			print(harf)
		else:
			print("*")
			kalanKelime+=1
	if kalanKelime==0:
		print(f"USTA YARIŞMACI {name} OYUNU KAZANIYOR!!!")
		break

	tahmin=input("Bir harf tahmin ediniz: ")
	tahmin_str+=tahmin

	if tahmin not in dogrucevap:
		can-=1
		print(f"Olamaz {name} yanlış tahmin yaptı!")
		print(f"Geriye sadece {can} can kaldı")

		if can==0:
			print(name +" yolun sonuna geldi ve elendi")