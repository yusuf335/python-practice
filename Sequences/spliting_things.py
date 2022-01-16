panagram = """The quick brown
 
 fox jumps \t over
  the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

lists = ['9', '223', '372', '845', '775', '807']

for new_list in lists:
    print(new_list)

for index in range(len(lists)):
    lists[index] = int(lists[index])
print(lists)

integer_values =[]
for values in lists:
    integer_values.append(int(values))
print(integer_values)
