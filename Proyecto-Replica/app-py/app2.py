import psycopg2
import random
import string
import time
from psycopg2 import OperationalError

DB_HOST = "postgres_primary"
DB_PORT = "5432"
DB_NAME = "postgres"
DB_USER = "user"
DB_PASSWORD = "password"

def generar_nombre_cliente():
    nombres = ['Juan', 'Ana', 'Pedro', 'María', 'Luis', 'Elena', 'Carlos', 'Sara']
    apellidos = ['García', 'López', 'Martínez', 'Rodríguez', 'Gómez', 'Díaz']
    return f"{random.choice(nombres)} {random.choice(apellidos)}"

def generar_correo(nombre_cliente):
    dominios = ['example.com', 'correo.com', 'email.com']
    nombre_formateado = nombre_cliente.replace(" ", ".").lower()
    return f"{nombre_formateado}@{random.choice(dominios)}"

def generar_edad():
    return random.randint(18, 70)  # Edad entre 18 y 70 años

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    print(f"Conexión a la base de datos {DB_NAME} exitosa.")
except OperationalError as e:
    print(f"Error al conectar a la base de datos: {e}")
    exit(1)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id SERIAL PRIMARY KEY,
        nombre_cliente VARCHAR(100),
        correo VARCHAR(100),
        edad INTEGER
    );
""")

print("Insertando clientes aleatorios en la tabla 'clientes'...")
for _ in range(5):
    nombre_cliente = generar_nombre_cliente()
    correo = generar_correo(nombre_cliente)
    edad = generar_edad()
    cur.execute("INSERT INTO clientes (nombre_cliente, correo, edad) VALUES (%s, %s, %s)",
                (nombre_cliente, correo, edad))

conn.commit()
print("Clientes insertados exitosamente.")

cur.execute("SELECT * FROM clientes;")
clientes = cur.fetchall()

print("Datos en la tabla 'clientes':")
for cliente in clientes:
    print(cliente)

cur.close()
conn.close()