import random

letters_small = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
letters_cap = [char.upper() for char in letters_small]
letters_list = letters_small + letters_cap

numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols_list = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

all_chars = letters_small + letters_cap + symbols_list + numbers_list

passLength = int(input("Enter Length: "))
# print(all_chars)

password = (
    [random.choice(letters_list) for letter in range(random.randint(4, 6))]
    + [random.choice(symbols_list) for symbol in range(random.randint(2, 4))]
    + [random.choice(numbers_list) for number in range(random.randint(2, 4))]
)
password = [random.choice(all_chars) for ch in range(passLength)]

random.shuffle(password)  # random list
rampass = "".join(password)
print(rampass)