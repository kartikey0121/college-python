sal=int(input(" enter salary"))
exp = int(input("total expeince "))
if exp<=5:
    sal=sal+10000
    print("total salary",sal)
elif 6<exp<=10: 
    sal=sal+20000
    print("total salary",sal)

else:
    sal=sal+30000
    print("total salary",sal)

