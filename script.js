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

    prevScrollPos = currentScrollPos;
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


//FLECHAS BLOG

document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.instagram-container');
    const cards = Array.from(container.children);
    const leftArrow = document.querySelector('.arrow.left');
    const rightArrow = document.querySelector('.arrow.right');

    let currentPage = 0;

    function getCardsPerPage() {
        return window.innerWidth <= 767 ? 1 : 3;
    }

    function updateView() {
        const perPage = getCardsPerPage();
        const totalPages = Math.ceil(cards.length / perPage);

        // Ocultar todas las tarjetas
        cards.forEach((card, i) => {
            card.style.display = 'none';
        });

        // Mostrar solo las de la página actual
        const start = currentPage * perPage;
        const end = start + perPage;
        cards.slice(start, end).forEach(card => {
            card.style.display = 'block';
        });

        // Desactivar flechas si estamos al límite
        leftArrow.disabled = currentPage === 0;
        rightArrow.disabled = currentPage >= totalPages - 1;
    }

    leftArrow.addEventListener('click', () => {
        if (currentPage > 0) {
            currentPage--;
            updateView();
        }
    });

    rightArrow.addEventListener('click', () => {
        const perPage = getCardsPerPage();
        if ((currentPage + 1) * perPage < cards.length) {
            currentPage++;
            updateView();
        }
    });

    window.addEventListener('resize', () => {
        currentPage = 0;
        updateView();
    });

    updateView();
});