import random

e =['s','k','q']
bsh=0
bco=0

for i in range(5):
    print("\n  ***** entekhab konid  : s=sang | k=kaqaz | q=qeychi \n")
    sh =input()
    print(" shoma = ", sh )
    co =random.choice(e)
    print(" computer = ",co)

    if co in e and sh in e :
        if co==sh:
            print("barande nadarim... ")
            i+=1
        else :
            if sh=='s':
                i+=1
                if co=='k':
                 print("computer barande shod :( " ) 
                 bco+=1
                elif sh=='q':
                 print("tabrik barande shodid :) " )
                 bsh+=1
            elif sh=='q':
                i+=1
                if co=='k':
                 print(" tabrik barande shodid :) " )
                 bsh+=1
                elif co=='s':
                 print(" computer barande shod... " ) 
                 bco+=1   
            elif sh=='k':
                i+=1
                if co=='s':
                 print("tabrik barande shodid :)" ) 
                 bsh+=1
                elif co=='q':
                 print("computer barande shod... " ) 
                 bco+=1
print('\n tedad bord shoma :',bsh,'\n tedad bord computer :',bco)
if bsh > bco :
    print("\n shoma barande bazi shodid :) " ) 
elif bco < bsh :
    print("\n motasefam shoma barande nashodid :( ")  
else :
    print('in bazi barande nadarad ... ')