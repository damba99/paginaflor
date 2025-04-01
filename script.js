let prevScrollPos = window.pageYOffset;
const navbar = document.getElementById('navbar');
const logoImg = document.getElementById('logo-img');
let timeoutId;


document.querySelector('.navbar-toggler').addEventListener('click', function () {
    document.querySelector('.navbar-nav').classList.toggle('show');
});

window.addEventListener('scroll', function() {
    const currentScrollPos = window.pageYOffset;

    if (currentScrollPos === 0) {
        navbar.classList.remove('navbar-scrolled');
        logoImg.src = 'images/logos/fv_blanco.png';
    } else {
        navbar.classList.add('navbar-scrolled');
        logoImg.src = 'images/logos/fv_verde1.png';
    }

    if (prevScrollPos > currentScrollPos) {
        navbar.classList.remove('navbar-hidden');
    } else {
        navbar.classList.add('navbar-hidden');
    }

    prevScrollPos = currentScrollPos;
});

document.addEventListener('mousemove', function(e) {
    if (e.clientY < 50) {
        navbar.classList.remove('navbar-hidden');
        clearTimeout(timeoutId);
    }
});

navbar.addEventListener('mouseleave', function() {
    if (window.pageYOffset !== 0) { 
        timeoutId = setTimeout(function() {
            navbar.classList.add('navbar-hidden');
        }, 2000);
    }
});

//SERVICIOS

// Selecciona el contenedor .servicios
const serviciosSection = document.querySelector('.servicios');

// Función que se ejecutará cuando el contenedor .servicios entre en la vista
const handleIntersection = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Si el contenedor .servicios está visible, activa la animación en las tarjetas
            const tarjetas = document.querySelectorAll('.contenedor_tarjeta');
            tarjetas.forEach((tarjeta, index) => {
                // Para las tarjetas impares, animación desde la izquierda
                if (index % 2 === 0) {
                    tarjeta.style.animation = 'slideInLeft 1s forwards';
                } else { // Para las tarjetas pares, animación desde la derecha
                    tarjeta.style.animation = 'slideInRight 1s forwards';
                }
            });
            observer.disconnect(); // Desconectar el observer una vez que la animación se haya ejecutado
        }
    });
};

// Crea un Intersection Observer
const observer = new IntersectionObserver(handleIntersection, {
    threshold: 0.5, // Se activa cuando al menos el 50% del contenedor es visible
});

// Comienza a observar el contenedor .servicios
observer.observe(serviciosSection);


