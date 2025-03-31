<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST['nombre'];
    $apellido = $_POST['apellido'];
    $telefono = $_POST['telefono'];
    $correo = $_POST['correo'];
    $mensaje = $_POST['mensaje'];

    $to = "abogadaflorenciavelazques@gmail.com"; // Reemplaza con tu correo electrónico
    $subject = "Nuevo mensaje de contacto";
    $body = "Nombre: $nombre\nApellido: $apellido\nTeléfono: $telefono\nCorreo: $correo\nMensaje: $mensaje";
    $headers = "From: $correo";

    if (mail($to, $subject, $body, $headers)) {
        echo "Correo enviado exitosamente!";
    } else {
        echo "Hubo un error al enviar el correo.";
    }
}
?>








.card-container {
        margin-bottom: 20px;
    }

    .servicios {
        display: grid;
        grid-template-columns: repeat(2, 1fr); /* 2 columnas por renglón */
        gap: 20px; /* Espacio entre las tarjetas */
    }

    .card {
        display: flex; 
        align-items: center; 
        justify-content: flex-start;
        background-color: red;
    }

    .card-image-wrapper {
        background-color: blue;
        padding: 10px;
        border-radius: 10px;
    }

    .card-img-top {
        width: 100px;
        border-bottom: 2px solid var(--verde);
    }

    .card-body {
        height: 130px;
        flex-grow: 1; 
        padding: 15px;
        background-color: #f8f9fa;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-family: 'Arial', sans-serif;
        color: #333;
    }
    
    .card-body h5 {
        color: var(--verde);
        font-size: 1.2em;
        margin-bottom: 10px;
        font-weight: 600;
    }
    
    .card-body p {
        font-size: 1em;
        color: #666;
        line-height: 1.4;
    }