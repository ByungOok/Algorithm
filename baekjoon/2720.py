T = int(input())
for i in range(0,T):
    Change = int(input())
    Quarter = Change // 25 
    Change = Change - Quarter * 25
    Dime = Change // 10
    Change = Change - Dime * 10
    Nickel = Change // 5
    Change = Change - Nickel * 5
    Penny = Change 
    print("%d %d %d %d" %(Quarter, Dime, Nickel, Penny))
