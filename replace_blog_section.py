from pathlib import Path
p = Path('index.html')
t = p.read_text('utf-8')
s = t.find('<section id="blog"')
if s == -1:
    raise ValueError('blog section not found')
c = t.find('<section id="contacto"', s)
if c == -1:
    raise ValueError('contacto section not found')
new = '''    <section id="blog" class="section blog">
        <div class="separador">
            <h2>REDES</h2>
        </div>
        <div class="redes-grid">
            <a class="red-social-card" href="https://www.instagram.com/abg.florencia/" target="_blank">
                <i class="fab fa-instagram"></i>
                <h3>Instagram</h3>
                <p>Producción constante de contenido útil, casos de éxito y tips legales.</p>
            </a>
            <a class="red-social-card" href="https://www.facebook.com/profile.php?id=61558880305161" target="_blank">
                <i class="fab fa-facebook"></i>
                <h3>Facebook</h3>
                <p>Actualizaciones de servicios y nuestro trabajo comunitario.</p>
            </a>
            <a class="red-social-card" href="https://wa.me/5493876570793" target="_blank">
                <i class="fab fa-whatsapp"></i>
                <h3>WhatsApp</h3>
                <p>Contacto rápido, turnos y consultas breves.</p>
            </a>
            <a class="red-social-card" href="mailto:abogadaflorenciavelazques@gmail.com" target="_blank">
                <i class="fas fa-envelope"></i>
                <h3>Email</h3>
                <p>Consultas formales y envío de documentación.</p>
            </a>
        </div>
        <div class="redes-highlight">
            <h3>Últimas novedades</h3>
            <p>Visita nuestras redes para ver ejemplos de asesorías y resultados.</p>
        </div>
    </section>
''' 
p.write_text(t[:s] + new + t[c:], 'utf-8')
print('updated')
