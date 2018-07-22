import math
# Gausah pake acara Recode Recode segala ya Kontol

def square () :
    x= float(input('[?]==// panjang sisi >> '))
    luas= x*x
    print (' ' )
    print ('[*]==// Luas >> ' , luas , 'cm2')
    
def cubic () :
	x=float(input('[?]==// panjang sisi >> '))
	luas= x*x
	print (' ' )
	print ('[*]==// Luas >> ' , luas , 'cm3')
    
def rectangle () :
    x= float(input('[?]==// panjang >> '))
    y= float(input('[?]==// lebar >> '))
    luas= x*y
    print (' ' )
    print ('[*]==// Luas >> ' , luas , 'cm2')
    
def balok () :
	x= float(input('[?]==// panjang >> '))
	y= float(input('[?]==// lebar >> '))
	z= float(input('[?]==// tinggi >> '))
	luas= x*y*z
	print (' ' )
	print ('[*]==// Luas >> ' , luas , 'cm3')
    
def triangle () :
    x= float(input('[?]==// alas >> '))
    y= float(input('[?]==// tinggi >> '))
    luas=0.5*x*y
    print (' ' )
    print ('[*]==// Luas >> ' , luas , 'cm2')
    
def circle () :
    x = float(input('[?]==// jari jari >> '))
    luas = 22/7*x*x
    print ('')
    print ('[*]==// Luas >> ' , luas , 'cm2')
              
def jajargenjang () :
    x= float(input('[?]==// tinggi >> '))
    y= float(input('[?]==// alas >> '))
    luas = x*y
    print ('')
    print ('[*]==// Luas >> ' , luas , 'cm2')

def trapesium () :
    x= float(input('[?]==// sisi atas >> '))
    y= float(input('[?]==// sisi bawah >> '))
    z= float(input('[?]==// tinggi >> '))
    luas = (x+y)*z/2
    print ('')
    print ('[*]==// Luas >> ' , luas, 'cm2')
             
def ketupat () :
    x= float(input('[?]==// diagonal 1 >> '))
    y= float(input('[?]==// diagonal 2 >> '))
    luas = 0.5*x*y
    print ('')
    print ('[*]==// Luas >> ' , luas, 'cm2')
    
def layang () :
	x= float(input('[?]==// diagonal 1 >> '))
	y= float(input('[?]==// diagonal 2 >> '))
	luas = 0.5*x*y
	print (' ' )
	print ('[*]==// Luas >> ' , luas , 'cm2')
    
         
pil = int(input('[+]===========================[+] \n[!]====//  Choose this  //====[!] \n[+]===========================[+] \n[1]==//      persegi      //==[1]\n[2]==//       kubik       //==[2]\n[3]==//  persegi panjang  //==[3]\n[4]==//       balok       //==[4]\n[5]==//     segi tiga     //==[5]\n[6]==//     lingkaran     //==[6]\n[7]==//   jajar genjang   //==[7]\n[8]==//     trapesium     //==[8]\n[9]==//   belah ketupat   //==[9]\n[10]==//  layang layang  //==[10]\n[+]===========================[+] \n\n[?]==// What is your choice? >> '))
if pil == 1 :
    square()
    
elif pil==2 :
	cubic()
    
elif pil==3 :
    rectangle()
    
elif pil==4 :
	balok()
    
elif pil==5:
    triangle()

elif pil==6 :
    circle()

elif pil ==7 :
    jajargenjang()

elif pil== 8 :
    trapesium()

elif pil== 9 :
    ketupat()
    
elif pil==10 :
	layang()
	
else :
    print (' ' )
    print ('[!]==// Yang Bener Dong Goblok')
