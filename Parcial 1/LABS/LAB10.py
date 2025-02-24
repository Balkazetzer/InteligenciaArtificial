ingreso = float(input())
if ingreso <= 85528:
    impuesto = ingreso * 0.18 - 556.02
    if impuesto < 0:
        impuesto = 0
else:
    impuesto = 14839.02 + (ingreso - 85528) * 0.32
print(round(impuesto))
