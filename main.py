string = input("Введите строку для определения длины, гласных, согласных в слове: ")

vowels = 0
consonants = 0

length = 0
all_vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
all_consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"

for char in string:

	length += 1

	if char in all_vowels:

		vowels += 1
	
	elif char in all_consonants:

		consonants += 1	

print(f"Длина строки: {length}, всего гласных: {vowels}, всего согласных: {consonants}")