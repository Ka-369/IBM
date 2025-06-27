import numpy as np
name="Mana Ruchulu"
is_open=True
rate=4.5
cus=0
dis=None
menu={"Dosa":10,"Idli":10,"Mysore bajji":20,"Poori":15,"Karam dosa":15}

def show():
    print("\nWelcome to",name)
    print("------ MENU ------")
    for i in menu:
        print(i,": ₹",menu[i])

def order():
    x=[]
    y=[]
    while True:
        z=input("Enter item (or 'done'): ").title()
        if z.lower()=="done":
            break
        if z in menu:
            q=int(input("Qty for "+z+": "))
            x.append(z)
            y.append(q)
        else:
            print("Not in menu")
    return x,y

def bill(i,j):
    p=np.array([menu[k] for k in i],dtype=float)
    q=np.array(j,dtype=int)
    t=p*q
    print("\n------- BILL -------")
    for n in range(len(i)):
        print(i[n],"x",q[n],"= ₹",t[n])
    total=np.sum(t)
    print("\nTotal = ₹",total)
    return total

def main():
    global cus
    if is_open:
        show()
        a,b=order()
        if a:
            total=bill(a,b)
            cus+=1
        else:
            print("No order")
    else:
        print("Closed")

main()
