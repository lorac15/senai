#3
horas_t = float (input("horas trabalhadas: "))
horas_e = float (input("horas extras: "))

print (f"salário bruto: R$ {(horas_t * 10.0) + (horas_e * 15.0)}")
print (f"salário líquido: R$ {((horas_t * 10) + (horas_e * 15)) * 0.10}")