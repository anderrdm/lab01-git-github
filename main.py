def main():
    nombre = input("Por favor, ingresa tu nombre: ").strip()
    if not nombre:
        nombre = "Estudiante"
    print(f"¡Hola, {nombre}! Bienvenido al control de versiones con Git y GitHub.")

if  __name__ == "__main__":
    main()