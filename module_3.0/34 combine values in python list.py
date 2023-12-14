# Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
# 300}, o {'item': 'item1', 'amount': 750}]


Sampledata: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
                300},{'item': 'item1', 'amount': 750}]

my_dict = []

for entry in Sampledata:
    item = entry['item']
    amount = entry['amount']

    if item in my_dict:
        my_dict[item] += amount

    else :
        my_dict[item] = amount

print(my_dict)