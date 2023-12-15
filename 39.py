a = open("demo1.txt", "r")
b = open("t", "w")
c = a.readlines()
d = len(c)
for i in range(0, d):

     if i % 2 == 0:
       b.write(c[i])
     else:
       pass
b.close()
b = open("t", "r")
e = b.read()
print(e)
print(d)
a.close()
b.close()