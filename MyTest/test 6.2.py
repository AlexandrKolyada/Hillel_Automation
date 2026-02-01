your_word = ""

while True:
    your_word = input("Enter your word with ""h/H"":" )
    if "h" in your_word.lower():
        print(f"Good: {your_word}")
        break
    else:
        print("Wrong word, try again")