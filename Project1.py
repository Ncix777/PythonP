strt=1
Dict={}
credit={}
list_cus=[]
temp_lis=[]
p_bought={}
amount=0
print("!Only For Customer Who Have Percise")
while strt==1:
    tot_bill=0
    nam=input("Enter Customer Name: ")
    shop=int(input("Enter No. Product Percised"))
    list_cus.append(nam)
    temp={}
    for i in range(shop):
        item=input("Enter Product Name: ")
        quan=int(input("Enter Quantity: "))
        price=int(input("Enter Price: "))
        temp[item]=[quan,price]
        temp_lis.append(temp)
        tot_bill+=price
    else:
        print(nam,"Total Bill Is",tot_bill)
        if tot_bill>0:
            amount=int(input("Enter The Amount Paid By Customer: "))
        bal=tot_bill-amount
        if bal>0:
            print("Customer",nam," Have To Pay Rs: ",bal)
            credit[nam]=[tot_bill,bal]
        else:
            print("Fully Paid")
    strt=int(input("\nEnter Choice\n1.Another Customer\n2.Exit\n"))
for i in range(len(list_cus)):
    p_bought[list_cus[i]]=[temp_lis[i]]
q=int(input("Do You Have Another Query\n1.Yes\n2.No Exit\n"))
while q==1:
    qes=int(input("1.List Of People Who Have Credited\n2.All Customer List\n3.Customer List With Product\n"))
    if qes==1:
        for i in credit.items():
            print(i)
    elif qes==2:
        print(list_cus)
    elif qes==3:
        for i in p_bought.items():
            print(i)
    q=int(input("Do You Have Another Query\n1.Yes\n2.No Exit\n"))

