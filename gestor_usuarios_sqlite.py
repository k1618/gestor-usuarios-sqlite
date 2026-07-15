import sqlite3

DB_NOMBRE = "usuarios.db"


def conectar():
    """Crea la conexión y la tabla de usuarios si no existe."""
    conexion = sqlite3.connect(DB_NOMBRE)
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            correo TEXT NOT NULL UNIQUE
        )
    """)
    conexion.commit()
    return conexion


def validar_nombre(nombre):
    return len(nombre.strip()) >= 3


def validar_edad(edad):
    return edad > 0


def validar_correo(correo):
    return "@" in correo and "." in correo.split("@")[-1]


def registrar_usuario(conexion):
    """Solicita datos, los valida, y los guarda en la base de datos."""
    nombre = input("Nombre: ")

    while True:
        try:
            edad = int(input("Edad: "))
            break
        except ValueError:
            print("Por favor ingresa un número válido.")

    correo = input("Correo electrónico: ")

    errores = []
    if not validar_nombre(nombre):
        errores.append("El nombre debe tener al menos 3 caracteres.")
    if not validar_edad(edad):
        errores.append("La edad debe ser mayor a 0.")
    if not validar_correo(correo):
        errores.append("El correo electrónico no tiene un formato válido.")

    if errores:
        print("\nNo se pudo registrar. Datos inválidos:")
        for error in errores:
            print(f"  - {error}")
        return

    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, edad, correo) VALUES (?, ?, ?)",
            (nombre, edad, correo)
        )
        conexion.commit()
        print(f"\n¡Usuario '{nombre}' registrado con éxito!")
    except sqlite3.IntegrityError:
        print("\nError: ya existe un usuario registrado con ese correo.")


def listar_usuarios(conexion):
    """Muestra todos los usuarios registrados."""
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, edad, correo FROM usuarios")
    usuarios = cursor.fetchall()

    if not usuarios:
        print("\nNo hay usuarios registrados todavía.")
        return

    print(f"\n{'ID':<5}{'Nombre':<20}{'Edad':<6}{'Correo':<30}")
    print("-" * 61)
    for id_usuario, nombre, edad, correo in usuarios:
        print(f"{id_usuario:<5}{nombre:<20}{edad:<6}{correo:<30}")


def buscar_usuario(conexion):
    """Busca usuarios por nombre (búsqueda parcial, no distingue mayúsculas)."""
    termino = input("Ingresa el nombre a buscar: ")
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT id, nombre, edad, correo FROM usuarios WHERE nombre LIKE ?",
        (f"%{termino}%",)
    )
    resultados = cursor.fetchall()

    if not resultados:
        print(f"\nNo se encontraron usuarios que coincidan con '{termino}'.")
        return

    print(f"\n{'ID':<5}{'Nombre':<20}{'Edad':<6}{'Correo':<30}")
    print("-" * 61)
    for id_usuario, nombre, edad, correo in resultados:
        print(f"{id_usuario:<5}{nombre:<20}{edad:<6}{correo:<30}")


def eliminar_usuario(conexion):
    """Elimina un usuario según su ID."""
    listar_usuarios(conexion)
    cursor = conexion.cursor()

    try:
        id_usuario = int(input("\nIngresa el ID del usuario a eliminar: "))
    except ValueError:
        print("ID inválido. Debe ser un número.")
        return

    cursor.execute("SELECT nombre FROM usuarios WHERE id = ?", (id_usuario,))
    resultado = cursor.fetchone()

    if not resultado:
        print(f"No existe ningún usuario con ID {id_usuario}.")
        return

    confirmacion = input(f"¿Seguro que quieres eliminar a '{resultado[0]}'? (s/n): ")
    if confirmacion.lower() == "s":
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
        conexion.commit()
        print(f"Usuario '{resultado[0]}' eliminado.")
    else:
        print("Operación cancelada.")


def mostrar_menu():
    print("\n" + "=" * 40)
    print("   GESTOR DE USUARIOS (SQLite)")
    print("=" * 40)
    print("1. Registrar nuevo usuario")
    print("2. Ver todos los usuarios")
    print("3. Buscar usuario por nombre")
    print("4. Eliminar usuario")
    print("5. Salir")
    print("=" * 40)


def main():
    conexion = conectar()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_usuario(conexion)
        elif opcion == "2":
            listar_usuarios(conexion)
        elif opcion == "3":
            buscar_usuario(conexion)
        elif opcion == "4":
            eliminar_usuario(conexion)
        elif opcion == "5":
            print("\n¡Hasta luego!")
            conexion.close()
            break
        else:
            print("\nOpción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()