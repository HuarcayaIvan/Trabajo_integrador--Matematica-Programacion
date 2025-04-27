print("""------------------------------------------------------------------
Bienvenido al Filtro de clientes de Seguros para Automotores
------------------------------------------------------------------""")

# Preguntar si el cliente figura en Veraz
veraz_input = input("¿El cliente figura en el Veraz? (SI/NO): ").upper()
veraz = veraz_input == "SI"

if veraz:
    print("Cliente RECHAZADO.")
else:
    # Preguntar si el uso es empresarial
    empresarial_input = input("¿El uso de la póliza es empresarial? (SI/NO): ").upper()
    empresarial = empresarial_input == "SI"

    if empresarial:
        print("Cliente ACEPTADO.")
    else:
        # Preguntar por el presupuesto
        presupuesto_input = input("Ingrese el presupuesto del cliente (en pesos): ")
        presupuesto = float(presupuesto_input)

        if presupuesto > 100000:
            print("Cliente ACEPTADO!!")
        else:
            print("Cliente RECHAZADO")

