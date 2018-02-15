# Creating a string
pancard_number = "CFUPM7814P"
# Length of the string
print("length of tha PAN card number:", len(pancard_number))
#containing two strings
name1 = "PAN "
name2 = "card"
name = name1 + name2
print(name)
print("Iterating the string using range()")
for index in range(0,len(pancard_number)):
    print (pancard_number [index])
print("Iterating the string using keyword in")
for valve in pancard_number:
    print(valve)

print("searching for a character in string")
if "F" in pancard_number:
    print("charecter present")

#Slicimg astring
print("the numbers in tha PAN card:", pancard_number[5:9])
print("last butone 3 characters in the PAN card:", pancard_number[-4:-1])

print(pancard_number)
