import psycopg2
import random
from psycopg2 import OperationalError

DB_HOST = "postgres_primary"
DB_PORT = "5432"
DB_NAME = "postgres"
DB_USER = "user"
DB_PASSWORD = "password"


CATEGORIAS_Y_PRODUCTOS = {
    'Electrónica': ['Teléfono', 'Monitor', 'Teclado', 'Altavoz', 'Cámara'],
    'Ropa': ['Camisa', 'Zapatos', 'Pantalones', 'Vestido', 'Abrigo'],
    'Hogar': ['Lámpara', 'Silla', 'Mesa', 'Cortinas', 'Estantería'],
    'Juguetes': ['Muñeca', 'Peluche', 'Rompecabezas', 'Carro', 'Jenga'],
    'Alimentos': ['Pan', 'Queso', 'Leche', 'Frutas', 'Cereal']
}

ADJETIVOS = ['Compacto', 'Elegante', 'Duradero', 'Colorido', 'Fresco']

def generar_nombre_producto(categoria):
    sustantivo = random.choice(CATEGORIAS_Y_PRODUCTOS[categoria])
    adjetivo = random.choice(ADJETIVOS)
    return f"{adjetivo} {sustantivo}"

def generar_precio():
    return round(random.uniform(10, 500), 2)  

def generar_categoria():
    return random.choice(list(CATEGORIAS_Y_PRODUCTOS.keys()))

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
    CREATE TABLE IF NOT EXISTS productos (
        id SERIAL PRIMARY KEY,
        nombre_producto VARCHAR(100),
        precio DECIMAL,
        categoria VARCHAR(50)
    );
""")

print("Insertando productos aleatorios en la tabla 'productos'...")
for _ in range(5):
    categoria = generar_categoria()
    nombre_producto = generar_nombre_producto(categoria)
    precio = generar_precio()
    cur.execute("INSERT INTO productos (nombre_producto, precio, categoria) VALUES (%s, %s, %s)",
                (nombre_producto, precio, categoria))

conn.commit()
print("Productos insertados exitosamente.")

cur.execute("SELECT * FROM productos;")
productos = cur.fetchall()

print("Datos en la tabla 'productos':")
for producto in productos:
    print(producto)

cur.close()
conn.close()