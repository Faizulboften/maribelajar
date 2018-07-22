import math
# Gausah pake acara Recode Recode segala ya Kontol


def banner():
	print ('''
[$]===========================[$]
[$]==//     Math Tool     //==[$]
[$]==// For Orang" Goblok //==[$]
[$]===========================[$]
[$]==// By >> N1ght.Hax0r //==[$]
[$]==// FB >> Putra AR    //==[$]
[$]===========================[$]
''')
def persegi () :
    x= float(input('[?]==// panjang sisi >> '))
    keliling = 4*x
    luas= x*x
    print (' ' )
    print '[*]==// Keliling >> ' , keliling , 'cm'
    print '[*]==// Luas >> ' , luas , 'cm2'
    
def kubik () :
	x=float(input('[?]==// panjang sisi >> '))
	luas= 6*x*x
	volume= x*x*x
	print (' ' )
	print '[*]==// Luas >> ' , luas , 'cm2'
	print '[*]==// Volume >> ' , volume , 'cm3'
    
def persegipanjang () :
    x= float(input('[?]==// panjang >> '))
    y= float(input('[?]==// lebar >> '))
    keliling = 2*(x+y)
    luas= x*y
    print (' ' )
    print '[*]==// Keliling >> ' , keliling , 'cm'
    print '[*]==// Luas >> ' , luas , 'cm2'
    
def balok () :
	x= float(input('[?]==// panjang >> '))
	y= float(input('[?]==// lebar >> '))
	z= float(input('[?]==// tinggi >> '))
	luas= 2((x*y)+(x*z)+(y*z))
	volume= x*y*z
	print (' ' )
	print '[*]==// Luas >> ' , luas , 'cm2'
	print '[*]==// Volume >> ' , volume , 'cm3'
    
def limas () :
	x= float(input('[?]==// luas alas >> '))
	y= float(input('[?]==// tinggi >> '))
	volume = 1/3*x*y
	print (' ' )
	print '[*]==// Volume >> ' , volume , 'cm3'
	
def segitiga () :
    ab= float(input('[?]==// AB >> '))
    bc= float(input('[?]==// BC >> '))
    ca= float(input('[?]==// CA >> '))
    x= float(input('[?]==// alas >> '))
    y= float(input('[?]==// tinggi >> '))
    keliling= ab+bc+ca
    luas=0.5*x*y
    print (' ' )
    print '[*]==// Keliling >> ' , keliling , 'cm'
    print '[*]==// Luas >> ' , luas , 'cm2'
    
def lingkaran () :
    x = float(input('[?]==// jari jari >> '))
    luas = 22/7*x*x
    print ('')
    print '[*]==// Luas >> ' , luas , 'cm2'

def bola () :
	x = float(input('[?]==// jari jari >> '))
	luas = 4*22/7*x*x
	volume = 4/3*22/7*x*x*x
	print ('')
	print '[*]==// Luas >> ' , luas , 'cm2'
	print '[*]==// Volume >> ' , volume , 'cm3'
              
def jajargenjang () :
    ab= float(input('[?]==// AB >> '))
    bc= float(input('[?]==// BC >> '))
    cd= float(input('[?]==// CD >> '))
    da= float(input('[?]==// DA >> '))
    x= float(input('[?]==// tinggi >> '))
    y= float(input('[?]==// alas >> '))
    keliling = ab+bc+cd+da
    luas = x*y
    print ('')
    print '[*]==// Keliling >> ' , keliling , 'cm'
    print '[*]==// Luas >> ' , luas , 'cm2'

def trapesium () :
    ab= float(input('[?]==// AB >> '))
    bc= float(input('[?]==// BC >> '))
    cd= float(input('[?]==// CD >> '))
    da= float(input('[?]==// DA >> '))
    x= float(input('[?]==// sisi atas >> '))
    y= float(input('[?]==// sisi bawah >> '))
    z= float(input('[?]==// tinggi >> '))
    keliling = ab+bc+cd+da
    luas = (x+y)*z/2
    print ('')
    print '[*]==// Keliling >> ' , keliling , 'cm'
    print '[*]==// Luas >> ' , luas, 'cm2'
             
def ketupat () :
    x= float(input('[?]==// diagonal 1 >> '))
    y= float(input('[?]==// diagonal 2 >> '))
    z= float(input('[?]==// sisi >> '))
    keliling = 4*z
    luas = 0.5*x*y
    print ('')
    print '[*]==// Keliling >> ' , keliling , 'cm'
    print '[*]==// Luas >> ' , luas, 'cm2'
    
def layang () :
	ab= float(input('[?]==// AB >> '))
	bc= float(input('[?]==// BC >> '))
	x= float(input('[?]==// diagonal 1 >> '))
	y= float(input('[?]==// diagonal 2 >> '))
	keliling = 2(ab+bc)
	luas = 0.5*x*y
	print (' ' )
	print '[*]==// Keliling >> ' , keliling , 'cm'
	print '[*]==// Luas >> ' , luas , 'cm2'
	
ans='Y'
ans=str(raw_input('[?]==// Apakah Gua Tampan (Y/N)?'))
if ans=='y'or ans=='Y':
    banner()
    
elif ans=='n'or ans=='N':
	print'[!]==// ASULO >:('
	exit()
      
else:
    print'[!]==// KENTOD'
    exit()
		
kontol = int(input('''
[+]===========================[+]
[!]====//  Tool Khusus  /
