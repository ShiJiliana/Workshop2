name_country = str(input('Введите название страны: '))
words = name_country.split()
print(*words, sep='\n')