# README

## :page_with_curl: Semesterarbeit 3 - test-push-2


| :ticket: Titel:                   | TrackMyGym: Tracke. Wachse. Gewinne.     |
| ----------------------------------- | ------------------------------------------ |
| :bust_in_silhouette: Studierende: | Lilia Mechani                            |
| :busts_in_silhouette: Dozenten:   | (PRJ) Corrado Parisi (MSVC) Boris Langer |


| :round_pushpin: Topics:             |
| ------------------------------------- |
| :computer: Microservices            |
| :paperclip: PRJ (Projektmanagement) |

# TrackMyGym: Tracke. Wachse. Gewinne.

## Inhaltsverzeichnis

## 📋 Projektübersicht

* [Einführung / README](#einführung--readme)
* [Projektinformationen](#projektinformationen)

### [1. 📊 Projektmanagement](#1--projektmanagement)

* [1.1 Projektbeschreibung](#11-projektbeschreibung)
* [1.2 Zeitplan](#12-zeitplan)
* [1.3 Risiko-Evaluation](#13-risiko-evaluation)
* [1.4 Risiko-Matrix](#14-risiko-matrix)
* [1.5 SWOT-Analyse](#15-swot-analyse)
* [1.6 Sprint-Dokumentation](#16-sprint-dokumentation)
  * [1.6.1 Sprint 1](#161-sprint-1)
  * [1.6.2 Sprint 2](#162-sprint-2)
  * [1.6.3 Sprint 3](#163-sprint-3)
* [1.7 Projekterweiterung](#17-projekterweiterung)
  * [1.7.1 Beschrieb zur Projekterweiterung](#171-beschrieb-zur-projekterweiterung)
  * [1.7.2 SEUSAG-Diagramm - Alte Struktur](#172-seusag-diagramm---alte-struktur)
  * [1.7.3 Neue Struktur](#173-neue-struktur)
* [1.8 Projekt Gantt-Diagramm](#18-projekt-gantt-diagramm)

### [2. 🛠️ Technische Dokumentation](#2-️-technische-dokumentation)

* [2.1 Architektur-Übersicht](#21-architektur-übersicht)
* [2.2 Microservices](#22-microservices)
  * [2.2.1 Frontend Service](#221-frontend-service)
  * [2.2.2 User Service](#222-user-service)
  * [2.2.3 Workout Service](#223-workout-service)
  * [2.2.4 Stats Service](#224-stats-service)

### [3. ☁️ Deployment & DevOps](#3-️-deployment--devops)

* [3.1 AWS EC2 Setup](#31-aws-ec2-setup)
* [3.2 CI/CD Pipeline](#32-cicd-pipeline)
* [3.3 GitHub Actions](#33-github-actions)
* [3.4 Produktionsumgebung](#34-produktionsumgebung)

### [4. 📱 User Interface](#4--user-interface)

* [4.1 Frontend Design](#41-frontend-design)
* [4.2 User Experience](#42-user-experience)
* [4.3 Screenshots](#43-screenshots)

### [5. 🧪 Testing & Qualitätssicherung](#5--testing--qualitätssicherung)

* [5.1 Pipeline-Testing](#51-pipeline-testing)
* [5.2 User-Testing](#52-user-testing)
* [5.3 10 Testfälle](#53-10-testfälle)

### [6. 📈 Ergebnisse & Reflexion](#6--ergebnisse--reflexion)

* [6.1 Erreichte Ziele](#61-erreichte-ziele)
* [6.2 Herausforderungen](#62-herausforderungen)
* [6.3 Lessons Learned](#63-lessons-learned)
* [6.4 Ausblick](#64-ausblick)

### [7. 📚 Anhang](#7--anhang)

* [7.1 Code-Repository](#71-code-repository)
* [7.2 Verwendete Technologien](#72-verwendete-technologien)
* [7.3 Quellen](#73-quellen)
* [7.4 Glossar](#74-glossar)
* [7.5 Kontaktangaben](#75-kontaktangaben)

---

## Quick Navigation

* 🚀[Live Demo](platzhalter)
* 💻[GitHub Repository](platzhalter)
* 📊[KanBan Projekt Board](platzhalter)

---

## Einführung / README

Willkommen zum Sprint Elemente Projekt...

## Projektinformationen

Grundlegende Informationen zum Projekt...

---

# 1. 📊 Projektmanagement

## 1.1 Projektbeschreibung

TrackMyGym: Tracke. Wachse. Gewinne.
Projektplanung
TrackMyGym ist eine Fitness-App, mit der Nutzer ihre Gym-Aktivitäten verfolgen können. Die App soll einfach erfassen, wann jemand im Gym war, welche Übungen gemacht wurden und mit welchen Gewichten trainiert wurde.
Die App TrackMyGym soll Benutzer auf mehreren Ebenen motivieren:
Durch Visualisierung des Fortschritts - indem Benutzer ihre Entwicklung über Zeit sehen können, erkennen sie ihre Verbesserungen konkret, was motivierender ist als subjektive Eindrücke
Durch Gewohnheitsbildung - das tägliche Check-in-System schafft eine Routine und macht regelmässige Gym-Besuche zur Gewohnheit
Durch Erfolgsbestätigung - die Dokumentation von steigenden Gewichten oder verbesserten Leistungen liefert messbare Beweise für den Trainingsfortschritt
Durch soziale Aspekte (in späteren Versionen) - Freunde und Gruppen sorgen für Verantwortungsgefühl und gesunden Wettbewerb
Durch Gamification-Elemente wie Leaderboards (In späteren Versionen) - der Vergleich mit anderen schafft zusätzliche Anreize durch freundschaftlichen Wettbewerb

Die App soll auf folgenden Technologien basieren:

- Backend: Python mit Flask (Microservices)
- Deployment: Docker-Container
- API: REST-Schnittstellen (Für motivierende Push-Notifications)

Persönlicher Bezug

Als regelmässiger Gym-Besucher fehlt mir eine einfache App, die meine Fortschritte trackt und gleichzeitig soziale Elemente bietet. TrackMyGym soll genau diese Lücke füllen und mir sowie anderen Fitness-Fans helfen, motiviert zu bleiben
TrackMyGym – Fortschritt messbar machen!


| :checkered_flag: Angezielte Kernfunktionen der App                                        |
| ------------------------------------------------------------------------------------------- |
| Für die erste Beta-Version von TrackMyGym sollte die App folgende Kernfunktionen bieten: |

- Grundlegendes Tracking von Gym-Besuchen (Check-in-System)
- Einfache Erfassung von Übungen und Gewichten
- Individuelle Fortschrittsanzeige für den Nutzer
- Einfache Benutzeroberfläche für die Eingabe und Anzeige der Daten
- Grundlegende Benutzerprofilverwaltung

Die sozialen Funktionen wie Freunde hinzufügen, Gruppenbildung und Leaderboards könnten für spätere Versionen geplant werden, nachdem die Kernfunktionen stabil laufen. Der technische Aufbau mit Python/Flask und Docker-Deployment sollte bereits in der Beta umgesetzt sein.

Weitere optionale Ziele für die App:

- Freunde hinzufügen: Verbindung mit anderen Nutzern
- Gruppen: Bildung von Trainingsgruppen
- Leaderboards: Freundschaftliche Wettkämpfe zwischen Nutzern/Gruppen          |

## 1.2 Zeitplan

Projektzeitleiste und Meilensteine


| Sprint | Arbeitsschritte                                                                          |
| -------- | ------------------------------------------------------------------------------------------ |
| 1      | GitHub–Obsidian Setup, Architekturplanung                                               |
| 3–4   | Start Entwicklung der Grundarchitektur                                                   |
| 2      | GUI-Planung, Erste Umsetzung der GUI                                                     |
| 2      | Verknüpfung der Elemente, API Push-Notifications, Erste Testphase                       |
| 3      | Verbesserung der App-Visualisierung, Statistiken, Abschluss der Datenbankfunktionalität |
| 3      | Vollendung der Dokumentation                                                             |
| 3      | Vorbereitung der Präsentation, Vollendung des Projekts, Abgabe                          |

## 1.3 Risiko-Evaluation

Identifizierte Projektrisiken und deren Bewertung

Um das Risiko des Projektes richtig einschätzen zu können, habe ich untenstehend eine Risiko-Matrix erstellt mit den allfälligen Projekt-Risiken.

```mermaid
graph TB
    subgraph "Risiko-Matrix: Sprint Elemente"
        subgraph Hoch["🔴 HOHE AUSWIRKUNG"]
            H1["Architekturplanung<br/>Fehlerhafte Basis"]
            H2["Grundarchitektur<br/>Technische Schulden"]
            H3["API Integration<br/>Service Kommunikation"]
        end
        subgraph Mittel["🟡 MITTLERE AUSWIRKUNG"]
            M1["GUI Planung<br/>Design Iterationen"]
            M2["Verknuepfung Elemente<br/>Integration Probleme"]
            M3["App Visualisierung<br/>Performance Issues"]
        end
        subgraph Niedrig["🟢 NIEDRIGE AUSWIRKUNG"]
            N1["GitHub Setup<br/>Tool Probleme"]
            N2["Dokumentation<br/>Unvollständigkeit"]
            N3["Präsentation<br/>Zeitverzug"]
        end
        subgraph Wahrscheinlichkeit["📊 Wahrscheinlichkeit"]
            W1["Hoch: Zeitdruck, Komplexität"]
            W2["Mittel: Design Änderungen"]
            W3["Niedrig: Setup, Dokumentation"]
        end
    end

    classDef hoch fill:#ff4757,stroke:#ff3742,stroke-width:2px,color:#fff
    classDef mittel fill:#ffa502,stroke:#ff9f43,stroke-width:2px,color:#fff
    classDef niedrig fill:#2ed573,stroke:#20bf6b,stroke-width:2px,color:#fff
    classDef info fill:#3742fa,stroke:#2f3542,stroke-width:1px,color:#fff

    class H1,H2,H3 hoch
    class M1,M2,M3 mittel
    class N1,N2,N3 niedrig
    class W1,W2,W3 info
```

Fabrkodierung:
🔴 Hohe Auswirkung (Kritisch)
🟡 Mittlere Auswirkung (Überwachen)
🟢 Niedrige Auswirkung (Akzeptabel)

## 1.4 Risiko-Matrix

Übersicht der Risiken nach Wahrscheinlichkeit und Auswirkung
![](assets/20250629_161158_image.png)

## 1.5 SWOT-Analyse

Stärken, Schwächen, Chancen und Risiken

![](assets/20250706_152917_image.png)

## 1.6 Sprint-Dokumentation

Dokumentation aller Sprint-Aktivitäten inklusive Userstories und Retrospektiven...

### 1.6.1 Sprint 1

# Sprint 1 – Planung & Review

## Zeitraum

5.5. - 9.5.25

## Sprintziel

1. Github – Obsidian setup
2. Architekturplanung
3. Aufbau KanBan Board

## User Stories mit Akzeptanzkriterien

## User Story 1:


| Title:                   | Priority: | Estimate: |
| -------------------------- | ----------- | ----------- |
| Github zu Obsidian Setup | High      | 1h        |

## Beschreibung:

Als Entwickler
Möchte ich **Meinen Text-Editor oder IDE zu meinem Github-Repo verknüpfen**
damit ich **Meine Projektdokumentation festhalten kann**.

## Akzeptanzkriterien:

- Ein verfügbares Repository für die Dokumentation der Semesterarbeit
- Präferierter IDE / Text-Editor welcher aufs Repo zugreifen kann und aktiv änderungen vornimmt

---

## User Story 2:


| Title:             | Priority: | Estimate: |
| -------------------- | ----------- | ----------- |
| Architekturplanung | High      | 2d        |

## Beschreibung:

Als Architekt
Möchte ich **Einen ersten Entwurf meiner Grundarchitektur erstellen**
damit ich **einen ersten Anhaltspunkt zum Architekturdesign habe, an welches sich das Projekt richten kann**.

## Akzeptanzkriterien:

- Ein Mermaid Diagramm mit der groben Vorstellung der Architektur
- Verständliche Beschriftung, Aufbau entsprechend der definierten Sachmittel

---

## User Story 3:


| Title:              | Priority: | Estimate: |
| --------------------- | ----------- | ----------- |
| Aufbau KanBan Board | Medium    | 1d        |

## Beschreibung:

Als Projektleiterin
Möchte ich **Projektvortschritt übersichtlich dokumentieren**
damit ich **meine Stakeholder den Fortschritt mitverfolgen können und ich Übersicht über die Aufgaben behalte**.

## Akzeptanzkriterien:

- Ein verfügbares KanBan Board mit den einzelnen Sprints und deren Ziele
- Die Funktionen Daten zu definieren und Cheklisten in den Zielen aufzubauen

## Aufgabenübersicht Sprint 1


| Aufgabe                  | Status              |
| -------------------------- | --------------------- |
| Github zu Obsidian Setup | Alternativ erledigt |
| Architekturplanung       | erledigt            |
| Aufbau Kan-Ban Board     | erledigt            |

PLANNER FOTO EINFÜGEN

## Sprint Review

### Was wurde erreicht?

- GitHub repo wurde erstellt
- IDE wurde mit GitHub verknüpft - Es wurde auf andere Lösung gewechselt - Da bessere Optionen zur Entwicklung
- Erster Entwurf einer groben Architekturplanung
- KanBan Board wurde erstellt - Microsoft Lists

![alt text](image-2.png)
*_KanBan Angfangs Sprint_

![alt text](image-3.png)
*_KanBan Ende Sprint_

### Herausforderungen

- Microsoft Lists bietet nicht alle benötigten Funktionen an. Es wurde am Anfang des 2. Sprints eine Ausweichmöglichkeit definiert
- Sprint 1 Zeitraum sehr klein

### Lessons Learned

- Mehr Austausch mit den Team-Kollegen und Collaboraters pflegen, um Lösungen zu vergleichen und voneinander zu profitieren. Durch einen Tipp von Teamkollegen, bin ich vollständig auf Visual-Studio gewechselt, da es wesentlich mehr Möglichkeiten anbietet, als Obsidian.

## Ausblick auf Sprint 2

- Wechsel / Migration des KanBan-Board
- Start Entwicklung der Grundarchitektur
- GUI Planung und erste Umsetzun

### 1.6.2 Sprint 2

# Sprint 2 – Planung & Review

## Zeitraum

9.5. - 2.6.25

## Sprintziel

1. Erste Umsetzung und GUI
2. Start Entwicklung der Grundarchitektur
3. Verknüpfung der Elemente, API und Testphase

## User Stories mit Akzeptanzkriterien

## User Story 1:


| Title:                  | Priority: | Estimate: |
| ------------------------- | ----------- | ----------- |
| Erste Umsetzung und GUI | High      | 1h        |

## Beschreibung:

Als Entwickler
Möchte ich **Die Erste Umsetzung der Grundarchitektur Umsetzen**
damit ich **Connectivität zum Fitness-Tracker sicherstellen kann**.

## Akzeptanzkriterien:

- Fehlerfreies herauffahren der Docker-Container
- Ereichbares Frontend mit GUI und dessen Grundfunktionen

---

## User Story 2:


| Title:                                                                           | Priority: | Estimate: |
| ---------------------------------------------------------------------------------- | ----------- | ----------- |
| Verknüpfung der Elemente, Testphase und allenfalls Evaluation von Erweiterungen | High      | 2d        |

## Beschreibung:

Als Architekt
Möchte ich **sicherstellen, das die Container untereinander kommunizieren können und welche Erweiterungen an der Lösung vorgenommen werden können**
damit ich **das Projekt in die Testphase übergeben kann**.

## Akzeptanzkriterien:

- Erreichbarkeit der Container untereinander
- Funktionales Frontend

---

## User Story 3:


| Title:                                                            | Priority: | Estimate: |
| ------------------------------------------------------------------- | ----------- | ----------- |
| Verbesserung der App-Visualisierung und Datenbank-Funktionalität | Medium    | 1d        |

## Beschreibung:

Als Engineer
Möchte ich **Die Visualisierung der App verbessern um eine angenehmeres Benutzererlebnis zu gestalten. **
damit ich **meine User die App nutzen können und persistente Daten auch abrufen können.

## Akzeptanzkriterien:

- Positives Feedback seitens Tester
- Persistenter Datenabruf

## Aufgabenübersicht Sprint 1


| Aufgabe                                                                                           | Status   |
| --------------------------------------------------------------------------------------------------- | ---------- |
| Erste Umsetzung und GUI                                                                           | erledigt |
| Verknüpfung der Elemente, Testphase und allenfalls Evaluation von ErweiterungenArchitekturplanun | erledigt |
| Verbesserung der App-Visualisierung und Datenbank-Funktionalität                                 | erledigt |

PLANNER FOTO EINFÜGEN

## Sprint Review

### Was wurde erreicht?

- Die Tracker-App erreichbarkeit sicherstellen
- Container Verknüpfen und erfolgreich herauffahren
- Erster Entwurf einer groben Architekturplanung
- App GUI attraktiver gestalten mit positivem User-Feedback

![alt text](image-4.png)
*_KanBan Angfangs Sprint_

![alt text](image-5.png)
*_KanBan Ende Sprint_

![alt text](image-1.png)
*_Vorgänger der aktuellen Version_

![alt text](image.png)
*_Verbessertes Design der Benutzeroberfläche_

### Herausforderungen

- Fitness-Begeisterte tester Finden
- API-Funktionalitäten gewährleisten

### Lessons Learned

## Ausblick auf Sprint 3

- Finale Version des GUI, Statistiken
- API Push Messages sicherstellen
- Übertrag auf AW

### 1.6.3 Sprint 3

Dritte Sprint-Iteration...

## 1.7 Projekterweiterung

Erweiterungen und Anpassungen des ursprünglichen Projektumfangs.

### 1.7.1 Beschrieb zur Projekterweiterung

Detaillierte Beschreibung der Erweiterungen

Da die nötigsten Projektziele vorzeitig erreicht wurden; habe ich zusammen mit Corrado Parisi entschieden, das Projekt zu erweitern um meine Microservice-Kompetenzen optimal zu demonstrieren.

Die Projekterweiterung beinhaltete

- Die Push-Benachrichtigungen-Funktionalität zu de-priorisieren und allfällig zu überspringen
- Die Fitness-Tracker Applikation auf einer EC2 Instanz zur Verfügung zu stellen für die Erreichbarkeit via Internet

Hierbei wurde

- Eine EC2 Inszanz erstellt
- Eine GitHub CI/CD Pipeline erstellt
- Die Pipeline auf ihre Funktionalität getestet

### 1.7.2 SEUSAG-Diagramm - Alte Struktur

Ursprüngliche Systemarchitektur

![](assets/20250629_165627_image.png)

***Aussenwelt:*** Der User greift auf die Nginx Instanz, um die Applikation via Localhost IP-Adresse zu erreichen.

Das Docker Compose wird manuell ausgeführt, um die Docker-Container zu initialisieren

***Rote Schicht:*** Auf dieser Schicht verweilt der Localhost (In diesem Szenario, eine Windows-Maschine)

***Grüne Schicht:*** Auf dieser Schicht operiert Docker;

Docker ist hierbei auf der lokalen Maschine aktiv und (noch) nicht auf der Cloud.

***Gelbe Schicht:***

Hier befinden sich die Container der verschiedenen Microservices der Fitness-Tracker Applikation. Die Informationen der Microservices befinden sich in einem JSON Storage-File.

### 1.7.3 Neue Struktur

Überarbeitete Systemarchitektur

![](assets/20250629_170604_image.png)

***Blaue Schicht:*** Auf dieser Schicht befindet sich der Entwicker, der via CI/CD Pipeline den Code auf die Lila Schicht pusht.

Der User greift wie gewohnt via Nginx auf die Applikation zu

***Lila Schicht:*** hier befindet sich die Amazon EC2 Instanz

***Grüne Schicht:*** Unterhalb der EC2 Instanz befindet sich die aktive Docker-Applikation

***Gelbe Schicht:*** Hier befinden sich die Mikroservices.



**Wichtige architektonische Verbesserungen:**

1. **Skalierbarkeit** : Von lokaler Maschine zu Cloud-Infrastruktur
2. **Automatisierung** : CI/CD Pipeline für automatische Deployments
3. **Accessibility** : Von localhost zu öffentlich zugänglicher App
4. **Professional Deployment** : Docker-Compose jetzt innerhalb der AWS-Umgebung

**Das zeigt den Übergang von:**

* 🔧**Development** → 🌐**Production**
* 🏠**Local** → ☁️**Cloud**
* 👨‍💻**Manual** → 🤖**Automated**

## 1.8 Projekt Gantt-Diagramm

Zeitliche Darstellung aller Projektaktivitäten

Dieses Diagramm zeigt die Projekt-Tätigkeiten und dessen Zeitfenster

```mermaid
gantt
dateFormat YYYY-MM-DD
title Fitness Tracker Projekt Zeitplan

section Sprint 1 (5.5-9.5)
Setup Architektur :done, s1, 2025-05-05, 4d

section Sprint 2 (9.5-2.6)
Grundarchitektur :active, s2t1, 2025-05-09, 12d
GUI Planung :s2t2, 2025-05-21, 7d
GUI Start :s2t3, 2025-05-28, 5d

section Sprint 3 (2.6-20.6)
GUI Fertig :s3t1, 2025-06-02, 7d
Verknuepfung :s3t2, 2025-06-09, 4d
API Testing :s3t3, 2025-06-13, 4d
Visualisierung :s3t4, 2025-06-17, 4d

section Meilensteine
Sprint 1 Ende :milestone, m1, 2025-05-09, 0d
Sprint 2 Ende :milestone, m2, 2025-06-02, 0d
Projektende :milestone, m3, 2025-06-20, 0d
```

---

# 2. 🛠️ Technische Dokumentation

## 2.1 Architektur-Übersicht

Gesamtarchitektur des Systems...

## 2.2 Microservices

Beschreibung der einzelnen Services...

### 2.2.1 Frontend Service

Client-seitige Anwendungslogik...

### 2.2.2 User Service

Benutzerverwaltung und Authentifizierung...

### 2.2.3 Workout Service

Workout-Management und -logik...

### 2.2.4 Stats Service

Statistiken und Auswertungen...

---

# 3. ☁️ Deployment & DevOps

## 3.1 AWS EC2 Setup

Konfiguration der AWS-Infrastruktur...

## 3.2 CI/CD Pipeline

Continuous Integration und Deployment-Prozesse...

## 3.3 GitHub Actions

Automatisierte Workflows und Tests...

## 3.4 Produktionsumgebung

Live-System und Monitoring...

---

# 4. 📱 User Interface

## 4.1 Frontend Design

Designkonzept und visuelle Gestaltung

## 4.2 User Experience

Benutzerfreundlichkeit und Usability...

## 4.3 Screenshots

Visuelle Darstellung der Anwendung...

---

# 5. 🧪 Testing & Qualitätssicherung

## 5.1 Pipeline-Testing

Automatisierte Tests in der CI/CD-Pipeline...

## 5.2 User-Testing

Benutzertests und Feedback...

## 5.3 10 Testfälle

Detaillierte Testszenarien und -ergebnisse...

---

# 6. 📈 Ergebnisse & Reflexion

## 6.1 Erreichte Ziele

Zusammenfassung der erfolgreich umgesetzten Projektziele...

## 6.2 Herausforderungen

Schwierigkeiten und Hindernisse während der Entwicklung...

## 6.3 Lessons Learned

Erkenntnisse und Lerneffekte aus dem Projekt...

## 6.4 Ausblick

Zukünftige Entwicklungen und Verbesserungsmöglichkeiten...

---

# 7. 📚 Anhang

## 7.1 Code-Repository

Links zum Quellcode und Repository...

## 7.2 Verwendete Technologien

Übersicht aller eingesetzten Tools und Frameworks...

## 7.3 Quellen

Referenzen und verwendete Literatur...

## 7.4 Glossar

Definitionen wichtiger Begriffe...

## 7.5 Kontaktangaben

Projektteam und Ansprechpartner...
