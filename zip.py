first_name = ["Jack", "Tom", "Dwayne"]
last_name  = ["Ryan","Holland", "Johnson"]

name = zip(first_name,last_name)

for a,b in name:
    print(a,b)

def pallindrome():
    while True:

        string=input("Enter the string or number you want to check")
        if string == string[::-1]:
         print("It is a pallindrome")
        else:
         print("It is not a pallindrome")

pallindrome()