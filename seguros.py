# Inicialización del contador
contador_decisiones = 0

print("""------------------------------------------------------------------
Bienvenido al Sistema de Recomendación de Seguros para Automotores
------------------------------------------------------------------""")

# Entrada de datos del usuario
Presupuesto = input("Cuenta con un presupuesto mayor a 45.000$ ? [Si] [No]").upper()

Veraz = input("Usted se encuentran en el veraz? [Si] [No]").upper()

Categoría = input("Uso [PRIVADO] o [EMPRESARIAL]?").upper()

# Primera decisión: calificación

if ((Presupuesto == "SI") or (Categoría == "EMPRESARIAL")) and (Veraz == "NO"):
    print("Usted califica para ser asegurado")
    contador_decisiones += 1
elif ((Presupuesto == "NO") and (Categoría == "PRIVADO")) and (Veraz == "NO"):
    print("Lo sentimos, no califica para ser asegurado")
    contador_decisiones += 2
else:
    print ("Lo sentimos, no califica para ser asegurado")
    exit()


# Definición de constantes
SEGURO1 = "La gente aseguradora SA"
SEGURO2 = "La Caja de ahorro y seguro"
SEGURO3 = "Golden Seguros SRL"
PLAN1 = "Terceros cobertura C"
PLAN2 = "Todo riesgo parcial"
PLAN3 = "Todo riesgo"

# Obtener presupuesto
presupuesto = float(input("Ingrese el monto mensual disponible a pagar: "))

if presupuesto < 45000:
    print("Lo sentimos, no hay planes disponibles para su presupuesto.")
    exit()

# Obtener frecuencia
while True:
    frecuencia = input("Ingrese la frecuencia de uso según las siguientes categorías [ALTA] [MEDIA] [BAJA]: ").upper()
    if frecuencia in ["ALTA", "MEDIA", "BAJA"]:
        break
    print("Error: Opción no válida. Las opciones son: ALTA, MEDIA o BAJA")

# Obtener actividad
while True:
    actividad = input("Ingrese el tipo de actividad [RURAL] [URBANA] [COMERCIAL]: ").upper()
    if actividad in ["RURAL", "URBANA", "COMERCIAL"]:
        break
    print("Error: Opción no válida. Las opciones son: RURAL, URBANA o COMERCIAL")

# Lógica de recomendación
# FRECUENCIA ALTA
if frecuencia == "ALTA":
    contador_decisiones += 100
    if actividad == "URBANA":
        contador_decisiones += 30
        if 45000 <= presupuesto < 75000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}.")
            contador_decisiones += 11
        elif 75000 <= presupuesto < 120000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}.")
            contador_decisiones += 12
        elif presupuesto >= 120000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN3}.")
            contador_decisiones += 13
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")
    
    elif actividad == "RURAL":
        contador_decisiones += 60
        if 90000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}.")
            contador_decisiones += 11
        elif 150000 <= presupuesto < 200000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}.")
            contador_decisiones += 12
        elif presupuesto >= 200000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN3}.")
            contador_decisiones += 13
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")
    
    elif actividad == "COMERCIAL":
        contador_decisiones += 90
        if 60000 <= presupuesto < 85000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}.")
            contador_decisiones += 11
        elif 85000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}.")
            contador_decisiones += 12
        elif presupuesto >= 150000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN3}.")
            contador_decisiones += 13
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")

# FRECUENCIA MEDIA
elif frecuencia == "MEDIA":
    contador_decisiones += 200
    if actividad == "URBANA":
        contador_decisiones += 30
        if 75000 <= presupuesto < 120000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}.")
            contador_decisiones += 12
        elif 150000 <= presupuesto < 200000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN2}.")
            contador_decisiones += 32
        elif presupuesto >= 200000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN2}.")
            contador_decisiones += 22
        elif 85000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN2}.")
            contador_decisiones += 22
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")
    
    elif actividad == "RURAL":
        contador_decisiones += 60
        if 120000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN3}.")
            contador_decisiones += 13
        elif 150000 <= presupuesto < 200000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN3}.")
            contador_decisiones += 33
        elif presupuesto >= 200000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN3}.")
            contador_decisiones += 23
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")
    
    elif actividad == "COMERCIAL":
        contador_decisiones += 90
        if 75000 <= presupuesto < 120000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}.")
            contador_decisiones += 12
        elif 150000 <= presupuesto < 200000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN2}.")
            contador_decisiones += 32
        elif 85000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN2}.")
            contador_decisiones += 22
        elif presupuesto >= 200000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN2}.")
            contador_decisiones += 22
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")

# FRECUENCIA BAJA
elif frecuencia == "BAJA":
    contador_decisiones += 300
    if actividad == "URBANA":
        contador_decisiones += 30
        if 45000 <= presupuesto < 75000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}.")
            contador_decisiones += 11
        elif 90000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN1}.")
            contador_decisiones += 31
        elif 60000 <= presupuesto < 85000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN1}.")
            contador_decisiones += 21
        elif presupuesto >= 150000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN1}.")
            contador_decisiones += 31
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")
    
    elif actividad == "RURAL":
        contador_decisiones += 60
        if 75000 <= presupuesto < 120000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}.")
            contador_decisiones += 12
        elif 150000 <= presupuesto < 200000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN2}.")
            contador_decisiones += 32
        elif 85000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN2}.")
            contador_decisiones += 22
        elif presupuesto >= 200000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN2}.")
            contador_decisiones += 23
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")
    
    elif actividad == "COMERCIAL":
        contador_decisiones += 90
        if 45000 <= presupuesto < 75000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}.")
            contador_decisiones += 11
        elif 90000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN1}.")
            contador_decisiones += 31
        elif 60000 <= presupuesto < 85000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN1}.")
            contador_decisiones += 21
        elif presupuesto >= 150000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN1}.")
            contador_decisiones += 31
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")

# Conversión manual a binario
numero = contador_decisiones
binario = ""
if numero == 0:
    binario = "0"
else:
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2

# Mostrar número de gestión
print("Número de gestión :", binario)
