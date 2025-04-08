import tkinter as tk
import random
from time import strftime
import quotes  # Hier importieren wir die Zitate aus der Datei 'quotes.py'

# Funktion, um die Uhrzeit zu aktualisieren
def time():
    time = strftime('%H:%M')  # Format für Stunden, Minuten, Sekunden
    date = strftime('%d.%m.%Y')  # Format für Stunden, Minuten, Sekunden
    label_time.config(text=str(time))  # Zeigt die Zeit im Label an
    label_time.config(text=str(date))  # Zeigt das Datum im Label an
    label_time.after(60000, time)  # Ruft sich alle 1000ms selbst auf (jede Sekunde)

def date():
    date = strftime('%d.%m.%Y')  # Format für Stunden, Minuten, Sekunden
    label_time.config(text=str(date))  # Zeigt das Datum im Label an
    label_time.after(60000, time)  # Ruft sich alle 1000ms selbst auf (jede Sekunde)

# Funktion, um ein neues Zitat anzuzeigen
def new_quote():
    quote = random.choice(quotes.quotes)  # Wählt zufällig ein Zitat aus der Liste
    label_quote.config(text=quote)  # Zeigt das Zitat im Label an

# Erstelle das Hauptfenster
root = tk.Tk()
root.title("G.R.A.I.L.")  # Titel des Fensters

# Fenstergröße und Layout
root.geometry("400x600")
root.config(bg="grey")

# Uhrzeit
label_time = tk.Label(root, font=("Helvetica", 24), fg="white", bg="grey")
label_time.pack(pady=20)

# Datum
label_date = tk.Label(root, font=("Helvetica", 24), fg="white", bg="grey")
label_date.pack(pady=20)

# Zitat-Label
label_quote = tk.Label(root, font=("Helvetica", 14), fg="white", bg="grey", wraplength=350)
label_quote.pack(pady=20)

# Button, um ein neues Zitat zu bekommen
button_new_quote = tk.Button(root, text="Neues Zitat", font=("Helvetica", 12), command=new_quote)
button_new_quote.pack(pady=10)

# Initialisiere die Uhrzeit
time()

# Initialisiere ein zufälliges Zitat
new_quote()

# Starte die GUI-Schleife
root.mainloop()
