from sqlalchemy import create_engine, text

# Sustituye con tu cadena de conexión desde Neon.tech
# Ejemplo: postgresql+pg8000://usuario:contraseña@ep-xxxxx.us-east-1.aws.neon.tech/neondb
DATABASE_URL = "postgresql+pg8000://neondb_owner:npg_jgLvA9Onc6CB@ep-still-mountain-ad6oq9x8-pooler.c-2.us-east-1.aws.neon.tech/neondb"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users"))
        print("Conexión exitosa. Datos en la tabla users:")
        for row in result:
            print(row)
except Exception as e:
    print("❌ Error al conectar:", e)
