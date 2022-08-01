from unicodedata import decimal, digit
card_number = list(input("Please enter your card: ").strip())
check_digit = card_number.pop()
card_number.reverse()
new_digits =[]
for index, digit in enumerate(card_number):
    if index % 2 == 0:
        new_digits.append(int(digit)* 2)
    
    else:
        new_digits.append(int(digit))

total = sum(new_digits)
integer_decimal = str(float(total/10)).split('.')[1]
number = int(integer_decimal)
final = 10 - number

if final == check_digit:
    print("This card is valid")
else:
    print("This card is not valid")

