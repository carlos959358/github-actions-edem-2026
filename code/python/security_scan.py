import re
from pathlib import Path

print("🔍 Ejecutando escaneo de seguridad (simulado)...")

patterns = [
    r'AKIA[0-9A-Z]{16}',        # AWS
    r'sk_live_[0-9a-zA-Z]{24}', # Stripe
    r'AIza[0-9A-Za-z_-]{35}'    # Google
]

found = False

for file in Path(".").rglob("*"):
    if file.is_file() and file.suffix in {".json", ".py", ".env", ".txt"}:
        try:
            content = file.read_text(errors="ignore")
            for pattern in patterns:
                if re.search(pattern, content):
                    print(f"⚠️ Posible clave API encontrada en {file}")
                    found = True
        except Exception:
            pass

if not found:
    print("✅ No se encontraron claves API expuestas")
