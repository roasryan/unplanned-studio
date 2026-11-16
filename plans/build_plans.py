#!/usr/bin/env python3
"""Builds /plans/<slug>.html: free growth plans for Houston companies under $150k, one per trade.
Run: python3 plans/build_plans.py  (from the repo root)"""
import html, os

HERE = os.path.dirname(os.path.abspath(__file__))

COMMON_TRACK = ("Keep one sheet with five columns: date, name, where they found you, booked (yes/no), job value. "
                "Fill it in every time the phone rings or a form comes in. After 30 days you'll know which source pays "
                "and which one only costs you money.")

T = {
 'roofing': dict(name='Roofing', who='roofers',
   cat='Roofing contractor', svcs='Roof replacement, roof repair, storm damage inspection, insurance claim help, gutters',
   review="The day after cleanup, once the magnet sweep is done, text a photo of the finished roof with your review link. People review while they're still proud of the house.",
   speed="After a hail storm, homeowners call three or four roofers. The first one who shows up with a ladder and photos usually gets the job. If you're on a roof, a text back in one minute (\"On a job, I'll call you by 4. Want me to come look tomorrow?\") holds the lead.",
   follow="Insurance jobs stall between the inspection and the adjuster visit. Ask for the adjuster date, put it on your calendar, and call the homeowner the day after it.",
   move=("Make your free inspection a real product",
         "Take 15–20 photos, mark the damage, and text the homeowner a one-page report the same day. A clear report wins jobs that a verbal \"looks fine\" never will. After every big storm, text your past customers within 48 hours and offer a free check."),
   week="Storm weeks are your busiest. Have a text ready to send that same night."),
 'hvac': dict(name='HVAC', who='HVAC companies',
   cat='HVAC contractor or Air conditioning contractor', svcs='AC repair, AC replacement, heating repair, maintenance tune-ups, duct cleaning, thermostats',
   review="Ask right after the air is blowing cold again and the house starts to cool. That's when the homeowner is most relieved. Text the link before you back out of the driveway.",
   speed="When an AC dies on a 98-degree afternoon, people call down the list until someone picks up. A missed call is usually a lost job. If you can't answer, text back within a minute with a time you can be there.",
   follow="For replacement quotes, send the written options the same day, then check in on day 2 and day 7. Most people are comparing two or three quotes and pick the company that stayed in touch.",
   move=("Sell a maintenance plan",
         "Two tune-ups a year for a flat yearly price. Members call you first when something breaks, and the spring and fall visits fill your slow weeks. Start by offering it on every repair call."),
   week="Book spring tune-ups in February and March, before the first heat wave fills your schedule."),
 'remodeling': dict(name='Remodeling', who='remodelers',
   cat='Remodeler (add Kitchen remodeler or Bathroom remodeler as extra categories)', svcs='Kitchen remodel, bathroom remodel, whole-home remodel, additions, flooring, cabinets',
   review="Ask at the final walkthrough, while you're both standing in the finished kitchen. Send the link that night with two before-and-after photos.",
   speed="Remodel buyers ask for three bids. Reply the same day with two times you can come measure. The first contractor who gets in the house usually sets the price everyone else is compared to.",
   follow="Remodels are big decisions that take weeks. Send a written scope, then follow up on day 2, day 7, day 14 and day 30. A short text with a photo of a similar finished job works better than \"just checking in\".",
   move=("Build a before-and-after gallery by neighborhood",
         "Every job gets before, during and after photos, tagged with the neighborhood (Heights kitchen, Katy bathroom). Post them on your Google profile and website. Buyers want proof you've done a house like theirs."),
   week="Most people plan remodels around the holidays and tax refunds. Keep your follow-up list warm in January and February."),
 'pools': dict(name='Pools', who='pool companies',
   cat='Swimming pool contractor (or Pool cleaning service if you mainly do service)', svcs='New pool builds, pool remodel and resurfacing, weekly pool service, equipment repair, leak detection',
   review="For builds, ask after the first swim, not on the last day of construction. For weekly service, ask after you fix a green pool or a broken pump.",
   speed="Pool buyers shop for months. Answer fast, but more important, get them on a call or a site visit in the first week while they're excited.",
   follow="Builds have a long decision. Follow up monthly with one useful thing: a design idea, a financing option, or a photo of a pool you just finished nearby.",
   move=("Tighten your service routes",
         "Weekly service pays best when stops are close together. Pick one or two neighborhoods, then leave a door hanger at the houses around every pool you already service."),
   week="People plan new pools in winter so they can swim by summer. Your busiest selling months are January to March."),
 'fencing-concrete': dict(name='Fencing / concrete', who='fence and concrete companies',
   cat='Fence contractor or Concrete contractor (add the other as a second category)', svcs='Wood fences, iron fences, gates, fence repair, driveways, patios, sidewalks',
   review="Text a photo of the finished fence or driveway with your review link the same afternoon. Ask them to mention the neighborhood.",
   speed="Fence and driveway jobs are often booked by whoever answers first. If you're on a job, text back within a minute with a time you can come measure.",
   follow="Send the written quote the same day, then follow up on day 2 and day 7. Add a reason: \"I have a crew free the week of the 18th.\"",
   move=("Work the street",
         "When you finish a fence, leave a door hanger at the 10 houses around it: \"We just built your neighbor's fence.\" Neighbors with the same old fence are your best leads. HOA neighborhoods often need matching fences, so ask the homeowner if the HOA has a standard."),
   week="After a big storm, fences go down all over town. Text your past customers and offer a free check."),
 'foundation': dict(name='Foundation', who='foundation repair companies',
   cat='the most specific foundation category Google lists for you', svcs='Slab foundation repair, pier and beam repair, foundation inspections, drainage, leveling',
   review="Ask after the final elevation readings show the house is level, and include the before-and-after readings in your text. Numbers make a strong review.",
   speed="Homeowners usually call when a door sticks or a crack shows up and they're worried. Call back fast and calm them down. The company that explains it clearly gets the inspection.",
   follow="Repairs are expensive and scary. Send the written plan with readings, then follow up on day 2, day 7 and day 21. Offer to walk them through it on a call.",
   move=("Partner with real estate agents and home inspectors",
         "Foundation questions come up often when older Houston homes on clay soil are sold. Agents and inspectors need someone fast and honest. Meet five of them, and promise a written report within 48 hours."),
   week="Houston's clay soil moves with long dry spells and heavy rain. Calls pick up after both, so be ready."),
 'plumbing': dict(name='Plumbing', who='plumbers',
   cat='Plumber', svcs='Drain cleaning, water heater repair and replacement, slab leaks, repiping, leak detection, emergency plumbing',
   review="Ask when the water is back on, while they're still relieved. Text the link before you leave.",
   speed="A leaking pipe can't wait. People call down the list until someone answers. If you miss a call, text back within a minute with a time.",
   follow="For big quotes like repipes or slab leaks, send the written options the same day, then follow up on day 2 and day 7.",
   move=("Go back to your past customers",
         "Your old customers are the cheapest jobs you'll ever book. Note water heater ages on every call, and text owners of older units before they fail. A yearly \"plumbing check\" text brings back repeat work."),
   week="Freezes and heavy rain bring a wave of calls. Have a plan for who answers the phone that week."),
 'electrical': dict(name='Electrical / generators', who='electricians and generator installers',
   cat='Electrician (add a generator category if Google lists one that fits)', svcs='Panel upgrades, standby generators, EV chargers, lighting, wiring repairs, inspections',
   review="Ask after the panel is live or the generator passes its first test run. Text the link the same day.",
   speed="After an outage, generator interest jumps and people call several installers. The first one who books a site visit usually wins.",
   follow="Generators and panel upgrades are big purchases. Send the written quote the same day, then follow up on day 2, day 7 and day 30.",
   move=("Sell generator maintenance",
         "Every standby generator needs regular service. A yearly plan keeps you in touch with the owner and brings repeat work. Offer it with every install."),
   week="Hurricane season starts June 1. Talk to generator leads in the spring, before installers book up."),
 'landscaping': dict(name='Landscaping', who='landscaping companies',
   cat='Landscaper (or Lawn care service if you mainly mow)', svcs='Lawn care, landscape design and install, irrigation, drainage, tree and shrub care, seasonal color',
   review="Ask after a new install or a big cleanup, with a photo of the finished yard.",
   speed="People asking for a mowing quote often message three companies. Reply the same day with a price or a time to look.",
   follow="For installs, send the written quote with a sketch or photo of a similar yard, then follow up on day 2 and day 7.",
   move=("Build tight routes and add on",
         "Mowing pays when stops are close together. Leave a door hanger around every yard you already service. Then offer add-ons to current customers: seasonal color, mulch, irrigation checks."),
   week="Spring is when people sign up. Start asking current customers for referrals in February."),
 'med-spa': dict(name='Med spa', who='med spas',
   cat='Medical spa', svcs='Botox and Dysport, fillers, facials, microneedling, laser hair removal, skin consults',
   review="Ask at the follow-up visit, when they can see their results, not on treatment day.",
   speed="Many clients message on Instagram or text before they book. Reply within minutes during open hours. A slow reply sends them to the next spa.",
   follow="After a consult, follow up on day 2 with a short note about what you discussed. Then once more on day 10.",
   move=("Rebook before they leave",
         "Botox and fillers repeat every few months. Book the next visit before the client walks out, and offer a membership for regulars. Always get written consent before using anyone's photos."),
   week="Before holidays, weddings and summer, demand goes up. Remind past clients a few weeks early."),
 'other': dict(name='Home service', who='home service companies',
   cat='the most specific category Google lists for your main service', svcs='Your top five services, each one written out separately',
   review="Ask right after the job, when the customer is happiest. Text the link before you leave.",
   speed="Most customers call two or three companies. If you can't answer, text back within a minute with a time you can help.",
   follow="Send every quote in writing the same day, then follow up on day 2 and day 7.",
   move=("Go back to your past customers",
         "Your old customers are the cheapest jobs you'll ever book. Text them once a season with something useful, and ask happy ones for a referral."),
   week="Find your slow months and plan a past-customer text before each one."),
}

SOURCES = [
 ('Google: How to improve your local ranking', 'https://support.google.com/business/answer/7091'),
 ('Harvard Business Review: The Short Life of Online Sales Leads', 'https://hbr.org/2011/03/the-short-life-of-online-sales-leads'),
]

CSS = """:root{--bg:#FAF9F6;--paper:#fff;--line:#E6E2DA;--text:#15171C;--soft:#5B616C;--mute:#8A8F98;--accent:#B5821F;--sand:#F3EEE5;
--display:'Inter Tight','Inter',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;--body:'Inter',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;color-scheme:light}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:400 17px/1.6 var(--body);-webkit-font-smoothing:antialiased}
a{color:inherit}:focus-visible{outline:3px solid #2563EB;outline-offset:3px;border-radius:6px}
.wrap{max-width:760px;margin:0 auto;padding:0 16px}
header{border-bottom:1px solid var(--line);background:rgba(250,249,246,.9);position:sticky;top:0;backdrop-filter:blur(8px);z-index:2}
header .wrap{display:flex;align-items:center;justify-content:space-between;height:64px}
.brand{display:flex;gap:10px;align-items:center;font:700 18px var(--display);text-decoration:none}
.brand i{width:30px;height:30px;border-radius:8px;background:var(--text);color:#fff;display:grid;place-items:center;font-style:normal}
.btn{display:inline-block;background:var(--text);color:#fff;text-decoration:none;font-weight:600;padding:12px 18px;border-radius:12px}
.btn.line{background:transparent;color:var(--text);border:1px solid var(--line)}
h1,h2,h3{font-family:var(--display);letter-spacing:-.02em;line-height:1.1;margin:0}
h1{font-size:clamp(32px,6vw,48px);font-weight:800}h2{font-size:24px;margin-bottom:8px}
.eyebrow{font:600 13px/1.2 var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin:40px 0 12px}
.lede{color:var(--soft);font-size:19px;margin:14px 0 0}
.note{background:var(--sand);border-radius:14px;padding:16px 18px;margin:24px 0;font-size:16px}
ol.steps{list-style:none;padding:0;margin:32px 0;display:grid;gap:16px;counter-reset:s}
ol.steps li{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:20px 20px 20px 64px;position:relative;counter-increment:s}
ol.steps li:before{content:counter(s);position:absolute;left:18px;top:18px;width:32px;height:32px;border-radius:9px;background:var(--text);color:#fff;display:grid;place-items:center;font:700 15px var(--display)}
ol.steps p{margin:6px 0 0;color:var(--soft)}ol.steps b{color:var(--text)}
.check{list-style:none;padding:0;margin:12px 0 0;display:grid;gap:8px}
.check li{padding-left:30px;position:relative}.check li:before{content:'';position:absolute;left:0;top:5px;width:16px;height:16px;border:2px solid var(--line);border-radius:5px;background:#fff}
.cta{background:var(--text);color:#fff;border-radius:20px;padding:28px 22px;margin:40px 0}
.cta p{color:#C9CDD4;margin:10px 0 18px}.cta .btn{background:#fff;color:var(--text)}
footer{color:var(--mute);font-size:14px;padding:24px 0 48px}footer a{color:var(--soft)}
.src{font-size:14px;color:var(--mute)}.src a{color:var(--soft)}"""

def page(slug, d):
    e = html.escape
    name, who = d['name'], d['who']
    title = f"Free growth plan for Houston {who}"
    steps = [
      ("Fix your Google Business Profile",
       f"Set your primary category to <b>{e(d['cat'])}</b>. List each service on its own: {e(d['svcs'])}. Add your real hours, service area and 10+ photos of your own jobs. Google says complete, accurate profiles are more likely to show up in local search."),
      ("Ask every happy customer for a review", e(d['review']) + " Reply to every review, good or bad. Google counts reviews and how you respond as part of how well-known you are."),
      ("Answer fast, or text back fast", e(d['speed']) + " One well-known Harvard Business Review study found companies that responded within an hour were about 7 times more likely to qualify the lead than ones that waited longer."),
      ("Follow up on every quote", e(d['follow']) + " When two quotes are close, the job often goes to the company that stayed in touch."),
      (e(d['move'][0]), e(d['move'][1])),
      ("Track where every job comes from", e(COMMON_TRACK)),
    ]
    li = "\n".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in steps)
    src = " · ".join(f'<a href="{u}" rel="noopener" target="_blank">{e(t)}</a>' for t, u in SOURCES)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)} · Unplanned &amp; Co.</title>
<meta name="description" content="A free, step-by-step growth plan for Houston {e(who)} under $150k a year: Google profile, reviews, fast replies, quote follow-up and tracking.">
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Inter+Tight:wght@700;800&display=swap">
<style>{CSS}</style></head><body>
<header><div class="wrap"><a class="brand" href="/"><i>U</i>Unplanned &amp; Co.</a><a class="btn line" href="/">Main site</a></div></header>
<main class="wrap">
<p class="eyebrow">Free growth plan · {e(name)}</p>
<h1>Your growth plan for {e(name if slug=='hvac' else name.lower()) if slug!='other' else 'home service'} in Houston.</h1>
<p class="lede">Made for {e(who)} doing under $150k a year. Six steps, in order. Most cost nothing but a few hours. Do one a week.</p>
<div class="note"><b>From Ryan:</b> these are the same basics I check first for bigger companies. Get these right and the phone gets busier. When it does, reply to the email this came in and tell me what you're stuck on. I may have an option for you.</div>
<ol class="steps">
{li}
</ol>
<h2>Your next 30 days</h2>
<ul class="check">
<li>Week 1: Google profile complete, every service listed, 10+ real photos.</li>
<li>Week 2: Review text ready to send. Ask every customer this week.</li>
<li>Week 3: Missed-call text set up on your phone. Every quote followed up.</li>
<li>Week 4: Start the tracking sheet and do step 5.</li>
</ul>
<p class="note"><b>Timing tip:</b> {e(d['week'])}</p>
<div class="cta"><h2 style="color:#fff">Want help with this?</h2>
<p>Reply to the email this plan came in. Tell me your trade and what's holding you back. I read every reply myself. Once you pass $150k a year, apply for the full growth audit.</p>
<a class="btn" href="/">See how it works</a></div>
<p class="src">Sources: {src}</p>
</main>
<footer><div class="wrap">Unplanned &amp; Co. · Houston, TX · <a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a></div></footer>
</body></html>
"""

if __name__ == '__main__':
    for slug, d in T.items():
        with open(os.path.join(HERE, slug + '.html'), 'w', encoding='utf8') as f:
            f.write(page(slug, d))
        print('wrote', slug)
