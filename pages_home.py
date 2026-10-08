from build_lib import *


def build_home():
    body = f'''
<!-- HERO -->
<section class="hero on-dark" data-hero aria-labelledby="hero-title">
  <div class="hero__media">
    <picture class="hero__poster">
      <source media="(max-width: 700px)" srcset="media/hero-mobile-poster.webp" type="image/webp">
      <source srcset="media/hero-desktop-poster.webp" type="image/webp">
      <img src="media/hero-desktop-poster.jpg" alt="Children at a partner school wave to the camera" width="1600" height="642" fetchpriority="high" decoding="async">
    </picture>
    <video class="hero__video" autoplay muted loop playsinline preload="auto" disablepictureinpicture aria-hidden="true" tabindex="-1"></video>
  </div>
  <div class="hero__content">
    <div class="container container--wide">
      <div class="hero__text">
        <span class="eyebrow">A Ray of Hope Kenya Initiative</span>
        <h1 class="h-hero" id="hero-title">Nourishing Children.<br>Building Futures.</h1>
        <p class="hero__sub">Every child deserves the opportunity to learn, grow and thrive.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="donate.html">Support Lishe</a>
          <a class="btn btn--secondary btn--light" href="programs.html">Our Work</a>
        </div>
      </div>
    </div>
  </div>
  <button class="hero__pause" type="button" aria-label="Pause background video"><i class="fa-solid fa-pause" aria-hidden="true"></i><span>Pause video</span></button>
</section>

<!-- IMPACT STATEMENT + NUMBERS -->
<section class="section" aria-labelledby="impact-h">
  <div class="container">
    <div class="statement">
      <div class="reveal">
        <span class="eyebrow">Why school meals</span>
        <h2 id="impact-h">Good nutrition changes what a child can do.</h2>
      </div>
      <div class="prose reveal" style="--d:.1s">
        <p class="lead">When children arrive at school hungry, they cannot concentrate, retain information or thrive. Lishe Kwa Mtoto, founded in 2024 under the Ray of Hope Foundation Kenya, addresses the link between hunger and educational outcomes.</p>
        <p>We deliver daily nutritious meals to vulnerable children in Trans Nzoia, West Pokot and other parts of Kenya's Arid and Semi-Arid Lands, tackling hunger, supporting attendance and giving every child a stronger foundation for learning.</p>
        <p><a class="link-arrow" href="about.html">Read our story <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a></p>
      </div>
    </div>
    <div class="stats" role="list">
      <div class="stat reveal" role="listitem"><span class="stat__num" data-count="11400" data-suffix="+">11,400+</span><span class="stat__label">Learners reached</span></div>
      <div class="stat reveal" role="listitem" style="--d:.08s"><span class="stat__num" data-count="30" data-suffix="+">30+</span><span class="stat__label">Schools supported</span></div>
      <div class="stat reveal" role="listitem" style="--d:.16s"><span class="stat__num" data-count="94" data-suffix="%">94%</span><span class="stat__label">Attendance at Cherang'any Primary, up from 61% (head teacher's report)</span></div>
      <div class="stat reveal" role="listitem" style="--d:.24s"><span class="stat__num">KES 150</span><span class="stat__label">Feeds one child for a full week</span></div>
    </div>
  </div>
</section>

<!-- WHAT WE DO -->
<section class="section section--white" aria-labelledby="what-h">
  <div class="container">
    <div class="split split--wide-text">
      <div class="reveal" style="max-width:440px">
        {media('west/t-7', 'A smiling schoolgirl holds a bowl of porridge outdoors', ar='4/5', pos='50% 30%', sizes='(min-width:900px) 36vw, 100vw')}
      </div>
      <div class="reveal" style="--d:.1s">
        <span class="eyebrow">What we do</span>
        <h2 id="what-h" style="margin-bottom:24px">A warm meal, before the first lesson.</h2>
        <div class="prose">
          <p class="lead">Community cooks at partner schools prepare hot porridge each morning, so children receive a filling meal before 8:30 AM.</p>
          <p>For many learners it is the most nutritious food of their day. We buy ingredients from local farmers, employ community cooks and work alongside teachers, parents and county leaders in some of Kenya's most food-insecure regions.</p>
        </div>
        <div class="btn-row" style="margin-top:32px">
          <a class="btn btn--secondary" href="school-feeding.html">How school feeding works</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FEATURED: THE LISHE MIX -->
<section class="feature on-dark" aria-labelledby="mix-h">
  <div class="feature__media">{img('tn/liavo2', 'A community cook serves porridge from a large pot to children in school uniform', sizes='(min-width:900px) 58vw, 100vw', pos='50% 45%')}</div>
  <div class="feature__body">
    <span class="eyebrow">The Lishe Mix</span>
    <h2 id="mix-h">Nutrition built from local grain.</h2>
    <p>Our locally formulated porridge flour combines maize, millet, cassava, sorghum and soybeans, designed for maximum nutrition at minimal cost. Every ingredient is grown in Kenya.</p>
    <div class="mix-big"><strong>90 kg</strong><span>one bag feeds about 300 children</span></div>
    <div class="chips on-dark-chips"><span>Maize</span><span>Millet</span><span>Sorghum</span><span>Cassava</span><span>Soybeans</span></div>
    <div class="btn-row"><a class="btn btn--primary" href="school-feeding.html">See the full programme</a></div>
  </div>
</section>

<!-- EDITORIAL PHOTOGRAPH -->
<section class="band on-dark" aria-label="Photograph and quotation">
  {img('tn/cherubai3', 'A crowd of schoolchildren raise their hands and smile', sizes='100vw', pos='50% 38%', cls='band__img')}
  <div class="band__content"><div class="container container--wide">
    <blockquote>"When children are fed, they can focus. When they focus, they can learn. When they learn, they can lead."</blockquote>
    <p class="caption">Learners at a partner school, Trans Nzoia County</p>
  </div></div>
</section>

<!-- HOW IT WORKS -->
<section class="section" aria-labelledby="how-h">
  <div class="container">
    <div class="split split--wide-text split--top">
      <div class="sticky-col reveal">
        <span class="eyebrow">How it works</span>
        <h2 id="how-h">From donation to plate.</h2>
        <p class="lead" style="margin-top:20px">Every shilling you give is transformed into a nutritious meal for a child who needs it most.</p>
        <div class="btn-row" style="margin-top:28px"><a class="btn btn--primary" href="donate.html">Start giving</a></div>
      </div>
      <ol class="steps">
        <li class="step reveal"><div><h3>You donate</h3><p>Your contribution is received securely by M-Pesa, card or bank transfer and tracked transparently.</p></div></li>
        <li class="step reveal"><div><h3>We source locally</h3><p>We purchase ingredients from local farmers, supporting community livelihoods while keeping meals fresh and nutritious.</p></div></li>
        <li class="step reveal"><div><h3>Children are fed</h3><p>Hot meals are prepared and served each day at partner schools, supporting concentration and attendance.</p></div></li>
      </ol>
    </div>
  </div>
</section>

<!-- PROGRAMS -->
<section class="section section--sand" aria-labelledby="prog-h">
  <div class="container">
    <div class="head">
      <div><span class="eyebrow">Programs</span><h2 id="prog-h">A complete approach to child nutrition.</h2></div>
      <a class="link-arrow" href="programs.html">All programs <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
    </div>
    <div class="prog">
      <article class="prog__item prog__item--lead reveal">
        {media('west/t-20', 'A schoolboy smiles while holding a bowl of porridge beside a cooking pot', ar='4/5', pos='50% 30%', extra='media--zoom', sizes='(min-width:900px) 50vw, 100vw')}
        <h3>School Feeding</h3>
        <p>Daily hot meals for vulnerable school children across Kenya's Arid and Semi-Arid Lands, prepared by community cooks.</p>
        <a class="link-arrow" href="school-feeding.html">Explore school feeding <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </article>
      <article class="prog__item reveal" style="--d:.1s">
        {media('em/women-4', 'A woman in traditional beaded jewellery holds a packet of food in front of a Ray of Hope banner', ar='3/2', pos='50% 22%', extra='media--zoom', sizes='(min-width:900px) 50vw, 100vw')}
        <h3>Emergency Response</h3>
        <p>Rapid food distribution to communities affected by floods, drought and displacement.</p>
        <a class="link-arrow" href="emergency.html">See how we respond <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </article>
      <article class="prog__item reveal" style="--d:.2s">
        {media('west/simitei-7', 'Adults seated in a classroom during a community meeting', ar='3/2', pos='50% 50%', extra='media--zoom', sizes='(min-width:900px) 50vw, 100vw')}
        <h3>Nutrition Education</h3>
        <p>Training teachers, parents and community health workers in child nutrition best practice.</p>
        <a class="link-arrow" href="programs.html#nutrition">Learn more <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </article>
    </div>
  </div>
</section>

<!-- WHERE WE WORK -->
<section class="section" aria-labelledby="where-h">
  <div class="container">
    <div class="head">
      <div><span class="eyebrow">Where we work</span><h2 id="where-h">Rooted in the communities we serve.</h2></div>
      <p class="lead" style="max-width:30em">Our team is based in Kitale, Trans Nzoia County, and works across Kenya's ASAL regions. See the work in photographs.</p>
    </div>
    <div class="places">
      <a class="place reveal" href="gallery-transnzoia.html">
        {img('tn/liavo3', 'Children queue to be served a meal outside a school in Trans Nzoia County', sizes='(min-width:720px) 50vw, 100vw', pos='50% 50%')}
        <div class="place__body"><h3>Trans Nzoia County</h3><span>View gallery <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></span></div>
      </a>
      <a class="place reveal" href="gallery-westpokot.html" style="--d:.1s">
        {img('west/simitei-14', 'A community cook serves porridge to children in West Pokot County', sizes='(min-width:720px) 50vw, 100vw', pos='30% 50%')}
        <div class="place__body"><h3>West Pokot County</h3><span>View gallery <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></span></div>
      </a>
    </div>
  </div>
</section>

<!-- STORY -->
<section class="section section--white" aria-labelledby="story-h">
  <div class="container">
    <div class="story">
      <div class="reveal">
        {media('tn/cherubai2', 'Schoolchildren in colourful clothes raise their hands and smile', ar='4/5', pos='45% 40%', sizes='(min-width:900px) 40vw, 100vw')}
        <p class="caption" style="margin-top:10px">Learners at a partner school, Trans Nzoia County.</p>
      </div>
      <div class="reveal" style="--d:.1s">
        <span class="eyebrow" id="story-h">Featured story</span>
        <blockquote class="pullquote">"I used to faint in class. Now I'm top of my school."</blockquote>
        <div class="prose" style="margin-top:28px">
          <p>Faith Chebet, nine, attends Cherang'any Primary School in Trans Nzoia County. Six months after meals began at her school, her attendance was perfect and she had moved from the bottom of her class to the top five.</p>
          <p class="attrib"><strong>Grace Wanjiru</strong>, Faith's mother: "A meal changed everything."</p>
        </div>
        <div class="btn-row" style="margin-top:28px"><a class="link-arrow" href="stories.html">Read more stories <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a></div>
      </div>
    </div>
  </div>
</section>

<!-- DONATION IMPACT -->
<section class="section" aria-labelledby="give-h">
  <div class="container">
    <div class="split split--top">
      <div class="reveal">
        <span class="eyebrow">Your donation becomes a meal</span>
        <h2 id="give-h">See what your gift does.</h2>
        <p class="lead" style="margin-top:20px">Choose an amount that suits you. Every contribution goes toward daily school meals for children who need them.</p>
        <div class="btn-row" style="margin-top:32px">
          <a class="btn btn--primary" href="donate.html">Donate now</a>
          <a class="btn btn--secondary" href="donate.html#other">Other ways to give</a>
        </div>
      </div>
      <div class="reveal" style="--d:.1s">
        <div class="tiers">
          <div class="tier"><span class="tier__amt">KES 150</span><span class="tier__what">feeds one child for a week</span></div>
          <div class="tier"><span class="tier__amt">KES 600</span><span class="tier__what">feeds one child for a month</span></div>
          <div class="tier"><span class="tier__amt">KES 1,800</span><span class="tier__what">feeds one child for a full term</span></div>
        </div>
        <p class="caption" style="margin-top:18px">Giving from outside Kenya? You can donate in USD, EUR, GBP and many other currencies.</p>
      </div>
    </div>
  </div>
</section>

<!-- LATEST NEWS -->
<section class="section section--sand" aria-labelledby="news-h">
  <div class="container">
    <div class="head">
      <div><span class="eyebrow">Newsroom</span><h2 id="news-h">Latest from the field.</h2></div>
      <a class="link-arrow" href="blog.html">All news <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
    </div>
    <div id="latestNews" aria-live="polite">
      <div class="empty-note"><p>Loading the latest updates&hellip;</p></div>
    </div>
  </div>
</section>

<!-- FINAL CTA -->
{cta('west/simitei-2', 'One meal. One child. One changed life.', 'KES 150 feeds one child for a full week. Your donation today becomes a child\'s chance tomorrow.',
     '<a class="btn btn--primary" href="donate.html">Donate KES 150</a><a class="btn btn--secondary btn--light" href="volunteer.html">Volunteer with us</a>', pos='50% 35%')}

'''
    scripts = '''<script src="firebase-init.js" defer></script>
<script>
document.addEventListener('DOMContentLoaded', function () {
  var F = window.LisheFirebase; if (!F) return;
  var GOAL = 500000;
  function fmtDate(ts) { return ts && ts.toDate ? ts.toDate().toLocaleDateString('en-KE', { day: 'numeric', month: 'long', year: 'numeric' }) : ''; }

  // Latest published posts
  F.whenNear(document.getElementById('latestNews'), function () {
    var box = document.getElementById('latestNews');
    function empty(msg) { box.innerHTML = '<div class="empty-note"><p>' + msg + '</p><p style="margin-top:14px"><a class="link-arrow" href="stories.html">Read our stories <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a></p></div>'; }
    F.db().then(function (db) {
      return db.collection('blogPosts').where('status', '==', 'published').orderBy('publishedAt', 'desc').limit(3).get();
    }).then(function (snap) {
      var posts = snap.docs.map(function (d) { var o = d.data(); o.id = d.id; return o; });
      if (!posts.length) { empty('New updates will be published here soon.'); return; }
      var e = F.esc, fb = 'img/west/t-8-800.webp';
      function meta(p) { return '<div class="post__meta"><span class="post__cat">' + e(p.categoryLabel || 'News') + '</span><span class="meta">' + e(fmtDate(p.publishedAt)) + '</span></div>'; }
      var lead = posts[0];
      var html = '<div class="news news--featured"><article class="post post--lead"><div class="media" style="--ar:16/10"><img src="' + e(lead.imageUrl || fb) + '" alt="" loading="lazy"></div>' + meta(lead) +
        '<h3><a href="blog.html?post=' + e(lead.id) + '">' + e(lead.title || 'Untitled') + '</a></h3><p>' + e(lead.excerpt || '') + '</p></article><div class="post-stack">';
      posts.slice(1).forEach(function (p) {
        html += '<article class="post post--row"><div class="media"><img src="' + e(p.imageUrl || fb) + '" alt="" loading="lazy"></div><div>' + meta(p) +
          '<h3 style="font-size:1.05rem"><a href="blog.html?post=' + e(p.id) + '">' + e(p.title || 'Untitled') + '</a></h3></div></article>';
      });
      box.innerHTML = html + '</div></div>';
    }).catch(function (err) { console.error('News:', err.message); empty('Updates are unavailable right now. Please check back soon.'); });
  });
});
</script>'''
    return page('index.html', 'home',
                'Lishe Kwa Mtoto | School Meals for Children in Kenya',
                'Lishe Kwa Mtoto delivers daily nutritious school meals, emergency food response and nutrition education to vulnerable children in Kenya. Support a child today.',
                body, scripts=scripts, with_schema=True,
                preload='<link rel="preload" as="image" href="media/hero-desktop-poster.webp" type="image/webp" media="(min-width: 701px)" fetchpriority="high">\n<link rel="preload" as="image" href="media/hero-mobile-poster.webp" type="image/webp" media="(max-width: 700px)" fetchpriority="high">\n')
