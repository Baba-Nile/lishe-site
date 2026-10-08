from build_lib import *

ARROW = '<i class="fa-solid fa-arrow-right" aria-hidden="true"></i>'


def build_about():
    mix_rows = [('Maize', '45 kg', 50), ('Millet', '13.5 kg', 15), ('Cassava', '9 kg', 10), ('Sorghum', '13.5 kg', 15), ('Soybeans', '9 kg', 10)]
    bars = ''.join(f'<div class="mix-bar"><span>{n}</span><span class="mix-bar__track"><span class="mix-bar__fill" style="--w:{w}%"></span></span><span class="mix-bar__val">{kg}</span></div>' for n, kg, w in mix_rows)
    sdgs = [
        ('2', 'Zero Hunger', 'Primary goal: nutritious daily school meals.'),
        ('3', 'Good Health and Well-being', 'Healthy growth, immunity and development.'),
        ('4', 'Quality Education', 'Better learning through consistent attendance.'),
        ('1', 'No Poverty', 'Easing the financial burden on vulnerable families.'),
        ('10', 'Reduced Inequalities', 'Equal opportunity for marginalised children.'),
        ('17', 'Partnerships for the Goals', 'Collaboration across all sectors of society.'),
    ]
    sdg_html = ''.join(f'<li><span class="sdg__no">{n}</span><div><strong>{t}</strong><span class="sdg__txt">{d}</span></div></li>' for n, t, d in sdgs)
    body = f'''
{split_hero('west/t-23', 'Schoolchildren queue along a school building holding bowls for their meal', 'About us', 'No child should learn on an empty stomach.',
            'Founded in 2024, Lishe Kwa Mtoto is a movement advancing Zero Hunger, Quality Education and Good Health for Kenya\'s children.', pos='25% 50%')}

{subnav([('story','Our story'),('approach','Approach'),('nutrition','Nutrition'),('impact','Impact'),('vision','Vision'),('team','Leadership'),('partners','Partners')])}

<section class="section" id="story" aria-labelledby="story-h">
  <div class="container">
    <div class="split split--wide-media split--top">
      <div class="prose reveal">
        <span class="eyebrow">Our story</span>
        <h2 id="story-h" style="margin-bottom:28px">Born from a simple belief.</h2>
        <p class="dropcap-lead">LisheKwaMtoto was born in 2024 from a simple yet powerful belief: no child should have to learn on an empty stomach.</p>
        <p>What began as a single outreach activity to provide meals for children in underserved communities quickly revealed a much deeper challenge. During that first initiative, volunteers met countless children who arrived at school without having eaten breakfast, while many others relied on their school meal as the only nutritious food they would receive all day. Hunger was silently robbing them of their ability to concentrate, participate in class and fully realise their potential.</p>
        <p>This experience became a defining moment. Rather than treating hunger as a temporary problem, LisheKwaMtoto committed itself to becoming part of the long-term solution. With the support of dedicated partners, generous donors, local leaders, schools and community volunteers, the initiative evolved into a structured school feeding programme focused on reaching children in Kenya's Arid and Semi-Arid Lands (ASALs), where food insecurity continues to affect thousands of families.</p>
      </div>
      <div class="reveal" style="--d:.1s">
        {media('tn/20250708-125015', 'Pupils in school uniform stand beside a Lishe Kwa Mtoto banner at a Trans Nzoia school', ar='4/5', pos='50% 35%', sizes='(min-width:900px) 40vw, 100vw')}
      </div>
    </div>
  </div>
</section>

<section class="band on-dark" aria-label="Photograph">
  {img('west/simitei-5', 'Schoolchildren sit and stand holding colourful bowls of porridge', sizes='100vw', pos='50% 40%', cls='band__img')}
  <div class="band__content"><div class="container container--wide">
    <blockquote>"Today, LisheKwaMtoto is more than a feeding programme. It is a movement."</blockquote>
    <p class="caption">West Pokot County</p>
  </div></div>
</section>

<section class="section" id="approach" aria-labelledby="approach-h">
  <div class="container">
    <div class="split split--wide-text split--top">
      <div class="sticky-col reveal">
        <span class="eyebrow">Our approach</span>
        <h2 id="approach-h">Meals that serve the global goals.</h2>
        <p class="lead" style="margin-top:20px">The initiative advances the United Nations Sustainable Development Goals, in particular SDG 2: Zero Hunger, SDG 3: Good Health and Well-being and SDG 4: Quality Education.</p>
        <p style="margin-top:16px;max-width:46ch">Every meal served represents an investment in a healthier, more educated and more equitable future.</p>
      </div>
      <ul class="sdg reveal" style="--d:.1s">{sdg_html}</ul>
    </div>
  </div>
</section>

<section class="section section--sand" id="nutrition" aria-labelledby="mix-h">
  <div class="container">
    <div class="head">
      <div><span class="eyebrow">Our nutrition model</span><h2 id="mix-h">The Lishe Mix.</h2></div>
      <p class="lead">A nutrient-rich porridge flour developed from locally sourced ingredients, designed for maximum nutrition at minimal cost.</p>
    </div>
    <div class="mix">
      <div class="reveal">
        <div class="mix-big mix-big--dark"><strong>90 kg</strong><span>One bag of the Lishe Mix feeds about 300 children one complete breakfast.</span></div>
        <div class="chips" style="margin-top:28px"><span>Maize</span><span>Millet</span><span>Sorghum</span><span>Cassava</span><span>Soybeans</span></div>
        <p style="margin-top:24px"><a class="link-arrow" href="school-feeding.html#meal">See the full composition <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a></p>
      </div>
      <div class="reveal" style="--d:.1s">
        <h3 style="margin-bottom:16px">What each ingredient provides</h3>
        <ul class="nutri">
          <li><strong>Energy</strong><span>Maize and cassava carbohydrates</span></li>
          <li><strong>Protein</strong><span>Soybeans and sorghum</span></li>
          <li><strong>Fibre</strong><span>Millet whole grain</span></li>
          <li><strong>Immunity</strong><span>Vitamins and minerals</span></li>
        </ul>
        <h3 style="margin:36px 0 12px">What it delivers for children</h3>
        <ul class="checks checks--dark">
          <li><i class="fa-solid fa-check" aria-hidden="true"></i>Increased attendance</li>
          <li><i class="fa-solid fa-check" aria-hidden="true"></i>Improved academic performance</li>
          <li><i class="fa-solid fa-check" aria-hidden="true"></i>Better child health</li>
          <li><i class="fa-solid fa-check" aria-hidden="true"></i>Reduced hunger-related dropout</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" id="impact" aria-labelledby="impact-h">
  <div class="container">
    <div class="split split--wide-text split--top">
      <div class="reveal">
        {media('west/simitei-6', 'A schoolboy holds a bowl of porridge while other children wait behind him', ar='4/5', pos='50% 28%', sizes='(min-width:900px) 36vw, 100vw')}
      </div>
      <div class="reveal" style="--d:.1s">
        <span class="eyebrow">Our impact</span>
        <h2 id="impact-h" style="margin-bottom:24px">When children are fed, they can lead.</h2>
        <div class="prose">
          <p class="lead">Since its inception, LisheKwaMtoto has reached more than 30 schools and positively impacted over 11,400 learners across Kenya.</p>
          <p>Teachers consistently report improved concentration, greater classroom participation and increased enthusiasm for learning. Schools have experienced reduced absenteeism and improved retention, while parents speak of healthier, happier children who return home with renewed confidence and hope.</p>
          <p>These outcomes demonstrate that proper nutrition is not only a health intervention but also a catalyst for educational success and community development.</p>
        </div>
        <div class="stats" style="grid-template-columns:repeat(2,minmax(0,1fr));margin-top:40px">
          <div class="stat"><span class="stat__num">33%</span><span class="stat__label">Rise in attendance</span></div>
          <div class="stat"><span class="stat__num">68%</span><span class="stat__label">Fall in dropout rate</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--green on-dark" id="vision" aria-labelledby="vision-h">
  <div class="container">
    <div class="split split--top">
      <div class="reveal">
        <span class="eyebrow">Our vision</span>
        <h2 id="vision-h">A future without child hunger.</h2>
        <figure style="margin-top:36px;padding-left:24px;border-left:4px solid var(--mango)">
          <blockquote style="font-size:1.35rem;font-weight:700;line-height:1.3;color:#fff">"Leadership is the willingness to serve."</blockquote>
          <figcaption class="caption" style="color:rgba(255,255,255,.8)">Jayson Mburu Mudenyo, Founder</figcaption>
        </figure>
      </div>
      <div class="prose reveal" style="--d:.1s">
        <p class="lead" style="color:#fff">We envision a future where no child is forced to choose between hunger and education.</p>
        <p style="color:rgba(255,255,255,.88)">Every child deserves the opportunity to learn in a safe, healthy environment where nutritious meals support academic achievement, personal development and lifelong success.</p>
        <p style="color:rgba(255,255,255,.88)">Realising this vision requires collaboration across every sector of society. Governments, businesses, development partners, schools, community organisations and compassionate individuals all have a role to play. Through strategic partnerships, financial support, food donations, volunteerism and advocacy, we can reach more schools and ensure that every child has the nourishment they need to succeed.</p>
        <div class="btn-row" style="margin-top:32px">
          <a class="btn btn--primary" href="donate.html">Support our mission</a>
          <a class="btn btn--secondary btn--light" href="volunteer.html">Volunteer</a>
          <a class="btn btn--secondary btn--light" href="contact.html">Partner with us</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="team" aria-labelledby="team-h">
  <div class="container">
    <div class="head"><div><span class="eyebrow">Leadership</span><h2 id="team-h">The people behind the programme.</h2></div></div>
    <ul class="ration">
      <li><strong>Jayson Mburu Mudenyo</strong><span>Founder and Executive Director</span></li>
      <li><strong>Mary Chebet</strong><span>Head of Programs</span></li>
      <li><strong>Dr. Naomi Wambua</strong><span>Nutrition and Health Advisor</span></li>
    </ul>
  </div>
</section>

{partners_block()}
'''
    return page('about.html', 'about', 'About Lishe Kwa Mtoto | Our Story, Approach and Impact',
                'Learn how Lishe Kwa Mtoto grew from a single outreach in 2024 into a school feeding movement for children in Kenya, built on the Lishe Mix and the Sustainable Development Goals.', body)


def build_programs():
    def kpis(items):
        return '<div class="kpis">' + ''.join(f'<div class="kpi"><strong>{n}</strong><span>{l}</span></div>' for n, l in items) + '</div>'
    def tags(items):
        return '<div class="tags">' + ''.join(f'<span>{t}</span>' for t in items) + '</div>'
    body = f'''
{page_hero('west/simitei-1', 'A long line of schoolchildren seated along a wall, eating from colourful bowls', 'Programs', 'Our programs.',
           'A community-rooted approach to ending child hunger and improving educational outcomes across Kenya.', pos='50% 40%')}

{subnav([('school-feeding', 'School Feeding'), ('emergency', 'Emergency Response'), ('nutrition', 'Nutrition Education')])}

<section class="feature feature--tall on-dark" id="school-feeding" aria-labelledby="sf-h">
  <div class="feature__media">{img('west/t-22', 'A schoolgirl in a pink shirt holds a bowl in a line of children', sizes='(min-width:900px) 58vw, 100vw', pos='50% 38%')}</div>
  <div class="feature__body">
    <span class="eyebrow">01 &middot; Core program</span>
    <h2 id="sf-h">School Feeding</h2>
    <p class="lead">Our flagship program delivers daily nutritious meals to vulnerable school children across Kenya's Arid and Semi-Arid Lands.</p>
    <p style="margin-top:16px">Since 2024 we have served over 11,400 learners across 30+ partner schools. At its heart is the Lishe Mix, a locally formulated porridge flour made from maize, millet, cassava, sorghum and soybeans. Every meal is prepared fresh by community cooks, creating local employment while ensuring quality.</p>
    {kpis([('11,400+', 'Learners reached'), ('30+', 'Partner schools'), ('94%', 'Attendance at Cherang\'any Primary')])}
    {tags(['SDG 2 Zero Hunger', 'SDG 3 Good Health', 'SDG 4 Quality Education'])}
    <div class="btn-row"><a class="btn btn--primary" href="school-feeding.html">Full details</a><a class="btn btn--secondary btn--light" href="donate.html">Support this program</a></div>
  </div>
</section>

<div class="container">
  <article class="prog-row" id="emergency" aria-labelledby="em-h">
    <div class="prog-row__media reveal">{media('em/women-1', 'A woman in traditional beaded jewellery holds a packet of food in front of a Ray of Hope banner', ar='4/5', pos='50% 25%', extra='media--zoom', sizes='(min-width:900px) 42vw, 100vw')}</div>
    <div class="reveal" style="--d:.1s">
      <span class="prog-row__no" aria-hidden="true">02</span>
      <span class="eyebrow">Rapid response</span>
      <h2 id="em-h">Emergency Food Response</h2>
      <p class="lead">When floods, drought or conflict displace families, we activate our Emergency Response Protocol and mobilise food distribution within 48 hours of a crisis alert.</p>
      <p style="margin-top:16px;max-width:60ch">We partner with county governments, the Kenya Red Cross and WFP Kenya to reach communities that cannot wait. Emergency ration packs of maize flour, legumes, cooking oil and salt are designed to sustain a family of five for 14 days. In 2024 we responded to three emergency events in Turkana, Baringo and West Pokot counties.</p>
      {kpis([('3', 'Emergencies responded to'), ('2,800', 'Families reached'), ('48 hrs', 'Average response time')])}
      {tags(['SDG 1 No Poverty', 'SDG 2 Zero Hunger', 'SDG 10 Reduced Inequalities'])}
      <div class="btn-row"><a class="btn btn--primary" href="emergency.html">Full details</a><a class="btn btn--secondary" href="donate.html">Emergency fund</a></div>
    </div>
  </article>

  <article class="prog-row prog-row--reverse" id="nutrition" aria-labelledby="ne-h" style="border-bottom:0">
    <div class="prog-row__media reveal">{media('west/simitei-8', 'Community members gathered in a hall for a workshop', ar='4/5', pos='50% 50%', extra='media--zoom', sizes='(min-width:900px) 42vw, 100vw')}</div>
    <div class="reveal" style="--d:.1s">
      <span class="prog-row__no" aria-hidden="true">03</span>
      <span class="eyebrow">Capacity building</span>
      <h2 id="ne-h">Nutrition Education</h2>
      <p class="lead">Sustainable change requires knowledge. We train teachers, school cooks, community health volunteers and parents on the fundamentals of child nutrition.</p>
      <p style="margin-top:16px;max-width:60ch">That means what to feed, when, and how to prepare affordable, balanced meals using local ingredients. We run quarterly workshops in each partner county, distribute illustrated nutrition guides in Swahili and local languages, and maintain a network of trained Community Nutrition Champions who carry the message to the last mile.</p>
      {kpis([('340+', 'Teachers trained'), ('60', 'Nutrition Champions'), ('12', 'Workshops per year')])}
      {tags(['SDG 3 Good Health', 'SDG 4 Quality Education', 'SDG 17 Partnerships'])}
      <div class="btn-row"><a class="btn btn--primary" href="donate.html">Support this program</a></div>
    </div>
  </article>
</div>

{cta_bar('Every program needs your support.', 'Choose a program to support, or give to our general fund and we will direct your donation where it is needed most.',
     '<a class="btn btn--primary" href="donate.html">Donate</a><a class="btn btn--secondary btn--light" href="volunteer.html">Volunteer</a>')}
'''
    return page('programs.html', 'programs', 'Programs | School Feeding, Emergency Response and Nutrition Education',
                'Explore Lishe Kwa Mtoto programs: daily school feeding with the Lishe Mix, 48-hour emergency food response, and nutrition education for teachers, cooks and parents in Kenya.', body)


def build_school():
    tl = [
        ('Local procurement', 'We partner with farmers\' cooperatives in each county to source maize, millet, cassava, sorghum and soybeans, ensuring freshness and boosting local agricultural incomes.'),
        ('Lishe Mix preparation', 'Ingredients are milled and blended into the Lishe Mix formula: a 90 kg bag that feeds approximately 300 children per serving.'),
        ('School delivery', 'Bags are delivered weekly to each partner school and stored in dedicated food stores managed by school feeding committees.'),
        ('Daily meal service', 'Community cooks prepare hot porridge each morning before the first lesson. Children receive a warm, filling meal before 8:30 AM.'),
        ('Monitoring and reporting', 'Our field officers conduct monthly visits, track attendance data, and report impact to donors and county governments.'),
    ]
    tl_html = ''.join(f'<li class="reveal"><div><h3>{t}</h3><p>{d}</p></div></li>' for t, d in tl)
    meal = [
        ('45', 'kg', 'Maize', 'Energy-rich carbohydrates for sustained concentration through the school day.'),
        ('13.5', 'kg', 'Millet', 'Dietary fibre supporting digestion and steady energy release.'),
        ('13.5', 'kg', 'Sorghum', 'Protein and B-vitamins supporting brain development.'),
        ('9', 'kg', 'Cassava', 'Additional energy and vitamin C to support immunity and growth.'),
        ('9', 'kg', 'Soybeans', 'Complete plant protein for muscle development and growth.'),
    ]
    meal_html = ''.join(f'<div class="meal__item reveal" style="--d:{i*0.06}s"><span class="meal__kg">{a}<small>{u}</small></span><h3>{n}</h3><p>{d}</p></div>' for i, (a, u, n, d) in enumerate(meal))
    counties = ['Trans Nzoia', 'West Pokot', 'Turkana', 'Baringo', 'Elgeyo Marakwet', 'Samburu']
    body = f'''
{page_hero('tn/cherubai5', 'Smiling children in bright school clothes raise their hands in a school compound', 'Core program', 'School feeding.',
           'Daily nutritious meals for 11,400+ learners across 30+ schools in Kenya\'s most food-insecure regions.', pos='50% 38%', buttons='<a class="btn btn--primary" href="donate.html">Fund a bag of Lishe Mix</a>', tall=True)}

{subnav([('farm','Farm to classroom'),('meal','The meal'),('impact','Impact')])}

<section class="section" id="farm" aria-labelledby="farm-h">
  <div class="container">
    <div class="split split--wide-text split--top">
      <div class="sticky-col reveal">
        <span class="eyebrow">How it works</span>
        <h2 id="farm-h">From farm to classroom.</h2>
        <p class="lead" style="margin-top:20px">The programme rests on three pillars: local sourcing, community ownership and nutritional excellence. Each morning, trained cooks at partner schools prepare Lishe Mix porridge from ingredients bought from local smallholder farmers.</p>
        <div style="margin-top:32px" class="reveal">{media('tn/liavo1', 'A child receives a bowl of porridge from a large cooking pot', ar='1/1', pos='50% 45%', sizes='(min-width:900px) 40vw, 100vw')}</div>
      </div>
      <ol class="timeline">{tl_html}</ol>
    </div>
  </div>
</section>

<section class="section section--sand" id="meal" aria-labelledby="meal-h">
  <div class="container">
    <div class="head">
      <div><span class="eyebrow">The Lishe Mix</span><h2 id="meal-h">What is in the meal?</h2></div>
      <p class="lead">A complete nutritional profile from locally grown Kenyan ingredients. These five make up one 90 kg bag.</p>
    </div>
    <div class="meal">{meal_html}</div>
    <div class="meal-total">
      <p>One 90 kg bag feeds approximately 300 children one complete, balanced breakfast.</p>
      <a class="btn btn--primary" href="donate.html">Fund a bag of Lishe Mix</a>
    </div>
  </div>
</section>

<section class="section" id="impact" aria-labelledby="sfimpact-h">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Impact</span>
        <h2 id="sfimpact-h" style="margin-bottom:20px">A meal that keeps children in class.</h2>
        <p class="lead">Teachers report better concentration, stronger participation and fewer absences once the morning meal begins.</p>
        <div class="result"><span class="result__from">61%</span><i class="fa-solid fa-arrow-right-long" aria-hidden="true"></i><span class="result__to">94%</span><p>Daily attendance at Cherang'any Primary after the morning meal began, according to the head teacher.</p></div>
        <div style="margin-top:40px">
          <h3 class="eyebrow" style="margin-bottom:14px">Counties covered</h3>
          <div class="chips">{''.join(f'<span>{c}</span>' for c in counties)}</div>
        </div>
      </div>
      <div class="reveal" style="--d:.1s">{media('west/simitei-4', 'A community cook serves porridge to a pupil from a large pot', ar='4/5', pos='40% 40%', sizes='(min-width:900px) 44vw, 100vw')}</div>
    </div>
  </div>
</section>

{cta_bar('Fund the next bag of Lishe Mix.', 'A single 90 kg bag feeds about 300 children one complete breakfast.',
     '<a class="btn btn--primary" href="donate.html">Donate now</a><a class="btn btn--secondary btn--light" href="gallery-westpokot.html">See the galleries</a>')}
'''
    return page('school-feeding.html', 'school-feeding', 'School Feeding Program | From Farm to Classroom',
                'See how Lishe Kwa Mtoto sources local grain, prepares the Lishe Mix and serves hot porridge to learners at 30+ partner schools in Kenya before the first lesson.', body)


def build_emergency():
    phases = [('0-6h', 'Alert and activation', 'Crisis alert received. Emergency Response team activated. County liaisons contacted.'),
              ('6-24h', 'Assessment', 'Rapid needs assessment deployed to the affected area. Number of families and severity mapped.'),
              ('24-48h', 'Procurement', 'Emergency ration packs procured from the nearest depot. Logistics and volunteers mobilised.'),
              ('48h+', 'Distribution', 'Food distributed at registered distribution points. Beneficiary data recorded for reporting.')]
    ph = ''.join(f'<div class="phase reveal" style="--d:{i*0.08}s"><span class="phase__time">{t}</span><h3>{h}</h3><p>{d}</p></div>' for i, (t, h, d) in enumerate(phases))
    body = f'''
{split_hero('em/img-20251109-wa0082', 'A field worker in waterproof boots stands in floodwater among tall trees', 'Rapid response', 'Emergency food response.',
            'When disaster strikes, we mobilise within 48 hours to reach displaced families in Kenya\'s most vulnerable regions.', pos='50% 50%',
            buttons='<a class="btn btn--primary" href="donate.html">Donate to the emergency fund</a>', reverse=True, dark=True)}

<div class="em-strip on-dark"><div class="container">
  <p><i class="fa-solid fa-circle-exclamation" aria-hidden="true"></i>Emergency Fund active. Your gift can reach crisis-hit families within 48 hours of a disaster.</p>
  <a class="btn btn--primary btn--sm" href="donate.html">Give now</a>
</div></div>

{subnav([('protocol','Response protocol'),('distribution','What we distribute'),('responses','Field responses')])}

<section class="section" id="protocol" aria-labelledby="proto-h">
  <div class="container">
    <div class="head">
      <div><span class="eyebrow" style="color:var(--alert)">Response protocol</span><h2 id="proto-h">48-hour activation.</h2></div>
      <p class="lead">A structured, fast-moving response framework built on field experience.</p>
    </div>
    <div class="phases">{ph}</div>
  </div>
</section>

<section class="section section--sand" id="distribution" aria-labelledby="dist-h">
  <div class="container">
    <div class="split split--top">
      <div class="reveal">
        <span class="eyebrow" style="color:var(--alert)">Emergency ration pack</span>
        <h2 id="dist-h" style="margin-bottom:20px">What we distribute.</h2>
        <p class="lead">Each pack is designed to sustain a family of five for 14 days. Packs are assembled in advance and stored at regional depots for immediate deployment.</p>
        <ul class="ration" style="margin-top:32px">
          <li><strong>10 kg maize flour</strong><span>Staple energy source</span></li>
          <li><strong>5 kg legumes</strong><span>Protein and iron</span></li>
          <li><strong>2 L cooking oil</strong><span>Healthy fats and calories</span></li>
          <li><strong>Iodised salt</strong><span>Mineral supplementation</span></li>
        </ul>
        <p class="note-line">One pack costs approximately KES 2,500 and feeds a family of five for 14 days.</p>
      </div>
      <div class="reveal" style="--d:.1s">
        {media('em/img-20251108-wa0090', 'A woman carries a sack of food on her head beside a Lishe banner', ar='4/5', pos='50% 35%', sizes='(min-width:900px) 40vw, 100vw')}
      </div>
    </div>
  </div>
</section>

<section class="section" id="responses" aria-labelledby="where-h">
  <div class="container">
    <div class="split split--wide-text split--top">
      <div class="sticky-col reveal">
        <span class="eyebrow" style="color:var(--alert)">Where we have responded</span>
        <h2 id="where-h">Field responses.</h2>
        <p class="lead" style="margin-top:20px">No family should face disaster alone.</p>
      </div>
      <div class="reveal" style="--d:.1s">
        <div class="incident"><span class="meta">November 2025<br>Trans Nzoia County</span><div><h3>Flood response</h3><p>Heavy rains displaced over 1,200 families along the river in the Sabwani and Namanjalala area.</p></div></div>
        <div class="incident"><span class="meta">October 2024<br>Trans Nzoia</span><div><h3>Flood response</h3><p>Supporting flood-affected families in Namanjalala.</p></div></div>
        <div class="incident"><span class="meta">July 2024<br>West Pokot County</span><div><h3>Drought relief</h3><p>A prolonged dry spell triggered food insecurity across the county. 800 families received emergency rations over a one-week distribution period.</p></div></div>
      </div>
    </div>
  </div>
</section>

<section class="section--sm" style="padding-top:0" aria-label="Field photographs">
  <div class="container">
    <div class="field-grid">
      <div class="reveal">{media('em/img-20251108-wa0089', 'A community leader speaks to a gathering beside bags of food', ar='4/5', pos='50% 30%', sizes='(min-width:900px) 50vw, 100vw')}</div>
      <div class="reveal" style="--d:.08s">{media('em/img-20251109-wa0083', 'A field worker wades through floodwater', ar='4/5', pos='50% 40%', sizes='(min-width:900px) 50vw, 100vw')}</div>
      <div class="reveal">{media('em/img-20251109-wa0071', 'River floodwater covering the land', ar='21/9', pos='50% 50%', sizes='100vw')}</div>
    </div>
  </div>
</section>

<section class="cta on-dark" style="background:#2a1209">
  <div class="container">
    <h2>Build our emergency reserve.</h2>
    <p>Funds held in the Emergency Reserve are deployed within hours of a crisis alert.</p>
    <div class="btn-row"><a class="btn btn--primary" href="donate.html">Donate to the emergency fund</a><a class="btn btn--secondary btn--light" href="volunteer.html">Volunteer for response</a></div>
  </div>
</section>
'''
    return page('emergency.html', 'emergency', 'Emergency Food Response | 48-Hour Activation in Kenya',
                'Lishe Kwa Mtoto mobilises emergency food packs within 48 hours of floods, drought or displacement in Kenya. See the response timeline, ration packs and how to give.', body)
