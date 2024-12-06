import sys
import os

# Füge den absoluten Pfad zu 'App' zur sys.path hinzu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'App')))

# Teste den Import
from models import Base
print("Modul 'app' erfolgreich importiert!")
