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
{
"slug": "make-flashcards-with-ai",
"title": "How to make flashcards with AI (Anki and Quizlet)",
"desc": "Turn notes, slides or a textbook chapter into flashcards in minutes with AI, then review them with spaced repetition so they stick.",
"answer": "To make flashcards with AI, give it your notes, slides or a chapter and ask for one question and one short answer per fact, then import them into Anki or Quizlet. Keep each card to a single fact, and review with spaced repetition so you see hard cards more often.",
"body": """
<h2>What makes a good flashcard?</h2>
<p>One fact per card. "What does the mitochondria do?" with a one-line answer beats a card that asks you to recite a whole paragraph. Short cards are faster to review and show you exactly what you don't know yet.</p>
<h2>How do you get AI to write the cards?</h2>
<p>Paste in a section of your notes or a chapter and ask for flashcards in a two-column format: question, then answer. Ask it to skip anything trivial and to phrase questions the way your teacher would. Check the cards once; AI can get a detail wrong, and fixing a card takes seconds.</p>
<h2>How do you get them into Anki or Quizlet?</h2>
<p>Both apps import plain text. In Anki, use File, then Import, and pick a text file with the question and answer separated by a tab or comma. In Quizlet, create a set and use Import to paste the list. Anki's free desktop app schedules reviews with spaced repetition; newer versions also offer the FSRS scheduler.</p>
<h2>Why does spaced repetition work?</h2>
<p>Reviewing a fact right before you'd forget it makes the memory last longer each time. Research on the spacing effect, including a large 2006 review by Cepeda and colleagues, found that spreading study over days beats cramming the same total time into one session.</p>
<h2>Making cards from whatever's on your screen</h2>
<p><a href="{US}">Utterseen</a> is a free AI voice assistant for Mac and Windows that sees your screen. Open your slides, notes or a PDF chapter, hold a key and say "make Anki flashcards from this," and it builds the deck for you. It can also quiz you out loud on the same material.</p>
""",
"faq": [
("Can ChatGPT make Anki flashcards?", "Yes. Ask for question and answer pairs separated by a tab, save them as a text file, and import it into Anki. Check the cards for mistakes before you study them."),
("How many flashcards should I review a day?", "Let the app decide. With spaced repetition, Anki shows you the cards that are due, which is usually a manageable number if you add new cards steadily rather than all at once."),
("Is Anki better than Quizlet?", "Anki's free desktop app has stronger spaced repetition scheduling. Quizlet is easier to share and use on the go. Both import AI-made cards."),
],
"sources": [("Cepeda et al. (2006), Distributed practice in verbal recall tasks, Psychological Bulletin", "https://doi.org/10.1037/0033-2909.132.3.354"), ("Anki manual: importing", "https://docs.ankiweb.net/importing/intro.html")],
},
{
"slug": "how-to-study-for-finals",
"title": "How to study for finals in less time",
"desc": "A finals plan that works: start a week out, quiz yourself instead of re-reading, space your reviews, and sleep. With AI shortcuts for each step.",
"answer": "To study for finals efficiently, start about a week out, spend most of your time quizzing yourself on practice questions instead of re-reading, spread reviews across several days, and protect your sleep the night before. Use AI to make the practice questions and study guides so your time goes into recall.",
"body": """
<h2>When should you start studying for finals?</h2>
<p>About a week before each exam, in short daily sessions. Spreading the same hours over several days helps you remember more than one long cram session, which is one of the most consistent findings in learning research.</p>
<h2>What should you actually do in each session?</h2>
<p>Quiz yourself. Work old exams and practice problems, or have AI write questions from your notes, and answer them without looking. Mark what you miss and start the next session with those. Re-reading and highlighting feel productive but help much less.</p>
<h2>How do you cover a whole semester fast?</h2>
<p>Make a one-page study guide per unit: key terms, formulas and the kinds of questions your teacher asks. AI can draft it from your slides and notes in minutes, and you fix what's off. Then quiz from the guide every day.</p>
<h2>Does sleep really matter the night before?</h2>
<p>Yes. Sleep helps your brain hold onto what you studied, and an all-nighter makes recall slower on test day. A shorter review in the evening and a full night's sleep beats studying until 4 a.m.</p>
<h2>A study helper that sees your screen</h2>
<p><a href="{US}">Utterseen</a> is a free AI voice assistant for Mac and Windows. With your slides, notes or a practice exam open, hold a key and ask it to quiz you, explain a problem step by step, or make a study guide PDF. It works on whatever's on your screen, so there's no copying into a chat window.</p>
""",
"faq": [
("How many hours a day should I study for finals?", "There's no fixed number. Several focused sessions of 30 to 60 minutes with breaks, spread over a week, usually beat one long day of cramming."),
("Is it better to re-read notes or do practice problems?", "Practice problems. Testing yourself is one of the best-supported study methods; re-reading is one of the weakest."),
("Can AI make a study guide from my notes?", "Yes. Give it your notes or slides and ask for key terms, formulas and likely questions. Utterseen can turn whatever's on your screen into a study guide PDF."),
],
"sources": [("Dunlosky et al. (2013), Improving Students' Learning With Effective Learning Techniques", "https://doi.org/10.1177/1529100612453266"), ("Cepeda et al. (2006), Distributed practice in verbal recall tasks", "https://doi.org/10.1037/0033-2909.132.3.354")],
},
{
"slug": "write-a-cover-letter-fast",
"title": "How to write a cover letter fast (that still sounds like you)",
"desc": "A simple three-paragraph cover letter you can tailor in minutes, plus how to use AI without sounding generic.",
"answer": "To write a cover letter fast, use three short paragraphs: why this role at this company, two specific results from your past that match the job, and a one-line close. Keep it under a page, reuse the structure for every application, and only rewrite the parts that name the company and the matching results.",
"body": """
<h2>How long should a cover letter be?</h2>
<p>Under one page, usually three or four short paragraphs. Hiring managers skim. A tight letter that hits the job's main requirements gets read; a long one gets skipped.</p>
<h2>What goes in each paragraph?</h2>
<p><b>Opening:</b> the role you're applying for and one real reason you want it at this company. <b>Middle:</b> two results from your past that match what the posting asks for, with numbers if you have them. <b>Close:</b> a line saying you'd like to talk, and thanks.</p>
<h2>How do you tailor it quickly?</h2>
<p>Keep a base letter. For each job, swap in the company name, the role, one line about why that company, and the two results that best match the posting's top requirements. That's a few minutes per application instead of starting over.</p>
<h2>How do you use AI without sounding generic?</h2>
<p>Give the AI the job posting and your resume, and ask for a draft using your real results. Then cut anything you wouldn't say out loud, like "I am thrilled to apply" or "dynamic team player." Specific beats polished.</p>
<h2>Drafting it from the posting on your screen</h2>
<p><a href="{US}">Utterseen</a> is a free AI assistant for Mac and Windows that sees your screen. With a job posting open, hold a key and ask for a cover letter for this job; it drafts one from your resume and can paste it into the application form. It can also tailor your resume to the same posting and fill out the rest of the form.</p>
""",
"faq": [
("Do employers still read cover letters?", "Some do and some don't, and you usually can't tell which. A short, specific letter is worth sending when the application allows one, especially for roles you really want."),
("Is it okay to use AI to write a cover letter?", "Yes, as long as the facts are true and you edit it to sound like you. Remove generic phrases and make sure the results it mentions are your real ones."),
("Should I write a new cover letter for every job?", "Tailor it, don't rewrite it. Keep the structure and swap the company, role and the results that match each posting."),
],
},
{
"slug": "fill-out-workday-applications-faster",
"title": "How to fill out Workday job applications faster",
"desc": "Why Workday applications take so long, and practical ways to get through them faster: resume parsing, saved answers and autofill.",
"answer": "To get through Workday applications faster, upload your resume to let Workday prefill what it can, then fix the fields it gets wrong, keep a document of answers you reuse, and use an autofill tool for the work history and education sections. Each company has its own Workday site, so expect to make an account for each one.",
"body": """
<h2>Why do Workday applications take so long?</h2>
<p>Each company runs its own Workday site, so you usually create a separate account per employer. Then the form asks for your full work history, education and the same yes or no questions every time, often across five or more pages.</p>
<h2>Does uploading your resume help?</h2>
<p>Yes, partly. Workday offers to autofill from your resume, and it gets the basics like contact details mostly right. It often splits or mislabels jobs and dates, so check each entry before you move on.</p>
<h2>What should you keep ready?</h2>
<p>A document with your work history in clean blocks (title, company, dates, three bullets), your education, references, and answers to common questions like work authorization and salary expectations. Copying from one place is faster than retyping from memory.</p>
<h2>How do you avoid making a new password every time?</h2>
<p>Use a password manager. It saves each company's Workday login and fills it next time, which also helps when you need to check your application status.</p>
<h2>Filling the whole form for you</h2>
<p><a href="{US}">Utterseen</a> is a free AI assistant for Mac and Windows that sees your screen. Open a Workday application, hold a key and say "fill this out," and it fills the fields from your resume, including the long work history pages. It never presses Submit unless you tell it to, so you review everything first.</p>
""",
"faq": [
("Why does every company make me create a new Workday account?", "Each employer runs its own Workday site, and accounts don't carry over between companies. A password manager makes this much less painful."),
("Can you autofill Workday applications?", "Workday's own resume upload fills part of the form. Autofill tools like Utterseen can fill the rest from your resume, and you review before submitting."),
("How long does a Workday application take?", "Often 20 to 45 minutes by hand because of the long work history sections. Resume parsing plus autofill can cut that to a few minutes of checking."),
],
},
{
"slug": "tailor-resume-to-job-description",
"title": "How to tailor your resume to a job description in 10 minutes",
"desc": "A quick method to match your resume to each job posting so it gets past screening and in front of a person.",
"answer": "To tailor your resume quickly, find the five or six skills the posting repeats, move your bullets that prove those skills to the top of each job, use the posting's exact wording where it's true for you, and cut bullets that don't match. Start from a master resume so you're choosing bullets, not writing them.",
"body": """
<h2>What should you look for in the job posting?</h2>
<p>The skills, tools and phrases it repeats, especially in the requirements section. If it says "stakeholder communication" three times, that's a top priority for whoever reads your resume.</p>
<h2>What do you change on the resume?</h2>
<p>The order and wording of bullets, the skills section, and sometimes the summary line. Put the bullets that prove the posting's top skills first under each job. Use their words where they're true: if they say "customer success" and you wrote "client support," match them.</p>
<h2>What shouldn't you change?</h2>
<p>Your titles, dates and facts. Tailoring is choosing and wording what's true, not adding skills you don't have. Anything on the resume can come up in the interview.</p>
<h2>How does a master resume save time?</h2>
<p>Keep one long file with every job and every result you've had. Each tailored resume is a one-page selection from it, which takes minutes instead of an hour.</p>
<h2>Tailoring with the posting on your screen</h2>
<p><a href="{US}">Utterseen</a> is a free AI assistant for Mac and Windows that sees your screen. Open a job posting, hold a key and ask it to tailor your resume to this job; it picks and rewords your real bullets to match. It can then fill out the application form from the same resume.</p>
""",
"faq": [
("Do I really need to tailor my resume for every job?", "A light tailoring pass for each job is worth it. Reordering bullets and matching the posting's words takes minutes and makes your resume line up with what the employer screens for."),
("What are ATS keywords?", "They're the skills and terms from the job posting that applicant tracking systems and recruiters look for. Using the posting's own wording, where true, helps your resume match."),
("Can AI tailor my resume?", "Yes. Give it the job posting and your resume and ask it to reorder and reword your existing bullets. Check that every line is still true."),
],
}
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
