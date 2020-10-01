#no 1
print("NO 1")
print("menentukan rata-rata dari 5 variabel")
a=int(input("masukkan nilai ke-1 :" ))
b=int(input("masukkan nilai ke-2 :" ))
c=int(input("masukkan nilai ke-3 :" ))
d=int(input("masukkan nilai ke-4 :" ))
e=int(input("masukkan nilai ke-5 :" ))
x=((a+b+c+d+e)/5)
print("nilai rata-rata : ", x)

#no 2
print("")
print("NO 2")
print("luas dan keliling bangun datar")
print("silahkan memilih bangun datar : ")
print("1. persegi panjang")
print("2. lingkaran")
print("3. persegi")
plh=int(input("masukkan pilihan anda (masukkan angkanya saja): "))
if plh<=3:
    if plh==1:
        pjg=int(input("masukkan panjang  : "))
        lbr=int(input("masukkan lebar  : "))
        lpp=(pjg*lbr)
        kpp=(2*(pjg+lbr))
        print("luas = ", lpp, ",", "keliling = ", kpp)
    elif plh==2:
        jr=int(input("masukkan jari-jari : "))
        ll=(3.16*jr**2)
        kl=(2*3.14*jr)
        print("luas = ", ll, ",", "keliling = ", kl)
    elif plh==3:
        s=int(input("masukkan panjang sisi : "))
        lp=(s**2)
        kp=(4*s)
        print("luas = ", lp, ",", "keliling = ", kp)
else:
    print("inputan salah")

#no 3
print("")
print("NO 3")
print("mencari BMI dam pengelompokan BMI")
bb=float(input("masukkan berat badan anda : "))
tb=float(input("maukkan tinggi badang anda : "))
kv=(tb/100)
bmi=(bb/(kv*kv))
print("bmi anda = ", bmi)
if bmi<18.5 :
    print("berat badan kurang")
elif bmi<22.9 :
    print("berat badan normal")
elif bmi<29.9 :
    print("berat badan berlebih")
else:
    print("obesitas")

#no 4
print("")
print("NO 4")
print("mencari nilai maksimal dan minimal")
bil=[]
angka=int(input("masukkan bilangan : "))
bil.append(angka)
pil=str(input("ingin memasukkan bilangan lagi? [y/t]"))
while pil=="y":
    angka=int(input("masukkan bilangan : "))
    bil.append(angka)
    pil=str(input("ingin memasukkan bilangan lagi? [y/t]"))
print("bilangan yang dimasukkan = ", bil)
print("bilangan terbesar ialah : ", max(bil))
print("bilangan terkecil ialah : ", min(bil))

#no 5
print("")
print("NO 5")
print("validasi username dan password")
ul=0
while ul<3 :
    usr=str(input("masukkan username : "))
    pw=str(input("masukkan password : "))
    if usr=='admin' and pw=='password':
        print("anda berhasil masuk")
        break
    else:
        print("maaf username dan password anda salah")
    ul+=1
        
