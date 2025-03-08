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
