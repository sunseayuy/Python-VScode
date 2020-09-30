number_English = {
    "0":"Zero",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
numbers = input('Phone: ')
output = ""
for item in numbers:
    output += number_English.get(item,'!')+" "
print(output)
    