def operate(input):
    hasil = ""

    for i in input:
        if i == "x":
            hasil += "*"
        elif i == ":":
            hasil += ":"
        else:
            hasil += i
    
    return f"{hasil}"

