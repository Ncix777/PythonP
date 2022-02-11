print("Welcome To my Shop\n")
strt=1
tot_bill=0
while strt==1:
    Food={"Rice":20,"Dal":90,"Atta":30,"Maida":30}
    Fruit={"Amla":50,"Mango":80,"Apple":100}
    Cometic={"Fair And Handsome":70,"Fair and Lovely":60,"Ponds":80}
    Basic={"Pen":10,"Pencil":10,"Geometry Box":175,"Eraser":5}
    choice=int(input("Available Types Of Product, Enter Choice:\n1.Food\n2.Fruit\n3.Cosmetic\n4.Basic\n"))
    amount=0
    if choice==1:
        print("Available Item",Food)
        proBuy=1
        while proBuy==1:
            item=input("Enter Product Name: ")
            for i in Food.keys():
                if item==i:
                    quan=int(input("Enter Quantity: "))
                    amount=amount+Food[item]*quan
                    break;
            else:
                print(item,"Out Of Stock")
            proBuy=int(input("1.Continue\n2.Bill\n"))
        else:
            print("Total Bill Is",amount)
    elif choice==2:
        print("Available Item",Fruit)
        proBuy=1
        while proBuy==1:
            item=input("Enter Product Name: ")
            for i in Fruit.keys():
                if item==i:
                    quan=int(input("Enter Quantity: "))
                    amount=amount+Fruit[item]*quan
                    break;
            else:
                print(item,"Out Of Stock")
            proBuy=int(input("1.Continue\n2.Bill\n"))
        else:
            print("Total Bill Is",amount)
    elif choice==3:
        print("Available Item",Cometic)
        proBuy=1
        while proBuy==1:
            item=input("Enter Product Name: ")
            for i in Cometic.keys():
                if item==i:
                    quan=int(input("Enter Quantity: "))
                    amount=amount+Cometic[item]*quan
                    break;
            else:
                print(item,"Out Of Stock")
            proBuy=int(input("1.Continue\n2.Bill\n"))
        else:
            print("Total Bill Is",amount)
    elif choice==4:
        print("Available Item",Basic)
        proBuy=1
        while proBuy==1:
            item=input("Enter Product Name: ")
            for i in Basic.keys():
                if item==i:
                    quan=int(input("Enter Quantity: "))
                    amount=amount+Basic[item]*quan
                    break;
            else:
                print(item,"Out Of Stock")
            proBuy=int(input("1.Continue\n2.Bill\n"))
        else:
            print("Total Bill Is",amount)
    tot_bill+=amount
    strt=int(input("1.Another Product\n2.Total Bill\n"))
else:
    print("Your Total Bill: ",tot_bill)
    
