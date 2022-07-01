def remove_not_quarters(stack):
    temp_stack = []
    for i in range(len(stack), 0, -1):
        coin = stack.pop()
        if coin[0] == "Q":
            temp_stack.append(coin)
    stack = []
    for i in range(len(temp_stack)):
        stack.append(temp_stack.pop())
    return stack

list_1 = [("Q", 2002), ("Q", 1997), ("P", 2015), ("Q", 2011), ("D", 1971), ("D", 2020), ("Q", 2013), ("Q", 1999), ("P", 2001)]
list_2 = [("Q", 2002), ("Q", 1997), ("Q", 2011), ("Q", 2013), ("Q", 1999)]
list_3 = [("P", 2012), ("N", 1986), ("P", 2010), ("N", 2011), ("D", 1919), ("D", 2022), ("P", 2009), ("N", 1980), ("P", 2011)]

print()
print(remove_not_quarters(list_1))
print(remove_not_quarters(list_2))
print(remove_not_quarters(list_3))
print()