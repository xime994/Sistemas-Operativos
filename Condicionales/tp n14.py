num=int(input("Ingrese el calculo que desa realizar:"))
v=int(input("Ingrese un valor:"))
if num == 1:
    val=100*v
elif num==2:
    val=100**v
elif num == 3:
    if v != 0:
        val=100/v
    else:
        print("no se puede dividir por cero")
else:
    val=0
print("el valor es:",val)