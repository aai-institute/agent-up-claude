---
id: mission-4-add-reference-files-and-templates
number: 4
title: Füge Referenzdateien und Vorlagen hinzu
summary: Leg die Listen und Vorlagen, die du jedes Mal einfügst, in den Ordner deines Skills, damit er kurz bleibt und jedes Mal dasselbe Layout ausfüllt. Am Ende hast du einen Skill-Ordner v4.
artefact: "Skill v4: Skill-Ordner mit Referenzdatei und Vorlage"
---

Track: Baseline
Level: practitioner
Time: 30 Minuten
Tools: Claude-Chat, Cowork oder Claude Code
Artefact kind: text
Artefact file: my-skill-v4.md

## Context
Du fügst bei deinem Skill noch immer dieselbe **Liste** ein oder korrigierst dasselbe **Layout**, und alles in die SKILL.md zu schreiben, würde den Skill lang und schwerer verständlich machen. Eine **Referenzdatei** und eine **Vorlage** im Skill-Ordner übernehmen das für dich und halten den Skill kurz.

## Your task
Verschiebe einen Block **Referenzmaterial** in eine **[[Referenzdatei]]** mit einem **Verweis**, füge eine **Vorlage** (ein **[[Asset]]**) hinzu, die dein Skill ausfüllt, und lösche Zeilen, die **nichts ändern**.

## After this, you can
Du kannst für jedes Material entscheiden, ob es in SKILL.md, in references/ oder in assets/ gehört, und so darauf verweisen, dass es nur bei Bedarf lädt.

## You need
- Deine **SKILL.md**, mindestens einmal getestet, oder das **Arbeitsbeispiel** in dieser Mission
- Einen Block **Referenzmaterial**, den du immer wieder einfügst (eine Liste von Kategorien, Stilregeln, Produktnamen), und eine **Vorlage**, der deine Ausgabe folgt
- **Claude** mit eingeschalteten Skills

## You need [claude-code]
- Deine **SKILL.md**, mindestens einmal getestet, oder das **Arbeitsbeispiel** in dieser Mission
- Einen Block **Referenzmaterial**, den du immer wieder einfügst (eine Liste von Kategorien, Stilregeln, Produktnamen), und eine **Vorlage**, der deine Ausgabe folgt
- Deinen Skill-Ordner in **~/.claude/skills/[name]/**

## You need [chatgpt, gemini]
- Deine **SKILL.md**, mindestens einmal getestet, oder das **Arbeitsbeispiel** in dieser Mission
- Einen Block **Referenzmaterial**, den du immer wieder einfügst (eine Liste von Kategorien, Stilregeln, Produktnamen), und eine **Vorlage**, der deine Ausgabe folgt
- Deinen Skill, in deinem Werkzeug **installiert**

## You need [no-skills]
- Deine **SKILL.md**, mindestens einmal getestet, oder das **Arbeitsbeispiel** in dieser Mission
- Einen Block **Referenzmaterial**, den du immer wieder einfügst (eine Liste von Kategorien, Stilregeln, Produktnamen), und eine **Vorlage**, der deine Ausgabe folgt
- Dein **Projekt** oder **Gem**, das neben den Anweisungen auch **Dateien** speichern kann

## You should already
- Einen **Skill installieren** und einen Test in einem **neuen Chat** ausführen können

## Concept
Heading: Die 3 Teile eines Skill-Ordners
Lead: Ein Skill ist ein **Ordner**. SKILL.md enthält, was **jede** Anfrage braucht; die anderen Ordner enthalten, was **manchmal** oder **im Ergebnis** gebraucht wird.
- SKILL.md: Der Skill-Kopf und die **Schritte**. Die KI liest die Datei **jedes Mal**, wenn der Skill läuft, deshalb bleibt sie kurz.
- references/: **Wissen**, das die KI nur öffnet, wenn ein Schritt darauf verweist: Regeln, Listen, Definitionen.
- assets/: **Dateien für das Ergebnis**, nicht als Anweisungen befolgt: eine Vorlage zum Ausfüllen, ein Logo, ein Beispiel-Layout.
Close: Ein **[[Verweis]]** mit einer Bedingung entscheidet, wann eine Datei geöffnet wird (**[[progressive Offenlegung]]**).
Toggle: Warum nicht ein langer Skill? | Alles in der SKILL.md wird bei **jedem** Lauf gelesen, zusammen mit deiner Anfrage und deinen Dateien. Eine lange Liste, die nur manche Anfragen brauchen, macht es leichter, die wichtigen Schritte zu übersehen; Anthropic rät zu **kurzen, fokussierten** Skills (unter **500 Zeilen**).
Toggle: Was bringt mir eine eigene Datei noch? | Du aktualisierst eine Liste **an einer Stelle**, ohne die Schritte anzufassen, und du siehst auf einen Blick, was der Skill weiß und was er tut.
Toggle: Gibt es einen vierten Ordner? | Ja: **scripts/**, für Schritte, die jedes Mal exakt gleich berechnet werden müssen. Für diese Aufgabe brauchst du ihn nicht.

## Check your understanding
Question: Dein Skill schreibt einen Monatsbericht. Jeder Bericht muss demselben Layout im Word-Stil folgen, und nur Berichte für den Vorstand brauchen die Liste mit 40 Risikokategorien. Wohin gehört was?
- A: Beides in SKILL.md, damit nichts fehlt
- B: Das Layout in assets/, die Risikoliste in references/ mit einem Verweis für Vorstandsberichte
- C: Das Layout in references/, die Risikoliste in assets/
- D: Beides in references/, ohne Verweis
Answer: B
Why: Das Layout wird in jeder Ausgabe genutzt, also ist es ein Asset, das die Schritte ausfüllen. Die Risikoliste ist Wissen, das nur Vorstandsberichte brauchen, also liegt sie in references/, und ein Verweis mit Bedingung öffnet sie nur dann. Bei A lädt alles jedes Mal; bei D werden die Dateien nie oder immer gelesen.

## Working example
Situation: Dein **Skill für das Status-Update** schreibt ein wöchentliches Update. Für Vorstandsversionen fügst du die **Risikokategorien** ein, und das **Layout** korrigierst du jedes Mal von Hand.
Input: Dein **getesteter Skill** (etwa 25 Zeilen), die Liste der Risikokategorien und das Layout des Updates.
- Die Kategorien nach **references/risk-categories.md** verschieben, mit einem Verweis für Vorstandsupdates.
- Das Layout als **assets/update-template.md** speichern und einen Schritt zum Ausfüllen hinzufügen.
- Eine Zeile löschen, die **nichts ändert**.
Result: Ein **Skill-Ordner v4**, der kurz bleibt, jedes Mal dasselbe Layout ausfüllt und die Kategorien nur bei Bedarf liest.
Ask: Willst du an einem eigenen Skill arbeiten oder am Arbeitsbeispiel? Sag mir, was du bei jeder Nutzung einfügst oder von Hand korrigierst.

## Steps
### Referenz
Use: Arbeite an einem Skill, den du geschrieben hast, oder am Arbeitsbeispiel unten.
Why: Wissen, das nur **manche** Anfragen brauchen, gehört nicht in die immer geladenen Schritte, und eine Datei, auf die nichts verweist, wird **nie gelesen**.
Do: Füge eine Liste, die du **schon hast** (höchstens 10 Zeilen), als Referenzdatei in den Chat ein, gib ihr einen Namen und füge deinen Schritten einen **Verweis** hinzu, der die Datei nennt und sagt, **wann** sie gelesen wird. Claude legt sie in **references/** ab, wenn es deine ZIP baut.
Ask: Sende den Dateinamen, was darin steht, und deine Verweiszeile.
Code:
```text
Datei: references/[name].md
Verweis: [n]. Wenn [Bedingung], lies references/[name].md, bevor du antwortest.
```
Example:
```text
Datei: references/refund-rules.md (die 5 Erstattungsfälle mit ihren Grenzen)
Verweis: 3. Wenn die Beschwerde eine Erstattung erwähnt, lies references/refund-rules.md, bevor du antwortest.
```
Weak:
```text
Alle Schritte nach references/steps.md verschoben. Verweis: Siehe Ordner references für weitere Informationen.
```

### Referenz [no-skills]
Use: Arbeite an einem Skill, den du geschrieben hast, oder am Arbeitsbeispiel unten.
Why: Wissen, das nur **manche** Anfragen brauchen, gehört nicht in die Anweisungen, und eine Datei, auf die nichts verweist, wird **nie gezielt** genutzt.
Do: Speichere einen Block Referenzmaterial als **eigene Datei**, füge sie deinem **Projekt** oder **Gem** hinzu und ergänze deine Anweisungen um einen **Verweis**, der die Datei nennt und sagt, **wann** sie genutzt wird.
Ask: Sende den Dateinamen, was darin steht, und deine Verweiszeile.
Example:
```text
Datei: refund-rules.md (die 5 Erstattungsfälle mit ihren Grenzen)
Verweis: 3. Wenn die Beschwerde eine Erstattung erwähnt, nutze refund-rules.md, bevor du antwortest.
```
Weak:
```text
Alle meine Anweisungen als Datei hochgeladen, das Anweisungsfeld ist jetzt leer.
```

### Vorlage
Why: Eine Vorlage, die die KI **ausfüllt**, ergibt jedes Mal dasselbe Layout, statt eines Layouts, das sie aus einer Beschreibung neu baut.
Do: Füge ein Ergebnis ein, das du **schon hast** (höchstens 8 Zeilen), ersetze die Teile, die sich ändern, durch **[Platzhalter]**, nenne es **assets/[vorlagenname].md** und füge einen Schritt hinzu, der der KI sagt, **diese Vorlage auszufüllen**.
Ask: Sende deine Vorlage und den Schritt, der sie nutzt.
Code:
```text
assets/[name].md:
[füge ein Ergebnis ein, das du schon hast, mit [Platzhaltern] für die Teile, die sich ändern]

Schritt: [n]. Fülle assets/[name].md aus. Behalte die Reihenfolge; ersetze nur die [Platzhalter].
```
Example:
```text
assets/reply-template.md:
Betreff: [kurzes Problem]
Guten Tag [Name], [Entschuldigung für das Problem]. [Lösung und Datum]. [Kontaktzeile]

Schritt: 4. Fülle assets/reply-template.md aus. Behalte Reihenfolge und Überschriften; ersetze nur die [Platzhalter].
```
Weak:
```text
Schritt: 4. Lass es wie unsere üblichen Antworten aussehen.
```

### Vorlage [no-skills]
Why: Eine Vorlage, die die KI **ausfüllt**, ergibt jedes Mal dasselbe Layout, statt eines Layouts, das sie aus einer Beschreibung neu baut.
Do: Speichere das Layout, dem deine Ausgabe immer folgt, als **Vorlagendatei** mit **[Platzhaltern]**, füge sie deinem Projekt oder Gem hinzu und ergänze eine Anweisung, die der KI sagt, **diese Vorlage auszufüllen**.
Ask: Sende deine Vorlage und die Anweisung, die sie nutzt.
Code:
```text
[name].md:
[füge ein Ergebnis ein, das du schon hast, mit [Platzhaltern] für die Teile, die sich ändern]

Anweisung: [n]. Fülle [name].md aus. Behalte die Reihenfolge; ersetze nur die [Platzhalter].
```
Example:
```text
reply-template.md:
Betreff: [kurzes Problem]
Guten Tag [Name], [Entschuldigung für das Problem]. [Lösung und Datum]. [Kontaktzeile]

Anweisung: 4. Fülle reply-template.md aus. Behalte Reihenfolge und Überschriften; ersetze nur die [Platzhalter].
```
Weak:
```text
Anweisung: 4. Lass es wie unsere üblichen Antworten aussehen.
```

### Kürzen [standard, fast-track]
Why: Jede Zeile in der SKILL.md wird bei jedem Lauf gelesen. Zeilen, die nichts ändern, machen die **wichtigen Zeilen** leichter übersehbar; sobald Vorlage und Liste ihre Arbeit tun, braucht es manche alten Zeilen nicht mehr. Nutze überall **einen Namen** für deine Hauptidee (einen **[[Leitbegriff]]**), dann hält die KI nicht zwei Namen für zwei verschiedene Dinge.
Do: Entferne **eine Zeile nach der anderen**, bei der du zweifelst, und führe den Test aus, der ihre Wirkung zeigen kann: Bleibt die Ausgabe gleich, **lösch sie**. Das ist der **[[Löschtest]]**. Verwende deinen **Leitbegriff** gleich in der Beschreibung, den Schritten und der Vorlage.
Ask: Sende die gelöschten Zeilen und deinen Leitbegriff; dein vollständiger **Skill v4** erscheint auf der Seite.
Example:
```text
Gelöscht: „Nutze eine klare Struktur“ (das macht jetzt die Vorlage), „Sei immer höflich“ (stand zweimal da).
Behalten: „Wenn die Bestellnummer fehlt, frage danach“ (ohne die Zeile hat die Ausgabe eine erfunden).
Leitbegriff: „Lösung-zuerst-Antwort“, in der Beschreibung, in Schritt 1 und im Titel der Vorlage.
```
Weak:
```text
Alles ist wichtig, also habe ich alles behalten.
```

### Weiter vertiefen [fast-track]
Why: Ein Agent, der einen **langen Ablauf** auf einmal sieht, hetzt oft durch die frühen Schritte, um ans Ende zu kommen; wenn du ihn in **Phasen** teilst, bleibt jeder Schritt gründlich.
Do: Teile deine Schritte in **zwei Phasen** (zum Beispiel „sammeln“ und „schreiben“), mit einer Prüfung dazwischen, und gib jeder Referenzdatei mit mehr als 100 Zeilen ein kurzes **Inhaltsverzeichnis**.
Ask: Sende deine zwei Phasen und die Prüfung dazwischen.

## Trust check
Watch for:
- Halte **echte Kundendaten** aus Referenzen und Assets heraus; nutze **[Platzhalter]** in Vorlagen. (DSGVO, Artikel 5)
- Prüfe, dass eine Referenzdatei keinem [VERIFY]-Kennzeichen und keiner Regel „fragen, nie raten“ **widerspricht**. (EU AI Act, Artikel 4)
- Wenn du eine Datei hinzufügst, die du nicht selbst geschrieben hast (eine Vorlage aus dem Netz, ein Logopaket), **lies oder öffne sie**, bevor du sie hochlädst. (Anthropic Skill-Sicherheit)
Rules:
- DSGVO, Artikel 5: Personenbezogene Daten müssen dem Zweck angemessen und erheblich sowie auf das für den Zweck notwendige Maß beschränkt sein. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de)
- EU AI Act, Artikel 4: Organisationen, die KI-Systeme anbieten oder nutzen, müssen dafür sorgen, dass ihr Personal für seine Rolle genug KI-Kompetenz hat: Es versteht die Werkzeuge und weiß, was die Ergebnisse bedeuten. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=de)
- Anthropic Skill-Sicherheit: Nutze nur Skills und Dateien, die du selbst erstellt oder aus einer vertrauenswürdigen Quelle hast, und prüfe vorher jede Datei, denn ein Skill kann Code ausführen und Webinhalte abrufen. [Anthropic-Dokumentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
Ask: Was in deiner Referenzdatei oder Vorlage könnte in drei Monaten **veraltet** sein, und wie merkst du das?

## Test
Do: Bitte Claude in einem Chat, die **neue ZIP** mit deinen Ordnern zu bauen, lade sie hoch und schalte die alte Version **aus**. Sende dann eine Anfrage, die **die Referenzdatei braucht**, in einem **neuen Chat**, und eine, die sie **nicht** braucht, in **einem weiteren neuen Chat**.
Check:
- Claude liest die Referenzdatei **nur** für die Anfrage, die sie braucht.
- Beide Ausgaben folgen genau deiner **Vorlage**.
- SKILL.md ist **nicht länger** als vorher, oder nur um die neuen Schrittzeilen länger.
Ask: Hat Claude die Referenzdatei nur bei Bedarf geöffnet und beide Male die Vorlage ausgefüllt? Schreib mir, was du erwartet hast und was herauskam.

## Test [claude-code]
Do: Speichere **references/** und **assets/** in deinem Skill-Ordner, starte eine **neue Sitzung**, sende eine Anfrage, die **die Referenzdatei braucht**, und in einer weiteren neuen Sitzung eine, die sie **nicht** braucht.
Check:
- Die Tool-Aufrufe zeigen, dass die Referenzdatei **nur** für die Anfrage gelesen wird, die sie braucht.
- Beide Ausgaben folgen genau deiner **Vorlage**.
- SKILL.md ist **nicht länger** als vorher, oder nur um die neuen Schrittzeilen länger.
Ask: Hat Claude Code die Referenzdatei nur bei Bedarf gelesen und beide Male die Vorlage ausgefüllt? Schreib mir, was du erwartet hast und was herauskam.

## Test [gemini]
Do: Lade den **ganzen Skill** mit seinen Ordnern **erneut hoch** und sende dann eine Anfrage, die **die Referenzdatei braucht**, in einem **neuen Chat**, und eine, die sie **nicht** braucht, in **einem weiteren neuen Chat**.
Check:
- Nur die erste Antwort nutzt Details, die **nur in der Referenzdatei** stehen.
- Beide Ausgaben folgen genau deiner **Vorlage**.
- SKILL.md ist **nicht länger** als vorher, oder nur um die neuen Schrittzeilen länger.
Ask: Hat nur die richtige Anfrage die Referenzdatei genutzt, und wurde die Vorlage beide Male ausgefüllt? Schreib mir, was du erwartet hast und was herauskam.

## Test [no-skills]
Do: Ergänze die **Anweisungen** um deinen Verweis und deinen Vorlagenschritt und sende dann eine Anfrage, die **die Datei braucht**, und eine, die sie **nicht** braucht, jeweils in einem **neuen Chat** in deinem Projekt oder Gem.
Check:
- Die erste Antwort nutzt Details, die **nur in der Datei** stehen.
- Beide Ausgaben folgen genau deiner **Vorlage**.
- Deine Anweisungen sind **nicht länger** als vorher, oder nur um die neuen Zeilen länger.
Ask: Hat die richtige Anfrage die Datei genutzt, und wurde die Vorlage beide Male ausgefüllt? Schreib mir, was du erwartet hast und was herauskam.

## Other ways
- Cowork: Bitte Cowork, aus deinem Text **references/ und assets/** in deinem Skill-Ordner **anzulegen** und dann die ZIP-Datei für dich zu erstellen.
- skill-creator: Bitte Claude, **den skill-creator zu nutzen**, um deinen Ordner zu prüfen und vorzuschlagen, was aus SKILL.md heraus soll.
- Aktivität: Öffne in einem Chat die **Aktivitätsansicht**, um zu sehen, wann dein Skill eine Datei öffnet.

## Other ways [claude-code]
- Lange Referenzen: Beginne jede Referenzdatei mit mehr als **100 Zeilen** mit einem kurzen Inhaltsverzeichnis, damit die KI den richtigen Teil findet.
- Projekt-Skill: Verschiebe den Ordner nach **.claude/skills/** in einem Repository, damit der Skill und seine Dateien nur in diesem Projekt laden.
- Binäre Assets: Leg Logos oder Beispieltabellen in **assets/** ab und nenne sie in dem Schritt, der sie nutzt.

## Other ways [chatgpt]
- Codex: Behalte denselben Ordner in **~/.agents/skills/**; Codex liest Referenzen und Assets auf dieselbe Weise.
- Editor: Öffne den Skills-Editor, um Dateien **ohne neues Hochladen** hinzuzufügen.
- Claude: Derselbe Ordner funktioniert ohne Änderungen in den Claude-Apps und in Claude Code.

## Other ways [gemini]
- Gemini CLI: Behalte denselben Ordner in **~/.gemini/skills/**; die CLI fragt, bevor sie einen Skill lädt.
- Dateitypen: Die Gemini-App nimmt in einem Skill Text-, Code-, Daten-, PDF- und Bilddateien an, insgesamt bis **100 MB**.
- Claude: Derselbe Ordner funktioniert ohne Änderungen in den Claude-Apps und in Claude Code.

## Other ways [no-skills]
- Wissensdateien: Behalte jede Referenz und jede Vorlage als **eigene Datei** im Projekt oder Gem, so benannt, dass der Verweis sie findet.
- Bereit für Skills: Behalte die Ordnerform (SKILL.md, references/, assets/) auf deinem Computer, damit sie sich als Skill hochladen lässt, sobald dein Werkzeug Skills hat.
- Claude: Derselbe Ordner lässt sich in Claude in jedem Tarif als Skill hochladen, auch im Free-Tarif.

## Done when
- SKILL.md enthält die Schritte, einen Verweis mit Bedingung und einen Vorlagenschritt.
- references/ und assets/ enthalten je eine Datei, ohne echte Kundendaten.
- Claude hat die Referenzdatei nur für die Anfrage gelesen, die sie brauchte, und die Vorlage beide Male ausgefüllt.

## Practice
- Füge am Ende von SKILL.md eine Versionszeile hinzu: „Version 3, [Monat Jahr]“.
- Finde in SKILL.md noch ein Stück Wissen, das nur manche Anfragen brauchen, und verschiebe es nach references/.
- Mach nächste Woche, nach ein paar echten Nutzungen, den Löschtest mit einem weiteren Absatz.

## Reusable template
Name: Skill-Ordner mit Referenzen und Assets
```text
[skill-name]/
  SKILL.md
  references/
    [referenzname].md
  assets/
    [vorlagenname].md

SKILL.md:
---
name: [skill-name]
description: [Tut was, mit deinem Leitbegriff] für [wen]. Verwenden, wenn [Worte, die ein Nutzer sagen würde]. Nicht verwenden für [den Beinahe-Treffer].
---
[Titel des Skills]

Schritte
1. [Handlung, mit deinem Leitbegriff: „[Leitbegriff]“]
2. Wenn [Bedingung], lies references/[referenzname].md, bevor du antwortest.
3. Fülle assets/[vorlagenname].md aus. Behalte die Reihenfolge; ersetze nur die [Platzhalter].

Wenn [Angabe] fehlt, frage danach. Rate nie.
[VERIFY] [was ein Mensch prüfen muss]

Version [n], [Monat Jahr].
```

## Glossary
- Progressive Offenlegung: Ein Skill lädt in Stufen: die Beschreibung immer, die Schritte, wenn er läuft, und die Dateien nur, wenn ein Schritt sie anfordert.
- Referenzdatei: Eine Datei im Ordner references/ eines Skills mit Wissen wie Regeln oder Listen, die nur gelesen wird, wenn ein Schritt sie braucht.
- Asset: Eine Datei im Ordner assets/ eines Skills, die in der Ausgabe genutzt wird, etwa eine Vorlage zum Ausfüllen oder ein Logo, und nicht als Anweisung befolgt wird.
- Verweis: Eine Zeile in den Schritten eines Skills, die eine Datei nennt und sagt, wann sie gelesen oder genutzt wird.
- Leitbegriff: Ein kurzer Begriff für eine Kernidee, überall in einem Skill gleich verwendet, sodass die KI ihn wiederholt und ihm folgt.
- Löschtest: Eine Zeile aus einem Skill entfernen und denselben Test ausführen: Ändert sich nichts, kann die Zeile weg.

## Sources
- [Agent Skills specification](https://agentskills.io/specification): Der Aufbau des Ordners (SKILL.md, references/, scripts/, assets/) und wofür jeder Ordner da ist.
- [Anthropic: Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): Die drei Ladestufen (Beschreibung, Schritte, Dateien) und der Rat, nur Dateien aus vertrauenswürdigen Quellen zu nutzen.
- [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices): Die Grenze von 500 Zeilen, Dateien nur eine Ebene tief und ein Inhaltsverzeichnis für Referenzdateien über 100 Zeilen.
- [Anthropic engineering: Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills): Warum ein Skill weit mehr Material enthalten kann, als ins Kontextfenster passt.
- [Matt Pocock: Building Great Agent Skills (AI Engineer)](https://www.youtube.com/watch?v=UNzCG3lw6O0): Schritte im Vergleich zu Referenzen, Verweise auf Kontext, Leitbegriffe wie „vertical slice“ und der Löschtest.
- [Google: Skills in the Gemini app](https://support.google.com/gemini/answer/17094296): Welche Dateitypen ein Skill-Ordner in der Gemini-App enthalten darf, und die Grenze von 100 MB.

## Coach notes
Arc: fourth of five in this topic (write the skill; install it and add an example; test and fix; reference files and templates; connect and get ready to share). Never name the other missions by number to the learner. Levels covered: structure (folder anatomy, references, templates, pointer, leading word, pruning).
Levels: guided (A, B) works on the working example or moves one list and one template, sees each example first, and hears plain words ("template" rather than "asset" until the learner uses it); standard (C) chooses the material alone; fast-track (D) gets the Go further step (phases, table of contents) and may discuss scripts/.
Guided mode (default for beginners): before a beginner writes each part, point to the step's "See an example" on the page, say in one sentence why it works (for example: "the pointer names a condition"), then ask for their version for their own case. Some familiarity: they try first and you point to the example after the first try. Experienced: only when they ask. The example is from a different case, so they adapt it instead of copying it.
Reference versus asset: a reference is read to decide or check something (rules, categories, definitions); an asset is used in the output (template, logo, sample layout). If the learner is unsure, ask: "Does the AI need to know this, or to fill or attach it?"
Short skill: most tested skills are 20 to 40 lines. The material usually comes from what the learner pastes into the chat or fixes by hand each time, not from SKILL.md. Ask: "What do you paste in or fix every time you use this skill?" Material every request needs and that is short (a rule of three lines) can stay in SKILL.md. Never invent material for them.
Leading word and trigger: keep the words users type as trigger words in the description; the leading word names the output and the core idea.
Likely errors: steps moved into the reference file instead of knowledge; a pointer without a condition ("see references"); a reference file that points to another reference file (keep one level deep); a template without placeholders, so the AI copies it literally; a template step that says "use" instead of "fill and keep the order"; real client data in the template; the ZIP holds a folder inside a folder; v2 and v3 both switched on.
Conflicts: a reference file that renames or adds things can break an existing VERIFY or "never guess" rule. Ask the learner to reread their checks after the Reference step.
Checking the test: in Claude apps the activity view shows which files the skill opened; in Claude Code the tool calls show it. If the learner cannot see it, ask for an output that only the reference file could produce.
Cannot upload today: paste SKILL.md, the reference file and the template into a fresh chat and ask Claude to follow the skill; say plainly that this shows the content works but not that the file loads only when needed.
Time budget for guided learners (30 minutes in total, profile and level question included): about 4 to 5 minutes per build step. They copy the step's fill-in lines and fill the [blanks]; they never write a part from an empty page. If a step runs over 8 minutes, accept a short version and note one improvement for later. The list and the template come from material the learner already has; never ask them to type a new one.
Feedback: name what the move achieved (a clear condition, a filled layout, a line removed), then the gap, then one fix.
Page state: set the full skill v4, the reference file and the template as the part for the last step (Template for guided; Prune for standard; Go further for fast-track). Guided learners skip Prune and the leading word; mention them only if asked.
Other vendors: ChatGPT and Codex read the same folder from .agents/skills; the Gemini app accepts a ZIP with SKILL.md at its root (max 100 MB, no Word or Excel files inside); Gemini CLI uses ~/.gemini/skills/.
