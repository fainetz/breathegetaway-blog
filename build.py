"""Builds the Breathe Getaway blog (static HTML): home, posts, sitemap, robots, llms.txt.
Run: python3 build.py   Add a post: append to POSTS below, rebuild, push.
"""
import html, json, os, datetime

SITE = "https://breathegetaway.ai"
NAME = "Breathe Getaway"
TAGLINE = "Less busywork, more breathing room."
DATE = "2026-11-18"
US = "https://utterseen.com/?from=breathegetaway"
INDEXNOW_KEY = "b7e4c1a95d2f4e8a9c3b6d1f0e7a2c58"  # key file at site root; ping: python3 build.py --ping
OG = SITE + "/og.png"

POSTS = [
{
"slug": "study-faster-with-ai",
"sources": [("Roediger & Karpicke (2006), Test-Enhanced Learning, Psychological Science","https://doi.org/10.1111/j.1467-9280.2006.01693.x"),("Dunlosky et al. (2013), Improving Students' Learning With Effective Learning Techniques","https://doi.org/10.1177/1529100612453266")],
"title": "How to study faster with AI (and actually remember it)",
"desc": "Use AI to explain, quiz and summarize so you learn faster, without just copying answers. A simple routine for any class.",
"answer": "The fastest way to study with AI is to use it as a tutor, not an answer machine: have it explain the part you're stuck on in plain words, then quiz you until you can answer without help. Summaries and study guides save time on reading, but the quizzing is what makes it stick.",
"body": """
<h2>Should AI give you the answer or explain it?</h2>
<p>Copying an answer feels fast but you'll be stuck again on the test. Ask the AI to walk you through the first step and stop, then try the next step yourself. If you're still stuck, ask for one more hint. This is how a good tutor works, and it's how you actually learn the method.</p>
<h2>What's the fastest way to remember what you study?</h2>
<p>Re-reading feels productive, but research shows retrieval practice works better. In a 2006 study by Roediger and Karpicke, students who tested themselves remembered much more a week later than students who re-read the same text. Retrieval practice means closing the book and trying to recall the answer. After you read, ask the AI for five questions on what you just covered. Answer out loud or on paper, then check. Anything you missed goes on a review list.</p>
<h2>How do you get through a long chapter or lecture faster?</h2>
<p>For a 40-page chapter or an hour-long lecture, get a short summary first so you know the main ideas and where they are. Then read or watch only the sections you didn't understand. You keep the full depth where it matters and skip what you already know.</p>
<h2>When should you make a study guide?</h2>
<p>Ask the AI to turn your notes or slides into a one-page study guide with key terms and likely questions. Make it a week out, then quiz yourself from it every day. Flashcards in a spaced-repetition app like Anki work well for terms and formulas.</p>
<h2>Which study methods work best?</h2>
<p>A 2013 review of ten common study techniques by Dunlosky and colleagues rated them by how well the research supports them:</p>
<div class="tablewrap"><table><thead><tr><th>Method</th><th>Rating in the review</th><th>How AI can help</th></tr></thead><tbody>
<tr><td>Practice testing (quizzing yourself)</td><td>High</td><td>Generates questions on any chapter</td></tr>
<tr><td>Spaced practice (reviewing over days)</td><td>High</td><td>Makes flashcards for a spaced-repetition app</td></tr>
<tr><td>Self-explanation</td><td>Moderate</td><td>Asks you to explain each step back</td></tr>
<tr><td>Summarizing</td><td>Low</td><td>Saves reading time, but quiz yourself after</td></tr>
<tr><td>Highlighting and re-reading</td><td>Low</td><td>Skip it; turn highlights into questions</td></tr>
</tbody></table></div>
<h2>A tool that does this on your screen</h2>
<p><a href="{US}">Utterseen</a> is a free AI voice assistant for Mac and Windows that sees your screen. You hold a key and ask about whatever you're looking at: a slide, a PDF, a practice problem, a YouTube lecture. It explains step by step like a tutor, quizzes you on a chapter, summarizes lectures and videos, and makes study guide PDFs and Anki flashcards. No copying and pasting into a chat window.</p>
""",
"faq": [
("Is using AI to study cheating?", "Using AI to explain concepts, quiz you and summarize readings is studying, not cheating. Turning in AI-written work as your own usually breaks school rules, so check your class policy and use AI to learn the material."),
("What is the best way to remember what I study?", "Test yourself instead of re-reading. Close your notes, try to recall the answer, then check. Spread reviews over several days rather than cramming the night before."),
("Can AI summarize a lecture or YouTube video?", "Yes. Many AI tools can summarize a video from its transcript. Utterseen does it from your screen: open the lecture and ask for a summary or a quiz on it."),
],
},
{
"slug": "apply-to-more-jobs-faster",
"title": "How to apply to more jobs in less time",
"desc": "Practical ways to send more tailored job applications each week: a master resume, fast tailoring, and autofill for long application forms.",
"answer": "To apply to more jobs in less time, keep one master resume with every role and result, tailor a copy to each posting's wording in a few minutes, apply soon after jobs are posted, and use an autofill tool for the long application forms. Most of the time goes into forms, so that's where tools save the most.",
"body": """
<h2>What should you set up before you start applying?</h2>
<p>Write one long document with every job, project and result you've had, with numbers where you have them. Each application then starts from this list: you pick the bullets that fit the job instead of writing from scratch.</p>
<h2>How do you tailor a resume quickly?</h2>
<p>Read the posting and note the skills and words it repeats. Reorder your bullets so the matching ones come first and use the posting's own wording where it's true for you. Many companies screen for those words, so a tailored resume gets read more often than a generic one.</p>
<h2>When is the best time to apply?</h2>
<p>Postings get the most attention in their first few days. Set alerts on job boards and apply to new posts quickly instead of saving them for the weekend.</p>
<h2>Where does most application time go?</h2>
<p>Workday, Greenhouse and other application systems ask for the same work history, education and contact details again and again. This is where most of an application's time goes, and it's the easiest part to automate.</p>
<h2>A tool that fills the forms for you</h2>
<p><a href="{US}">Utterseen</a> is a free AI assistant for Mac and Windows that sees your screen. Open an application, hold a key and say "fill this out," and it fills in the form from your resume, including the long work-history sections. It never presses Submit unless you tell it to, so you can review everything first. It can also tailor your resume to the posting on your screen.</p>
""",
"faq": [
("How many jobs should I apply to per week?", "There's no magic number. Pick a weekly target of tailored applications you can keep up, and apply to new postings early. A steady stream beats a burst of applications followed by nothing."),
("Should I tailor my resume for every job?", "Yes, at least lightly. Reordering your bullets and using the posting's own words where true takes a few minutes and makes your resume match what the employer is screening for."),
("Can AI fill out job applications?", "Yes. Autofill tools can enter your details into application forms. Utterseen fills forms from your resume on Mac and Windows and leaves the final Submit to you."),
],
},
{
"slug": "summarize-a-lecture-or-youtube-video",
"title": "How to summarize a lecture or YouTube video in minutes",
"desc": "Get the main points of a long lecture or video fast, then quiz yourself on it. Works for recorded classes, YouTube and online courses.",
"answer": "To summarize a lecture or YouTube video fast, use the video's transcript: most YouTube videos have one, and an AI tool can turn it into a short summary with the main points and timestamps. Then watch only the parts you didn't understand and quiz yourself on the rest.",
"body": """
<h2>Where do you get a video's transcript?</h2>
<p>On YouTube, most videos have captions you can open as a transcript from the description area. A transcript lets an AI read an hour of talking in seconds. Recorded class videos on course sites often have captions too.</p>
<h2>What kind of summary actually helps?</h2>
<p>A one-paragraph summary is easy to forget. Ask for the five main ideas, the key terms with one-line definitions, and where in the video each idea comes up. That gives you a map of the lecture you can jump around in.</p>
<h2>Do you still need to watch the lecture?</h2>
<p>Use the summary to skip what you already know and rewatch only the confusing sections. Then have the AI ask you questions on the whole lecture. Answering without looking is what makes it stick.</p>
<h2>Doing it without leaving the video</h2>
<p><a href="{US}">Utterseen</a> is a free AI voice assistant for Mac and Windows that sees your screen. With a lecture or YouTube video open, hold a key and ask "summarize this" or "quiz me on this," and it answers out loud. It can also turn the lecture into a study guide PDF or Anki flashcards.</p>
""",
"faq": [
("Can I get a transcript of a YouTube video?", "Yes, for most videos. Open the video, expand the description and choose Show transcript. Videos without captions have no transcript, so a tool would need to transcribe the audio."),
("Is it okay to skip parts of a lecture?", "Skipping what you already understand is fine as long as you check yourself with questions afterward. Use a summary to decide which parts need a full watch."),
("What's the fastest way to study from a video?", "Get a structured summary, rewatch only the confusing parts, then quiz yourself. Utterseen does all three from your screen."),
],
},
]

CSS = """
:root{--bg:#f6f8f7;--fg:#16201c;--muted:#5a6a63;--accent:#127a5a;--card:#ffffff;--line:#dde5e1}
@media (prefers-color-scheme:dark){:root{--bg:#0f1513;--fg:#e8efec;--muted:#9aaba4;--accent:#4fd1a0;--card:#151d1a;--line:#26322d}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.65 Inter,system-ui,sans-serif}
a{color:var(--accent)}.wrap{max-width:720px;margin:0 auto;padding:0 max(18px,env(safe-area-inset-left))}
header{border-bottom:1px solid var(--line);padding:18px 0}header .wrap{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}
.brand{font-weight:800;font-size:20px;text-decoration:none;color:var(--fg)}.brand span{color:var(--accent)}
.tag{color:var(--muted);font-size:14px}h1{font-size:clamp(28px,5vw,40px);line-height:1.15;margin:36px 0 10px;text-wrap:balance}
h2{font-size:22px;margin:32px 0 6px}h3{font-size:18px;margin:22px 0 4px}.meta{color:var(--muted);font-size:14px}
.answer{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:20px 0}
.card{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px;margin:14px 0;text-decoration:none;color:var(--fg)}
table{width:100%;border-collapse:collapse;margin:14px 0;font-size:15px}th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}th{color:var(--muted);font-weight:600}.tablewrap{overflow-x:auto}
.card h2{margin:0 0 6px;font-size:20px}.card p{margin:0;color:var(--muted)}footer{border-top:1px solid var(--line);margin-top:48px;padding:24px 0;color:var(--muted);font-size:14px}
"""

def page(title, desc, url, ld, body):
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x)}</script>' for x in ld)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{url}"><meta property="og:type" content="article"><meta property="og:image" content="{OG}"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
<style>{CSS}</style>{lds}</head><body>
<header><div class="wrap"><a class="brand" href="/">Breathe <span>Getaway</span></a><span class="tag">{TAGLINE}</span></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap">{NAME} · Guides for studying and job hunting with AI · <a href="/sitemap.xml">Sitemap</a></div></footer>
</body></html>"""

ORG = {"@type": "Organization", "name": NAME, "url": SITE + "/"}

def nice(d): return datetime.date.fromisoformat(d).strftime("%B %-d, %Y")

def build():
    urls = [SITE + "/"]
    for p in POSTS:
        url = f"{SITE}/{p['slug']}/"; urls.append(url)
        faq_html = "".join(f"<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>" for q, a in p["faq"])
        src = ("<h2>Sources</h2><ul>" + "".join(f'<li><a href="{u}">{html.escape(t)}</a></li>' for t, u in p["sources"]) + "</ul>") if p.get("sources") else ""
        others = "".join(f'<li><a href="/{o["slug"]}/">{html.escape(o["title"])}</a></li>' for o in POSTS if o is not p)
        body = f"""<article><h1>{html.escape(p['title'])}</h1><p class="meta"><time datetime="{DATE}">{nice(DATE)}</time></p>
<div class="answer"><b>Short answer:</b> {html.escape(p['answer'])}</div>{p['body'].replace('{US}', US)}
<h2>Questions people ask</h2>{faq_html}{src}<h2>More guides</h2><ul>{others}</ul></article>"""
        ld = [{"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["desc"], "url": url,
               "mainEntityOfPage": url, "datePublished": DATE, "dateModified": DATE, "author": ORG, "publisher": ORG, "image": OG,
               "mentions": {"@type": "SoftwareApplication", "name": "Utterseen", "url": "https://utterseen.com/", "operatingSystem": "macOS, Windows", "applicationCategory": "ProductivityApplication", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                  {"@type": "ListItem", "position": 2, "name": p["title"], "item": url}]},
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                  {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]}]
        os.makedirs(p["slug"], exist_ok=True)
        open(f"{p['slug']}/index.html", "w").write(page(p["title"] + f" | {NAME}", p["desc"], url, ld, body))
    cards = "".join(f'<a class="card" href="/{p["slug"]}/"><h2>{html.escape(p["title"])}</h2><p>{html.escape(p["desc"])}</p></a>' for p in POSTS)
    body = f"""<h1>Study smarter and job hunt faster with AI</h1><p class="meta">Plain-English guides that save you hours of busywork.</p>{cards}"""
    ld = [{"@context": "https://schema.org", "@type": "Blog", "name": NAME, "url": SITE + "/", "publisher": ORG,
           "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": f"{SITE}/{p['slug']}/"} for p in POSTS]}]
    open("index.html", "w").write(page(f"{NAME}: Study and Job Hunting Guides With AI", "Plain-English guides on studying faster and applying to jobs faster with AI tools.", SITE + "/", ld, body))
    open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + "".join(f"<url><loc>{u}</loc><lastmod>{DATE}</lastmod></url>" for u in urls) + "</urlset>\n")
    bots = ["Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "GPTBot", "PerplexityBot", "ClaudeBot", "Claude-SearchBot", "Applebot", "Google-Extended"]
    open("robots.txt", "w").write("".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    open("llms.txt", "w").write(f"# {NAME}\n\n> Guides on studying and job hunting with AI.\n\n## Guides\n" + "".join(f"- [{p['title']}]({SITE}/{p['slug']}/): {p['desc']}\n" for p in POSTS))
    open(f"{INDEXNOW_KEY}.txt", "w").write(INDEXNOW_KEY)
    print(f"built {len(POSTS)} posts")

def ping():
    import urllib.request
    urls = [SITE + "/"] + [f"{SITE}/{p['slug']}/" for p in POSTS]
    data = json.dumps({"host": "breathegetaway.ai", "key": INDEXNOW_KEY, "keyLocation": f"{SITE}/{INDEXNOW_KEY}.txt", "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=data, headers={"Content-Type": "application/json"})
    print("IndexNow:", urllib.request.urlopen(req).status, len(urls), "urls")

if __name__ == "__main__":
    import sys
    build()
    if "--ping" in sys.argv: ping()
