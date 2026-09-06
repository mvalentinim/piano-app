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
    ("Sul Mac: clonare il repo `brain` da GitHub in `~/brain` (`git clone`). Dentro, creare le cartelle `inbox/`, `fonti/`, `ambiti/`, `progetti/`, `metodo/`, `pipeline/`, `piano/`, ciascuna con un file `.gitkeep` vuoto. Nessun'altra cartella: se qualcosa non sa dove andare, va in inbox", 15),
    ("Sul Mac: creare `~/brain/CLAUDE.md` (il file che Claude Code legge all'avvio). Contenuto: (1) cosa c'è in ogni cartella, una riga per cartella; (2) convenzione dei file: un file per cosa, prime 3 righe = data, fonte, ambito; (3) cosa non toccare: `pipeline/` e `metodo/` non si spostano mai col triage; (4) lingua: italiano. Massimo 40 righe. Commit", 40),
    ("Cattura da Mac: un'app Scorciatoie che chiede un testo (o prende gli appunti/il link copiato) e lo salva come `~/brain/inbox/AAAA-MM-GG-HHMM.md` con le 3 righe di intestazione. Metterla nella barra dei menu. Test con 3 cose reali: se servono più di 3 tocchi, semplificare", 40),
    ("Cattura da Android: creare in OneDrive la cartella `brain-inbox/` (FUORI dal repo). Condividi → OneDrive → quella cartella: link, screenshot, note vocali. Test con 3 cose reali", 30),
    ("Versare in `~/brain/fonti/` due corsi passati: una sottocartella per corso (`fonti/corso-<nome>/`), dentro i materiali che hai (programma, slide, esercizi, esportati in testo/markdown o PDF) e un file `NOTE.md`: cosa ha funzionato, cosa no, quante ore ti è costato. Commit", 50),
    ("Con Claude Code in `~/brain`: chiedere di creare il comando `/triage` (file `.claude/commands/triage.md`). Deve: (a) spostare i file da `~/OneDrive/brain-inbox/` in `inbox/`; (b) per ogni file in `inbox/` proporre ambito e cartella di destinazione e aggiungere le 3 righe di intestazione se mancano; (c) spostare SOLO dopo la tua conferma; (d) non toccare `metodo/` e `pipeline/`. Provarlo sui file catturati", 120),
    ("Con Claude Code: comando `/riepilogo` (`.claude/commands/riepilogo.md`) che elenca cosa è entrato negli ultimi 7 giorni, dove è finito, cosa resta in inbox, e propone la bozza delle 5 righe di log per l'app", 60),
    ("Commit di tutto. Nell'app: spuntare le attività, minuti effettivi, attrito, chiudere la settimana", 35),
], micro=["Catturare tutto quello che incontri (link, idee, screenshot), grezzo, senza organizzare: sono i dati di test per `/triage`"],
   evid=["auto:commits:brain", "auto:files:brain/inbox", "manuale: screenshot del test di cattura da Android"],
   note="Due sessioni da 3 h (o una da 5-6 nel weekend + una da 60 min). Attività 1-5 nella prima sessione, 6-8 nella seconda. Sessioni sotto le 2 h non contano come sviluppo."))


# ---------- S2 ----------
weeks.append(W(2, "Sprint", "Codificare il metodo", 390, [
    ("Sul Mac, in `~/brain/metodo/`: creare 7 file vuoti, uno per passaggio della catena: `01-analisi-fabbisogni.md`, `02-obiettivi-apprendimento.md`, `03-struttura-curriculum.md`, `04-contenuti-modulo.md`, `05-esercizi-valutazione.md`, `06-materiali-docente.md`, `07-pacchetto-elearning.md`. Ogni file ha 5 titoli fissi: Cosa entra / Cosa esce / Criteri di qualità / Tono e stile / Vincoli", 15),
    ("Con Claude Code in `~/brain`: prompt «Leggi CLAUDE.md e i corsi in fonti/. Per ciascun file in metodo/ fammi domande, una alla volta, finché le 5 sezioni non sono compilate con le mie risposte. Non inventare: se non so rispondere, scrivi TODO». Rispondere a voce alta come faresti a un collaboratore nuovo. Sono ~30 min a passaggio", 200),
    ("Rileggere i 7 file e correggere a mano ciò che Claude ha frainteso. In `Vincoli` devono comparire, dove rilevanti: framework di competenze usati, requisiti di accreditamento, regole dei fondi interprofessionali, formati richiesti dai clienti", 55),
    ("Scegliere IL passaggio da automatizzare per primo: quello che oggi ti costa più ore per corso. Non il più facile. Scriverlo in `~/brain/piano/decisioni.md` come blocco: data, passaggio scelto, perché, cosa la riaprirebbe", 15),
    ("Creare `~/brain/pipeline/spec-01.md` con 4 sezioni: Input (i file reali che il passaggio riceve, con esempio preso da un corso in fonti/), Output atteso (formato esatto: docx? markdown? tabella? con esempio reale), Come si giudica (3-5 criteri verificabili: «tutti gli obiettivi sono misurabili», «ogni modulo ha durata», ecc.), Cosa non deve fare", 60),
    ("Misura di partenza: quante ore ti costa oggi quel passaggio su un corso tipo? Scriverlo in `decisioni.md` sotto la decisione. Senza questo numero a S4 non puoi dire se ha funzionato", 15),
    ("Commit, spunte nell'app, chiusura settimana", 30),
], micro=["Cattura in routine", "`/triage` a fine settimana (poi commit)"],
   evid=["auto:commits:brain", "auto:files:brain/metodo", "manuale: numero di ore di partenza scritto in decisioni.md"],
   stop={"testo": "Hai fatto almeno 10 ore di sprint in S1+S2?", "altrimenti": "Lo sprint diventa di 6 settimane: Impostazioni → spostamento = 2. Non comprimere S3 e S4."},
   note="Prima sessione (3 h): attività 1-3. Seconda sessione (3 h): attività 4-7. È la settimana meno divertente e la più determinante: il salto di qualità della pipeline viene da questi 7 file, non dai prompt."))

# ---------- S3 ----------
weeks.append(W(3, "Sprint", "Costruire la prima pipeline", 390, [
    ("Con Claude Code in `~/brain`: prompt «Leggi CLAUDE.md, metodo/ e pipeline/spec-01.md. Crea il comando `.claude/commands/pipeline-01.md` che, dato il percorso di una cartella corso, produce l'output descritto nella spec nel formato richiesto, salvandolo in `<cartella corso>/output/`. Deve rileggere il file metodo/ corrispondente ogni volta e rispettare i Vincoli». Far generare anche un `pipeline/README.md` con: come si lancia, cosa produce", 90),
    ("Primo test: `/pipeline-01 fonti/corso-<primo>`. Confrontare l'output con ciò che avevi prodotto a mano per quel corso (è in fonti/). Annotare in `pipeline/test-01.md` ogni differenza: giusta, sbagliata, o «il metodo non lo diceva»", 60),
    ("Per ogni riga «il metodo non lo diceva»: aggiungere la regola al file giusto in `metodo/`. NON correggere il prompt del comando. Poi rilanciare. Ripetere finché le differenze sono solo di gusto", 120),
    ("Secondo test sul secondo corso in fonti/. Stesso confronto, stessa tabella in `pipeline/test-01.md`. Se il metodo cambia ancora molto, va bene: è il suo lavoro", 60),
    ("Chiedere a Claude Code: «Quali informazioni ti sono mancate per fare bene questi due corsi?». Le risposte utili vanno in metodo/, le altre in `pipeline/spec-01.md` sezione «Cosa non deve fare»", 30),
    ("Salvare i due output in `progetti/pipeline-01/` (non in fonti/). Commit, chiusura settimana", 30),
], micro=["Cattura in routine", "`/triage` a fine settimana"],
   evid=["auto:commits:brain", "auto:files:brain/pipeline", "manuale: due output della pipeline salvati in progetti/pipeline-01/"],
   note="Prima sessione (3 h): attività 1-3. Seconda sessione (3 h): attività 4-6. Il comando vive in `brain/.claude/commands/`: `pipeline/` contiene spec, test e documentazione."))

# ---------- S4 ----------
weeks.append(W(4, "Sprint", "Misura, chiusura, documentazione", 330, [
    ("Test reale: se hai un corso in lavorazione, creare `progetti/corso-<nome>/` con i materiali di input e lanciare `/pipeline-01` su di esso. Se non c'è, usare un terzo corso passato aggiunto a fonti/. Lavorare l'output come se dovesse essere consegnato: cronometrare il tempo di correzione", 120),
    ("Compilare la tabella in `~/brain/piano/decisioni.md`: ore a mano (misura di S2) / ore con pipeline (correzione cronometrata) / correzioni: minori o sostanziali / costo in token (da `/cost` in Claude Code, o dalla dashboard di consumo) / costo stimato per corso", 45),
    ("Con Claude Code: «Scrivi metodo/caso-studio-01.md per un lettore esterno: il problema, la catena di produzione, cosa è stato automatizzato, i numeri della tabella, cosa ha reso possibile il risultato (il metodo codificato), limiti attuali». Rileggere e correggere: è il primo materiale che potresti mostrare a un cliente", 90),
    ("Decisione di chiusura sprint in `decisioni.md`: la pipeline è usabile con correzioni minori e in meno tempo? Sì → Fase 2-bis confermata per S21. No → S21-S32 tornano al metodo. Compilare «cosa la riaprirebbe»", 30),
    ("In agenda: evento ricorrente settimanale «Blocco» (60-75 min, giorno fisso) e «Chiusura» (10 min, altro giorno) con il link all'app, da S5 in poi. Per S21-S32: 6 blocchi da 2,5 h nelle settimane dispari", 15),
    ("Commit, chiusura settimana nell'app", 30),
], micro=["Cattura in routine", "`/triage` a fine settimana"],
   evid=["auto:commits:brain", "auto:files:brain/metodo", "manuale: tabella ore prima/dopo/costo in decisioni.md", "manuale: eventi ricorrenti creati in agenda"],
   stop={"testo": "La prima pipeline ha prodotto, su almeno un corso, un output che avresti usato con correzioni minori e in meno tempo?", "altrimenti": "La Fase 2-bis non si apre a S21. Le settimane 21-32 diventano lavoro sul metodo, non sugli agenti."},
   note="Prima sessione (3 h): attività 1-2. Seconda sessione (2,5 h): attività 3-6. Da S5 il ritmo cambia: meno di 2 ore a settimana. Non trascinare lo sprint."))

# ---------- S5-S12: Fase 1 ----------
micro_0bis = ["Cattura in routine + `/triage` a fine settimana + commit", "Un corso passato in più in `fonti/corso-<nome>/` con NOTE.md (obiettivo: 6 corsi a S8)"]
micro_f1 = ["Cattura in routine + `/triage` + commit"]

weeks.append(W(5, "Fase 1 — Media server", "Ricerca e acquisto hardware", 60, [
    ("Creare `~/brain/progetti/media-server/` con `acquisti.md`. Cercare e annotare prezzo e link per: mini-PC con Intel N100 e 16 GB RAM (~200 €), box USB o DAS per i dischi che hai già (~80 €; contare quanti dischi e quale interfaccia), disco esterno per backup di capienza ≥ somma dei dischi attuali (~100 €), microSD 512 GB classe A2 (~45 €), lettore ottico USB (80-120 €)", 30),
    ("Prima di ordinare il lettore: decidere se ti servono solo DVD o anche Blu-ray. Per Blu-ray verificare che il modello sia indicato come compatibile con il software di ripping che userai (S11). Annotare la scelta", 10),
    ("Ordinare tutto. Incollare in `acquisti.md` la conferma d'ordine (numero, data, totale). Commit", 20),
], micro=micro_0bis, evid=["auto:commits:brain", "auto:files:brain/inbox", "manuale: acquisti.md con conferme d'ordine"]))

weeks.append(W(6, "Fase 1 — Media server", "Preparazione del mini-PC", 45, [
    ("Sul mini-PC: installare Ubuntu Server (o Debian) da chiavetta USB, utente non-root, SSH abilitato. Dal Mac: `ssh utente@<ip>` deve funzionare. Annotare IP e credenziali in un gestore password, NON in brain/", 25),
    ("Sul mini-PC via SSH: installare Docker (script ufficiale `get.docker.com`) e verificare con `docker run hello-world`. Collegare il box dei dischi, montare i dischi con voce in `/etc/fstab` così ripartono al riavvio. Creare `/srv/media/musica`, `/srv/media/film`, `/srv/backup`", 20),
], micro=micro_0bis, evid=["auto:commits:brain", "manuale: output di `docker --version` via SSH incollato in progetti/media-server/setup.md"]))

weeks.append(W(7, "Fase 1 — Media server", "Backup prima di tutto", 45, [
    ("Collegare il disco di backup. Sul mini-PC: script `/srv/backup/backup.sh` che fa `rsync -a --delete` da `/srv/media/` a `/srv/backup/media/`, con log su file. Provarlo a mano una volta e controllare che i file ci siano", 30),
    ("Schedularlo con cron ogni notte (es. 03:00). Verificare il mattino dopo che il log riporti l'esecuzione. Scrivere in `progetti/media-server/setup.md` come si ripristina un file dal backup: se non sai rispondere in 3 righe, il backup non serve", 15),
], micro=micro_0bis, evid=["auto:commits:brain", "manuale: riga del log del primo backup notturno incollata in setup.md"],
   note="Si fa ADESSO, prima di versare qualsiasi cosa sui dischi. Un backup configurato dopo non si fa mai."))

weeks.append(W(8, "Fase 1 — Media server", "Navidrome e prima revisione costi", 60, [
    ("Sul mini-PC: cartella `/srv/docker/navidrome/` con `docker-compose.yml` (immagine `deluan/navidrome`, porta 4533, volume musica in sola lettura su `/srv/media/musica`, volume dati su `./data`). `docker compose up -d`. Copiare 5-10 album in FLAC che già possiedi in `/srv/media/musica/<Artista>/<Album>/`", 25),
    ("Dal Mac, browser su `http://<ip>:4533`: creare l'utente admin, attendere l'indicizzazione, riprodurre un brano. Aggiungere il compose a `progetti/media-server/setup.md`", 20),
    ("Prima revisione costi (sono passate 4 settimane di consumo reale): aprire la dashboard di consumo del piano Claude aziendale, annotare in `piano/decisioni.md` spesa mensile effettiva, quota dovuta allo sprint, e se il piano attuale è quello giusto per il regime ordinario. Decidere: tenere / scendere / salire", 15),
], micro=micro_0bis, evid=["auto:commits:brain", "auto:files:brain/fonti", "manuale: screenshot Navidrome con almeno 1 album", "manuale: blocco «revisione abbonamenti S8» in decisioni.md"],
   stop={"testo": "Catturi 3-4 cose a settimana senza sforzo e il triage gira senza che tu lo eviti? (conta i file in inbox/ delle ultime 4 settimane)", "altrimenti": "Semplifica: una sola cartella `inbox/`, niente `/triage` automatico, solo cattura. Seconda verifica a S12."}))

weeks.append(W(9, "Fase 1 — Media server", "Sincronizzazione con il FiiO JM21", 60, [
    ("Sul JM21: installare Symfonium dal Play Store (~5 €). Aggiungere un provider Subsonic con l'indirizzo `http://<ip>:4533` e le credenziali Navidrome. Verificare che veda la libreria in Wi-Fi", 15),
    ("Primo caricamento massivo: NON via cavo USB (il JM21 è USB 2.0, lentissimo). Inserire la microSD nel lettore di schede del Mac, copiare la cartella musica, rimettere la scheda nel JM21. In Symfonium: impostare la cache/download sulla microSD", 25),
    ("Sincronizzazione incrementale: in Symfonium attivare il download automatico di ciò che aggiungi ai preferiti o a una playlist «Da scaricare», solo in Wi-Fi. Test: aggiungere un album su Navidrome, verificare che arrivi sul JM21. Annotare il flusso in `setup.md`", 20),
], micro=micro_f1, evid=["auto:commits:brain", "manuale: foto del JM21 che riproduce un album dalla libreria"]))

weeks.append(W(10, "Fase 1 — Media server", "Jellyfin e TV", 60, [
    ("Sul mini-PC: `/srv/docker/jellyfin/docker-compose.yml` (immagine `jellyfin/jellyfin`, porta 8096, volume film su `/srv/media/film`, dispositivo `/dev/dri` passato al container per la transcodifica hardware Intel). `docker compose up -d`. Copiare 1-2 file video di prova", 20),
    ("Browser su `http://<ip>:8096`: configurazione iniziale, libreria «Film» su `/media/film`. In Dashboard → Riproduzione: abilitare transcodifica hardware Intel QuickSync. Sulla TV: installare l'app Jellyfin (o usare il browser della TV), collegare, riprodurre. Verificare nella dashboard che la transcodifica usi l'hardware. Annotare in `setup.md`", 40),
], micro=micro_f1, evid=["auto:commits:brain", "manuale: riga in setup.md con esito del test sulla TV (fluido / a scatti / transcodifica hw sì/no)"]))

weeks.append(W(11, "Fase 1 — Media server", "Flusso di ripping", 60, [
    ("Creare `~/brain/ambiti/audio-video/ripping.md`. CD: software (es. XLD su Mac, o `abcde`/`whipper` su Linux), formato FLAC, tag da MusicBrainz, cartella `<Artista>/<Anno> - <Album>/<NN> - <Titolo>.flac`. DVD/Blu-ray: software scelto (es. MakeMKV per l'estrazione, HandBrake per la compressione), preset (es. H.265 1080p qualità 20), cartella `<Titolo> (<Anno>)/<Titolo>.mkv` (formato che Jellyfin riconosce)", 40),
    ("Nota legale, da scrivere nello stesso file: in Italia la copia privata di supporti che possiedi è ammessa (compenso già incluso nel prezzo dei supporti vergini), ma l'aggiramento delle protezioni anticopia è area grigia. Leggere una fonte affidabile aggiornata, scrivere in 3 righe la posizione che scegli (es. solo supporti che possiedi, nessuna condivisione). Commit", 20),
], micro=micro_f1, evid=["auto:commits:brain", "auto:files:brain/ambiti", "manuale: ripping.md presente con sezione legale compilata"]))

weeks.append(W(12, "Fase 1 — Media server", "Verifica del flusso e chiusura fase", 60, [
    ("Rippare 1 CD e 1 DVD seguendo alla lettera `ripping.md`. Copiare sul mini-PC (`rsync` o SMB). Verificare che compaiano in Navidrome e Jellyfin con copertina e metadati giusti. Cronometrare: quanti minuti di attenzione reale richiede un CD? Annotarlo in ripping.md", 40),
    ("Chiusura Fase 1 in `piano/decisioni.md`: cosa funziona, cosa resta aperto (ognuno con: lo faccio nei micro-momenti / lo lascio), spesa totale vs 550 € previsti. Seconda verifica dell'abitudine di cattura: contare i file entrati in inbox/ nelle 8 settimane", 20),
], micro=micro_f1, evid=["auto:commits:brain", "manuale: 2 supporti rippati visibili in Navidrome/Jellyfin (screenshot)", "manuale: blocco «chiusura Fase 1» in decisioni.md"],
   stop={"testo": "Seconda verifica: la cattura regge da 8 settimane? (file in inbox/ ≥ 3 a settimana in media)", "altrimenti": "Riduci a una cartella e niente automazioni. Il second brain non cresce finché l'abitudine non tiene."}))

# ---------- S13-S20: F1 corso ----------
corso_note = "Il blocco settimanale è il corso. Nessun altro progetto attivo: il media server è in regime, la pipeline gira. Da qui in poi i micro-momenti includono il ripping a ritmo libero."
for n in range(13, 21):
    i = n - 12
    tasks = [
        (f"Corso agentic AI (deeplearning.ai) — tappa {i} di 8: seguire il blocco di lezioni della settimana (dividere il corso rimanente in {9-i} parti uguali e fare la prima). Fare gli esercizi pratici, non solo guardare", 55 if n < 18 else 50),
        (f"Una sola nota: `~/brain/fonti/corso-agentic/{i:02d}-<argomento>.md` con 3 sezioni: Cosa ho imparato (5 righe max), Come si applica alla mia catena di produzione (riferimento esplicito a un file di metodo/ o a una pipeline), Cosa cambierei nella pipeline-01. Commit", 20),
    ]
    if n == 13:
        tasks.insert(0, ("Creare `~/brain/fonti/corso-agentic/` e `progetti/media-server/libreria.md` (album rippati e acquistati, aggiornato nei micro-momenti). Fase 1-bis parte: da ora ripping e acquisti CD usati / Bandcamp a ritmo libero, budget 800-1.000 €", 15))
    if n == 18:
        tasks.append(("Iniziare `~/brain/metodo/architettura-pipeline-2-3.md`: sezione 1 «Cosa ha insegnato pipeline-01» (rileggere pipeline/test-01.md e decisioni.md di S4): errori ricorrenti, dove il metodo era carente, cosa ha funzionato", 20))
    if n == 19:
        tasks.append(("`architettura-pipeline-2-3.md` sezione 2: quale passaggio della catena automatizzare per secondo (quello adiacente a pipeline-01, che ne riceve l'output o glielo fornisce) e per terzo. Per ciascuno: input, output, come si giudica, cosa del corso si applica", 20))
    if n == 20:
        tasks.append(("Completare `architettura-pipeline-2-3.md` sezione 3: come le pipeline si passano l'output (file, cartelle, convenzioni), cosa resta manuale tra un passaggio e l'altro, costo stimato per corso. Rileggere tutto: è il progetto della Fase 2-bis", 25))
    stop = {"testo": "Esiste metodo/architettura-pipeline-2-3.md completo nelle 3 sezioni?", "altrimenti": "La Fase 2-bis non parte a S21: il blocco di S21 diventa scrittura del progetto, e i cicli slittano di 2 settimane (Impostazioni → spostamento)."} if n == 20 else None
    weeks.append(W(n, "F1 — Corso agentic AI", f"Corso agentic AI, tappa {i} di 8" + (" e progetto pipeline 2-3" if n >= 18 else ""), 95 if n == 20 else (90 if n in (13,18,19) else 75), tasks,
        micro=["Cattura + `/triage` + commit", "Ripping CD/DVD (Fase 1-bis), aggiornare libreria.md", "Acquisti CD usati / Bandcamp"],
        evid=["auto:commits:brain", "auto:files:brain/fonti", "manuale: nota della tappa presente in fonti/corso-agentic/"], stop=stop,
        note=corso_note if n == 13 else None))

# ---------- S21-S32: Fase 2-bis ----------
A_note = "Settimana A: un solo blocco da 2,5 h con Claude Code, in agenda già da S4. Se non può essere di 2,5 h, salta il ciclo intero: non frazionare. Prima di iniziare: `git pull`, aprire Claude Code in ~/brain, incollare il prompt indicato."
B_note = "Settimana B: 60 minuti, niente sviluppo. Corso o test o misura."
micro_2 = ["Cattura + `/triage` + commit", "Ripping a ritmo libero"]
cyc = {
 21: ("A", "Seconda pipeline: specifiche e scaffold", [
    ("Creare `pipeline/spec-02.md` copiando la struttura di spec-01 (Input / Output atteso / Come si giudica / Cosa non deve fare), compilata dal passaggio scelto in `metodo/architettura-pipeline-2-3.md`. Input = l'output reale di pipeline-01 (o ciò che pipeline-01 richiede in ingresso)", 40),
    ("Con Claude Code: «Leggi CLAUDE.md, metodo/, pipeline/spec-02.md e .claude/commands/pipeline-01.md. Crea .claude/commands/pipeline-02.md con la stessa struttura. Aggiorna pipeline/README.md». Primo lancio grezzo su un corso in fonti/", 80),
    ("Annotare in `pipeline/test-02.md` le differenze rispetto al lavoro fatto a mano (giusta / sbagliata / il metodo non lo diceva). Commit", 30)]),
 22: ("B", "Corso MCP + test", [
    ("Claude Academy → corso su MCP (connettere Claude a fonti dati): prima metà. Nota in `fonti/claude-academy/mcp-1.md`: quali fonti dati delle mie pipeline potrebbero arrivare via MCP (cartelle cliente, Drive, modelli di documento)", 45),
    ("Lanciare `/pipeline-02` su un secondo corso in fonti/, annotare gli errori in test-02.md. Commit", 15)]),
 23: ("A", "Seconda pipeline: costruzione", [
    ("Per ogni riga «il metodo non lo diceva» in test-02.md: aggiungere la regola al file giusto in metodo/. Rilanciare su entrambi i corsi. Ripetere finché restano solo differenze di gusto", 90),
    ("Con Claude Code: «Quali informazioni ti sono mancate per fare bene pipeline-02?» → metodo/ o spec-02 sezione «Cosa non deve fare»", 30),
    ("Salvare gli output in `progetti/pipeline-02/`. Commit", 30)]),
 24: ("B", "Corso MCP + test", [
    ("Claude Academy → corso MCP, seconda metà. Nota `fonti/claude-academy/mcp-2.md`: decidere se un MCP serve davvero alle pipeline ora, o va rimandato (scriverlo in decisioni.md)", 45),
    ("Test pipeline-02 su un terzo corso. Commit", 15)]),
 25: ("A", "Le due pipeline in sequenza", [
    ("Creare `progetti/corso-test-catena/` con gli input iniziali di un corso. Lanciare pipeline-01 e poi pipeline-02 sull'output della prima (o nell'ordine in cui la catena li prevede). Annotare in `pipeline/test-catena.md` cosa si rompe nel passaggio: formato, nomi file, informazioni perse", 90),
    ("Con Claude Code: sistemare le convenzioni di passaggio (cartella `output/` con nomi fissi, un file `contesto.md` che ogni pipeline aggiorna). Aggiornare pipeline/README.md: come si lancia la catena completa. Commit", 60)]),
 26: ("B", "Misura", [
    ("Tabella in `piano/decisioni.md` «Misura S26»: per passaggio 1 e passaggio 2: ore a mano (S2 + stima per il secondo) / ore con pipeline (cronometrare la correzione dell'ultimo test) / correzioni minori o sostanziali / token per corso / costo per corso. Totale catena", 45),
    ("Decisione scritta: ciclo 4 costruisce la terza pipeline, oppure irrobustisce le due? Criterio: se il passaggio 2 ha risparmiato tempo misurabile → terza; altrimenti → metodo e irrobustimento", 15)]),
 27: ("A", "Terza pipeline o irrobustimento", [
    ("SE terza pipeline: `pipeline/spec-03.md` (30 min) + con Claude Code `.claude/commands/pipeline-03.md` (90 min) + primo test e `pipeline/test-03.md` (30 min). SE irrobustimento: prendere i 5 errori più frequenti in test-01/test-02, correggere metodo/, aggiungere a ogni comando un passo finale di autoverifica sui criteri della spec («Come si giudica»), rilanciare", 150)]),
 28: ("B", "Revisione abbonamenti + corso", [
    ("Revisione abbonamenti (mese 7). Dati: tabella S26 + dashboard consumo. Rispondere in `decisioni.md`: (1) costo mensile reale, (2) quanto del consumo è triage/riassunti/classificazione (volume) e quanto è pipeline (difficoltà), (3) il piano alto è giustificato dal solo lavoro di difficoltà? (4) cosa sposterei in locale a S33", 30),
    ("Claude Academy → il corso più utile secondo ciò che hai incontrato (scegliere in base agli attriti del log): prima metà. Nota in `fonti/claude-academy/`", 30)]),
 29: ("A", "Costruzione", [
    ("Continuare ciò che è stato deciso a S26/S27: costruzione della terza pipeline (correzione del metodo, test su 2-3 corsi, come per pipeline-02) oppure irrobustimento. Output in `progetti/pipeline-03/` o aggiornamento dei test. Commit", 150)]),
 30: ("B", "Corso + test", [
    ("Claude Academy → corso scelto, seconda metà. Nota", 45),
    ("Test della catena completa su un corso nuovo. Annotare. Commit", 15)]),
 31: ("A", "Consolidamento e documentazione", [
    ("Rileggere tutti i file di metodo/ dall'inizio: sono coerenti tra loro dopo 3 mesi di correzioni? Con Claude Code: «Trova contraddizioni e duplicati tra i file di metodo/» e risolverle", 60),
    ("`pipeline/README.md` definitivo: prerequisiti, come si lancia ogni comando e la catena, dove finiscono gli output, cosa resta manuale, costo per corso. Deve poterlo seguire un collaboratore. Commit", 90)]),
 32: ("B", "Chiusura fase e caso studio", [
    ("Con Claude Code: «Scrivi metodo/caso-studio-02.md per un lettore esterno: la catena a 2-3 passaggi, i numeri della misura S26 aggiornati, cosa ha reso possibile il risultato, cosa venderesti come servizio». Rileggere. Chiusura Fase 2-bis in decisioni.md con «cosa la riaprirebbe». Commit", 60)]),
}
for n, (tipo, tit, tasks) in cyc.items():
    stop = None
    if n == 26: stop = {"testo": "La seconda pipeline ha risparmiato tempo misurabile (tabella S26)?", "altrimenti": "Il ciclo 4 non costruisce la terza: S27-S31 tornano al metodo e all'irrobustimento."}
    if n == 28: stop = {"testo": "Il carico di lavoro «di difficoltà» giustifica ancora da solo il piano alto?", "altrimenti": "Rivedi l'abbonamento ora. Anticipa la Fase 3: usa le settimane B (S30, S32) per installare Ollama sul Mac."}
    weeks.append(W(n, "Fase 2-bis — Pipeline 2 e 3", f"Settimana {tipo}: {tit}", 150 if tipo=="A" else 60, tasks,
        micro=micro_2,
        evid=["auto:commits:brain", "auto:files:brain/pipeline", "manuale: test-0N.md o output aggiornati"] if tipo=="A" else ["auto:commits:brain", "auto:files:brain/fonti", "manuale: nota corso o tabella in decisioni.md"],
        stop=stop, note=A_note if n == 21 else (B_note if n == 22 else None)))

# ---------- S33-S40: Fase 3 ----------
f3 = {
 33: ("Locale sul Mac: installazione", [
    ("Sul Mac: installare Ollama (`brew install ollama` o dal sito) e avviarlo. Scaricare un modello 7-14B per compiti veloci (es. `ollama pull` di un Qwen o Llama recente in quella fascia) e un ~32B quantizzato per compiti più difficili (verificare al momento quali sono i modelli consigliati: cambiano ogni pochi mesi). Test: `ollama run <modello>` con una domanda", 30),
    ("Primo test di triage: prendere 10 file di inbox/, chiedere al modello locale (via `ollama run` o un piccolo script) ambito e destinazione. Confrontare con ciò che avrebbe fatto `/triage`. Annotare in `progetti/modelli-locali/test-triage.md`: accordo su N/10, tempo per file, memoria usata (Activity Monitor)", 30)]),
 34: ("Locale: migrare il triage", [
    ("Con Claude Code: «Riscrivi il comando /triage in modo che la classificazione (ambito, destinazione, intestazione) sia fatta da uno script che chiama Ollama in locale (`http://localhost:11434`), e Claude Code faccia solo la conferma e lo spostamento». Test su 20 file. Tabella accordo/tempo in test-triage.md. Se l'accordo è < 8/10, provare il modello più grande", 60)]),
 35: ("Locale: riassunti e trascrizioni", [
    ("Trascrizione: installare whisper in locale (es. `whisper.cpp` o `mlx-whisper` su Mac) e trascrivere 2 video/audio salvati in inbox/. Riassunto con il modello locale, salvato come nota in fonti/ con intestazione. Script in `pipeline/locale/`. Annotare tempi e qualità in `progetti/modelli-locali/test-riassunti.md`", 60)]),
 36: ("Locale: specifica d'acquisto, libreria, certificazione", [
    ("`progetti/macchina-domestica.md` sezione «Requisiti reali»: quali modelli usi davvero da 3 settimane, RAM richiesta da ciascuno, quante esecuzioni a settimana, tempi di attesa che ti infastidiscono, cosa NON riesci a fare sul Mac. Questa è la specifica della 3-bis; senza dati qui, la 3-bis non si apre", 30),
    ("Verifica libreria: contare gli album in Navidrome, aggiornare libreria.md, spesa musica finora. Decisione certificazione (F3) in decisioni.md: verificare sul sito ufficiale stato del programma e requisiti; serve a te o alla società? Se è argomento di vendita → fissare una data; se è validazione personale → il portfolio di caso-studio vale di più", 30)]),
 37: ("Router a consumo: setup", [
    ("Creare account OpenRouter (o equivalente). PRIMA di tutto: impostare un tetto di spesa mensile (es. 20 €) e un alert. Creare una chiave API con nome «pipeline». Test con una chiamata da script. Annotare in `progetti/modelli-locali/router.md`: modelli scelti per il livello intermedio (2 candidati, costo per milione di token)", 60)]),
 38: ("Router: collegare il livello intermedio", [
    ("Identificare nelle pipeline i passi «intermedi» (riformulazioni, estrazioni, formattazione: non il ragionamento sul metodo). Con Claude Code: instradare quei passi al router via script in `pipeline/locale/`. Lanciare la catena su un corso di test e confrontare l'output con quello tutto-frontiera. Annotare differenze in router.md", 60)]),
 39: ("Router: misura", [
    ("Tabella in `decisioni.md` «Misura S39»: per un corso completo, costo e tempo con i tre livelli (locale / router / frontiera) contro il costo tutto-frontiera di S26. Qualità: correzioni minori o sostanziali. Se la qualità cala in modo sostanziale, tornare al frontiera per quel passo e annotare perché", 60)]),
 40: ("Chiusura Fase 3", [
    ("In `decisioni.md`, chiusura Fase 3: (1) il volume (triage, riassunti, trascrizioni) gira in locale senza che tu torni al livello alto? (2) il router copre l'intermedio? (3) costo mensile atteso da ora in poi vs S8. Preparare la decisione 3-bis: rileggere `progetti/macchina-domestica.md` e scrivere, PRIMA di guardare un listino, quale dei 3 criteri di apertura potrebbe valere e con quale dato", 60)]),
}
for n, (tit, tasks) in f3.items():
    stop = None
    if n == 36: stop = {"testo": "La libreria musicale supera i 30 album?", "altrimenti": "Il server è finito così com'è: nessun altro investimento. Il budget musica residuo si libera per la decisione di S48."}
    if n == 40: stop = {"testo": "Triage e riassunti girano in locale senza che tu torni al livello alto per insofferenza?", "altrimenti": "Annota se è un problema di modello (troppo piccolo → la 3-bis ha senso) o di flusso (lento, scomodo → la 3-bis non lo risolve)."}
    weeks.append(W(n, "Fase 3 — Modelli locali e routing", tit, 60, tasks,
        micro=["Cattura + `/triage` (in locale da S34) + commit", "Ripping a ritmo libero"],
        evid=["auto:commits:brain", "auto:files:brain/progetti", "manuale: tabella o nota di test aggiornata"], stop=stop,
        note="Blocco da 60 min. Il volume va in locale, la difficoltà resta in alto: ogni settimana annota i numeri, perché sono loro a decidere la 3-bis." if n == 33 else None))

# ---------- S41-S52 ----------
apri_note = "Le settimane 42-47 e 49-51 valgono solo se la 3-bis si è aperta a S41. Se è chiusa, sono settimane di solo mantenimento (micro-momenti): usa il blocco per ciò che è rimasto indietro nel log."
for n in range(41, 53):
    stop = None; note = None
    if n == 41:
        tit = "Decisione di apertura 3-bis"
        tasks = [("PRIMA di guardare listini. In `decisioni.md`, blocco «Apertura 3-bis»: per ciascuno dei 3 criteri scrivere vale/non vale e il dato che lo prova: (1) il Mac non regge i modelli che il triage e il livello intermedio richiedono davvero (dato: test-triage.md, macchina-domestica.md); (2) sono emersi dati di clienti che non possono passare da servizi esterni (dato: quali corsi, quali clausole); (3) c'è un'occasione dimostrativa già identificata con data (dato: quale). Se nessuno vale: fase CHIUSA, budget resta. «Il piacere di costruirla» si somma, non sostituisce", 60)]
        stop = {"testo": "Vale almeno un criterio di apertura della macchina domestica, con un dato a supporto?", "altrimenti": "Fase chiusa. Le settimane 42-47 e 49-51 diventano mantenimento."}
        note = apri_note
    elif 42 <= n <= 44:
        tit = "Requisiti macchina domestica"
        step = {42: "Tradurre i requisiti reali (macchina-domestica.md) in numeri: VRAM necessaria per i modelli scelti alla quantizzazione usata, RAM di sistema, spazio disco, rumore accettabile (dove starà?), consumo. Fasce indicative da riverificare: 1.500-2.000 € per modelli fino a 32B; 2.500-3.500 € per 70B quantizzati",
                43: "Confrontare 3 opzioni scritte in macchina-domestica.md: (a) PC assemblato con GPU consumer usata/nuova, (b) workstation preconfigurata, (c) Mac Studio / mini con memoria unificata. Per ognuna: prezzo, VRAM/RAM, modelli che regge, rumore, chi la monta",
                44: "Leggere 2-3 fonti recenti (r/LocalLLaMA, guide di build per inferenza locale) SOLO per verificare le 3 opzioni, non per scoprirne altre. Scegliere. Scrivere in decisioni.md la scelta e «cosa la riaprirebbe»"}[n]
        tasks = [("(Solo se 3-bis aperta) " + step, 60)]
    elif 45 <= n <= 47:
        tit = "Scelta e acquisto"
        step = {45: "Lista componenti o configurazione definitiva con link e prezzi in macchina-domestica.md. Totale ≤ 3.000 €. Ricordare: non è un risparmio, contando l'ammortamento costa più di un'API",
                46: "Ordinare (o far ordinare). Conferme in macchina-domestica.md. Preparare il piano di messa in opera: sistema operativo, driver, Ollama, come il Mac e il mini-PC la raggiungono in rete",
                47: "Se arrivata: montaggio/installazione OS e driver, `ollama pull` dei modelli reali, primo benchmark (token/s) annotato. Se non arrivata: rivedere il log delle ultime 12 settimane e recuperare 1 cosa rimasta indietro"}[n]
        tasks = [("(Solo se 3-bis aperta) " + step, 60)]
    elif n == 48:
        tit = "Decisione PC gaming"
        tasks = [("In `decisioni.md`, blocco «Gaming»: (1) ore giocate negli ultimi 12 mesi (conta davvero: Steam, console, telefono); (2) a quali titoli, e se girano su hardware leggero; (3) quanto resta del budget personale: riserva 350-650 €, di più solo se la libreria si è fermata a S36. Opzioni: console usata / handheld / PC / niente. Un PC da 1.200 € entra solo se il budget musica è rimasto inutilizzato. Decidere e scrivere «cosa la riaprirebbe»", 45),
                 ("(Se 3-bis aperta) Stato della messa in opera: cosa resta per S49-S51", 15)]
        stop = {"testo": "Hai giocato abbastanza da giustificare la spesa, e resta budget?", "altrimenti": "Console, handheld, o niente. Non un PC da 1.200 €."}
    elif 49 <= n <= 51:
        tit = "Messa in opera macchina domestica"
        step = {49: "Migrare `/triage` e gli script in pipeline/locale/ dal Mac alla macchina (endpoint Ollama in rete). Test su 20 file. Il Mac torna a essere solo il posto dove lavori",
                50: "Migrare trascrizioni e riassunti; provare sulla macchina il modello più grande che il Mac non reggeva. Confronto qualità in test-triage.md / test-riassunti.md",
                51: "Backup della configurazione (compose, script) in `progetti/macchina-domestica/`. Aggiungere la macchina al backup notturno del mini-PC se contiene dati. Misura: costo mensile API dopo la migrazione vs S39"}[n]
        tasks = [("(Solo se 3-bis aperta) " + step, 60)]
    else:
        tit = "Chiusura anno e piano anno 2"
        tasks = [("Revisione annuale: rileggere `log.md` intero (tutte le righe «attrito»), `decisioni.md` e questo piano. In `piano/revisione-anno-1.md`: cosa è caduto e perché, ore pianificate vs effettive, spesa vs budget per ogni voce, le 3 cose che hanno funzionato, le 3 che rifaresti diversamente", 45),
                 ("Con Claude Code: «Leggi revisione-anno-1.md, decisioni.md e piano.json. Proponi il piano dell'anno 2 con la stessa struttura: fasi, criteri di stop, ore, budget». Correggere e salvare in `piano/piano-anno-2.md`. Aggiornare gen.py dell'app. Commit", 45)]
    weeks.append(W(n, "Fase 3-bis / Fase 4", tit, 90 if n == 52 else 60, tasks,
        micro=["Cattura + `/triage` + commit", "Ripping a ritmo libero"],
        evid=["auto:commits:brain", "auto:files:brain/progetti", "manuale: blocco in decisioni.md o aggiornamento di macchina-domestica.md"],
        stop=stop, note=note))

weeks.sort(key=lambda w: w["settimana"])
assert [w["settimana"] for w in weeks] == list(range(1, 53))

piano = {
    "titolo": "Piano progetti personali — 12 mesi (v2)",
    "inizio": START.isoformat(),
    "versione": "2.1",
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
