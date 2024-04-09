data = "Hellow world siva is very Good Boy"

li = ['hello', 'world', 'siva', 'is', 'very', 'good', 'Boy']

data_li = data.split()

result = []


for i in data_li:
    if ((i.startswith('s') or i.startswith('S')) and (i.endswith('a') or i.endswith('A')) and (len(i)==4)):
        result.append(i.upper())

print(result)
result_name = result[0]
print(result_name)


ol = []

for i in data:
    if ((i in 'aeiouAEIOU') and (i not in ol)):
        ol.append(i)

ol.sort()

print(ol)








