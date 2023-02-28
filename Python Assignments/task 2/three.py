a, b, c = 10, 20, 30
avg = (a+b+c)/3
print("Average: ", avg)

if avg > a and avg > b and avg > c:
    print (f"{avg} is grater than {a}, {b}, {c}")
elif avg > a and avg > b:
    print (f"{avg} is grater than {a}, {b}")
elif avg > a and avg > c:
    print (f"{avg} is grater than {a}, {c}")
elif avg > c and avg > b:
    print (f"{avg} is grater than {c}, {b}")
elif avg > a:
    print (f"{avg} is grater than {a}")
elif avg > b:
    print (f"{avg} is grater than {b}")
elif avg > c:
    print (f"{avg} is grater than {c}")





