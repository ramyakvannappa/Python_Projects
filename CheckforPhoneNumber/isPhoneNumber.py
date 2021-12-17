# 444-011-2020

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for num in range(0,3):
        if not text[num].isdecimal():
            return False
    if text[3] != "-":
        return False
    for num in range(4,7):
        if not text[num].isdecimal():
            return False
    if text[7] != "-":
        return False
    for num in range(8,12):
        if not text[num].isdecimal():
            return False
    return True

message= "Call office at 111-111-1111 or 222-222-2222"

found_number = False
for element in range(0,len(message)):
    chunk = message[element:element+12]
    if isPhoneNumber(chunk):
        print(f"The phone number is {chunk}")
        found_number = True

if not found_number :
    print("Phone number not found")
