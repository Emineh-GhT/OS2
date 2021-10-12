s=int (input("zaman ra be sanye vared konid:"))

h=int (s/3600)
s=s%3600
m=int (s/60)
s=s%60

print(h,":",m,":",s)