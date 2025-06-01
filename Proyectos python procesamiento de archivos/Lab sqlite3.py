import sqlite3

class todo:
    def __init__(self):
        self.conexion = sqlite3.connect("C:\\Users\\Luis Reyes\\Downloads\\tareas.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tareas (
                            id INTEGER PRIMARY KEY,
                            nombre TEXT NOT NULL,
                            prioridad INTEGER NOT NULL
                            );""")
        
    def añadir(self):
        nombre = input("Ingresa una tarea: ")
        prioridad = input("Nivel de prioridad: ")
        self.cursor.execute("INSERT INTO tareas (nombre, prioridad) VALUES (?, ?)", (nombre, prioridad))
        self.conexion.commit()

    def leer_datos(self):
        for datos in self.cursor.execute("SELECT * FROM tareas"):
            print(datos)

    def eliminar_datos(self):
        elimnar = input("Id de tarea a eliminar: ")
        self.cursor.execute("DELETE FROM tareas where id = ?", (elimnar))
        self.conexion.commit()
    
    def encontrar_tarea(self):
        nombre = input("Nombre de tarea a encontrar: ")
        prio = input("Nivel de prioridad: ")
        dato = self.cursor.execute("SELECT * FROM tareas WHERE (nombre = ? AND prioridad = ?)", (nombre, prio))
        bucle = dato.fetchone()
        print(bucle)

    def actualizar_datos(self):
        idd = input("Id de la tarea que desea actualizar: ")
        nombre = input("Nuevo nombre: ")
        prioridad = input("Nueva prioridad: ")
        id_nuevo = input("Nuevo id: ")
        self.cursor.execute("UPDATE tareas SET id = ?, nombre = ?, prioridad = ? WHERE id = ?", (id_nuevo, nombre, prioridad, idd))
        self.conexion.commit()

salir = True

app = todo()

while salir:
    print("1. Leer tareas") 
    print("2. Añadir tareas")
    print("3. Cambiar tareas")
    print("4. Eliminar tareas")
    print("5. Encontrar tareas")
    print("6. Salir")
    opcion = input("Elige una opcion: ")
    match opcion:
        case "1":
            app.leer_datos()
        case "2":
            app.añadir()
        case "3":
            app.actualizar_datos()
        case "4":
            app.eliminar_datos()
        case "5":
            app.encontrar_tarea()
        case "6":
            salir = False
            print("Has salido")