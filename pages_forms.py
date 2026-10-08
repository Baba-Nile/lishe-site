from build_lib import *

ARROW = '<i class="fa-solid fa-arrow-right" aria-hidden="true"></i>'
PAYNECTA = 'https://paynecta.co.ke/pay/Lishe%20Kwa%20Mtoto'


def build_donate():
    cur_opts = ''.join(f'<option value="{c}">{c} - {n}</option>' for c, n in [
        ('KES', 'Kenyan shilling'), ('USD', 'US dollar'), ('EUR', 'Euro'), ('GBP', 'British pound'), ('CAD', 'Canadian dollar'),
        ('AUD', 'Australian dollar'), ('CHF', 'Swiss franc'), ('SEK', 'Swedish krona'), ('NOK', 'Norwegian krone'), ('DKK', 'Danish krone'),
        ('JPY', 'Japanese yen'), ('CNY', 'Chinese yuan'), ('INR', 'Indian rupee'), ('AED', 'UAE dirham'), ('ZAR', 'South African rand'),
        ('UGX', 'Ugandan shilling'), ('TZS', 'Tanzanian shilling')])
    intl_links = ''.join(f'<a class="btn btn--secondary btn--block" href="{u}" target="_blank" rel="noopener"><i class="fa-solid fa-globe" aria-hidden="true"></i> Give with {n}</a>' for n, u in INTL_PAY_LINKS.items())
    body = f"""
{split_hero('west/t-1', 'A smiling schoolboy holds a bowl of porridge beside a serving pot', 'Donate', 'Your donation becomes a meal.',
            'KES 150 feeds one child for a full week. Give from anywhere in the world, in your own currency.', pos='50% 28%',
            buttons='<a class="btn btn--primary" href="#give">Give now</a>')}

<section class="section" id="give" aria-labelledby="impact-h">
  <div class="container">
    <div class="donate">
      <div>
        <span class="eyebrow">Your impact</span>
        <h2 id="impact-h" style="margin-bottom:20px">See what your gift does before you give.</h2>
        <p class="lead">When you donate to Lishe Kwa Mtoto, your contribution goes directly to school feeding programmes. Children in our partner schools are fed on the days we serve.</p>
        <div class="ladder" style="margin-top:36px">
          <div class="ladder__row"><span class="ladder__amt"><small>KES</small>150<span class="ladder__eq" data-kes="150"></span></span><div><h3>One child fed for a full week</h3><p>A week of nutritious daily meals that fuel learning, growth and school attendance.</p></div></div>
          <div class="ladder__row"><span class="ladder__amt"><small>KES</small>600<span class="ladder__eq" data-kes="600"></span></span><div><h3>One month of meals</h3><p>Sustain a child's nutrition through an entire school month: four full weeks.</p></div></div>
          <div class="ladder__row"><span class="ladder__amt"><small>KES</small>1,800<span class="ladder__eq" data-kes="1800"></span></span><div><h3>A full school term</h3><p>Give one child a completely fed school term.</p></div></div>
          <div class="ladder__row"><span class="ladder__amt"><small>KES</small>500,000<span class="ladder__eq" data-kes="500000"></span></span><div><h3>Feed a whole school</h3><p>Fund our annual campaign goal and reach hundreds of children in one school.</p></div></div>
        </div>

        <ul class="trust" aria-label="Why donors trust us">
          <li><i class="fa-solid fa-shield-halved" aria-hidden="true"></i>Transparent: donations are recorded and shown live on this page</li>
          <li><i class="fa-solid fa-lock" aria-hidden="true"></i>Secure payments through PayNecta, M-Pesa or bank transfer</li>
          <li><i class="fa-solid fa-globe" aria-hidden="true"></i>International donors welcome, in many currencies</li>
          <li><i class="fa-solid fa-receipt" aria-hidden="true"></i>Donation receipts available on request</li>
        </ul>

        <div class="progress" aria-live="polite" id="campaign">
          <div class="progress__top"><span class="progress__raised" id="progRaised">KES 0</span><span class="caption">raised toward the campaign goal of KES 500,000</span></div>
          <div class="progress__bar" role="progressbar" aria-label="Campaign progress" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" id="progBar"><div class="progress__fill" id="progFill"></div></div>
          <div class="progress__meta"><span id="progPct">0% complete</span><span><span id="progDonors">0</span> donors so far</span></div>
        </div>

        <div class="feed">
          <h3><span class="live-dot" aria-hidden="true"></span> Recent donations</h3>
          <div id="liveFeedList"><div class="feed-item"><span class="caption">Loading recent donations&hellip;</span></div></div>
        </div>
      </div>

      <aside class="donate__panel" aria-labelledby="panel-h">
        <div class="donate__panel-head"><h2 id="panel-h">Make a donation</h2><p>Two steps. Any currency.</p></div>
        <div class="donate__panel-body">
          <div class="dstep"><b>1</b> Choose currency and amount</div>
          <div class="cur-row">
            <label class="sr-only" for="curSel">Currency</label>
            <select id="curSel" autocomplete="off">{cur_opts}</select>
          </div>
          <div class="amounts" id="amounts" role="group" aria-label="Donation amount">
            <button type="button" class="amount" data-amt="150">150</button>
            <button type="button" class="amount active" data-amt="300" aria-pressed="true">300</button>
            <button type="button" class="amount" data-amt="600">600</button>
            <button type="button" class="amount" data-amt="1500">1,500</button>
            <button type="button" class="amount" data-amt="3000">3,000</button>
            <button type="button" class="amount" data-amt="0" id="customChip">Other</button>
          </div>
          <div class="field" id="customField" hidden>
            <label for="customAmt">Enter amount</label>
            <div class="amt-input"><span class="cur-tag" id="curTag">KES</span><input type="number" id="customAmt" min="1" step="any" inputmode="decimal" placeholder="Amount"></div>
          </div>
          <p class="convert" id="convert" aria-live="polite"></p>
          <p class="outcome" id="outcome" aria-live="polite"><span>KES 300 feeds <strong>2</strong> children for a full week</span></p>

          <div class="dstep"><b>2</b> Choose how to pay</div>
          <div class="pay-tabs" role="tablist" aria-label="Payment method">
            <button type="button" role="tab" id="tabOnline" aria-selected="true" aria-controls="paneOnline">Pay online</button>
            <button type="button" role="tab" id="tabBank" aria-selected="false" aria-controls="paneBank" tabindex="-1">Bank transfer</button>
          </div>

          <div class="pay-pane" id="paneOnline" role="tabpanel" aria-labelledby="tabOnline">
            <div class="btn-stack">
              <a id="paynectaLink" href="{PAYNECTA}?amount=300" target="_blank" rel="noopener" class="btn btn--primary btn--block"><i class="fa-solid fa-lock" aria-hidden="true"></i> <span id="payLabel">Donate KES 300</span></a>
              {intl_links}
            </div>
            <p class="caption" style="margin-top:12px" id="payNote">Pay by M-Pesa STK push, card or bank through PayNecta. Enter your M-Pesa number at checkout and confirm the prompt on your phone.</p>
            <div class="qr kes-only"><img src="https://api.qrserver.com/v1/create-qr-code/?size=208x208&data=https://paynecta.co.ke/pay/Lishe%20Kwa%20Mtoto" alt="QR code linking to the PayNecta donation page" width="104" height="104" loading="lazy"><p>Scan with your phone camera to pay on mobile.</p></div>
          </div>

          <div class="pay-pane" id="paneBank" role="tabpanel" aria-labelledby="tabBank" hidden>
            <ul class="kv"><li><span>Bank</span><strong>Equity Bank Kenya</strong></li><li><span>Account name</span><strong>Ray of Hope Foundation Kenya</strong></li><li><span>Account no.</span><strong>0190272341642</strong></li><li><span>Branch</span><strong>Kitale Branch</strong></li><li><span>Swift code</span><strong>EQBLKENA</strong></li></ul>
            <p class="ref-box">Payment reference: <span id="refText">LISHE DONATION - your name</span></p>
            <p class="caption" style="margin-top:12px" id="bankNote">Email your transfer confirmation to {EMAIL_INFO} so we can match your gift and send a receipt. International banks may charge transfer fees and convert at their own rate.</p>
            <div class="kes-only" style="margin-top:20px;padding-top:16px;border-top:1px solid var(--line)">
              <h3 style="font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;font-weight:800;color:var(--muted);margin-bottom:6px">M-Pesa Paybill / Till</h3>
              <ul class="kv"><li><span>Till / Business no.</span><strong>{PAYBILL}</strong></li><li><span>Account name</span><strong>Lishe Kwa Mtoto</strong></li><li><span>Amount</span><strong>KES <span id="mpesaAmt">300</span></strong></li></ul>
              <p class="caption" style="margin-top:10px">Lipa na M-Pesa, then Buy Goods or Pay Bill. This is the same till connected to PayNecta, so payments are recorded either way.</p>
            </div>
          </div>
          <span id="other"></span>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="section section--sand" aria-labelledby="faq-h">
  <div class="container">
    <div class="split split--wide-text split--top">
      <div><span class="eyebrow">Questions</span><h2 id="faq-h">Giving to Lishe Kwa Mtoto.</h2></div>
      {faq([
        ('Can I donate from outside Kenya?', 'Yes. Choose your currency in the donation panel and we show the Kenyan shilling equivalent and the number of children your gift feeds. Pay online by card, or send an international bank transfer.'),
        ('Which exchange rate is used?', 'The panel shows an indicative rate, refreshed live when available. Online payments are processed in Kenyan shillings, so your card issuer or bank applies its own final rate and any fees.'),
        ('How can I pay?', 'By M-Pesa STK push, card or bank through PayNecta, by M-Pesa Paybill or Till number (Kenya), or by direct bank transfer. All details are in the donation panel.'),
        ('Will I receive a receipt?', 'Donation receipts are available on request. Email ' + EMAIL_INFO + ' with your payment details.'),
        ('Can I choose which program my gift supports?', 'Yes. Tell us which program you would like to support, or give to our general fund and we will direct your donation where it is needed most.'),
        ('How do I know my donation is recorded?', 'Donations are recorded and shown live on this page as soon as they are confirmed.'),
      ])}
    </div>
  </div>
</section>
"""
    scripts = """<script src="firebase-init.js" defer></script>
<script>
document.addEventListener('DOMContentLoaded', function () {
  var BASE = 'https://paynecta.co.ke/pay/Lishe%20Kwa%20Mtoto', GOAL = 500000, WEEK = 150, MIN_KES = 50;
  // Approximate fallback rates (units per 1 USD). Replaced by live rates when the request succeeds.
  var rates = { USD: 1, KES: 129, EUR: 0.92, GBP: 0.79, CAD: 1.37, AUD: 1.52, CHF: 0.88, SEK: 10.5, NOK: 10.7, DKK: 6.9, JPY: 150, CNY: 7.2, INR: 83, AED: 3.6725, ZAR: 18.5, UGX: 3750, TZS: 2600 };
  var live = false, cur = 'KES', amount = 300, chipIndex = 1;
  var $ = function (id) { return document.getElementById(id); };
  var sel = $('curSel'), amounts = $('amounts'), custom = $('customAmt'), cfield = $('customField');

  function fmt(v, c) {
    try { return new Intl.NumberFormat(undefined, { style: 'currency', currency: c || cur, maximumFractionDigits: (v < 100 && v % 1 !== 0) ? 2 : 0 }).format(v); }
    catch (e) { return (c || cur) + ' ' + Math.round(v).toLocaleString('en-US'); }
  }
  function perKes() { return rates[cur] / rates.KES; }          // units of cur per 1 KES
  function toKes(a) { return cur === 'KES' ? a : a / perKes(); }
  function nice(x) {
    var s = x < 10 ? 1 : x < 100 ? 5 : x < 1000 ? 50 : x < 10000 ? 500 : 5000;
    return Math.max(s, Math.round(x / s) * s);
  }
  function presets(c) {
    if (c === 'KES') return [150, 300, 600, 1500, 3000];
    if (['USD', 'EUR', 'CAD', 'AUD', 'CHF'].indexOf(c) > -1) return [5, 10, 25, 50, 100];
    if (c === 'GBP') return [5, 10, 20, 40, 80];
    return [5, 10, 25, 50, 100].map(function (u) { return nice(u * rates[c]); });
  }
  function renderChips() {
    var list = presets(cur);
    amounts.innerHTML = list.map(function (v, i) { return '<button type="button" class="amount' + (i === chipIndex ? ' active' : '') + '" data-amt="' + v + '"' + (i === chipIndex ? ' aria-pressed="true"' : '') + '>' + v.toLocaleString('en-US') + '</button>'; }).join('') +
      '<button type="button" class="amount' + (chipIndex === -1 ? ' active' : '') + '" data-amt="0" id="customChip">Other</button>';
    if (chipIndex >= 0) { amount = list[chipIndex]; cfield.hidden = true; } else { cfield.hidden = false; amount = parseFloat(custom.value) || 0; }
    $('curTag').textContent = cur;
  }
  function sync() {
    var kes = Math.ceil(toKes(amount)), kids = Math.floor(kes / WEEK), ok = kes >= MIN_KES;
    var conv = $('convert');
    if (cur === 'KES') { conv.hidden = true; }
    else {
      conv.hidden = false;
      conv.innerHTML = ok ? '<strong>' + fmt(amount) + '</strong> is about <strong>KES ' + kes.toLocaleString('en-US') + '</strong>. Rate: 1 ' + cur + ' = KES ' + (rates.KES / rates[cur]).toLocaleString('en-US', { maximumFractionDigits: 2 }) + (live ? ' (live rate).' : ' (approximate rate; live rates unavailable).')
                : 'The minimum donation is about KES ' + MIN_KES + ' (' + fmt(MIN_KES * perKes()) + ').';
    }
    $('outcome').innerHTML = !ok ? '<span>Enter at least KES ' + MIN_KES + ' to continue.</span>' : kids >= 1
      ? '<span>' + fmt(amount) + ' feeds <strong>' + kids + '</strong> ' + (kids === 1 ? 'child' : 'children') + ' for a full week</span>'
      : '<span>Every contribution counts. KES 150 feeds one child for a full week.</span>';
    var link = $('paynectaLink');
    if (ok) { link.href = BASE + '?amount=' + kes; link.removeAttribute('aria-disabled'); link.style.opacity = ''; link.style.pointerEvents = ''; }
    else { link.href = '#give'; link.setAttribute('aria-disabled', 'true'); link.style.opacity = '.55'; link.style.pointerEvents = 'none'; }
    $('payLabel').textContent = ok ? 'Donate ' + fmt(amount) + (cur === 'KES' ? '' : ' (about KES ' + kes.toLocaleString('en-US') + ')') : 'Enter an amount';
    $('mpesaAmt').textContent = kes.toLocaleString('en-US');
    $('payNote').textContent = cur === 'KES'
      ? 'Pay by M-Pesa STK push, card or bank through PayNecta. Enter your M-Pesa number at checkout and confirm the prompt on your phone.'
      : 'Card payments are processed in Kenyan shillings (about KES ' + kes.toLocaleString('en-US') + '). Your card issuer converts at its own rate. If a card is declined, use a bank transfer or contact us.';
    document.querySelectorAll('.kes-only').forEach(function (e) { e.hidden = cur !== 'KES'; });
    document.querySelectorAll('[data-kes]').forEach(function (e) { e.textContent = cur === 'KES' ? '' : 'about ' + fmt(Number(e.getAttribute('data-kes')) * perKes()); });
  }
  function setCurrency(c, keepChip) {
    if (!rates[c]) return; cur = c; sel.value = c;
    if (!keepChip) chipIndex = 1;
    renderChips(); sync();
  }
  amounts.addEventListener('click', function (e) {
    var b = e.target.closest('.amount'); if (!b) return;
    var list = presets(cur), v = parseFloat(b.getAttribute('data-amt'));
    if (v === 0) { chipIndex = -1; renderChips(); custom.focus(); }
    else { chipIndex = list.indexOf(v); renderChips(); }
    sync();
  });
  custom.addEventListener('input', function () { amount = parseFloat(custom.value) || 0; sync(); });
  sel.addEventListener('change', function () { setCurrency(sel.value, false); });

  // Payment tabs
  var tabs = [$('tabOnline'), $('tabBank')], panes = [$('paneOnline'), $('paneBank')];
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { tabs.forEach(function (x, j) { var on = i === j; x.setAttribute('aria-selected', String(on)); x.tabIndex = on ? 0 : -1; panes[j].hidden = !on; }); });
    t.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { var n = tabs[(i + 1) % 2]; n.focus(); n.click(); } });
  });

  // Initial render, then try to detect the visitor's currency
  renderChips(); sync();
  try {
    var region = ((navigator.language || '').split('-')[1] || '').toUpperCase();
    var tz = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
    var map = { US: 'USD', GB: 'GBP', CA: 'CAD', AU: 'AUD', CH: 'CHF', SE: 'SEK', NO: 'NOK', DK: 'DKK', JP: 'JPY', CN: 'CNY', IN: 'INR', AE: 'AED', ZA: 'ZAR', UG: 'UGX', TZ: 'TZS',
      DE: 'EUR', FR: 'EUR', IT: 'EUR', ES: 'EUR', NL: 'EUR', IE: 'EUR', BE: 'EUR', AT: 'EUR', FI: 'EUR', PT: 'EUR' };
    if (tz.indexOf('Africa/Nairobi') !== 0 && region !== 'KE' && map[region]) setCurrency(map[region], false);
  } catch (e) {}
  // Live exchange rates (free public endpoint); fallback table is used if this fails
  fetch('https://open.er-api.com/v6/latest/USD').then(function (r) { return r.json(); }).then(function (d) {
    if (d && d.rates && d.rates.KES) { Object.keys(rates).forEach(function (k) { if (d.rates[k]) rates[k] = d.rates[k]; }); live = true; renderChips(); sync(); }
  }).catch(function () {});

  // Reference text for bank transfer
  $('refText').textContent = 'LISHE DONATION - your full name';

  var F = window.LisheFirebase, e = F.esc;
  function ago(ts) {
    if (!ts || !ts.toDate) return 'recently';
    var m = Math.floor((Date.now() - ts.toDate().getTime()) / 60000);
    if (m < 1) return 'just now'; if (m < 60) return m + ' min ago';
    var h = Math.floor(m / 60); if (h < 24) return h + ' hr' + (h > 1 ? 's' : '') + ' ago';
    var d = Math.floor(h / 24); return d + ' day' + (d > 1 ? 's' : '') + ' ago';
  }
  var list = $('liveFeedList');
  F.db().then(function (db) {
    db.collection('donations').orderBy('timestamp', 'desc').limit(8).onSnapshot(function (snap) {
      if (snap.empty) { list.innerHTML = '<div class="feed-item"><span class="caption">Be the first to donate today.</span></div>'; return; }
      list.innerHTML = snap.docs.map(function (d) {
        var x = d.data();
        return '<div class="feed-item"><strong>' + e(x.displayName || 'Kind Donor') + '</strong><span class="when">' + e(ago(x.timestamp)) + '</span><span class="amt">KES ' + (Number(x.amount) || 0).toLocaleString('en-US') + '</span></div>';
      }).join('');
    }, function (err) { console.error('Feed:', err.message); list.innerHTML = '<div class="feed-item"><span class="caption">Recent donations are unavailable right now.</span></div>'; });
    db.collection('donations').onSnapshot(function (snap) {
      var total = 0; snap.forEach(function (d) { total += Number(d.data().amount) || 0; });
      var pct = Math.min(100, Math.round(total / GOAL * 100));
      $('progRaised').textContent = 'KES ' + total.toLocaleString('en-US');
      $('progFill').style.width = pct + '%';
      $('progBar').setAttribute('aria-valuenow', pct);
      $('progPct').textContent = pct + '% complete';
      $('progDonors').textContent = snap.size.toLocaleString('en-US');
    }, function (err) { console.error('Totals:', err.message); });
  }).catch(function (err) { console.error(err); list.innerHTML = '<div class="feed-item"><span class="caption">Recent donations are unavailable right now.</span></div>'; });
});
</script>"""
    return page('donate.html', 'donate', 'Donate | Your Donation Becomes a Meal for a Child in Kenya',
                'Give to Lishe Kwa Mtoto in KES, USD, EUR, GBP and more. Pay by M-Pesa, card or bank transfer. KES 150 feeds one child for a full week.', body,
                scripts=scripts + '\n<script src="https://paynecta.co.ke/widget.js" data-slug="Lishe Kwa Mtoto" defer></script>')


def build_volunteer():
    roles = [
        ('School Feeding Volunteer', 'Help serve meals at partner schools, support cooks, and assist with meal counting and record-keeping.', '2-3 days a week, field-based'),
        ('Nutrition Educator', 'Facilitate workshops for parents, teachers and community health volunteers on child nutrition best practice.', 'Weekends, training provided'),
        ('Emergency Response Volunteer', 'Be on call for rapid deployment during floods, drought or displacement. Pack rations and assist distribution.', 'On call, 48-hour activation'),
        ('Data & Monitoring Officer', 'Collect attendance data, conduct beneficiary surveys, and support monitoring, evaluation and donor reporting.', 'Flexible, remote possible'),
        ('Communications & Media Volunteer', 'Photograph field activities, write impact stories, and support social media content and campaigns.', 'Flexible, skills-based'),
        ('Fundraising & Events Volunteer', 'Help organise fundraising events, donor engagement activities and community awareness campaigns.', 'Evenings and weekends'),
    ]
    roles_html = ''.join(
        f'<button type="button" class="role reveal" data-role="{esc(r)}" aria-pressed="false"><h3>{esc(r).replace("&amp;", "&amp;")}</h3><p>{d}</p><span class="role__commit">{c}<i class="fa-solid fa-arrow-down" aria-hidden="true"></i></span></button>'
        for r, d, c in roles)
    body = f'''
{page_hero('west/t-4', 'Schoolchildren line up with cups and bowls for their meal', 'Volunteer', 'Volunteer with us.',
           'Leadership is the willingness to serve. Join hundreds of volunteers across Kenya making hunger history, one meal at a time.', pos='40% 50%',
           buttons='<a class="btn btn--primary" href="#roles">Find your role</a>')}

<section class="section" aria-labelledby="why-h">
  <div class="container">
    <div class="split split--wide-text split--top">
      <div class="reveal">{media('west/simitei-3', 'Pupils seated in a row smile as they eat', ar='4/5', pos='50% 35%', sizes='(min-width:900px) 36vw, 100vw')}</div>
      <div class="reveal" style="--d:.1s">
        <span class="eyebrow">Why volunteer</span>
        <h2 id="why-h" style="margin-bottom:24px">Your time is a child's meal.</h2>
        <div class="prose">
          <p class="lead">Volunteers are the engine of Lishe Kwa Mtoto. From packing emergency ration bags at our Kitale depot to running nutrition workshops in schools, every hour you give translates into children being fed and communities being strengthened.</p>
          <p>Realising our vision of a Kenya where no child learns on an empty stomach requires collaboration across every sector. Whether you are a student, a professional or a retiree, there is a role for you.</p>
        </div>
        <ul class="checks checks--dark" style="margin-top:28px">
          <li><i class="fa-solid fa-check" aria-hidden="true"></i>Gain field experience in humanitarian nutrition programmes</li>
          <li><i class="fa-solid fa-check" aria-hidden="true"></i>Build a network of change-makers across Kenya</li>
          <li><i class="fa-solid fa-check" aria-hidden="true"></i>Receive a verified volunteer certificate for each engagement</li>
          <li><i class="fa-solid fa-check" aria-hidden="true"></i>Travel support provided for field deployments</li>
          <li><i class="fa-solid fa-check" aria-hidden="true"></i>See first-hand the impact your time creates</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--sand" id="roles" aria-labelledby="roles-h">
  <div class="container">
    <div class="head"><div><span class="eyebrow">Volunteer roles</span><h2 id="roles-h">Find your role.</h2></div>
      <p class="lead">Choose a role that matches your skills and availability. Select one to add it to your application.</p></div>
    <div class="roles">{roles_html}</div>
  </div>
</section>

<section class="section" aria-labelledby="how-h">
  <div class="container">
    <div class="head"><div><span class="eyebrow">The process</span><h2 id="how-h">From application to the field.</h2></div></div>
    <div class="process">
      <div class="process__item reveal"><span class="process__no">01</span><h3>Apply</h3><p>Tell us about yourself, your preferred role and your availability. It takes about three minutes.</p></div>
      <div class="process__item reveal" style="--d:.08s"><span class="process__no">02</span><h3>We review</h3><p>We review all applications within 5 working days.</p></div>
      <div class="process__item reveal" style="--d:.16s"><span class="process__no">03</span><h3>Next steps</h3><p>Our volunteer coordinator contacts you with next steps for your chosen role.</p></div>
    </div>
  </div>
</section>

<section class="section section--white" id="apply" aria-labelledby="apply-h">
  <div class="container container--narrow">
    <form class="form-card" id="volForm" novalidate>
      <h2 id="apply-h" style="font-size:var(--fs-h2)">Volunteer application</h2>
      <p>Takes 3 minutes. We review all applications within 5 working days.</p>
      <div class="field"><label for="vName">Full name *</label><input type="text" id="vName" name="name" autocomplete="name" required></div>
      <div class="field-row">
        <div class="field"><label for="vEmail">Email address *</label><input type="email" id="vEmail" name="email" autocomplete="email" required placeholder="you@email.com"></div>
        <div class="field"><label for="vPhone">Phone number *</label><input type="tel" id="vPhone" name="phone" autocomplete="tel" required placeholder="07XX XXX XXX"></div>
      </div>
      <div class="field"><label for="vCounty">County or location</label>
        <select id="vCounty"><option value="">Select your county</option><option>Trans Nzoia</option><option>West Pokot</option><option>Turkana</option><option>Baringo</option><option>Elgeyo Marakwet</option><option>Nairobi</option><option>Other</option></select></div>
      <div class="field"><label for="vRole">Preferred role</label>
        <select id="vRole"><option value="">Select a role</option>{''.join(f'<option>{esc(r)}</option>' for r, _, _ in roles)}</select></div>
      <div class="field"><label for="vAvail">Availability</label>
        <select id="vAvail"><option>Weekdays</option><option>Weekends</option><option>Both</option><option>On-call for emergencies</option></select></div>
      <div class="field"><label for="vWhy">Why do you want to volunteer with Lishe Kwa Mtoto?</label><textarea id="vWhy" placeholder="Tell us briefly what motivates you to join our mission"></textarea></div>
      <div class="field"><label for="vSkills">Relevant skills or experience (optional)</label><textarea id="vSkills" style="min-height:100px" placeholder="Any skills, training or experience that would help in your chosen role"></textarea></div>
      <button class="btn btn--primary btn--block" type="submit" id="volSubmit">Submit application</button>
      <p class="form-msg" id="volMsg" role="status"></p>
    </form>
  </div>
</section>

<section class="section" aria-labelledby="vfaq-h">
  <div class="container">
    <div class="split split--wide-text split--top">
      <div><span class="eyebrow">Questions</span><h2 id="vfaq-h">Before you apply.</h2></div>
      {faq([
        ('How long until I hear back?', 'We review all applications within 5 working days. Our volunteer coordinator then contacts you with next steps for your chosen role.'),
        ('Do I need experience?', 'Not for every role. Nutrition educators receive training, and you can tell us about any relevant skills in your application.'),
        ('Is travel supported?', 'Travel support is provided for field deployments.'),
        ('Will I get recognition?', 'Yes. Each volunteer receives a verified volunteer certificate for each engagement.'),
        ('Can I volunteer remotely?', 'Some roles, such as data and monitoring, can be done remotely. Others are field-based.'),
      ])}
    </div>
  </div>
</section>
'''
    scripts = '''<script src="firebase-init.js" defer></script>
<script>
document.addEventListener('DOMContentLoaded', function () {
  var F = window.LisheFirebase, roleSel = document.getElementById('vRole');
  document.querySelectorAll('.role').forEach(function (card) {
    card.addEventListener('click', function () {
      document.querySelectorAll('.role').forEach(function (c) { c.classList.remove('selected'); c.setAttribute('aria-pressed', 'false'); });
      card.classList.add('selected'); card.setAttribute('aria-pressed', 'true');
      roleSel.value = card.getAttribute('data-role');
      document.getElementById('apply').scrollIntoView({ behavior: 'smooth', block: 'start' });
      document.getElementById('vName').focus({ preventScroll: true });
    });
  });
  var form = document.getElementById('volForm'), msg = document.getElementById('volMsg'), btn = document.getElementById('volSubmit');
  function say(t, ok) { msg.textContent = t; msg.className = 'form-msg show'; msg.style.borderLeftColor = ok ? 'var(--green)' : 'var(--alert)'; msg.style.background = ok ? '#eaf4ee' : '#fbf1ec'; }
  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var v = function (id) { return document.getElementById(id).value.trim(); };
    var name = v('vName'), email = v('vEmail'), phone = v('vPhone');
    if (!name || !email || !phone) { say('Please fill in your name, email and phone number.', false); return; }
    btn.disabled = true; btn.textContent = 'Submitting...';
    F.db().then(function (db) {
      return db.collection('volunteers').add({ name: name, email: email, phone: phone, county: v('vCounty'), role: v('vRole'), availability: v('vAvail'), motivation: v('vWhy'), skills: v('vSkills'), status: 'pending', submittedAt: firebase.firestore.FieldValue.serverTimestamp() });
    }).then(function () {
      say('Application received. Thank you for choosing to serve. Our volunteer coordinator will contact you within 5 working days.', true);
      btn.textContent = 'Application submitted'; form.reset();
    }).catch(function (err) { btn.disabled = false; btn.textContent = 'Submit application'; say('Submission failed. Please try again. (' + err.message + ')', false); });
  });
});
</script>'''
    return page('volunteer.html', 'volunteer', 'Volunteer | Join Lishe Kwa Mtoto in Kenya',
                'Volunteer with Lishe Kwa Mtoto in school feeding, nutrition education, emergency response, monitoring, communications or fundraising. Apply in three minutes.', body, scripts=scripts)


def build_contact():
    body = f'''
{split_hero('tn/20250708-130156', 'Lishe Kwa Mtoto team members and partners gather around bags of Lishe Mix at a school', 'Contact', 'Get in touch.',
            'Whether you want to donate, partner, volunteer or simply learn more, we would love to hear from you.', pos='50% 45%', reverse=True)}

<section class="section" aria-labelledby="contact-h">
  <div class="container">
    <div class="contact">
      <div class="reveal">
        <span class="eyebrow">Contact information</span>
        <h2 id="contact-h">Our team is based in Kitale.</h2>
        <p class="lead" style="margin-top:20px">We operate across Kenya's ASAL regions from Kitale, Trans Nzoia County.</p>
        <ul class="contact-list">
          <li><i class="fa-solid fa-envelope" aria-hidden="true"></i><div><strong>Email</strong><a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a><br><a href="mailto:{EMAIL_PROGRAMS}">{EMAIL_PROGRAMS}</a></div></li>
          <li><i class="fa-solid fa-phone" aria-hidden="true"></i><div><strong>Phone and WhatsApp</strong><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br><a href="{WHATSAPP}" target="_blank" rel="noopener">Message us on WhatsApp</a></div></li>
          <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i><div><strong>Office</strong><address><span>Ray of Hope Foundation Kenya<br>Kitale Town, Trans Nzoia County<br>P.O. Box 1234 - 30200 Kitale</span></address></div></li>
          <li><i class="fa-solid fa-clock" aria-hidden="true"></i><div><strong>Office hours</strong><span>Mon to Fri: 8:00 AM - 5:00 PM<br>Sat: 9:00 AM - 1:00 PM</span></div></li>
          <li><i class="fa-solid fa-hand-holding-heart" aria-hidden="true"></i><div><strong>M-Pesa Paybill (donations)</strong><span>{PAYBILL}</span></div></li>
        </ul>
        <p class="caption" style="margin-top:20px">We respond to all messages within 2 working days.</p>
      </div>
      <form class="form-card reveal" id="ctForm" style="--d:.1s" novalidate>
        <h2 style="font-size:var(--fs-h3)">Send a message</h2>
        <p>Tell us how we can help or how you would like to support our mission.</p>
        <div class="label" id="aboutLbl" style="font-size:.8125rem;font-weight:700;color:var(--ink);margin-bottom:10px">I am reaching out about</div>
        <div class="subjects" role="group" aria-labelledby="aboutLbl">
          <button type="button" class="subject active" aria-pressed="true">General Enquiry</button>
          <button type="button" class="subject" aria-pressed="false">Donation</button>
          <button type="button" class="subject" aria-pressed="false">Partnership</button>
          <button type="button" class="subject" aria-pressed="false">Volunteer</button>
          <button type="button" class="subject" aria-pressed="false">Media / Press</button>
        </div>
        <div class="field"><label for="ctName">Full name *</label><input type="text" id="ctName" autocomplete="name" required></div>
        <div class="field-row">
          <div class="field"><label for="ctEmail">Email address *</label><input type="email" id="ctEmail" autocomplete="email" required placeholder="you@email.com"></div>
          <div class="field"><label for="ctPhone">Phone (optional)</label><input type="tel" id="ctPhone" autocomplete="tel" placeholder="07XX XXX XXX"></div>
        </div>
        <div class="field"><label for="ctOrg">Organisation (optional)</label><input type="text" id="ctOrg" autocomplete="organization"></div>
        <div class="field"><label for="ctSubject">Subject *</label><input type="text" id="ctSubject" value="General Enquiry" required></div>
        <div class="field"><label for="ctMessage">Message *</label><textarea id="ctMessage" required></textarea></div>
        <button class="btn btn--primary btn--block" type="submit" id="ctSubmit"><i class="fa-solid fa-paper-plane" aria-hidden="true"></i> Send message</button>
        <p class="form-msg" id="ctMsg" role="status"></p>
      </form>
    </div>
  </div>
</section>
'''
    scripts = '''<script src="firebase-init.js" defer></script>
<script>
document.addEventListener('DOMContentLoaded', function () {
  var F = window.LisheFirebase, subj = document.getElementById('ctSubject');
  document.querySelectorAll('.subject').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('.subject').forEach(function (x) { x.classList.remove('active'); x.setAttribute('aria-pressed', 'false'); });
      b.classList.add('active'); b.setAttribute('aria-pressed', 'true'); subj.value = b.textContent.trim();
    });
  });
  var form = document.getElementById('ctForm'), msg = document.getElementById('ctMsg'), btn = document.getElementById('ctSubmit');
  function say(t, ok) { msg.textContent = t; msg.className = 'form-msg show'; msg.style.borderLeftColor = ok ? 'var(--green)' : 'var(--alert)'; msg.style.background = ok ? '#eaf4ee' : '#fbf1ec'; }
  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var v = function (id) { return document.getElementById(id).value.trim(); };
    if (!v('ctName') || !v('ctEmail') || !v('ctMessage')) { say('Please fill in your name, email and message.', false); return; }
    btn.disabled = true; btn.textContent = 'Sending...';
    F.db().then(function (db) {
      return db.collection('messages').add({ name: v('ctName'), email: v('ctEmail'), phone: v('ctPhone'), organization: v('ctOrg'), subject: v('ctSubject'), message: v('ctMessage'), status: 'unread', sentAt: firebase.firestore.FieldValue.serverTimestamp() });
    }).then(function () { say('Message sent. We will get back to you within 2 working days.', true); btn.textContent = 'Sent'; form.reset(); })
      .catch(function (err) { btn.disabled = false; btn.innerHTML = '<i class="fa-solid fa-paper-plane" aria-hidden="true"></i> Send message'; say('Failed to send. Please try again or WhatsApp us. (' + err.message + ')', false); });
  });
});
</script>'''
    return page('contact.html', 'contact', 'Contact Lishe Kwa Mtoto | Kitale, Kenya',
                'Contact Lishe Kwa Mtoto in Kitale, Trans Nzoia County, to donate, partner, volunteer or ask about our school feeding work. Email, phone, WhatsApp and message form.', body, scripts=scripts)
