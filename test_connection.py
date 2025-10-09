import psycopg2

# 🔸 Sustituye esta cadena con la tuya desde Neon.tech
connection_string = "postgresql+pg8000://neondb_owner:npg_jgLvA9Onc6CB@ep-still-mountain-ad6oq9x8-pooler.c-2.us-east-1.aws.neon.tech/neondb"

try:
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()
    print("Conexión exitosa. Datos en la tabla users:")
    for row in rows:
        print(row)
    conn.close()
except Exception as e:
    print("Error al conectar:", e)
