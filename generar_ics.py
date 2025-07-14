import csv
from datetime import datetime

# Leer el archivo CSV
with open('feriados.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    events = list(reader)

lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "CALSCALE:GREGORIAN", "X-WR-CALNAME:Feriados Perú 2025"]

for event in events:
    fecha = datetime.strptime(event['fecha'], "%Y-%m-%d").strftime("%Y%m%d")
    nombre = event['nombre']
    lines.extend([
        "BEGIN:VEVENT",
        f"SUMMARY:{nombre}",
        f"DTSTART;VALUE=DATE:{fecha}",
        f"DTEND;VALUE=DATE:{fecha}",
        "END:VEVENT"
    ])

lines.append("END:VCALENDAR")

with open('Feriados_Peru_2025_Nombrado.ics', 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))
