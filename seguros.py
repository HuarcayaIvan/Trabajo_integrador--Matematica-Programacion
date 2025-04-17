print("""------------------------------------------------------------------
Bienvenido al Sistema de Recomendación de Seguros para Automotores
------------------------------------------------------------------""")

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
    if actividad == "URBANA":
        if 45000 <= presupuesto < 75000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}.")
        elif 75000 <= presupuesto < 120000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}.")
        elif presupuesto >= 120000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN3}.")
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")
    
    elif actividad == "RURAL":
        if 90000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}.")
        elif 150000 <= presupuesto < 200000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}.")
        elif presupuesto >= 200000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN3}.")
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")
    
    elif actividad == "COMERCIAL":
        if 60000 <= presupuesto < 85000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}.")
        elif 85000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}.")
        elif presupuesto >= 150000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN3}.")
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")

# FRECUENCIA MEDIA
elif frecuencia == "MEDIA":
    if actividad == "URBANA":
        if 75000 <= presupuesto < 120000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}.")
        elif 150000 <= presupuesto < 200000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN2}.")
        elif presupuesto >= 200000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN2}.")
        elif 85000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN2}.")
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")
    
    elif actividad == "RURAL":
        if 120000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN3}.")
        elif 150000 <= presupuesto < 200000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN3}.")
        elif presupuesto >= 200000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN3}.")
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")
    
    elif actividad == "COMERCIAL":
        if 75000 <= presupuesto < 120000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}.")
        elif 150000 <= presupuesto < 200000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN2}.")
        elif 85000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN2}.")
        elif presupuesto >= 200000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN2}.")
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")

# FRECUENCIA BAJA
elif frecuencia == "BAJA":
    if actividad == "URBANA":
        if 45000 <= presupuesto < 75000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}.")
        elif 90000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN1}.")
        elif 60000 <= presupuesto < 85000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN1}.")
        elif presupuesto >= 150000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN1}.")
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")
    
    elif actividad == "RURAL":
        if 75000 <= presupuesto < 120000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}.")
        elif 150000 <= presupuesto < 200000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN2}.")
        elif 85000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN2}.")
        elif presupuesto >= 200000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN2}.")
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")
    
    elif actividad == "COMERCIAL":
        if 45000 <= presupuesto < 75000:
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}.")
        elif 90000 <= presupuesto < 150000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN1}.")
        elif 60000 <= presupuesto < 85000:
            print(f"Le recomendamos contratar {SEGURO2} con el plan {PLAN1}.")
        elif presupuesto >= 150000:
            print(f"Le recomendamos contratar {SEGURO3} con el plan {PLAN1}.")
        else:
            print("Lo sentimos, no hay planes disponibles para su presupuesto.")
