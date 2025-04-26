print("""---------------------------------------------------------------------------------------
Simulador de circuito lógico del Filtro Binario de clientes de Seguros para Automotores
---------------------------------------------------------------------------------------""")

# Preguntas al cliente (ENTRADAS)
veraz = input("¿El cliente figura en el Veraz? (SI/NO): ").upper() == "SI"
comercial = input("¿El uso es comercial? (SI/NO): ").upper() == "SI"
presupuesto = float(input("Ingrese el presupuesto ($): ")) >= 100000

# Estructura del circuito y SALIDA
salida = (
    ((presupuesto and not comercial) # AND1
     or comercial) # OR
    and not veraz # AND_FINAL
)

if salida:
    print("Cliente ACEPTADO!!")
else:
    print("Cliente RECHAZADO")
