inti=input("ENTER DATE1 IN DD/MM/YYYY FORMAT")
final=input("ENTER DATE2 IN DD/MM/YYYY FORMAT")
s=int(inti[6:])
f=int(final[6:])
l=""
nl=""
for i in range(s,f+1):
    if i%4==0 or (i%100!=0 and i%400==0):
        l=l+str(i)
        if i<f:
            l=l+","
    else:
        nl=nl+str(i)
        if i<f:
            nl=nl+","
print("LEAP YEARS: ",l)
print("NOT LEAP YEARS: ",nl)
