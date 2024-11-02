# Calculadora básica en Python

# Función para realizar la operación seleccionada
def calculadora():
    print("Selecciona la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    # Solicitar al usuario que elija una opción
    opcion = input("Introduce la opción (1/2/3/4): ")

    if opcion in ('1', '2', '3', '4'):
        # Pedir al usuario dos números
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if opcion == '1':
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")

        elif opcion == '2':
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    else:
        print("Opción no válida. Intenta de nuevo.")

# Ejecutar la calculadora
calculadora()
