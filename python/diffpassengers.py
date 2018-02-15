## Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
#The ticket number should be generated as airline:src:dest:number
#where

#1.Consider AI as the value for airline
#2.src and dest should be the first three characters of the source and destination cities.
#3.number should be auto-generated starting from 101
'''The program should return the list of ticket numbers of last five passengers.
#Note: If passenger count is less than 5, return the list of all generated ticket numbers.'''
def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[106]
#we have to write some logic hear

#use the bellow return statement
    return ticket_number_list
#provide different values for airline,src.dest and numverof passengers
print(generate_ticket("AI","Bangalore","London",7))

[root@awsserver python]# cat diffpassenger.py
##Bagagge checking is different for different type of passengers
for passenger in "A", "A", "FC", "C", "FA", "SP", "A", "A":
    if (passenger == "FC" or passenger == "FA"):
        print ("no check required")
        continue

    if (passenger == "SP"):
        print ("Declare emergency in the airport")
        break

    if (passenger == "A" or passenger == "c"):
        print ("proceed with normal security check")


    print ("check the person")
    print ("check for cabbin baggage")
