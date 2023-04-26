var= '1900,00'

var= var.replace("$", "").replace(".", "").split()
price = var.split(sep=',')[0]

print(price)
