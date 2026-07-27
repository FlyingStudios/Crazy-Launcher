import sys #Importiert wichtige Bibiotheken
#Hier bricht es
from steam import games
from window import MainWindow
from PySide6.QtWidgets import QApplication
import os

def load_stylesheet(path):
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, path)

    with open(full_path, "r") as file:
        return file.read()

app = QApplication(sys.argv) #Eine abkürzung für einen Befehl
app.setStyleSheet(load_stylesheet("ui/style.qss")) #Lädt die stylesheet datei


window = MainWindow(games)

window.show() #Zeigt das Fenster

sys.exit(app.exec()) #Sorgt dafür das das Fenster nicht direkt zugeht