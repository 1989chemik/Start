#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

# ===== STAŁE FIZYCZNE =====
M_WATER = 18.0        # g/mol
R = 8.314             # J/(mol*K)
T = 293.15            # K (20°C)
V = 40.0              # m^3 (typowy pokój)

LONG_TEXT = """
BigPharma – entropia, nauka i sumienie

1. Czym jest światowa BigPharma – mity, fakty i teorie spiskowe
2. Zachodni rynek farmaceutyczny
3. Chiński rynek farmaceutyczny – kopiowanie czy ewolucja?
4. Polski rynek farmaceutyczny
5. Entropia w farmacji i granice powtarzalności
6. Nieoznaczoność w farmacji – nauka wobec chaosu
7. Polityka a nauka
8. Kościół a nauka – historia, konflikt, przyszłość
9. Aborcja, linie komórkowe i etyka współczesnej farmacji
10. Medycyna niskoentropowa jako alternatywa
11. Ze skrajności w skrajność – kryzys cywilizacyjny
12. Trzecia wojna światowa – wojna w szpitalach
13. Polska jako Mojżesz narodów – mit czy zadanie?
14. Zadania stojące przed polską nauką
15. Teleportacja jonów i granice współczesnej fizyki
16. Zakończenie: Nauka zakorzeniona w prawdzie


Wstęp
Czym jest światowa BigPharma?

Wokół globalnego przemysłu farmaceutycznego narosło wiele mitów, półprawd i teorii spiskowych. Od pytań o pochodzenie wirusa HIV, przez testy szczepionek na zwierzętach, aż po etyczny problem wykorzystywania linii komórkowych powstałych z nienarodzonych dzieci.

Czy koncerny farmaceutyczne ponoszą odpowiedzialność za globalne kryzysy zdrowotne?
Czy produkcja szczepionek oparta na liniach komórkowych pochodzących z aborcji ma przyszłość?
Czy kopiowanie zachodnich modeli przez Chiny doprowadzi do rzeczywistego postępu?

Współczesna nauka deklaruje, że opiera się na prawdzie. Problem polega na tym, że coraz częściej jest to prawda chwilowa, statystyczna, podporządkowana rynkowi i polityce. Tymczasem prawda naukowa nie jest własnością jednostek – ani Hipokratesa, ani Marii Skłodowskiej-Curie – lecz jest zapisem wiedzy budowanej przez wieki.

Chrześcijański Kościół odegrał kluczową rolę w rozwoju nauki, kształtując umysły takich postaci jak Izaak Newton czy Mikołaj Kopernik. Dziś Kościół jednoznacznie sprzeciwia się aborcji. Być może właśnie teraz nadszedł moment, w którym to nauka powinna ponownie czerpać z etyki Kościoła.

Współczesna farmacja wymaga absolutnej powtarzalności. Linie komórkowe pochodzące z aborcji są powtarzalne – i właśnie dlatego stały się fundamentem wielu technologii. Jednak niska entropia pojedynczej dawki leku prowadzi do gwałtownego wzrostu entropii całego systemu farmaceutycznego.

Przyszłość należy do medycyny niskoentropowej.

Aby ją osiągnąć, musimy pogodzić się z nieoznaczonością partii, z fundamentalnymi prawami fizyki i z etyką, której nie da się zamknąć w równaniu – nawet jeśli pojawia się w nim stała Boltzmanna.

Po zakończeniu II wojny światowej świat doświadczył głodu i chaosu. Następnie rozpoczęła się inna wojna – cicha, prowadzona w szpitalach i laboratoriach – wojna z nienarodzonym życiem.

Ta książka jest próbą postawienia pytań, na które nauka boi się dziś odpowiedzieć.


Jedyna słuszna droga BigPharmy – droga wybrukowana przez polskich naukowców

Historia nauki wielokrotnie pokazała, że prawdziwy przełom nie rodzi się w centrach finansowych świata, lecz na jego peryferiach.

Zachodni model farmacji osiągnął granice swojej wydajności. Farmacja stała się narzędziem polityki, rynków kapitałowych i ideologii.

Chiński model, oparty na kopiowaniu zachodnich rozwiązań, nie rozwiązuje problemu – jedynie go replikuje.

Polska stoi w zupełnie innym miejscu historii. Przez wieki była krajem pogranicza: między Wschodem a Zachodem, między wiarą a rozumem, między cierpieniem a nadzieją.

Polscy naukowcy nauczyli się myśleć systemowo. Rozumieć, że nieoznaczoność nie jest błędem nauki, lecz jej fundamentalną cechą. Że życie biologiczne nie jest produktem przemysłowym.

To właśnie polska szkoła myślenia może zaproponować nowy paradygmat BigPharmy: farmację niskoentropową, opartą na etyce, lokalnych rozwiązaniach i szacunku dla życia od poczęcia do naturalnej śmierci.

Jeżeli światowa farmacja ma odzyskać sens, musi spojrzeć na Polskę – nie jak na rynek zbytu, lecz jak na źródło nowego myślenia.

Licencja książki w pełni otwarta (za zgodą??? Sieci Badawczej Łukasiewicz)
technik chemik Rafał Żylak
"""

PHARMA_SVG = """
data:image/svg+xml;utf8,
<svg xmlns='http://www.w3.org/2000/svg' width='300' height='120'>
<rect width='300' height='120' fill='%23161a1d'/>
<g stroke='%2333aa99' stroke-width='4' fill='none'>
<circle cx='60' cy='60' r='30'/>
<line x1='90' y1='60' x2='140' y2='60'/>
<rect x='140' y='45' width='100' height='30' rx='15'/>
</g>
</svg>
"""

class MyHandler(BaseHTTPRequestHandler):

    def send_html(self, html):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def do_GET(self):
        self.render_page()

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(length).decode("utf-8")
        params = parse_qs(data)

        result = ""
        try:
            mass = float(params["mass"][0])
            n = mass / M_WATER
            p = (n * R * T) / V
            result = f"""
            <div class='result'>
            <b>Mole:</b> {n:.4f} mol<br>
            <b>Ciśnienie:</b> {p:.2f} Pa ({p/100:.4f} hPa)
            </div>
            """
        except Exception as e:
            result = f"<div class='result'>Błąd: {e}</div>"

        self.render_page(result)

    def render_page(self, result=""):
        html = f"""
<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<title>BigPharma</title>
<style>
body {{ background:#0f1113; color:#eaeaea; font-family:Arial; margin:0; }}
header {{ text-align:center; padding:40px; }}
.container {{ max-width:1000px; margin:auto; padding:30px; }}
.text {{ white-space:pre-wrap; line-height:1.7; background:#161a1d; padding:30px; }}
.calc {{ margin-top:40px; padding:20px; background:#121517; }}
.result {{ margin-top:15px; padding:15px; background:#1b2024; border-left:4px solid #33aa99; }}
input,button {{ padding:10px; font-size:1em; }}
button {{ background:#33aa99; border:none; cursor:pointer; }}
</style>
</head>
<body>

<header>
<img src="{PHARMA_SVG}">
<h1>BigPharma</h1>
<p>Entropia • Nauka • Sumienie</p>
</header>

<div class="container">
<div class="text">{LONG_TEXT}</div>

<div class="calc">
<h2>Kalkulator ciśnienia pary wodnej</h2>
<form method="POST">
<input type="number" step="any" name="mass" placeholder="masa wody [g]" required>
<button type="submit">Oblicz</button>
</form>
{result}
</div>
</div>

</body>
</html>
"""
        self.send_html(html)

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), MyHandler).serve_forever()
