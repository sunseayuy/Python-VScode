customer = {
    "name":"John Smith",
    "age":30,
    "is_verfied":True
}
print(customer["name"])
print(customer.get("name"))
print(customer.get("birthday","1998-1-1"))

customer["name"] = "Jack Smith"
print(customer["name"])

customer["birthdate"] = "June 1 1980"
print(customer["birthdate"])
