---
id: mission-5-connect-and-share-your-skill
number: 5
title: Verbinde deinen Skill und mach ihn teilbar
summary: Lass deinen Skill aus einer App lesen, die du schon mit Claude verbindest, begrenze, was er tun darf, und pack ihn mit Version und kurzer Karte zusammen, damit andere ihn nutzen können.
artefact: "Skill v5: verbundener Skill mit Schutzregeln, Versionszeile und Skill-Karte"
---

Track: Baseline
Level: practitioner
Time: 30 Minuten
Tools: Claude-Chat, Cowork oder Claude Code, mit einer verbundenen App
Artefact kind: text
Artefact file: my-skill-v5.md

## Context
Du **kopierst** Daten noch von Hand aus deiner Ablage **hinein**, und niemand sonst könnte deinen Skill nutzen, ohne dich zu fragen. Einen Schritt zu **verbinden**, eine **Schutzregel** und eine kurze **Karte** lösen beides.

## Your task
Lass einen Schritt deines Skills **aus einer verbundenen App lesen**, füge **Schutzregeln** hinzu, was er tun darf, und schreib eine **Versionszeile und eine Skill-Karte**, damit jemand anderes ihn nutzen kann.

## After this, you can
Du kannst einen Schritt eines Skills mit einer klaren Grenze an eine App anbinden und einen Skill so vorbereiten, dass jemand anderes ihn nutzen kann, ohne dich zu fragen.

## You need
- Deinen **Skill-Ordner**, mindestens einmal getestet, oder das **Arbeitsbeispiel** in dieser Mission
- **Claude** mit eingeschalteten Skills und eine **verbundene App**, die du bei der Arbeit nutzen darfst (zum Beispiel Google Drive oder einen Kalender)
- **Testdaten** in dieser App, oder eine Kopie ohne Namen

## You need [claude-code]
- Deinen **Skill-Ordner**, mindestens einmal getestet, oder das **Arbeitsbeispiel** in dieser Mission
- **Claude Code** und einen **MCP-Server** oder ein verbundenes Tool, das du bei der Arbeit nutzen darfst
- **Testdaten**, oder eine Kopie ohne Namen

## You need [chatgpt]
- Deinen **Skill-Ordner**, mindestens einmal getestet, oder das **Arbeitsbeispiel** in dieser Mission
- **ChatGPT** in einem Arbeitsbereich mit **Skills** und einer **verbundenen App**, die dein Admin erlaubt

## You need [gemini]
- Deinen **Skill-Ordner**, mindestens einmal getestet, oder das **Arbeitsbeispiel** in dieser Mission
- Die **Gemini-App** mit Skills und einer **verbundenen Google-App** (Drive, Kalender oder Gmail)

## You need [no-skills]
- Deinen **Skill-Ordner**, mindestens einmal getestet, oder das **Arbeitsbeispiel** in dieser Mission
- Dein **Projekt** oder **Gem** und eine **verbundene App**, die dein Werkzeug anbietet, oder einen Dateiexport der Daten

## You should already
- Einen **Skill installieren** und einen Test in einem **neuen Chat** ausführen können

## Concept
Heading: Die 3 Dinge, die ein Skill braucht, bevor andere sich darauf verlassen
Lead: Ein Skill, der seine Daten selbst holt und den andere nutzen, braucht **eine Verbindung**, **Schutzregeln** und **eine Karte**.
- Verbindung: Ein Schritt liest **Live-Daten** aus einer **[[verbundenen App|Verbundene App]]**, die du schon mit Claude nutzt, etwa einer Ablage oder einem Kalender, statt dass du sie einfügst.
- Schutzregeln: **[[Regeln|Schutzregeln]]** dafür, was der Skill **lesen** darf und wann er **vorher fragen** muss: beim Senden, Speichern, Löschen.
- Karte: Eine **[[Skill-Karte]]**, eine Seite **neben** dem Skill-Ordner: was er tut, wann man ihn nutzt, was man prüft, wer sich um ihn kümmert.
Close: Jeder der drei Teile bekommt unten einen eigenen Schritt, mit seinem Grund.
Toggle: Ist ein verbundener Skill eine Automatisierung? | Nein. Ein Skill läuft weiterhin nur, wenn jemand ihn **anfragt**. Automatisierungen, die **von selbst** laufen, nach Zeitplan oder bei einem Ereignis, sind ein eigenes Thema.
Toggle: Warum liegt die Karte neben dem Ordner und nicht darin? | Alles **im** Ordner liest die KI. Die Karte ist für **Menschen**, deshalb liegt sie neben dem Ordner.

## Check your understanding
Question: Dein Skill liest die Termine dieser Woche aus einem verbundenen Kalender und entwirft eine Zusammenfassung. Welche Schutzregel ist am wichtigsten?
- A: Sei vorsichtig mit dem Kalender
- B: Nur lesen; nie Termine anlegen, ändern oder löschen; jeden Entwurf vor dem Senden zeigen
- C: Nutze den Kalender so oft wie möglich
- D: Keine Schutzregeln nötig, weil der Kalender verbunden ist
Answer: B
Why: B nennt, was der Skill lesen darf und was er nie tun oder nur nach Rückfrage tun darf. A ist zu vage, um ihr zu folgen, C erhöht das Risiko, und D übersieht, dass eine Verbindung echte Daten erreicht.

## Working example
Situation: Dein **Skill für das Status-Update** braucht die Aufgaben dieser Woche, die du von Hand aus einer **geteilten Aufgabenliste** in deiner Ablage kopierst. Zwei andere Teamleads wollen den Skill auch nutzen.
Input: Dein **getesteter Skill-Ordner** und die Aufgabenliste in deiner verbundenen Ablage, nur mit Testaufgaben.
- Den Aufgabenschritt so umschreiben, dass er die Liste aus der Ablage **liest**.
- **Schutzregeln** hinzufügen: nur lesen, vor jedem Speichern oder Senden fragen.
- Projektnamen durch **[Platzhalter]** ersetzen und eine **Versionszeile** hinzufügen.
- Eine kurze **Skill-Karte** für die beiden Teamleads schreiben.
Result: Ein **Skill v5**, der seine Eingabe selbst holt und bereit zum Teilen ist.
Ask: Willst du an einem eigenen Skill arbeiten oder am Arbeitsbeispiel? Sag mir, welche Daten du noch von Hand hineinkopierst.

## Steps
### Verbinden
Use: Arbeite an einem Skill, den du geschrieben hast, oder am Arbeitsbeispiel unten.
Why: Beim Kopieren von Hand schleichen sich Fehler und alte Versionen ein; ein Schritt, der **die App nennt** und **genau sagt, was gelesen wird**, lässt den Skill die Daten selbst holen.
Do:
1. Wähle den **einen Schritt**, für den du noch Daten von Hand hineinkopierst. Wenn die App **noch nicht verbunden** oder nicht erlaubt ist, lade stattdessen eine **Datei** mit denselben Daten in den Chat hoch.
2. Öffne in Claude **Anpassen > Konnektoren** (Customize > Connectors), so nennt Claude verbundene Apps, und verbinde die App mit den Daten.
3. Öffne in einem Chat **+ > Konnektoren** (+ > Connectors) und prüfe, dass die App **eingeschaltet** ist.
4. Schreib den Schritt in SKILL.md so um, dass er **die App nennt**, genau sagt, **was gelesen** wird, und was passiert, wenn die App **nicht erreichbar** ist.
Ask: Sende deinen umgeschriebenen Schritt und die Zeile für den Fall, dass die App nicht erreichbar ist.
Code:
```text
[n]. Lies [was genau] aus [App-Name], [Ordner oder Datei]. Nutze nur, was die App liefert.
     Wenn [App-Name] nicht erreichbar ist, sag das und frag mich nach den Daten. Erfinde sie nie.
```
Example:
```text
2. Lies den Lieferstatus aus Google Drive, Tabelle „Bestellungen diesen Monat“, Zeile mit der Bestellnummer. Nutze nur die Spalte „Status“.
   Wenn Google Drive nicht erreichbar ist, sag das und frag mich nach dem Status. Erfinde ihn nie.
```
Weak:
```text
2. Hol die Daten aus Drive.
```

### Verbinden [claude-code]
Use: Arbeite an einem Skill, den du geschrieben hast, oder am Arbeitsbeispiel unten.
Why: Beim Kopieren von Hand schleichen sich Fehler und alte Versionen ein; ein Schritt, der **das Tool nennt** und **genau sagt, was gelesen wird**, lässt den Skill die Daten selbst holen.
Do:
1. Wähle den einen Schritt, der **Live-Daten** aus einem anderen System braucht (ein Issue-Tracker, eine Ablage, eine Datenbank).
2. Verbinde dieses System als **MCP-Server** in Claude Code, oder nutze einen, den du schon hast.
3. Schreib den Schritt so um, dass er **das Tool nennt** (ServerName:tool_name) und genau sagt, **was gelesen** wird.
4. Ergänze, was passiert, wenn das Tool **nicht erreichbar** ist: das sagen und fragen, die Daten nie erfinden.
Ask: Sende deinen umgeschriebenen Schritt und die Zeile für den Fall, dass das Tool nicht erreichbar ist.
Example:
```text
2. Lies die offenen Issues mit dem Label „release“ mit GitHub:list_issues. Nutze nur Titel und Nummer.
   Wenn GitHub nicht erreichbar ist, sag das und bitte mich um die Liste. Erfinde nie Issues.
```
Weak:
```text
2. Schau in GitHub nach.
```

### Verbinden [chatgpt]
Use: Arbeite an einem Skill, den du geschrieben hast, oder am Arbeitsbeispiel unten.
Why: Beim Kopieren von Hand schleichen sich Fehler und alte Versionen ein; ein Schritt, der **die App nennt** und **genau sagt, was gelesen wird**, lässt den Skill die Daten selbst holen.
Do:
1. Verbinde in ChatGPT die **App**, die dein Schritt braucht (dein Admin entscheidet, welche Apps es gibt).
2. Schreib in deinem Skill den gewählten Schritt so um, dass er **die App nennt** und genau sagt, **was gelesen** wird.
3. Ergänze, was passiert, wenn die App **nicht erreichbar** ist: das sagen und fragen, die Daten nie erfinden.
4. Aktualisiere den Skill im **Skills-Editor** oder lade ihn erneut hoch.
Ask: Sende deinen umgeschriebenen Schritt und die Zeile für den Fall, dass die App nicht erreichbar ist.

### Verbinden [gemini]
Use: Arbeite an einem Skill, den du geschrieben hast, oder am Arbeitsbeispiel unten.
Why: Beim Kopieren von Hand schleichen sich Fehler und alte Versionen ein; ein Schritt, der **die App nennt** und **genau sagt, was gelesen wird**, lässt den Skill die Daten selbst holen.
Do:
1. Prüfe in der Gemini-App, dass die **Google-App**, die dein Schritt braucht (Drive, Kalender oder Gmail), verbunden ist.
2. Schreib unter **Einstellungen > Skills** (Settings > Skills) den gewählten Schritt so um, dass er **die App nennt** und genau sagt, **was gelesen** wird.
3. Ergänze, was passiert, wenn die App **nicht erreichbar** ist: das sagen und fragen, die Daten nie erfinden.
4. Klicke auf **Speichern** (Save). Skripte in Skills der Gemini-App können keine externen Websites aufrufen, deshalb gehören Web-Schritte nicht in scripts/.
Ask: Sende deinen umgeschriebenen Schritt und die Zeile für den Fall, dass die App nicht erreichbar ist.

### Verbinden [no-skills]
Use: Arbeite an einem Skill, den du geschrieben hast, oder am Arbeitsbeispiel unten.
Why: Beim Kopieren von Hand schleichen sich Fehler und alte Versionen ein; ein Schritt, der **die App nennt** und **genau sagt, was gelesen wird**, lässt den Skill die Daten selbst holen.
Do:
1. Verbinde in deinem KI-Werkzeug die **App**, die dein Schritt braucht, wenn es verbundene Apps anbietet.
2. Schreib den Schritt in deinen Projekt- oder Gem-Anweisungen so um, dass er **die App nennt** und genau sagt, **was gelesen** wird.
3. Ergänze, was passiert, wenn die App **nicht erreichbar** ist: das sagen und fragen, die Daten nie erfinden.
Ask: Sende deinen umgeschriebenen Schritt und die Zeile für den Fall, dass die App nicht erreichbar ist.

### Schutzregeln
Why: Über die App erreicht der Skill deine **echten Dateien und Daten**. Schutzregeln sind Regeln im Skill: Er bleibt beim **Lesen** und **fragt dich**, bevor er etwas sendet, speichert oder löscht. Was die App überhaupt erreichen kann, legen dein Konto und dein Admin fest.
Do: Füge einen Abschnitt **Schutzregeln** hinzu: was der Skill **lesen** darf, dass er **vor** jedem Schreiben, Senden oder Löschen **fragt**, und ein **[VERIFY]**-Kennzeichen an dem, was die App zurückgibt.
Ask: Sende deine Schutzregeln.
Code:
```text
# Schutzregeln
- Nur lesen: [was]. Nie [ändern / senden / löschen]: [was].
- Bevor du etwas sendest oder speicherst, zeig den Entwurf und warte auf „ja“.
- [VERIFY] [was die App geliefert hat] stimmt mit [wo du es prüfen kannst] überein.
```
Example:
```text
# Schutzregeln
- Nur lesen: Bestellstatus und Lieferdatum aus dem Shopsystem. Ändere nie eine Bestellung.
- Bevor du etwas sendest oder speicherst, zeig den Entwurf und warte auf „ja“.
- [VERIFY] Die Bestellnummer in der Antwort stimmt mit der überein, die das Shopsystem geliefert hat.
```
Weak:
```text
Sei vorsichtig mit dem Shopsystem.
```

### Skill-Karte
Why: Andere entscheiden in **einer Minute**, ob sie einen Skill nutzen, und können dich nicht fragen; eine Versionszeile zeigt allen, **welche Kopie** aktuell ist.
Do: Ersetze Namen, Kundendaten und Links im Ordner durch je einen **[[Platzhalter]]**, füge als letzte Zeile **Version, Verantwortliche und Datum** hinzu und schreib eine **einseitige Skill-Karte** neben den Ordner.
Ask: Sende deine **Skill-Karte**; die Versionszeile steht am Ende deines Skills auf der Seite.
Code:
```text
[skill-name], Version [n], verantwortlich: [Team oder Rolle], geprüft im [Monat Jahr]
Tut: [was, für wen]. Nutzen, wenn: [Situationen]. Nicht für: [Beinahe-Treffer].
Vor der Nutzung prüfen: [VERIFY-Punkte]. Braucht: [App, Zugang].
```
Example:
```text
Version 1.0, verantwortlich: Teamleitung Kundenservice, geprüft im Oktober 2026.

Skill-Karte: complaint-reply-drafts, Version 1.0
Tut: entwirft Antworten auf Kundenbeschwerden in unserem Support-Ton.
Nutzen, wenn: du eine Beschwerde-E-Mail einfügst. Nicht für: Vertriebs- oder interne E-Mails.
Ausfüllen: [Support-Adresse] in der Vorlage.
Vor dem Senden prüfen: jeden Erstattungsbetrag und jedes Datum (mit [VERIFY] markiert).
Braucht: Claude mit Skills; Konnektor zum Shopsystem, nur lesen.
```
Weak:
```text
Ein Skill für Antworten. Frag mich, wenn etwas unklar ist.
```

### Weiter vertiefen [fast-track]
Why: Manche Schritte müssen jedes Mal **genau dasselbe Ergebnis** liefern, und manche Skills sollen **nur laufen, wenn man sie beim Namen aufruft**.
Do: Füge ein **Skript** in scripts/ für einen exakten Schritt hinzu (führe es einmal mit Testdaten aus und prüfe das Ergebnis von Hand), oder ergänze in Claude Code den Skill-Kopf um **disable-model-invocation: true**, wenn der Skill nur als /[name] laufen soll.
Ask: Sende dein Skript und sein Testergebnis, oder deinen Skill-Kopf mit dem Grund.

## Trust check
Watch for:
- Verbinde mit dem **geringsten Zugriff**, den der Schritt braucht, zuerst mit Testdaten, und schreib nie Passwörter oder Schlüssel in den Skill. (DSGVO, Artikel 5)
- Behalte einen **Menschen in der Schleife**: Der Skill fragt, bevor er etwas sendet, speichert oder löscht. (EU AI Act, Artikel 4)
- Bevor du einen Skill installierst, den **jemand anderes** geschrieben hat, lies jede Datei und achte auf Skripte und Webadressen. (Anthropic Skill-Sicherheit)
Rules:
- DSGVO, Artikel 5: Personenbezogene Daten müssen dem Zweck angemessen und erheblich sowie auf das für den Zweck notwendige Maß beschränkt sein. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de)
- EU AI Act, Artikel 4: Organisationen, die KI-Systeme anbieten oder nutzen, müssen dafür sorgen, dass ihr Personal für seine Rolle genug KI-Kompetenz hat: Es versteht die Werkzeuge und weiß, was die Ergebnisse bedeuten. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=de)
- Anthropic Skill-Sicherheit: Nutze nur Skills, die du selbst erstellt oder aus einer vertrauenswürdigen Quelle hast, und prüfe vorher jede Datei, denn ein Skill kann Code ausführen und Webinhalte abrufen. [Anthropic-Dokumentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
Ask: Welche Daten **liest** dein verbundener Schritt?

## Test
Do: Sende in einem **neuen Chat** mit verbundener App eine Anfrage, die den verbundenen Schritt braucht; schalte dann die App für diesen Chat **aus** und sende sie erneut.
Check:
- Mit eingeschalteter App nutzt das Ergebnis die **Live-Daten**, und der Skill **fragt** vor jeder Änderung.
- Mit ausgeschalteter App **sagt** der Skill, dass er die App **nicht erreicht**, statt Daten zu erfinden.
- Wer nur deine **Skill-Karte** liest, weiß, wann der Skill zu nutzen ist und was zu prüfen ist.
Ask: Was ist mit eingeschalteter und ausgeschalteter App passiert? Schreib mir, was herauskam.

## Test [claude-code]
Do: Starte eine **neue Sitzung** und sende eine Anfrage, die den verbundenen Schritt braucht; sende sie dann in einer weiteren neuen Sitzung mit ausgeschaltetem Tool erneut.
Check:
- Mit eingeschaltetem Tool nutzt das Ergebnis die **Live-Daten**, und der Skill **fragt** vor jeder Änderung.
- Mit ausgeschaltetem Tool **sagt** der Skill, dass er es **nicht erreicht**, statt Daten zu erfinden.
- Wer nur deine **Skill-Karte** liest, weiß, wann der Skill zu nutzen ist und was zu prüfen ist.
Ask: Was ist mit eingeschaltetem und ausgeschaltetem Tool passiert? Schreib mir, was herauskam.

## Test [no-skills]
Do: Sende in einem neuen Chat in deinem Projekt oder Gem eine Anfrage, die den verbundenen Schritt braucht; sende sie dann erneut in einem Chat **ohne** die App oder Datei.
Check:
- Mit App oder Datei nutzt das Ergebnis deren **Daten** und fragt vor jeder Änderung.
- Ohne sie **sagt** das Ergebnis, dass die Daten fehlen, statt sie zu erfinden.
- Wer nur deine **Skill-Karte** liest, weiß, wann der Skill zu nutzen ist und was zu prüfen ist.
Ask: Was ist in beiden Chats passiert? Schreib mir, was herauskam.

## Other ways
- Team und Enterprise: Nutze die Option zum **Teilen** des Skills, oder bitte einen Admin, ihn in der **Organisationsbibliothek** zu veröffentlichen.
- Andere Tarife: Teile die **ZIP-Datei und die Skill-Karte** über eine geteilte Ablage; jede Person lädt sie unter **Anpassen > Skills** (Customize > Skills) hoch.
- Datei statt App: Lade einen **Dateiexport** mit dem Skill hoch, um den Schritt zu testen, bevor du etwas verbindest.

## Other ways [claude-code]
- Projekt-Skill: Committe den Ordner nach **.claude/skills/** im Repository deines Teams, damit alle, die dort arbeiten, ihn bekommen.
- Plugin: Bündle den Skill in einem **Plugin** für dein Team; Skills in einem Plugin werden als plugin-name:skill-name aufgerufen.
- Erlaubte Tools: **allowed-tools** im Skill-Kopf genehmigt Tools vorab; um ein Tool zu sperren, nutze Berechtigungsregeln in deinen Einstellungen.

## Other ways [chatgpt]
- Arbeitsbereich: Nutze **Skills teilen** (Share skills) oder bitte einen Admin, den Skill in deinem Arbeitsbereich zu **veröffentlichen**.
- Plugins: In ChatGPT kann ein Skill neben Apps in einem **Plugin** liegen; die App bringt die Daten, der Skill den Arbeitsablauf.
- Codex: Committe den Ordner nach **.agents/skills** in einem geteilten Repository.

## Other ways [gemini, no-skills]
- Geteilte Ablage: Leg die **ZIP-Datei und die Skill-Karte** in einen gemeinsamen Ordner, mit der Version im Dateinamen.
- Datei statt App: Lade einen **CSV-Export** mit dem Skill hoch, um den Schritt zuerst zu testen.
- Claude: Derselbe Ordner lässt sich in Claude in jedem Tarif als Skill hochladen, mit Konnektoren.

## Done when
- Ein Schritt nennt die verbundene App, sagt, was gelesen wird, und was passiert, wenn die App nicht erreichbar ist.
- Schutzregeln beschränken den Skill aufs Lesen und lassen ihn vor jeder Änderung fragen.
- Der Ordner enthält keine personenbezogenen Daten, endet mit einer Versionszeile und hat eine einseitige Skill-Karte daneben.

## Practice
- Lies jede Datei eines Skills, den du nicht geschrieben hast, bevor du ihn installierst, und notiere jedes Skript und jede Webadresse.
- Führe deinen Skill einmal mit echten Daten aus, nur lesend, und vergleiche das Ergebnis mit dem, was du von Hand geschrieben hättest.
- Trag dir in drei Monaten einen Termin ein, um deinen Skill und seine Skill-Karte erneut zu prüfen.

## Reusable template
Name: Verbundener Schritt, Schutzregeln und Skill-Karte
```text
[n]. Lies [was genau] aus [Name der App]. Nutze nur, was zurückkommt.
     Wenn [App] nicht erreichbar ist, sag das und bitte mich um die Daten. Erfinde sie nie.

# Schutzregeln
- Nur lesen: [was]. Nie [ändern / senden / löschen]: [was].
- Bevor du etwas sendest oder speicherst, zeig den Entwurf und warte auf „ja“.
- [VERIFY] [Ergebnis der App] stimmt mit [Stelle, an der ein Mensch es prüfen kann] überein.

Version [n], verantwortlich: [Team oder Rolle], geprüft im [Monat Jahr].

Skill-Karte: [skill-name], Version [n]
Tut: [was, für wen]. Nutzen, wenn: [Situationen]. Nicht für: [Beinahe-Treffer].
Ausfüllen: [Platzhalter]. Prüfen: [VERIFY-Punkte]. Braucht: [Werkzeug, App, Zugriff].
```

## Glossary
- Verbundene App: Eine App wie eine Ablage oder ein Kalender, die du mit deinem KI-Werkzeug verbindest, damit es dort Daten lesen oder Aktionen ausführen kann.
- Schutzregeln: Ein Abschnitt in einem Skill, der begrenzt, was er lesen und ändern darf und wann er vorher fragen muss.
- Skill-Karte: Eine einseitige Notiz neben einem Skill-Ordner, die Menschen sagt, was der Skill tut, wann man ihn nutzt und was man prüft.
- Platzhalter: Eine markierte Lücke wie [Kunde], die in einem geteilten Skill echte Daten ersetzt.

## Sources
- [Claude Help Centre: Use connectors](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities): Wie du eine verbundene App hinzufügst und pro Chat einschaltest, und wie Admins Schreibaktionen begrenzen können.
- [OpenAI: Skills and plugins](https://developers.openai.com/plugins/concepts/skills): Die verbundene App bringt Live-Informationen und Aktionen; der Skill bringt den Arbeitsablauf drumherum.
- [Claude Help Centre: Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude): Skills mit Kollegen teilen und in Team und Enterprise in einer Organisationsbibliothek veröffentlichen.
- [Anthropic: The complete guide to building skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf): Keine README im Skill-Ordner, und Regeln für Namen geteilter Skills.
- [Anthropic: Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): Nutze nur Skills aus vertrauenswürdigen Quellen und prüfe jede Datei, denn Skills können Code ausführen.
- [Claude Code docs: Skills](https://code.claude.com/docs/en/skills): Projekt-Skills, Plugins, allowed-tools und disable-model-invocation.

## Coach notes
Arc: last of five in this topic (write the skill; install it and add an example; test and fix; reference files and templates; connect and get ready to share). Never name the other missions by number to the learner. Levels covered: connect (light) and share (light).
Curriculum boundaries: this topic sits in the no-code Integrating Agents track. Keep connecting to apps the learner already connects to Claude; automations that run on their own belong to the n8n topic, building agents with tools (MCP in depth) to the single-agent prototype topic, permission design to "Scoping permissions and production guardrails", and handover documentation and usage tracking to "Handing off what you built responsibly". Mention them only if the learner asks how to go further.
Levels: guided (A, B) uses a connector they already have (often a drive or calendar), hears "connected app" not MCP, and may use a file export instead; standard (C) chooses the step alone; fast-track (D) uses the claude-code variant with an MCP tool and gets the Go further step (script or by-name-only).
No connector allowed at work: use a file export uploaded with the skill as a stand-in and say plainly that this tests the step, not the live connection. The guard still applies.
Likely errors: a step that says "use the drive" without saying what to read; no line for when the app is unavailable; a guard that says "be careful"; real customer data in the first test; a card that describes how the skill was built instead of how to use and check it; a README inside the folder instead of a card next to it.
Time budget for guided learners (30 minutes in total, profile and level question included): about 4 to 5 minutes per build step. They copy the step's fill-in lines and fill the [blanks]; they never write a part from an empty page. If a step runs over 8 minutes, accept a short version and note one improvement for later. If the connector is not set up, use the file route; connecting an app is not worth 10 minutes of a 30-minute mission.
Feedback: name what is clear (the step, the limit, the card), then the gap, then one fix.
Page state: set the full skill v5 with its guard, version line and card as the part for the last step (Card; Go further for fast-track).
Other vendors: ChatGPT plugins can bundle skills with apps, and workspaces can share and publish skills; Gemini app skills can include scripts that cannot reach external websites, and connect to Google apps. Where equivalence breaks: connector names and permissions differ per tool, so the guard must name the app as the learner sees it.
