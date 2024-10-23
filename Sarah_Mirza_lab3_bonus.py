
weight = float(input("Enter the total weight of your package: ")) #FC1
price = 0 #FC2
print()

if weight<0: #FC3
    print("Error: Weight cannot be negative. Enter a postive number.") #FC4

else:

    if weight <= 2: #FC5
        price = weight * 1.50 #FC6
        print("Shipping Rate: $1.50") #FC7
        print(f"   Total Cost: ${price:.02f}") #FC8

    elif weight>2 and weight<=6: #FC9
        price = weight * 3.00 #FC10
        print("Shipping Rate: $3.00") #FC11
        print(f"   Total Cost: ${price:.02f}") #FC12

    elif weight>6 and weight<=10: #FC13
        price = weight * 4.00 #FC14
        print("Shipping Rate: $4.00") #FC15
        print(f"   Total Cost: ${price:.02f}") #FC16

    elif weight>10: #FC17
        price = weight * 4.75 #FC18
        print("Shipping Rate: $4.75") #FC19
        print(f"   Total Cost: ${price:.02f}") #FC20

