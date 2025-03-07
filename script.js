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
        logoImg.src = 'images/logos/fv_verde1.png';
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

//CARRUSEL

