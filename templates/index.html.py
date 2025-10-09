<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Usuarios - Base de Datos Neon</title>
</head>
<body>
    <h1>Lista de usuarios</h1>

    <form action="/add" method="POST">
        <input type="text" name="name" placeholder="Nombre" required>
        <input type="email" name="email" placeholder="Correo" required>
        <button type="submit">Agregar</button>
    </form>

    <ul>
        {% for user in users %}
            <li>{{ user[1] }} - {{ user[2] }}</li>
        {% endfor %}
    </ul>
</body>
</html>
