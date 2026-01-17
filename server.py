#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

# ===== STAŁE FIZYCZNE =====
M_WATER = 18.0        # g/mol
R = 8.314             # J/(mol*K)
T = 293.15            # K (20°C)
V = 40.0              # m^3 (typowy pokój)

class MyHandler(BaseHTTPRequestHandler):

    def send_html(self, html):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def do_GET(self):
        html = """
<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<title>BigPharma</title>
<style>
body { font-family: Arial; background:#111; color:#eee; text-align:center; }
input, button { font-size: 1.2em; padding: 10px; margin: 10px; }
button { cursor:pointer; }
</style>
</head>
<body>

<h1>BigPharma</h1>
<h3>Kalkulator ciśnienia pary wodnej</h3>

<form method="POST">
    <label>Ilość dostarczonej wody [g]</label><br>
    <input type="number" step="any" name="mass" required><br>
    <button type="submit">OBLICZ</button>
</form>

</body>
</html>
"""
        self.send_html(html)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(length).decode("utf-8")
        params = parse_qs(data)

        try:
            mass_g = float(params["mass"][0])

            n = mass_g / M_WATER
            pressure_pa = (n * R * T) / V

            result = f"""
<ul>
<li>Mole: <b>{n:.4f} mol</b></li>
<li>Ciśnienie: <b>{pressure_pa:.2f} Pa</b></li>
<li>Ciśnienie: <b>{pressure_pa/100:.4f} hPa</b></li>
<li>Ciśnienie: <b>{pressure_pa/1000:.6f} kPa</b></li>
<li>Ciśnienie: <b>{pressure_pa/100000:.8f} bar</b></li>
</ul>
"""

        except Exception as e:
            result = f"<p><b>Błąd:</b> {e}</p>"

        html = f"""
<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<title>BigPharma – wynik</title>
<style>
body {{ font-family: Arial; background:#111; color:#eee; text-align:center; }}
a {{ color:#0af; font-size:1.2em; }}
</style>
</head>
<body>

<h1>WYNIK</h1>

{result}

<br><br>
<a href="/">← Wróć</a>

</body>
</html>
"""
        self.send_html(html)


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), MyHandler)
    print("Serwer działa lokalnie na http://127.0.0.1:8000")
    server.serve_forever()
