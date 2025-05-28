#----------------------------------------------------
# G.R.A.I.L.

# G eneric
# R ealistic
# A rtificial
# I ntelligent
# L ifeform

# Letzte Bearbeitung: 24.04.2025
# Version 1.000.0-rc1-cd1
#         1                 = Erste stabile Version
#           000             = keine neuen Funktionen, neue Funktionen = n+1
#               0           = keine Bugfixes oder Patches
#                -rc0/1     = Release candidate
#                    -cd0/1 = design change

# Desktop-widget with following features: 
# - current day in year in calendarweek incl. reaction from list            done
# - current time incl. reaction from list                                   done
# - random quotes, new quote per button                                     done
# - Tabellenanordnung                                                       done
# - timer                                                                   pending
# - Optische Erinnerung an trinken, alle 25 Minuten                         done
# - ...
# rest will follow...
# ----------------------------------------------- 

import tkinter as tk                                                                                            # Import der Module und Funktionen
import random, quotes, locale, Reaktionen, time
from datetime import datetime

locale.setlocale(locale.LC_TIME, "de_DE.UTF-8")                                                                 # Lokale Tagesanzeigen für DE, Globale Einstellung für dieses Script

root = tk.Tk()                                                                                                  # Fenster definieren
root.title("G.R.A.I.L. ~~SANDBOX.grid~~")                                                                       # Titel des Fensters
root.geometry("450x450")                                                                                        # Größe und Position des Fensters
root.config(bg="light gray")                                                                                    # Hintergrundfarbe des Fensters

root.grid_columnconfigure(1, weight=2)
root.grid_rowconfigure(1, weight=0)

timer_intervall = 1500  # z.B. 1 Stunde = 3600 Sekunden
timer_restzeit = timer_intervall


def datum():                                                                                                    # Erstellt ein Objekt für das Datum
    label1_datum.config(text=str(f"Tag: " + datetime.now().strftime("%j")+" KW: "+ datetime.now().strftime("%V.%Y")))   # Formatierung: laufender Tag in KW in Jahr
    label2_datum.config(text=str(datetime.now().strftime("%A, %d.%m.%Y")))                                      # Tagesname, Tag, Monat, Jahr

label1_datum = tk.Label(root, font=("Arial", 14, "bold"), fg="black", bg="white", wraplength=400)               # label für Tag# in KW.Jahr
label1_datum.grid(row=1,column=1,padx=15,pady=5, sticky="nsew")
label2_datum = tk.Label(root, font=("Arial", 14, "bold"), fg="black", bg="white", wraplength=400)               # label für das Tagesdatum
label2_datum.grid(row=2,column=1,padx=15,pady=5, sticky="nsew")

def tagesreaktion():                                                                                            # Reagiert mit einem Kommentar auf den aktuellen Tag
    heute = datetime.now().strftime("%A")
    reaktion = random.choice(Reaktionen.ReaktionenWochentag.get(heute, ["..."]))
    label_tagesreaktion.config(text=reaktion)
    root.after(900000, tagesreaktion)

label_tagesreaktion = tk.Label(root, font=("Arial", 14), fg="black", bg="white", wraplength=400)                # Erstellt ein Label für Reaktion auf Tag
label_tagesreaktion.grid(row=3,column=1,padx=15,pady=5, sticky="nsew")

def update_time():                                                                                              # Erstellt das Objekt für die Uhrzeit, aktualisiert sich selbst
    aktuelle_Zeit = datetime.now().strftime("%H:%M")
    label_time.config(text= str(f"Es ist " + aktuelle_Zeit + " Uhr."))                                          # Zeigt die Zeit im Label an
    label_time.after(1000, update_time)                                                                         # Ruft sich alle 1000ms selbst auf

label_time = tk.Label(root, font=("Arial", 14, "bold"), fg="black", bg="white", wraplength=400)                 # Erstellt ein Label für die Uhrzeit
label_time.grid(row=4,column=1,padx=15,pady=5, sticky="nsew")

def zeit_reaktion():                                                                                            # Funktionen für Reaktionen auf Uhrzeit
    stunde = datetime.now().hour
    if 7 <= stunde < 9:
        kommentar = random.choice(Reaktionen.ReaktionenZeit["vor9"])
    elif 9 <= stunde < 10:
        kommentar = random.choice(Reaktionen.ReaktionenZeit["ab9"])  
    elif 10 <= stunde < 11:
        kommentar = random.choice(Reaktionen.ReaktionenZeit["ab10"])
    elif 11 <= stunde < 12:
        kommentar = random.choice(Reaktionen.ReaktionenZeit["ab11"])
    elif 12 <= stunde < 13:
        kommentar = random.choice(Reaktionen.ReaktionenZeit["ab12"])
    elif 13 <= stunde < 14:
        kommentar = random.choice(Reaktionen.ReaktionenZeit["ab13"])
    elif 14 <= stunde < 15:
        kommentar = random.choice(Reaktionen.ReaktionenZeit["ab14"])
    elif 15 <= stunde < 16:
        kommentar = random.choice(Reaktionen.ReaktionenZeit["ab15"])
    elif 16 <= stunde < 17:
        kommentar = random.choice(Reaktionen.ReaktionenZeit["ab16"])
    elif 17 <= stunde < 18:
        kommentar = random.choice(Reaktionen.ReaktionenZeit["ab17"])
    elif 18 <= stunde < 19:
        kommentar = random.choice(Reaktionen.ReaktionenZeit["ab18"])
    elif 19 <= stunde < 20:
        kommentar = random.choice(Reaktionen.ReaktionenZeit["ab19"])
    elif 20 <= stunde < 22:
        kommentar = random.choice(Reaktionen.ReaktionenZeit["ab20"])
    else:
        kommentar = random.choice(Reaktionen.ReaktionenZeit["sonst"])

    label_zeit_reaktion.config(text=kommentar)
    root.after(600000, zeit_reaktion)                                                                           # aktualisiert die Rekation alle 10 Minuten

label_zeit_reaktion = tk.Label(root, font=("Arial", 14), fg="black", bg="white", wraplength=400)                # Erstellt ein Label für Reaktion auf Uhrzeit
label_zeit_reaktion.grid(row=5,column=1,padx=15,pady=5, sticky="nsew")

def new_quote():                                                                                                # Funktion, um ein neues Zitat anzuzeigen
    neues_zitat  = random.choice(quotes.Quotes)                                                                 # Wählt zufällig ein Zitat aus der Liste
    button_quote.config(text=neues_zitat)                                                                       # Zeigt das Zitat im Label an
    root.after(600000, new_quote)

button_quote = tk.Button(root, text=random.choice(quotes.Quotes), font=("Arial", 14, "bold"), bg="white", wraplength=380, command=new_quote)                 # Button, für neues Zitat 
button_quote.grid(row=6,column=1, padx=15,pady=5, sticky="nsew")


def update_trink_timer():
    global timer_restzeit
    if timer_restzeit > 0:
        timer_restzeit -= 1
        label_trink_timer.config(text=f"Trinken in {timer_restzeit // 60} Min", bg="light blue")
    else:
        label_trink_timer.config(text="Trinken!", bg="red")
    root.after(1000, update_trink_timer)

def reset_trink_timer(event=None):
    global timer_restzeit
    timer_restzeit = timer_intervall
    label_trink_timer.config(bg="light blue")

label_trink_timer = tk.Button(root, text="", font=("Courier", 14, "bold"), fg="black", bg="white", width=25)
label_trink_timer.grid(row=7, column=1, padx=15, pady=5, sticky="nsew")
label_trink_timer.bind("<Button-1>", reset_trink_timer)


datum()
tagesreaktion()
update_time()
zeit_reaktion()
new_quote()

update_trink_timer()


root.mainloop()         # Fenster starten
