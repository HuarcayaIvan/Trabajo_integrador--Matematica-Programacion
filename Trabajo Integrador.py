#Premisa del programa: sistema que facilita a los usuarios a encontrar el mejor seguro vehicular. Tomando como factores: ubicación, frecuencia, actividad y presupuesto del usuario.

print("""------------------------------------------------------------------
Bienvenido al Sistema de Recomendación de Seguros para Automotores
------------------------------------------------------------------""")

#Definicion de constantes. 
SEGURO1 = "La gente aseguradora SA"
SEGURO2 = "La Caja de ahorro y seguro"
SEGURO3 = "Golden Seguros SRL"
PLAN1 = "Terceros cobertura C"
PLAN2 = "Todo riesgo parcial"
PLAN3 = "Todo riesgo"
# Para mas informacion acerca de los valores dirigirse a la documentacion/anexos

#Definicion de variable clave
Presupuesto = float(input("Ingrese el monto mensual disponible a pagar: "))

# Inicio de estructura condicional para la recomendación según frecuencia.
if Presupuesto < 45000:
    print("Lo sentimos, no hay planes disponibles para su presupuesto.")
    exit()
else:
    #Definicion de variables complementarias
    Frecuencia = input("Ingrese la frecuencia de uso segun las siguientes categorias [ALTA] [MEDIA] [BAJA].").upper()
    Actividad = input("Ingrese el tipo de actividad [RURAL] [URBANA] [COMERCIAL].").upper()

#///// Inicio de estructura condicional para la recomendacion de aseguradora frecuencia ALTA /////
if ((Frecuencia == "ALTA") and (Actividad == "URBANA")):
    if 45000 <= Presupuesto < 75000 :
        print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}. ")
    elif 75000 <= Presupuesto < 120000 :
        print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}. ")
    else:
        Presupuesto >= 120000 
        print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN3}. ")

if (Frecuencia == "ALTA") and (Actividad == "RURAL") and (Presupuesto > 90000):
    if 90000 <= Presupuesto < 150000 :
        print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}. ")
    elif 150000 <= Presupuesto < 200000 :
        print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}. ")
    else:
        Presupuesto >= 200000
        print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN3}. ")

if (Frecuencia == "ALTA") and (Actividad == "COMERCIAL") and (Presupuesto > 60000):
    if 60000 <= Presupuesto < 85000 :
        print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}. ")
    elif 85000 <= Presupuesto < 150000 :
        print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}. ")
    else :
        Presupuesto >= 150000
        print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN3}. ")
else:
    print("Lo sentimos, no hay planes disponibles para su presupuesto.")
