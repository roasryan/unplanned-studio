# Handoff: Unplanned & Co. ads + /audit landing page (Nov 23, 2026)

Everything from the Nov 23 session: the ad drafts, the data behind them, the landing-page review, and the /audit page draft. The messages below are copied word for word.

## What's in this folder

| Path | What it is |
|---|---|
| `ads/ad-a.png`, `ad-b.png`, `ad-c.png` | The three new ad images (1080×1350), ready to upload |
| `ads/ads.html` + `ads/shot.js` | Source for the ad images. Edit the HTML, then run `node shot.js` to re-render the PNGs. (`shot.js` reads `/home/claude/ads/ads.html`; change the path for your machine.) |
| `landing-page-screens/` | Phone screenshots of the /audit draft: top of page, the lock-screen animation, the About me card, the full page and the application pop-up |
| `data/meta-ads-2026-11-23.json` | Every Meta Ads number pulled that day: account spend, campaign total, lifetime results for all 18 ads, S8's creative and trend |
| `data/dashboard-and-leads-2026-11-23.md` | The lead-sheet check and the dashboard spend update |
| `data/landing-page-review.md` | The text read of unplannedco.com the review was based on |

**The /audit page itself is on a different branch:** `audit-landing-page`, file `audit/index.html`. This `handoff-2026-11-23` branch is notes only. **Don't merge it into main**, since main is your live site and these notes would become public.

---

## 1. Handoff summary

**Ad results so far (Meta campaign "Static test – $3/day per ad," ID 120272399628620362):**
- The campaign has spent its full $150 cap. Across all ads: about 70 page visits and 2 applications (one from S5c, one from S1).
- Only S8 "One guy – Ryan edits" is still on. It has 6 clicks and 0 leads. It uses the S5c growth-report image.
- The "Unfinished applications" tab has never had a row, so most visitors likely never open the form. The page is the bottleneck, not the form.

**New ad drafts:** three images with the bottom line "Don't trust me? Good. Look at unplannedco.com and see what I'm about."
- **A (top pick):** a 2:07 Saturday lock screen with 3 missed calls and "Never mind, we found someone." Headline: "You didn't lose that job. Your voicemail did."
- **B:** "I'm one guy. If I miss, you get paid back." (the 60-day setup-fee-back guarantee)
- **C:** "~~More leads~~ won't fix your business."
- None are uploaded to Meta yet. The campaign needs more budget before a new ad can run.

**Problems with the main site, unplannedco.com:**
- It doesn't continue the "one guy" ad.
- It shows dental, med spa and salon demos, so it reads like a web developer.
- There's no photo of Ryan, and every number on it is labeled a sample.
- The guarantees sit at section 8 of 13, in about 1,400 words with 12+ buttons.

**Fix built: unplannedco.com/audit.** It's a draft on the GitHub branch `audit-landing-page` in roasryan/unplanned-studio, file audit/index.html. It is not merged or live.
- The ad's headline at the top, with animated lock-screen notifications.
- "About me: I'm one guy, not an agency," with a photo card.
- The 4 places jobs leak out, 3 guarantees, a not-for-under-$150k line and how it works.
- The same application pop-up as the main site, plus an apply bar that stays at the bottom on phones.
- Tracking: applications are tagged "Audit page (ad)," plus a new event when visitors scroll to the guarantees.

**Waiting on Ryan:**
1. A photo of himself, which goes in /img/ryan.webp, then set `RYAN_PHOTO`.
2. A 3–4 sentence about-me in his own words.
3. Confirm the line "You text me directly, not a support inbox."
4. Decide whether to remove "Med spa" from the application's business types.

**Next steps:** merge the branch, then upload ad A as a paused ad pointing to unplannedco.com/audit and add budget.

---

## 2. Scheduled check, 06:01 UTC

This run was at 06:01 UTC (00:01 Chicago), so I ran the new lead check and the ad spend update. The daily outreach leads job only runs at 6 AM Chicago, so it was skipped.

- **New lead check:** No new applications. Both real rows in the sheet (the Nov 5 and Nov 12 applicants) are already on the dashboard, so no alert went out. The November spend figure on the dashboard is up to date at $152.23, dated Nov 23.
- **Ad spend update (sent to your phone):**
  - $152.23 spent this month and $0 so far today.
  - The static test campaign has hit its $150 cap. It had 0 views, clicks and leads today.
  - 17 of the 18 ads are paused, either directly or because their ad set is paused. Only "S8 One guy - Ryan edits" is active, and none were rejected.

Push notification text that was sent:

> Ad spend: $152.23 this month · $0.00 today
> Static test campaign: $150.00 of $150 cap (cap reached) · today 0 views / 0 clicks / 0 leads
> 17 of 18 ads not active (paused or ad set paused); only "S8 One guy - Ryan edits" is ACTIVE. None rejected.
> Campaign https://www.facebook.com/adsmanager/manage/campaigns/edit?act=279018720625731&selected_campaign_ids=120272399628620362 · Dashboard https://claude.ai/artifact/7fJ9eHyo26xPPg9ZtKiqz2

---

## 3. The current ad (S8)

Here's your one active ad, **"S8 One guy - Ryan edits - main page."** It uses the Apply Now button.

- Open it in Ads Manager: https://www.facebook.com/adsmanager/manage/ads/edit?act=279018720625731&selected_ad_ids=120272631654970362
- The Facebook and Instagram preview links from that day expire, so open the ad in Ads Manager to see it.

This ad is still marked as running, but the campaign has used its full $150 cap, so it had no views today.

---

## 4. "More outrageous" ad drafts + the website line

I agree a bolder image is worth testing, but it may not be what's holding you back. All your ads together have spent about $150 and brought in 2 leads: one from S5c and one from S1. Your current ad, S8, is getting clicks at about the same rate as the others (3.5%), but it has 0 leads from only 399 views. People are clicking, so the bigger leak may be between the click and the application. Still, a sharper hook is a fair thing to test.

I made three drafts, all with your website line at the bottom:

- **A – Missed calls:** a phone lock screen showing 3 missed calls and "Never mind, we found someone." The headline is "You didn't lose that job. Your voicemail did." This is my pick: owners have lived that moment, so it stops the scroll without any hype.
- **B – One guy plus your guarantee:** "I'm one guy. If I miss, you get paid back." Below that is your 60-day booked-appointment promise. Please check that it matches the exact terms you'll honor.
- **C – Not more leads:** "More leads" crossed out, then "won't fix your business," with a line saying it's only for $150K+ companies.

I reworded your bottom line to "Don't trust me? Good. Look at unplannedco.com and see what I'm about." Starting with "Good" sounds confident. Starting with "If you don't trust me" can read like you expect them not to.

I haven't changed anything in Ads Manager. The campaign has also used its full $150, so a new ad won't show until you add budget. If you want, I can upload A as a new paused ad in that campaign so you can review it before it goes live.

### Exact text on each image

**A** (files: `ads/ad-a.png`)
- Lock screen: "2:07" / "Saturday"
- Notification 1: "Missed call (3)" / "Unknown · Katy, TX" / "now"
- Notification 2: "\"Never mind, we found someone.\"" / "New message" / "2m"
- Headline: "YOU DIDN'T LOSE THAT JOB. YOUR VOICEMAIL DID."
- Footer: "Don't trust me? Good. Look at unplannedco.com and see what I'm about."

**B** (`ads/ad-b.png`)
- Headline: "I'M ONE GUY. IF I MISS, YOU GET PAID BACK."
- Subtext: "Miss your booked-appointment target in 60 days? Your setup fee comes back."
- Stamp: "60-DAY TARGET"
- Footer: "Don't trust me? Good. Look at unplannedco.com and see what I'm about."

**C** (`ads/ad-c.png`)
- Headline: "~~MORE LEADS~~ WON'T FIX YOUR BUSINESS."
- Subtext: "You already pay for leads that never become jobs. I book the ones you're losing."
- Small: "Houston home-service companies, $150K+/yr only."
- Footer: "Don't trust me? Good. Look at unplannedco.com and see what I'm about."

---

## 5. Turning clicks into applications

Short answer: I wouldn't start with an animation or a new pop-up. The page has a bigger problem: it doesn't match the ad, and it makes you look like a web developer. Here's what I'm basing that on.

**What the numbers show:** across all your ads, about 70 people reached the page and 2 applied, so roughly 3% (my own math from the Meta numbers). Your "Unfinished applications" tab has never had a single row. That suggests most visitors never even open the form. If that tab saves anyone who starts and quits, then nobody has started. Either way, the problem looks like the page, not the form.

**What I found reading unplannedco.com** (my sandbox couldn't load your site directly, so this comes from a text read of the page):

1. **It doesn't continue the ad.** The ad says "I'm one guy, I answer at 2 AM." The page opens on a feature tour, 24 features, 27 demo sites and package options. Someone who clicked because of you never sees you.
2. **The demo sites push away the owners you want.** The demo sites include dental implants, med spa and hair salon. A roofer with 4 trucks sees a website shop, not a growth partner. Those demo links also send people off to the catalog site, and they rarely come back.
3. **There's no reason to trust you yet.** The page has no photo of you and no video. It also says outright that the names, reviews and numbers are samples. Your guarantees are strong, but they're buried at section 8 of 13.
4. **It's about 1,400 words with 12+ buttons.** The pop-up form already exists. A fancier one won't help if people never reach it.

**What I'd do, in order:**

1. **Build a short page just for this ad** (for example unplannedco.com/audit) and send ad traffic there instead of the main page:
   - The ad's headline at the top, so it reads as the same message.
   - A 45-second selfie video of you right under it. This is the "see what I'm about" you wanted on the ad, so put it where they land.
   - The 4 leaks, the guarantee and the "only $150K+" line.
   - One button: Apply.
2. **On the main page,** remove the dental, med-spa and salon demos and move the guarantees near the top.
3. **One small animation is fine,** like the missed-call notifications from ad A sliding in at the top so it feels like the same ad. That's polish, though. It won't fix the conversion problem.
4. **Make sure we can see where people drop off:** page view, form opened, then application sent. That way the next $150 tells us something.

None of this needs new claims you can't back up. You can't show real client results yet, so your face and the guarantee carry the trust.

---

## 6. The /audit page draft

I built the /audit page as a draft and pushed it to a new branch, `audit-landing-page`. Your live site hasn't changed.

A picture and an about-me section work well. I gave the page an **About me** section with a large round photo spot that shows "RB" until your photo is in. A video can go there later if you want one, but you don't need it.

The page, top to bottom:

- **Top:** "You didn't lose that job. Your voicemail did." Below it, a phone lock screen drops in three notifications: missed calls, a voicemail, then "Never mind, we found someone." It continues ad A, so people know they're in the right place.
- **About me:** "I'm one guy, not an agency." Then your line about only taking a few companies per trade, being texted directly and fixing things at 2 AM, with your photo card next to it.
- **The rest:** the 4 places jobs leak out, then 3 guarantees (setup fee back, live in 21 days, you own it). Then "Not for you yet if you're under $150k," and how it works.
- **Apply:** the same application pop-up as your main site, plus an apply bar that stays at the bottom on phones. There are no demo sites, catalog or 24-feature list.
- **Tracking:** new applications show "Audit page (ad)" as the source, so you can tell them apart. I also added an event for when someone scrolls down to the guarantees, so we can see how far people get.

I checked it on an iPhone-size screen: the animation plays and the application pop-up opens.

**What I need from you:**

1. **A photo** of you in work clothes, ideally at a job site or by a truck. A clear face shot is fine; a polished headshot isn't needed.
2. **Your about-me, in your own words:** 3–4 sentences on why you do this, what you did before, and why Houston. I wrote a draft from how you've described yourself, but it should be yours. Send me rough notes and I'll tighten them.

**Before it goes live:**

- I added "You text me directly, not a support inbox" to your card. Remove it if that's not how you want to work.
- The application still lists "Med spa" as a business type. I'd remove it for this ad.

Once you send the photo and about-me, I'll add them. Then it's ready to merge and point the new ad at unplannedco.com/audit.

### Where to plug things in (audit/index.html, in the `<head>` script)

```js
window.LEAD_SOURCE='Audit page (ad)';
window.RYAN_VIDEO='';   // optional: YouTube link or .mp4 URL
window.RYAN_PHOTO='';   // set to '/img/ryan.webp' once the photo is added
```

The about-me text is in the `<section aria-labelledby="meH">` block. Tracking events: Meta `PageView`, `StartApplication` (form opened), `ViewGuarantee` (new, scrolled to guarantees), `Lead` (application sent), `Schedule` (call booked).

### Exact page copy (top to bottom)

- Pill: "Houston · Home service companies doing $150k+ a year"
- H1: "You didn't lose that job. Your voicemail did."
- Sub: "I'm Ryan. I set up the fast replies, the follow-up and the tracking so the leads you already pay for turn into booked jobs. Then I stay and run it with you."
- Lock screen: "2:07 / Saturday" · "Missed call (3) — Unknown · Katy, TX — now" · "Voicemail — \"Hi, my AC is out, can someone…\" — 1m" · "\"Never mind, we found someone.\" — New message — 2m"
- Button: "Get my free 15-minute Growth Audit" · "About 2 minutes to apply. You keep the plan either way."
- Ticks: "Hit the target or your setup fee back" · "Only a few companies per trade per area" · "You own everything"
- About me: "I'm one guy, not an agency." / "That's the catch. It's also the point." / "I only take a few companies per trade in each part of Houston. You text me, not a ticket system. When something breaks at 2 AM on a Monday, I'm the one who fixes it." / "I don't just set it up and disappear. I run it, check it every week and show you one simple report: which leads came in, which got booked, and which ones slipped."
- Card: "Ryan Bernal · Founder, Unplanned & Co. · Houston, TX" · "You text me directly, not a support inbox" · "Your site, ad accounts and customer list stay yours" · "Audit first. You decide after."
- Leaks: "You don't need more leads first. You need to stop losing the ones you pay for." — 01 Calls you can't answer · 02 Leads nobody answers fast ("A form comes in at 9 PM. By 7 AM they already booked whoever called first.") · 03 Quotes nobody follows up ("You send the estimate, then nothing. The job goes to the company that called twice.") · 04 No idea what's working ("You pay for Google, Angi and Facebook, but can't say which one booked last Tuesday's job.")
- Guarantees: "I take the risk, so you don't have to." — Setup fee back · Live in 21 days ($100 off per day late) · You own it
- "Not for you yet if you're under $150k a year. Come back when you're there."
- How it works: "Audit first. Decide after." — Apply (2 minutes) · 15-minute Growth Audit · Live in 21 days
- Final section: "See where your next jobs are hiding." + "Start my application" + the sample audit card
- Phone sticky bar: "Get my free Growth Audit"
