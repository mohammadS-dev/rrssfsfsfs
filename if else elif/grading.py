#grading from mohammad

english = int(input("enter your english marks"))
hindi = int(input("enter your hindi marks"))
maths =int(input("enter your maths marks"))
urdu =int(input("enter your urdu marks"))

total = english + hindi + maths + urdu 
print (total)

percentage = total / 400*100 

print("your percentage is", percentage)


if percentage >= 50:
    print ("Grade B")

elif percentage == 100: 
    print ("Topper hai bhai")

elif percentage < 50 :
    print ("fail hai")