input_your_symbol = input("Enter your symbol: " )

count = set()
for char in input_your_symbol:
    if char not in count:
        count.add(char)

if len(count) > 10:
    print("True")
else:
    print("False")