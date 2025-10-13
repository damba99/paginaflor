const navbar = document.getElementById('navbar');
const logoImg = document.getElementById('logo-img');

const updateNavbarState = () => {
    if (!navbar || !logoImg) return;
    if (window.scrollY > 10) {
        navbar.classList.add('navbar-scrolled');
        logoImg.src = 'images/logos/fv_blanco.png';
    } else {
        navbar.classList.remove('navbar-scrolled');
        logoImg.src = 'images/logos/fv_verde1.png';
    }
};

document.addEventListener('DOMContentLoaded', () => {
    updateNavbarState();
    window.addEventListener('scroll', updateNavbarState);

    const navbarToggler = document.querySelector('.navbar-toggler');
    if (navbarToggler) {
        navbarToggler.addEventListener('click', () => {
            document.getElementById('navbarNav')?.classList.toggle('show');
        });
    }

    const telefonoInput = document.getElementById('telefono');
    const errorTelefono = document.getElementById('errorTelefono');

    const validateTelefonoInput = (value) => /^[0-9+\-()\s]*$/.test(value);

    if (telefonoInput) {
        telefonoInput.addEventListener('keypress', (event) => {
            const key = event.key;
            if (!validateTelefonoInput(key)) {
                event.preventDefault();
                if (errorTelefono) {
                    errorTelefono.textContent = 'Solo se permiten números y símbolos + - ( )';
                }
            }
        });

        telefonoInput.addEventListener('input', () => {
            const isValid = validateTelefonoInput(telefonoInput.value);
            telefonoInput.classList.toggle('error', !isValid);
            if (errorTelefono) {
                errorTelefono.textContent = isValid ? '' : 'Solo se permiten números y símbolos + - ( )';
            }
        });
    }

    const form = document.getElementById('contact-form');
    const mensajeError = document.getElementById('mensajeError');
    const mensajeExito = document.getElementById('mensajeExito');

    if (form) {
        const fields = {
            nombre: document.getElementById('errorNombre'),
            telefono: errorTelefono,
            correo: document.getElementById('errorCorreo'),
            mensaje: document.getElementById('errorMensaje'),
        };

        const inputs = {
            nombre: form.nombre,
            telefono: form.telefono,
            correo: form.correo,
            mensaje: form.mensaje,
        };

        const resetFeedback = () => {
            Object.values(fields).forEach((field) => {
                if (field) field.textContent = '';
            });
            Object.values(inputs).forEach((input) => {
                if (input) input.classList.remove('error');
            });
            if (mensajeError) mensajeError.style.display = 'none';
            if (mensajeExito) mensajeExito.style.display = 'none';
        };

        const setError = (fieldKey, message) => {
            const fieldMessage = fields[fieldKey];
            if (fieldMessage) fieldMessage.textContent = message;
            const input = inputs[fieldKey];
            if (input) input.classList.add('error');
        };

        const validators = {
            nombre: (value) => /^[a-zA-ZÁÉÍÓÚÜÑáéíóúüñ\s]+$/.test(value.trim()),
            telefono: (value) => /^[0-9+\-()\s]+$/.test(value.trim()),
            correo: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value.trim()),
            mensaje: (value) => value.trim().length >= 10 && !/[<>]/.test(value),
        };

        form.addEventListener('submit', async (event) => {
            event.preventDefault();
            resetFeedback();

            const data = {
                nombre: form.nombre.value,
                telefono: form.telefono.value,
                correo: form.correo.value,
                mensaje: form.mensaje.value,
            };

            let valid = true;

            Object.entries(data).forEach(([key, value]) => {
                if (!validators[key](value)) {
                    valid = false;
                    switch (key) {
                        case 'nombre':
                            setError(key, 'El nombre solo puede contener letras y espacios.');
                            break;
                        case 'telefono':
                            setError(key, 'El teléfono contiene caracteres inválidos.');
                            break;
                        case 'correo':
                            setError(key, 'Ingresá un correo electrónico válido.');
                            break;
                        case 'mensaje':
                            setError(key, 'El mensaje debe tener al menos 10 caracteres.');
                            break;
                        default:
                            break;
                    }
                }
            });

            if (!valid) {
                if (mensajeError) {
                    mensajeError.textContent = 'Revisá la información ingresada.';
                    mensajeError.style.display = 'block';
                }
                return;
            }

            const formData = new FormData(form);
            const payload = new URLSearchParams(formData).toString();

            try {
                const response = await fetch('/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: payload,
                });

                if (response.ok) {
                    form.reset();
                    Object.values(inputs).forEach((input) => input.classList.remove('error'));
                    if (mensajeExito) {
                        mensajeExito.textContent = '¡Gracias! Tu mensaje fue enviado correctamente.';
                        mensajeExito.style.display = 'block';
                    }
                    if (mensajeError) {
                        mensajeError.style.display = 'none';
                    }
                } else {
                    throw new Error('Error en el envío');
                }
            } catch (error) {
                if (mensajeError) {
                    mensajeError.textContent = 'No pudimos enviar el formulario. Intentalo nuevamente.';
                    mensajeError.style.display = 'block';
                }
            }
        });
    }
});
