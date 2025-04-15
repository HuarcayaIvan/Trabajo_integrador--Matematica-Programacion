#Premisa del programa: sistema que facilita a los usuarios a encontrar el mejor seguro vehicular. Tomando como factores: ubicación, frecuencia, actividad y presupuesto del usuario.

print("""------------------------------------------------------------------
Bienvenido al Sistema de Recomendación de Seguros para Automotores
------------------------------------------------------------------""")

#Definicion de constantes. 

#Seguros
SEGURO1 = "La gente aseguradora SA"
SEGURO2 = "La Caja de ahorro y seguro"
SEGURO3 = "Golden Seguros SRL"
#Planes (Para mas informacion acerca de los valores dirigirse a la documentacion/anexos)
PLAN1 = "Terceros cobertura C"
PLAN2 = "Todo riesgo parcial"
PLAN3 = "Todo riesgo"

#Definicion de variable clave
Presupuesto = float(input("Ingrese el monto mensual disponible a pagar: "))

# Inicio de estructura condicional para la recomendación según frecuencia de uso.
if Presupuesto < 45000:
    print("Lo sentimos, no hay planes disponibles para su presupuesto.")
else:
    #Definicion de variables complementarias
    Uso = input("Ingrese la frecuencia de uso segun las siguientes categorias [ALTA] [MEDIA] [BAJA].").upper()
    Actividad = input("Ingrese el tipo de actividad [RURAL] [URBANA] [COMERCIAL].").upper()

    if (Uso == "ALTA") and (Actividad == "URBANA"):
        if 45000 <= Presupuesto < 75000 :
            print(f"""Le recomendamos contratar {SEGURO1} con el plan {PLAN1}.
            Este es su codigo """)
        elif 75000 <= Presupuesto < 120000 :
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}. ")
        elif Presupuesto >= 120000 :
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN3}. ")

    if (Uso == "ALTA") and (Actividad == "RURAL"):
        if 90000 <= Presupuesto < 150000 :
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}. ")
        elif 150000 <= Presupuesto < 200000 :
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}. ")
        elif Presupuesto >= 200000 :
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN3}. ")

    if (Uso == "ALTA") and (Actividad == "COMERCIAL"):
        if 60000 <= Presupuesto < 85000 :
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}. ")
        elif 85000 <= Presupuesto < 150000 :
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}. ")
        elif Presupuesto >= 150000 :
            print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN3}. ")


    if (Uso == "ALTA"):
        if (Actividad == "COMERCIAL"): 
            if 60000 <= Presupuesto < 85000 :
                print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN1}. ")
            elif 85000 <= Presupuesto < 150000 :
                print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN2}. ")
            elif Presupuesto >= 150000 :
                print(f"Le recomendamos contratar {SEGURO1} con el plan {PLAN3}. ")
        else:
            if (Actividad == "COMERCIAL"): 