from datetime import datetime
name=input("enter your  name")
#list of items
lists='''

Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 30/kg
oil     Rs 20/liter
panner  Rs 80/kg
magi    Rs 110/kg
boost   Rs 90/each
colgate Rs 90/each

'''
# print(lists)
# Declaration

price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

# rates for items  in dictionary

items={'Rice':20,'Sugar':30,'Salt':30,'oil':20,'panner':80,'magi':110,'boost':90,'colgate':90}
option=int(input("for list of items press 1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or  2 fro exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter  quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
          print("sorry your entered item is not available ")
    else:
        print("you enter wromg number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Raja super market",25*"=")
            print(25*"=","rajanagaram",31*"=")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',4*" ",'   quantity',3*" ",'price',9*"")
            for i in range(len(pricelist)):
                print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
            print(i,ilist[i],qlist[i],plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:''-','Rs',totalprice)
            print("gst amount",50*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(50*" ","Thanks for visiting")f
            print(75*"-")




