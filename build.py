"""Generates the Lishe Kwa Mtoto static site. Run: python3 build.py
Pages are static HTML (nav/footer included) so they work without JavaScript and are fully crawlable.
Edit build_lib.py for SITE_URL, contact details and social links."""
import shutil, os, re
from build_lib import *
from pages_home import build_home
from pages_core import build_about, build_programs, build_school, build_emergency
from pages_content import build_stories, build_blog, build_gallery_tn, build_gallery_wp
from pages_forms import build_donate, build_volunteer, build_contact

PAGES = {
    'index.html': build_home, 'about.html': build_about, 'programs.html': build_programs,
    'school-feeding.html': build_school, 'emergency.html': build_emergency, 'stories.html': build_stories,
    'blog.html': build_blog, 'gallery-transnzoia.html': build_gallery_tn, 'gallery-westpokot.html': build_gallery_wp,
    'donate.html': build_donate, 'volunteer.html': build_volunteer, 'contact.html': build_contact,
}
for name, fn in PAGES.items():
    write(name, fn())
    print('built', name)

urls = ''.join(f'<url><loc>{SITE_URL}/{"" if n == "index.html" else n}</loc></url>' for n in PAGES)
write('sitemap.xml', f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
write('robots.txt', f'User-agent: *\nAllow: /\nDisallow: /admin-login.html\nDisallow: /admin-dashboard.html\nSitemap: {SITE_URL}/sitemap.xml\n')
