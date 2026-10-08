"""Shared helpers for generating the Lishe Kwa Mtoto static site.
Edit SITE_URL and SOCIAL below, then run:  python3 build.py
"""
import json, html
from datetime import date

# ---- Configuration ---------------------------------------------------------
SITE_URL = 'https://lishekwamtotokenya.org'   # CHANGE if the live domain differs (used for canonical + Open Graph URLs)
ORG_NAME = 'Lishe Kwa Mtoto'
ORG_LONG = 'Lishe Kwa Mtoto, a Ray of Hope Kenya Initiative'
EMAIL_INFO = 'info@lishekwamtotokenya.org'
EMAIL_PROGRAMS = 'programs@lishekwamtotokenya.org'
PHONE_DISPLAY = '+254 114 159862'
PHONE_TEL = '+254114159862'
WHATSAPP = 'https://wa.me/254114159862'
PAYBILL = '4677836'
# Only fill in real URLs. Empty entries are not rendered (no dead "#" links).
SOCIAL = {
    'facebook': '',   # e.g. https://www.facebook.com/yourpage
    'x-twitter': '',
    'instagram': '',
    'linkedin-in': '',
    'youtube': '',
}
# Optional extra international payment links (PayPal, Stripe Payment Link, Wise, etc.). Only filled entries are shown.
INTL_PAY_LINKS = {
    # 'PayPal': 'https://www.paypal.com/donate/?hosted_button_id=XXXX',
}
YEAR = date.today().year

META = json.load(open('img_meta.json'))


# ---- Images ----------------------------------------------------------------
def esc(s):
    return html.escape(str(s), quote=True)


def img(key, alt, *, sizes='100vw', pos=None, eager=False, cls='', fetch=None):
    """Responsive <img> with width/height, srcset (800w + 1600w) and lazy loading."""
    w, h = META[key]
    m = max(w, h)
    w800, h800 = round(w * 800 / m), round(h * 800 / m)
    srcset = f'img/{key}-800.webp {w800}w, img/{key}.webp {w}w'
    attrs = [f'src="img/{key}.webp"', f'srcset="{srcset}"', f'sizes="{sizes}"', f'width="{w}"', f'height="{h}"', f'alt="{esc(alt)}"', 'decoding="async"']
    if eager:
        attrs.append('fetchpriority="high"')
    else:
        attrs.append('loading="lazy"')
    if fetch:
        attrs.append(f'fetchpriority="{fetch}"')
    if pos:
        attrs.append(f'style="object-position:{pos}"')
    if cls:
        attrs.append(f'class="{cls}"')
    return '<img ' + ' '.join(attrs) + '>'


def media(key, alt, *, ar='4/3', pos='50% 50%', sizes='(min-width:900px) 50vw, 100vw', eager=False, extra='', cap=None):
    """Aspect-ratio controlled photo frame."""
    inner = f'<div class="media {extra}" style="--ar:{ar};--pos:{pos}">{img(key, alt, sizes=sizes, eager=eager)}</div>'
    if cap:
        return f'<figure>{inner}<figcaption class="caption">{cap}</figcaption></figure>'
    return inner


# ---- Navigation ------------------------------------------------------------
NAV = [
    ('about', 'About', 'about.html', None),
    ('work', 'Our Work', 'programs.html', [
        ('programs', 'All Programs', 'programs.html'),
        ('school-feeding', 'School Feeding', 'school-feeding.html'),
        ('emergency', 'Emergency Response', 'emergency.html'),
    ]),
    ('stories', 'Stories', 'stories.html', None),
    ('news', 'News', 'blog.html', None),
    ('gallery', 'Gallery', 'gallery-transnzoia.html', [
        ('gallery-transnzoia', 'Trans Nzoia County', 'gallery-transnzoia.html'),
        ('gallery-westpokot', 'West Pokot County', 'gallery-westpokot.html'),
    ]),
    ('volunteer', 'Volunteer', 'volunteer.html', None),
    ('contact', 'Contact', 'contact.html', None),
]


def group_of(key):
    for k, _, _, sub in NAV:
        if sub and any(s[0] == key for s in sub):
            return k
    return key


def header(current):
    grp = group_of(current)
    items = []
    for k, label, href, sub in NAV:
        if sub:
            cur = ' is-current' if grp == k else ''
            links = []
            for sk, l, h in sub:
                ac = ' aria-current="page"' if sk == current else ''
                links.append('<a href="' + h + '"' + ac + '>' + l + '</a>')
            items.append(
                '<div class="nav__item' + cur + '"><button class="nav__trigger" type="button" aria-expanded="false" aria-haspopup="true">' + label +
                '<i class="fa-solid fa-chevron-down" aria-hidden="true"></i></button><div class="nav__menu">' + ''.join(links) + '</div></div>')
        else:
            ac = ' aria-current="page"' if current == k else ''
            items.append('<a class="nav__link" href="' + href + '"' + ac + '>' + label + '</a>')
    mobile = ['<a href="index.html">Home</a>']
    for k, label, href, sub in NAV:
        if k == 'gallery':
            for _, l, h in sub:
                mobile.append('<a href="' + h + '">' + l.replace(' County', '') + ' Gallery</a>')
            continue
        mobile.append('<a href="' + href + '">' + label + '</a>')
        if sub:
            for _, l, h in sub:
                if h != href:
                    mobile.append('<a class="is-sub" href="' + h + '">' + l + '</a>')
    return f'''<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="container container--wide site-header__inner">
    <a class="brand" href="index.html" aria-label="{ORG_NAME} home">
      <img src="img/brand/lishe-mark.webp" alt="" width="46" height="46">
      <span class="brand__name">Lishe Kwa Mtoto<small>A Ray of Hope Kenya Initiative</small></span>
    </a>
    <nav class="nav" aria-label="Primary">{''.join(items)}</nav>
    <div class="header-actions">
      <a class="btn btn--primary btn--sm" href="donate.html">Donate</a>
      <button class="nav-toggle" id="navToggle" type="button" aria-expanded="false" aria-controls="mobileNav" aria-label="Open menu"><i class="fa-solid fa-bars" aria-hidden="true"></i></button>
    </div>
  </div>
</header>
<nav class="mobile-nav" id="mobileNav" aria-label="Mobile">{''.join(mobile)}<a class="btn btn--primary btn--block" href="donate.html">Donate</a></nav>'''


def footer(news=True):
    social = ''.join(
        f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n.replace("-", " ").title()}"><i class="fa-brands fa-{n}" aria-hidden="true"></i></a>'
        for n, u in SOCIAL.items() if u)
    social += f'<a href="{WHATSAPP}" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i></a>'
    social += f'<a href="mailto:{EMAIL_INFO}" aria-label="Email"><i class="fa-solid fa-envelope" aria-hidden="true"></i></a>'
    newsblock = '''<div class="footer__news">
      <div><h4>Stay in the loop</h4><p>Monthly impact updates and field stories. No spam.</p></div>
      <form data-newsletter novalidate>
        <label class="sr-only" for="fnEmail">Email address</label>
        <input type="email" id="fnEmail" placeholder="Your email address" autocomplete="email" required>
        <button class="btn btn--primary" type="submit">Subscribe</button>
        <p class="form-status" role="status"></p>
      </form>
    </div>''' if news else ''
    return f'''<footer class="site-footer">
  <div class="container container--wide">
    <div class="footer__top">
      <div class="footer__brand">
        <img src="img/brand/lishe-logo.webp" alt="Lishe Kwa Mtoto, a Ray of Hope Kenya Initiative" width="120" height="134" loading="lazy">
        <p>Nourishing children through daily school meals, emergency food response and nutrition education in Kenya.</p>
        <a class="btn btn--primary" href="donate.html">Support Lishe</a>
        <div class="social">{social}</div>
      </div>
      <nav class="footer__col" aria-label="Programs">
        <h4>Our work</h4>
        <ul>
          <li><a href="programs.html">All programs</a></li>
          <li><a href="school-feeding.html">School Feeding</a></li>
          <li><a href="emergency.html">Emergency Response</a></li>
          <li><a href="gallery-transnzoia.html">Trans Nzoia gallery</a></li>
          <li><a href="gallery-westpokot.html">West Pokot gallery</a></li>
        </ul>
      </nav>
      <nav class="footer__col" aria-label="Organization">
        <h4>Organization</h4>
        <ul>
          <li><a href="about.html">About us</a></li>
          <li><a href="about.html#partners">Partners</a></li>
          <li><a href="stories.html">Stories</a></li>
          <li><a href="blog.html">News</a></li>
          <li><a href="volunteer.html">Volunteer</a></li>
          <li><a href="donate.html">Donate</a></li>
        </ul>
      </nav>
      <div class="footer__col">
        <h4>Contact</h4>
        <address>
          <ul>
            <li><a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a></li>
            <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
            <li>Kitale, Trans Nzoia County, Kenya</li>
            <li><a href="contact.html">Send a message</a></li>
          </ul>
        </address>
      </div>
    </div>
    {newsblock}
    <div class="footer__bottom">
      <span>&copy; {YEAR} Lishe Kwa Mtoto, a Ray of Hope Foundation Kenya initiative. All rights reserved.</span>
      <ul><li><a href="admin-login.html">Staff login</a></li></ul>
    </div>
  </div>
</footer>'''


# ---- Page shell ------------------------------------------------------------
def schema():
    same = [u for u in SOCIAL.values() if u]
    data = {
        '@context': 'https://schema.org',
        '@type': 'NGO',
        'name': ORG_NAME,
        'alternateName': ORG_LONG,
        'url': SITE_URL + '/',
        'logo': SITE_URL + '/img/brand/lishe-logo.webp',
        'description': 'Lishe Kwa Mtoto provides daily nutritious school meals, emergency food response and nutrition education for children in Kenya.',
        'foundingDate': '2024',
        'email': EMAIL_INFO,
        'telephone': PHONE_TEL,
        'address': {'@type': 'PostalAddress', 'addressLocality': 'Kitale', 'addressRegion': 'Trans Nzoia County', 'addressCountry': 'KE'},
        'areaServed': ['Trans Nzoia County', 'West Pokot County', 'Kenya'],
    }
    if same:
        data['sameAs'] = same
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'


def page(fname, key, title, desc, body, *, og_image='img/og-lishe.jpg', preload='', scripts='', extra_head='', with_schema=False, robots='index,follow', nav_key=None, news=True):
    url = SITE_URL + ('/' if fname == 'index.html' else '/' + fname)
    og = SITE_URL + '/' + og_image
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0b5d3b">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{ORG_NAME}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{og}">
<link rel="icon" href="favicon.png" type="image/png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<link rel="stylesheet" href="style.css">
{preload}{extra_head}{schema() if with_schema else ''}
</head>
<body>
{header(nav_key or key)}
<main id="main">
{body}
</main>
{footer(news)}
<script src="firebase-init.js" defer></script>
<script src="shared.js" defer></script>
{scripts.replace('<script src="firebase-init.js" defer></script>', '')}
</body>
</html>
'''


# ---- Reusable blocks -------------------------------------------------------
def page_hero(img_key, alt, eyebrow, title, sub, *, pos='50% 40%', buttons='', cls='', tall=False):
    c = 'phero' + (' phero--tall' if tall else '') + (' ' + cls if cls else '')
    return f'''<section class="{c}">
  {img(img_key, alt, sizes='100vw', pos=pos, eager=True, cls='phero__img')}
  <div class="phero__content"><div class="container">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    <p class="phero__sub">{sub}</p>
    {f'<div class="btn-row">{buttons}</div>' if buttons else ''}
  </div></div>
</section>'''


def split_hero(img_key, alt, eyebrow, title, sub, *, pos='50% 40%', buttons='', reverse=False, dark=False):
    cls = ('shero' + (' shero--reverse' if reverse else '') + (' shero--dark on-dark' if dark else ''))
    return f'''<section class="{cls}">
  <div class="shero__grid">
    <div class="shero__text">
      <span class="eyebrow">{eyebrow}</span>
      <h1>{title}</h1>
      <p class="lead">{sub}</p>
      {f'<div class="btn-row">{buttons}</div>' if buttons else ''}
    </div>
    <div class="shero__media">{img(img_key, alt, sizes='(min-width:900px) 52vw, 100vw', pos=pos, eager=True)}</div>
  </div>
</section>'''


def cta(img_key, title, text, buttons, *, pos='50% 40%', alt=''):
    return f'''<section class="cta on-dark">
  {img(img_key, alt, sizes='100vw', pos=pos, cls='cta__img')}
  <div class="container">
    <h2>{title}</h2>
    <p>{text}</p>
    <div class="btn-row">{buttons}</div>
  </div>
</section>'''


def cta_bar(title, text, buttons):
    return f'''<section class="cta-bar on-dark">
  <div class="container"><div class="cta-bar__inner">
    <div><h2>{title}</h2><p>{text}</p></div>
    <div class="btn-row">{buttons}</div>
  </div></div>
</section>'''


def partners_block():
    logos = [
        ('img/partners/spread-truth.webp', 'Spread Truth', True),
        ('img/partners/step-30.webp', 'Step 30', False),
        ('img/partners/veko-sounds.webp', 'Veko Sounds', False),
        ('img/partners/vessel-of-hope.webp', 'Vessel of Hope', False),
        ('img/partners/h2o-water-drops.png', 'Water Drops', False),
    ]
    tiles = ''.join(
        f'<li class="partner reveal" style="--d:{i*0.06}s"><div class="partner__logo{" partner__logo--sm" if sm else ""}"><img src="{src}" alt="{n} logo" loading="lazy"></div><span class="partner__name">{n}</span></li>'
        for i, (src, n, sm) in enumerate(logos))
    return f'''<section class="section section--white" id="partners" aria-labelledby="partners-h">
  <div class="container">
    <div class="head">
      <div><span class="eyebrow">Partners and supporters</span><h2 id="partners-h">Together, we reach more children.</h2></div>
      <p class="lead">Organisations and communities who stand alongside Lishe Kwa Mtoto.</p>
    </div>
    <ul class="partner-grid">{tiles}</ul>
    <p class="caption" style="margin-top:20px">Interested in partnering with us? <a href="contact.html" style="color:var(--green);font-weight:700;text-decoration:underline;text-underline-offset:3px">Get in touch</a>.</p>
  </div>
</section>'''


def subnav(items):
    links = ''.join(f'<li><a href="#{i}">{l}</a></li>' for i, l in items)
    return f'<nav class="subnav" aria-label="On this page"><div class="container"><ul>{links}</ul></div></nav>'


def faq(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'


def write(fname, content):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
