a=input("zaman ra vared konid va bein har bakhsh ( : ) bezarid:")

h, m, s =a.split(":")

x=int (h)*3600
y=int (m)*60
z=int (s)

sec=x + y+ z

print(sec)