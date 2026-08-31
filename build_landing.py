import base64, os, io
from PIL import Image

logo_path = os.path.join(os.path.dirname(__file__), 'לוגו.png')
logo_b64 = base64.b64encode(open(logo_path, 'rb').read()).decode()
logo_src = f'data:image/png;base64,{logo_b64}'

# רק המגן — ללא הכיתוב שמתחת (חיתוך העליון + קיצוץ שוליים שקופים לצמוד)
_img = Image.open(logo_path).convert('RGBA')
_shield = _img.crop((0, 0, 455, 375))
_shield = _shield.crop(_shield.getbbox())
_buf = io.BytesIO()
_shield.save(_buf, format='PNG')
shield_src = f'data:image/png;base64,{base64.b64encode(_buf.getvalue()).decode()}'

# ── רשימת התוכנות — מקור אמת אחד לשמש ולרשת הפירוט ──
# rgb = צבע הדגשה מעודן לכל תוכנה ; svg = אייקון קו נקי
_SVG = {
 "hr":'<path d="M16 19v-1a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v1"/><circle cx="9" cy="7" r="3"/><path d="M22 19v-1a4 4 0 0 0-3-3.87"/><path d="M16 4.13a4 4 0 0 1 0 7.75"/>',
 "hours":'<path d="M5 2h9l5 5v15H5z"/><path d="M14 2v5h5"/><path d="M8 11h6M8 14h6"/><circle cx="11" cy="18" r="2"/>',
 "transport":'<rect x="4" y="3" width="16" height="14" rx="2"/><path d="M4 11h16"/><path d="M7 17v2M17 17v2"/><circle cx="8" cy="14" r=".6" fill="currentColor"/><circle cx="16" cy="14" r=".6" fill="currentColor"/>',
 "journal":'<path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/><path d="M4 17.5h13"/><path d="M9 7h6"/>',
 "fees":'<path d="M6 2h12v20l-3-2-3 2-3-2-3 2V2z"/><path d="M9 7h6M9 11h6M9 15h4"/>',
 "salary":'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M8 13h8M8 17h5"/>',
 "security":'<path d="M12 22s7.5-3.8 7.5-9.5V5.4L12 2.5 4.5 5.4v7.1C4.5 18.2 12 22 12 22z"/><path d="M8.8 12.2l2.2 2.2 4.2-4.4"/>',
 "mapping":'<path d="M9 3 3 5.5v15L9 18l6 3 6-2.5v-15L15 6z"/><path d="M9 3v15M15 6v15"/>',
 "nitzanim":'<path d="M12 22v-9.5"/><path d="M12 12.5c0-4 3.2-7.2 7.2-7.2 0 4-3.2 7.2-7.2 7.2z"/><path d="M12 16c0-2.9-2.3-5.2-5.2-5.2 0 2.9 2.3 5.2 5.2 5.2z"/>',
}
def _icon(k):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{_SVG[k]}</svg>'

PRODUCTS = [
    {"id":"hr",        "name":"שליטה מלאה על כוח אדם, תקציב וכלי ניהול — במקום אחד", "rgb":"198,160,75",  "live":True, "url":"hr.tpshk.org.il",
     "desc":'מערכת מתקדמת לניהול ובקרת מערך כוח האדם להבטחת התנהלות תקינה, שקופה ויעילה. המודול מספק תמונת מצב מדויקת בזמן אמת, תוך השוואה חכמה ורציפה בין התקן המאושר לבין האיוש בפועל — הן ברמת המוסד, התפקיד וחתך הזמן המבוקש. לצד זאת, המערכת מאפשרת בניית תקציב וניהול פיננסי חכם על בסיס "תקציב אפס", בסנכרון אוטומטי ומלא עם נתוני משרד החינוך העדכניים — לשליטה, שקיפות וביטחון בניהול משאבי האגף.'},
    {"id":"transport", "name":"בקרה ואופטימיזציה של תקציבי הסעות",          "rgb":"70,154,128",  "live":False,
     "desc":'פלטפורמה מקצה-לקצה לניהול מערך ההסעות ברשות: אופטימיזציה אוטומטית של מסלולים, בקרה בזמן אמת ושקיפות מלאה מול הספקים. הכל במקום אחד, בהתאמה לצרכי השלטון המקומי.<br>המערכת חוסכת עלויות, מקצרת זמני נסיעה ומייעלת את כל התהליך — מתכנון המסלול ועד לבקרה השוטפת.'},
    {"id":"hours",     "name":"מיצוי הכנסות, ניהול תקציב וניהול שעות ההוראה והמנהלה בתיכונים", "rgb":"124,104,168", "live":False, "url":"ay.tpshk.org.il",
     "desc":'התוכנה מספקת מענה כולל למוסד ולרשות ומבצעת באופן אוטומטי לחלוטין תקציב למוסד, ניהול מלא ואוטומטי של שעות ההוראה ועובדי המנהלה למול הניצול. השירותים מסופקים לעשרות רבות של מוסדות.'},
    {"id":"journal",   "name":"פקודת יומן אוטומטית",                       "rgb":"176,138,70",  "live":False, "url":"py.tpshk.org.il",
     "desc":'המערכת מבצעת קליטה אוטומטית ומהירה של תקציבי משרדי הממשלה, ודואגת לרישום מדויק וישיר שלהם בספרי התקציב של הרשות — תוך ייעול ומיכון תהליכים לחיסכון בזמן ומניעת טעויות.'},
    {"id":"fees",      "name":"אגרות חוץ - מענה מקיף",                     "rgb":"176,98,84",   "live":False, "url":"ag.tpshk.org.il",
     "desc":'מערך כלים רחב המסייע במיצוי זכויות ומשאבים לרשות הקולטת בשלל תחומים מורכבים: גני ילדים, ליווי בהסעות, שיבוץ סייעות ודירוגי ותק.'},
    {"id":"salary",    "name":"ביקורת שכר אוטומטית (עובדי הוראה)",         "rgb":"150,116,84",  "live":False,
     "desc":'אוטומציה חכמה לניהול ובקרת נתוני שכר בחינוך העל-יסודי. המערכת מבצעת סנכרון והצלבה מדויקת של שכר עובדי הוראה אל מול נתוני משרד החינוך.'},
    {"id":"security",  "name":"אבטחת מוסדות חינוך",                        "rgb":"168,96,132",  "live":False, "url":"am.tpshk.org.il",
     "desc":'בקרה פיננסית ומקסום הכנסות באבטחת מוסדות חינוך, על בסיס הצלבה מלאה בין התקן המאושר, השעות המדווחות והחשבוניות בפועל. המערכת קוראת אוטומטית את קבצי המערכות הארציות, החשבוניות ודוחות הנוכחות, ומעניקה למקבלי ההחלטות איתור מיידי של פערים, השלכה תקציבית בשקלים ושליטה מלאה מול חברות האבטחה.'},
    {"id":"mapping",   "name":"בדיקת מיפוי חינוך מיוחד",                     "rgb":"110,146,92",  "live":False,
     "desc":'בקרה ומיצוי תקציב מלא של מערך החינוך המיוחד ברשות, על בסיס הצלבה אוטומטית בין דוח המשבצת, מצבות התלמידים בגנים ובבתי הספר, קובץ המוכרים והקצאת הסייעות. המערכת מאתרת פערי הקצאה בקודים 160 ו-172, בסייעות הכיתתיות ובימי החופשות בשני המגזרים, ומפיקה קבצים מוכנים להגשה למשרד החינוך.'},
    {"id":"nitzanim", "name":"בקרת תכנית ניצנים",                          "rgb":"108,118,180", "live":False, "url":"nz.tpshk.org.il",
     "desc":'בקרה תקציבית ותפעולית מלאה על תכנית "ניצנים" ברשות המקומית. המערכת מושכת אוטומטית את נתוני התקצוב העדכניים ממית"ר ומצליבה אותם מול דיווחי הביצוע החודשיים, מאתרת פערים וטעויות דיווח, ומפיקה דוחות חלוקה למפעילים ולמוסדות לצד צפי תקציב שנתי — שליטה מלאה בכל שקל של התכנית.'},
]
for _p in PRODUCTS:
    _p["icon"] = _icon(_p["id"])

# מיקומי השמש [x%, y%] — 9 נקודות על אליפסה סביב הלוגו, מרווחים שווים (כל 40°)
NODE_POS = [
    [50, 19],  # כח אדם ותקציב (ארוך) — מרכז, עליון
    [70, 26],  # הסעות (ארוך)        — ימין, עליון
    [80, 45],  # שעות הוראה          — ימין, אמצע
    [77, 66],  # פקודת יומן          — ימין, תחתון
    [61, 80],  # אגרות חוץ           — מרכז-ימין, תחתון
    [39, 80],  # שכר הוראה           — מרכז-שמאל, תחתון
    [23, 66],  # אבטחת מוסדות חינוך  — שמאל, תחתון
    [20, 45],  # מיפוי חנ״מ          — שמאל, אמצע
    [30, 26],  # בקרת תכנית ניצנים   — שמאל, עליון
]

# מיקומי טבעת ייעודיים לפלאפון — אובל אנכי סימטרי סביב הלוגו (9 נקודות כל 40°)
MOBILE_NODE_POS = [
    [50, 12],  # למעלה
    [72, 21],  # עליון-ימין
    [84, 43],  # ימין עליון
    [80, 69],  # ימין תחתון
    [62, 86],  # תחתון-ימין
    [38, 86],  # תחתון-שמאל
    [20, 69],  # שמאל תחתון
    [16, 43],  # שמאל עליון
    [28, 21],  # עליון-שמאל
]

# תוויות קצרות לריבועי השמש בפלאפון (השם המלא נשאר ברשת המוצרים)
NODE_SHORT = [
    "כח אדם ותקציב", "הסעות", "שעות הוראה",
    "פקודת יומן", "אגרות חוץ", "שכר הוראה",
    "אבטחת מוסדות", "מיפוי חנ״מ", "ניצנים",
]

# בניית נודות השמש (אייקון + שם בלבד)
nodes_html = ""
for i, p in enumerate(PRODUCTS):
    cls = "live" if p["live"] else "soon"
    status = "זמין עכשיו" if p["live"] else "בפיתוח"
    nodes_html += f'''    <div class="pnode {cls}" id="pn{i}" data-target="card-{p['id']}" data-rgb="{p['rgb']}">
      <button type="button" class="pnode-card" aria-label="{p['name']} — {status}. מעבר לפירוט התוכנה">
        <span class="pnode-icon" style="background:rgba({p['rgb']},.16);color:rgb({p['rgb']})" aria-hidden="true">{p['icon']}</span>
        <span class="pnode-name">{p['name']}</span>
        <span class="pnode-name-sm" aria-hidden="true">{NODE_SHORT[i]}</span>
      </button>
    </div>
'''

# בניית רשת הפירוט (כל התוכנות גלויות) — בלי תגיות/קישורים בשלב זה
grid_html = ""
for p in PRODUCTS:
    live_cls = " live" if p["live"] else ""
    # אייקון: מגן החברה לתוכנה שסומנה shield, אחרת אייקון הקו הרגיל
    if p.get("shield"):
        icon_html = '<div class="prod-icon prod-icon-shield"><img src="__SHIELD__" alt="סמל המגן של ד.ר שחקים בע&quot;מ"></div>'
    else:
        icon_html = f'<div class="prod-icon" style="background:rgba({p["rgb"]},.15);color:rgb({p["rgb"]})" aria-hidden="true">{p["icon"]}</div>'
    # קישור לתוכנה החיה באינטרנט — מוצג בסוף הריבוע
    link_html = ''
    if p.get("url"):
        link_html = (f'\n        <a href="https://{p["url"]}" class="prod-link" target="_blank" rel="noopener" '
                     f'aria-label="מעבר לתוכנה {p["name"]} בכתובת {p["url"]} (נפתח בחלון חדש)">'
                     f'<span aria-hidden="true">🌐</span> {p["url"]}</a>')
    grid_html += f'''      <article class="prod-card{live_cls}" id="card-{p['id']}" style="--clr:{p['rgb']}">
        {icon_html}
        <h3 class="prod-name">{p['name']}</h3>
        <p class="prod-desc">{p['desc']}</p>{link_html}
      </article>
'''

# POS ל-JS
pos_js = "[" + ",".join(f"[{x},{y}]" for x, y in NODE_POS) + "]"
mpos_js = "[" + ",".join(f"[{x},{y}]" for x, y in MOBILE_NODE_POS) + "]"

page = r"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ד.ר שחקים בע"מ | Technology Platform</title>
<link rel="icon" type="image/png" href="__SHIELD__">
<link rel="apple-touch-icon" href="__SHIELD__">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@500;700;800;900&family=Rubik:wght@400;500;700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --navy:#294368;
  --navy2:#1E3356;
  --gold:#C8A951;
  --gold2:#E8D48A;
  --white:#FFFFFF;
  --off:#F7F6F2;
  --ink:#1A1A2E;
  --muted:#6B7A94;
  --brd:#E2E0D8;
}

/* טקסט לקוראי מסך בלבד */
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;
  clip:rect(0,0,0,0);white-space:nowrap;border:0}

/* ── נגישות: דילוג לתוכן + מיקוד מקלדת נראה לעין ── */
.skip-link{
  position:absolute;top:-60px;right:12px;z-index:200;
  background:var(--navy);color:#fff;padding:10px 18px;border-radius:0 0 8px 8px;
  font-size:.9rem;font-weight:700;text-decoration:none;transition:top .2s;
}
.skip-link:focus{top:0}
a:focus-visible,button:focus-visible,input:focus-visible,textarea:focus-visible,
[tabindex]:focus-visible,summary:focus-visible{
  outline:3px solid #B8860B;outline-offset:3px;border-radius:4px;
}
.hub-section a:focus-visible,.hub-section [tabindex]:focus-visible,
.contact a:focus-visible,footer a:focus-visible,.topbar a:focus-visible{
  outline-color:#F0D98A;
}
html{scroll-behavior:smooth}
body{font-family:'Segoe UI',Arial,sans-serif;color:var(--ink);background:var(--white);direction:rtl;overflow-x:hidden}

/* ── רכיב נגישות צף ── */
.a11y-btn{
  position:fixed;bottom:20px;right:20px;z-index:150;
  width:54px;height:54px;border-radius:50%;border:none;
  background:var(--navy);color:#fff;cursor:pointer;
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 6px 22px rgba(41,67,104,.4);
  transition:transform .2s,background .2s;
}
.a11y-btn:hover{background:var(--navy2);transform:scale(1.08)}
.a11y-btn svg{width:28px;height:28px}
.a11y-panel{
  position:fixed;bottom:86px;right:20px;z-index:150;
  width:290px;max-width:calc(100vw - 40px);
  background:#fff;border:1.5px solid var(--brd);border-radius:16px;
  box-shadow:0 20px 60px rgba(41,67,104,.26);
  padding:18px;display:none;flex-direction:column;gap:8px;
}
.a11y-panel[data-open="1"]{display:flex}
.a11y-panel h2{font-size:1rem;font-weight:800;color:var(--navy);margin-bottom:6px}
.a11y-opt{
  display:flex;align-items:center;gap:10px;width:100%;
  padding:10px 12px;border:1.5px solid var(--brd);border-radius:10px;
  background:#fff;color:var(--ink);font-family:inherit;font-size:.87rem;font-weight:600;
  cursor:pointer;text-align:right;transition:all .18s;
}
.a11y-opt:hover{border-color:var(--navy);background:#F4F6FA}
.a11y-opt[aria-pressed="true"]{background:var(--navy);color:#fff;border-color:var(--navy)}
.a11y-opt span[aria-hidden]{font-size:1.05rem;min-width:22px}
.a11y-reset{margin-top:4px;background:none;border:none;color:var(--muted);font-family:inherit;
  font-size:.8rem;text-decoration:underline;cursor:pointer;padding:6px}
.a11y-links{display:flex;flex-direction:column;gap:4px;margin-top:8px;padding-top:12px;border-top:1px solid var(--brd)}
.a11y-links button{background:none;border:none;color:var(--navy);font-family:inherit;font-size:.82rem;
  font-weight:600;text-decoration:underline;cursor:pointer;text-align:right;padding:4px}

/* מצבי נגישות פעילים — נשמרים ב-localStorage */
html[data-a11y-font="1"]{font-size:112.5%}
html[data-a11y-font="2"]{font-size:125%}
html[data-a11y-font="3"]{font-size:140%}
html[data-a11y-contrast="1"] body{background:#000;color:#fff}
html[data-a11y-contrast="1"] .hero-headline,
html[data-a11y-contrast="1"] .hero-body,
html[data-a11y-contrast="1"] .products,
html[data-a11y-contrast="1"] .about,
html[data-a11y-contrast="1"] .hero-top,
html[data-a11y-contrast="1"] .contact,
html[data-a11y-contrast="1"] .hub-section,
html[data-a11y-contrast="1"] footer,
html[data-a11y-contrast="1"] .topbar,
html[data-a11y-contrast="1"] nav{background:#000!important}
html[data-a11y-contrast="1"] .prod-card,
html[data-a11y-contrast="1"] .why-card,
html[data-a11y-contrast="1"] .contact-right,
html[data-a11y-contrast="1"] .pnode-card,
html[data-a11y-contrast="1"] .a11y-panel,
html[data-a11y-contrast="1"] .modal-box,
html[data-a11y-contrast="1"] .cookie-bar{background:#000!important;border-color:#FFD700!important}
html[data-a11y-contrast="1"] h1,html[data-a11y-contrast="1"] h2,
html[data-a11y-contrast="1"] h3,html[data-a11y-contrast="1"] .products-title,
html[data-a11y-contrast="1"] .prod-name,html[data-a11y-contrast="1"] .tech-platform,
html[data-a11y-contrast="1"] .contact-left h2{
  color:#FFD700!important;-webkit-text-fill-color:#FFD700!important;background:none!important;
}
html[data-a11y-contrast="1"] p,html[data-a11y-contrast="1"] .prod-desc,
html[data-a11y-contrast="1"] .about-sub,html[data-a11y-contrast="1"] .hero-sub,
html[data-a11y-contrast="1"] .footer-txt,html[data-a11y-contrast="1"] .why-card p,
html[data-a11y-contrast="1"] .cdet-inline,html[data-a11y-contrast="1"] li,
html[data-a11y-contrast="1"] .modal-box li,html[data-a11y-contrast="1"] label{color:#fff!important}
html[data-a11y-contrast="1"] a,html[data-a11y-contrast="1"] .nav-links a,
html[data-a11y-contrast="1"] .prod-link{color:#FFD700!important}
html[data-a11y-contrast="1"] .btn-navy,html[data-a11y-contrast="1"] .nav-cta,
html[data-a11y-contrast="1"] .cf-submit,html[data-a11y-contrast="1"] .btn-gold,
html[data-a11y-contrast="1"] .a11y-btn{background:#FFD700!important;color:#000!important}
html[data-a11y-contrast="1"] input,html[data-a11y-contrast="1"] textarea{
  background:#000!important;color:#fff!important;border-color:#FFD700!important}
html[data-a11y-contrast="1"] .hub-section::before,
html[data-a11y-contrast="1"] .hub-section::after{display:none}

/* הדגשת קישורים */
html[data-a11y-links="1"] a{text-decoration:underline!important;text-underline-offset:3px;
  text-decoration-thickness:2px!important;font-weight:700!important}
html[data-a11y-links="1"] .prod-card,html[data-a11y-links="1"] .pnode-card{outline:2px dashed rgba(200,169,81,.7)}

/* עצירת אנימציות — גם לפי בחירת המשתמש וגם לפי הגדרת מערכת ההפעלה */
html[data-a11y-motion="1"] *,html[data-a11y-motion="1"] *::before,html[data-a11y-motion="1"] *::after{
  animation:none!important;transition:none!important;scroll-behavior:auto!important;
}
@media(prefers-reduced-motion:reduce){
  *,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}
}

/* ── מודאלים: הצהרת נגישות + מדיניות פרטיות ── */
.modal{
  position:fixed;inset:0;z-index:180;
  background:rgba(15,22,38,.72);
  display:none;align-items:flex-start;justify-content:center;
  padding:5vh 4%;overflow-y:auto;
}
.modal[data-open="1"]{display:flex}
.modal-box{
  background:#fff;border-radius:20px;max-width:760px;width:100%;
  padding:38px 40px 34px;position:relative;
  box-shadow:0 40px 90px rgba(0,0,0,.4);
}
.modal-box h2{font-size:1.5rem;font-weight:900;color:var(--navy);margin-bottom:6px}
.modal-box h3{font-size:1rem;font-weight:800;color:var(--navy);margin:22px 0 8px}
.modal-box p,.modal-box li{font-size:.9rem;color:#3D4A5E;line-height:1.8}
.modal-box ul{padding-right:22px;margin:6px 0}
.modal-box li{margin-bottom:5px}
.modal-updated{font-size:.76rem;color:var(--muted);margin-bottom:4px}
.modal-close{
  position:absolute;top:16px;left:18px;
  width:38px;height:38px;border-radius:50%;border:1.5px solid var(--brd);
  background:#fff;color:var(--navy);font-size:1.2rem;cursor:pointer;line-height:1;
}
.modal-close:hover{background:var(--navy);color:#fff;border-color:var(--navy)}
.modal-contact{background:#F4F6FA;border-right:4px solid var(--gold);border-radius:10px;padding:16px 18px;margin-top:10px}
@media(max-width:560px){.modal-box{padding:34px 22px 26px}.modal-box h2{font-size:1.25rem}}

/* ── באנר עוגיות ── */
.cookie-bar{
  position:fixed;bottom:0;right:0;left:0;z-index:170;
  background:#fff;border-top:2px solid var(--gold);
  box-shadow:0 -8px 34px rgba(41,67,104,.18);
  padding:18px 5%;display:none;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap;
}
.cookie-bar[data-open="1"]{display:flex}
.cookie-bar p{font-size:.86rem;color:#3D4A5E;line-height:1.65;max-width:620px;margin:0}
.cookie-bar button{font-family:inherit;font-size:.85rem;font-weight:700;cursor:pointer;
  padding:10px 22px;border-radius:9px;border:none;white-space:nowrap}
.cookie-accept{background:var(--navy);color:#fff}
.cookie-accept:hover{background:var(--navy2)}
.cookie-reject{background:#fff;color:var(--navy);border:1.5px solid var(--brd)!important}
.cookie-reject:hover{border-color:var(--navy)!important}
.cookie-more{background:none;color:var(--navy);text-decoration:underline;padding:10px 6px!important}
.cookie-actions{display:flex;gap:10px;align-items:center;flex-wrap:wrap}

/* ── צ'קבוקס הסכמה בטופס ── */
.consent-row{display:flex;align-items:flex-start;gap:9px;margin-top:2px}
.consent-row input[type=checkbox]{
  width:19px;height:19px;min-width:19px;margin-top:2px;
  accent-color:var(--navy);cursor:pointer;
}
.consent-row label{font-size:.82rem;color:#3D4A5E;line-height:1.6;cursor:pointer}
.consent-row label button{background:none;border:none;padding:0;color:var(--navy);
  font-family:inherit;font-size:.82rem;font-weight:700;text-decoration:underline;cursor:pointer}
.form-note{font-size:.76rem;color:var(--muted);line-height:1.6;margin-top:2px}

/* TOP BAR */
.topbar{
  position:fixed;top:0;right:0;left:0;z-index:101;
  background:var(--navy2);
  color:rgba(255,255,255,.65);
  font-size:.58rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;
  text-align:center;padding:7px 5%;
  height:30px;display:flex;align-items:center;justify-content:center;gap:14px;
}
.topbar-dot{width:3px;height:3px;background:var(--gold);border-radius:50%;opacity:.7}

/* NAV */
nav{
  position:fixed;top:30px;right:0;left:0;z-index:100;
  background:rgba(255,255,255,.96);backdrop-filter:blur(14px);
  border-bottom:1px solid var(--brd);
  padding:0 5%;display:flex;align-items:center;justify-content:space-between;height:92px;
}
.nav-brand{display:flex;align-items:center;gap:12px;text-decoration:none;cursor:pointer}
.nav-brand img{height:66px;width:auto}
.nav-brand-name{font-size:.92rem;font-weight:700;color:var(--navy)}
.nav-brand-sub{font-size:.58rem;font-weight:700;color:var(--gold);letter-spacing:.08em}
.nav-links{display:flex;gap:28px;list-style:none;position:absolute;left:50%;transform:translateX(-50%)}
.nav-links a{text-decoration:none;color:var(--muted);font-size:.87rem;transition:color .2s}
.nav-links a:hover{color:var(--navy)}
.nav-cta{background:var(--navy);color:#fff;padding:9px 22px;border-radius:8px;font-size:.84rem;font-weight:600;text-decoration:none;transition:all .2s}
.nav-cta:hover{background:var(--navy2);transform:translateY(-1px)}
.nav-login{border:1.5px solid var(--navy);color:var(--navy);padding:8px 18px;border-radius:8px;font-size:.84rem;font-weight:600;text-decoration:none;transition:all .2s;display:flex;align-items:center;gap:6px}
.nav-login:hover{background:var(--navy);color:#fff}

/* Sun node icon (color set inline per product) */
.pnode-icon{border-radius:12px;padding:9px;display:inline-flex;align-items:center;justify-content:center;margin-bottom:2px}
.pnode-icon svg{width:clamp(22px,2vw,27px);height:clamp(22px,2vw,27px)}

/* ── ABOVE-FOLD: hero text + hub, full viewport ── */
.above-fold{
  min-height:calc(100vh - 94px);
  margin-top:94px;
  display:flex;flex-direction:column;
}

/* TECH PLATFORM — above hub */
.hero-top{
  background:var(--white);
  padding:22px 6% 18px;
  text-align:center;
  flex:0 0 auto;
}
.tech-platform{
  font-size:clamp(1rem,1.6vw,1.35rem);
  font-weight:800;letter-spacing:.28em;text-transform:uppercase;
  color:var(--navy);
  display:inline-flex;align-items:center;gap:14px;
}
.tech-platform .tp-dot{
  width:6px;height:6px;border-radius:50%;
  background:linear-gradient(135deg,var(--gold),var(--gold2));
  flex-shrink:0;
}

/* HEADLINE — below the fold */
.hero-headline{
  background:var(--white);
  padding:56px 6% 40px;
  text-align:center;
}
.hero-headline h1{
  font-size:clamp(2rem,3.8vw,3.4rem);
  font-weight:900;line-height:1.1;margin-bottom:0;
  background:linear-gradient(to right,#E8D48A 0%,#C8A951 20%,#4a6898 55%,#1E3356 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}

/* HERO BODY — subtitle + chips + CTA */
.hero-body{
  background:var(--white);
  padding:20px 6% 52px;
  text-align:center;
}
.hero-sub{font-size:.98rem;color:var(--muted);line-height:1.75;margin-bottom:22px;max-width:560px;margin-left:auto;margin-right:auto}
.tech-row{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-bottom:32px}
.tech-chip{font-size:.6rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:4px 11px;border-radius:100px;background:rgba(41,67,104,.06);color:var(--navy);border:1px solid rgba(41,67,104,.12)}
.hero-actions{display:flex;gap:12px;flex-wrap:wrap;justify-content:center}
.btn-navy{background:var(--navy);color:#fff;padding:13px 30px;border-radius:9px;font-size:.9rem;font-weight:700;text-decoration:none;box-shadow:0 4px 20px rgba(41,67,104,.3);transition:all .22s}
.btn-navy:hover{background:var(--navy2);transform:translateY(-2px);box-shadow:0 8px 28px rgba(41,67,104,.4)}
.btn-out{color:var(--navy);padding:13px 26px;border-radius:9px;font-size:.9rem;font-weight:600;text-decoration:none;border:2px solid rgba(41,67,104,.18);transition:all .22s}
.btn-out:hover{border-color:var(--navy);background:rgba(41,67,104,.04)}

/* HUB — fills remaining viewport between tech-platform and headline */
.hub-section{
  flex:1;
  min-height:260px;
  background:linear-gradient(170deg,#1E3356 0%,#253f6a 50%,#2a4570 100%);
  position:relative;overflow:hidden;
}
/* dot texture */
.hub-section::after{
  content:'';position:absolute;inset:0;
  background-image:radial-gradient(rgba(255,255,255,.05) 1px, transparent 1px);
  background-size:30px 30px;pointer-events:none;z-index:0;
}
/* ambient glows */
.hub-section::before{
  content:'';position:absolute;inset:0;
  background:
    radial-gradient(ellipse 45% 60% at 22% 80%, rgba(200,169,81,.07) 0%, transparent 70%),
    radial-gradient(ellipse 40% 55% at 78% 20%, rgba(200,169,81,.06) 0%, transparent 70%),
    radial-gradient(ellipse 30% 40% at 50% 50%, rgba(41,67,104,.0) 0%, transparent 60%);
  pointer-events:none;z-index:0;
}

.hub-canvas{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:1;overflow:visible}

/* Center orb — full logo on a light medallion */
.hub-orb{
  position:absolute;top:50%;left:50%;
  transform:translate(-50%,-50%);
  width:188px;height:188px;border-radius:50%;
  background:linear-gradient(145deg,#2a4570,#1E3356);
  display:flex;align-items:center;justify-content:center;
  box-shadow:
    0 0 0 1px rgba(200,169,81,.55),
    0 0 0 12px rgba(200,169,81,.06),
    0 0 0 28px rgba(200,169,81,.03),
    0 0 90px rgba(200,169,81,.20),
    0 18px 56px rgba(0,0,0,.4);
  z-index:4;
}
.hub-orb img{width:auto;height:140px;display:block}

/* pulse rings */
.orb-pulse{
  position:absolute;top:50%;left:50%;
  width:188px;height:188px;border-radius:50%;
  border:1px solid rgba(200,169,81,.28);
  opacity:0;pointer-events:none;z-index:3;
  animation:orbPulse 3.8s ease-out infinite;
  transform:translate(-50%,-50%);
}
.orb-pulse:nth-child(2){animation-delay:1.3s}
.orb-pulse:nth-child(3){animation-delay:2.6s}
@keyframes orbPulse{
  0%{transform:translate(-50%,-50%) scale(1);opacity:.45}
  100%{transform:translate(-50%,-50%) scale(3.2);opacity:0}
}

/* Product node cards */
.pnode{position:absolute;z-index:5;transform:translate(-50%,-50%)}
.pnode-card{
  font:inherit;color:inherit;
  background:rgba(255,255,255,.07);
  border:1px solid rgba(255,255,255,.14);
  border-radius:14px;padding:12px 13px 11px;
  width:clamp(140px,12vw,178px);
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;
  text-align:center;cursor:pointer;
  backdrop-filter:blur(10px);
  transition:all .28s cubic-bezier(.34,1.5,.64,1);
}
.pnode.live .pnode-card{border-color:rgba(200,169,81,.5);box-shadow:0 4px 20px rgba(0,0,0,.22)}
.pnode .pnode-card:hover{
  background:rgba(255,255,255,.14);border-color:var(--gold);
  transform:translateY(-6px) scale(1.05);
  box-shadow:0 16px 44px rgba(0,0,0,.3),0 0 22px rgba(200,169,81,.22);
}
.pnode.soon .pnode-card{opacity:.82}
.pnode.soon .pnode-card:hover{opacity:1}
.pnode-name{font-family:'Rubik',sans-serif;font-size:clamp(.78rem,.95vw,.92rem);font-weight:400;color:#fff;line-height:1.3}
.pnode-name-sm{display:none;font-family:'Rubik',sans-serif;font-weight:400;color:#fff;line-height:1.25}
.pnode-icon{display:inline-flex}

/* pulsing ring on live card */
.pnode.live::before{
  content:'';
  position:absolute;
  inset:-6px;border-radius:18px;
  border:1.5px solid rgba(200,169,81,.4);
  animation:ringPulse 2.4s ease-in-out infinite;
  pointer-events:none;z-index:-1;
}
@keyframes ringPulse{
  0%,100%{opacity:.5;transform:scale(1)}
  50%{opacity:1;transform:scale(1.03)}
}
.pnode.live.active::before{opacity:0!important}

/* floating animations — each node unique */
.pnode.live{animation:f0 4.4s ease-in-out infinite}
#pn1{animation:f1 5.2s ease-in-out infinite .5s}
#pn2{animation:f2 4.8s ease-in-out infinite 1s}
#pn3{animation:f3 5.6s ease-in-out infinite .2s}
#pn4{animation:f4 4.2s ease-in-out infinite .8s}
#pn5{animation:f5 6s ease-in-out infinite 1.4s}
@keyframes f0{0%,100%{transform:translate(-50%,-50%) translateY(0px)}50%{transform:translate(-50%,-50%) translateY(-8px)}}
@keyframes f1{0%,100%{transform:translate(-50%,-50%) translateY(0px)}50%{transform:translate(-50%,-50%) translateY(-5px)}}
@keyframes f2{0%,100%{transform:translate(-50%,-50%) translateY(0px)}50%{transform:translate(-50%,-50%) translateY(-10px)}}
@keyframes f3{0%,100%{transform:translate(-50%,-50%) translateY(0px)}50%{transform:translate(-50%,-50%) translateY(-4px)}}
@keyframes f4{0%,100%{transform:translate(-50%,-50%) translateY(0px)}50%{transform:translate(-50%,-50%) translateY(-7px)}}
@keyframes f5{0%,100%{transform:translate(-50%,-50%) translateY(0px)}50%{transform:translate(-50%,-50%) translateY(-11px)}}

/* PRODUCTS GRID */
.btn-gold{display:inline-block;background:var(--gold);color:var(--navy);padding:11px 26px;border-radius:9px;font-size:.84rem;font-weight:700;text-decoration:none;transition:all .2s}
.btn-gold:hover{background:var(--gold2);transform:translateY(-2px)}
.products{padding:84px 5% 88px;background:linear-gradient(180deg,var(--off) 0%,#fff 100%);text-align:center}
.products-head{margin-bottom:40px}
.products-title{font-size:clamp(2rem,3.4vw,2.8rem);font-weight:900;color:var(--navy);margin-bottom:18px;letter-spacing:-.01em}
.products-title .pt-gold{
  background:linear-gradient(120deg,#C8A951,#E8D48A,#C8A951);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.pt-rule{display:flex;align-items:center;justify-content:center;gap:10px;margin-bottom:16px}
.pt-rule::before,.pt-rule::after{content:'';width:54px;height:2px;background:linear-gradient(90deg,transparent,var(--gold))}
.pt-rule::after{background:linear-gradient(90deg,var(--gold),transparent)}
.pt-rule span{width:7px;height:7px;border-radius:50%;background:var(--gold);box-shadow:0 0 0 4px rgba(200,169,81,.14)}
.products-sub{font-size:1.06rem;font-weight:500;color:var(--navy);opacity:.78;max-width:520px;margin:0 auto;line-height:1.7;letter-spacing:.01em}
.prod-grid{
  display:grid;grid-template-columns:repeat(3,1fr);gap:22px;
  max-width:1180px;margin:0 auto;
}
.prod-card{
  position:relative;
  background:#fff;border:1.5px solid var(--brd);border-radius:20px;
  padding:30px 24px 26px;text-align:center;
  display:flex;flex-direction:column;align-items:center;
  box-shadow:0 8px 30px rgba(41,67,104,.05);
  transition:transform .28s cubic-bezier(.34,1.3,.64,1),box-shadow .28s,border-color .28s;
}
.prod-card:hover{transform:translateY(-6px);box-shadow:0 20px 50px rgba(41,67,104,.13);border-color:rgb(var(--clr))}
.prod-icon{
  width:72px;height:72px;border-radius:20px;
  display:flex;align-items:center;justify-content:center;margin-bottom:18px;
}
.prod-icon svg{width:34px;height:34px}
.prod-name{font-family:'Heebo',sans-serif;font-size:1.18rem;font-weight:800;color:var(--navy);line-height:1.3;margin-bottom:11px}
.prod-desc{font-family:'Heebo',sans-serif;font-size:.86rem;font-weight:400;color:var(--muted);line-height:1.65;text-align:center}
.prod-badge{display:inline-block;font-size:.62rem;font-weight:700;letter-spacing:.05em;padding:5px 14px;border-radius:100px}
.prod-badge-live{background:rgba(34,200,100,.13);color:#27ae60}
.prod-badge-soon{background:rgba(41,67,104,.07);color:var(--muted)}
.prod-link{
  margin-top:12px;display:inline-block;
  font-size:.78rem;font-weight:700;letter-spacing:.02em;
  color:rgb(var(--clr));text-decoration:none;
  border-bottom:1.5px solid rgba(var(--clr),.35);
  padding-bottom:1px;transition:border-color .2s;
}
.prod-link:hover{border-color:rgb(var(--clr))}
/* קישור לתוכנה באינטרנט — נצמד לתחתית הריבוע */
.prod-card .prod-link{margin-top:auto;padding-top:16px}
/* אייקון מגן החברה (במקום אייקון הקו) לתוכנה החיה */
.prod-icon-shield{background:transparent!important;width:auto;height:72px;margin-bottom:14px}
.prod-icon-shield img{height:72px;width:auto;display:block;filter:drop-shadow(0 4px 10px rgba(41,67,104,.18))}
/* highlight when navigated from sun */
.prod-card.highlight{
  border-color:rgb(var(--clr));
  box-shadow:0 0 0 4px rgba(var(--clr),.18),0 22px 56px rgba(var(--clr),.28);
  transform:translateY(-6px) scale(1.03);
  animation:cardPop .5s ease;
}
@keyframes cardPop{0%{transform:scale(1)}55%{transform:translateY(-10px) scale(1.07)}100%{transform:translateY(-6px) scale(1.03)}}
/* כרטיס יחיד שנשאר לבדו בשורה האחרונה — ממורכז בעמודה האמצעית ולא נצמד לקצה */
@media(min-width:1001px){.prod-grid>.prod-card:last-child:nth-child(3n+1){grid-column:2}}
@media(max-width:1000px){.prod-grid{grid-template-columns:repeat(2,1fr)}}
/* מספר אי-זוגי של ריבועים — האחרון ממורכז בשורה בתצוגת שתי עמודות */
@media(min-width:561px) and (max-width:1000px){.prod-grid>.prod-card:last-child:nth-child(2n+1){grid-column:1/-1;justify-self:center;width:calc(50% - 11px)}}
@media(max-width:560px){.prod-grid{grid-template-columns:1fr}}

/* ABOUT */
.about{padding:88px 5%;background:var(--white);text-align:center}
.sec-ey{font-size:.63rem;font-weight:700;letter-spacing:.16em;color:var(--gold);text-transform:uppercase;margin-bottom:12px}
.about h2{font-size:clamp(1.6rem,2.8vw,2.3rem);font-weight:800;color:var(--navy);margin-bottom:10px}
.about-sub{font-size:.93rem;color:var(--muted);margin-bottom:50px;max-width:560px;margin-left:auto;margin-right:auto;line-height:1.75}
.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;max-width:920px;margin:0 auto}
.why-card{padding:32px 24px;border:1px solid var(--brd);border-radius:16px;text-align:right;transition:all .25s}
.why-card:hover{border-color:var(--navy);box-shadow:0 12px 36px rgba(41,67,104,.09);transform:translateY(-4px)}
.why-icon{width:46px;height:46px;background:linear-gradient(135deg,var(--navy),var(--navy2));border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.2rem;margin-bottom:16px}
.why-card h3{font-size:.97rem;font-weight:700;color:var(--navy);margin-bottom:9px}
.why-card p{font-size:.83rem;color:var(--muted);line-height:1.65}
.why-eng{display:inline-block;margin-top:11px;font-size:.55rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);border:1px solid rgba(200,169,81,.3);padding:3px 10px;border-radius:100px}

/* CONTACT */
.contact{
  background:linear-gradient(150deg,#1E3356 0%,#253f6a 60%,#294368 100%);
  padding:80px 5%;
  overflow:hidden;position:relative;
}
.contact::before{
  content:'';position:absolute;
  top:-80px;left:35%;
  width:480px;height:480px;
  background:radial-gradient(circle,rgba(200,169,81,.09),transparent 70%);
  border-radius:50%;pointer-events:none;
}
.contact::after{
  content:'';position:absolute;
  bottom:-60px;right:10%;
  width:320px;height:320px;
  background:radial-gradient(circle,rgba(200,169,81,.05),transparent 70%);
  border-radius:50%;pointer-events:none;
}
.contact-grid{
  display:grid;grid-template-columns:1fr 1fr;gap:56px;
  max-width:1080px;margin:0 auto;align-items:center;
  position:relative;z-index:1;
}
.contact-left{display:flex;flex-direction:column}
.contact-left h2{font-size:clamp(2rem,3.2vw,3rem);font-weight:900;color:#fff;line-height:1.15;margin-bottom:18px}
#rotText{display:inline-block;transition:opacity .38s ease,transform .38s ease}
.contact-left h2 .gold{background:linear-gradient(120deg,#C8A951,#E8D48A);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.contact-left p{font-size:.93rem;color:rgba(255,255,255,.62);line-height:1.8;margin-bottom:36px;max-width:380px}
/* floating white card */
.contact-right{
  background:var(--white);
  border-radius:24px;
  padding:44px 40px;
  box-shadow:0 32px 80px rgba(0,0,0,.28),0 0 0 1px rgba(255,255,255,.06);
  display:flex;flex-direction:column;gap:24px;
}
.cdet{display:flex;align-items:center;gap:16px}
.cdet-icon{
  width:46px;height:46px;min-width:46px;
  background:linear-gradient(135deg,var(--navy),var(--navy2));
  border-radius:12px;display:flex;align-items:center;justify-content:center;
  font-size:1rem;color:#fff;
  box-shadow:0 4px 14px rgba(41,67,104,.22);
}
.cdet-info{display:flex;flex-direction:column;gap:2px}
.cdet-label{font-size:.62rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.cdet strong{font-size:.93rem;color:var(--navy);font-weight:600}
.contact-divider{height:1px;background:var(--brd)}
/* contact mini-details on left */
.contact-dets{display:flex;flex-direction:column;gap:10px;margin-top:24px}
.cdet-inline{display:flex;align-items:center;gap:10px;font-size:.85rem;color:rgba(255,255,255,.7)}
.cdet-inline a{color:inherit;text-decoration:none}
.cdet-inline a:hover{text-decoration:underline}
.cdet-inline span{font-size:1rem}
/* contact form */
.contact-form{display:flex;flex-direction:column;gap:14px}
.cf-row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.contact-form input,.contact-form textarea{
  width:100%;padding:11px 15px;
  border:1.5px solid var(--brd);border-radius:10px;
  font-family:inherit;font-size:.87rem;color:var(--ink);
  background:#fafaf8;outline:none;transition:border-color .2s;direction:rtl;
}
.contact-form input:focus,.contact-form textarea:focus{border-color:var(--navy);background:#fff}
.contact-form textarea{min-height:100px;resize:vertical}
.cf-submit{
  background:var(--navy);color:#fff;
  padding:13px;border:none;border-radius:10px;
  font-family:inherit;font-size:.92rem;font-weight:700;
  cursor:pointer;transition:background .2s;
}
.cf-submit:hover{background:var(--navy2)}
.cf-thanks{display:none;text-align:center;color:var(--navy);font-weight:700;padding:14px;font-size:.95rem}
@media(max-width:860px){.contact-grid{grid-template-columns:1fr;gap:32px}.contact-right{padding:32px 28px}.cf-row{grid-template-columns:1fr}}

/* FOOTER */
footer{background:var(--navy2);padding:34px 5%;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:14px}
.footer-brand{display:flex;align-items:center;gap:10px}
.footer-brand img{height:26px;filter:brightness(0) invert(1);opacity:.6}
.footer-txt{font-size:.68rem;color:rgba(255,255,255,.38)}
.footer-legal{display:flex;gap:8px;align-items:center;flex-wrap:wrap;justify-content:center}
.footer-legal button{background:none;border:none;font-family:inherit;font-size:.72rem;
  color:rgba(255,255,255,.9);text-decoration:underline;cursor:pointer;padding:4px}
.footer-legal button:hover{color:var(--gold2)}
.footer-legal .sep{color:rgba(255,255,255,.4);font-size:.7rem}

/* ───────── MOBILE / TABLET ───────── */
@media(max-width:860px){
  /* top bar — keep on one line, smaller, drop the longest phrase + its dot */
  .topbar{font-size:.54rem;letter-spacing:.05em;gap:9px;padding:7px 4%}
  .tb-long,.topbar>span:nth-child(4){display:none}

  /* hero sizes to content; header offset is set precisely by JS (fitHeader) */
  .above-fold{min-height:auto}

  /* nav — wrap to two tidy rows so BOTH buttons stay visible */
  nav{height:auto;min-height:0;padding:9px 4%;flex-wrap:wrap;justify-content:space-between;row-gap:9px}
  .nav-links{display:none}
  .nav-brand-sub{display:none}
  .nav-brand{gap:9px}
  .nav-brand img{height:50px}
  .nav-brand-name{font-size:.86rem}
  nav>div:last-child{flex-basis:100%;justify-content:center}
  .nav-login,.nav-cta{padding:8px 15px;font-size:.78rem;white-space:nowrap}

  /* hub — keep the FULL sun (orb + rays + nodes), scaled down proportionally */
  .hub-section{flex:0 0 auto;min-height:108vw;max-height:470px;padding:0;position:relative;overflow:hidden}
  .hub-orb{width:104px;height:104px}
  .hub-orb img{height:78px}
  .orb-pulse{width:104px;height:104px}
  .pnode-card{width:clamp(76px,23vw,96px);padding:7px 6px 6px;border-radius:11px;gap:2px}
  .pnode-icon{padding:6px;border-radius:9px;margin-bottom:0}
  .pnode-icon svg{width:18px;height:18px}
  .pnode-name{display:none}
  .pnode-name-sm{display:block;font-size:.6rem}

  /* tighten section paddings for phone */
  .hero-top{padding:18px 6% 14px}
  .hero-headline{padding:40px 6% 26px}
  .hero-body{padding:18px 6% 40px}
  .products{padding:56px 5% 60px}
  .about{padding:60px 5%}
  .contact{padding:56px 5%}
  .why-grid{grid-template-columns:1fr}
}

@media(max-width:560px){
  .tech-platform{letter-spacing:.16em;gap:8px;font-size:.92rem}
  /* shrink big headings so they don't overflow the phone width */
  .hero-headline h1{font-size:1.7rem}
  .products-title{font-size:1.6rem}
  .contact-left h2{font-size:1.9rem}
  .about h2{font-size:1.5rem}
  .prod-grid{grid-template-columns:1fr}
  /* stacked, full-width CTA buttons */
  .hero-actions{flex-direction:column;align-items:stretch}
  .btn-navy,.btn-out{text-align:center}
  footer{justify-content:center;text-align:center}
}
</style>
</head>
<body>

<a href="#main" class="skip-link">דילוג לתוכן הראשי</a>

<div class="topbar">
  <span class="tb-item">Economic Advisory</span>
  <span class="topbar-dot" aria-hidden="true"></span>
  <span class="tb-item">Digital Transformation</span>
  <span class="topbar-dot" aria-hidden="true"></span>
  <span class="tb-item tb-long">SaaS Solutions for Local Government</span>
</div>

<nav aria-label="ניווט ראשי">
  <a href="#" class="nav-brand" onclick="window.scrollTo({top:0,behavior:'smooth'});return false;">
    <img src="__LOGO__" alt="לוגו ד.ר שחקים בע&quot;מ — חזרה לראש העמוד">
    <div>
      <div class="nav-brand-name">ד.ר שחקים בע"מ</div>
      <div class="nav-brand-sub">Technology Platform</div>
    </div>
  </a>
  <ul class="nav-links">
    <li><a href="#about">אודות</a></li>
    <li><a href="#contact">צרו קשר</a></li>
  </ul>
  <div style="display:flex;gap:10px;align-items:center">
    <a href="https://tpshk.org.il" class="nav-login" target="_blank" rel="noopener">🌐 מעבר לאתר החברה <span class="sr-only">(נפתח בחלון חדש)</span></a>
    <a href="#contact" class="nav-cta">לקביעת הדגמה חינמית</a>
  </div>
</nav>

<main id="main">
<div class="above-fold">

  <!-- TECHNOLOGY PLATFORM — above hub -->
  <div class="hero-top">
    <div class="tech-platform">
      <span class="tp-dot"></span>
      Technology Platform
      <span class="tp-dot"></span>
    </div>
  </div>

  <!-- HUB — full width dark, fills rest of viewport -->
  <div class="hub-section" id="hubSection">

    <svg class="hub-canvas" id="hubSvg"></svg>

    <div class="orb-pulse"></div>
    <div class="orb-pulse"></div>
    <div class="orb-pulse"></div>

    <div class="hub-orb">
      <img src="__LOGO__" alt="לוגו ד.ר שחקים">
    </div>

    <!-- 9 product nodes — icon + name only, placed by JS -->
__NODES__
  </div><!-- /hub-section -->
</div><!-- /above-fold -->

<!-- HEADLINE — below the fold, revealed on scroll -->
<div class="hero-headline">
  <h1>מהפכה טכנולוגית בשלטון המקומי</h1>
</div>

<!-- HERO BODY — sub text + chips + CTAs -->
<div class="hero-body">
  <p class="hero-sub">ניהול תקציבים, כוח אדם ומשאבים ברשויות מקומיות לרבות אופטימיזציה — בפלטפורמת ענן אחת חכמה ומשולבת.</p>
  <div class="tech-row">
    <span class="tech-chip">Cloud SaaS</span>
    <span class="tech-chip">GovTech</span>
    <span class="tech-chip">Real-Time Analytics</span>
    <span class="tech-chip">Data-Driven</span>
  </div>
  <div class="hero-actions">
    <a href="#products" class="btn-navy">גלה את הפלטפורמה ↓</a>
    <a href="#contact" class="btn-out">קבל הדגמה</a>
  </div>
</div>

<!-- PRODUCTS GRID — all products, always visible -->
<section class="products" id="products">
  <div class="products-head">
    <div class="sec-ey">הפלטפורמה</div>
    <h2 class="products-title">הפלטפורמה הטכנולוגית שלנו</h2>
    <div class="pt-rule"><span></span></div>
    <p class="products-sub">מערכת אחת, פתרונות רבים</p>
  </div>
  <div class="prod-grid">
__GRID__
  </div>
</section>

<!-- ABOUT -->
<section class="about" id="about">
  <div class="sec-ey">מי אנחנו</div>
  <h2>מומחיות כלכלית, חדשנות טכנולוגית</h2>
  <p class="about-sub">ד.ר שחקים בע"מ היא חברת יעוץ כלכלי לרשויות מקומיות, המתרחבת לעולם ה-AI עם פלטפורמות SaaS ייעודיות לשלטון המקומי.</p>
  <div class="why-grid">
    <div class="why-card">
      <div class="why-icon">🧠</div>
      <h3>ידע עמוק ומומחיות טכנולוגית</h3>
      <p>עשרות שנות ניסיון ביעוץ כלכלי לרשויות, בשילוב פיתוח תוכנה מתקדם המותאם בדיוק לשלטון המקומי.</p>
      <div class="why-eng">Domain Expertise · Purpose-Built</div>
    </div>
    <div class="why-card">
      <div class="why-icon">☁️</div>
      <h3>Cloud SaaS</h3>
      <p>כל הפלטפורמות שלנו מבוססות ענן — ללא התקנה מקומית, נגישות מכל מקום, מאובטחות ומעודכנות תמיד.</p>
      <div class="why-eng">Cloud-Native · Zero Setup · Secure</div>
    </div>
    <div class="why-card">
      <div class="why-icon">🤝</div>
      <h3>ליווי מלא</h3>
      <p>הטמעה מקצועית, הדרכת צוותים, תמיכה שוטפת ועדכוני תקנות אוטומטיים — שותפים לניהול, לא רק ספקים.</p>
      <div class="why-eng">Full Onboarding · Ongoing Support</div>
    </div>
  </div>
</section>

<!-- CONTACT -->
<section class="contact" id="contact">
  <div class="contact-grid">
    <div class="contact-left">
      <div class="sec-ey" style="color:var(--gold2);margin-bottom:16px">צרו קשר</div>
      <h2>נשמח<br><span class="gold" id="rotText">לשמוע מכם</span></h2>
      <p>נשמח לתאם הדגמה חינמית ולהסביר כיצד הפלטפורמה שלנו יכולה לחסוך לרשות שלכם שעות עבודה בכל חודש.</p>
      <div class="contact-dets">
        <div class="cdet-inline"><span aria-hidden="true">📧</span> <a href="mailto:info@shk.org.il">info@shk.org.il</a></div>
        <div class="cdet-inline"><span aria-hidden="true">📞</span> <a href="tel:086550759">08-6550759</a></div>
        <div class="cdet-inline"><span aria-hidden="true">🏢</span> האורגים 21, אשדוד</div>
      </div>
    </div>
    <div class="contact-right">
      <form class="contact-form" id="contactForm" onsubmit="sendForm(event)">
        <div class="cf-row">
          <div>
            <label for="cfName" class="sr-only">שם מלא</label>
            <input type="text" id="cfName" name="name" placeholder="שם מלא" autocomplete="name" required>
          </div>
          <div>
            <label for="cfPhone" class="sr-only">טלפון</label>
            <input type="tel" id="cfPhone" name="phone" placeholder="טלפון" autocomplete="tel">
          </div>
        </div>
        <label for="cfEmail" class="sr-only">כתובת מייל</label>
        <input type="email" id="cfEmail" name="email" placeholder="כתובת מייל" autocomplete="email" required>
        <label for="cfMsg" class="sr-only">הודעה</label>
        <textarea id="cfMsg" name="message" placeholder="הודעה..." required></textarea>

        <!-- אישור מדיניות פרטיות — חובה, לא מסומן מראש (חוק הגנת הפרטיות, תיקון 13) -->
        <div class="consent-row">
          <input type="checkbox" id="cfPrivacy" name="privacy_consent" required>
          <label for="cfPrivacy">קראתי ואני מאשר/ת את <button type="button" onclick="openModal('modalPrivacy')">מדיניות הפרטיות</button> ואת השימוש בפרטים שמסרתי לצורך יצירת קשר בנוגע לפנייה זו. <span aria-hidden="true">*</span></label>
        </div>
        <p class="form-note">בטופס זה נאספים: שם מלא, כתובת מייל, מספר טלפון ותוכן ההודעה. הפרטים משמשים אך ורק למענה על פנייתך ואינם מועברים לצד שלישי.</p>

        <button type="submit" class="cf-submit">שלח הודעה ←</button>
      </form>
      <div class="cf-thanks" id="cfThanks" role="status">✓ תודה! נחזור אליכם בהקדם.</div>
    </div>
  </div>
</section>
</main>

<footer>
  <div class="footer-brand">
    <img src="__LOGO__" alt="לוגו ד.ר שחקים בע&quot;מ">
    <div class="footer-txt">Technology Platform · ד.ר שחקים בע"מ</div>
  </div>
  <div class="footer-legal" role="navigation" aria-label="קישורים משפטיים">
    <button type="button" onclick="openModal('modalA11y')">הצהרת נגישות</button>
    <span class="sep" aria-hidden="true">·</span>
    <button type="button" onclick="openModal('modalPrivacy')">מדיניות פרטיות</button>
    <span class="sep" aria-hidden="true">·</span>
    <button type="button" onclick="openModal('modalCookies')">מדיניות עוגיות</button>
    <span class="sep" aria-hidden="true">·</span>
    <button type="button" onclick="openModal('modalTerms')">תקנון ותנאי שימוש</button>
  </div>
  <div class="footer-txt">© 2026 כל הזכויות שמורות לד.ר שחקים בע"מ</div>
</footer>

<!-- ═══════════ רכיב נגישות ═══════════ -->
<button type="button" class="a11y-btn" id="a11yBtn" aria-label="פתיחת תפריט נגישות" aria-expanded="false" aria-controls="a11yPanel">
  <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="12" cy="3.8" r="2.2"/><path d="M20.5 7.6c-2.6.9-5.3 1.4-8.5 1.4s-5.9-.5-8.5-1.4a1.1 1.1 0 1 0-.7 2.1c1.9.7 3.9 1.1 6 1.3v2.3l-2.4 6.8a1.1 1.1 0 0 0 2.1.8L10.4 15h3.2l1.9 5.9a1.1 1.1 0 0 0 2.1-.8L15.2 13.3V11c2.1-.2 4.1-.6 6-1.3a1.1 1.1 0 1 0-.7-2.1z"/></svg>
</button>

<div class="a11y-panel" id="a11yPanel" role="dialog" aria-label="תפריט נגישות" aria-modal="false">
  <h2>הגדרות נגישות</h2>
  <button type="button" class="a11y-opt" id="optFont" aria-pressed="false">
    <span aria-hidden="true">🔠</span> הגדלת טקסט <span id="fontLevel" style="margin-inline-start:auto;font-size:.78rem">רגיל</span>
  </button>
  <button type="button" class="a11y-opt" id="optContrast" aria-pressed="false">
    <span aria-hidden="true">◐</span> ניגודיות גבוהה
  </button>
  <button type="button" class="a11y-opt" id="optMotion" aria-pressed="false">
    <span aria-hidden="true">⏸</span> עצירת אנימציות
  </button>
  <button type="button" class="a11y-opt" id="optLinks" aria-pressed="false">
    <span aria-hidden="true">🔗</span> הדגשת קישורים
  </button>
  <button type="button" class="a11y-reset" id="a11yReset">איפוס כל ההגדרות</button>
  <div class="a11y-links">
    <button type="button" onclick="openModal('modalA11y')">הצהרת הנגישות המלאה</button>
    <button type="button" onclick="openModal('modalPrivacy')">מדיניות פרטיות</button>
  </div>
</div>

<!-- ═══════════ מודאל: הצהרת נגישות ═══════════ -->
<div class="modal" id="modalA11y" role="dialog" aria-modal="true" aria-labelledby="a11yTitle">
  <div class="modal-box">
    <button type="button" class="modal-close" aria-label="סגירת החלון">✕</button>
    <p class="modal-updated">עודכן לאחרונה: יולי 2026</p>
    <h2 id="a11yTitle">הצהרת נגישות</h2>
    <p>ד.ר שחקים בע"מ רואה חשיבות רבה במתן שירות שוויוני לכלל הציבור, ופועלת להנגשת אתר זה לאנשים עם מוגבלות בהתאם ל<strong>תקן הישראלי 5568</strong> ברמת התאמה <strong>AA</strong>, ובהתאם ל<strong>חוק שוויון זכויות לאנשים עם מוגבלות, התשנ"ח-1998</strong> ולתקנות שהותקנו מכוחו.</p>

    <h3>מה הונגש באתר</h3>
    <ul>
      <li><strong>ניווט מלא במקלדת</strong> — ניתן להגיע לכל קישור, כפתור ושדה באמצעות מקש Tab בלבד, עם חיווי מיקוד ברור וקישור "דילוג לתוכן הראשי".</li>
      <li><strong>תמיכה בקוראי מסך</strong> — מבנה כותרות היררכי, תוויות (labels) לכל שדה בטופס, טקסט חלופי (alt) לכל התמונות ותיאורי ARIA לרכיבים אינטראקטיביים.</li>
      <li><strong>ניגודיות צבעים</strong> — יחס ניגודיות של 4.5:1 לפחות לטקסט רגיל, בהתאם לדרישת התקן.</li>
      <li><strong>רכיב נגישות ייעודי</strong> — הגדלת טקסט (עד 140%), מצב ניגודיות גבוהה, עצירת אנימציות והדגשת קישורים. ההגדרות נשמרות בדפדפן שלך לביקורים הבאים.</li>
      <li><strong>כיבוד העדפות מערכת</strong> — האתר מזהה אוטומטית הגדרת "צמצום תנועה" (prefers-reduced-motion) במערכת ההפעלה ועוצר אנימציות בהתאם.</li>
      <li><strong>התאמה למכשירים ניידים</strong> — האתר מותאם לגלישה בטלפון ובטאבלט ותומך בהגדלת תצוגה.</li>
    </ul>

    <h3>הסתייגויות והחרגות</h3>
    <p>למרות מאמצינו, ייתכן שיימצאו באתר חלקים או תכנים שטרם הונגשו במלואם. אנו ממשיכים לפעול לשיפור רמת הנגישות באופן שוטף. אם נתקלת בתקלת נגישות או בעמוד שאינו נגיש — נשמח שתדווח/י לנו ונטפל בכך בהקדם.</p>

    <h3>פרטי רכזת הנגישות</h3>
    <div class="modal-contact">
      <p>
        <strong>רכזת נגישות:</strong> רעות בוקר<br>
        <strong>טלפון:</strong> <a href="tel:086550759">08-6550759</a><br>
        <strong>דוא"ל:</strong> <a href="mailto:info@shk.org.il">info@shk.org.il</a><br>
        <strong>כתובת:</strong> האורגים 21, אשדוד
      </p>
      <p style="margin-top:10px">פניות בנושא נגישות ייענו תוך <strong>3 ימי עסקים</strong>.</p>
    </div>
  </div>
</div>

<!-- ═══════════ מודאל: מדיניות פרטיות ═══════════ -->
<div class="modal" id="modalPrivacy" role="dialog" aria-modal="true" aria-labelledby="privTitle">
  <div class="modal-box">
    <button type="button" class="modal-close" aria-label="סגירת החלון">✕</button>
    <p class="modal-updated">עודכן לאחרונה: יולי 2026</p>
    <h2 id="privTitle">מדיניות פרטיות</h2>
    <p>ד.ר שחקים בע"מ (ח.פ. 516572419, האורגים 21, אשדוד) מכבדת את פרטיותך. מדיניות זו מסבירה איזה מידע נאסף באתר, לשם מה, וכיצד הוא מוגן — בהתאם ל<strong>חוק הגנת הפרטיות, התשמ"א-1981, לרבות תיקון 13 שנכנס לתוקף באוגוסט 2025</strong>.</p>

    <h3>איזה מידע נאסף</h3>
    <p>המידע היחיד שאנו אוספים הוא מידע שאת/ה מוסר/ת לנו מרצונך בטופס יצירת הקשר:</p>
    <ul>
      <li><strong>שם מלא</strong></li>
      <li><strong>כתובת דואר אלקטרוני</strong></li>
      <li><strong>מספר טלפון</strong> (אופציונלי)</li>
      <li><strong>תוכן ההודעה</strong> שכתבת</li>
      <li><strong>תאריך ושעת הפנייה ומקורה</strong> — נשמרים לצורך תיעוד ההסכמה שנתת</li>
    </ul>
    <p>אין חובה חוקית למסור מידע זה, אך בלעדיו לא נוכל לחזור אליך.</p>

    <h3>למה המידע משמש</h3>
    <ul>
      <li>מענה על פנייתך ויצירת קשר חוזר בנוגע אליה בלבד</li>
      <li>תיאום הדגמה או מתן מידע על השירותים שביקשת</li>
    </ul>
    <p><strong>איננו מבצעים דיוור שיווקי</strong> ואיננו שולחים הודעות פרסומיות. פרטיך לא ישמשו לצרכים אחרים מעבר לפנייה שיזמת.</p>

    <h3>העברת מידע לצד שלישי</h3>
    <p>איננו מוכרים, משכירים או מעבירים את פרטיך לצדדים שלישיים למטרות מסחריות. שליחת הטופס מתבצעת באמצעות שירות <strong>FormSubmit</strong>, המעביר את תוכן הפנייה לתיבת הדוא"ל שלנו. מידע עשוי להימסר לגורם שלישי רק אם נידרש לכך על פי דין או צו שיפוטי.</p>

    <h3>אבטחת המידע</h3>
    <p>אנו נוקטים אמצעי אבטחה סבירים להגנה על המידע שנאסף מפני גישה, שימוש או גילוי בלתי מורשים:</p>
    <ul>
      <li>העברת הנתונים מתבצעת בתקשורת מוצפנת (HTTPS/TLS)</li>
      <li>הגישה למידע מוגבלת לעובדים המורשים לכך בלבד ולצורך מילוי תפקידם</li>
      <li>המידע אינו נשמר במסד נתונים פומבי ואינו חשוף לגישה חיצונית</li>
      <li>המידע נשמר לפרק הזמן הנדרש לטיפול בפנייה ולעמידה בחובות שבדין, ולאחר מכן נמחק</li>
    </ul>

    <h3>זכויותיך</h3>
    <p>על פי חוק, את/ה זכאי/ת <strong>לעיין</strong> במידע שנאסף אודותיך, <strong>לתקן</strong> מידע שגוי או לא מעודכן, ו<strong>לבקש את מחיקתו</strong>. לממש זכויות אלה ניתן בפנייה אלינו בפרטים שלהלן, ונטפל בבקשה בתוך פרק זמן סביר ובהתאם להוראות הדין.</p>

    <h3>יצירת קשר בנושא פרטיות</h3>
    <div class="modal-contact">
      <p>
        <strong>דוא"ל:</strong> <a href="mailto:info@shk.org.il">info@shk.org.il</a><br>
        <strong>טלפון:</strong> <a href="tel:086550759">08-6550759</a><br>
        <strong>כתובת:</strong> האורגים 21, אשדוד
      </p>
    </div>
  </div>
</div>

<!-- ═══════════ מודאל: תקנון ותנאי שימוש ═══════════ -->
<div class="modal" id="modalTerms" role="dialog" aria-modal="true" aria-labelledby="termsTitle">
  <div class="modal-box">
    <button type="button" class="modal-close" aria-label="סגירת החלון">✕</button>
    <p class="modal-updated">עודכן לאחרונה: 9 באוגוסט 2026</p>
    <h2 id="termsTitle">תקנון ותנאי שימוש — מערכת שחקים</h2>
    <div class="modal-contact">
      <p>
        <strong>בעלים / מפעיל:</strong> ד.ר שחקים בע"מ (ח.פ. 516572419)<br>
        <strong>כתובת:</strong> האורגים 21, אשדוד<br>
        <strong>דוא"ל:</strong> <a href="mailto:info@shk.org.il">info@shk.org.il</a><br>
        <strong>טלפון:</strong> <a href="tel:086550759">08-6550759</a>
      </p>
    </div>
    <h3>1. כללי, הצדדים ותחולת התקנון</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">מסמך זה מהווה תקנון ותנאי שימוש והתקשרות מחייבים (להלן: &quot;התקנון&quot;) בקשר עם השימוש במערכת שחקים ובשירותים הניתנים באמצעותה או בקשר אליה.</li>
      <li style="margin-bottom:6px">המערכת מופעלת על ידי ד.ר שחקים (להלן: &quot;המפעיל&quot;).</li>
      <li style="margin-bottom:6px">המערכת מיועדת ללקוחות משרד רואי החשבון, לרבות רשויות מקומיות וגופים נוספים המקבלים שירות מהמשרד, וכן לעובדים, בעלי תפקידים ומשתמשים שהוסמכו מטעמם כדין (להלן, יחד ולחוד: &quot;הלקוח&quot; או &quot;המשתמש&quot;).</li>
      <li style="margin-bottom:6px">השימוש במערכת הוא לשימוש מקצועי, ארגוני ועסקי בלבד, ובהתאם למטרות השירות ולהרשאות שניתנו למשתמש.</li>
      <li style="margin-bottom:6px">עצם הגישה למערכת, פתיחת חשבון, התחברות או שימוש בה מהווים אישור כי המשתמש קרא את התקנון, הבין אותו ומסכים לפעול לפיו.</li>
      <li style="margin-bottom:6px">ככל שקיים בין המפעיל לבין הלקוח הסכם פרטני, הצעת מחיר, הזמנה או מסמך התקשרות אחר, יחולו הוראות תקנון זה בנוסף אליו. במקרה של סתירה מפורשת, יגברו הוראות המסמך הפרטני ביחס לאותו עניין.</li>
    </ol>
    <h3>2. מהות המערכת והשירותים</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">מערכת שחקים היא מערכת דיגיטלית שנועדה לסייע ללקוחות לבצע בקרה, ניתוח והצגת תמונת מצב בנוגע לתקציבים, תקנים, כוח אדם, נתוני שכר, נתונים תפעוליים ומידע הנוגע למוסדות חינוך ולפעילות הרשות או הארגון.</li>
      <li style="margin-bottom:6px">המערכת מאפשרת, בין היתר, קליטת נתונים, הזנת מידע, העלאת קבצים ומסמכים, הצגת מידע, ביצוע השוואות, איתור פערים, הפקת דוחות ותובנות ותמיכה בתהליכי בקרה וקבלת החלטות.</li>
      <li style="margin-bottom:6px">חלק מהמידע המשמש את המערכת עשוי להגיע ממערכות הלקוח, מתוכנות שכר, ממידע שמקורו במשרד החינוך, מקבצים שמועלים למערכת או מהזנה של משתמשים מורשים.</li>
      <li style="margin-bottom:6px">המפעיל רשאי לשנות, לעדכן, להוסיף או לגרוע פונקציות, ממשקים ורכיבים במערכת, ובלבד ששינוי כאמור לא יגרע באופן בלתי סביר מעיקר השירות שניתן ללקוח לפי התקשרות פרטנית, ככל שקיימת.</li>
    </ol>
    <h3>3. הגדרות</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">&quot;המערכת&quot; – מערכת שחקים, לרבות הממשקים, האזור האישי, מסדי הנתונים, כלי הניתוח, רכיבי הבינה המלאכותית וכל רכיב טכנולוגי נלווה.</li>
      <li style="margin-bottom:6px">&quot;מידע לקוח&quot; – כל מידע, נתון, קובץ, מסמך, תוכן או רשומה שהלקוח או מי מטעמו מזינים, מעלים, מעבירים או מעמידים לרשות המערכת.</li>
      <li style="margin-bottom:6px">&quot;משתמש מורשה&quot; – אדם שהלקוח אישר לו גישה למערכת בהתאם לתפקידו ולהרשאות שהוגדרו עבורו.</li>
      <li style="margin-bottom:6px">&quot;שירותי צד שלישי&quot; – שירותי תשתית, ענן, אחסון, דואר אלקטרוני, בינה מלאכותית, פיתוח, ניטור, אבטחה או שירות טכנולוגי חיצוני אחר שהמערכת מסתמכת עליו.</li>
      <li style="margin-bottom:6px">&quot;פלט AI&quot; – כל תוצר, ניתוח, חילוץ, סיכום, המלצה, מסקנה או מידע אחר המופק באמצעות רכיב מבוסס בינה מלאכותית.</li>
    </ol>
    <h3>4. פתיחת חשבון, זיהוי והרשאות</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">הגישה למערכת תתאפשר למשתמשים מורשים בלבד, בהתאם להרשאות שהוגדרו על ידי הלקוח או מי שהוסמך לכך מטעמו.</li>
      <li style="margin-bottom:6px">הלקוח אחראי לקבוע מי רשאי להשתמש במערכת, להגדיר הרשאות לפי צורך ותפקיד, להסיר או לחסום משתמשים שאינם זקוקים עוד לגישה ולוודא כי המשתמשים מטעמו מודעים לחובות החלות עליהם.</li>
      <li style="margin-bottom:6px">הלקוח והמשתמשים מתחייבים למסור פרטים נכונים ומעודכנים, לשמור בסוד את פרטי ההתחברות, לא לשתף סיסמאות ולא לאפשר שימוש בחשבון על ידי מי שאינו מורשה.</li>
      <li style="margin-bottom:6px">יש להודיע למפעיל ללא דיחוי על חשד לשימוש בלתי מורשה, אובדן פרטי גישה, חשיפת סיסמה או אירוע אבטחה הנוגע לחשבון.</li>
      <li style="margin-bottom:6px">המפעיל רשאי לדרוש מעת לעת אמצעי זיהוי ואימות נוספים, לרבות אימות דו-שלבי, כאשר הדבר נדרש לצורכי אבטחה או ניהול הרשאות.</li>
    </ol>
    <h3>5. מידע הלקוח ואחריות לתכנים ולמקור המידע</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">הלקוח הוא האחראי לקבוע איזה מידע יוזן או יועמד לרשות המערכת, לאילו מטרות, באיזה היקף ועל ידי אילו משתמשים.</li>
      <li style="margin-bottom:6px">הלקוח מצהיר ומתחייב כי הוא רשאי כדין לאסוף, להחזיק, להשתמש, להעביר ולהעמיד לרשות המערכת את מידע הלקוח, וכי השימוש במידע במסגרת המערכת תואם את מטרותיו, סמכויותיו, חובותיו וההרשאות החלות עליו.</li>
      <li style="margin-bottom:6px">מבלי לגרוע מהאמור, הלקוח אחראי במיוחד לחוקיות עיבודם של נתוני עובדים, נתוני שכר, מידע על תלמידים ומידע רגיש אחר, לרבות קיומם של יידוע, הרשאות, הסכמות או בסיס חוקי אחר, ככל שנדרש.</li>
      <li style="margin-bottom:6px">הלקוח מתחייב שלא להזין או להעלות למערכת מידע שאינו נדרש לצורך השירות, מידע שהעברתו אסורה לפי דין או הסכם, או מידע שלצורך עיבודו אין בידו סמכות או הרשאה מתאימה.</li>
      <li style="margin-bottom:6px">הלקוח אחראי לדיוק, לשלמות, לעדכניות ולאמינות של מידע הלקוח. המפעיל אינו אחראי לשגיאה, פער, מסקנה או תוצאה הנובעים ממידע שגוי, חלקי, לא מעודכן או בלתי תקין שהוזן למערכת.</li>
    </ol>
    <h3>6. שימוש בבינה מלאכותית</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">המערכת עשויה לכלול רכיבים מבוססי בינה מלאכותית לצורך סריקת קבצים, חילוץ נתונים, ניתוח מידע, הצגת מידע, הפקת תובנות ותמיכה בתהליכי בקרה.</li>
      <li style="margin-bottom:6px">לצורך הפעלת רכיבים אלה, מידע וקבצים הנדרשים לעיבוד עשויים להישלח לספק בינה מלאכותית חיצוני, בהתאם למדיניות הפרטיות ולהגדרות השירות.</li>
      <li style="margin-bottom:6px">פלטי AI הם כלי עזר בלבד. הם עשויים לכלול טעויות, חוסרים, אי-דיוקים או מסקנות שאינן מתאימות לנסיבות המקרה, ואין לראות בהם תחליף לבדיקה אנושית, מקצועית או עצמאית.</li>
      <li style="margin-bottom:6px">הלקוח והמשתמשים מתחייבים לבדוק ולאמת מידע מהותי לפני הסתמכות עליו, ובפרט לפני קבלת החלטה תקציבית, תפעולית, ארגונית, מקצועית או אחרת.</li>
      <li style="margin-bottom:6px">המפעיל אינו מתחייב כי פלט AI יהיה מלא, מדויק, עדכני או מתאים למטרה מסוימת, ולא יישא באחריות להחלטה שהתקבלה על סמך פלט שלא נבדק כנדרש.</li>
      <li style="margin-bottom:6px">המפעיל אינו עושה שימוש בנתוני הלקוחות לצורך אימון מודלים של בינה מלאכותית מטעמו, אלא אם נמסר על כך גילוי נפרד ונקבע אחרת בהתאם לדין ולהתקשרות בין הצדדים.</li>
    </ol>
    <h3>7. רישיון שימוש וקניין רוחני</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">בכפוף לעמידה בתקנון ובהתקשרות עם המפעיל, ניתנת ללקוח זכות שימוש מוגבלת, לא בלעדית, בלתי ניתנת להעברה וניתנת לביטול, לצורך שימוש פנימי במערכת בהתאם למטרות השירות.</li>
      <li style="margin-bottom:6px">כל זכויות הקניין הרוחני במערכת ובכל רכיב שלה, לרבות התוכנה, הקוד, מבנה המערכת, העיצוב, הממשקים, המתודולוגיות, התהליכים, האלגוריתמים, כלי הניתוח, השמות, הסימנים והתיעוד, הן של המפעיל או של מעניקי הרישיון שלו.</li>
      <li style="margin-bottom:6px">אין להעתיק, לשכפל, להפיץ, למכור, להשכיר, להעמיד לרשות צד שלישי, לבצע הנדסה לאחור, לפרק, לעקוף מנגנוני הגנה או לעשות שימוש במערכת לצורך בניית מוצר או שירות מתחרה, אלא אם הדבר הותר במפורש ובכתב או לפי דין קוגנטי.</li>
      <li style="margin-bottom:6px">הזכויות במידע הלקוח הגולמי נשארות בידי הלקוח. הלקוח מעניק למפעיל הרשאה מוגבלת להשתמש במידע ככל שנדרש לצורך אספקת השירותים, תפעול, אבטחה, תחזוקה, תמיכה, גיבוי, תיקון תקלות ועמידה בדין.</li>
    </ol>
    <h3>8. שימוש חוקי ואסור</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">הלקוח והמשתמשים מתחייבים להשתמש במערכת אך ורק למטרות חוקיות, בתום לב, בהתאם לדין, להסכמים החלים עליהם, למדיניות הארגונית ולהרשאות שניתנו להם.</li>
      <li style="margin-bottom:6px">אין להשתמש במערכת לצורך פעולה בלתי חוקית, פגיעה בפרטיות, הפרת זכויות של צד שלישי, גישה למידע ללא הרשאה, התחזות, הטעיה, שיבוש פעילות, הפצת קוד זדוני או כל שימוש העלול לפגוע במערכת, במפעיל, בלקוח אחר או בצד שלישי.</li>
      <li style="margin-bottom:6px">אין לנסות לעקוף הרשאות, מנגנוני זיהוי או אבטחה, לבצע חדירה, סריקה בלתי מורשית, שאיבת נתונים, scraping, crawling, harvesting, data mining או שימוש אוטומטי חריג שאינו חלק מהשימוש הרגיל שהמערכת מאפשרת.</li>
      <li style="margin-bottom:6px">אין להעלות למערכת קוד זדוני, קובץ מזיק או תוכן שעלול לשבש את השירות או לסכן מידע, משתמשים או תשתיות.</li>
      <li style="margin-bottom:6px">המפעיל רשאי להגביל, להשעות או לחסום שימוש שנראה לו, על בסיס סביר, כבלתי חוקי, מסוכן, פוגעני, בלתי מורשה או מנוגד לתקנון.</li>
    </ol>
    <h3>9. אבטחת מידע וחובות המשתמש</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">המפעיל פועל ליישום אמצעי אבטחת מידע סבירים ומתאימים לאופי המערכת ולמידע המעובד בה, לרבות מנגנוני זיהוי, ניהול הרשאות, תיעוד פעולות, הצפנה ואמצעי הגנה טכנולוגיים.</li>
      <li style="margin-bottom:6px">אין באפשרות המפעיל להבטיח חסינות מוחלטת מפני תקלה, חדירה, אובדן מידע, שימוש בלתי מורשה, השבתה או אירוע סייבר, ואין לראות באמצעי האבטחה התחייבות לכך שאירועים כאמור לא יתרחשו.</li>
      <li style="margin-bottom:6px">הלקוח אחראי לאבטחת סביבת השימוש שמטעמו, לרבות מחשבים וציוד קצה, חשבונות דואר, רשתות, סיסמאות, הרשאות משתמשים והדרכת העובדים.</li>
      <li style="margin-bottom:6px">הלקוח מתחייב לשתף פעולה באופן סביר עם המפעיל במקרה של אירוע אבטחה, חשד לאירוע, בירור תקלה או צורך בצמצום סיכון.</li>
    </ol>
    <h3>10. פרטיות והגנת מידע</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">עיבוד מידע אישי במסגרת המערכת נעשה בהתאם למדיניות הפרטיות של מערכת שחקים, המהווה מסמך משלים לתקנון זה.</li>
      <li style="margin-bottom:6px">ביחס למידע שהלקוח מזין, מעלה, מעביר או מעמיד לרשות המערכת לצורך קבלת השירות, הלקוח הוא הגורם הקובע את מטרות עיבוד המידע ואת היקפו, והמפעיל מעבד את המידע לצורך מתן השירות ובהתאם להתקשרות בין הצדדים.</li>
      <li style="margin-bottom:6px">הלקוח אחראי למסור לנושאי המידע הודעות, יידוע או הסברים הנדרשים ממנו לפי דין, ולנהל את הפניות והזכויות החלות עליו כבעל סמכות ביחס למידע, ככל שנדרש.</li>
      <li style="margin-bottom:6px">מידע עשוי להיות מעובד באמצעות ספקי צד שלישי ובתשתיות מחוץ לישראל, כמפורט במדיניות הפרטיות.</li>
    </ol>
    <h3>11. שירותי צד שלישי</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">המערכת מסתמכת על שירותי צד שלישי, לרבות שירותי ענן, אחסון, תשתית, דואר אלקטרוני, בינה מלאכותית, ניטור, פיתוח ושירותים טכנולוגיים נוספים.</li>
      <li style="margin-bottom:6px">המפעיל רשאי להחליף ספקי צד שלישי או רכיבים טכנולוגיים מעת לעת, לפי צרכי השירות, אבטחתו, זמינותו, תחזוקתו ושיפורו.</li>
      <li style="margin-bottom:6px">שירותי צד שלישי כפופים גם לתנאיהם ולמדיניות שלהם. המפעיל אינו שולט באופן מלא בזמינותם, באיכותם או בשינויים המבוצעים בהם.</li>
    </ol>
    <h3>12. זמינות, תחזוקה, תקלות ושינויים</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">המפעיל יפעל במאמצים סבירים להעמיד את המערכת לשימוש תקין וזמין, אולם אינו מתחייב לזמינות רציפה או מלאה, לזמינות של 100%, להעדר תקלות, לשירות בלתי מופרע או לרמת זמינות מסוימת, אלא אם נקבע אחרת במפורש בהסכם פרטני.</li>
      <li style="margin-bottom:6px">ייתכנו מעת לעת תקלות, שיבושים, האטות, הפסקות שירות, עבודות תחזוקה, עדכונים, שינויים או מגבלות טכנולוגיות, לרבות עקב שירותי צד שלישי או נסיבות שאינן בשליטת המפעיל.</li>
      <li style="margin-bottom:6px">כאשר תובא לידיעת המפעיל תקלה מהותית שבתחום אחריותו, המפעיל יפעל באופן סביר לבדיקתה ולתיקונה בתוך זמן סביר, בהתחשב במהות התקלה, חומרתה, מורכבות הטיפול, זמינות כוח אדם ותלות בספקים או גורמים חיצוניים. אין בהוראה זו התחייבות לזמן תיקון קבוע או מוגדר.</li>
      <li style="margin-bottom:6px">במקרה של תחזוקה מתוכננת העלולה לגרום להשבתה מהותית, המפעיל ישתדל למסור הודעה מראש, ככל שהדבר אפשרי וסביר בנסיבות.</li>
      <li style="margin-bottom:6px">המפעיל אינו אחראי לעיכוב או אי-יכולת לתקן תקלה הנובעים ממערכת הלקוח, נתוני הלקוח, ציוד קצה, חיבור אינטרנט, שירות חיצוני, הרשאות חסרות או גורם שאינו בשליטתו הסבירה.</li>
    </ol>
    <h3>13. תמיכה ושיתוף פעולה</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">הלקוח ימסור למפעיל מידע סביר הדרוש לצורך בירור תקלה או בקשת תמיכה, לרבות תיאור התקלה, מועד התרחשותה, צילומי מסך או פרטים טכניים רלוונטיים, ככל שניתן למסור אותם כדין.</li>
      <li style="margin-bottom:6px">המפעיל רשאי לבקש מהלקוח לבצע פעולות סבירות לצורך אבחון, בידוד או תיקון תקלה.</li>
      <li style="margin-bottom:6px">עיכוב במסירת מידע, הרשאות או שיתוף פעולה מצד הלקוח עשוי לעכב את הטיפול בתקלה, והמפעיל לא יישא באחריות לעיכוב הנובע מכך.</li>
    </ol>
    <h3>14. השעיה, הגבלת גישה וסיום שימוש</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">המפעיל רשאי להגביל, להשעות או לחסום גישה למערכת, כולה או חלקה, במקרה של הפרת התקנון, שימוש בלתי חוקי או בלתי מורשה, סיכון אבטחה, פגיעה במערכת או בצד שלישי, אי-עמידה בהוראות הדין, או כאשר הדבר נדרש לפי הוראת רשות מוסמכת.</li>
      <li style="margin-bottom:6px">ככל שהדבר אפשרי וסביר, תימסר ללקוח הודעה מתאימה לפני נקיטת פעולה; במקרה דחוף, אבטחתי או משפטי, המפעיל רשאי לפעול ללא הודעה מוקדמת.</li>
      <li style="margin-bottom:6px">סיום ההתקשרות והשימוש במערכת יהיה בהתאם להסכם הפרטני שבין הצדדים, ככל שקיים.</li>
      <li style="margin-bottom:6px">עם סיום ההתקשרות, הגישה למערכת עשויה להיחסם ומידע יימחק, יישמר או יהפוך לאנונימי בהתאם להסכם, למדיניות הפרטיות, לצורכי גיבוי, אבטחה, הגנה על זכויות ולדרישות הדין.</li>
    </ol>
    <h3>15. הגבלת אחריות</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">המערכת והשירותים ניתנים על בסיס מצבם וזמינותם בפועל. המפעיל אינו מציג מצג או התחייבות לכך שהמערכת תתאים לכל צורך פרטני של הלקוח, תפעל ללא הפסקה או תקלה, או שתוצאות, דוחות, ניתוחים ופלטים יהיו חפים משגיאות.</li>
      <li style="margin-bottom:6px">המערכת היא כלי מסייע לבקרה, ניתוח והצגת מידע, ואינה מחליפה שיקול דעת מקצועי, בדיקה עצמאית, אימות מול מערכות המקור או אחריות של בעלי התפקידים אצל הלקוח.</li>
      <li style="margin-bottom:6px">המפעיל לא יישא באחריות לנזק, טעות או תוצאה הנובעים ממידע לקוח שגוי, חסר או לא מעודכן; שימוש בלתי מורשה; הרשאה שגויה; אי-עמידה של הלקוח בדין; הסתמכות על פלט AI ללא בדיקה; תקלה בשירות צד שלישי; חיבור אינטרנט; ציוד הלקוח; או פעולה או מחדל של גורם שאינו בשליטת המפעיל.</li>
      <li style="margin-bottom:6px">בכפוף לכל דין שאינו ניתן להתניה, המפעיל לא יישא באחריות לנזק עקיף, תוצאתי, מיוחד או אגבי, לרבות אובדן רווח, הכנסה, חיסכון צפוי, מוניטין, הזדמנות עסקית, נתונים או השבתת פעילות.</li>
      <li style="margin-bottom:6px">בכל מקרה, ובכפוף לדין שאינו ניתן להתניה, אחריותו המצטברת של המפעיל בגין נזק ישיר הנובע מהמערכת או מהשירותים לא תעלה על סכום התמורה ששולם בפועל למפעיל בגין השירותים במהלך ששת החודשים שקדמו לאירוע שהקים את עילת התביעה.</li>
      <li style="margin-bottom:6px">הגבלות האחריות חלות בכל עילה משפטית, חוזית, נזיקית או אחרת, ומהוות חלק מהקצאת הסיכונים שבין הצדדים. אין בהן כדי לשלול אחריות שלא ניתן לשלול או להגביל לפי דין.</li>
    </ol>
    <h3>16. שיפוי</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">הלקוח ישפה את המפעיל בגין נזק, חבות, הוצאה, קנס או תשלום סביר שיוטלו עליו עקב תביעה או דרישה של צד שלישי שמקורה בהפרת התקנון על ידי הלקוח, שימוש בלתי חוקי או בלתי מורשה במערכת, מידע שהלקוח לא היה רשאי לעבד או להעביר, הפרת זכויות צד שלישי או הפרת דין החלה על הלקוח.</li>
      <li style="margin-bottom:6px">חובת השיפוי תחול בכפוף לכך שהמפעיל יודיע ללקוח על הדרישה בתוך זמן סביר ויאפשר לו, ככל שניתן, להשתתף בטיפול בה, ובלבד שאין בכך כדי לפגוע בזכויות המפעיל או בחובותיו לפי דין.</li>
    </ol>
    <h3>17. סודיות</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">כל צד ישמור בסוד מידע עסקי, מקצועי, טכנולוגי או אחר של הצד השני שהגיע אליו במסגרת ההתקשרות ואשר מטבעו או מנסיבות מסירתו הוא מידע סודי.</li>
      <li style="margin-bottom:6px">המפעיל יהיה רשאי לעשות שימוש במידע סודי של הלקוח רק במידה הנדרשת לצורך מתן השירותים, תחזוקה, תמיכה, אבטחה, תיקון תקלות, הגנה על זכויות ועמידה בדרישות הדין.</li>
      <li style="margin-bottom:6px">התחייבות הסודיות לא תחול על מידע שהיה פומבי שלא עקב הפרה, מידע שהתקבל כדין מצד שלישי, מידע שהיה בידי הצד המקבל קודם למסירתו, או מידע שחובה למסרו לפי דין או דרישה מוסמכת.</li>
    </ol>
    <h3>18. כוח עליון</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">המפעיל לא ייחשב כמפר ולא יישא באחריות לעיכוב, שיבוש, השבתה או אי-יכולת לספק שירות הנובעים מנסיבות שאינן בשליטתו הסבירה, לרבות מלחמה, מצב חירום, אירוע ביטחוני, אסון טבע, שביתה, תקלה רחבת היקף בתקשורת או בחשמל, מתקפת סייבר, תקלה אצל ספק ענן או AI, שינוי רגולטורי או הוראת רשות מוסמכת.</li>
      <li style="margin-bottom:6px">בנסיבות כאמור יפעל המפעיל, ככל שניתן באופן סביר, לצמצום הפגיעה ולהשבת השירות לפעילות.</li>
    </ol>
    <h3>19. עדכונים בתקנון</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">המפעיל רשאי לעדכן תקנון זה מעת לעת עקב שינויים במערכת, בשירותים, בטכנולוגיה, בספקים, באבטחת המידע או בדרישות הדין.</li>
      <li style="margin-bottom:6px">כאשר יבוצע שינוי מהותי, תימסר הודעה בדרך סבירה, בהתאם לנסיבות ולהוראות הדין. המשך שימוש במערכת לאחר כניסת העדכון לתוקף יהווה הסכמה לתקנון המעודכן, בכפוף לדין ולהסכם פרטני.</li>
    </ol>
    <h3>20. הוראות כלליות</h3>
    <ol style="padding-right:22px;margin:6px 0">
      <li style="margin-bottom:6px">הלקוח אינו רשאי להמחות או להעביר את זכויותיו או התחייבויותיו לפי התקנון לצד שלישי ללא הסכמה מראש ובכתב של המפעיל, למעט אם נקבע אחרת בהסכם פרטני.</li>
      <li style="margin-bottom:6px">הימנעות צד מעמידה על זכות לפי התקנון לא תיחשב ויתור עליה.</li>
      <li style="margin-bottom:6px">אם הוראה מהוראות התקנון תיקבע כבלתי תקפה או בלתי אכיפה, לא יהיה בכך כדי לפגוע ביתר הוראות התקנון.</li>
      <li style="margin-bottom:6px">על התקנון והשימוש במערכת יחולו דיני מדינת ישראל. סמכות השיפוט תהיה נתונה לבתי המשפט המוסמכים בישראל, אלא אם נקבע אחרת בהסכם פרטני.</li>
      <li style="margin-bottom:6px">בכל שאלה או פנייה בנוגע למערכת או לתקנון ניתן לפנות למפעיל באמצעות פרטי הקשר המפורטים בראש מסמך זה.</li>
    </ol>
  </div>
</div>

<!-- ═══════════ מודאל: מדיניות עוגיות ═══════════ -->
<div class="modal" id="modalCookies" role="dialog" aria-modal="true" aria-labelledby="ckTitle">
  <div class="modal-box">
    <button type="button" class="modal-close" aria-label="סגירת החלון">✕</button>
    <p class="modal-updated">עודכן לאחרונה: יולי 2026</p>
    <h2 id="ckTitle">מדיניות עוגיות (Cookies)</h2>
    <p>עוגייה (Cookie) היא קובץ טקסט קטן שנשמר בדפדפן שלך בעת הגלישה באתר. להלן פירוט מלא של השימוש באתר זה.</p>

    <h3>עוגיות הכרחיות בלבד</h3>
    <p>אתר זה עושה שימוש מצומצם ביותר, ורק באחסון מקומי (localStorage) הנדרש לתפקוד תקין:</p>
    <ul>
      <li><strong>הגדרות הנגישות שבחרת</strong> — גודל טקסט, ניגודיות, עצירת אנימציות והדגשת קישורים. נשמרות כדי שלא תצטרך/י להגדיר אותן מחדש בכל ביקור.</li>
      <li><strong>אישור הודעת העוגיות</strong> — כדי שההודעה לא תוצג לך שוב.</li>
    </ul>

    <h3>מה איננו עושים</h3>
    <p>אתר זה <strong>אינו משתמש</strong> בעוגיות מעקב, בפיקסלים פרסומיים, ב-Google Analytics, ב-Facebook Pixel או בכל כלי מעקב או פרסום מבוסס-צד-שלישי. המידע השמור בדפדפן שלך <strong>אינו נשלח לשרתינו ואינו מזהה אותך אישית</strong>.</p>

    <h3>איך למחוק</h3>
    <p>ניתן למחוק את המידע בכל עת דרך הגדרות הדפדפן (ניקוי נתוני גלישה), או באמצעות כפתור "איפוס כל ההגדרות" בתפריט הנגישות. מחיקה לא תפגע ביכולת השימוש באתר.</p>
    <p>לפרטים נוספים ראו את <button type="button" onclick="openModal('modalPrivacy')" style="background:none;border:none;color:var(--navy);font:inherit;font-weight:700;text-decoration:underline;cursor:pointer;padding:0">מדיניות הפרטיות</button>.</p>
  </div>
</div>

<!-- ═══════════ באנר עוגיות ═══════════ -->
<div class="cookie-bar" id="cookieBar" role="region" aria-label="הודעת עוגיות">
  <p><strong>אנחנו משתמשים באחסון מקומי בדפדפן</strong> כדי לשמור את הגדרות הנגישות שתבחר/י ואת אישור ההודעה הזו בלבד. איננו משתמשים בעוגיות מעקב או בפיקסלים פרסומיים.</p>
  <div class="cookie-actions">
    <button type="button" class="cookie-accept" id="cookieAccept">הבנתי</button>
  </div>
</div>

<script>
// 9 product nodes — balanced ring [xPct, yPct], kept inside bounds
const POS = __POS__;
const MPOS = __MPOS__;          // tighter symmetric ring for phones
let CUR = POS;                  // active position set (desktop vs mobile)

const hub = document.getElementById('hubSection');
const svg = document.getElementById('hubSvg');
const nodes = hub.querySelectorAll('.pnode');
let geo = {W:0, H:0, cx:0, cy:0};
let pinnedIdx = null;  // הקרן הננעלת בלחיצה (ברירת מחדל: ללא הדגשה)
let hoverIdx = null;   // הקרן המודגשת זמנית במעבר עכבר

function layout() {
  CUR = (window.innerWidth <= 600) ? MPOS : POS;
  const W = hub.offsetWidth, H = hub.offsetHeight;
  geo = {W, H, cx:W*0.5, cy:H*0.5};
  svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
  nodes.forEach((n, i) => {
    n.style.left = (W * CUR[i][0] / 100) + 'px';
    n.style.top  = (H * CUR[i][1] / 100) + 'px';
  });
  drawRays();
}

function drawRays() {
  const {W, H, cx, cy} = geo;
  const active = (hoverIdx != null) ? hoverIdx : pinnedIdx;

  let inner = `
    <defs>
      <radialGradient id="cg" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="rgba(200,169,81,.14)"/>
        <stop offset="100%" stop-color="rgba(200,169,81,0)"/>
      </radialGradient>
    </defs>
    <ellipse cx="${cx}" cy="${cy}" rx="${W*.32}" ry="${H*.38}" fill="url(#cg)"/>
  `;

  // draw non-active rays first, active on top
  const order = [];
  nodes.forEach((n,i)=>{ if(i!==active) order.push(i); });
  if (active!=null) order.push(active);

  order.forEach(i => {
    const n = nodes[i];
    const nx = W * CUR[i][0] / 100;
    const ny = H * CUR[i][1] / 100;
    const rgb = n.dataset.rgb || '255,255,255';

    if (i === active) {
      inner += `<line x1="${cx}" y1="${cy}" x2="${nx}" y2="${ny}" stroke="rgba(${rgb},.22)" stroke-width="7" stroke-linecap="round"/>`;
      inner += `<line x1="${cx}" y1="${cy}" x2="${nx}" y2="${ny}" stroke="rgba(${rgb},.95)" stroke-width="2.4" stroke-dasharray="7 5" stroke-linecap="round">
                  <animate attributeName="stroke-dashoffset" from="0" to="-24" dur="1.1s" repeatCount="indefinite"/></line>`;
      inner += `<circle cx="${nx}" cy="${ny}" r="6" fill="rgb(${rgb})"/>`;
      inner += `<circle cx="${nx}" cy="${ny}" r="6" fill="none" stroke="rgba(${rgb},.4)" stroke-width="2">
                  <animate attributeName="r" from="6" to="15" dur="1.4s" repeatCount="indefinite"/>
                  <animate attributeName="opacity" from=".6" to="0" dur="1.4s" repeatCount="indefinite"/></circle>`;
    } else {
      inner += `<line x1="${cx}" y1="${cy}" x2="${nx}" y2="${ny}" stroke="rgba(255,255,255,.11)" stroke-width="1" stroke-dasharray="3 9">
                  <animate attributeName="stroke-dashoffset" from="0" to="-24" dur="${2.4+i*0.4}s" repeatCount="indefinite"/></line>`;
      inner += `<circle cx="${nx}" cy="${ny}" r="2.5" fill="rgba(255,255,255,.2)"/>`;
    }
  });

  svg.innerHTML = inner;
}

nodes.forEach((n, i) => {
  // hover → highlight this ray temporarily
  n.addEventListener('mouseenter', () => { hoverIdx = i; drawRays(); });
  n.addEventListener('mouseleave', () => { hoverIdx = null; drawRays(); });
  // מיקוד מקלדת → אותה הדגשה בדיוק כמו מעבר עכבר
  n.addEventListener('focusin',  () => { hoverIdx = i; drawRays(); });
  n.addEventListener('focusout', () => { hoverIdx = null; drawRays(); });
  // click → pin this ray permanently + scroll to its card & highlight it
  n.addEventListener('click', () => {
    pinnedIdx = i; hoverIdx = null; drawRays();
    const card = document.getElementById(n.dataset.target);
    if (!card) return;
    document.querySelectorAll('.prod-card.highlight').forEach(c=>c.classList.remove('highlight'));
    const y = card.getBoundingClientRect().top + window.scrollY - 120;
    window.scrollTo({top:y, behavior:'smooth'});
    setTimeout(()=>{
      card.classList.remove('highlight'); void card.offsetWidth;
      card.classList.add('highlight');
    }, 420);
  });
});

// keep the content starting exactly below the fixed top-bar + nav (handles the
// taller two-row mobile nav without guessing a fixed margin)
function fitHeader(){
  const tb=document.querySelector('.topbar'), nv=document.querySelector('nav'), af=document.querySelector('.above-fold');
  if(af && tb && nv) af.style.marginTop = (tb.offsetHeight + nv.offsetHeight) + 'px';
}
function relayout(){ fitHeader(); layout(); }
relayout();
window.addEventListener('resize', relayout);
window.addEventListener('load', relayout);

// rotating contact headline
(function(){
  const phrases=['לשמוע מכם','לתאם הדגמה','לענות על שאלות'];
  let idx=0;
  const el=document.getElementById('rotText');
  if(!el) return;
  setInterval(()=>{
    el.style.opacity='0';
    el.style.transform='translateY(-14px)';
    setTimeout(()=>{
      idx=(idx+1)%phrases.length;
      el.textContent=phrases[idx];
      el.style.transform='translateY(14px)';
      requestAnimationFrame(()=>requestAnimationFrame(()=>{
        el.style.opacity='1';
        el.style.transform='translateY(0)';
      }));
    },380);
  },3200);
})();

/* ═══════════ רכיב נגישות — נשמר ב-localStorage ═══════════ */
(function(){
  const root=document.documentElement;
  const store={
    get(k,d){ try{ return localStorage.getItem('a11y_'+k) ?? d; }catch(e){ return d; } },
    set(k,v){ try{ localStorage.setItem('a11y_'+k,v); }catch(e){} },
    del(k){ try{ localStorage.removeItem('a11y_'+k); }catch(e){} }
  };
  const FONT_LABELS=['רגיל','גדול','גדול מאוד','ענק'];

  function apply(){
    const font=store.get('font','0');
    const contrast=store.get('contrast','0');
    const motion=store.get('motion','0');
    const links=store.get('links','0');
    font==='0' ? root.removeAttribute('data-a11y-font') : root.setAttribute('data-a11y-font',font);
    contrast==='1' ? root.setAttribute('data-a11y-contrast','1') : root.removeAttribute('data-a11y-contrast');
    motion==='1' ? root.setAttribute('data-a11y-motion','1') : root.removeAttribute('data-a11y-motion');
    links==='1' ? root.setAttribute('data-a11y-links','1') : root.removeAttribute('data-a11y-links');
    const fo=document.getElementById('optFont');
    if(fo){ fo.setAttribute('aria-pressed',font!=='0'); document.getElementById('fontLevel').textContent=FONT_LABELS[+font]; }
    const set=(id,on)=>{const el=document.getElementById(id); if(el) el.setAttribute('aria-pressed',on);};
    set('optContrast',contrast==='1'); set('optMotion',motion==='1'); set('optLinks',links==='1');
    if(typeof relayout==='function') relayout();
  }

  const btn=document.getElementById('a11yBtn'), panel=document.getElementById('a11yPanel');
  function togglePanel(open){
    const isOpen = open ?? panel.getAttribute('data-open')!=='1';
    panel.setAttribute('data-open', isOpen?'1':'0');
    btn.setAttribute('aria-expanded', isOpen);
    if(isOpen) panel.querySelector('.a11y-opt').focus();
  }
  btn.addEventListener('click',()=>togglePanel());
  document.addEventListener('click',e=>{
    if(panel.getAttribute('data-open')==='1' && !panel.contains(e.target) && !btn.contains(e.target)) togglePanel(false);
  });
  document.addEventListener('keydown',e=>{
    if(e.key==='Escape' && panel.getAttribute('data-open')==='1'){ togglePanel(false); btn.focus(); }
  });

  document.getElementById('optFont').addEventListener('click',()=>{
    store.set('font', String((+store.get('font','0')+1)%4)); apply();
  });
  document.getElementById('optContrast').addEventListener('click',()=>{
    store.set('contrast', store.get('contrast','0')==='1'?'0':'1'); apply();
  });
  document.getElementById('optMotion').addEventListener('click',()=>{
    store.set('motion', store.get('motion','0')==='1'?'0':'1'); apply();
  });
  document.getElementById('optLinks').addEventListener('click',()=>{
    store.set('links', store.get('links','0')==='1'?'0':'1'); apply();
  });
  document.getElementById('a11yReset').addEventListener('click',()=>{
    ['font','contrast','motion','links'].forEach(store.del);
    try{ localStorage.removeItem('cookie_consent'); }catch(e){}
    apply();
  });

  apply();
})();

/* ═══════════ מודאלים — עם מלכודת מיקוד והחזרת המיקוד ═══════════ */
let _lastFocus=null;
function openModal(id){
  const m=document.getElementById(id);
  if(!m) return;
  _lastFocus=document.activeElement;
  m.setAttribute('data-open','1');
  document.body.style.overflow='hidden';
  m.querySelector('.modal-close').focus();
}
function closeModal(m){
  m.setAttribute('data-open','0');
  document.body.style.overflow='';
  if(_lastFocus) _lastFocus.focus();
}
document.querySelectorAll('.modal').forEach(m=>{
  m.querySelector('.modal-close').addEventListener('click',()=>closeModal(m));
  m.addEventListener('click',e=>{ if(e.target===m) closeModal(m); });
  m.addEventListener('keydown',e=>{
    if(e.key==='Escape'){ closeModal(m); return; }
    if(e.key!=='Tab') return;
    const f=[...m.querySelectorAll('a[href],button,input,textarea,[tabindex]:not([tabindex="-1"])')]
              .filter(el=>el.offsetParent!==null);
    if(!f.length) return;
    const first=f[0], last=f[f.length-1];
    if(e.shiftKey && document.activeElement===first){ e.preventDefault(); last.focus(); }
    else if(!e.shiftKey && document.activeElement===last){ e.preventDefault(); first.focus(); }
  });
});

/* ═══════════ באנר עוגיות ═══════════ */
(function(){
  const bar=document.getElementById('cookieBar');
  let consent=null;
  try{ consent=localStorage.getItem('cookie_consent'); }catch(e){}
  if(!consent) setTimeout(()=>bar.setAttribute('data-open','1'),900);
  const decide=v=>{ try{ localStorage.setItem('cookie_consent',v); }catch(e){} bar.setAttribute('data-open','0'); };
  document.getElementById('cookieAccept').addEventListener('click',()=>decide('accepted'));
})();

async function sendForm(e){
  e.preventDefault();
  const f=e.target;
  if(!f.privacy_consent.checked){
    alert('יש לאשר את מדיניות הפרטיות לפני שליחת הטופס.');
    f.privacy_consent.focus();
    return;
  }
  const btn=f.querySelector('button[type=submit]');
  const orig=btn.textContent;
  btn.disabled=true; btn.textContent='שולח...';
  try{
    const fd=new FormData(f);
    // תיעוד ההסכמה — מתי, איך ומאיפה ניתנה (חוק הגנת הפרטיות)
    fd.set('privacy_consent','כן — אושר במפורש בטופס');
    fd.append('תאריך ושעת ההסכמה', new Date().toLocaleString('he-IL',{dateStyle:'full',timeStyle:'medium'}));
    fd.append('מקור ההסכמה', 'טופס יצירת קשר · ' + window.location.href);
    fd.append('_subject','פנייה חדשה מדף הנחיתה — תוכנות שחקים');
    fd.append('_template','table');
    fd.append('_captcha','false');
    const res=await fetch('https://formsubmit.co/ajax/info@shk.org.il',{
      method:'POST',
      headers:{'Accept':'application/json'},
      body:fd
    });
    const data=await res.json();
    if(String(data.success)!=='true') throw new Error();
    const thanks=document.getElementById('cfThanks');
    f.style.display='none';
    thanks.style.display='block';
    setTimeout(()=>{
      f.reset();
      btn.disabled=false; btn.textContent=orig;
      thanks.style.display='none';
      f.style.display='';
    },5000);
  }catch(err){
    btn.disabled=false; btn.textContent=orig;
    alert('אירעה שגיאה בשליחה. נסו שוב, או כתבו לנו ישירות ל-info@shk.org.il');
  }
}
</script>
</body>
</html>"""

import shutil
html = (page
        .replace('__NODES__', nodes_html)
        .replace('__GRID__', grid_html)
        .replace('__MPOS__', mpos_js)
        .replace('__POS__', pos_js)
        .replace('__LOGO__', logo_src)
        .replace('__SHIELD__', shield_src))
out = os.path.join(os.path.dirname(__file__), 'index.html')
bak = os.path.join(os.path.dirname(__file__), 'index_backup.html')
if os.path.exists(out):
    shutil.copy(out, bak)
    print('Backup saved: index_backup.html')
open(out, 'w', encoding='utf-8').write(html)
print(f'Done! {len(html):,} chars')
