import random, locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, "de_DE.UTF-8")  # oder "de_DE" unter Windows   


ReaktionenTermine = [                                                           # Reaktionen auf Termine
    "Sieh an, es ist wach.",
    "So schnüre er die Pantoffeln, es ist Zeit für Arbeit.",
    "Ernsthaft, jemand will sich mit dir unterhalten?",
    "",         ]

ReaktionenWetterSonne = [                                                       # Reaktionen auf Sonne
    "Strahlender Sonnenschein. Ekelerregend",
    "Kein wölkchen am Himmel, man möchte weinen.",
    "",
    "",         ]

ReaktionenWetterRegen = [                                                       # Reaktionen auf Wetter
    "Strömender Regen, das richtige für einen Spaziergang. Nackt, und ohne Regenschirm",
    "",
    "",         ]

ReaktionenPollen = [                                                            # Reaktionen auf Pollenflug
    "Atmen wird ohnehin überbewertet.",
    "Ich wette, du hättest jetzt gern deine Medikamente.",
    "Lass das Nasenspray hier, dann hab ich bald Ruhe vor dir.",
                    ]

ReaktionenZeit = {                                                              # Reaktionen auf Uhrzeit
    "vor9": [
        "Solange es genug Kaffee gibt, wird niemand verletzt.",
        "Aus dem Bett gefallen, oder vom Erdbeben rausgeschaukelt?",
        "So früh und schon wach? Bemerkenswert... irgendwie.",
        "Hier geht's lang zum Kaffee.",
        #"",
                    ],

    "ab9": [
        "So früh und schon wach? Bemerkenswert... irgendwie.",
        "Hier geht's lang zum Kaffee.",
        "Tu nicht so, als würdest du schon arbeiten wollen.",
        #"",
                    ],

    "ab10": [
        "Na, hast du schon Hunger?",
        "Wo bleibt denn das zweite Frühstück?!",
        "Frühstück? Oder Simulation von Aktivität?",
        #"",
                    ],
        
    "ab11": [
        "Nicht mehr lange bis zur unverdienten Pause.",
        "Tschakka, du schaffst das (hoffentlich).",
        #"",
                    ],

    "ab12": [
        "Zeit für den zweiten Gang.",
        "'n gud'n!",
        "Du verfressenes etwas....",
        "*PINNG*, Essen ist fertig!",
        "Übertreib's nicht schon wieder.",
        "Die heiße Schlacht um's kalte Buffet.",
        #"",
                    ],

    "ab13": [
        "Das Fresskoma in seiner vollen Pracht.",
        "Bitte schlafen sie JETZT!",
        "",
                    ],

    "ab14": [
        "Der Nachmittag zieht sich wie Kaugummi...",
        "Ab welcher Uhrzeit ist es keine Arbeitsverweigerung mehr?",
        "Feierabend in Sichtweite!",
        #"",
                    ],
    
    "ab15": [
        "Tschakka, du schaffst das (hoffentlich).",
        "Gib's zu: Lust hast du keine mehr.",
                    ],
    
    "ab16": [
        "Bald geschafft – oder zumindest fast nicht völlig gescheitert.",
        "Kein Bier vor 4. Irgendwo ist bestimmt schon 4",
        #"",
                    ],
    
    "ab17": [
        "Das Wochenende ist in Sichtweite.",
        "Feierabend. Die Legende verlässt das Gelände.",
        #"",
                    ],

    "ab18": [
        "Hast du kein zuhause?",
        "Du bist ja immer noch hier.",
        "Hörst du das? Das ist der Lockruf der Couch.",
        #"",
                    ],

    "ab19": [
        #"",
                    ],
    
    "ab20": [
        #"",
                    ],

    "sonst": [
        "Was du jetzt wohl tun solltest? Irgendwas mit Sinn?",
        "Zeit vergeht. Leistung leider nicht.",
        "Ich beobachte. Und beurteile.",
        "Nur noch ein paar Stunden bis zur Sinnkrise.",
        "Mal wieder nur Unsinn im Sinn?",
        #"",
                    ]
}

ReaktionenWochentag = {                                                         # Reaktionen auf Wochentag
    "Montag": [
        "Montag. Und keiner hat dich vermisst.",
        "Montag. Das Elend hat einen neuen Namen.",
        "War das ein mimimi?",
        "Was wir heute tun? Das gleiche wie jeden Tag: Versuchen, die Weltherrschaft an uns zu reißen",
                    ],

    "Dienstag": [
        "Dienstag: das schwarze Schaf unter den Wochentagen.",
        "Schon wieder....",
        "Was wir heute tun? Das gleiche wie jeden Tag: Versuchen, die Weltherrschaft an uns zu reißen",
                    ],

    "Mittwoch": [
        "Bergfest! Nur noch nicht mehr lange bis zur Erschöpfungspause.",
        "Wochenhalbzeit.",
        "Es geht stramm auf's Wochenende zu.",
        "Was wir heute tun? Das gleiche wie jeden Tag: Versuchen, die Weltherrschaft an uns zu reißen",
        "Was, erst Mittwoch?",
                    ],

    "Donnerstag": [
        "Donnerstag. Der kleine Freitag für Optimisten.",
        "Das Wochenende ist schon fast in Sichtweite.",
        "Was wir heute tun? Das gleiche wie jeden Tag: Versuchen, die Weltherrschaft an uns zu reißen",
        "",
                    ],

    "Freitag": [
        "Freitag. Die Illusion von Freiheit.",
        "Freitag... Wo zum Henker steckt Freitag?",
        "Man kann das Wochenende schon riechen.",
        "Was wir heute tun? Das gleiche wie jeden Tag: Versuchen, die Weltherrschaft an uns zu reißen",
        "",
                    ],

    "Samstag": [
        "Samstag. Du hast Zeit. Und trotzdem keine Lust.",
        "Was wir heute tun? Das gleiche wie jeden Tag: Versuchen, die Weltherrschaft an uns zu reißen",
        "",
                    ],

    "Sonntag": [
        "Sonntag. Morgen ist wieder alles vorbei.",
        "Was wir heute tun? Das gleiche wie jeden Tag: Versuchen, die Weltherrschaft an uns zu reißen",
        "",
                    ]
}
  
Endungen = {                                                                    # Reaktionen auf Interaktion
    "Gut": [
    "",
    "",         ],

    "Schlecht":[
    "Abstoßend, ist es nicht?",
    "Ekelhaft.",
    "Widerwärtig.",
    "Wie hast du das denn schon wieder geschafft?",
    "",
    "",         ],

    "Neutral":[
    "Aber wen kümmert das schon?",
    "",
                ]}

Beleidigungen = [                                                               # Braucht das noch eine Erklärung?
    "Man möchte brechen.",
    "Ruhm ist leider nicht alles.",
    "Tu wenigstens einmal etwas nützliches und geh spazieren.",
    "Selbst eine Scheibe Toast ist produktiver als du.",
    "Ich sehe, du hast ein Wettrennen mit der Intelligenz. Wer gewinnt?",
    "Erbärmlich.",
    "Fünf Punkte Abzug für Gryffindor – für unerträgliche Besserwisserei.",
    "Dabeisein auch etwas wert.",
    "Ein Trauerspiel....",
    "Nun denn, auf dass euer Bestes genug sein möge.",
    "Schade um den Aufwand.",
    "Warum bist du überhaupt noch hier?",
    "Oh toll, du schon wieder.",
    "Selbst der Ladebalken langweilt sich.",
    "Nicht mal hier hat man seine Ruhe.",
    "Hast du wirklich geglaubt, das funktioniert?",
    "",
    "",         ]


# Funktionsbibliothek für Hauptroutine
def Wochentag():
    print(random.choice(ReaktionenWochentag[datetime.now().strftime("%A")]))
