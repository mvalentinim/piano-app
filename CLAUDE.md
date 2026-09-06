# piano-app — istruzioni per Claude Code

App statica (GitHub Pages) che mostra ogni settimana cosa fare, quanto tempo bloccare, quali evidenze raccogliere, e scrive il log a fine settimana.

## Principio
Il valore sta nei file, non nell'app. `piano.json`, `stato.json`, `log.md`, `decisioni.md` sono la verità. L'app li legge e li scrive via GitHub Contents API. Se l'app sparisce, i file restano leggibili.

## File
- `index.html` — tutta l'app (HTML+CSS+JS, nessuna build, nessuna dipendenza oltre al font).
- `piano.json` — 52 settimane. Generato da `gen.py`; **modifica gen.py, non il JSON a mano**, poi `python3 gen.py`.
- `stato.json` — offset del calendario, chiusure settimanali, spunte. Scritto dall'app.
- `log.md` — appeso dall'app a ogni chiusura.
- `decisioni.md` — scritto a mano (o con Claude Code), mai dall'app.

## Schema di una settimana in piano.json
`settimana, inizio, fine, fase, titolo, minuti, attivita[{testo,minuti}], micro[], evidenze[], stop{testo,altrimenti}|null, note|null`

Evidenze: `auto:commits:brain|pipeline`, `auto:files:brain/<cartella>`, `manuale: <testo>`.

## Regole
- Mobile first, una colonna, max 640px. Niente framework.
- Non introdurre un database, un backend o localStorage per i dati del piano: solo token e impostazioni stanno in localStorage.
- Ogni modifica al piano passa da gen.py e produce un commit con messaggio "piano: …".
- Le settimane si spostano solo con `offset`, mai rinumerando.
- Se una feature richiede più di una sessione, non è per questa app: va in `decisioni.md` come idea.

## Prossime iterazioni possibili (in ordine di utilità)
1. Notifica il giorno della chiusura: GitHub Action schedulata che apre una issue "Chiudi la settimana N" (le issue arrivano via mail e app GitHub sul telefono).
2. Evidenza Navidrome: conteggio album via API, solo quando il server è raggiungibile (S36).
3. Pagina "piano intero": tabella delle 52 settimane con stato.
4. Pulsante "prepara il blocco": genera il prompt di apertura per Claude Code con il contesto della settimana.
