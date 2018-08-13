import math
import os
# Python 3
# Gausah pake acara Recode Recode segala ya Kontol

W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray

def banner():
	print (G+'[$]'+B+'==========================='+G+'[$]')
	print ('[$]'+B+'==//     '+C+'Math Tool'+B+'     //=='+G+'[$]')
	print ('[$]'+B+'==// '+C+'For Orang" '+R+'Goblok'+B+' //=='+G+'[$]')
	print ('[$]'+B+'==========================='+G+'[$]')
	print ('[$]'+B+'==// '+C+'By >> '+O+'N1ght.Hax0r '+B+'//=='+G+'[$]')
	print ('[$]'+B+'==// '+C+'FB >> '+O+'Putra AR    '+B+'//=='+G+'[$]')
	print ('[$]'+B+'==========================='+G+'[$]')


def prima():
    num = int(input("[?]==// Masukkan bilangan\n[+]==>> "))
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print("[*]==// Angka >>",num,"\n[!]==// bukan bilangan prima")
                print("[*]==// Karena",i,"dikali",num//i,"=",num)
                break
        else:
            print("[*]==// Angka >>",num,"\n[!]==// adalah bilangan prima")

    else:
        print("[*]==// Angka >>",num, "\n[!]==// bukan bilangan prima")

def fakt(x):
    
    print ("\n[!]==// Faktor dari", x, "adalah:")
    for i in range(1, x+1):
        if x % i == 0:
            print ("[*]==>>", i)

def faktor():
    num = int(input("[?]==// Masukkan bilangan\n[+]==>> "))
    fakt(num)

def mean():
    data = str(input('[?]==// Masukan data\n[+]==>> '))
    a = str(round(sum(data) / len(data), 2))
    print("[!]==// Mean >>", a)

def median():
    data = str(input('[?]==// Masukan data\n[+]==>> '))
    data.sort()
    if len(data) % 2 == 0:
        a = int(len(data) / 2)
        b = (data[a - 1] + data[a]) / 2
        median = str(b)

    else:
        a = int((len(data) + 1) / 2)
        median = str(data[a - 1])
        
    print("[!]==// Median >>", median)

def modus():
    data = str(input('[?]==// Masukan data\n[+]==>> '))
    modus = max(set(data), key=data.count)
    a = data.count(modus)
    b = []
    for i in data:
        if a - 1 < data.count(i):
            b.append(i)
    c = b[::a]
    modus1 = 'Modus data adalah '
    modus2 = []
    if len(c) == 1:
        modus1 += str(c[0])
    else:
        for i in c:
            modus2.append(str(i))
        modus1 += ' & '.join(modus2)
    
    print("[!]==// Modus >>",modus)

def keliling_persegi () :
    x= float(input('[?]==// panjang sisi >> '))
    keliling = 4*x
    print (' ' )
    print ('[*]==// Keliling >> ' , keliling , 'cm')
    
def luas_kubik () :
	x=float(input('[?]==// panjang sisi >> '))
	luas= 6*x*x
	print (' ' )
	print ('[*]==// Luas >> ' , luas , 'cm2')
    
def keliling_persegipanjang () :
    x= float(input('[?]==// panjang >> '))
    y= float(input('[?]==// lebar >> '))
    keliling = 2*(x+y)
    print (' ' )
    print ('[*]==// Keliling >> ' , keliling , 'cm')
    
def luas_balok () :
	x= float(input('[?]==// panjang >> '))
	y= float(input('[?]==// lebar >> '))
	z= float(input('[?]==// tinggi >> '))
	luas= 2*((x*y)+(x*z)+(y*z))
	print (' ' )
	print ('[*]==// Luas >> ' , luas , 'cm2')
    
def volume_limas () :
	x= float(input('[?]==// luas alas >> '))
	y= float(input('[?]==// tinggi >> '))
	volume = 1/3*x*y
	print (' ' )
	print ('[*]==// Volume >> ' , volume , 'cm3')
	
def keliling_segitiga () :
    ab= float(input('[?]==// AB >> '))
    bc= float(input('[?]==// BC >> '))
    ca= float(input('[?]==// CA >> '))
    print (' ' )
    print ('[*]==// Keliling >> ' , keliling , 'cm')
    


def luas_bola () :
	x = float(input('[?]==// jari jari >> '))
	luas = 4*22/7*x*x
	print ('')
	print ('[*]==// Luas >> ' , luas , 'cm2')
              
def keliling_jajargenjang () :
    ab= float(input('[?]==// AB >> '))
    bc= float(input('[?]==// BC >> '))
    cd= float(input('[?]==// CD >> '))
    da= float(input('[?]==// DA >> '))
    keliling = ab+bc+cd+da
    print ('')
    print ('[*]==// Keliling >> ' , keliling , 'cm')

def keliling_trapesium () :
    ab= float(input('[?]==// AB >> '))
    bc= float(input('[?]==// BC >> '))
    cd= float(input('[?]==// CD >> '))
    da= float(input('[?]==// DA >> '))
    keliling = ab+bc+cd+da
    print ('')
    print ('[*]==// Keliling >> ' , keliling , 'cm')
             
def keliling_ketupat () :
    z= float(input('[?]==// sisi >> '))
    keliling = 4*z
    print ('')
    print ('[*]==// Keliling >> ' , keliling , 'cm')
    
def keliling_layang () :
	ab= float(input('[?]==// AB >> '))
	bc= float(input('[?]==// BC >> '))
	keliling = 2*(ab+bc)
	print (' ' )
	print ('[*]==// Keliling >> ' , keliling , 'cm')


def luas_persegi () :
    x= float(input('[?]==// panjang sisi >> '))
    luas= x*x
    print (' ' )
    print ('[*]==// Luas >> ' , luas , 'cm2')
    
def volume_kubik () :
    x=float(input('[?]==// panjang sisi >> '))
    volume= x*x*x
    print (' ' )
    print ('[*]==// Volume >> ' , volume , 'cm3')
    
def luas_persegipanjang () :
    x= float(input('[?]==// panjang >> '))
    y= float(input('[?]==// lebar >> '))
    luas= x*y
    print (' ' )
    print ('[*]==// Luas >> ' , luas , 'cm2')
    
def volume_balok () :
    x= float(input('[?]==// panjang >> '))
    y= float(input('[?]==// lebar >> '))
    z= float(input('[?]==// tinggi >> '))
    volume= x*y*z
    print (' ' )
    print ('[*]==// Volume >> ' , volume , 'cm3')
    
def luas_segitiga () :
    x= float(input('[?]==// alas >> '))
    y= float(input('[?]==// tinggi >> '))
    luas=0.5*x*y
    print (' ' )
    print ('[*]==// Luas >> ' , luas , 'cm2')

def luas_lingkaran () :
    x = float(input('[?]==// jari jari >> '))
    luas = 22/7*x*x
    print ('')
    print ('[*]==// Luas >> ' , luas , 'cm2')

def volume_bola () :
    x = float(input('[?]==// jari jari >> '))
    volume = 4/3*22/7*x*x*x
    print ('')
    print ('[*]==// Volume >> ' , volume , 'cm3')
              
def luas_jajargenjang () :
    x= float(input('[?]==// tinggi >> '))
    y= float(input('[?]==// alas >> '))
    luas = x*y
    print ('')
    print ('[*]==// Luas >> ' , luas , 'cm2')

def luas_trapesium () :
    x= float(input('[?]==// sisi atas >> '))
    y= float(input('[?]==// sisi bawah >> '))
    z= float(input('[?]==// tinggi >> '))
    luas = (x+y)*z/2
    print ('')
    print ('[*]==// Luas >> ' , luas, 'cm2')
             
def luas_ketupat () :
    x= float(input('[?]==// diagonal 1 >> '))
    y= float(input('[?]==// diagonal 2 >> '))
    luas = 0.5*x*y
    print ('')
    print ('[*]==// Luas >> ' , luas, 'cm2')
    
def luas_layang () :
    x= float(input('[?]==// diagonal 1 >> '))
    y= float(input('[?]==// diagonal 2 >> '))
    luas = 0.5*x*y
    print (' ' )
    print ('[*]==// Luas >> ' , luas , 'cm2')
	
def tanya_3M() :      
    fuck = int(input('''
[+]===========================[+]
[!]====// Bangun  Ruang //====[!]
[+]===========================[+]
[1]==//       Mean        //==[1]
[2]==//       Median      //==[2]
[3]==//       Modus       //==[3]
[+]===========================[+]

[?]==// What is your choice? >> '''))

    if fuck == 1 :
        mean()
    elif fuck == 2 :
        median()
    elif fuck == 3 :
        modus()
    else :
        banner()
def tanya_persegi():
    ans='0'
    ans=str(input('[?]==// Keliling / Luas / Volume (K/L/V)?'))
    if ans=='k'or ans=='K':
        keliling_persegi()
    
    elif ans=='l'or ans=='L':
        luas_persegi()

    elif ans=='v'or ans=='V':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_persegipanjang():
    ans='0'
    ans=str(input('[?]==// Keliling / Luas / Volume (K/L/V)?'))
    if ans=='k'or ans=='K':
        keliling_persegipanjang()
    
    elif ans=='l'or ans=='L':
        luas_persegipanjang()

    elif ans=='v'or ans=='V':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_layang():
    ans='0'
    ans=str(input('[?]==// Keliling / Luas / Volume (K/L/V)?'))
    if ans=='k'or ans=='K':
        keliling_layang()
    
    elif ans=='l'or ans=='L':
        luas_layang()

    elif ans=='v'or ans=='V':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_ketupat():
    ans='0'
    ans=str(input('[?]==// Keliling / Luas / Volume (K/L/V)?'))
    if ans=='k'or ans=='K':
        keliling_ketupat()
    
    elif ans=='l'or ans=='L':
        luas_ketupat()

    elif ans=='v'or ans=='V':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_trapesium():
    ans='0'
    ans=str(input('[?]==// Keliling / Luas / Volume (K/L/V)?'))
    if ans=='k'or ans=='K':
        keliling_trapesium()
    
    elif ans=='l'or ans=='L':
        luas_trapesium()

    elif ans=='v'or ans=='V':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_jajargenjang():
    ans='0'
    ans=str(input('[?]==// Keliling / Luas / Volume (K/L/V)?'))
    if ans=='k'or ans=='K':
        keliling_jajargenjang()
    
    elif ans=='l'or ans=='L':
        luas_jajargenjang()

    elif ans=='v'or ans=='V':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_segitiga():
    ans='0'
    ans=str(input('[?]==// Keliling / Luas / Volume (K/L/V)?'))
    if ans=='k'or ans=='K':
        keliling_segitiga()
    
    elif ans=='l'or ans=='L':
        luas_segitiga()

    elif ans=='v'or ans=='V':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_lingkaran():
    ans='0'
    ans=str(input('[?]==// Keliling / Luas / Volume (K/L/V)?'))
    if ans=='k'or ans=='K':
        pilbangundatar()
    
    elif ans=='l'or ans=='L':
        luas_lingkaran()

    elif ans=='v'or ans=='V':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_bola():
    ans='0'
    ans=str(input('[?]==// Keliling / Luas / Volume (K/L/V)?'))
    if ans=='k'or ans=='K':
        pilbangunruang()
    
    elif ans=='l'or ans=='L':
        luas_bola()

    elif ans=='v'or ans=='V':
        volume_bola()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_balok():
    ans='0'
    ans=str(input('[?]==// Keliling / Luas / Volume (K/L/V)?'))
    if ans=='k'or ans=='K':
        pilbangunruang()
    
    elif ans=='l'or ans=='L':
        luas_balok()

    elif ans=='v'or ans=='V':
        volume_balok()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_kubik():
    ans='0'
    ans=str(input('[?]==// Keliling / Luas / Volume (K/L/V)?'))
    if ans=='k'or ans=='K':
        pilbangunruang()
    
    elif ans=='l'or ans=='L':
        luas_kubik()

    elif ans=='v'or ans=='V':
        volume_kubik()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_limas():
    ans='0'
    ans=str(input('[?]==// Keliling / Luas / Volume (K/L/V)?'))
    if ans=='k'or ans=='K':
        pilbangunruang()
    
    elif ans=='l'or ans=='L':
        pilbangunruang()

    elif ans=='v'or ans=='V':
        volume_limas()      
    else:
        print ('[!]==// Abort')
        exit()

def pilbangundatar() :		
    fuck = int(input('''
[+]===========================[+]
[!]====// Bangun  Datar //====[!]
[+]===========================[+]
[1]==//      persegi      //==[1]
[2]==//  persegi panjang  //==[2]
[3]==//     segi tiga     //==[3]
[4]==//     lingkaran     //==[4]
[5]==//   jajar genjang   //==[5]
[6]==//     trapesium     //==[6]
[7]==//   belah ketupat   //==[7]
[8]==//   layang layang   //==[8]
[+]===========================[+]

[?]==// What is your choice? >> '''))

    if fuck == 1 :
        tanya_persegi()
    elif fuck == 2 :
        tanya_persegipanjang()
    elif fuck == 3 :
        tanya_segitiga()
    elif fuck == 4 :
        tanya_lingkaran()
    elif fuck == 5 :
        tanya_jajargenjang()
    elif fuck == 6 :
        tanya_trapesium()
    elif fuck == 7 :
        tanya_ketupat()
    elif fuck == 8 :
        tanya_layang()
    else :
        banner()
def pilbangunruang() :      
    fuck = int(input('''
[+]===========================[+]
[!]====// Bangun  Ruang //====[!]
[+]===========================[+]
[1]==//       kubik       //==[1]
[2]==//       balok       //==[2]
[3]==//       limas       //==[3]
[4]==//        bola       //==[4]
[+]===========================[+]

[?]==// What is your choice? >> '''))

    if fuck == 1 :
        tanya_kubik()
    elif fuck == 2 :
        tanya_balok()
    elif fuck == 3 :
        tanya_limas()
    elif fuck == 4 :
        tanya_bola()
    else :
        banner()

def menu() :
    fuck = int(input('''
[+]===========================[+]
[!]====//     Menu      //====[!]
[+]===========================[+]
[1]==//   Bangun  Datar   //==[1]
[2]==//   Bangun  Ruang   //==[2]
[3]==//       Prima       //==[3]
[4]==//      Faktor       //==[4]
[5]==// Mean/Median/Modus //==[5]
[+]===========================[+]

[?]==// What is your choice? >> '''))

    if fuck == 1 :
        pilbangundatar()
    elif fuck == 2 :
        pilbangunruang()
    elif fuck == 3 :
        prima()
    elif fuck == 4 :
        faktor()
    elif fuck == 5 :
        tanya_3M()
    else :
        banner()
banner()
menu()
