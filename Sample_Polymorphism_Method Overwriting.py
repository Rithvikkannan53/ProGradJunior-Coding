def add(datatype, *args):
    if datatype == "int":
        sample = 0

    if datatype == "str":
        sample = ' '

    if datatype == "float":
        sample = 0.0
        
    for x in args:
        sample = sample + x

    print(sample)

add('int',10,20,50,6)
add('str','Good',' ','Evening')
add('float',10.1,29.5,7.9)
add('int')
