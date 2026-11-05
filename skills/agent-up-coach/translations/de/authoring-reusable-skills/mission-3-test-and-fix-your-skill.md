---
id: mission-3-test-and-fix-your-skill
number: 3
title: Teste deinen Skill und behebe, was nicht klappt
summary: Probier deinen Skill mit drei kurzen Testanfragen aus, eine davon muss er ignorieren, und korrigiere den Teil hinter jedem Fehler. Am Ende hast du einen getesteten Skill v3, auf den du dich verlässt.
artefact: "Skill v3: getestete und korrigierte SKILL.md"
---

Track: Baseline
Level: foundation
Time: 30 Minuten
Tools: Claude-Chat, Cowork oder Claude Code
Artefact kind: text
Artefact file: my-skill-v3.md

## Context
Ein Skill, der einmal funktioniert hat, kann bei der nächsten **ungewöhnlichen Anfrage** trotzdem scheitern, und oft merkst du es erst, wenn es ein Kollege oder Kunde merkt. **Drei kurze Tests** und eine Korrektur pro Fehler zeigen dir, wo er zuerst bricht.

## Your task
Schreib **3 Testanfragen** mit dem Ergebnis, das du erwartest, führe jede in einem neuen Chat aus und **korrigiere** den einen Teil hinter jedem Fehler.

## After this, you can
Du kannst an einem fehlgeschlagenen Test erkennen, welcher Teil eines Skills ihn verursacht hat, und genau diesen Teil korrigieren.

## You need
- Deinen **installierten Skill** mit einem Beispiel, oder das **Arbeitsbeispiel** in dieser Mission
- **2 oder 3 kurze Beispieleingaben** (je 5 bis 10 Zeilen), mit erfundenen Namen

## You need [no-skills]
- Deinen **Skill** in einem Projekt oder Gem, oder das **Arbeitsbeispiel** in dieser Mission
- **2 oder 3 kurze Beispieleingaben** (je 5 bis 10 Zeilen), mit erfundenen Namen

## You should already
- Einen **Skill installieren** und in einem **neuen Chat** ausführen können

## Concept
Heading: Die 3 Tests, die jeder Skill braucht
Lead: Jeder Test ist **eine Anfrage** mit dem Ergebnis, das du **erwartest**, aufgeschrieben, **bevor** du ihn ausführst.
- Normal: Soll den Skill **starten**, mit typischer Eingabe. Zeigt, dass der Skill seine Aufgabe erfüllt.
- Knifflig: Soll ihn starten, mit **fehlender oder ungewöhnlicher** Eingabe. Zeigt, ob er nachfragt oder rät.
- Beinahe-Treffer: Soll ihn **nicht starten**. Zeigt, ob die Beschreibung zu weit gefasst ist.
Close: Das ist der **volle Test** deines Skills. Anthropic empfiehlt **mindestens 3 Tests**; halte Beispiele bei **5 bis 10 Zeilen**, damit das Testen schnell bleibt.
Toggle: Woher kann ein Fehler kommen? | Aus **einem Teil**: der Beschreibung (der Skill startet für die falsche Anfrage), den Schritten (falsche Handlungen), dem Format (falsche Form) oder einer **[[fehlenden Regel|Fehlende Regel]]** (erfundene Details).
Toggle: Muss ich nach jeder Änderung alle drei Tests wiederholen? | Nein. Prüfe nach einer kleinen Änderung **nur, was du geändert hast**. Wiederhole alle drei, wenn du dich bei echter Arbeit auf den Skill **verlassen** willst.

## Check your understanding
Question: Deine Testanfrage lautet „Entwirf eine Vertriebs-E-Mail zu unserem neuen Angebot“, und dein Skill schreibt Antworten auf Beschwerden. Welches Ergebnis zählt als bestanden?
- A: Der Skill startet und schreibt eine höfliche Vertriebs-E-Mail
- B: Der Skill startet nicht
- C: Der Skill startet und fragt nach einer Bestellnummer
Answer: B
Why: Das ist ein Beinahe-Treffer: Die Anfrage sieht ähnlich aus, ist aber eine andere Aufgabe, deshalb ist das richtige Ergebnis, dass der Skill still bleibt. A und C bedeuten beide, dass die Beschreibung zu weit gefasst ist.

## Working example
Situation: Dein **Skill für das Status-Update** ist installiert. Du willst wissen, wie er mit einem **fehlenden Fälligkeitsdatum** und einer Anfrage nach einem **Besprechungsprotokoll** umgeht.
Input: Dein **installierter Skill** und drei kurze Beispielnotizen, mit erfundenen Namen.
- Den **normalen** Test mit vollständigen Notizen schreiben.
- Den **kniffligen** Test mit einer Aufgabe ohne Fälligkeitsdatum schreiben.
- Den **[[Beinahe-Treffer]]** schreiben: eine Anfrage nach einem Besprechungsprotokoll.
- Jeden Test in einem **neuen Chat** ausführen und den **einen Teil** hinter jedem Fehler korrigieren.
Result: Ein **Skill v3**, der alle drei Tests besteht.
Ask: Willst du einen Skill testen, den du geschrieben hast, oder das Arbeitsbeispiel? Wenn du noch keinen Skill hast, sag es, dann gebe ich dir einen kurzen Skill zum Testen.

## Steps
### Testset
Use: Arbeite an einem Skill, den du geschrieben hast, oder am Arbeitsbeispiel unten.
Why: Ein Test zählt nur, wenn du das **erwartete Ergebnis vor** dem Lauf aufgeschrieben hast; danach kann jede Ausgabe richtig aussehen.
Do: Schreib **3 Testanfragen**: normal, knifflig und Beinahe-Treffer, jede mit dem **erwarteten Ergebnis**. Bitte im Chat um **erfundene Beispiele** für deine Aufgabe, damit du sie nicht abtippen musst.
Ask: Sende dein **[[Testset]]** im Chat.
Code:
```text
1. Normal: „[Anfrage]“ + [Beispiel]  Erwartet: [was ein gutes Ergebnis enthält]
2. Knifflig: „[Anfrage]“ + [Beispiel, in dem etwas fehlt]  Erwartet: fragt nach [...]
3. Beinahe-Treffer: „[ähnliche Anfrage, andere Aufgabe]“  Erwartet: Skill startet nicht
```
Example:
```text
1. Normal: „Entwirf eine Antwort auf diese Beschwerde über eine verspätete Lieferung.“ (mit Bestellnummer)
   Erwartet: Skill lädt, unter 120 Wörtern, Entschuldigung, Lieferdatum.
2. Knifflig: eine Beschwerde ohne Bestellnummer.
   Erwartet: Skill lädt, fragt nach der Bestellnummer, erfindet nichts.
3. Beinahe-Treffer: „Entwirf eine Vertriebs-E-Mail zu unserem neuen Lieferplan.“
   Erwartet: Skill lädt nicht.
```
Weak:
```text
Probier es mit ein paar E-Mails aus und schau, ob es funktioniert.
```

### Ausführen
Why: Ein **neuer Chat** für jeden Test stellt sicher, dass nur dein Skill und die Anfrage die Antwort bestimmen, nicht das, was du vorher geschrieben hast.
Do:
1. Öffne einen **neuen Chat** mit ausgeschaltetem Gedächtnis (Memory).
2. Sende **Test 1** mit seinem Beispiel und notiere, ob Claude sagt, dass es **deinen Skill nutzt**.
3. Vergleiche die Ausgabe mit dem, was du **erwartet** hast, und notiere bestanden oder nicht bestanden.
4. Wiederhole das für **Test 2** und **Test 3**, jeweils in einem weiteren neuen Chat.
Ask: Sende deine Ergebnisse: jeden Test, bestanden oder nicht bestanden, und was bei einem Fehler herauskam.

### Ausführen [claude-code]
Why: Eine **neue Sitzung** für jeden Test stellt sicher, dass nur dein Skill und die Anfrage die Antwort bestimmen, nicht das, was du vorher geschrieben hast.
Do:
1. Starte eine **neue Sitzung** (**claude**) in einem Ordner ohne CLAUDE.md, damit keine Projektregeln den Test beeinflussen.
2. Sende **Test 1** mit seinem Beispiel und notiere, ob Claude Code sagt, dass es **deinen Skill nutzt**.
3. Vergleiche die Ausgabe mit dem, was du **erwartet** hast, und notiere bestanden oder nicht bestanden.
4. Wiederhole das für **Test 2** und **Test 3**, jeweils in einer neuen Sitzung. Führe den Beinahe-Treffer **3 Mal** aus: Das Auslösen kann schwanken.
Ask: Sende deine Ergebnisse: jeden Test, bestanden oder nicht bestanden, und was bei einem Fehler herauskam.

### Ausführen [chatgpt, gemini]
Why: Ein **neuer Chat** für jeden Test stellt sicher, dass nur dein Skill und die Anfrage die Antwort bestimmen, nicht das, was du vorher geschrieben hast.
Do:
1. Öffne einen **neuen Chat**, wenn möglich mit ausgeschaltetem Gedächtnis (Memory) oder persönlichem Kontext.
2. Sende **Test 1** mit seinem Beispiel und notiere, ob die Antwort **deinem Skill folgt**.
3. Vergleiche die Ausgabe mit dem, was du **erwartet** hast, und notiere bestanden oder nicht bestanden.
4. Wiederhole das für **Test 2** und **Test 3**, jeweils in einem neuen Chat.
Ask: Sende deine Ergebnisse: jeden Test, bestanden oder nicht bestanden, und was bei einem Fehler herauskam.

### Ausführen [no-skills]
Why: Ein **neuer Chat** für jeden Test stellt sicher, dass nur dein Skill und die Anfrage die Antwort bestimmen, nicht das, was du vorher geschrieben hast.
Do:
1. Öffne einen **neuen Chat in deinem Projekt** oder Gem und sende **Test 1** mit seinem Beispiel.
2. Mach dasselbe für **Test 2** und notiere dann bestanden oder nicht bestanden, gemessen an dem, was du **erwartet** hast.
3. Öffne für **Test 3** einen einfachen neuen Chat, füge nur **Name und Beschreibung** und die Anfrage ein und frag: „Würde dieser Skill hier greifen? Ja oder nein.“
Ask: Sende deine Ergebnisse: jeden Test, bestanden oder nicht bestanden, und was bei einem Fehler herauskam.

### Korrigieren
Why: Mach **eine Änderung pro Fehler**, damit du siehst, welche Änderung gewirkt hat. Wenn du alles neu schreibst oder für jedes Problem eine neue Regel ergänzt, wird der Skill länger, und alte Regeln widersprechen sich (dieses Anhäufen heißt **[[Sediment]]**).
Do: Nenne für jeden fehlgeschlagenen Test den **Teil**, der ihn verursacht hat (Beschreibung, Anweisungen, Format oder fehlende Regel), und schreib die **neue Zeile**, die die alte ersetzt.
Ask: Sende jeden Fehler, den Teil, die alte und die neue Zeile; dein vollständiger **Skill v3** erscheint auf der Seite.
Code:
```text
Test [n] nicht bestanden: [was herauskam]. Teil: [Beschreibung / Schritte / Format / fehlende Regel]
Alt: [alte Zeile]
Neu: [neue Zeile]
```
Example:
```text
Test 3 nicht bestanden: Die Vertriebs-E-Mail hat den Skill geladen. Teil: Beschreibung, „E-Mails“ ist zu weit gefasst.
Alt: Verwenden, wenn der Nutzer um eine Antwort auf eine E-Mail bittet.
Neu: Verwenden, wenn der Nutzer eine Kundenbeschwerde einfügt. Nicht verwenden für Vertriebs- oder Marketing-E-Mails.
```
Weak:
```text
Der Skill ist noch nicht gut genug, deshalb habe ich alles neu geschrieben.
```

### Weiter vertiefen [fast-track]
Why: Die KI wählt nicht jedes Mal gleich, deshalb beweist **ein** bestandener Lauf wenig, und ein Lauf **ohne** den Skill zeigt, was der Skill beiträgt.
Do: Führe deinen **Beinahe-Treffer dreimal** aus und **Test 1 einmal mit ausgeschaltetem Skill**; notiere jeden Lauf, der abweicht.
Ask: Sende, wie viele der drei Läufe mit dem Beinahe-Treffer bestanden haben und was dem Lauf ohne den Skill gefehlt hat.

## Trust check
Watch for:
- Teste mit **erfundenem oder anonymisiertem** Material, nie mit der Nachricht eines echten Kunden. (DSGVO, Artikel 5)
- Werte einen Test nur als bestanden, wenn die Ausgabe dem entspricht, was du **vor dem Lauf aufgeschrieben** hast. (EU AI Act, Artikel 4)
- Installiere nur Skills, die du **selbst geschrieben** oder aus einer vertrauenswürdigen Quelle hast, und lies vorher jede Datei. (Anthropic Skill-Sicherheit)
Rules:
- DSGVO, Artikel 5: Personenbezogene Daten müssen dem Zweck angemessen und erheblich sowie auf das für den Zweck notwendige Maß beschränkt sein. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de)
- EU AI Act, Artikel 4: Organisationen, die KI-Systeme anbieten oder nutzen, müssen dafür sorgen, dass ihr Personal für seine Rolle genug KI-Kompetenz hat: Es versteht die Werkzeuge und weiß, was die Ergebnisse bedeuten. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=de)
- Anthropic Skill-Sicherheit: Nutze nur Skills, die du selbst erstellt oder aus einer vertrauenswürdigen Quelle hast, und prüfe vorher jede Datei, denn ein Skill kann Code ausführen. [Anthropic-Dokumentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
Ask: Wie genau wirst du die Ausgabe dieses Skills nach diesen Tests nächste Woche **prüfen**?

## Test
Do: Füge deinen **korrigierten Skill** mit „Befolge diesen Skill bei meiner nächsten Nachricht“ in einen **neuen Chat** ein und führe jeden **fehlgeschlagenen Test** erneut aus. Nur wenn du die **Beschreibung** geändert hast, aktualisiere den installierten Skill (bitte Claude um die neue ZIP) und sende den Beinahe-Treffer erneut.
Check:
- Jeder Test, der vorher **nicht bestanden** war, ist jetzt bestanden.
- Der **Beinahe-Treffer** bleibt still, auch wenn du ihn **mit anderen Worten** schreibst.
- Jede Änderung hat **einen Fehler** behoben, den du benennen kannst.
Ask: Haben die fehlgeschlagenen Tests mit der korrigierten Version bestanden? Schreib mir, welcher noch nicht bestanden ist, falls einer, und was herauskam.

## Test [claude-code]
Do: Bearbeite die **SKILL.md** direkt, starte eine **neue Sitzung** in einem Ordner ohne CLAUDE.md und führe dann jeden **fehlgeschlagenen Test** und den **Beinahe-Treffer** erneut aus, jeweils in einer neuen Sitzung.
Check:
- Jeder Test, der vorher **nicht bestanden** war, ist jetzt bestanden.
- Der **Beinahe-Treffer** bleibt still, auch wenn du ihn **mit anderen Worten** schreibst.
- Jede Änderung hat **einen Fehler** behoben, den du benennen kannst.
Ask: Haben die fehlgeschlagenen Tests mit der korrigierten Version bestanden? Schreib mir, welcher noch nicht bestanden ist, falls einer, und was herauskam.

## Test [gemini]
Do: Ändere unter **Einstellungen > Skills** (Settings > Skills) die Beschreibung oder die Anweisungen und klicke auf **Speichern** (Save). Führe dann jeden **fehlgeschlagenen Test** und den **Beinahe-Treffer** erneut aus, jeweils in einem **neuen Chat**.
Check:
- Jeder Test, der vorher **nicht bestanden** war, ist jetzt bestanden.
- Der **Beinahe-Treffer** bleibt still, auch wenn du ihn **mit anderen Worten** schreibst.
- Jede Änderung hat **einen Fehler** behoben, den du benennen kannst.
Ask: Haben die fehlgeschlagenen Tests mit der korrigierten Version bestanden? Schreib mir, welcher noch nicht bestanden ist, falls einer, und was herauskam.

## Test [no-skills]
Do: Aktualisiere die **Projekt- oder Gem-Anweisungen** mit der korrigierten Version, führe dort jeden **fehlgeschlagenen Test** in einem neuen Chat aus und wiederhole die **Beschreibungsprüfung** für den Beinahe-Treffer.
Check:
- Jeder Test, der vorher **nicht bestanden** war, ist jetzt bestanden.
- Die Beschreibungsprüfung sagt **nein** für den Beinahe-Treffer, auch **mit anderen Worten**.
- Jede Änderung hat **einen Fehler** behoben, den du benennen kannst.
Ask: Haben die fehlgeschlagenen Tests mit der korrigierten Version bestanden? Schreib mir, welcher noch nicht bestanden ist, falls einer, und was herauskam.

## Other ways
- Beim Namen aufrufen: Bitte in einem Chat um deinen Skill mit seinem **Namen**, um die Schritte **getrennt vom automatischen Start** zu testen.
- skill-creator: Bitte Claude, **den skill-creator zu nutzen**, um deine Tests mit und ohne Skill auszuführen und die Ergebnisse nebeneinander zu zeigen.
- Zwei Chats: Nutze **einen Chat**, um den Skill zu verbessern, und einen **neuen Chat**, um ihn zu testen, damit der Test deine Erklärungen nie sieht.

## Other ways [claude-code]
- Beim Namen aufrufen: Führe **/[name]** mit jedem Beispiel aus, um die Anweisungen **getrennt vom Auslöser** zu testen.
- skill-creator: Bitte Claude Code, **den skill-creator zu nutzen**, um deine Tests mit und ohne Skill auszuführen und zu vergleichen.
- Projekt-Skill: Speichere den Ordner in **.claude/skills/** eines Projekts, damit der Skill nur dort lädt.

## Other ways [chatgpt]
- Beim Namen aufrufen: Tippe **@[name]** in die Nachricht, um deinen Skill gezielt auszuführen und die Anweisungen **getrennt vom Auslöser** zu testen.
- Codex: Speichere den Ordner in **~/.agents/skills/**, ruf ihn mit **$[name]** auf und nutze **$skill-creator**, um weitere Tests zu entwerfen.
- Editor: Öffne den Skills-Editor, um den Skill **ohne neues Hochladen** zu ändern.

## Other ways [gemini]
- Beim Namen aufrufen: Tippe **/** und wähle deinen Skill, um die Anweisungen **getrennt von der automatischen Auswahl** zu testen.
- Gemini CLI: Speichere den Ordner in **~/.gemini/skills/**. Die CLI fragt, bevor sie **einen Skill lädt**, so siehst du jedes Mal, wann er genutzt wird.
- Direkt bearbeiten: Ändere unter **Einstellungen > Skills** (Settings > Skills) die Beschreibung oder die Anweisungen und klicke auf **Speichern** (Save).

## Other ways [no-skills]
- Prompt-Bibliothek: Behalte die SKILL.md als Datei und füge sie für jeden Test in einen **neuen Chat** ein.
- Claude: Dieselbe SKILL.md lässt sich in Claude in jedem Tarif hochladen, auch im Free-Tarif, wenn du den **Auslöser** wirklich testen willst.
- Später: Wenn dein Werkzeug oder Tarif Skills bekommt, wiederhole den Test mit dem **Beinahe-Treffer** unter echten Bedingungen.

## Done when
- Dein Testblatt hat 3 Anfragen, jede mit einem erwarteten Ergebnis, das vor dem Lauf aufgeschrieben wurde.
- Jeder Fehler hat einen benannten Teil und eine geänderte Zeile.
- Der korrigierte Skill ist installiert und besteht die Tests, die vorher nicht bestanden waren.

## Practice
- Schalte den Skill **aus**, führe Test 1 erneut aus und notiere, was der Skill beiträgt: Das ist deine **[[Baseline]]**.
- Nimm eine echte Anfrage aus dieser Woche, die dich überrascht hat, als vierten Test auf.
- Formuliere einen zweiten Beinahe-Treffer mit anderen Worten und prüfe, ob der Skill still bleibt.

## Reusable template
Name: Skill-Test- und Korrekturblatt
```text
Skill: [name], v2 > v3

1. Normal: „[Anfrage]“ + [kurzes Beispiel]
   Erwartet: [Skill lädt] + [was eine gute Ausgabe enthält]
   Ergebnis: [bestanden / nicht bestanden: was herauskam]
2. Knifflig: „[Anfrage]“ + [unvollständiges oder ungewöhnliches Beispiel]
   Erwartet: [Skill lädt] + [fragt nach ... / geht mit ... um]
   Ergebnis: [bestanden / nicht bestanden: was herauskam]
3. Beinahe-Treffer: „[ähnliche Anfrage, die nicht diese Aufgabe ist]“
   Erwartet: Skill lädt nicht
   Ergebnis: [bestanden / nicht bestanden]

Fehler > Teil > Änderung: [Test] > [Beschreibung / Anweisungen / Format / fehlende Regel] > [neue Zeile]
Neuer Test mit v3: [bestanden / nicht bestanden]
```

## Glossary
- Testset: Eine kurze Liste von Anfragen mit dem erwarteten Ergebnis, die du bei jeder Änderung an einem Skill wieder verwendest.
- Beinahe-Treffer: Eine Anfrage, die deiner Aufgabe ähnlich sieht, aber ein anderes Ergebnis braucht, sodass der Skill nicht laden darf.
- Baseline (Vergleichslauf): Dieselbe Anfrage ohne den Skill ausgeführt, um zu sehen, was der Skill beiträgt.
- Fehlende Regel: Eine Anweisung, die ein Skill braucht, aber nicht hat, oft dazu, was bei fehlenden Informationen zu tun ist.
- Sediment: Alte Regeln, die sich mit der Zeit als Altlasten in einem Skill anhäufen und nichts mehr an seinem Verhalten ändern.

## Sources
- [Claude Help Centre: Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude): Die Tarife mit Skills (Free bis Enterprise) und der genaue Menüpfad zum Hochladen einer ZIP-Datei.
- [Claude Help Centre: How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills): Der Aufbau der ZIP-Datei: Der Skill-Ordner muss auf der obersten Ebene der ZIP-Datei liegen.
- [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices): Mindestens 3 Auswertungen erstellen und mit einem Lauf ohne den Skill vergleichen.
- [Anthropic: skill-creator skill](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md): Wie Anthropic selbst einen Skill testet, mit und ohne den Skill.
- [Anthropic: The complete guide to building skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf): Tests für den Auslöser und ein konkretes Ziel: Der Skill lädt bei mindestens 90 % der Anfragen, bei denen er laden soll.
- [Anthropic: Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): Warum du nur Skills aus vertrauenswürdigen Quellen installieren solltest.
- [Matt Pocock: Building Great Agent Skills (AI Engineer)](https://www.youtube.com/watch?v=UNzCG3lw6O0): Warum sich Regeln als Sediment anhäufen, und der Löschtest für Zeilen, die nichts ändern.

## Coach notes
Arc: third of five in this topic (write the skill; install it and add an example; test and fix; reference files and templates; connect and get ready to share). Never name the other missions by number to the learner. Levels covered: test and fix.
No failures: if every test passed, the learner writes one harder awkward test (two missing details, or input in another language) and runs it first. If that passes too, the Fix step becomes a near-miss rephrasing test; say so plainly.
Diagnosis: wrong skill or no skill loaded means the description; right skill but wrong steps means the instructions; right steps but wrong shape means the format; invented details mean a missing "ask, never guess" rule. A rule that exists but does not reach this case counts as a missing rule: widen it, do not add a second one. Several failures: fix the one that changes the most first.
Levels: guided (A, B) shapes three tests with your questions and sees the step's example before writing; standard (C) writes the tests alone; fast-track (D) may test out with an existing test sheet and a fixed version, and gets the Go further step (repeated runs, run without the skill).
Guided mode (default for beginners): before a beginner writes each part, point to the step's "See an example" on the page, say in one sentence why it works (for example: "it names a near miss"), then ask for their version for their own case. Some familiarity: they try first and you point to the example after the first try. Experienced: only when they ask. The example is from a different case, so they adapt it instead of copying it; if they copy it word for word, ask what changes for their task. Beginners can also take the working example instead of their own task, so the page example and their task differ only in the details.
Starter skill: if the learner has no skill yet and chose the working example, draft a short skill for the working example adapted to their role. Say you drafted it for them and that it has at least one weak spot their tests should find (for example a description without a near miss). This is a test object, not their artefact.
Likely errors: the expected result is written after the run, so every output passes; the awkward test is complete and clean; the near miss is too different to test anything ("write a poem"); tests run in the chat where the skill was written, so context leaks in; the learner pastes the SKILL.md into the chat instead of uploading it, which tests the instructions but not the trigger.
Upload problems: see the install mission's notes; the most common are a ZIP with a folder inside a folder and a file saved as SKILL.md.txt.
Cannot upload today (no permission, admin block): do the closest honest substitute and say so. For the trigger, open a fresh chat, paste only the name and description plus the request, and ask "Would this skill apply to this request? Yes or no." Label it a proxy on the test sheet. For tests 1 and 2, paste the whole skill into a fresh chat.
Skills that use a connector or MCP tool: test them in the tool where that connector works (often Claude Code or Cowork), not in plain chat.
Time budget for guided learners (30 minutes in total, profile and level question included): about 4 to 5 minutes per build step. They copy the step's fill-in lines and fill the [blanks]; they never write a part from an empty page. If a step runs over 8 minutes, accept a short version and note one improvement for later. The coach may give made-up test samples (5 lines each) for the learner's task: they are test material, not the learner's artefact.
Time: allow at most two feedback rounds per step. Expected results stay short (one line each).
Feedback: name the test that is well written, then the one that tests nothing, then one fix.
Trust question: push for a concrete answer tied to their work ("I check every figure for the next four weeks"), not "I will be careful".
Page state: set the full skill v3 as the part for the last step (Fix; Go further for fast-track).
Other vendors: in ChatGPT (eligible Business, Enterprise and Edu workspaces) and the Gemini app the same three tests work; the near-miss test applies only where the skill loads automatically from its description.
