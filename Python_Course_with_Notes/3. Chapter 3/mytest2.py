
Name = input("Please enter your name \n")
Date = input("Date \n")

letter = '''Dear <|Name|>
            You are Selected :)
            <|Date|>'''

letter = letter.replace("<|Name|>", Name)
letter = letter.replace("<|Date|>", Date)

print(letter)