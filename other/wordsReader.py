#2.Read content word by word from a text file.

with open('oda.txt') as f:
   for line in f:
       for word in line.split():
           print(word)