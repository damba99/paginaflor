from pathlib import Path

base = '''<!DOCTYPE html>
<html class="dark" lang="es">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<link rel="stylesheet" href="/styles/servicios.css"/>
<title>{title}</title>
</head>
<body class="page-body">
<!-- NAVBAR -->
<nav class="navbar">
  <div class="navbar-container">
    <img class="navbar-logo" src="https://lh3.googleusercontent.com/aida/ADBb0uhx0IPoUvh9g0LaBw_qHe_mDwXdSOIlvCltaHrwgYYO8RDj4E8YEDTM99Ci2UcD9Tn5btxpY3Rh8d9AXkcofNbd36OLQCDiKQN11WqLtrfN64jWNDqHYa0wYA2sXE-AMa5aoNm0ze3It68Ro4eNDJ31btjbSFvhKkvrcqjAYEd3LTMacjUhNgRT2UzBll6eK4F_E3x5Pi_Iwv9cQZb9wvL8T88wnEKS8M-UmvRAq8Mt0IW_n_lUg1wt8WjtR1wmtjijDXFXAmh4Ud4"/>

    <div class="navbar-menu">
      <a class="nav-link" href="/index.html">Inicio</a>
      <a class="nav-link nav-link-active" href="/servicios.html">Servicios</a>
      <a class="nav-link" href="/nosotros.html">Quienes somos</a>
      <a class="nav-link" href="/contacto.html">Contacto</a>
    </div>
  </div>
</nav>

<main class="main-content">
<!-- Hero Section -->
<section class="hero-section">
  <div class="hero-container">
    <div class="hero-left">
      <span class="hero-subtitle">ESPECIALIDADES</span>
      <h1 class="hero-title">{hero_head} <br/> <span class="text-accent italic">{hero_accent}</span></h1>
    </div>
    <div class="hero-right">
      <p class="hero-description">{hero_description}</p>
      <div class="hero-divider"></div>
    </div>
  </div>
</section>

<!-- Services Section -->
<section class="services-section">
  <div class="services-container">
    <div class="services-header">
      <h2 class="services-title">Qué incluye este servicio</h2>
    </div>
    <div class="services-grid">
{cards}
    </div>
  </div>
</section>

<!-- CTA Section -->
<section class="cta-section">
  <div class="cta-container">
    <h2 class="cta-title">¿Necesitas asesoramiento?</h2>
    <p class="cta-description">Nuestro equipo está listo para acompañarte en cada paso, brindándote la seguridad legal que tu familia merece.</p>
    <div class="cta-buttons">
      <a class="btn btn-primary" href="https://wa.me/5493876570793" target="_blank"><span class="material-symbols-outlined">chat</span>WhatsApp</a>
      <a class="btn btn-secondary" href="/contacto.html"><span class="material-symbols-outlined">mail</span>Formulario de contacto</a>
    </div>
  </div>
</section>
</main>

<!-- FOOTER -->
<footer class="footer">
  <div class="footer-wrapper">
    <div class="footer-grid">
      <div>
        <h4 class="footer-title">Contacto</h4>
        <div class="footer-contact-list">
          <a href="tel:+5493876570793" class="footer-link"><span class="material-symbols-outlined">call</span><span>+54 9 387 657 0793</span></a>
          <a href="mailto:abogadaflorenciavelazques@gmail.com" class="footer-link"><span class="material-symbols-outlined">mail</span><span>abogadaflorenciavelazques@gmail.com</span></a>
          <a href="https://wa.me/5493876570793" target="_blank" class="footer-link"><span class="material-symbols-outlined">chat</span><span>WhatsApp</span></a>
          <div class="footer-item"><span class="material-symbols-outlined">schedule</span><span>Atención con turno previo</span></div>
        </div>
      </div>
      <div class="footer-center">
        <img class="footer-logo" src="images/sera_justicia-07.png"/>
        <div class="footer-social-icons">
          <a href="tel:+5493876570793" class="social-icon"><i class="fa-solid fa-phone"></i></a>
          <a href="https://www.instagram.com/abg.florencia/" class="social-icon"><i class="fa-brands fa-instagram"></i></a>
          <a href="https://www.facebook.com/profile.php?id=61558880305161" class="social-icon"><i class="fa-brands fa-facebook"></i></a>
          <a href="https://wa.me/5493876570793" class="social-icon"><i class="fa-brands fa-whatsapp"></i></a>
          <a href="mailto:abogadaflorenciavelazques@gmail.com" class="social-icon"><i class="fa-solid fa-envelope"></i></a>
          <a href="#" class="social-icon"><i class="fa-brands fa-tiktok"></i></a>
        </div>
      </div>
      <div class="footer-location">
        <h4 class="footer-title">Ubicación</h4>
        <a href="https://maps.app.goo.gl/goGy7ivc9SQD79vU8" target="_blank" class="footer-address">Barrio Mirasoles Manzana 498 A<br>casa 15, Ciudad de Salta</a>
        <p class="footer-company">Estudio Jurídico Integral<br>Velazques Ayarde</p>
      </div>
    </div>
  </div>
  <div class="footer-bottom"><p class="footer-copyright">© 2025 Estudio Jurídico Integral Velazques Ayarde. Todos los derechos reservados.</p></div>
</footer>
</html>
'''

def card(icon,title,desc):
    return f'      <div class="service-card">\n        <span class="material-symbols-outlined service-card-icon">{icon}</span>\n        <h3 class="service-card-title">{title}</h3>\n        <p class="service-card-text">{desc}</p>\n      </div>\n'

services = {
    'servicio_derecho_civil.html': {
      'title':'Derecho Civil | Florencia Velazques A.',
      'hero_head':'Derecho','hero_accent':'Civil',
      'hero_description':'Asesoramiento y representación en conflictos entre particulares, contratos, responsabilidad civil, sucesiones y derechos reales.',
      'cards':[('gavel','Contratos y obligaciones','Redacción, revisión y resolución de controversias contractuales.'),
               ('home_work','Locaciones y desalojo','Protección en arrendamientos, desalojos y derechos locativos.'),
               ('family_restroom','Sucesiones y herencias','Tramitación de declaratorias de herederos y reparto de bienes.'),
               ('car_crash','Daños y perjuicios','Reclamos civiles por accidentes y perjuicios patrimoniales.'),
               ('gavel','Responsabilidad civil','Demandas por incumplimientos y negligencias contractuales.'),
      ]
    },
    'servicio_derecho_administrativo.html': {
      'title':'Derecho Administrativo | Florencia Velazques A.',
      'hero_head':'Derecho','hero_accent':'Administrativo',
      'hero_description':'Consultoría en procedimientos administrativos, recursos, licitaciones y defensa judicial frente al Estado.',
      'cards':[('gavel','Recursos administrativos','Presentación de impugnaciones y recursos ante organismos públicos.'),
               ('account_balance','Contrataciones públicas','Asesoramiento en licitaciones, contratos y cumplimiento de normas.'),
               ('verified','Sanciones y multas','Defensa en procedimientos sancionatorios y reclamos de multas.'),
               ('document_scanner','Seguridad jurídica','Obtención de habilitaciones y certificaciones administrativas.'),
               ('balance','Derecho regulatorio','Cumplimiento de normativas sectoriales y auditorías legales.'),
      ]
    },
    'servicio_derecho_previsional.html': {
      'title':'Derecho Previsional | Florencia Velazques A.',
      'hero_head':'Derecho','hero_accent':'Previsional',
      'hero_description':'Gestión de jubilaciones, pensiones y prestaciones sociales con enfoque personalizado para garantizar derechos previsionales.',
      'cards':[('elderly','Jubilaciones y pensiones','Iniciación y mejora de expedientes jubilatorios y pensionarios.'),
               ('family_restroom','Asignaciones familiares','Trámites de asignaciones por hijo, maternal y subsidios estatales.'),
               ('medical_services','Incapacidades y subsidios','Acceso a beneficios por discapacidad y retiros por enfermedad.'),
               ('settings','Reajustes y actualizaciones','Reclamos por recálculo de haberes y reajustes incorrectos.'),
               ('support_agent','Asesoría permanente','Acompañamiento integral frente a Anses y organismos previsionales.'),
      ]
    },
    'servicio_marcas_y_patentes.html': {
      'title':'Marcas y Patentes | Florencia Velazques A.',
      'hero_head':'Protección de','hero_accent':'Marcas y Patentes',
      'hero_description':'Defensa y registro de propiedad intelectual para marcas, modelos y patentes en Argentina y el exterior.',
      'cards':[('branding_watermark','Registro de marcas','Búsqueda, presentación y seguimiento de inscripciones ante el INPI.'),
               ('lightbulb','Patentes y diseños','Protección de invenciones, diseños industriales y derechos de autor.'),
               ('gavel','Conflictos de propiedad','Litigios y mediaciones por uso indebido de signos distintivos.'),
               ('shield','Vigilancia de marcas','Monitoreo de terceros y oposición a inscripciones conflictivas.'),
               ('public','Licencias y cesiones','Redacción de acuerdos de transferencia de tecnología y know-how.'),
      ]
    },
    'servicio_derecho_tributario.html': {
      'title':'Derecho Tributario | Florencia Velazques A.',
      'hero_head':'Derecho','hero_accent':'Tributario',
      'hero_description':'Asesoramiento fiscal integral en materia impositiva, aduanera y planes de pagos para empresas y particulares.',
      'cards':[('receipt_long','Planificación fiscal','Estrategias para optimizar la carga impositiva con cumplimiento normativo.'),
               ('account_balance_wallet','Impuestos nacionales','Resolución de obligaciones de AFIP y presentación de declaraciones juradas.'),
               ('gavel','Litigios tributarios','Defensa en juicios fiscales y recursos administrativos tributarios.'),
               ('badge','Monotributo y autónomos','Regularización y asesoramiento contable para contribuyentes.'),
               ('balance','Auditorías fiscales','Representación frente a inspecciones y controles tributarios.'),
      ]
    },
    'servicio_extrajudiciales.html': {
      'title':'Mediación y Extrajudiciales | Florencia Velazques A.',
      'hero_head':'Soluciones','hero_accent':'Extrajudiciales',
      'hero_description':'Mediación y negociación para resolver conflictos sin juicio, con foco en resultados prácticos y ahorro de tiempo.',
      'cards':[('handshake','Mediaciones familiares','Acuerdos en divorcios, régimen de visitas y alimentos sin proceso judicial.'),
               ('people_alt','Negociación comercial','Reestructuración de deudas y acuerdos entre empresas y proveedores.'),
               ('gavel','Conciliaciones civiles','Gestión de acuerdos en reclamos de consumidores y responsabilidad civil.'),
               ('scale_balance','Acuerdos extrajudiciales','Redacción y formalización de compromisos con fuerza obligatoria.'),
               ('item_pending','Gestión de cobros','Recupero de créditos y ejecución de acuerdos consensuados.'),
      ]
    }
}

for filename, content in services.items():
    path = Path(filename)
    cards_markup = ''.join(card(icon,title,desc) for icon,title,desc in content['cards'])
    html = base.format(title=content['title'], hero_head=content['hero_head'], hero_accent=content['hero_accent'], hero_description=content['hero_description'], cards=cards_markup)
    path.write_text(html, encoding='utf-8')
    print(f'Updated {filename}')
