---
id: mission-1-write-your-first-skill
number: 1
title: Schreib deinen ersten Skill
summary: Mach aus einer Aufgabe, die du der KI immer wieder erklärst, einen Skill, den sie selbst lädt. Am Ende hast du eine vollständige SKILL.md mit Auslöser, Anweisungen und Prüfungen.
artefact: "Skill v1: SKILL.md mit Auslöser, Anweisungen und Prüfungen"
---

Track: Baseline
Level: foundation
Time: 30 Minuten
Tools: Claude-Chat, Cowork oder Claude Code
Artefact kind: text
Artefact file: my-skill-v1.md

## Context
Nach jedem **Team-Meeting** erklärst du deinem KI-Chat wieder **dieselben Regeln**: Mach aus meinen Notizen eine Follow-up-Mail, liste auf, was wir vereinbart haben, ergänze die nächsten Schritte mit Datum, halte es kurz. Und das Ergebnis ist trotzdem jedes Mal anders. Mit einem **[[Skill]]** erklärst du es **einmal**, und die KI macht es **von selbst** richtig, sobald die Aufgabe ansteht. Das spart dir jede Woche Zeit, und einen Skill zu schreiben ist leichter, als es aussieht.

## Your task
Nach dieser Mission wirst du **einfache Skills selbst erstellen** können.

## After this, you can
In den nächsten Schritten siehst du, **was ein Skill ist**, schreibst **deinen ersten Skill** Schritt für Schritt und **testest ihn**, um zu sehen, wie er wirklich funktioniert.

## You need
- **Claude**-Chat, Cowork oder Claude Code, in jedem Tarif
- Eine **wiederkehrende Aufgabe**, mindestens monatlich, mit jedes Mal ähnlichem Ergebnis, oder das **Arbeitsbeispiel** in dieser Mission

## You need [claude-code]
- **Claude Code** im Terminal oder Editor
- Eine **wiederkehrende Aufgabe**, mindestens monatlich, mit jedes Mal ähnlichem Ergebnis, oder das **Arbeitsbeispiel** in dieser Mission

## You need [chatgpt]
- **ChatGPT** in einem Business-, Enterprise-, Healthcare- oder Edu-Arbeitsbereich mit eingeschalteten **Skills**, oder **Codex**
- Eine **wiederkehrende Aufgabe**, mindestens monatlich, mit jedes Mal ähnlichem Ergebnis, oder das **Arbeitsbeispiel** in dieser Mission

## You need [gemini]
- Die **Gemini-App** mit einem privaten Google-Konto und **Skills**, oder **Gemini CLI**
- Eine **wiederkehrende Aufgabe**, mindestens monatlich, mit jedes Mal ähnlichem Ergebnis, oder das **Arbeitsbeispiel** in dieser Mission

## You need [no-skills]
- Deinen üblichen **KI-Chat** (zum Beispiel ChatGPT, Gemini oder Copilot), in dem du einen **neuen Chat** öffnen kannst
- Eine **wiederkehrende Aufgabe**, mindestens monatlich, mit jedes Mal ähnlichem Ergebnis, oder das **Arbeitsbeispiel** in dieser Mission

## You should already
- Einen Prompt mit **Aufgabe, Kontext und Erfolgskriterien** schreiben können

## Concept
Heading: Die 3 Teile, die jeder Skill braucht
Lead: Ein Skill ist eine **Datei mit Anweisungen**, die die KI **nur liest, wenn die Aufgabe ansteht**. Zum Beispiel ein Skill, der **deine Notizen der Woche** in eine kurze Zusammenfassung verwandelt. Programmieren musst du dafür nicht: Es ist **normaler Text**.
- Name: Was der Skill tut, in **Kleinbuchstaben mit Bindestrichen**. Beispiel: **weekly-notes-summary**
- Beschreibung: Der [[Auslöser]], der der KI sagt, **wann** sie den Skill nutzen soll, und wann nicht (der **[[Beinahe-Treffer]]**). Beispiel: "Nutzen, wenn ich meine Notizen der Woche einfüge. Nicht für Sitzungsprotokolle."
- Anweisungen: Die **Schritte**, denen die KI folgt, einer nach dem anderen. Beispiel: "1. Ordne die Notizen nach Projekt. 2. Schreib, was erledigt ist und was als Nächstes kommt. 3. Höchstens eine halbe Seite."
Toggle: Warum ein Skill und kein gespeicherter Prompt? | Ein Prompt wirkt nur, wenn du daran denkst, ihn einzufügen. Die KI liest **Name und Beschreibung** jedes Skills die ganze Zeit, nur wenige Zeilen pro Skill, und öffnet die **Anweisungen erst**, wenn eine Anfrage passt.
Toggle: Ist ein Skill nur eine Datei? | Ein Skill ist ein **Ordner**. Die SKILL.md ist die einzige Datei, die er für den Anfang braucht; Listen, Vorlagen und andere Dateien kannst du später in den Ordner legen.

## Check your understanding
Question: Du hast drei Skills installiert. Welchen Teil liest die KI, um zu entscheiden, ob sie einen davon für deine Anfrage nutzt?
- A: Die nummerierten Schritte in den Anweisungen
- B: Name und Beschreibung im Skill-Kopf
- C: Die Beispiele am Ende der Datei
- D: Alle drei, jedes Mal
Answer: B
Why: Nur der Skill-Kopf, wenige Zeilen pro Skill, wird immer gelesen. Anweisungen und Beispiele laden erst, nachdem die KI den Skill anhand seiner Beschreibung gewählt hat, und bei D wäre der Kontext mit allen Skills auf einmal gefüllt.

## Working example
Situation: Nach jedem **Team-Meeting** machst du aus deinen Notizen eine **Follow-up-Mail**.
Input: Deine **Meeting-Notizen**, ohne Kundennamen.
- Schreib in kurzen Punkten, was das Team **vereinbart** hat.
- Liste die **nächsten Schritte** auf, jeweils mit Datum.
- Frag nach dem **Datum**, wenn ein Schritt keins hat, statt zu raten.
Result: Ein **Skill**, der die Follow-up-Mail nach jedem Meeting auf dieselbe Weise schreibt.

## Steps
### Auslöser
Use: Nimm eine eigene Aufgabe oder das Arbeitsbeispiel unten. Am besten eignen sich Aufgaben, die du **wiederholst**, mit einem Ergebnis in **derselben Form**, bei denen du weißt, wie **gut** aussieht.
Why: Die Beschreibung ist der **einzige Teil**, den die KI liest, bevor sie entscheidet: Ist sie vage, lädt der Skill nie, und ist sie zu weit, lädt er bei den falschen Anfragen.
Do: Schreib den **Namen** und eine **[[Beschreibung]]** von etwa 200 Zeichen: was der Skill tut, **wann** er genutzt wird und **wann nicht**.
Ask: Sende deinen **[[Skill-Kopf]]**, also Name und Beschreibung, im Chat.
Code:
```text
---
name: [was-der-skill-tut-mit-bindestrichen]
description: [Tut was] für [wen]. Verwenden, wenn [Worte, die jemand tippen würde]. Nicht verwenden für [eine ähnliche Anfrage, die etwas anderes braucht].
---
```
Example:
```text
---
name: complaint-reply-drafts
description: Entwirft Antworten auf Kundenbeschwerden in unserem Support-Ton, mit Entschuldigung, Lösung und nächstem Schritt. Verwenden, wenn der Nutzer eine Beschwerde-E-Mail einfügt oder um eine Antwort auf eine Beschwerde bittet. Nicht verwenden für Vertriebs-E-Mails oder interne Nachrichten.
---
```
Weak:
```text
---
name: My Email Helper
description: Ich helfe bei E-Mails.
---
```

### Anweisungen
Why: Jeder Schritt muss eine **konkrete Handlung** sein: „Sei professionell“ ist vage, also rät die KI, aber „Beginne mit einem Satz, der das Problem nennt“ setzt sie jedes Mal gleich um.
Do: Schreib deine **Schritte**, **eine Handlung** pro Schritt, und das **[[Ausgabeformat]]**.
Ask: Schick sie in den Chat.
Code:
```text
# Schritte
1. [erste Handlung]
2. [nächste Handlung]
3. [nächste Handlung]

# Ausgabeformat
[Länge], [Aufbau], [Sprache]
```
Example:
```text
# Schritte
1. Nenne das Problem des Kunden in einem Satz, in seinen Worten.
2. Entschuldige dich einmal, für genau dieses Problem.
3. Nenne die Lösung oder den nächsten Schritt, mit Datum, wenn die Beschwerde eins nennt.
4. Schließe mit einer Kontaktzeile.

# Ausgabeformat
Höchstens 120 Wörter. Reiner Text, keine Aufzählungspunkte. Gleiche Sprache wie die Beschwerde.
```
Weak:
```text
Schreibe eine nette, professionelle Antwort, die den Kunden glücklich macht.
```

### Prüfungen
Why: Fehlt eine Angabe, füllt die KI die Lücke mit etwas, das richtig klingt, und das Ergebnis **sieht korrekt aus, obwohl es falsch ist**.
Do: Schreib **eine Regel** für den Fall, dass eine Angabe fehlt, und **ein [[VERIFY-Kennzeichen]]** für das, was ein Mensch prüfen muss.
Ask: Schick deine zwei Zeilen in den Chat.
Code:
```text
# Wenn etwas fehlt
- Wenn [Angabe] fehlt, frage danach. Rate nie.

# Vor der Antwort prüfen
- [VERIFY] [die Zahl, das Datum oder der Name, die zur Eingabe passen müssen]
```
Example:
```text
# Wenn etwas fehlt
- Wenn die Bestellnummer fehlt, frage danach. Erfinde nie eine.

# Vor der Antwort prüfen
- [VERIFY] Jeder Erstattungsbetrag und jedes Datum steht in der Beschwerde oder in dem, was der Nutzer gesagt hat.
```
Weak:
```text
Sei genau und prüfe alles doppelt.
```

### Weiter vertiefen [fast-track]
Why: Wenn du mehrere Skills hast, können zwei Beschreibungen um **dieselbe Anfrage** konkurrieren, und die KI wählt vielleicht den falschen.
Do: Schreib den Kopf eines **zweiten Skills**, der deinem ähnelt (zum Beispiel die interne Version derselben Aufgabe), sodass jede Beschreibung die andere als ihren **Beinahe-Treffer** nennt.
Ask: Sende beide Skill-Köpfe.
Example:
```text
complaint-reply-drafts: ... Nicht verwenden für interne Eskalationsnotizen.
complaint-escalation-notes: Schreibt die interne Notiz zu einer Beschwerde an die Teamleitung. Nicht verwenden für Antworten an den Kunden.
```

## Trust check
Watch for:
- Halte **echte Namen und Kundendaten** aus dem Skill heraus. Er wird gespeichert, wiederverwendet und später vielleicht geteilt. (DSGVO, Artikel 5)
- Setze ein **[VERIFY]**-Kennzeichen an jeden Schritt, bei dem eine falsche Zahl, ein falsches Datum oder ein falscher Name jemanden erreichen könnte. (EU AI Act, Artikel 4)
- Wenn du mit einem **echten Dokument** testest, entferne vorher **personenbezogene und vertrauliche Daten**, vor allem in einem kostenlosen KI-Tool. (DSGVO, Artikel 5)
Rules:
- DSGVO, Artikel 5: Personenbezogene Daten müssen dem Zweck angemessen und erheblich sowie auf das für den Zweck notwendige Maß beschränkt sein. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de)
- EU AI Act, Artikel 4: Organisationen, die KI-Systeme anbieten oder nutzen, müssen dafür sorgen, dass ihr Personal für seine Rolle genug KI-Kompetenz hat: Es versteht die Werkzeuge und weiß, was die Ergebnisse bedeuten. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=de)
- Schweizer DSG, Artikel 6: Für Lernende in der Schweiz gilt: Personendaten müssen rechtmäßig, nach Treu und Glauben und verhältnismäßig bearbeitet werden. [Fedlex](https://www.fedlex.admin.ch/eli/cc/2022/491/de)
Ask: Welcher Schritt in deinem Skill könnte etwas erzeugen, das **richtig aussieht, aber falsch ist**?

## Test
Do:
1. Lade deine **SKILL.md** aus dem Chat herunter.
2. Öffne in Claude einen **[[neuen Chat|Neuer Chat]]** außerhalb jedes Projekts.
3. Schalte den **Inkognito-Chat** ein (das Geist-Symbol oben rechts), damit dein Gedächtnis die Antwort nicht beeinflusst.
4. Hänge deine **SKILL.md** an und schreib: **„Nutze diesen Skill. Erfinde ein kurzes Beispiel für das Dokument, das er bearbeitet, ohne echte Daten und mit einer fehlenden Angabe, und wende den Skill darauf an.“**
5. Lieber ein eigenes Dokument? Schreib **„Nutze diesen Skill für dieses Dokument:“** und füge es darunter ein.
Check:
- Die Ausgabe folgt deinen **Anweisungen und dem Format** ohne Nacharbeit.
- Wo die Beispieleingabe etwas auslässt, **fragt** die KI nach, statt zu raten.
- Wer nur deine Beschreibung liest, kann sagen, **wann** der Skill laufen soll.
Ask: Ist die Ausgabe deinem Skill gefolgt? Schreib mir, was du erwartet hast und was herauskam.

## Test [claude-code]
Do:
1. Speichere deinen Skill als **~/.claude/skills/[name]/SKILL.md**.
2. Starte **claude** in einem Ordner ohne Projektdateien.
3. Bitte es, deine Aufgabe an **einem kurzen erfundenen Beispiel** zu erledigen, ohne echte Daten und mit einer fehlenden Angabe.
Check:
- Claude Code meldet für das Beispiel, dass es **deinen Skill nutzt**.
- Die Ausgabe folgt deinen **Anweisungen und dem Format** ohne Nacharbeit.
- Wo die Beispieleingabe etwas auslässt, **fragt** die KI nach, statt zu raten.
Ask: Hat dein Skill geladen, und ist die Ausgabe ihm gefolgt? Schreib mir, was du erwartet hast und was herauskam.

## Test [chatgpt]
Do:
1. Lade deine **SKILL.md** aus dem Chat herunter.
2. Öffne in ChatGPT einen **[[neuen Chat|Neuer Chat]]** außerhalb jedes Projekts.
3. Schalte oben den **temporären Chat** ein, damit dein Gedächtnis die Antwort nicht beeinflusst.
4. Hänge deine **SKILL.md** an und schreib: **„Nutze diesen Skill. Erfinde ein kurzes Beispiel für das Dokument, das er bearbeitet, ohne echte Daten und mit einer fehlenden Angabe, und wende den Skill darauf an.“**
5. Lieber ein eigenes Dokument? Schreib **„Nutze diesen Skill für dieses Dokument:“** und füge es darunter ein.
Check:
- Die Ausgabe folgt deinen **Anweisungen und dem Format** ohne Nacharbeit.
- Wo die Beispieleingabe etwas auslässt, **fragt** die KI nach, statt zu raten.
- Wer nur deine Beschreibung liest, kann sagen, **wann** der Skill laufen soll.
Ask: Ist die Ausgabe deinem Skill gefolgt? Schreib mir, was du erwartet hast und was herauskam.

## Test [gemini]
Do:
1. Lade deine **SKILL.md** aus dem Chat herunter.
2. Öffne in der Gemini-App einen **[[neuen Chat|Neuer Chat]]**.
3. Schalte den **temporären Chat** ein, damit frühere Chats die Antwort nicht beeinflussen.
4. Hänge deine **SKILL.md** an und schreib: **„Nutze diesen Skill. Erfinde ein kurzes Beispiel für das Dokument, das er bearbeitet, ohne echte Daten und mit einer fehlenden Angabe, und wende den Skill darauf an.“**
5. Lieber ein eigenes Dokument? Schreib **„Nutze diesen Skill für dieses Dokument:“** und füge es darunter ein.
Check:
- Die Ausgabe folgt deinen **Anweisungen und dem Format** ohne Nacharbeit.
- Wo die Beispieleingabe etwas auslässt, **fragt** die KI nach, statt zu raten.
- Wer nur deine Beschreibung liest, kann sagen, **wann** der Skill laufen soll.
Ask: Ist die Ausgabe deinem Skill gefolgt? Schreib mir, was du erwartet hast und was herauskam.

## Test [no-skills]
Do:
1. Lade deine **SKILL.md** aus dem Chat herunter.
2. Öffne in deinem KI-Chat einen **[[neuen Chat|Neuer Chat]]** außerhalb jedes Projekts.
3. Nutze den **temporären oder privaten Chat**, falls es einen gibt, damit dein Gedächtnis die Antwort nicht beeinflusst.
4. Hänge deine **SKILL.md** an (oder füge ihren Text ein) und schreib: **„Nutze diesen Skill. Erfinde ein kurzes Beispiel für das Dokument, das er bearbeitet, ohne echte Daten und mit einer fehlenden Angabe, und wende den Skill darauf an.“**
5. Lieber ein eigenes Dokument? Schreib **„Nutze diesen Skill für dieses Dokument:“** und füge es darunter ein.
Check:
- Die Ausgabe folgt deinen **Anweisungen und dem Format** ohne Nacharbeit.
- Wo die Beispieleingabe etwas auslässt, **fragt** die KI nach, statt zu raten.
- Wer nur deine Beschreibung liest, kann sagen, **wann** der Skill laufen soll.
Ask: Ist die Ausgabe deinem Skill gefolgt? Schreib mir, was du erwartet hast und was herauskam.

## Other ways
- Cowork: Bitte Cowork, **deinen Text** als SKILL.md in einem Skill-Ordner in deinem verbundenen Ordner zu speichern, bereit zur Installation.
- skill-creator: Bitte Claude, **den skill-creator zu nutzen**, damit er dich befragt und einen Skill entwirft. Prüfe dann jede Zeile so wie hier.

## Other ways [claude-code]
- Beim Namen aufrufen: Tippe **/[name]** am Anfang einer Nachricht, um deinen Skill **gezielt** auszuführen, auch wenn die Beschreibung ihn nicht auslösen würde.
- skill-creator: Bitte Claude Code, **den skill-creator zu nutzen**, damit er dich befragt und einen Skill entwirft. Prüfe dann jede Zeile so wie hier.
- Claude-App: Lade denselben Ordner als ZIP-Datei unter **Anpassen > Skills** (Customize > Skills) hoch, um den Skill auch im Claude-Chat und in Cowork zu nutzen.

## Other ways [chatgpt]
- Mit Chat erstellen: Wähle unter **Plugins > Skills** die Option **Mit Chat erstellen** (Create with chat) und lass dich von ChatGPT befragen. Prüfe dann jede Zeile so wie hier.
- Codex: Speichere den Ordner in **~/.agents/skills/** und ruf ihn mit **$[name]** auf.
- Claude: Dieselbe SKILL.md funktioniert ohne Änderungen in den **Claude-Apps** und in Claude Code.

## Other ways [gemini]
- Mit Gemini erstellen: Wähle unter **Einstellungen > Skills** die Option **Mit Gemini erstellen** (Create with Gemini). Prüfe dann jede Zeile so wie hier.
- Gemini CLI: Speichere den Ordner in **~/.gemini/skills/** und tippe **/skills list**, um ihn zu sehen.
- Claude: Dieselbe SKILL.md funktioniert ohne Änderungen in den **Claude-Apps** und in Claude Code.

## Other ways [no-skills]
- Projekt oder Gem: Füge die Anweisungen in die **Projektanweisungen** (ChatGPT) oder in ein **Gem** (Gemini) ein. Sie gelten dort für jeden Chat, deshalb löst die Beschreibung nichts aus.
- Prompt-Bibliothek: Speichere die SKILL.md als Datei und füge sie in einen **neuen Chat** ein, wenn die Aufgabe ansteht.
- Später: Wenn dein Werkzeug oder Tarif Skills bekommt, funktioniert dieselbe SKILL.md **ohne Änderungen**.

## Done when
- Deine SKILL.md hat einen Namen, eine Beschreibung mit Beinahe-Treffer, nummerierte Anweisungen und ein Ausgabeformat.
- Sie hat mindestens eine Regel „fragen, nie raten“ und ein [VERIFY]-Kennzeichen.
- Deine Testausgabe brauchte keine Nacharbeit, oder du weißt, welchen Teil du als Nächstes verbesserst.

## Practice
- Schreib einen zweiten Beinahe-Treffer und prüfe, ob deine Beschreibung ihn schon ausschließt.
- Setze ein weiteres [VERIFY]-Kennzeichen an den Schritt, dem du am wenigsten traust.
- Schreib eine Anweisung, die eine Eigenschaft beschreibt („sei klar“), als Handlung um („ein Satz pro Punkt“).

## Reusable template
Name: Vorlage Skill v1
```text
---
name: [was-der-skill-tut-kleingeschrieben-mit-bindestrichen]
description: [Tut was] für [wen]. Verwenden, wenn [Worte, die ein Nutzer sagen würde]. Nicht verwenden für [den Beinahe-Treffer].
---

[Titel des Skills]

# Schritte
1. [erste Handlung]
2. [nächste Handlung]
3. [nächste Handlung]

# Ausgabeformat
[Länge, Aufbau, Sprache]

# Wenn etwas fehlt
- Wenn [Angabe] fehlt, frage danach. Rate nie.

# Vor der Antwort prüfen
- [VERIFY] [die Zahl, das Datum oder der Name, die zur Eingabe passen müssen]
```

## Glossary
- Skill: Ein Ordner mit einer SKILL.md-Datei voller Anweisungen, die die KI nur lädt, wenn eine Aufgabe sie braucht.
- Auslöser: Die Übereinstimmung zwischen einer Anfrage und der Beschreibung eines Skills, durch die die KI den Skill lädt.
- Beschreibung: Der Teil im Kopf eines Skills, der sagt, was er tut, wann er genutzt wird und wann nicht. Die KI liest ihn, um zu entscheiden.
- Ausgabeformat: Die Form der Antwort: Länge, Aufbau, Abschnitte und Sprache.
- VERIFY-Kennzeichen: Eine Markierung in einem Skill für einen Schritt, dessen Ausgabe ein Mensch prüfen muss, bevor sie genutzt wird.
- Beinahe-Treffer: Eine Anfrage, die deiner Aufgabe ähnelt, aber etwas anderes braucht. Der Skill darf dafür nicht starten.
- Skill-Kopf: Der Block zwischen den beiden ---Zeilen oben in der SKILL.md, mit Name und Beschreibung.
- Neuer Chat: Ein neuer Chat ohne frühere Nachrichten und mit ausgeschaltetem Gedächtnis, sodass nur dein Skill und deine Anfrage die Antwort bestimmen.

## Sources
- [Anthropic: Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): Der Aufbau eines Skills und warum nur Name und Beschreibung, wenige Zeilen pro Skill, immer gelesen werden.
- [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices): Wie du die Beschreibung in der dritten Person schreibst, mit dem, was der Skill tut, und wann er genutzt wird.
- [Claude Help Centre: How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills): Was in eine SKILL.md gehört und warum Passwörter oder Schlüssel nicht in einen Skill gehören.
- [Agent Skills specification](https://agentskills.io/specification): Der offene Standard: Name bis 64 Zeichen, Beschreibung bis 1.024, auch von ChatGPT, Gemini CLI und anderen genutzt.
- [Anthropic: The complete guide to building skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf): Die Schätzung von 15 bis 30 Minuten für einen ersten Skill und die Regeln für Namen.
- [Matt Pocock: Building Great Agent Skills (AI Engineer)](https://www.youtube.com/watch?v=UNzCG3lw6O0): Warum jeder automatische Skill Kontext hinzufügt und warum ein klarer Auslöser ihn vorhersehbar hält.

## Coach notes
Arc: first of five in this topic (write the skill; install it and add an example; test and fix; reference files and templates; connect and get ready to share). Never name the other missions by number to the learner. Levels covered: spot a task, trigger, steps, a first guard. The learner leaves with the simplest skill that works.
Levels (from the topic's level question, see SKILL.md): guided (A, B) uses the working example or a simple own task, sees each step's example before writing, and hears plain words only; standard (C) tries first, then sees the example; fast-track (D) may test out by pasting an existing skill that meets Done when, and gets the Go further step (overlapping descriptions). Technical words (token, frontmatter, MCP) only for fast-track or once the learner uses them.
Guided mode (default for beginners): before a beginner writes each part, point to the step's "See an example" on the page, say in one sentence why it works (for example: "it names a near miss"), then ask for their version for their own case. Some familiarity: they try first and you point to the example after the first try. Experienced: only when they ask. The example is from a different case, so they adapt it instead of copying it; if they copy it word for word, ask what changes for their task. Beginners can also take the working example instead of their own task, so the page example and their task differ only in the details.
Own task (standard and fast-track only; skip for guided to save time): when the learner picks their own task, ask once which parts the AI should do and which stay with them (judgement, sign-off). Pilot learners asked for this task split before writing the skill. Keep it to one question.
Pilot feedback to respect: never ask the learner to guess what the page has just explained; never draft the whole skill before they write it (pilot learners lost motivation when asked to rewrite a skill Claude had already written); ask for short answers where possible.
Likely errors: the name has capitals or spaces; the description says what but not when, or has no near miss; the description is in the first person ("I help..."); instructions describe qualities ("be professional") instead of actions; no rule for missing information, so the skill guesses; a real email with client names pasted into the skill as an example.
People data (HR, candidates, health): only made-up or anonymised samples; the decision about a person stays with a person; company rules and, in Germany, the works council decide what may be pasted into an AI tool. The EU AI Act treats AI used to select or evaluate candidates as high-risk, so a skill like this only drafts and a person decides.
Feedback: name the part that works, then the one gap, then one fix. For the description, ask: "Which request would someone send that looks like this but is not this task?"
Real case for the near miss: a pilot learner's text-compression skill triggered on "summarise" and kept firing for summaries, a different task. Use it when a learner's trigger is too broad.
Description language: the sources do not say which language works best. If the learner works in two languages, suggest naming trigger words in both and checking it in the install-and-test mission; do not claim more.
Page state: set the full skill as the part for the last step (Checks; Go further for fast-track) when it is final, so the learner can copy it.
Claude Code: in the claude-code variant the test already saves the skill in ~/.claude/skills/ and tests the trigger, so the install step in the next mission becomes a quick check. Start the test in a new session in a folder without a CLAUDE.md, so nothing else shapes the result.
Skill or something else (experienced learners): a skill fits a repeated task with a fixed shape; a CLAUDE.md or project instructions fit rules that apply to every request; a plain script fits a step with no judgement at all.
Test: deliver the learner's SKILL.md as a downloadable draft file before the test (SKILL.md rule in SKILL.md §8). Attaching it tests the steps, not the automatic start; say so plainly. If the result shows something to refine, they change it in this chat and you deliver the updated file.
Time budget for guided learners (30 minutes in total, profile and level question included): about 4 to 5 minutes per build step. They copy the step's fill-in lines and fill the [blanks]; they never write a part from an empty page. If a step runs over 8 minutes, accept a short version and note one improvement for later.
Time: allow at most two feedback rounds per step; if a part is still weak, note it as something to fix later and move on. If the learner's own task is complex, keep the sample input for the test short (5 to 10 lines). If time runs out, the test can open the next session.
Other vendors: ChatGPT and Codex read the same SKILL.md (ChatGPT skills on eligible Business, Enterprise and Edu workspaces, called with @skill); the Gemini app is replacing Gems with skills (personal accounts from November 2026), called with "/". Where equivalence breaks: a Custom GPT's or Gem's instructions are always on and do not trigger, so the description has no effect there.
