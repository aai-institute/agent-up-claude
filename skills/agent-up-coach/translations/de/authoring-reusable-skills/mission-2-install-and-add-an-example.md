---
id: mission-2-install-and-add-an-example
number: 2
title: Installiere deinen Skill mit einem Beispiel
summary: Installiere deinen Skill, damit er von selbst lädt, und ergänze ein Beispiel für ein gutes Ergebnis und eine Regel für einen Sonderfall. Am Ende ist dein Skill installiert und zuverlässiger.
artefact: "Skill v2: installierte SKILL.md mit Beispiel und Sonderfallregel"
---

Track: Baseline
Level: foundation
Time: 30 Minuten
Tools: Claude-Chat, Cowork oder Claude Code
Artefact kind: text
Artefact file: my-skill-v2.md

## Context
Dein Skill funktioniert, wenn du ihn anhängst oder einfügst, aber du musst daran denken, und Länge und Ton schwanken trotzdem. **Installiert** und mit einem **Beispiel** startet er von selbst und liefert das Ergebnis, das du meinst.

## Your task
Ergänze deinen Skill um **ein [[Beispiel]]** für ein gutes Ergebnis und **eine [[Sonderfallregel]]** für einen ungewöhnlichen Fall, **[[installiere|Installieren]]** ihn dann und prüfe, dass er bei der richtigen Anfrage startet.

## After this, you can
Du kannst einer KI mit einem Beispiel zeigen, welches Ergebnis du willst, und einen Skill so installieren, dass er von selbst lädt.

## You need
- Deine **SKILL.md** mit Name, Beschreibung, Schritten und Prüfungen, oder das **Arbeitsbeispiel** in dieser Mission
- **Claude** in jedem Tarif, mit der Berechtigung, Skills einzuschalten

## You need [claude-code]
- Deine **SKILL.md** mit Name, Beschreibung, Schritten und Prüfungen, oder das **Arbeitsbeispiel** in dieser Mission
- **Claude Code** und einen Ordner **ohne** Projektdateien

## You need [chatgpt]
- Deine **SKILL.md** mit Name, Beschreibung, Schritten und Prüfungen, oder das **Arbeitsbeispiel** in dieser Mission
- **ChatGPT** in einem Business-, Enterprise-, Healthcare- oder Edu-Arbeitsbereich, in dem dein Admin das **Hochladen von Skills** erlaubt

## You need [gemini]
- Deine **SKILL.md** mit Name, Beschreibung, Schritten und Prüfungen, oder das **Arbeitsbeispiel** in dieser Mission
- Die **Gemini-App** mit einem privaten Google-Konto (ab 18 Jahren, **Keep-Aktivität** eingeschaltet)

## You need [no-skills]
- Deine **SKILL.md** mit Name, Beschreibung, Schritten und Prüfungen, oder das **Arbeitsbeispiel** in dieser Mission
- Deinen üblichen **KI-Chat** mit **Projekten** (ChatGPT) oder **Gems** (Gemini)

## You should already
- Eine **SKILL.md** mit Name, Beschreibung, Schritten und Prüfungen schreiben können

## Concept
Heading: Die 2 Dinge, die einen Skill zuverlässig machen
Lead: Schritte sagen, **was zu tun ist**. Ein Beispiel und eine Sonderfallregel zeigen, **wie gut aussieht** und was zu tun ist, wenn die Eingabe **nicht normal** ist.
- Beispiel: Eine kurze **Eingabe mit dem guten Ergebnis** dazu. Die KI übernimmt Länge, Ton und Aufbau.
- Sonderfallregel: Eine Regel für den **ungewöhnlichen Fall**, der dir am häufigsten begegnet: fehlende Daten, eine andere Sprache, eine sehr lange Eingabe.
Close: Schritte sagen, was zu tun ist; das **Beispiel** zeigt das Ergebnis, und die **Sonderfallregel** deckt den Fall ab, der am häufigsten schiefgeht.

## Check your understanding
Question: Dein Skill schreibt zu lange Antworten, obwohl in den Schritten „halte es kurz“ steht. Was hilft am meisten?
- A: „Sehr kurz“ in Großbuchstaben schreiben
- B: Ein Beispiel für eine gute Antwort mit der richtigen Länge ergänzen
- C: Drei weitere Schritte zur Länge ergänzen
- D: Das Ausgabeformat entfernen
Answer: B
Why: „Kurz“ bedeutet für die KI und für dich etwas anderes. Ein Beispiel zeigt die Länge, die du meinst. A und C ergänzen Wörter, ohne das Ergebnis zu zeigen; D entfernt die wenige Anleitung, die es gab.

## Working example
Situation: Dein **Skill für das Status-Update** funktioniert, aber die Updates werden jede Woche länger, und einmal hatte ein Projekt **gar kein Update**.
Input: Dein **Skill v1** und ein Freitags-Update, mit dem du zufrieden warst, ohne Namen.
- Das gute Update als **Beispiel** ans Ende des Skills setzen.
- Eine Regel ergänzen: Hat ein Projekt **kein Update**, „diese Woche kein Update“ schreiben und nachfragen.
- Den Skill in Claude **installieren**.
- Prüfen, dass er bei „schreib mein Freitags-Update“ startet und **nicht** bei „schreib ein Besprechungsprotokoll“.
Result: Ein **installierter Skill v2**, der Updates wie dein Beispiel schreibt.
Ask: Willst du an einem Skill arbeiten, den du geschrieben hast, oder am Arbeitsbeispiel? Wenn du noch keinen Skill hast, sag es, dann gebe ich dir einen kurzen Skill zum Start.

## Steps
### Beispiel
Use: Arbeite an einem Skill, den du geschrieben hast, oder am Arbeitsbeispiel unten.
Why: Ein Beispiel legt **Länge, Ton und Aufbau** auf einmal fest; ohne es rät die KI, was du mit „kurz“ oder „klar“ meinst.
Do: Füge am Ende deines Skills **ein kurzes Beispiel** hinzu: eine typische **Eingabe** und das **gute Ergebnis**, das du dafür willst. Nimm ein Ergebnis, das du **schon hast**, und ändere die Namen.
Ask: Sende das Beispiel, das du ergänzt hast.
Code:
```text
# Beispiel
Eingabe: [eine typische Eingabe, 2 bis 4 Zeilen, Namen erfunden]
Gutes Ergebnis: [ein Ergebnis, mit dem du zufrieden warst, Namen erfunden]
```
Example:
```text
# Beispiel
Eingabe: „Bestellung 4471 kam kaputt an. Ich brauche sie bis Freitag.“
Gute Antwort: „Es tut mir leid, dass Ihre Bestellung 4471 kaputt angekommen ist. Wir schicken heute Ersatz; er kommt bis Donnerstag an. Fragen: [Support-Adresse].“
```
Weak:
```text
# Beispiel
Schreibe eine gute Antwort, wie unsere besten.
```

### Sonderfallregel
Why: Die meisten Fehler entstehen im **ungewöhnlichen Fall**: Hat der Skill dafür keine Regel, improvisiert die KI.
Do: Nenne den **ungewöhnlichen Fall**, der dir bei dieser Aufgabe am häufigsten begegnet, und ergänze **eine Regel** dafür: was die KI tun soll, statt zu improvisieren.
Ask: Sende den ungewöhnlichen Fall und deine Regel.
Code:
```text
# Wenn die Eingabe ungewöhnlich ist
- Wenn [der ungewöhnliche Fall], [was stattdessen zu tun ist]. Wenn du unsicher bist, frage nach.
```
Example:
```text
Ungewöhnlicher Fall: Die Beschwerde ist in einer anderen Sprache.
Regel: Antworte in der Sprache der Beschwerde. Wenn du nicht sicher bist, welche Sprache es ist, frage nach.
```
Weak:
```text
Behandle Sonderfälle gut.
```

### Installieren
Why: Ein in den Chat eingefügter Skill wirkt nur in diesem Chat. **Installiert** sieht die KI seine Beschreibung in **jedem** Chat und startet ihn selbst, wenn eine Anfrage passt.
Do:
1. Öffne in Claude **Einstellungen > Funktionen** (Settings > Capabilities) und schalte **Codeausführung und Dateierstellung** ein.
2. Füge deinen Skill in einen neuen Chat ein und frag: **„Speichere das als SKILL.md in einem Ordner namens [name] und gib mir den Ordner als ZIP.“** Lade die ZIP-Datei herunter.
3. Wenn das nicht klappt, frag im Chat nach dem Weg von Hand. Die ZIP von Claude enthält den Ordner mit deinem **[[Skill-Kopf]]** oben in der SKILL.md, gepackt in eine **[[ZIP-Datei]]**.
4. Öffne **Anpassen > Skills** (Customize > Skills), klicke auf **+**, wähle **Skill hochladen** (Upload a skill) und dann deine ZIP-Datei.
5. Prüfe, dass der Skill in der Liste erscheint und **eingeschaltet** ist.
Ask: Sag mir, wenn dein Skill in der Liste erscheint, oder welche Meldung du siehst.

### Installieren [claude-code]
Why: Ein in den Chat eingefügter Skill wirkt nur in diesem Chat. **Installiert** sieht die KI seine Beschreibung in **jedem** Chat und startet ihn selbst, wenn eine Anfrage passt.
Do:
1. Erstelle den Ordner **~/.claude/skills/[name]/** mit dem Befehl unten.
2. Speichere **nur deinen Skill** darin als **SKILL.md**: Die Datei beginnt mit der **---** Zeile deines Skill-Kopfs.
3. Starte **claude** in einem Ordner ohne Projektdateien.
4. Tippe **/skills** und prüfe, dass dein Skill in der Liste steht.
Code:
```bash
mkdir -p ~/.claude/skills/[name]
```
Ask: Sag mir, wenn dein Skill in der Liste erscheint, oder welche Meldung du siehst.

### Installieren [chatgpt]
Why: Ein in den Chat eingefügter Skill wirkt nur in diesem Chat. **Installiert** sieht die KI seine Beschreibung in **jedem** Chat und startet ihn selbst, wenn eine Anfrage passt.
Do:
1. Erstelle einen Ordner, der **genau wie dein Skill** heißt, und speichere **nur deinen Skill** darin als **SKILL.md**.
2. Komprimiere den **Ordner** zu einer **ZIP**-Datei.
3. Öffne in ChatGPT in der Seitenleiste **Plugins** und dann den Tab **Skills**.
4. Wähle **Erstellen** (Create), dann **Vom Computer hochladen** (Upload from your computer), und wähle deine ZIP-Datei aus.
5. Warte, bis der **Scan** fertig ist, und prüfe, dass der Skill in deiner Liste steht.
Ask: Sag mir, wenn dein Skill in der Liste erscheint, oder welche Meldung du siehst.

### Installieren [gemini]
Why: Ein in den Chat eingefügter Skill wirkt nur in diesem Chat. **Installiert** sieht die KI seine Beschreibung in **jedem** Chat und startet ihn selbst, wenn eine Anfrage passt.
Do:
1. Erstelle einen Ordner, der **genau wie dein Skill** heißt, und speichere **nur deinen Skill** darin als **SKILL.md**.
2. Öffne in der Gemini-App **Einstellungen** und dann **Skills**.
3. Wähle **Erstellen** (Create) und lade deinen **Skill-Ordner** oder seine SKILL.md hoch.
4. Wähle den Skill aus, öffne **Mehr** (More) und wähle **Aktivieren** (Activate).
Ask: Sag mir, wenn dein Skill als aktiv angezeigt wird, oder welche Meldung du siehst.

### Installieren [no-skills]
Why: Dein Werkzeug hat **keinen automatischen Auslöser**, deshalb hält ein Projekt oder Gem die Anweisungen, und der Beinahe-Treffer wird zu einem **Beschreibungs-Check**.
Do:
1. Erstelle ein **Projekt** (ChatGPT) oder ein **Gem** (Gemini), das wie dein Skill heißt.
2. Füge die **Anweisungen** deines Skills in sein Anweisungsfeld ein, also alles unter dem Skill-Kopf.
3. Speichere es und bewahre **Name und Beschreibung** in einer Notiz für den Beinahe-Treffer-Test auf.
Ask: Sag mir, wenn dein Projekt oder Gem gespeichert ist, oder welche Meldung du siehst.

### Weiter vertiefen [fast-track]
Why: Schritte brauchen unterschiedlich viel **Freiheit**: Offene Schritte funktionieren am besten mit einem Ziel, heikle Schritte mit exaktem Wortlaut.
Do: Markiere jeden Schritt deines Skills als **Ziel** (mehrere gute Wege), **Muster** (ein bevorzugter Weg) oder **exakt** (muss immer gleich sein), und schreib einen exakten Schritt Wort für Wort neu.
Ask: Sende deine markierten Schritte und den neu geschriebenen exakten Schritt.
Example:
```text
1. Das Problem in einem Satz nennen: Ziel
2. Entschuldigung: Muster („Es tut mir leid, dass ...“)
3. Erstattungsbetrag: exakt. „Übernimm den Betrag aus der Preisliste. Berechne oder runde ihn nie.“
```

## Trust check
Watch for:
- Erfinde das **Beispiel**: keine echten Namen, Bestellnummern oder Kundendaten. (DSGVO, Artikel 5)
- Installiere nur Skills, die du **selbst geschrieben** oder aus einer vertrauenswürdigen Quelle hast, und lies vorher jede Datei. (Anthropic Skill-Sicherheit)
Rules:
- DSGVO, Artikel 5: Personenbezogene Daten müssen dem Zweck angemessen und erheblich sowie auf das für den Zweck notwendige Maß beschränkt sein. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de)
- Anthropic Skill-Sicherheit: Nutze nur Skills, die du selbst erstellt oder aus einer vertrauenswürdigen Quelle hast, und prüfe vorher jede Datei, denn ein Skill kann Code ausführen. [Anthropic-Doku](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
Ask: Ist in deinem Beispiel irgendetwas **echt**, das erfunden sein sollte?

## Test
Do: Sende in einem **neuen Chat** eine Anfrage, die dein Skill bearbeiten soll, mit einer kurzen Beispieleingabe; sende dann in einem weiteren neuen Chat eine **ähnliche Anfrage**, die er ignorieren soll.
Check:
- Claude zeigt für die erste Anfrage, dass es **deinen Skill nutzt**, ohne dass du ihn nennst.
- Die ähnliche Anfrage läuft **ohne** deinen Skill.
Ask: Ist dein Skill nur bei der richtigen Anfrage gestartet?

## Test [claude-code]
Do: Starte eine **neue Sitzung** in einem Ordner ohne CLAUDE.md und sende eine Anfrage, die dein Skill bearbeiten soll; sende dann in einer weiteren neuen Sitzung eine **ähnliche Anfrage**, die er ignorieren soll.
Check:
- Claude Code zeigt für die erste Anfrage, dass es **deinen Skill nutzt**, ohne dass du ihn nennst.
- Die ähnliche Anfrage läuft **ohne** deinen Skill.
Ask: Ist dein Skill nur bei der richtigen Anfrage gestartet?

## Test [no-skills]
Do: Sende in einem neuen Chat in deinem **Projekt oder Gem** eine Anfrage mit einer kurzen Beispieleingabe; füge dann in einem normalen neuen Chat nur **Name und Beschreibung** mit einer ähnlichen Anfrage ein und frag: „Würde dieser Skill hier greifen? Ja oder nein.“
Check:
- Deine **Sonderfallregel** greift, wenn du den ungewöhnlichen Fall sendest.
- Der Beschreibungs-Check sagt **nein** zur ähnlichen Anfrage.
Ask: Was kam in beiden Chats heraus?

## Other ways
- Cowork: Bitte Cowork, **deinen Skill** als Ordner und ZIP-Datei in deinem verbundenen Ordner zu speichern, und lade ihn dann hoch.
- Beim Namen aufrufen: Bitte in einem Chat um deinen Skill mit seinem **Namen**, um ihn **gezielt** auszuführen.
- skill-creator: Bitte Claude, **den skill-creator zu nutzen**, damit er ein besseres Beispiel für deinen Skill vorschlägt.

## Other ways [claude-code]
- Beim Namen aufrufen: Tippe **/[name]**, um deinen Skill **gezielt** auszuführen, auch wenn die Beschreibung ihn nicht starten würde.
- Projekt-Skill: Speichere den Ordner unter **.claude/skills/** eines Projekts, damit er nur dort lädt.
- Claude-Apps: Lade denselben Ordner als ZIP-Datei unter **Anpassen > Skills** (Customize > Skills) hoch, um ihn auch im Claude-Chat zu nutzen.

## Other ways [chatgpt]
- Beim Namen aufrufen: Tippe **@[name]**, um deinen Skill **gezielt** auszuführen.
- Editor: Ändere den Skill im **Skills-Editor**, ohne ihn neu hochzuladen.
- Codex: Speichere den Ordner unter **~/.agents/skills/** und ruf ihn mit **$[name]** auf.

## Other ways [gemini]
- Beim Namen aufrufen: Tippe **/** und wähle deinen Skill.
- Direkt bearbeiten: Ändere unter **Einstellungen > Skills** die Anweisungen und klicke auf **Speichern**.
- Gemini CLI: Speichere den Ordner unter **~/.gemini/skills/**.

## Other ways [no-skills]
- Prompt-Bibliothek: Bewahre die SKILL.md als Datei auf und füge sie in einen **neuen Chat** ein, wenn die Aufgabe ansteht.
- Claude: Dieselbe SKILL.md lässt sich in Claude in **jedem Tarif**, auch Free, als Skill hochladen.
- Später: Wenn dein Werkzeug Skills bekommt, funktioniert dieselbe Datei **ohne Änderungen**.

## Done when
- Dein Skill hat ein erfundenes Beispiel für ein gutes Ergebnis und eine Regel für einen ungewöhnlichen Fall.
- Der Skill ist installiert und eingeschaltet.
- Er ist bei der richtigen Anfrage gestartet und nicht bei der ähnlichen.

## Practice
- Sende den ungewöhnlichen Fall aus deiner Sonderfallregel und prüfe, ob die Regel greift.
- Ersetze dein Beispiel durch ein besseres aus dieser Woche, mit erfundenen Namen.
- Schreib eine zweite ähnliche Anfrage mit anderen Worten und prüfe, ob der Skill still bleibt.

## Reusable template
Name: Beispiel und Sonderfallregel
```text
# Beispiel
Eingabe: [eine typische Eingabe, erfunden]
Gutes Ergebnis: [das Ergebnis, das du willst, mit der richtigen Länge und dem richtigen Aufbau]

# Wenn die Eingabe ungewöhnlich ist
- Wenn [der ungewöhnliche Fall], [was stattdessen zu tun ist]. Wenn unsicher, frage nach.
```

## Glossary
- Beispiel: Eine kurze Eingabe mit dem guten Ergebnis dazu, in einem Skill ergänzt, damit die KI Länge, Ton und Aufbau übernimmt.
- Sonderfallregel: Eine Regel in einem Skill für den ungewöhnlichen Fall, der dir am häufigsten begegnet, damit die KI nicht improvisiert.
- Installieren: Einen Skill zu deinem KI-Werkzeug hinzufügen, damit er immer sichtbar ist und von selbst starten kann.
- ZIP-Datei: Eine komprimierte Datei, die einen ganzen Ordner enthält, damit du einen Skill in einem Schritt hochladen kannst.
- Skill-Kopf: Der Block zwischen den beiden --- Zeilen oben in der SKILL.md, mit Name und Beschreibung.

## Sources
- [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices): Beispiele mit Eingabe und Ausgabe helfen der KI, den gewünschten Stil und Detailgrad zu treffen.
- [Claude Help Centre: Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude): Die Tarife, die Skills enthalten, und der Menüweg zum Hochladen einer ZIP-Datei.
- [Claude Help Centre: How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills): Der Aufbau der ZIP-Datei: Der Skill-Ordner muss ganz oben in der ZIP-Datei liegen.
- [Anthropic: Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): Warum nur Name und Beschreibung immer sichtbar sind und warum du nur vertrauenswürdige Skills installieren solltest.
- [Google: Skills in der Gemini-App](https://support.google.com/gemini/answer/17094296?hl=de): Wie du in der Gemini-App einen Skill erstellst und aktivierst.

## Coach notes
Arc: second of five in this topic (write the skill; install it and add an example; test and fix; reference files and templates; connect and get ready to share). Never name the other missions by number to the learner. Levels covered: guard (example, edge rule) and install.
Levels: guided (A, B) sees each step's example before writing, gets Claude to build the ZIP, and hears plain words only (say "the block at the top" for header); standard (C) tries first; fast-track (D) may test out with an installed skill that has an example, and gets the Go further step.
Starter skill: if the learner has no skill yet, draft a short v1 for the working example adapted to their role and say you drafted it. The example and the edge rule stay theirs.
Likely errors: an example that describes quality instead of showing a result; a real email pasted as the example; an edge rule for a rare case instead of the most common one; the ZIP holds a folder inside a folder; the file is saved as SKILL.md.txt.
Menus: if the learner's app shows other menu names than the page, ask what they see and guide from there; menu names change between app versions.
Upload problems: "SKILL.md.txt" (Windows hides extensions: let Claude build the ZIP); "contents zipped instead of the folder"; an error that says "frontmatter" means the header block at the top; "folder name does not match" (rename the folder to the name); "invalid characters" (capitals, spaces, umlauts in the name). On Team or Enterprise an admin may need to enable skills. Menu names change; ask what they see.
Time budget for guided learners (30 minutes in total, profile and level question included): about 4 to 5 minutes per build step. They copy the step's fill-in lines and fill the [blanks]; they never write a part from an empty page. If a step runs over 8 minutes, accept a short version and note one improvement for later.
Cannot upload today: paste the skill into a fresh chat to check the example, and use the description check ("Would this skill apply? Yes or no.") for the similar request; label both as stand-ins.
Time: two feedback rounds per step at most. The test checks only what this mission changed: does the installed skill start by itself for the right request and stay quiet for the similar one. Output quality is not re-checked here; the full test set comes in the test-and-fix mission.
Page state: set the full skill v2 as the part for the last step (Install; Go further for fast-track).
Other vendors: ChatGPT (eligible workspaces) and the Gemini app read the same SKILL.md; the description starts the skill only where skills load automatically.
