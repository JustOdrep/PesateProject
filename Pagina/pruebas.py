var= '1900,00'

var= var.replace("$", "").replace(".", "")
price = var.split(sep=',')[0]

print(price)
