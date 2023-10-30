a=str(input("enter first string:"))
b=str(input("enter second string:"))
print(a.replace(a[0],b[0])+' '+b.replace(b[0],a[0]))