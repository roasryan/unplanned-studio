"""Builds the area pages (areas/<slug>/index.html), the areas hub, sitemap.xml and robots.txt.
Edit AREAS, then run: python3 areas/build_areas.py"""
import json, html, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://unplannedco.com'
AREAS = [
 dict(slug='katy', fix='For Katy companies I start with speed: an instant text back on every form and missed call, and online booking so the homeowner picks a time before they shop around. Then follow-up on every quote, and a report showing which neighborhoods and ads book jobs.', name='Katy', county='Harris, Fort Bend and Waller counties',
  intro="Katy spreads across three counties along I-10 and the Grand Parkway, and master-planned neighborhoods like Cinco Ranch and Cross Creek Ranch keep adding rooftops. For a roofer, HVAC company or pool builder, that means a steady flow of homeowners shopping for a first big upgrade, and a lot of competitors chasing the same Google searches.",
  leak="A Cross Creek Ranch homeowner fills out your form at 9 PM asking about a pool. By 7 AM they've already booked two other builders who texted back first. The lead was paid for. The job went somewhere else.",
  trades='roofing, HVAC, pools and landscaping',
  faq=("Do you only work with Katy companies?", "No. I work with home service companies across greater Houston. Katy is one of the busiest areas because of how fast it's growing, so speed to the lead matters even more there.")),
 dict(slug='sugar-land', fix='For Sugar Land companies I start with estimate follow-up: a simple sequence that checks in after every quote until the job is won or lost. Then fast replies on new calls and forms, and a list of past customers due for their next job.', name='Sugar Land', county='Fort Bend County',
  intro="Sugar Land sits along I-69 and Highway 6 in Fort Bend County. Neighborhoods like First Colony started going up in the late 1970s and 80s, so a lot of homes now need new roofs, new AC systems and remodeled kitchens at the same time newer areas like Riverstone fill in.",
  leak="A First Colony owner gets three roof quotes. Yours was the best price, but nobody followed up after you sent it. The company that called back twice got the job.",
  trades='roofing, HVAC, remodeling and plumbing',
  faq=("I get most of my Sugar Land work from referrals. Why would I need this?", "Keep the referrals. The system makes sure every referral that calls or texts gets an answer fast, and it shows you which past customers to ask for the next one.")),
 dict(slug='the-woodlands', fix='For Woodlands companies I start with long-cycle follow-up that keeps in touch while a project waits on approval. Then online booking for estimates, a text-back on missed calls, and tracking that shows which leads turned into jobs months later.', name='The Woodlands', county='Montgomery and Harris counties',
  intro="The Woodlands is a township north of Houston, mostly in Montgomery County, known for its heavy tree cover and strict residential design review. Exterior projects often need approval before work starts, so fence, roofing and remodeling jobs take longer to close and need more follow-up.",
  leak="A homeowner asks for a fence estimate, then waits on design review. Six weeks later they're approved, but nobody on your side checked in. They hire whoever reached out last.",
  trades='roofing, fencing, remodeling and tree-heavy gutter and landscape work',
  faq=("My Woodlands jobs take months to close. Does follow-up really matter?", "That's exactly where it matters most. Long sales cycles are where quotes go quiet. I set up follow-up that keeps checking in until the job is approved, won or lost.")),
 dict(slug='cypress', fix='For Cypress companies I start with after-hours coverage: a text back on every missed call and online booking that works at 8 PM. Then follow-up on quotes and tracking so you know which ads bring in the new-build owners.', name='Cypress', county='northwest Harris County',
  intro="Cypress is an unincorporated area along US 290 in northwest Harris County, with large newer communities like Bridgeland and Towne Lake. New homes mean first-time buyers looking for pools, patios, landscaping and upgrades, and they search on their phones in the evening.",
  leak="A new Bridgeland owner searches for a patio cover at 8 PM and taps your call button. It rings to voicemail. They tap the next company on the map.",
  trades='pools, landscaping, patio covers, HVAC and electrical',
  faq=("Most of my Cypress calls come after hours. What can I do?", "Every missed call gets a text back in under a minute, and customers can pick a time online at night. You wake up to booked visits instead of voicemails.")),
 dict(slug='pearland', fix='For Pearland companies I start with the form: short, phone number required, and a booking time right after. Then a fast text back on calls you miss, follow-up after every inspection, and one report on what booked.', name='Pearland', county='Brazoria, Fort Bend and Harris counties',
  intro="Pearland grew along the State Highway 288 corridor south of Houston, with Shadow Creek Ranch on its west side. Like much of the Houston area it sits on expansive clay soil, so foundation, plumbing and drainage work stays in demand.",
  leak="A homeowner notices a crack over a door and requests a foundation inspection online. Your form asks 11 questions and doesn't require a phone number. They give up halfway and call someone else.",
  trades='foundation repair, plumbing, drainage and roofing',
  faq=("Can you help with high-ticket jobs like foundation repair?", "Yes. Big-ticket jobs are where one recovered lead pays for the system. I focus on fast first contact and follow-up after the inspection.")),
 dict(slug='spring', fix="For Spring companies I start with the calls your techs can't answer: a text back in under a minute and online booking. Then reminders that cut no-shows, and tracking that shows which jobs came from which source.", name='Spring', county='north Harris County',
  intro="Spring is an unincorporated area in north Harris County along I-45 and the Grand Parkway, home to Old Town Spring. It mixes established neighborhoods from the 1970s and 80s with new subdivisions, so the same company might be replacing a 20-year-old AC in the morning and quoting a new build in the afternoon.",
  leak="Your tech is in an attic on a 98-degree afternoon. Three calls come in. Two hang up when they hit voicemail and never call back.",
  trades='HVAC, plumbing, electrical and roofing',
  faq=("My techs answer the phone themselves. Is that a problem?", "It works until they're on a job. A missed-call text back and online booking catch the calls they can't answer, without hiring a dispatcher.")),
 dict(slug='league-city', fix="For League City companies I start with surge handling: an instant text and booking link for every caller, and one list of every request in order. Then follow-up after the rush, so storm leads don't go cold.", name='League City', county='Galveston County',
  intro="League City sits in Galveston County between Houston and Galveston, near Clear Lake. Being this close to the coast means storm season drives sudden spikes in calls for roofing, generators and water damage work, often all on the same week.",
  leak="A tropical storm rolls through on Thursday. By Friday you have 40 missed calls and no way to sort who needs you first. By Monday half of them have hired someone else.",
  trades='roofing, standby generators, water damage and HVAC',
  faq=("How do you handle storm surges?", "Every caller gets an instant text with a booking link, so people pick a time instead of waiting on hold. You see every request in one list, sorted by when it came in.")),
 dict(slug='conroe', fix='For Conroe companies I start with booking that knows your map: service-area checks on every address and drive time between visits. Then a text back on missed calls and follow-up on every estimate.', name='Conroe', county='Montgomery County',
  intro="Conroe is the county seat of Montgomery County, along I-45 north of The Woodlands, with Lake Conroe to the west. Service areas up here are spread out, so a booked visit in the wrong spot can cost a crew an hour of driving.",
  leak="Your calendar books a 9 AM estimate on the far side of Lake Conroe and a 10 AM one back in town. The crew is late to both.",
  trades='roofing, HVAC, pools and fencing',
  faq=("My service area is huge. Can the booking handle that?", "Yes. The booking checks the address against your service area and can leave drive time between visits, so your day makes sense on a map.")),
 dict(slug='pasadena', fix='For Pasadena companies I start with a site customers can read in English or Spanish, with price ranges and a text button. Then a fast text back on missed calls and follow-up on every quote.', name='Pasadena', county='Harris County',
  intro="Pasadena is east of Houston in Harris County, near the Houston Ship Channel, with many established neighborhoods and a large Spanish-speaking population. Homeowners here compare prices closely and often prefer to talk or text in Spanish.",
  leak="A homeowner reads your English-only site, can't find a price range, and texts a competitor whose page is in Spanish.",
  trades='plumbing, HVAC, roofing and remodeling',
  faq=("Can my site be in Spanish too?", "Yes. I can set up every page in Spanish, so Spanish-speaking customers can read, book and text you in the language they prefer.")),
 dict(slug='humble', fix='For Humble companies I start with tracking: every lead tied to the ad or search it came from and the job it became. Then a fast text back on missed calls, follow-up on estimates, and one monthly report by source.', name='Humble', county='northeast Harris County',
  intro="Humble is in northeast Harris County near George Bush Intercontinental Airport, with Atascocita, Kingwood and Lake Houston close by. Many companies here serve the whole northeast side, so knowing which neighborhoods and which ads bring in jobs decides where the money goes next.",
  leak="You spend on Google, Facebook and Angi, but nobody can tell you which one booked last month's Kingwood remodel. So you keep paying for all three.",
  trades='remodeling, roofing, HVAC and plumbing',
  faq=("I run ads in a few places. Can you tell me which ones work?", "Yes. Every lead is tracked from the ad or search it came from to the booked job, and you get one simple monthly report by source.")),
]
NEAR = {a['slug']: [] for a in AREAS}
order = [a['slug'] for a in AREAS]
for i, a in enumerate(AREAS):
    NEAR[a['slug']] = [order[(i + k) % len(order)] for k in (1, 2, 3)]
BYS = {a['slug']: a for a in AREAS}
E = html.escape

HEAD = '''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#FAF9F6">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:image" content="https://unplannedco.com/img/og-home.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Anton&display=swap">
<link rel="stylesheet" href="/areas/area.css">
<script type="application/ld+json">{ld}</script>
</head><body>
<header class="top"><div class="wrap"><a class="logo" href="/"><svg viewBox="0 0 32 32" aria-hidden="true"><rect x="2" y="2" width="28" height="28" rx="8" fill="#15171C"/><path d="M10.5 10v7.5a5.5 5.5 0 0 0 11 0V10" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/></svg>Unplanned &amp; Co.</a><details class="nav-menu"><summary>Services <span aria-hidden="true">▾</span></summary><div class="nav-pop"><a href="/services/"><b>All services</b><span>Everything I can set up and run for you</span></a><a href="/services/#now"><b>Start right now (free)</b><span>Audit, growth plan for your trade, demo sites</span></a><a href="/#claim"><b>Claim 1 free service</b><span>Held for you for 48 hours</span></a><a href="/#demo"><b>Free 15-minute Growth Audit</b><span>Apply in about 2 minutes</span></a><a href="https://catalog.unplannedco.com/" target="_blank" rel="noopener"><b>Demo sites</b><span>Try one built for your trade</span></a><a href="/areas/"><b>Areas we serve</b><span>Houston and nearby cities</span></a><a href="/#faq"><b>Questions owners ask</b><span>Cost, contracts, guarantees</span></a></div></details><a class="btn" href="/#demo">Apply now</a></div></header>
<main class="wrap">
'''
FOOT = '''</main>
<footer><div class="wrap"><span>© 2026 Unplanned &amp; Co. · Serving Houston and the surrounding areas</span><nav><a href="/services/">Services</a><a href="/areas/">Areas we serve</a><a href="/privacy.html">Privacy</a><a href="/terms.html">Terms</a></nav></div></footer>
</body></html>
'''

def page(a):
    url = f"{SITE}/areas/{a['slug']}/"
    title = f"Home Service Marketing in {a['name']}, TX | Unplanned & Co."
    desc = f"Home service marketing in {a['name']}, TX: more booked jobs from the leads you already get. Free 15-minute Growth Audit. Setup fee back if we miss the target."
    q, ans = a['faq']
    ld = [{"@context": "https://schema.org", "@type": "ProfessionalService", "name": "Unplanned & Co.", "url": SITE + "/",
           "description": f"Growth partner for home service companies in {a['name']}, TX: fast lead response, online booking, follow-up and lead tracking.",
           "areaServed": [{"@type": "City", "name": f"{a['name']}, TX"}, {"@type": "City", "name": "Houston, TX"}]},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
              {"@type": "ListItem", "position": 2, "name": "Areas we serve", "item": SITE + "/areas/"},
              {"@type": "ListItem", "position": 3, "name": a['name'], "item": url}]},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
              {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}}]}]
    near = ''.join(f'<a href="/areas/{s}/">{E(BYS[s]["name"])}</a>' for s in NEAR[a['slug']])
    body = f'''<nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a> › <a href="/areas/">Areas we serve</a> › {E(a['name'])}</nav>
<section class="hero">
  <p class="pill">{E(a['name'])}, TX · home service companies doing $150K+</p>
  <h1>More booked jobs for {E(a['name'])} home service companies.</h1>
  <p class="sub">Home service marketing in {E(a['name'])} that starts with the leads you already pay for: fast replies, online booking and follow-up, tracked to the job.</p>
  <a class="btn big" href="/">Start my free Growth Audit</a>
</section>
<section><h2>Home service work in {E(a['name'])}</h2><p>{E(a['intro'])}</p><p>I work with {E(a['trades'])} companies here and across {E(a['county'])}.</p></section>
<section class="moment"><h2>Where {E(a['name'])} jobs slip away</h2><p>{E(a['leak'])}</p></section>
<section><h2>What I set up in {E(a['name'])}</h2><p>{E(a['fix'])}</p>
<p class="guar">We set a booked-appointment target for your first 60 days. Miss it and your setup fee comes back, in writing, as long as your team answers new leads within an hour.</p></section>
<section class="faq"><h2>Question from {E(a['name'])} owners</h2><details open><summary>{E(q)}</summary><p>{E(ans)}</p></details></section>
<section class="cta"><h2>Get your free 15-minute Growth Audit.</h2><p>You keep the plan either way. Under $150K a year? Still apply and I'll email you a growth plan for your trade.</p><a class="btn big" href="/">Apply now</a></section>
<p class="near">Also serving: {near} · <a href="/areas/">All areas</a></p>
'''
    return HEAD.format(title=E(title), desc=E(desc), url=url, ld=json.dumps(ld)) + body + FOOT

def hub():
    url = f"{SITE}/areas/"
    title = "Areas We Serve: Houston Home Service Marketing | Unplanned & Co."
    desc = "Home service marketing for companies across greater Houston: Katy, Sugar Land, The Woodlands, Cypress, Pearland, Spring, League City, Conroe and more."
    ld = {"@context": "https://schema.org", "@type": "ProfessionalService", "name": "Unplanned & Co.", "url": SITE + "/",
          "areaServed": [{"@type": "City", "name": "Houston, TX"}] + [{"@type": "City", "name": f"{a['name']}, TX"} for a in AREAS]}
    items = ''.join(f'<li><a href="/areas/{a["slug"]}/"><b>{E(a["name"])}</b><span>{E(a["trades"].capitalize())}</span></a></li>' for a in AREAS)
    body = f'''<nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a> › Areas we serve</nav>
<section class="hero"><p class="pill">Houston and the surrounding areas</p><h1>Areas we serve.</h1>
<p class="sub">I help home service companies across greater Houston turn the leads they already get into booked jobs. Pick your area to see what that looks like there. Outside these areas? Still apply.</p></section>
<ul class="grid">{items}</ul>
<section class="cta"><h2>Get your free 15-minute Growth Audit.</h2><a class="btn big" href="/">Apply now</a></section>
'''
    return HEAD.format(title=E(title), desc=E(desc), url=url, ld=json.dumps(ld)) + body + FOOT


SERVICES = [
 ("Win the lead", [
  ("Missed-call text back", "Anyone you miss gets a text within a minute, so they wait for you instead of calling the next company."),
  ("60-second lead alerts", "Name, mobile, address and best time to call, straight to your phone."),
  ("Online booking", "Customers pick a real open time, synced both ways with your Google Calendar."),
  ("Text-us button", "Customers text you from any page instead of filling out a long form."),
  ("Instant price tool", "Price ranges for your services, or an instant roof quote from the satellite outline."),
  ("AI receptionist and website chat", "Optional. Answers after hours and books the visit when nobody can pick up."),
 ]),
 ("Follow up and close", [
  ("Estimate follow-up", "Every quote gets checked on until it's won or lost, so jobs stop going quiet."),
  ("Reminders that cut no-shows", "Confirmation and reminder texts before every visit."),
  ("Change orders", "Customers approve extra work with a signature on their phone."),
 ]),
 ("Bring them back", [
  ("Referral program", "Referral links for realtors, inspectors and past customers, with payouts tracked."),
  ("Past-customer comebacks", "A reactivation campaign every quarter to customers you already served."),
  ("Review requests", "A review request after every job, without asking by hand."),
  ("Memberships", "Maintenance or club plans that bring customers back every year."),
 ]),
 ("Get found", [
  ("Website built to book jobs", "Your services, photos and brand, fast on phones, with booking on every page."),
  ("Service and city pages", "A page for every service and the areas you cover, so you show up in more searches."),
  ("Google Business Profile tune-up", "Services, hours and categories set up to show in Maps."),
  ("Ads managed for you", "Google and Meta. You film the clips, I handle setup, targeting and tracking."),
  ("Spanish site", "Every page in Spanish for Houston's Spanish-speaking customers."),
 ]),
 ("Know what's working", [
  ("Tracking on every lead", "Meta and Google tracking, so each lead ties back to the ad or search it came from."),
  ("One simple monthly report", "Cost per lead, close rate and booked jobs by source."),
  ("You own it all", "Domain, site, ad accounts and customer list stay yours."),
 ]),
]
PLANS = [("roofing","Roofing"),("hvac","HVAC"),("plumbing","Plumbing"),("foundation","Foundation"),("remodeling","Remodeling"),("pools","Pools"),("fencing-concrete","Fencing / concrete"),("electrical","Electrical"),("landscaping","Landscaping"),("med-spa","Med spa"),("other","Other trades")]

def services():
    url = f"{SITE}/services/"
    title = "Services: Home Service Growth in Houston | Unplanned & Co."
    desc = "Everything Unplanned & Co. sets up and runs for Houston home service companies: lead response, booking, estimate follow-up, referrals, reviews, SEO, ads and tracking."
    ld = {"@context": "https://schema.org", "@type": "ProfessionalService", "name": "Unplanned & Co.", "url": SITE + "/",
          "areaServed": [{"@type": "City", "name": "Houston, TX"}],
          "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
              {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "description": d}} for _, items in SERVICES for n, d in items]}}
    groups = ''.join(f'<section><h2>{E(g)}</h2><ul class="svc">' + ''.join(f'<li><b>{E(n)}</b><span>{E(d)}</span><em class="ask">Interested? Mention it on your call with Unplanned &amp; Co.</em></li>' for n, d in items) + '</ul></section>' for g, items in SERVICES)
    plans = ''.join(f'<a href="/plans/{k}.html">{E(v)}</a>' for k, v in PLANS)
    body = (f'<nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a> › Services</nav>\n'
      '<section class="hero"><p class="pill">Houston home service companies</p><h1>Services.</h1>\n'
      '<p class="sub">Everything I can set up and run for you. Your plan is custom built from your audit, so not every service goes in every plan. See something you want? Mention it on your call and I\'ll tell you if it fits.</p></section>\n'
      '<section id="now"><h2>Start right now (free)</h2>\n<ul class="grid">\n'
      '<li><a href="/#claim"><b>Claim 1 free service</b><span>Referral program, past-customer comeback, review requests or a Google profile tune-up. Held 48 hours, free if we work together.</span></a></li>\n'
      '<li><a href="/#demo"><b>Free 15-minute Growth Audit</b><span>Apply in about 2 minutes, pick your call time right after. Keep the plan either way.</span></a></li>\n'
      '<li><a href="https://catalog.unplannedco.com/" target="_blank" rel="noopener"><b>Try a demo site</b><span>Book a visit on a working site built for your trade.</span></a></li>\n'
      '<li><a href="/areas/"><b>Areas we serve</b><span>See what this looks like in your part of Houston.</span></a></li>\n</ul>\n'
      f'<p><b>Free growth plan for your trade:</b></p><p class="near">{plans}</p></section>\n'
      + groups +
      '<section class="cta"><h2>Not sure what you need?</h2><p>That\'s what the audit is for. I\'ll show you where your jobs are slipping and which of these fixes it first.</p><a class="btn big" href="/#demo">Get my free Growth Audit</a></section>\n')
    return HEAD.format(title=E(title), desc=E(desc), url=url, ld=json.dumps(ld)) + body + FOOT

os.makedirs(os.path.join(ROOT, 'services'), exist_ok=True)
open(os.path.join(ROOT, 'services', 'index.html'), 'w').write(services())

for a in AREAS:
    d = os.path.join(ROOT, 'areas', a['slug']); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(page(a))
open(os.path.join(ROOT, 'areas', 'index.html'), 'w').write(hub())
urls = [SITE + '/', SITE + '/services/', SITE + '/areas/'] + [f"{SITE}/areas/{a['slug']}/" for a in AREAS]
open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{u}</loc></url>\n' for u in urls) + '</urlset>\n')
open(os.path.join(ROOT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
print(len(AREAS), 'area pages')
