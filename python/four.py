#for loop practice
for number in 1,2,3,4,5:
    print ("the current number",number)

[root@awsserver python]# cat four.py
#while loop example
baggage_count=100
no_of_baggage_picked=0
while(baggage_count > 0):
    no_of_baggage_picked = (int)(input ("number of baggage:"))
    baggage_count = baggage_count - no_of_baggage_picked
    print("No. of baggage remeaining:",baggage_count)
