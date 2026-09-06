# piano-app

Ti dice cosa fare questa settimana, quanto tempo bloccare, e scrive il log al posto tuo.

## Messa in opera (15 minuti, anche da telefono)

1. **Crea il repo** `piano-app` su GitHub (pubblico o privato; con privato GitHub Pages richiede un piano a pagamento, quindi conviene pubblico: il piano non contiene dati sensibili — verifica).
2. **Carica questi file** nel repo (Add file → Upload files, oppure `git push` da Claude Code): `index.html`, `piano.json`, `stato.json`, `log.md`, `decisioni.md`, `gen.py`, `CLAUDE.md`, `README.md`.
3. **Attiva Pages:** Settings → Pages → Source: Deploy from a branch → `main` / root. Dopo un minuto l'app è su `https://<utente>.github.io/piano-app/`.
4. **Crea il token:** Settings (profilo) → Developer settings → Personal access tokens → Fine-grained. Repository access: `piano-app` più i repo `brain` e `pipeline`. Permessi: Contents → Read and write. Scadenza: 1 anno.
5. **Apri l'app**, Impostazioni: incolla il token, scrivi `utente/piano-app`, `utente/brain`, `utente/pipeline`. Salva. Il token resta solo nel browser del dispositivo.
6. **Aggiungi la pagina alla schermata home** del telefono (condividi → Aggiungi a schermata Home).
7. **Metti in agenda** l'evento ricorrente della chiusura settimanale con il link all'app. È l'unico trigger esterno: l'app non può aprirsi da sola.

## Come si usa
- Apri: vedi settimana, fase, minuti da bloccare, attività con i minuti, micro-momenti, criterio di stop se cade quella settimana.
- Spunta le attività man mano.
- Le evidenze automatiche leggono i commit della settimana nei repo osservati e i file nelle cartelle di `brain/`.
- A fine settimana: minuti effettivi, attrito, prossimo blocco → **Chiudi la settimana**. L'app appende a `log.md` e aggiorna `stato.json` con un commit.
- Se sei indietro di 3+ settimane, l'app lo dice e propone di spostare il calendario. Non comprime mai.

## Per iterare con Claude Code
Clona il repo, apri Claude Code nella cartella: `CLAUDE.md` contiene le regole e le prossime iterazioni suggerite. Prompt di partenza consigliato:

> Leggi CLAUDE.md. Implementa la prossima iterazione 1 (notifica di chiusura via GitHub Action + issue). Non toccare index.html se non serve.
