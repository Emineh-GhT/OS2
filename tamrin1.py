import math

i=1
a=1
while i>0:
    if int(a)==0:
        t = input("\n\n**********\n\n aya edame midahid? ( Ble = b | kheir = n) : ")
        if t== 'b':
            a=1
        elif t== 'n' :
            a=0
            break

    if int(a)==1:
        print("\n *** mashin hesab ***\n")
        print("""
        1.tafriq
        2.jam
        3.taqsim
        4.zarb
        5.radikal
        6.sinus
        7.cosinus
        8.tanzhant
        9.cotanzhant
        10.logaritm
        """)

    n = input("che amali anjam bedam ? ")
    a=0
        
    if int(n)==1:
        x=input("avalin adad : ")
        y=input("dovomin adad : ")
        z=int (x) - int (y)
        print("tafriq = ", z)
        
    if int(n)==2:
        x=input("avalin adad : ")
        y=input("dovomin adad : ")
        z=int (x) + int (y)
        print("jam = ", z)

    if int(n)==3:
        x=input("avalin adad : ")
        y=input("dovomin adad : ")
        z=int (x) / int (y)
        print("taqsim = ", z)    

    if int(n)==4:
        x=input("avalin adad : ")
        y=input("dovomin adad : ")
        z=int (x) * int (y)
        print("zarb = ", z) 
        
        
    if int(n)==5:
        x=input("adad ra vared konid : ")
        z=int (x)**(1/2)
        print("radical = ", z) 
        


    if int(n)==6:
        x=int(input("daraje : "))
        math.radians=x/360 *2 *math.pi
        z=math.sin (math.radians)
        print("sinus = ", float(z))
        

    if int(n)==7:
        x=int(input("daraje : "))
        math.radians=x/360 *2 *math.pi
        z=math.cos (math.radians)
        print("cosinus = ", float(z))   
        

    if int(n)==8:
        x=int(input("daraje : "))
        math.radians=x/360 *2 *math.pi
        z=math.tan (math.radians)
        print("tanzhant = ", float(z))
        

    if int(n)==9:
        x=int(input("daraje : "))
        math.radians=x/360 *2 *math.pi
        z=math.atan (math.radians)
        print("cotanzhant = ", float(z))
        


    if int(n)==10:
        x=int(input("adad ra vared konid : "))
        z=math.log(x)
        print("logaritm = ", z)  