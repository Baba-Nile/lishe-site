from build_lib import *

ARROW = '<i class="fa-solid fa-arrow-right" aria-hidden="true"></i>'


def build_stories():
    def entry(meta, quote, paras, name, role, key, alt, pos, ar='4/5'):
        ps = ''.join(f'<p>{p}</p>' for p in paras)
        return f'''<article class="story-entry reveal">
  <div class="story-entry__aside"><span class="meta">{meta}</span><blockquote>{quote}</blockquote>
    <div style="margin-top:24px">{media(key, alt, ar=ar, pos=pos, sizes='(min-width:900px) 32vw, 100vw')}</div></div>
  <div class="story-entry__body">{ps}<div class="byline"><strong>{name}</strong><span>{role}</span></div></div>
</article>'''
    body = f'''
{split_hero('tn/cherubai1', 'A crowd of schoolchildren gathered in a school compound', 'Stories', 'Stories of change.',
            'The greatest measure of our success is found not in numbers, but in lives transformed.', pos='50% 45%', reverse=True)}

<section class="section" aria-labelledby="lead-h">
  <div class="container">
    <div class="lead-story">
      <div class="reveal">
        <span class="eyebrow" id="lead-h">Featured story &middot; Trans Nzoia County</span>
        <blockquote>"I used to faint in class. Now I'm top of my school."</blockquote>
        <div class="prose">
          <p>Faith Chebet is nine years old and attends Cherang'any Primary School in Trans Nzoia County. Before Lishe Kwa Mtoto began serving meals at her school in early 2024, Faith's mother, a casual labourer, would often send her to school with nothing more than a cup of weak tea. By mid-morning, Faith would be unable to concentrate. Her teacher, Mr. Barasa, recalls that she fainted twice in a single term from hunger.</p>
          <p>Six months after the feeding programme started, Faith's transformation was remarkable. Her attendance, previously irregular, became perfect. She moved from the bottom of her class to the top five. Her favourite day, she says, is when the cooks prepare githeri with carrots, a meal she calls "the best food in the world."</p>
          <p>"A meal changed everything," says her mother Grace. "She comes home happy now. She asks to do her homework. She wants to become a doctor."</p>
        </div>
        <div class="byline"><strong>Grace Wanjiru</strong><span>Faith's mother, Trans Nzoia County</span></div>
      </div>
      <div class="reveal" style="--d:.1s">
        {media('tn/cherubai6', 'Schoolchildren in bright clothing raise their hands and smile', ar='4/5', pos='45% 35%', sizes='(min-width:900px) 40vw, 100vw', cap='Learners at a partner school in Trans Nzoia County. Illustrative photograph.')}
      </div>
    </div>
  </div>
</section>

<section class="section--sm" aria-label="More stories" style="padding-top:0">
  <div class="container">
    {entry('Head teacher &middot; Trans Nzoia', '"Our school attendance jumped from 61% to 94% in one term."',
           ['Mr. Samuel Barasa has been head teacher at Cherang\'any Primary for 11 years. He watched generations of children arrive hungry and struggle to learn. When the Lishe Kwa Mtoto program began in January 2024, he tracked the attendance data carefully. By April, the numbers told a story he had never seen before: from 61% daily attendance to 94%, a transformation he credits entirely to the morning meal.',
            '"The children come eager to learn. They arrive early. They stay engaged through to lunch. Teachers are happier because they are actually teaching, not managing hungry, restless children."'],
           'Mr. Samuel Barasa', 'Head Teacher, Cherang\'any Primary', 'tn/liavo4', 'Pupils in red uniforms queue with bowls at a serving point', '50% 50%', '4/3')}
    {entry('Community cook &middot; West Pokot', '"This program gave me a job and gave children a future."',
           ['Mary Rotich is one of 60 community cooks employed by Lishe Kwa Mtoto across our partner schools. A widow with four children of her own, Mary was struggling to find stable income in Kapenguria, West Pokot, before she was trained and hired as a school cook in 2024.',
            '"I wake up at 5 AM to prepare the porridge. By the time children arrive, everything is ready. I know every child by name. When I see them eat, when I see them smile, I feel like I am doing God\'s work."'],
           'Mary Rotich', 'Community Cook, Kapenguria, West Pokot', 'west/simitei-13', 'A woman serves porridge from a large pot to schoolchildren', '25% 40%', '4/3')}
    {entry('Farmer supplier &middot; Kitale', '"They buy from us at fair prices. Our farm is thriving."',
           ['Joseph Wekesa farms 3 acres of maize and soybeans in Kitale. When Lishe Kwa Mtoto approached his cooperative in mid-2024 to supply ingredients for the Lishe Mix, it changed his household\'s economic trajectory. He now supplies 2 tonnes of maize per month at a guaranteed price, removing the uncertainty of market fluctuations.',
            '"Before, I was selling to middlemen at whatever price they offered. Now I have a contract. My children are also in school, and eating better themselves."'],
           'Joseph Wekesa', 'Smallholder Farmer, Kitale, Trans Nzoia', 'tn/20250708-130128', 'Students stand beside sacks of Lishe Mix flour', '50% 55%', '4/3')}
    {entry('County official &middot; Trans Nzoia', '"The ripple effect is remarkable."',
           ['Dr. Asha Mwangi, Director of Education for Trans Nzoia County, has partnered with Lishe Kwa Mtoto since the program\'s inception. She says the data from county schools is unambiguous: schools participating in the feeding program consistently outperform non-participant schools on attendance, retention and end-of-term assessments.',
            '"When children eat, they stay in school. When they stay in school, entire families break out of poverty cycles. This is not charity. It is the most efficient investment we know in human capital."'],
           'Dr. Asha Mwangi', 'Director of Education, Trans Nzoia County', 'tn/20250708-125817', 'School staff and partners gather beside a vehicle and bags of Lishe Mix', '50% 50%', '4/3')}
    <p class="disclosure">Photographs show learners and partners at Lishe Kwa Mtoto programmes and are illustrative; they do not necessarily depict the people quoted.</p>
  </div>
</section>

{cta('west/t-2', 'Help write the next story.', 'Every meal adds a chapter to a child\'s story. Your support keeps the next one going.',
     '<a class="btn btn--primary" href="donate.html">Donate</a><a class="btn btn--secondary btn--light" href="volunteer.html">Volunteer with us</a>', pos='50% 35%')}
'''
    return page('stories.html', 'stories', 'Stories of Change | Lishe Kwa Mtoto',
                'Read stories from learners, teachers, cooks, farmers and county partners whose lives are changing through school meals from Lishe Kwa Mtoto in Kenya.', body)


def build_blog():
    body = f'''
<section class="section--sm" style="padding-block:clamp(48px,6vw,88px) 0">
  <div class="container">
    <span class="eyebrow">Newsroom</span>
    <h1 style="max-width:14em">News and updates from the field.</h1>
    <p class="lead" style="margin-top:20px;max-width:36em">Updates, impact reports and stories from our work feeding Kenya's children.</p>
  </div>
</section>
<section class="section" style="padding-top:clamp(32px,4vw,56px)">
  <div class="container">
    <div class="filters" role="group" aria-label="Filter posts by category">
      <button class="filter active" type="button" data-cat="all" aria-pressed="true">All posts</button>
      <button class="filter" type="button" data-cat="feeding" aria-pressed="false">School Feeding</button>
      <button class="filter" type="button" data-cat="emergency" aria-pressed="false">Emergency Response</button>
      <button class="filter" type="button" data-cat="impact" aria-pressed="false">Impact Reports</button>
      <button class="filter" type="button" data-cat="community" aria-pressed="false">Community</button>
    </div>
    <div id="blogGrid" aria-live="polite"><div class="empty-note"><p>Loading posts&hellip;</p></div></div>

    <div class="newsletter">
      <div><h2>Stay updated.</h2><p>Get monthly impact reports, field stories and ways to help, straight to your inbox.</p></div>
      <div>
        <form class="newsletter-form" id="newsletterForm" novalidate>
          <label class="sr-only" for="nlEmail">Email address</label>
          <input type="email" id="nlEmail" name="email" placeholder="Your email address" autocomplete="email" required>
          <button class="btn btn--primary" type="submit">Subscribe</button>
        </form>
        <p class="form-status" id="nlStatus" role="status"></p>
      </div>
    </div>
  </div>
</section>

<dialog id="postDialog" aria-labelledby="postTitle" style="max-width:min(760px,calc(100vw - 24px));width:100%;border:0;padding:0;background:var(--white)">
  <div style="padding:clamp(24px,4vw,48px);position:relative">
    <button type="button" id="postClose" class="btn btn--secondary btn--sm" style="position:absolute;top:12px;right:12px" aria-label="Close article"><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>
    <div id="postBody"></div>
  </div>
</dialog>
'''
    scripts = '''<script src="firebase-init.js" defer></script>
<script>
document.addEventListener('DOMContentLoaded', function () {
  var F = window.LisheFirebase, e = F.esc;
  var grid = document.getElementById('blogGrid'), posts = [], active = 'all';
  var FALLBACK = 'img/west/t-8-800.webp';
  function fmt(ts) { return ts && ts.toDate ? ts.toDate().toLocaleDateString('en-KE', { day: 'numeric', month: 'long', year: 'numeric' }) : ''; }
  function meta(p) { return '<div class="post__meta"><span class="post__cat">' + e(p.categoryLabel || 'News') + '</span><span class="meta">' + e(fmt(p.publishedAt)) + '</span>' + (p.author ? '<span class="meta">By ' + e(p.author) + '</span>' : '') + '</div>'; }
  function card(p, lead) {
    return '<article class="post' + (lead ? ' post--lead' : '') + '"><div class="media"><img src="' + e(p.imageUrl || FALLBACK) + '" alt="" loading="lazy"></div>' + meta(p) +
      '<h3><a href="?post=' + e(p.id) + '" data-post="' + e(p.id) + '">' + e(p.title || 'Untitled') + '</a></h3><p>' + e(p.excerpt || '') + '</p>' +
      '<p style="margin-top:14px"><a class="link-arrow" href="?post=' + e(p.id) + '" data-post="' + e(p.id) + '">Read article ' + '<i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a></p></article>';
  }
  function render() {
    var list = active === 'all' ? posts : posts.filter(function (p) { return p.category === active; });
    if (!list.length) { grid.innerHTML = '<div class="empty-note"><p>No posts in this category yet. Check back soon.</p></div>'; return; }
    var html = '<div class="news news--featured" style="margin-bottom:clamp(32px,4vw,56px)">' + card(list[0], true) + '<div class="post-stack">';
    list.slice(1, 3).forEach(function (p) { html += card(p, false); });
    html += '</div></div>';
    if (list.length > 3) { html += '<div class="news">'; list.slice(3).forEach(function (p) { html += card(p, false); }); html += '</div>'; }
    grid.innerHTML = html;
  }
  document.querySelectorAll('.filter').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('.filter').forEach(function (x) { var on = x === b; x.classList.toggle('active', on); x.setAttribute('aria-pressed', String(on)); });
      active = b.getAttribute('data-cat'); render();
    });
  });

  var dlg = document.getElementById('postDialog');
  function openPost(id) {
    var p = posts.filter(function (x) { return x.id === id; })[0]; if (!p || !dlg.showModal) return;
    var paras = String(p.content || p.excerpt || '').split(/\\n{2,}|\\n/).filter(Boolean).map(function (t) { return '<p>' + e(t) + '</p>'; }).join('');
    document.getElementById('postBody').innerHTML = meta(p) + '<h2 id="postTitle" style="margin:8px 0 24px;font-size:var(--fs-h2)">' + e(p.title || 'Untitled') + '</h2>' +
      (p.imageUrl ? '<div class="media" style="--ar:16/9;margin-bottom:24px"><img src="' + e(p.imageUrl) + '" alt=""></div>' : '') + '<div class="prose">' + paras + '</div>';
    dlg.showModal();
  }
  grid.addEventListener('click', function (ev) { var a = ev.target.closest('[data-post]'); if (a) { ev.preventDefault(); openPost(a.getAttribute('data-post')); } });
  document.getElementById('postClose').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('click', function (ev) { if (ev.target === dlg) dlg.close(); });

  F.db().then(function (db) {
    db.collection('blogPosts').where('status', '==', 'published').orderBy('publishedAt', 'desc').onSnapshot(function (snap) {
      posts = snap.docs.map(function (d) { var o = d.data(); o.id = d.id; return o; });
      render();
      var q = new URLSearchParams(location.search).get('post'); if (q) { openPost(q); history.replaceState(null, '', location.pathname); }
    }, function (err) { console.error('Blog:', err.message); grid.innerHTML = '<div class="empty-note"><p>Posts could not be loaded. Please try again later.</p></div>'; });
  }).catch(function () { grid.innerHTML = '<div class="empty-note"><p>Posts could not be loaded. Please try again later.</p></div>'; });

  // Newsletter (same Firestore collection as before)
  var form = document.getElementById('newsletterForm'), status = document.getElementById('nlStatus');
  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var email = document.getElementById('nlEmail').value.trim();
    if (!/^\\S+@\\S+\\.\\S+$/.test(email)) { status.textContent = 'Please enter a valid email address.'; return; }
    status.textContent = 'Subscribing...';
    F.db().then(function (db) {
      return db.collection('subscribers').add({ email: email, subscribedAt: firebase.firestore.FieldValue.serverTimestamp(), source: 'blog_page' });
    }).then(function () { status.textContent = 'Subscribed. Thank you.'; form.reset(); })
      .catch(function () { status.textContent = 'Subscription failed. Please try again.'; });
  });
});
</script>'''
    return page('blog.html', 'news', 'News and Updates | Lishe Kwa Mtoto Newsroom',
                'Impact reports, field updates and stories from Lishe Kwa Mtoto\'s school feeding and emergency response work across Kenya.', body, scripts=scripts, news=False)


def gallery_items(items):
    out = []
    for key, cap, cls, pos, cat in items:
        w, h = META[key]
        m = max(w, h)
        w800 = round(w * 800 / m)
        out.append(f'''<button type="button" class="g-item {cls}" data-lightbox data-cat="{cat}" data-full="img/{key}.webp" data-alt="{esc(cap)}" data-caption="{esc(cap)}" aria-label="Open photograph: {esc(cap)}">
<img src="img/{key}-800.webp" srcset="img/{key}-800.webp {w800}w, img/{key}.webp {w}w" sizes="(min-width:900px) 25vw, 50vw" width="{w}" height="{h}" alt="{esc(cap)}" loading="lazy" decoding="async" style="--pos:{pos}">
<span class="g-item__cap">{esc(cap)}</span></button>''')
    return '\n'.join(out)


def gallery_page(fname, key, title, desc, county, intro, hero_keys, items, other, filters=None):
    mosaic = ''.join(img(k, a, sizes='(min-width:900px) 25vw, 50vw', pos=p, eager=(i == 0)) for i, (k, a, p) in enumerate(hero_keys))
    fb = ''
    if filters:
        fb = '<div class="filters" role="group" aria-label="Filter photographs">' + ''.join(
            f'<button class="filter{" active" if i == 0 else ""}" type="button" data-filter="{c}" aria-pressed="{"true" if i == 0 else "false"}">{l}</button>' for i, (c, l) in enumerate(filters)) + '</div>'
    body = f'''
<section class="ghero on-dark">
  <div class="ghero__mosaic" aria-hidden="false">{mosaic}</div>
  <div class="container"><div class="ghero__text">
    <div><span class="eyebrow eyebrow--light">Photo gallery</span><h1>{county}</h1></div>
    <p class="lead">{intro}</p>
  </div></div>
</section>
<section class="section" style="padding-top:clamp(32px,4vw,56px)">
  <div class="container container--wide">
    <div class="gallery-bar">{fb}<a class="link-arrow" href="{other[0]}">{other[1]} {ARROW}</a></div>
    <div class="gallery">{gallery_items(items)}</div>
  </div>
</section>
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photograph viewer">
  <button type="button" class="lb-close" aria-label="Close"><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>
  <button type="button" class="lb-prev" aria-label="Previous photograph"><i class="fa-solid fa-chevron-left" aria-hidden="true"></i></button>
  <button type="button" class="lb-next" aria-label="Next photograph"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i></button>
  <figure><img src="" alt=""><figcaption></figcaption></figure>
</div>
{cta_bar('Help us create more moments like these.', 'Every meal served is a child ready to learn.',
     '<a class="btn btn--primary" href="donate.html">Donate now</a><a class="btn btn--secondary btn--light" href="' + other[0] + '">' + other[1] + '</a>')}
'''
    return page(fname, key, title, desc, body, og_image='img/og-lishe.jpg')


def build_gallery_tn():
    items = [
        ('tn/cherubai3', 'Pupils raise their hands at a partner school', 'g-big', '50% 40%', 'all'),
        ('tn/liavo3', 'Children queue to be served porridge', 'g-wide', '50% 50%', 'all'),
        ('tn/20250708-130647', 'A pupil with her meal beside a Lishe banner', 'g-tall', '50% 35%', 'all'),
        ('tn/liavo1', 'A child receives a bowl of porridge', '', '50% 45%', 'all'),
        ('tn/20250708-125817', 'Lishe Mix handed over at a school event', 'g-wide', '50% 55%', 'all'),
        ('tn/cherubai1', 'Pupils gather in the school compound', 'g-wide', '50% 45%', 'all'),
        ('tn/20250926-wa0132' if False else 'tn/img-20250926-wa0132', 'A pupil holds a bowl at the serving pot', 'g-tall', '50% 30%', 'all'),
        ('tn/liavo6', 'Serving porridge from a large pot', '', '50% 50%', 'all'),
        ('tn/20250708-130128', 'Students beside sacks of Lishe Mix flour', 'g-tall', '50% 50%', 'all'),
        ('tn/liavo4', 'Learners at the serving point', 'g-wide', '50% 50%', 'all'),
        ('tn/20250708-131332', 'Pupils line up with bowls', 'g-tall', '50% 40%', 'all'),
        ('tn/img-20250926-wa0129', 'Children with bowls beside the school building', 'g-wide', '40% 50%', 'all'),
        ('tn/liavo2', 'A community cook serves from a large pot', '', '50% 50%', 'all'),
        ('tn/cherubai6', 'Pupils celebrating at a partner school', '', '45% 40%', 'all'),
        ('tn/20250708-130156', 'School staff and partners with bags of Lishe Mix', 'g-wide', '50% 45%', 'all'),
        ('tn/img-20250926-wa0128', 'Children queue for their meal', 'g-tall', '50% 35%', 'all'),
        ('tn/img-20250926-wa0131', 'Children holding out bowls', 'g-wide', '50% 50%', 'all'),
        ('tn/library', 'A well-stocked library room', '', '50% 50%', 'all'),
    ]
    return gallery_page('gallery-transnzoia.html', 'gallery-transnzoia', 'Trans Nzoia Gallery | School Feeding Photographs',
                        'Photographs of school feeding, Lishe Mix distribution and community activity from Lishe Kwa Mtoto in Trans Nzoia County, Kenya.',
                        'Trans Nzoia County', 'Documenting our work across Kitale, Cherang\'any and the wider Trans Nzoia region, 2024 to 2025.',
                        [('tn/cherubai3', 'Pupils raise their hands', '50% 40%'), ('tn/liavo3', 'Children queue for porridge', '50% 50%'), ('tn/liavo1', 'A child receives porridge', '50% 45%'), ('tn/cherubai2', 'Happy pupils', '45% 40%'), ('tn/liavo4', 'Learners with bowls', '50% 50%')],
                        items, ('gallery-westpokot.html', 'West Pokot gallery'))


def build_gallery_wp():
    F, C = 'feeding', 'community'
    items = [
        ('west/simitei-1', 'Children eating their morning meal along a school wall', 'g-big', '30% 50%', F),
        ('west/t-7', 'A schoolgirl smiles with her bowl of porridge', 'g-tall', '50% 30%', F),
        ('west/simitei-2', 'Pupils on a bench with bowls and cups', 'g-wide', '50% 40%', F),
        ('west/simitei-13', 'A community cook serves porridge', '', '25% 45%', C),
        ('west/t-1', 'A boy smiles beside the serving pot', 'g-tall', '50% 30%', F),
        ('west/simitei-7', 'A community meeting in a classroom', 'g-wide', '50% 50%', C),
        ('west/t-4', 'Children line up with cups and bowls', 'g-wide', '40% 50%', F),
        ('west/simitei-10', 'Pupils eating beside the school building', 'g-tall', '50% 40%', F),
        ('west/t-9', 'A child enjoys a meal outdoors', 'g-tall', '50% 35%', F),
        ('west/simitei-5', 'Children hold up colourful bowls', 'g-wide', '50% 40%', F),
        ('west/simitei-8', 'A workshop gathered in a school hall', 'g-tall', '50% 50%', C),
        ('west/t-6', 'Pupils seated on a wall with their meals', '', '50% 45%', F),
        ('west/t-20', 'A schoolboy holds his bowl by the pot', 'g-tall', '50% 30%', F),
        ('west/simitei-14', 'Children wait to be served', 'g-wide', '25% 50%', F),
        ('west/t-21', 'A pupil in a pink shirt in the meal queue', 'g-tall', '50% 40%', F),
        ('west/simitei-12', 'Pupils with bowls along a veranda', 'g-tall', '50% 40%', F),
        ('west/t-3', 'A community member at a meeting', 'g-tall', '50% 30%', C),
        ('west/t-23', 'The meal queue along the school building', 'g-wide', '30% 50%', F),
        ('west/simitei-15', 'Cooks and pupils at the serving pot', '', '30% 40%', C),
        ('west/t-8', 'A pupil rests with her bowl on the grass', 'g-wide', '50% 45%', F),
        ('west/t-25', 'Children hold out their bowls', 'g-wide', '50% 40%', F),
        ('west/t-19', 'Pupils with brightly coloured bowls', '', '50% 40%', F),
    ]
    return gallery_page('gallery-westpokot.html', 'gallery-westpokot', 'West Pokot Gallery | School Feeding Photographs',
                        'Photographs of school feeding, community training and meal service from Lishe Kwa Mtoto in West Pokot County, Kenya.',
                        'West Pokot County', 'Scenes from school feeding, community meetings and field work across West Pokot County, 2024 to 2025.',
                        [('west/simitei-1', 'Children eating along a school wall', '30% 50%'), ('west/t-7', 'A smiling schoolgirl', '50% 30%'), ('west/simitei-2', 'Pupils with bowls on a bench', '50% 40%'), ('west/t-20', 'A schoolboy with his bowl', '50% 30%'), ('west/simitei-5', 'Colourful bowls', '50% 40%')],
                        items, ('gallery-transnzoia.html', 'Trans Nzoia gallery'),
                        filters=[('all', 'All'), ('feeding', 'School feeding'), ('community', 'Community and training')])
