import json
from datetime import date, timedelta

START = date(2026, 9, 7)  # lunedì S1

def W(n, fase, titolo, blocco, tasks, micro=None, evid=None, stop=None, note=None):
    d = START + timedelta(weeks=n-1)
    return {
        "settimana": n,
        "inizio": d.isoformat(),
        "fine": (d + timedelta(days=6)).isoformat(),
        "fase": fase,
        "titolo": titolo,
        "minuti": blocco,
        "attivita": [{"testo": t, "minuti": m} for t, m in tasks],
        "micro": micro or [],
        "evidenze": evid or [],
        "stop": stop,
        "note": note,
    }

weeks = []

# ---------- SPRINT ----------
weeks.append(W(1, "Sprint", "Fondamenta del second brain e triage", 390, [
    ("Creare `brain/` su cartella sincronizzata; sottocartelle: inbox, fonti, ambiti, progetti, metodo, pipeline, piano. Nessun'altra", 20),
    ("Scrivere `brain/CLAUDE.md`: struttura, convenzioni (un file per cosa, 3 righe di intestazione), cosa l'agente non deve toccare", 40),
    ("Cattura su Mac: scorciatoia che salva testo o link in `inbox/`. Test con 3 cose reali: se servono più di 3 tocchi, semplificare", 40),
    ("Cattura su Android: condivisione verso la stessa cartella. Stesso test", 30),
    ("Versare in `fonti/` due corsi passati completi: struttura, materiali, cosa ha funzionato", 50),
    ("Con Claude Code: comando `/triage` che legge `inbox/`, propone ambito e destinazione per ogni file, sposta solo dopo conferma", 120),
    ("Con Claude Code: comando `/riepilogo` che dice cosa è entrato, dove è finito, cosa resta in inbox", 60),
    ("Provare triage e riepilogo su tutto ciò che hai catturato in settimana; primo commit", 30),
], micro=["Catturare tutto quello che incontri, grezzo, senza organizzare"],
   evid=["auto:commits:brain", "auto:files:brain/inbox", "manuale: screenshot del test di cattura da Android"],
   note="Due sessioni da 3 h (o una da 5-6 nel weekend + una da 60 min). Sessioni sotto le 2 h non contano come sviluppo."))

weeks.append(W(2, "Sprint", "Codificare il metodo", 390, [
    ("Con Claude Code come intervistatore: un documento in `metodo/` per ogni passaggio della catena (analisi fabbisogni → obiettivi → struttura → contenuti → esercizi/valutazione → materiali docente → pacchetto e-learning)", 180),
    ("Per ogni passaggio: cosa entra, cosa esce, criteri di qualità, tono, vincoli (framework competenze, accreditamenti, fondi interprofessionali)", 90),
    ("Scegliere IL passaggio da automatizzare per primo: quello che ti ruba più tempo. Scriverne le specifiche in `pipeline/spec-01.md`: input reale, output atteso, come si giudica", 60),
    ("Misura di partenza: quante ore ti costa oggi quel passaggio su un corso tipo. Scriverlo in `piano/decisioni.md`", 30),
    ("Commit e chiusura settimana nell'app", 30),
], micro=["Cattura in routine", "Triage con `/triage` a fine settimana"],
   evid=["auto:commits:brain", "auto:files:brain/metodo", "manuale: numero di ore di partenza scritto in decisioni.md"],
   stop={"testo": "Hai fatto almeno 10 ore di sprint in S1+S2?", "altrimenti": "Lo sprint diventa di 6 settimane. Nell'app: Impostazioni → sposta tutto di 2 settimane."}))

weeks.append(W(3, "Sprint", "Costruire la prima pipeline", 390, [
    ("Con Claude Code, in `pipeline/`: il passaggio scelto come comando riusabile che legge `metodo/` e i materiali del corso e produce l'output nel formato che usi davvero", 180),
    ("Test sui due corsi passati in `fonti/`: confrontare ciò che avevi prodotto a mano con l'output della pipeline", 90),
    ("Ogni volta che l'output è sbagliato per una ragione che il metodo non diceva: correggere `metodo/`, non il prompt", 90),
    ("Commit e chiusura settimana", 30),
], micro=["Cattura in routine", "Triage a fine settimana"],
   evid=["auto:commits:brain", "auto:commits:pipeline", "manuale: due output della pipeline salvati in progetti/"]))

weeks.append(W(4, "Sprint", "Misura, chiusura, documentazione", 330, [
    ("Usare la pipeline su un corso in lavorazione, se c'è; altrimenti sul terzo corso passato", 120),
    ("Misurare: ore prima, ore dopo, qualità dell'output (correzioni minori / sostanziali), costo in token per corso", 45),
    ("Documentare in `metodo/caso-studio-01.md` cosa è stato costruito e come. È il primo materiale vendibile", 90),
    ("Scrivere la decisione di chiusura sprint in `piano/decisioni.md` con il campo 'cosa la riaprirebbe'", 30),
    ("Creare l'evento ricorrente in agenda per il blocco settimanale e la chiusura (regime ordinario da S5)", 15),
    ("Chiusura settimana", 30),
], micro=["Cattura in routine", "Triage a fine settimana"],
   evid=["auto:commits:brain", "auto:commits:pipeline", "manuale: tabella ore prima/dopo/costo in decisioni.md"],
   stop={"testo": "La prima pipeline ha prodotto, su almeno un corso, un output che avresti usato con correzioni minori e in meno tempo?", "altrimenti": "La Fase 2-bis non si apre a S21. Le settimane 21-32 diventano lavoro sul metodo, non sugli agenti."}))

# ---------- S5-S12: Fase 1 (blocco) + 0-bis (micro) ----------
f1 = {
    5: ("Ricerca e acquisto hardware", 60, [("Verificare prezzi correnti e ordinare: mini-PC N100 (~200 €), box/DAS per i dischi esistenti (~80 €), disco backup (~100 €), microSD 512 GB (~45 €), lettore ottico USB (80-120 €)", 45), ("Prima di ordinare il lettore: verificare che sia compatibile con i formati che vuoi estrarre (DVD/Blu-ray)", 15)], ["manuale: conferme d'ordine (screenshot o riga in log)"]),
    6: ("Preparazione del mini-PC", 45, [("Sistema operativo sul mini-PC, accesso remoto (SSH), Docker", 30), ("Collegare i dischi; creare la struttura `musica/`, `film/`, `backup/`", 15)], ["manuale: output di `docker --version` via SSH"]),
    7: ("Backup prima di tutto", 45, [("Configurare il backup automatico dei dischi esistenti sul disco nuovo. Si fa ADESSO, prima di versarci qualsiasi cosa", 35), ("Verificare che il primo backup sia partito e schedulato", 10)], ["manuale: log del primo backup completato"]),
    8: ("Navidrome", 60, [("Installare Navidrome in Docker, puntarlo su `musica/`", 25), ("Indicizzazione e test di riproduzione da browser", 20), ("Revisione costi abbonamenti: con 4 settimane di consumo reale, il piano aziendale è dimensionato bene? Scrivere la risposta in decisioni.md", 15)], ["manuale: screenshot Navidrome con almeno 1 album", "manuale: riga in decisioni.md sugli abbonamenti"]),
    9: ("Sincronizzazione con il FiiO JM21", 60, [("Installare Symfonium sul JM21 e collegarlo a Navidrome", 15), ("Primo caricamento massivo: microSD nel lettore di schede sul Mac, NON via cavo USB (il JM21 è USB 2.0)", 25), ("Configurare download selettivo e verificare l'aggiornamento incrementale via Wi-Fi", 20)], ["manuale: foto del JM21 che riproduce dalla libreria"]),
    10: ("Jellyfin e TV", 60, [("Installare Jellyfin in Docker, puntarlo su `film/`", 20), ("Collegarlo alla TV e testare la riproduzione (verificare transcodifica hardware N100)", 40)], ["manuale: riga in log con esito test TV"]),
    11: ("Flusso di ripping", 60, [("Definire il processo per DVD/Blu-ray: software, impostazioni di qualità, convenzione di denominazione. Scriverlo in `brain/ambiti/audio-video/ripping.md`", 40), ("Nota legale: in Italia la copia privata è ammessa, l'aggiramento delle protezioni è area grigia. Informarsi e annotare la posizione scelta", 20)], ["auto:files:brain/ambiti", "manuale: file ripping.md presente"]),
    12: ("Verifica del flusso e chiusura fase", 60, [("Prima verifica del flusso di ripping sui formati che possiedi (1 CD, 1 DVD)", 40), ("Chiusura Fase 1: cosa resta aperto va in decisioni.md. Seconda verifica abitudine di cattura", 20)], ["manuale: 2 file rippati visibili in Navidrome/Jellyfin"]),
}
for n, (tit, mins, tasks, ev) in f1.items():
    stop = None
    if n == 8:
        stop = {"testo": "Catturi 3-4 cose a settimana senza sforzo e il triage gira senza che tu lo eviti?", "altrimenti": "Semplifica: una sola cartella, niente triage automatico. Seconda verifica a S12."}
    if n == 12:
        stop = {"testo": "Seconda verifica: la cattura regge da 8 settimane?", "altrimenti": "Riduci a una cartella. Il second brain non cresce finché l'abitudine non tiene."}
    weeks.append(W(n, "Fase 1 — Media server", tit, mins, tasks,
        micro=["Cattura in routine + `/triage` a fine settimana", "Un corso passato in più in `fonti/` (obiettivo: 6 a S8)"] if n <= 8 else ["Cattura in routine + `/triage`"],
        evid=ev + ["auto:commits:brain", "auto:files:brain/inbox"], stop=stop))

# ---------- S13-S20: F1 corso ----------
for n in range(13, 21):
    i = n - 12
    tasks = [(f"Corso agentic AI (deeplearning.ai), tappa {i} di 8: seguire le lezioni della settimana", 60),
             ("Una sola nota in `fonti/corso-agentic/` per la settimana: cosa ho imparato, come si applica alla mia catena di produzione", 15)]
    if n >= 18:
        tasks.append(("Iniziare/completare `metodo/architettura-pipeline-2-3.md`: cosa ha insegnato la prima pipeline, come progettare le due successive", 15))
    stop = {"testo": "Esiste il progetto scritto delle pipeline 2 e 3 in metodo/?", "altrimenti": "La Fase 2-bis non parte a S21: la settimana 21 diventa scrittura del progetto."} if n == 20 else None
    weeks.append(W(n, "F1 — Corso agentic AI", f"Corso agentic AI, settimana {i} di 8", 90 if n >= 18 else 75, tasks,
        micro=["Cattura + `/triage`", "Ripping CD a ritmo libero (Fase 1-bis)", "Acquisti CD usati / Bandcamp"],
        evid=["auto:commits:brain", "auto:files:brain/fonti"], stop=stop))

# ---------- S21-S32: Fase 2-bis ciclo quindicinale ----------
cycles = {
    21: ("A", "Seconda pipeline: specifiche e scaffold", [("Con Claude Code: il passaggio adiacente al primo. Specifiche in `pipeline/spec-02.md`, scaffold del comando", 120), ("Primo test grezzo sui corsi passati", 30)]),
    22: ("B", "Corso MCP + test", [("Claude Academy: corso su MCP / connessione a fonti dati (prima metà)", 45), ("Test della pipeline 2 su un corso passato, annotare gli errori", 15)]),
    23: ("A", "Seconda pipeline: costruzione", [("Costruzione completa della pipeline 2, test sui corsi passati", 120), ("Correggere `metodo/` dove l'output sbaglia per cause non scritte", 30)]),
    24: ("B", "Corso MCP + test", [("Claude Academy: corso MCP (seconda metà)", 45), ("Test pipeline 2, annotare", 15)]),
    25: ("A", "Le due pipeline si passano l'output", [("Pipeline 1 → pipeline 2 in sequenza su un corso intero", 120), ("Messa a regime, documentazione in `pipeline/README.md`", 30)]),
    26: ("B", "Misura", [("Ore prima/dopo e costo per corso con due pipeline. Tabella in decisioni.md", 60)]),
    27: ("A", "Terza pipeline o irrobustimento", [("Decisione in base a S26: terza pipeline (passaggio successivo) oppure irrobustire le due esistenti. Scriverla in decisioni.md e iniziare", 150)]),
    28: ("B", "Revisione abbonamenti + corso", [("Revisione abbonamenti (mese 7): con i costi per corso di due pipeline, il piano alto è ancora giustificato? Quanto è volume spostabile in locale? Scrivere in decisioni.md", 30), ("Claude Academy: il corso più utile secondo l'esperienza (prima metà)", 30)]),
    29: ("A", "Costruzione", [("Costruzione della terza pipeline o dell'irrobustimento deciso a S27", 150)]),
    30: ("B", "Corso + test", [("Claude Academy: corso scelto (seconda metà)", 45), ("Test, annotare", 15)]),
    31: ("A", "Consolidamento e documentazione", [("Consolidamento delle pipeline; documentazione completa in `metodo/`", 150)]),
    32: ("B", "Chiusura fase e caso studio", [("Scrivere `metodo/caso-studio-02.md`: la catena a 2-3 passaggi, numeri, cosa venderesti", 60)]),
}
for n, (tipo, tit, tasks) in cycles.items():
    stop = {"testo": "La seconda pipeline ha risparmiato tempo misurabile?", "altrimenti": "Il ciclo 4 non costruisce la terza: S27-S31 tornano al metodo."} if n == 26 else None
    if n == 28:
        stop = {"testo": "Il carico giustifica ancora il piano alto?", "altrimenti": "Rivedi l'abbonamento e anticipa la Fase 3 a S29 nelle settimane B."}
    mins = 150 if tipo == "A" else 60
    weeks.append(W(n, "Fase 2-bis — Pipeline 2 e 3", f"Settimana {tipo}: {tit}", mins, tasks,
        micro=["Cattura + `/triage`", "Ripping CD"],
        evid=["auto:commits:pipeline", "auto:commits:brain"] if tipo == "A" else ["auto:commits:brain", "manuale: nota corso in fonti/"],
        stop=stop,
        note="Settimana A: un solo blocco da 2,5 h con Claude Code. Se non può essere di 2,5 h, salta il ciclo, non frazionare." if tipo == "A" else "Settimana B: 60 min, niente sviluppo."))

# ---------- S33-S40: Fase 3 ----------
f3 = {
    33: ("Locale sul Mac: installazione", [("Ollama o LM Studio sul MacBook 32 GB; scaricare un 7-14B e un ~32B quantizzato", 30), ("Primo test: triage dell'inbox con il modello locale", 30)]),
    34: ("Locale: migrare il triage", [("Riscrivere `/triage` per usare il modello locale; confrontare qualità con il livello alto su 20 file", 60)]),
    35: ("Locale: riassunti e trascrizioni", [("Riassunti dell'inbox e trascrizione dei video salvati in locale (whisper + modello)", 60)]),
    36: ("Locale: specifica d'acquisto + verifica libreria", [("Annotare in `progetti/macchina-domestica.md`: quali modelli usi davvero, quanta memoria, quante volte a settimana. È la specifica della 3-bis", 30), ("Verifica libreria musicale: quanti album in Navidrome? Decisione certificazione (F3): serve a te o alla società? Scrivere in decisioni.md", 30)]),
    37: ("Router a consumo: setup", [("Configurare OpenRouter (o equivalente). TETTI DI SPESA prima di collegare qualsiasi workflow", 60)]),
    38: ("Router: collegare il livello intermedio", [("Instradare i compiti intermedi delle pipeline sul router; verificare qualità", 60)]),
    39: ("Router: misura", [("Costo reale per corso con i tre livelli. Tabella in decisioni.md", 60)]),
    40: ("Chiusura Fase 3", [("Il volume gira in locale? Il router copre l'intermedio? Scrivere in decisioni.md e preparare la decisione 3-bis", 60)]),
}
for n, (tit, tasks) in f3.items():
    stop = None
    if n == 36:
        stop = {"testo": "La libreria musicale supera i 30 album?", "altrimenti": "Il server è finito così com'è. Il budget musica si libera per la decisione di S48."}
    if n == 40:
        stop = {"testo": "Triage e riassunti girano in locale senza che tu torni al livello alto per insofferenza?", "altrimenti": "Annota se è un problema di modello (→ 3-bis ha senso) o di flusso (→ 3-bis non lo risolve)."}
    weeks.append(W(n, "Fase 3 — Modelli locali e routing", tit, 60, tasks,
        micro=["Cattura + `/triage` (ora in locale)", "Ripping CD"],
        evid=["auto:commits:brain", "auto:commits:pipeline"], stop=stop))

# ---------- S41-S52: 3-bis (condizionata) + Fase 4 ----------
for n in range(41, 53):
    if n == 41:
        tasks = [("PRIMA di guardare listini: scrivere in decisioni.md quale criterio di apertura vale (MacBook insufficiente su dati reali / dati clienti che non possono uscire / occasione dimostrativa già identificata). Se nessuno vale: fase chiusa, budget resta", 60)]
        tit = "Decisione di apertura 3-bis"
        stop = {"testo": "Vale almeno un criterio di apertura della macchina domestica?", "altrimenti": "Fase chiusa. Le settimane 42-47 diventano mantenimento: solo micro-momenti."}
    elif 42 <= n <= 44:
        tasks = [("(Solo se 3-bis aperta) Requisiti reali dalla Fase 3: modelli, memoria, frequenza. Fascia: 1.500-2.000 € fino a 32B; 2.500-3.500 € per 70B", 60)]
        tit = "Requisiti macchina domestica"
        stop = None
    elif 45 <= n <= 47:
        tasks = [("(Solo se 3-bis aperta) Scelta configurazione e acquisto. Ricordare: non è un risparmio, contando l'ammortamento costa più di un'API", 60)]
        tit = "Scelta e acquisto"
        stop = None
    elif n == 48:
        tasks = [("Decisione PC gaming su due dati: quanto hai giocato davvero in 12 mesi, quanto resta del budget personale (riserva 350-650 €; di più solo se la libreria si è fermata a S36). Console, handheld, PC, o niente. Scrivere in decisioni.md", 60), ("(Se 3-bis aperta) Ordine della macchina", 30)]
        tit = "Decisione PC gaming"
        stop = {"testo": "Hai giocato abbastanza e resta budget?", "altrimenti": "Console, handheld, o niente. Non un PC da 1.200 €."}
    elif 49 <= n <= 51:
        tasks = [("(Solo se 3-bis aperta) Messa in opera, migrazione dei carichi locali dal MacBook", 60)]
        tit = "Messa in opera macchina domestica"
        stop = None
    else:
        tasks = [("Revisione annuale (45 min): rileggere il piano intero, cosa è caduto e perché, premesse ancora valide?", 45), ("Scrivere il piano dell'anno 2 in piano/", 45)]
        tit = "Chiusura anno e piano anno 2"
        stop = None
    weeks.append(W(n, "Fase 3-bis / Fase 4", tit, 60 if n != 52 else 90, tasks,
        micro=["Cattura + `/triage`", "Ripping CD"],
        evid=["auto:commits:brain", "manuale: riga in decisioni.md"], stop=stop))

weeks.sort(key=lambda w: w["settimana"])
assert [w["settimana"] for w in weeks] == list(range(1, 53))

piano = {
    "titolo": "Piano progetti personali — 12 mesi (v2)",
    "inizio": START.isoformat(),
    "versione": "2.0",
    "capienza_minuti_settimana": {"sprint": 390, "ordinario": 105},
    "fasi": [
        {"nome": "Sprint", "settimane": [1, 4]},
        {"nome": "Fase 1 — Media server", "settimane": [5, 12]},
        {"nome": "F1 — Corso agentic AI", "settimane": [13, 20]},
        {"nome": "Fase 2-bis — Pipeline 2 e 3", "settimane": [21, 32]},
        {"nome": "Fase 3 — Modelli locali e routing", "settimane": [33, 40]},
        {"nome": "Fase 3-bis / Fase 4", "settimane": [41, 52]},
    ],
    "settimane": weeks,
}
json.dump(piano, open("piano.json", "w"), ensure_ascii=False, indent=2)
print(len(weeks), "settimane;", sum(w["minuti"] for w in weeks)/60, "ore totali")
