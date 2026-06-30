import base64, os, io
from PIL import Image

logo_path = os.path.join(os.path.dirname(__file__), 'לוגו.png')
logo_b64 = base64.b64encode(open(logo_path, 'rb').read()).decode()
logo_src = f'data:image/png;base64,{logo_b64}'

# רק המגן — ללא הכיתוב שמתחת (קיים בשורות 375-453)
_img = Image.open(logo_path).convert('RGBA')
_shield = _img.crop((0, 0, 455, 375))
_buf = io.BytesIO()
_shield.save(_buf, format='PNG')
shield_src = f'data:image/png;base64,{base64.b64encode(_buf.getvalue()).decode()}'

# ── רשימת התוכנות — מקור אמת אחד לשמש ולרשת הפירוט ──
# rgb = צבע הדגשה מעודן לכל תוכנה ; svg = אייקון קו נקי
_SVG = {
 "hr":'<path d="M16 19v-1a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v1"/><circle cx="9" cy="7" r="3"/><path d="M22 19v-1a4 4 0 0 0-3-3.87"/><path d="M16 4.13a4 4 0 0 1 0 7.75"/>',
 "budget":'<path d="M21 12V7H5a2 2 0 0 1 0-4h14v4"/><path d="M3 5v14a2 2 0 0 0 2 2h16v-5"/><path d="M18 12a2 2 0 0 0 0 4h4v-4z"/>',
 "hours":'<path d="M5 2h9l5 5v15H5z"/><path d="M14 2v5h5"/><path d="M8 11h6M8 14h6"/><circle cx="11" cy="18" r="2"/>',
 "transport":'<rect x="4" y="3" width="16" height="14" rx="2"/><path d="M4 11h16"/><path d="M7 17v2M17 17v2"/><circle cx="8" cy="14" r=".6" fill="currentColor"/><circle cx="16" cy="14" r=".6" fill="currentColor"/>',
 "journal":'<path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/><path d="M4 17.5h13"/><path d="M9 7h6"/>',
 "fees":'<path d="M6 2h12v20l-3-2-3 2-3-2-3 2V2z"/><path d="M9 7h6M9 11h6M9 15h4"/>',
 "welfare":'<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.29 1.51 4.04 3 5.5l7 7Z"/>',
 "salary":'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M8 13h8M8 17h5"/>',
}
def _icon(k):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{_SVG[k]}</svg>'

PRODUCTS = [
    {"id":"hr",        "name":"שליטה מלאה על כח אדם בחינוך וברווחה ברשות", "rgb":"198,160,75",  "live":True,
     "desc":'מערכת מתקדמת לניהול ובקרת מערך כוח האדם להבטחת התנהלות תקינה, שקופה ויעילה. המודול מספק תמונת מצב מדויקת בזמן אמת, תוך השוואה חכמה ורציפה בין התקן המאושר לבין האיוש בפועל — הן ברמת המוסד, התפקיד וחתך הזמן המבוקש.'},
    {"id":"budget",    "name":"בניית תקציב על בסיס אפס",                   "rgb":"62,114,160",  "live":False,
     "desc":'בניית תקציב וניהול פיננסי חכם לאגפי חינוך על בסיס "תקציב אפס". המערכת מסתנכרנת באופן אוטומטי ומלא עם נתוני משרד החינוך העדכניים, ומעניקה למקבלי ההחלטות שליטה מלאה, שקיפות וביטחון בניהול משאבי האגף.'},
    {"id":"hours",     "name":"בקרה וניהול שעות הוראה בתיכונים",          "rgb":"124,104,168", "live":False,
     "desc":'כלי אנליטי מתקדם לניהול ומקסום שעות התקן במוסד החינוכי. המערכת מאפשרת בקרה הדוקה וקבלת החלטות מבוססות-נתונים לייעול מקסימלי של שעות התקן במוסד.'},
    {"id":"transport", "name":"בקרה ואופטימיזציה של תקציבי הסעות",          "rgb":"70,154,128",  "live":False,
     "desc":'בקרה ומקסום הכנסות מערך ההיסעים ברשות, תוך הבטחת שלמות הדיווח.'},
    {"id":"journal",   "name":"פקודת יומן אוטומטית",                       "rgb":"176,138,70",  "live":False,
     "desc":'המערכת מבצעת קליטה אוטומטית ומהירה של תקציבי משרדי הממשלה, ודואגת לרישום מדויק וישיר שלהם בספרי התקציב של הרשות — תוך ייעול ומיכון תהליכים לחיסכון בזמן ומניעת טעויות.'},
    {"id":"fees",      "name":"אגרות חוץ - מענה מקיף",                     "rgb":"176,98,84",   "live":False,
     "desc":'מערך כלים רחב המסייע במיצוי זכויות ומשאבים לרשות הקולטת בשלל תחומים מורכבים: גני ילדים, ליווי בהסעות, שיבוץ סייעות ודירוגי ותק.'},
    {"id":"welfare",   "name":"ביקורת שכר כוח אדם - משרד הרווחה",          "rgb":"72,150,156",  "live":False,
     "desc":'מערכת ייעודית לבקרה מקיפה על כוח האדם באגף הרווחה, לרבות בדיקת כלל הפעולות מול הדיווחים המאושרים למשרד.'},
    {"id":"salary",    "name":"בקרה מדוקדקת על שכר עובדי ההוראה",          "rgb":"150,116,84",  "live":False,
     "desc":'אוטומציה חכמה לניהול ובקרת נתוני שכר בחינוך העל-יסודי. המערכת מבצעת סנכרון והצלבה מדויקת של שכר עובדי הוראה אל מול נתוני משרד החינוך.'},
]
for _p in PRODUCTS:
    _p["icon"] = _icon(_p["id"])

# מיקומי השמש [x%, y%] — פיזור אחיד סביב השמש עם מרווחים שווים; זוויות מעט לא-סימטריות
NODE_POS = [
    [75, 32],  # ניהול כח אדם (ארוך) — ימין, עליון-אמצע
    [35, 22],  # בניית תקציב         — שמאל, עליון
    [58, 19],  # ניהול תיכונים       — מרכז-ימין, עליון
    [80, 56],  # הסעות (ארוך)        — ימין, אמצע
    [67, 76],  # פקודת יומן          — ימין, תחתון
    [42, 81],  # אגרות חוץ           — מרכז-שמאל, תחתון
    [25, 68],  # בקרת כח אדם         — שמאל, תחתון
    [21, 42],  # שכר תיכונים (ארוך)  — שמאל, אמצע
]

# מיקומי טבעת ייעודיים לפלאפון — אובל אנכי סימטרי סביב הלוגו (8 נקודות כל 45°)
MOBILE_NODE_POS = [
    [50, 12],  # למעלה
    [25, 24],  # עליון-שמאל
    [75, 24],  # עליון-ימין
    [85, 50],  # ימין
    [75, 76],  # תחתון-ימין
    [50, 88],  # למטה
    [25, 76],  # תחתון-שמאל
    [15, 50],  # שמאל
]

# תוויות קצרות לריבועי השמש בפלאפון (השם המלא נשאר ברשת המוצרים)
NODE_SHORT = [
    "ניהול כח אדם", "תקציב", "שעות הוראה", "הסעות",
    "פקודת יומן", "אגרות חוץ", "שכר רווחה", "שכר הוראה",
]

# בניית נודות השמש (אייקון + שם בלבד)
nodes_html = ""
for i, p in enumerate(PRODUCTS):
    cls = "live" if p["live"] else "soon"
    nodes_html += f'''    <div class="pnode {cls}" id="pn{i}" data-target="card-{p['id']}" data-rgb="{p['rgb']}">
      <div class="pnode-card">
        <div class="pnode-icon" style="background:rgba({p['rgb']},.16);color:rgb({p['rgb']})">{p['icon']}</div>
        <div class="pnode-name">{p['name']}</div>
        <div class="pnode-name-sm">{NODE_SHORT[i]}</div>
      </div>
    </div>
'''

# בניית רשת הפירוט (כל התוכנות גלויות) — בלי תגיות/קישורים בשלב זה
grid_html = ""
for p in PRODUCTS:
    live_cls = " live" if p["live"] else ""
    grid_html += f'''      <div class="prod-card{live_cls}" id="card-{p['id']}" style="--clr:{p['rgb']}">
        <div class="prod-icon" style="background:rgba({p['rgb']},.15);color:rgb({p['rgb']})">{p['icon']}</div>
        <div class="prod-name">{p['name']}</div>
        <div class="prod-desc">{p['desc']}</div>
      </div>
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
html{scroll-behavior:smooth}
body{font-family:'Segoe UI',Arial,sans-serif;color:var(--ink);background:var(--white);direction:rtl;overflow-x:hidden}

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
  padding:0 5%;display:flex;align-items:center;justify-content:space-between;height:64px;
}
.nav-brand{display:flex;align-items:center;gap:12px;text-decoration:none;cursor:pointer}
.nav-brand img{height:34px;width:auto}
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
  display:grid;grid-template-columns:repeat(4,1fr);gap:22px;
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
/* highlight when navigated from sun */
.prod-card.highlight{
  border-color:rgb(var(--clr));
  box-shadow:0 0 0 4px rgba(var(--clr),.18),0 22px 56px rgba(var(--clr),.28);
  transform:translateY(-6px) scale(1.03);
  animation:cardPop .5s ease;
}
@keyframes cardPop{0%{transform:scale(1)}55%{transform:translateY(-10px) scale(1.07)}100%{transform:translateY(-6px) scale(1.03)}}
@media(max-width:1000px){.prod-grid{grid-template-columns:repeat(2,1fr)}}
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
  .nav-brand img{height:30px}
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

<div class="topbar">
  <span class="tb-item">Economic Advisory</span>
  <span class="topbar-dot"></span>
  <span class="tb-item">Digital Transformation</span>
  <span class="topbar-dot"></span>
  <span class="tb-item tb-long">SaaS Solutions for Local Government</span>
</div>

<nav>
  <a href="#" class="nav-brand" onclick="window.scrollTo({top:0,behavior:'smooth'});return false;">
    <img src="__LOGO__" alt="לוגו">
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
    <a href="https://tpshk.org.il" class="nav-login" target="_blank">🌐 מעבר לאתר החברה</a>
    <a href="#contact" class="nav-cta">לקביעת הדגמה חינמית</a>
  </div>
</nav>

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

    <!-- 8 product nodes — icon + name only, placed by JS -->
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
        <div class="cdet-inline"><span>📧</span> info@shk.org.il</div>
        <div class="cdet-inline"><span>📞</span> 08-6550759</div>
        <div class="cdet-inline"><span>🏢</span> האורגים 21, אשדוד</div>
      </div>
    </div>
    <div class="contact-right">
      <form class="contact-form" id="contactForm" onsubmit="sendForm(event)">
        <div class="cf-row">
          <input type="text" name="name" placeholder="שם מלא" required>
          <input type="tel" name="phone" placeholder="טלפון">
        </div>
        <input type="email" name="email" placeholder="כתובת מייל" required>
        <textarea name="message" placeholder="הודעה..." required></textarea>
        <button type="submit" class="cf-submit">שלח הודעה ←</button>
      </form>
      <div class="cf-thanks" id="cfThanks">✓ תודה! נחזור אליכם בהקדם.</div>
    </div>
  </div>
</section>

<footer>
  <div class="footer-brand">
    <img src="__LOGO__" alt="לוגו">
    <div class="footer-txt">Technology Platform · ד.ר שחקים בע"מ</div>
  </div>
  <div class="footer-txt">© 2026 כל הזכויות שמורות לד.ר שחקים בע"מ</div>
</footer>

<script>
// 8 product nodes — balanced ring [xPct, yPct], kept inside bounds
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

async function sendForm(e){
  e.preventDefault();
  const f=e.target;
  const btn=f.querySelector('button[type=submit]');
  const orig=btn.textContent;
  btn.disabled=true; btn.textContent='שולח...';
  try{
    const fd=new FormData(f);
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
