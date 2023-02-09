Scrabble = {1:['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
          2: ['Д', 'К', 'Л', 'М', 'П', 'У','D', 'G'],
          3: ['Б', 'Г', 'Ё', 'Ь', 'Я','B', 'C', 'M', 'P'],
          4: ['Й', 'Ы','F', 'H', 'V', 'W', 'Y'],
          5: ['Ж', 'З', 'Х', 'Ц', 'Ч','K'],
          8: ['Ш', 'Э', 'Ю','J', 'X'],
          10: ['Ф', 'Щ', 'Ъ','Q', 'Z']}
word = input('введите слово для расчета его стоимости: ')
countWord = []
for el in word.upper():
    countWord.append(el)
result = 0
for el in countWord:
    for k, i in Scrabble.items():        
        if el in i:
            result += k
 
print(result)