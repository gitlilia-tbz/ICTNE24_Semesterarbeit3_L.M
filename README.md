# README

# 🏋️‍♀️ FitTracker Pro: Tracke. Wachse. Gewinne.
![alt text](top_bar.gif)

### Fitness Tracking Platform mit Microservices Architektur

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)![Version](https://img.shields.io/badge/Version-v1.0-blue)
![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white)![Top Language](https://img.shields.io/github/languages/top/gitlilia-tbz/ICTNE24_Semesterarbeit3_L.M)
![Flask](https://img.shields.io/badge/Flask-2.3.3-black?logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker&logoColor=white)
![AWS EC2](https://img.shields.io/badge/Deployed%20on-AWS%20EC2-orange?logo=amazon-aws&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-green?logo=github&logoColor=white)
![Weather API](https://img.shields.io/badge/Weather-OpenWeatherMap-blue?logo=openweathermap&logoColor=white)

---

**Studierende:** Lilia Mechani | **Semester:** 3 | **Dozenten:** (PRJ) Corrado Parisi (MSVC) Boris Langer.

[🚀 Live Demo](http://52.202.224.208/) • [📖 Repo](https://github.com/gitlilia-tbz/ICTNE24_Semesterarbeit3_L.M) • [🏗️ KanBan](https://semesterarbeit3liliam.atlassian.net/jira/software/projects/KAN/boards/1)

## Inhaltsverzeichnis

## 📋 Projektübersicht

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
  * [1.7.4 Neue Struktur (Persistent + Weather API)](#174-neue-struktur-persistent--weather-api)
* [1.8 Projekt Gantt-Diagramm](#18-projekt-gantt-diagramm)

### [2. 🛠️ Technische Dokumentation](#2-️-technische-dokumentation)

* [2.1 Architektur-Übersicht](#21-architektur-übersicht)
* [2.2 Microservices](#22-microservices)
  * [2.2.1 Frontend Service](#221-frontend-service)
  * [2.2.2 User Service](#222-user-service)
  * [2.2.3 Workout Service](#223-workout-service)
  * [2.2.4 Stats Service](#224-stats-service)
  * [2.2.5 Weather Service](#225-weather-service)

### [3. ☁️ Deployment & DevOps](#3-️-deployment--devops)

* [3.1 AWS EC2 Setup](#31-aws-ec2-setup)
* [3.2 CI/CD Pipeline](#32-cicd-pipeline)
* [3.3 GitHub Actions](#33-github-actions)
* [3.4 Produktionsumgebung](#34-produktionsumgebung)

### [4. 📱 User Interface](#4--user-interface)

* [4.1 Frontend Design](#41-frontend-design)
* [4.2 User Experience](#42-user-experience)

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
- Leaderboards: Freundschaftliche Wettkämpfe zwischen Nutzern/Gruppen

## 1.2 Zeitplan

Projektzeitleiste und Meilensteine


| Sprint | Zeitpunkt     | Arbeitsschritte                                                                          |
| -------- | --------------- | ------------------------------------------------------------------------------------------ |
| 1      | 5.5. - 9.5.25 | GitHub–Obsidian Setup, Architekturplanung                                               |
| 2      | 9.5. - 2.6.25 | Start Entwicklung der Grundarchitektur                                                   |
| 2      | 9.5. - 2.6.25 | GUI-Planung, Erste Umsetzung der GUI                                                     |
| 2      | 9.5. - 2.6.25 | Verknüpfung der Elemente, API Push-Notifications, Erste Testphase                       |
| 3      | 2.6. - 9.7.25 | Verbesserung der App-Visualisierung, Statistiken, Abschluss der Datenbankfunktionalität |
| 3      | 2.6. - 9.7.25 | Vollendung der Dokumentation                                                             |
| 3      | 2.6. - 9.7.25 | Vorbereitung der Präsentation, Vollendung des Projekts, Abgabe                          |

![](assets/20250708_175314_image.png)

***✨ Alle ✨ markierten Erweiterungen:***

1. **🐘 PostgreSQL Database Migration** ✨ NEU
2. **🔄 SQLAlchemy ORM Integration** ✨ NEU
3. **🌤️ Weather API Service Development** ✨ NEU
4. **☁️ AWS EC2 Deployment & CI/CD** ✨ NEU
5. **🏗️ Microservices Architektur Erweiterung** ✨ NEU

Bei diesen Erweiterungen handelt es sich um erreichte Ziele ausserhalb des Ursprünglichen Projektscopes. Diese Erweiterungen wurden nach Absprache mit dem Projektmanagement-Dozenten im Sprint 3 implementiert, um das Projekt in Sachen Cloud-Native zu festigen.

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

Stärken, Schwächen, Chancen und Risiken des Projektes innerhalb der SWOT Analyse:

![](assets/20250706_152917_image.png)

Ziel ist es, bewusst mich primär an den Stärken zu orientieren um den positiven Fokus zu behalten und die schädlichen Aspekte der SWOT-Analyse präventiv anzugehen.

## 1.6 Sprint-Dokumentation

Dokumentation aller Sprint-Aktivitäten inklusive Userstories und Retrospektiven.

### 1.6.1 Sprint 1



#### **Zeitraum**

5.5. - 9.5.25

---

#### **Sprintziel**

1. Github – Obsidian setup
2. Architekturplanung
3. Aufbau KanBan Board

---


#### **User Stories mit Akzeptanzkriterien**
---

📍​**User Story 1:**


| Title:                   | Priority: | Estimate: |
| -------------------------- | ----------- | ----------- |
| Github zu Obsidian Setup | High      | 1h        |



Als Entwickler
Möchte ich **Meinen Text-Editor oder IDE zu meinem Github-Repo verknüpfen**
damit ich **Meine Projektdokumentation festhalten kann**.

**Akzeptanzkriterien:**

- Ein verfügbares Repository für die Dokumentation der Semesterarbeit
- Präferierter IDE / Text-Editor welcher aufs Repo zugreifen kann und aktiv änderungen vornimmt

---

📍​**User Story 2:**


| Title:             | Priority: | Estimate: |
| -------------------- | ----------- | ----------- |
| Architekturplanung | High      | 2d        |



Als Architekt
Möchte ich **Einen ersten Entwurf meiner Grundarchitektur erstellen**
damit ich **einen ersten Anhaltspunkt zum Architekturdesign habe, an welches sich das Projekt richten kann**.

**Akzeptanzkriterien:**

- Ein Mermaid Diagramm mit der groben Vorstellung der Architektur
- Verständliche Beschriftung, Aufbau entsprechend der definierten Sachmittel

---

📍​**User Story 3:**


| Title:              | Priority: | Estimate: |
| --------------------- | ----------- | ----------- |
| Aufbau KanBan Board | Medium    | 1d        |

Als Projektleiterin
Möchte ich **Projektvortschritt übersichtlich dokumentieren**
damit ich **meine Stakeholder den Fortschritt mitverfolgen können und ich Übersicht über die Aufgaben behalte**.

**Akzeptanzkriterien:**

- Ein verfügbares KanBan Board mit den einzelnen Sprints und deren Ziele
- Die Funktionen Daten zu definieren und Cheklisten in den Zielen aufzubauen

---

#### **Aufgabenübersicht Sprint 1**


| Aufgabe                  | Status              |
| -------------------------- | --------------------- |
| Github zu Obsidian Setup | Alternativ erledigt |
| Architekturplanung       | erledigt            |
| Aufbau Kan-Ban Board     | erledigt            |

---

#### **Sprint Review**

⭐​​**Was wurde erreicht?**

- GitHub repo wurde erstellt
- IDE wurde mit GitHub verknüpft - Es wurde auf andere Lösung gewechselt - Da bessere Optionen zur Entwicklung
- Erster Entwurf einer groben Architekturplanung
- KanBan Board wurde erstellt - Microsoft Lists

![alt text](image-2.png)
*_KanBan Angfangs Sprint_

![alt text](image-3.png)
*_KanBan Ende Sprint_

#### 🏔️​ **Herausforderungen**

- Microsoft Lists bietet nicht alle benötigten Funktionen an. Es wurde am Anfang des 2. Sprints eine Ausweichmöglichkeit definiert
- Sprint 1 Zeitraum sehr klein


#### 📚​ **Lessons Learned**

- Mehr Austausch mit den Team-Kollegen und Collaboraters pflegen, um Lösungen zu vergleichen und voneinander zu profitieren. Durch einen Tipp von Teamkollegen, bin ich vollständig auf Visual-Studio gewechselt, da es wesentlich mehr Möglichkeiten anbietet, als Obsidian.

---

#### **Retrospektive**


| **📈 More Of**                                                                                                                                                                                             | **📉 Less Of**                                                                                       | **✅ Keep Doing**                                                                                                                                                       | **🛑 Stop Doing**                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mehr Austausch mit Team-Kollegen und Collaboraters pflegen**<br>• Lösungen vergleichen und voneinander profitieren <br>• Durch Teamkollegen-Tipp erfolgreich von Obsidian zu Visual Studio gewechselt | **Sprint-Zeitraum zu klein wählen**<br>• Sprint 1 Zeitraum war zu kurz für effektive Arbeitsweise | **Offenheit für Tool-Empfehlungen** <br>• Visual Studio bietet wesentlich mehr Möglichkeiten als Obsidian <br><br>** Proaktive Lösungssuche bei Tool-Limitationen** | ***Abhängigkeit von unvollständigen Tools ohne Backup-Plan***<br>• Microsoft Lists bietet nicht alle benötigten Funktionen <br>• Ausweichmöglichkeit wurde erst am Anfang des 2. Sprints definiert |

#### **Ausblick auf Sprint 2**

- Wechsel / Migration des KanBan-Board - **Tool-Migration abschließen** - Vollständiger Wechsel zu Visual Studio
- Start Entwicklung der Grundarchitektur
- GUI Planung und erste Umsetzung

### 1.6.2 Sprint 2



#### **Zeitraum**

9.5. - 2.6.2

---

#### **Sprintziel**

1. Erste Umsetzung und GUI
2. Start Entwicklung der Grundarchitektur
3. Verknüpfung der Elemente, API und Testphase

---


#### **User Stories mit Akzeptanzkriterien**
---

📍​**User Story 1:**


| Title:                  | Priority: | Estimate: |
| ------------------------- | ----------- | ----------- |
| Erste Umsetzung und GUI | High      | 1h        |



Als Entwickler
Möchte ich **Die Erste Umsetzung der Grundarchitektur Umsetzen**
damit ich **Connectivität zum Fitness-Tracker sicherstellen kann**.

**Akzeptanzkriterien:**

- Fehlerfreies herauffahren der Docker-Container
- Ereichbares Frontend mit GUI und dessen Grundfunktionen

---

📍​**User Story 2:**


| Title:                                                                           | Priority: | Estimate: |
| ---------------------------------------------------------------------------------- | ----------- | ----------- |
| Verknüpfung der Elemente, Testphase und allenfalls Evaluation von Erweiterungen | High      | 2d        |



Als Architekt
Möchte ich **sicherstellen, das die Container untereinander kommunizieren können und welche Erweiterungen an der Lösung vorgenommen werden können**
damit ich **das Projekt in die Testphase übergeben kann**.

**Akzeptanzkriterien:**

- Erreichbarkeit der Container untereinander
- Funktionales Frontend

---

📍​**User Story 3:**


| Title:                                                            | Priority: | Estimate: |
| ------------------------------------------------------------------- | ----------- | ----------- |
| Verbesserung der App-Visualisierung und Datenbank-Funktionalität | Medium    | 1d        |

Als Engineer
Möchte ich **Die Visualisierung der App verbessern um eine angenehmeres Benutzererlebnis zu gestalten. **
damit ich **meine User die App nutzen können und persistente Daten auch abrufen können.

**Akzeptanzkriterien:**

- Positives Feedback seitens Tester
- Persistenter Datenabruf

---

#### **Aufgabenübersicht Sprint 2**


| Aufgabe                                                                                           | Status   |
| --------------------------------------------------------------------------------------------------- | ---------- |
| Erste Umsetzung und GUI                                                                           | erledigt |
| Verknüpfung der Elemente, Testphase und allenfalls Evaluation von ErweiterungenArchitekturplanun | erledigt |
| Verbesserung der App-Visualisierung und Datenbank-Funktionalität                                 | erledigt |


---

#### **Sprint Review**

⭐​​**Was wurde erreicht?**

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

#### 🏔️​ **Herausforderungen**

- Fitness-Begeisterte tester Finden
- API-Funktionalitäten gewährleisten


#### 📚​ **Lessons Learned**

- Fitness-Begeisterte tester Finden
- API-Funktionalitäten gewährleisten

---

#### **Retrospektive**


| **📈 More Of**                                                                                                                                      | **📉 Less Of**                                                                          | **✅ Keep Doing**                                                                    | **🛑 Stop Doing**                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Frühzeitige Suche nach Fitness-Begeisterten für Tests<br /><br> <br />und Projekterweiterung in Erwägung setzen für Cloud-Native Ansatz<br><br> | **Zu späte Tester-Suche** <br>Tester-Rekrutierung nicht auf letzten Moment verschieben | ** Fokus auf Zielgruppe**<br>• Weiterhin gezielt für Fitnessbegeisterte Entwickeln | Evtl. Push-Benachrichtigungen on Hold setzen, um Cloud-Native Funktionalitäten zu priorisieren |

#### **Ausblick auf Sprint 3**

- Finale Version des GUI, Statistiken
- Übertrag auf AWS -> Cloud Native Ansatz
- Beta-Testing-Programm starten - Strukturiertes Feedback für Fitness-Begeisterte einrichten

### 1.6.3 Sprint 3



#### **Zeitraum**

2.6. - 9.7.25

---

#### **Sprintziel**

1. Verbesserung der App Visualisierung
2. Statistiken
3. Abschluss Datenbankfunktionalität
4. Dokumentation fertigstellen
5. Präsentation vorbereiten
6. Ende - Abgabe

✨ Projekterweiterungen:

7. ✨ PostgreSQL / SQLAlchemy Database
8. ✨ Weather API
9. ✨ AWS EC2 / CI/CD

---


#### **User Stories mit Akzeptanzkriterien**
---

📍​**User Story 1:**


| Title:                  | Priority: | Estimate: |
| ------------------------- | ----------- | ----------- |
| Verbesserung der App Visualisierung | High      | 1.5h        |



Als Benutzer
Möchte ich eine verbesserte und intuitive Benutzeroberfläche mit ansprechendem Design
damit ich die App effizient und angenehm nutzen kann.

**Akzeptanzkriterien:**

- Responsives Design für verschiedene Bildschirmgrößen
- Benutzerfreundliche Navigation und Layout
- Konsistente Farbgebung und Typografie
- Positive Bewertung durch Usability-Tests

---

📍​**User Story 2:**


| Title:                                                                           | Priority: | Estimate: |
| ---------------------------------------------------------------------------------- | ----------- | ----------- |
|  Statistiken-Dashboard implementieren | High      | 2d        |



Als Benutzer
Möchte ich **umfassende Statistiken und Datenvisualisierungen meiner Fitness-Daten** einsehen
damit ich meine Fortschritte **verfolgen und analysieren kann.**

**Akzeptanzkriterien:**

- Darstellung von Trainingsstatistiken in Charts/Grafiken
- Zeitraum-Filter für Datenanalyse (Tag, Woche, Monat)


---

📍​**User Story 3:**


| Title:                                                            | Priority: | Estimate: |
| ------------------------------------------------------------------- | ----------- | ----------- |
| AWS EC2 Deployment und CI/CD Pipeline | High    | 1.5d        |

Als DevOps Engineer
Möchte ich eine **automatisierte Deployment-Pipeline auf AWS EC2 einrichten**
damit ich **kontinuierliche Integration und Deployment gewährleisten kann.**

**Akzeptanzkriterien:**
- Erfolgreiche Deployment auf AWS EC2
- Automatisierte CI/CD Pipeline konfiguriert
---

📍**User Story 4:**

| Title:                                                            | Priority: | Estimate: |
| ------------------------------------------------------------------- | ----------- | ----------- |
| Datenbankfunktionalität abschliessen | High    | 1d        |

Als Entwickler
Möchte ich **die vollständige PostgreSQL/SQLAlchemy Integration finalisieren**
damit ich **zuverlässige Datenpersistierung und -abfrage gewährleisten kann.**

**Akzeptanzkriterien:**
- Datenbankmigrationen funktionsfähig
- Optimierte Datenbankabfragen implementiert


---

📍**User Story 5:**

| Title:                                                            | Priority: | Estimate: |
| ------------------------------------------------------------------- | ----------- | ----------- |
| Weather API Integration | Medium    | 0.5d        |

Als Benutzer
Möchte ich **aktuelle Wetterdaten in der App angezeigt bekommen**
damit ich **meine Outdoor-Trainings besser planen kann.**

**Akzeptanzkriterien:**
- Integration einer zuverlässigen Weather API
- Anzeige von aktuellen Wetterdaten und Vorhersage
- Standortbasierte Wetterinformationen
- Fehlerbehandlung bei API-Ausfällen
---

#### **Aufgabenübersicht Sprint 3**




| Aufgabe | Status |
|---------|--------|
| Verbesserung der App Visualisierung | Done |
| Statistiken-Dashboard implementieren | Done |
| Datenbankfunktionalität abschliessen | Done|
| Weather API Integration | Done |
| Dokumentation fertigstellen | Done |
| AWS EC2 Deployment und CI/CD Pipeline | Done |
| Präsentation vorbereiten | Done |

---

#### **Sprint Review**

⭐​​**Was wurde erreicht?**

- EC2 Instanz erreichbar, alle Container gesund
- Datenbank wurde von JSON zu richtiger Datenbank migriert
- Statistiken wurden eingebaut
- Weather API eingebaut, zeigt aktuelles Wetter von Zürich an.


![alt text](image-9.png)
Sprint 3 Spalte


![alt text](image-11.png)
Alle Einträge mit Userstories 

#### 🏔️​ **Herausforderungen**

- Übertrag der alten "Datenbank"
- Lange Wartezeiten seitens API-Funktionalität


#### 📚​ **Lessons Learned**

- Gelernt, externe API einzusetzen
- Eine richtige Datenbank bietet bessere persistenz und schützt vor Daten-Korrumpierung
- Usability / Friendly User interfaces gestalten

---

#### **Retrospektive**

| **📈 More Of**                                                                                                                                      | **📉 Less Of**                                                                          | **✅ Keep Doing**                                                                    | **🛑 Stop Doing**                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Frühzeitige API-Integration planen<br /><br>Mehr Zeit für Datenmigration einplanen<br><br>Cloud-Native Ansatz konsequent verfolgen | **Zu späte Performance-Optimierung** <br>API-Wartezeiten nicht erst am Ende addressieren | **Fokus auf Datenpersistenz**<br>• Weiterhin auf robuste Datenbankintegration setzen | JSON-basierte Datenstrukturen für kritische Daten vermeiden, da sie anfällig für Korruption sind |

+++ Alle User Stories sind im KanBan ersichtlich
https://semesterarbeit3liliam.atlassian.net/jira/software/projects/KAN/boards/1

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

### 1.7.4 Neue Struktur (Persistent + Weather API)

![](assets/20250707_190323_image.png)

+++ Für bessere/stabilere persistenz innerhalb der Umgebung habe ich mich dazu entschieden, von einem simplen JSON-File als storage-solution für die Daten, zu einer Datenbank zu wechseln.

Risiken des JSON-Files:

⚠️ **Weniger robust als echte DBs**

* **Corruption** : JSON-File kann bei unvollständigem Write corrumpiert werden
* **No Transactions** : Kein Rollback bei Fehlern
* **Race Conditions** : Gleichzeitige Writes können Daten zerstören

**🐘 PostgreSQL Integration: Vorteile**

* **Von JSON-Files zu echter Datenbank** - Data Persistence
* **SQLAlchemy ORM** - Objekt-relationale Mappings für Python
* **ACID-Transactions** - Datenintegrität und Konsistenz garantiert
* **Foreign Key Relationships** - Users ↔ Workouts Verknüpfungen
* **Performance Optimierung** - SQL-Indexes und Aggregationen

+++ Zudem, wurde für eine vollständige Demonstration für die Kommunikation meiner Microservices in die Aussenwelt, ein ***Weather Microservice*** hinzugefügt:

**🌤️ Weather Service Integration:**

* **Neuer Microservice** - Externe API Integration
* **OpenWeatherMap API** - Live Wetter-Daten für Workout-Planung
* **Graceful Degradation / Error Resilience** - Demo-Mode Fallback bei API-Ausfall
* **Personalisierte Empfehlungen** - Workout-Advice basierend auf Wetter

**🏗️ Architektur-Verbesserungen:**

* **4 Microservices** statt 3
* **Shared Database** - Konsistente Datenarchitektur
* **External API** - Real-Life Anwendungszweck

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

Gesamtarchitektur des Systems

![](assets/20250707_200029_image.png)

## 2.2 Microservices

**Jeder Service hat eine klare Rolle:**

* 🖥️**Frontend** = UI & Orchestrierung
* 👤**User** = Profile Management
* 💪**Workout** = Exercise Logging
* 📊**Stats** = Analytics & Insights
* 🌤️**Weather** = External Integratio

### 2.2.1 Frontend Service

🖥️ Web-Interface und API-Gateway für alle anderen Services

**Port:** 5000 | **Tech:** Flask + Templates + Bootstrap

**Funktionen:**

* User Dashboard mit Workout-Historie
* Responsive UI mit Bootstrap-Design
* Service-übergreifende API-Orchestrierung
* Health-Check Monitoring aller Services

```python
@app.route('/user/<user_id>')
def user_dashboard(user_id):
    user = requests.get(f"{USER_SERVICE_URL}/users/{user_id}")
    workouts = requests.get(f"{WORKOUT_SERVICE_URL}/workouts?user_id={user_id}")
    stats = requests.get(f"{STATS_SERVICE_URL}/stats/{user_id}/summary")
    return render_template('dashboard.html', user=user, workouts=workouts, stats=stats)
```

### 2.2.2 User Service

👤 Benutzerverwaltung und Profil-Management

**Port:** 5001 | **Tech:** Flask + SQLAlchemy + PostgreSQL

Funktionen:**

* CRUD-Operationen für User-Profile
* Email-Uniqueness Validation
* User-Authentifizierung Vorbereitung
* Basis für alle anderen Service

```python
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'], age=data.get('age'))
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201
```

### 2.2.3 Workout Service

💪 Workout-Logging und Exercise-Management

**Port:** 5002 | **Tech:** Flask + SQLAlchemy + PostgreSQL

**Funktionen:**

- Workout-Erfassung (Typ, Dauer, Kalorien)
- User-Validation über User Service
- Foreign Key Relationships zu Users
- Basis-Daten für Statistics Service

```python
@app.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()
    if not verify_user_exists(data['user_id']):
        return jsonify({"error": "User not found"}), 404
  
    workout = Workout(user_id=data['user_id'], exercise_type=data['exercise_type'])
    db.session.add(workout)
    db.session.commit()
    return jsonify(workout.to_dict()), 201
```

### 2.2.4 Stats Service

📊 Analytics und Performance-Tracking

**Port:** 5003 | **Tech:** Flask + SQLAlchemy + PostgreSQL

**Funktionen:**

- SQL-Aggregationen für Workout-Statistiken
- Personal Records Tracking
- Weekly/Monthly Trends
- Read-Only Database Access

```python
@app.route('/stats/<user_id>/summary', methods=['GET'])
def get_user_stats_summary(user_id):
    result = db.session.query(
        func.count(Workout.id).label('total_workouts'),
        func.sum(Workout.duration).label('total_duration'),
        func.avg(Workout.calories_burned).label('avg_calories')
    ).filter(Workout.user_id == user_id).first()
  
    return jsonify({
        "total_workouts": result.total_workouts,
        "total_duration": result.total_duration,
        "average_calories": round(float(result.avg_calories or 0), 2)
    })
```

### 2.2.5 Weather Service

🌤️ Wetter-basierte Workout-Empfehlungen

**Port:** 5004 | **Tech:** Flask + External API Integration

**Funktionen:**

- OpenWeatherMap API Integration
- Personalisierte Workout-Advice
- Demo-Mode Fallback
- External API Error Handling

```python
@app.route('/weather/workout-advice', methods=['GET'])
def get_workout_advice():
    weather_data = get_current_weather()
  
    if weather_data.get('demo_mode'):
        return jsonify({"advice": "Demo mode - indoor workouts recommended"})
  
    temp = weather_data['temperature']
    if temp > 25:
        advice = "Hot weather - stay hydrated, prefer early morning workouts!"
    elif temp < 5:
        advice = "Cold weather - warm up thoroughly, layer clothing!"
    else:
        advice = "Perfect weather for outdoor activities!"
  
    return jsonify({"advice": advice, "weather": weather_data})
```

# 3. ☁️ Deployment & DevOps

## 3.1 AWS EC2 Setup

🚀 EC2 Instance Erstellen:

- **AWS Console** → EC2 Dashboard → "Launch Instance"
- **Image**: Ubuntu Server 22.04 LTS (free tier eligible)
- **Instance Type**: t2.micro (free tier)
- **Key Pair**: ED25519 (moderne Verschlüsselung)
- **Security Group**:

  - SSH (Port 22) - Your IP only (später auf 0.0.0.0/0 erweitert)
  - HTTP (Port 80) - Anywhere (0.0.0.0/0)
  - HTTPS (Port 443) - Anywhere (0.0.0.0/0)

  ![](assets/20250707_201347_image.png)
- ![](assets/20250707_201411_image.png)

SSH Connection:

```bash
chmod 400 your-key.pem
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

Dependencies Installation:

```bash
sudo apt update
sudo apt install docker.io docker-compose git -y
sudo usermod -aG docker ubuntu
# Logout/Login für Docker Permissions
```

![](assets/20250707_201427_image.png)

![](assets/20250707_201452_image.png)

📦 Code Deployment

Repository Clone:

```bash
git clone https://github.com/gitlilia-tbz/ICTNE24_Semesterarbeit3_L.M.git
cd ICTNE24_Semesterarbeit3_L.M
```

Environment Configuration:

```bash
nano .env
```

**Inhalt:**

```
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-super-secret-production-key
USER_SERVICE_URL=http://user-service:5001
WORKOUT_SERVICE_URL=http://workout-service:5002
STATS_SERVICE_URL=http://stats-service:5003
WEATHER_SERVICE_URL=http://weather-service:5004

# PostgreSQL Configuration
DB_PASSWORD=secure_production_password_456
DATABASE_URL=postgresql://trackmygym_user:secure_production_password_456@postgres:5432/trackmygym

# Weather API
OPENWEATHER_API_KEY=your_openweather_api_key
```

Initial Deployment:

```bash
docker-compose up -d
```

![](assets/20250707_201524_image.png)

Spätere Korrekturen: SSH Port 22 auf "Anywhere" (0.0.0.0/0) erweitert

![](assets/20250707_201656_image.png)

## 3.2 CI/CD Pipeline

🔄 Pipeline Setup GitHub Secrets Config

GitHub Secrets:

**Repository Settings** → **Secrets and Variables** → **Actions**

**Secrets hinzugefügt:**

* `HOST` = EC2 Public IP Address
* `USERNAME` = ubuntu
* `PRIVATE_KEY` = Complete SSH private key (.pem file content)

  ![](assets/20250707_203650_image.png)

## 3.3 GitHub Actions

**`.github/workflows/deploy.yml`:**

```yaml
name: Deploy TrackMyGym to AWS EC2
on:
  push:
    branches: [ main, master ]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    - name: Deploy to EC2
      uses: appleboy/ssh-action@v0.1.8
      with:
        host: ${{ secrets.HOST }}
        username: ${{ secrets.USERNAME }}
        key: ${{ secrets.PRIVATE_KEY }}
        script: |
          cd ICTNE24_Semesterarbeit3_L.M
          git pull origin main
          docker-compose down
          docker-compose build --no-cache
          docker-compose up -d
          docker system prune -f
```

**`.github/workflows/pr-check.yml`:**

```yaml
name: PR Health Check
on:
  pull_request:
    branches: [ main, master ]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    - name: Build Docker images
      run: docker-compose build
    - name: Test containers start
      run: |
        docker-compose up -d
        sleep 45
        docker-compose ps
        docker-compose down
```

## 3.4 Produktionsumgebung

🛡️Production

Security Group Update:

**Problem** : SSH nur von eigener IP → GitHub Actions kann nicht deployen

**Lösung** : SSH Port 22 auf "Anywhere" (0.0.0.0/0) erweitert

Optimierungen für Produktion:

* **Frontend app.py** : SECRET_KEY aus Environment Variable
* **Docker-compose** : Production Environment Variables
* **No Volumes** : Code in Container images (immutable deployment)
* **Health Checks** : PostgreSQL health checks für Service Dependencies

---

📊 PostgreSQL Migration:

Database Upgrade;

**Von JSON Files zu PostgreSQL:**

* **init.sql** : Database Schema mit Sample Data
* **SQLAlchemy Models** : User & Workout Entities
* **All Services** : Umstellung auf PostgreSQL
* **Requirements.txt** : psycopg2-binary + Flask-SQLAlchemy

Weather Service Integration:

* **Neuer Microservice** : External API Integration
* **OpenWeatherMap API** : Live Weather Data
* **Fallback Strategy** : Demo Data bei API-Ausfall
* **Docker-compose Extension** : weather-service hinzugefüg

+++ Bonus: Weather App Setup: +++

📋 API Account & Key Setup

1. OpenWeatherMap Account erstellen:

- **Website**: https://openweathermap.org/api
- **Sign Up**: Kostenloser Account (keine Kreditkarte nötig)
- **Free Tier**: 1,000 API calls/Tag, 60 calls/Minute

2. API Key generieren**

- **Dashboard** → **"My API Keys"**
- **Create Key** → Name: "TrackMyGym"
- **Key erhalten**: `BEISPIELKEY`
- **⏰ Aktivierung**: 10-15 Minuten warten -> WICHTIG

3. API Key testen

```bash
# Direct API test
curl "https://api.openweathermap.org/data/2.5/weather?lat=47.3769&lon=8.5417&appid=YOUR_API_KEY&units=metric"

# Expected Response:
{"coord":{"lon":8.54,"lat":47.38},"weather":[...],"main":{"temp":15.2}}
```

---

🏗️ Zweite Phase: Weather Service Development

**4. Service Directory erstellen**

```bash
mkdir weather-service
cd weather-service
```

**5. Requirements definieren**

**`weather-service/requirements.txt`:**

```txt
Flask==2.3.3
Flask-CORS==4.0.0
requests==2.31.0
```

**6. Dockerfile erstellen**

**`weather-service/Dockerfile`:**

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5004
CMD ["python", "app.py"]
```

**7. Weather Service Logic entwickeln**

**`weather-service/app.py`:**

```python
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

WEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', 'demo_key')
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy", 
        "service": "weather-service",
        "api_key_configured": WEATHER_API_KEY != 'demo_key'
    })

@app.route('/weather/current', methods=['GET'])
def get_current_weather():
    try:
        # Zürich coordinates
        params = {
            'lat': 47.3769,
            'lon': 8.5417,
            'appid': WEATHER_API_KEY,
            'units': 'metric'
        }
  
        response = requests.get(WEATHER_URL, params=params, timeout=10)
  
        # API Key invalid/not configured
        if response.status_code == 401:
            return jsonify({
                "error": "Weather API key not configured or invalid",
                "demo_mode": True,
                "weather_data": get_demo_weather()
            }), 200
  
        if response.status_code == 200:
            weather_data = response.json()
            return jsonify(process_weather_data(weather_data))
        else:
            return jsonify({"error": "Weather service unavailable"}), 503
  
    except Exception as e:
        return jsonify({
            "error": "Weather service error",
            "demo_mode": True,
            "weather_data": get_demo_weather()
        }), 200

def get_demo_weather():
    """Fallback demo data when API unavailable"""
    return {
        "temperature": 18.5,
        "feels_like": 17.8,
        "humidity": 65,
        "weather_main": "Clouds",
        "weather_description": "Partly Cloudy",
        "wind_speed": 2.1,
        "city": "Zurich",
        "country": "CH",
        "demo_mode": True
    }

def process_weather_data(raw_data):
    """Process API response into app-friendly format"""
    return {
        "temperature": round(raw_data['main']['temp'], 1),
        "feels_like": round(raw_data['main']['feels_like'], 1),
        "humidity": raw_data['main']['humidity'],
        "weather_main": raw_data['weather'][0]['main'],
        "weather_description": raw_data['weather'][0]['description'].title(),
        "wind_speed": raw_data.get('wind', {}).get('speed', 0),
        "city": raw_data.get('name', 'Zurich'),
        "country": raw_data.get('sys', {}).get('country', 'CH'),
        "demo_mode": False
    }

@app.route('/weather/workout-advice', methods=['GET'])
def get_workout_advice():
    """Generate workout recommendations based on weather"""
    try:
        # Get current weather
        weather_response = requests.get("http://localhost:5004/weather/current")
        weather_data = weather_response.json()
  
        if weather_data.get('demo_mode'):
            weather_info = weather_data['weather_data']
        else:
            weather_info = weather_data
  
        advice = generate_workout_advice(weather_info)
        return jsonify({"weather": weather_info, "advice": advice})
  
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_workout_advice(weather_info):
    """Smart workout recommendations based on conditions"""
    temp = weather_info['temperature']
    weather_main = weather_info['weather_main']
  
    advice = {
        "primary_message": "",
        "activity_suggestions": [],
        "safety_tips": [],
        "gear_recommendations": []
    }
  
    # Weather-based recommendations
    if weather_main in ['Rain', 'Drizzle']:
        advice["primary_message"] = "🏠 Better to exercise indoors today"
        advice["activity_suggestions"] = ["Indoor gym session", "Home yoga", "Treadmill running"]
        advice["gear_recommendations"] = ["Yoga mat", "Indoor shoes"]
    elif temp > 25:
        advice["primary_message"] = "☀️ Hot weather - stay hydrated!"
        advice["activity_suggestions"] = ["Early morning runs", "Swimming", "Water sports"]
        advice["safety_tips"] = ["Stay hydrated", "Avoid midday sun", "Take breaks"]
        advice["gear_recommendations"] = ["Sun hat", "Extra water", "SPF 30+"]
    elif temp < 5:
        advice["primary_message"] = "❄️ Cold weather - warm up thoroughly!"
        advice["activity_suggestions"] = ["Indoor workouts", "Hot yoga", "Gym sessions"]
        advice["safety_tips"] = ["Warm up indoors", "Layer clothing", "Protect extremities"]
        advice["gear_recommendations"] = ["Thermal layers", "Gloves", "Warm hat"]
    else:
        advice["primary_message"] = "🌟 Perfect weather for outdoor workouts!"
        advice["activity_suggestions"] = ["Running", "Cycling", "Outdoor sports", "Hiking"]
        advice["gear_recommendations"] = ["Comfortable athletic wear", "Running shoes"]
  
    return advice

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=False)
```

---

🔗 Frontend Integration

8. Frontend Service erweitern

**`frontend/app.py` - Weather Integration hinzufügen:**

```python
WEATHER_SERVICE_URL = os.getenv('WEATHER_SERVICE_URL', 'http://localhost:5004')

@app.route('/user/<user_id>')
def user_dashboard(user_id):
    # ... existing code ...
  
    # Get weather info for workout planning
    weather_info = get_weather_info()
  
    return render_template('dashboard.html', 
                         user=user, 
                         workouts=workouts, 
                         stats=stats,
                         weather=weather_info)  # ← New weather data

def get_weather_info():
    """Get current weather information"""
    try:
        response = requests.get(f"{WEATHER_SERVICE_URL}/weather/current", timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        logger.warning(f"Weather service unavailable: {e}")
    return None

# Weather API proxy endpoints
@app.route('/api/weather/current')
def weather_current():
    try:
        response = requests.get(f"{WEATHER_SERVICE_URL}/weather/current", timeout=5)
        return response.json(), response.status_code
    except:
        return {"error": "Weather service unavailable"}, 503

@app.route('/api/weather/workout-advice')
def weather_workout_advice():
    try:
        response = requests.get(f"{WEATHER_SERVICE_URL}/weather/workout-advice", timeout=5)
        return response.json(), response.status_code
    except:
        return {"error": "Weather advice unavailable"}, 503
```

🔗 dashboard.html 

9. **Wettervorschläge / Workoutadvice für die Wettervorschläge / Workout-Advice ergänzen**
    
  ```html
  // Add this to the <script> section in dashboard.html

function loadWorkoutAdvice() {
    const adviceContainer = document.getElementById('workout-advice');
    adviceContainer.innerHTML = '<div class="text-center"><i class="fas fa-spinner fa-spin"></i> Getting advice...</div>';
    
    fetch('/api/weather/workout-advice')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                adviceContainer.innerHTML = `<div class="alert alert-danger">Error: ${data.error}</div>`;
                return;
            }
            
            const advice = data.advice;
            let html = `
                <div class="alert alert-info">
                    <h6><i class="fas fa-brain me-2"></i>${advice.primary_message}</h6>
                    
                    <strong>Recommended Activities:</strong>
                    <ul class="mb-2">
                        ${advice.activity_suggestions.map(activity => `<li>${activity}</li>`).join('')}
                    </ul>
                    
                    ${advice.safety_tips.length > 0 ? `
                    <strong>Safety Tips:</strong>
                    <ul class="mb-2">
                        ${advice.safety_tips.map(tip => `<li>${tip}</li>`).join('')}
                    </ul>
                    ` : ''}
                    
                    ${advice.gear_recommendations.length > 0 ? `
                    <strong>Gear Recommendations:</strong>
                    <ul class="mb-0">
                        ${advice.gear_recommendations.map(gear => `<li>${gear}</li>`).join('')}
                    </ul>
                    ` : ''}
                </div>
            `;
            adviceContainer.innerHTML = html;
        })
        .catch(error => {
            adviceContainer.innerHTML = `<div class="alert alert-danger">Error loading advice: ${error}</div>`;
        });
}

// Auto-refresh weather every 30 minutes
setInterval(function() {
    if (window.location.pathname.includes('/user/')) {
        location.reload();
    }
}, 30 * 60 * 1000);
  ```

---

🐳 9. Docker Integration

Docker-Compose erweitern:

**`docker-compose.yml` - Weather Service hinzufügen:**

```yaml
services:
  # ... existing services ...
  
  weather-service:
    build: ./weather-service
    environment:
      - FLASK_ENV=production
      - FLASK_DEBUG=False
      - OPENWEATHER_API_KEY=${OPENWEATHER_API_KEY}  # ← Environment Variable
    networks:
      - fitness-network
    restart: unless-stopped

  frontend:
    build: ./frontend
    environment:
      # ... existing vars ...
      - WEATHER_SERVICE_URL=http://weather-service:5004  # ← Service URL
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - fitness-network
    restart: unless-stopped
```

10.  Environment Configuration

**`.env` file erweitern:**

```bash
# Existing variables...
FLASK_ENV=production
SECRET_KEY=your-secret-key
DB_PASSWORD=secure_password

# Weather API Configuration
OPENWEATHER_API_KEY=BEISPIELKEY  # ← API Key hinzufügen
```

---

🖥️ 11. UI Integration

Dashboard Template erweitern:

**`templates/dashboard.html` - Weather Widget hinzufügen:**

```html
<!-- Weather Widget in Right Sidebar -->
{% if weather %}
<div class="card mb-4">
    <div class="card-header">
        <h3 class="mb-0"><i class="fas fa-cloud-sun me-2"></i>Weather & Workout</h3>
    </div>
    <div class="card-body">
        <div class="text-center mb-3">
            <div class="weather-temp">{{ weather.temperature }}°C</div>
            <div>{{ weather.weather_description }}</div>
        </div>
  
        {% if weather.outdoor_suitable %}
            <div class="alert alert-success">Great for outdoor workouts!</div>
        {% else %}
            <div class="alert alert-warning">Better to exercise indoors</div>
        {% endif %}
  
        <button class="btn btn-outline-primary btn-sm w-100" onclick="loadWorkoutAdvice()">
            <i class="fas fa-lightbulb me-2"></i>Get Workout Advice
        </button>
  
        <div id="workout-advice" class="mt-3"></div>
  
        {% if weather.demo_mode %}
        <small class="text-muted">Demo weather data (API key not configured)</small>
        {% endif %}
    </div>
</div>
{% endif %}
```

12. JavaScript für Workout Advice

```javascript
function loadWorkoutAdvice() {
    fetch('/api/weather/workout-advice')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('workout-advice').innerHTML = 
                    `<div class="alert alert-danger">Error: ${data.error}</div>`;
                return;
            }
  
            const advice = data.advice;
            let html = `
                <div class="alert alert-info">
                    <h6>${advice.primary_message}</h6>
                    <strong>Recommended Activities:</strong>
                    <ul>${advice.activity_suggestions.map(a => `<li>${a}</li>`).join('')}</ul>
                </div>
            `;
            document.getElementById('workout-advice').innerHTML = html;
        });
}
```

---

🚀 13. Deployment

Build & Deploy:

```bash
# Build new weather service
docker-compose build weather-service

# Deploy complete stack
docker-compose down
docker-compose up -d

# Verify deployment
docker-compose ps
curl http://localhost/api/weather/current
```

14. Testing & Verification

```bash
# Test weather service health
curl http://localhost:5004/health

# Test weather data
curl http://localhost/api/weather/current

# Test workout advice
curl http://localhost/api/weather/workout-advice

# Check environment variable
docker-compose exec weather-service env | grep OPENWEATHER
```

Features, welche neu dazugekommen sind::

- ✅ **Live Wetter-Daten** für Zürich
- ✅ **Workout Recommendations** basierend auf Wetter
- ✅ **Demo Mode Fallback** bei API-Ausfall -> Demo Daten werden bei nicht-Erreichbarkeit angezeigt -> **Error Handling** für externe Dependencies
- ✅ **UI Integration** im User Dashboard, auch für Mobil
- ✅ **Environment Configuration** für API Keys

# TrackMyGym - Projekt Ordnerstruktur

<pre><div class="relative group/copy rounded-lg"><div class="sticky opacity-0 group-hover/copy:opacity-100 top-2 py-2 h-12 w-0 float-right"><div class="absolute right-0 h-8 px-2 items-center inline-flex"><button class="inline-flex
  items-center
  justify-center
  relative
  shrink-0
  can-focus
  select-none
  disabled:pointer-events-none
  disabled:opacity-50
  disabled:shadow-none
  disabled:drop-shadow-none text-text-300
          border-transparent
          transition
          font-ui
          tracking-tight
          duration-300
          ease-[cubic-bezier(0.165,0.85,0.45,1)]
          hover:bg-bg-400
          aria-pressed:bg-bg-400
          aria-checked:bg-bg-400
          aria-expanded:bg-bg-300
          hover:text-text-100
          aria-pressed:text-text-100
          aria-checked:text-text-100
          aria-expanded:text-text-100 h-8 w-8 rounded-md active:scale-95 backdrop-blur-md" type="button" aria-label="In die Zwischenablage kopieren" data-state="closed"><div class="relative"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" viewBox="0 0 256 256" class="transition-all opacity-100 scale-100"><path d="M200,32H163.74a47.92,47.92,0,0,0-71.48,0H56A16,16,0,0,0,40,48V216a16,16,0,0,0,16,16H200a16,16,0,0,0,16-16V48A16,16,0,0,0,200,32Zm-72,0a32,32,0,0,1,32,32H96A32,32,0,0,1,128,32Zm72,184H56V48H82.75A47.93,47.93,0,0,0,80,64v8a8,8,0,0,0,8,8h80a8,8,0,0,0,8-8V64a47.93,47.93,0,0,0-2.75-16H200Z"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" viewBox="0 0 256 256" class="absolute top-0 left-0 transition-all opacity-0 scale-50"><path d="M229.66,77.66l-128,128a8,8,0,0,1-11.32,0l-56-56a8,8,0,0,1,11.32-11.32L96,188.69,218.34,66.34a8,8,0,0,1,11.32,11.32Z"></path></svg></div></button></div></div><div class=""><pre class="code-block__code !my-0 !rounded-lg !text-sm !leading-relaxed"><code><span><span>ICTNE24_Semesterarbeit3_L.M/
</span></span><span>│
</span><span>├── 📄 docker-compose.yml              # Orchestrierung aller Services
</span><span>├── 📄 init.sql                        # PostgreSQL Schema & Sample Data
</span><span>├── 📄 .env                           # Environment Variables (nicht in Git!)
</span><span>├── 📄 .gitignore                     # Git ignore rules
</span><span>├── 📄 README.md                      # Projekt Dokumentation
</span><span>│
</span><span>├── 📁 .github/                       # GitHub Actions CI/CD
</span><span>│   └── 📁 workflows/
</span><span>│       ├── 📄 deploy.yml             # Production Deployment Pipeline
</span><span>│       └── 📄 pr-check.yml           # Pull Request Health Checks
</span><span>│
</span><span>├── 📁 frontend/                      # Frontend Service (Port 5000)
</span><span>│   ├── 📄 app.py                     # Flask App + Templates + API Gateway
</span><span>│   ├── 📄 Dockerfile                 # Container Definition
</span><span>│   ├── 📄 requirements.txt           # Python Dependencies
</span><span>│   ├── 📁 templates/                 # Jinja2 HTML Templates
</span><span>│   │   ├── 📄 base.html              # Base Template Layout
</span><span>│   │   ├── 📄 index.html             # Homepage mit User Overview
</span><span>│   │   └── 📄 dashboard.html         # User Dashboard mit Weather Widget
</span><span>│   └── 📁 static/                    # CSS, JavaScript, Images
</span><span>│       ├── 📁 css/
</span><span>│       │   └── 📄 style.css          # Custom Styling + Bootstrap
</span><span>│       └── 📁 js/
</span><span>│           └── 📄 app.js             # Frontend JavaScript Logic
</span><span>│
</span><span>├── 📁 user-service/                  # User Service (Port 5001)
</span><span>│   ├── 📄 app.py                     # Flask API + SQLAlchemy User Model
</span><span>│   ├── 📄 Dockerfile                 # Container mit PostgreSQL Support
</span><span>│   └── 📄 requirements.txt           # Flask + SQLAlchemy + psycopg2
</span><span>│
</span><span>├── 📁 workout-service/               # Workout Service (Port 5002)
</span><span>│   ├── 📄 app.py                     # Flask API + SQLAlchemy Workout Model
</span><span>│   ├── 📄 Dockerfile                 # Container mit PostgreSQL Support
</span><span>│   └── 📄 requirements.txt           # Flask + SQLAlchemy + psycopg2 + requests
</span><span>│
</span><span>├── 📁 stats-service/                 # Stats Service (Port 5003)
</span><span>│   ├── 📄 app.py                     # Flask API + SQL Aggregations
</span><span>│   ├── 📄 Dockerfile                 # Container mit PostgreSQL Support
</span><span>│   └── 📄 requirements.txt           # Flask + SQLAlchemy + psycopg2 + requests
</span><span>│
</span><span>├── 📁 weather-service/               # Weather Service (Port 5004)
</span><span>│   ├── 📄 app.py                     # Flask API + OpenWeatherMap Integration
</span><span>│   ├── 📄 Dockerfile                 # Container Definition
</span><span>│   └── 📄 requirements.txt           # Flask + requests
</span><span>│
</span><span>└── 📁 nginx/                         # Reverse Proxy
</span><span>    ├── 📄 Dockerfile                 # Nginx Container
</span><span>    └── 📄 nginx.conf                 # Proxy Configuration</span></code></pre></div></div></pre>

🔗 Service Dependencies

````mermaid


graph TD
    Frontend --> UserService
    Frontend --> WorkoutService  
    Frontend --> StatsService
    Frontend --> WeatherService
  
    WorkoutService -.-> UserService
    StatsService -.-> WorkoutService
    WeatherService --> OpenWeatherAPI
  
    UserService --> PostgreSQL
    WorkoutService --> PostgreSQL
    StatsService --> PostgreSQL
````

📊 File Count Summary

<pre class="font-styrene border-border-100/50 overflow-x-scroll w-full rounded border-[0.5px] shadow-[0_2px_12px_hsl(var(--always-black)/5%)]"><table class="bg-bg-100 min-w-full border-separate border-spacing-0 text-sm leading-[1.88888] whitespace-normal"><thead class="border-b-border-100/50 border-b-[0.5px] text-left"><tr class="[tbody>&]:odd:bg-bg-500/10"><th class="text-text-000 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] font-400 px-2 [&:not(:first-child)]:border-l-[0.5px]">Kategorie</th><th class="text-text-000 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] font-400 px-2 [&:not(:first-child)]:border-l-[0.5px]">Anzahl Dateien</th></tr></thead><tbody><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>Python Apps</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">5 (1 Frontend + 4 Microservices)</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>Dockerfiles</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">5 (alle Services + nginx)</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>Requirements</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">5 (Python Dependencies)</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>Templates</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">3 (HTML Jinja2 Templates)</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>Static Files</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">2 (CSS + JavaScript)</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>Config Files</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">4 (docker-compose, nginx, init.sql, .env)</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>CI/CD</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">2 (GitHub Actions Workflows)</td></tr><tr class="[tbody>&]:odd:bg-bg-500/10"><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]"><strong>Documentation</strong></td><td class="border-t-border-100/50 [&:not(:first-child)]:-x-[hsla(var(--border-100) / 0.5)] border-t-[0.5px] px-2 [&:not(:first-child)]:border-l-[0.5px]">1 (README.md)</td></tr></tbody></table></pre>

**Total: ~27 Dateien**

---

🎨 Code Distribution

* **~60% Backend Logic** (Flask APIs, SQLAlchemy Models, Database Integration)
* **~20% Infrastructure** (Docker, CI/CD, Database Schema)
* **~15% Frontend** (Templates, CSS, JavaScript)
* **~5% Configuration** (Environment, Nginx, Documentation)

# 4. 📱 User Interface

## 4.1 Frontend Design

**Designkonzept und visuelle Gestaltung**
![alt text](image-6.png)
GUI auf Desktop Oberfläche

![alt text](mobile.gif)
GUI auf Mobiler Oberfläche

## 4.2 User Experience


![alt text](refresh.gif)
***Quick Actions - Systemstatus:***
Die Applikation bietet die Möglichkeitn an, den Systemhealth zu aktualisieren. Somit bleiben die User vortlaufend über den Service-Health informiert, ohne den Admin aufrufen zu müssen.

![alt text](user_erstellen.gif)
***User erstellen und User Dashboard:***
Einen User ganz einfach und rasch erstellen: Name, Email und Angaben zur Person werden für die Usererstellung angefragt, aber nicht zwingend benötigt. Nach der erstellung kann man direkt auf das Dashboard zugreifen.

![alt text](workout_hinterlegen.gif)
***Wetter-Vorschläge und hinterlegen eines ersten Workouts:***
Bei bedarf kann man Anhand der Wetter-Vorschläge seine Workouts planen. Vorbereitet auf jede Wetterbedingung! Anhand eines Scripts werden mit Hilfe der Wetter-Angaben personalisierte Vorschläge generiert.
![alt text](weitere_workouts.gif)
***Weitere Workouts hinzufügen, Statistiken und Farb-Kodierungen:*** 
Es können weitere Workouts im Dashboard hinterlegt werden. Für eine übersichtliche Darstellung hat jeder Workout-Typ einen eigenen Farbcode. Die Workouts werden analysiert und in der Statistik angezeigt / zusammengerechnet.


# 5. 🧪 Testing & Qualitätssicherung

## 5.1 Pipeline-Testing
![alt text](image-8.png)
Der erste Test-Push vom Repo aus war erfolgreich, nachdem alle Secrets korrekt hinterlegt wurden
![alt text](image-7.png)
Der erste Test-Push war eine Anpassung des Übertitels in "Test fuer pipeline!" innerhalb des **dashboard.html** file.


## 5.2 User-Testing

**Benutzertests und Feedback:** Beta-Test

📋 Beta-Test Phase Dokumentation



**Zeitraum:** 3 Tage (6.7. - 8.7.2025)  
**Testpersonen:** 2 (1 männlich/28J, 1 weiblich/31J) - beide sportlich aktiv  
**Gesamtbewertung:** Sehr gut ⭐⭐⭐

---

**👥 Testpersonen**
- **S. (M, 28):** Kraftsportler, 5x/Woche Training
- **M. (W, 31):** Kickboxen und Joggen, , 1x/Woche Training
---

**✅ Positive Ergebnisse**
- **Benutzerfreundlichkeit:** App ist übersichtlich und schnell bedienbar
- **Weather-Feature:** Überraschend nützlich für Outdoor-Sport-Planung
- **Design:** Moderne, ansprechende Optik


---

**🔧 Feedback & Verbesserungswünsche seitens Probanten**

| Feature | Priorität | Details |
|---------|-----------|---------|
| **Schrittzähler Integration** | Hoch | Beide wünschen tägliche Schritte-Tracking |
| **Eigene Tagesziele** | Hoch | Personalisierte Trainings-/Kalorienziele definieren |
| **Anpassbare Themes** | Mittel | Dark Mode und Farbthemen-Auswahl |
| **Dauerhafte Verfügbarkeit** | Kritisch | App war 2x offline (AWS Learner Lab Problem) |

---

**🐛 Identifizierte Probleme**
- **Server Downtime:** App nicht erreichbar durch AWS Learner Lab Limitationen

---

**🎯 Nächste Schritte**
1. **Kritisch:** Vielleicht eine Migration zu stabilerer Cloud-Infrastruktur
2. **Hoch:** Schrittzähler + Tagesziele implementieren
3. **Mittel:** Theme-System mit Dark Mode oder weiteren Farben

**Fazit:** App ist grundsätzlich sehr gut, braucht aber stabile Hosting-Lösung und erweiterte Personalisierung für Produktiveinsatz.

+++ Feeback seitens Probanten:

***"Nice", "Das einfache Dashboard gefällt mir mega" "Voll Geil", "Das Design gefällt mir"***


## 5.3 10 Testfälle

| Test # | Wenn das... | Dann das... | Status |
|--------|-------------|-------------|---------|
| 1 | User mit neuer Email registriert | Account wird erstellt und in PostgreSQL gespeichert | ✅ PASS |
| 2 | User mit bereits existierender Email registriert | Fehlermeldung "Email bereits vorhanden" erscheint | ✅ PASS |
| 3 | Workout mit gültigen Daten (Running, 30min, 300cal) erfasst | Workout wird gespeichert und im Dashboard angezeigt | ✅ PASS |
| 4 | Mehrere Workouts erfassen | Werden aufgelistet | ✅ PASS |
| 5 | User mit 3 Workouts (30, 45, 60 Min) hat | Stats zeigen Total: 3, Duration: 135 Min, Avg: 45 Min | ✅ PASS |
| 6 | Weather API mit gültigem Key aufgerufen | Live-Wetter für Zürich wird korrekt angezeigt | ✅ PASS |
| 7 | Weather API mit ungültigem Key aufgerufen | Demo-Mode aktiviert, Fallback-Daten angezeigt | ✅ PASS |
| 8 | `docker-compose up -d` ausgeführt | Alle 5 Services (Frontend, User, Workout, Stats, Weather) laufen healthy | ✅ PASS |
| 9 | Aufrufen der Mobile Version  | Website Mobil erreichbar | ✅ PASS |
| 10 | App auf Mobile (375px) und Desktop (1920px) getestet | Layout passt sich responsive an, keine horizontalen Scrollbars | ✅ PASS |

**Test Summary:** 10/10 PASS ✅ | **Success Rate:** 100%

# 6. 📈 Ergebnisse & Reflexion

## 6.1 Erreichte Ziele

Das TrackMyGym Projekt hat alle ursprünglich definierten Ziele erreicht und sogar übertroffen:

🎯 Kernfunktionalitäten 100% erreicht
- ✅ Grundlegendes Tracking von Gym-Besuchen implementiert
- ✅ Einfache Erfassung von Übungen und Gewichten
- ✅ Individuelle Fortschrittsanzeige für jeden Nutzer
- ✅ Benutzerfreundliche GUI mit responsivem Design
- ✅ Benutzerprofilverwaltung vollständig funktional

🚀 Projekterweiterungen Bonus-Ziele erreicht:
- ✅ **PostgreSQL Migration** - Von JSON zu professioneller Datenbank
- ✅ **Weather API Integration** - Live-Wetter mit Workout-Empfehlungen - Externe API
- ✅ **AWS EC2 Deployment** - Cloud-native Lösung
- ✅ **CI/CD Pipeline** - Automatisierte Deployments
- ✅ **4 Microservices** - Skalierbare Architektur


## 6.2 Herausforderungen


Weather API
- **Problem:** Es hat ungewöhnlich lange gedauert, bis die richtigen Daten auf dem Dashboard zu sehen waren
- **Impact:** Ungewissheit ob die API tatsächlich funktioniert und Wartezeiten für die Tests
- ✅**Lösung:** 1 Tag warten

JSON-Storage

- **Problem:** Keine "Richtige" Datenbanklösung für meine Microservices.
- **Impact:** Erhebliches Risiko für die Datenintegrität, Datenkorruption möglich
- ✅**Lösung:** Migration von JSON-Storage auf richtige Datenbank

Cloud-Native Ansatz
- **Problem:** Projekt-Scope lokal -> App nicht auf der Cloud
- **Impact:** Keinen Zugriff aus dem Internet und keine automatischen Deployments via CI/CD Pipeline
- ✅**Lösung:** Projekterweiterung -> Absprache mit dem Dozenten, Projektweiterung visualisieren und Umsetzen. EC2 Instanz, Pipeline, Datenbank und externe API hinzugefügt.

## 6.3 Lessons Learned

🛠️​**Technisch:**

APIs: Immer Fallback-Strategien für externe Services.

PostgreSQL > JSON: Echte Datenbanken schützen vor Korruption


🔄**DevOps:**

CI/CD: Automatisierte Tests sparen Zeit und Nerven

AWS EC2: Einfacher als gedacht, aber Security beachten

Environment Variables: Secrets nie ins Git!


​📋​**Projektmanagement:**

Früh testen: User-Feedback wichtig

Scope Creep: Erweiterungen früh mit Stakeholdern besprechen. Speziell die Cloud-Native erweiterungen

Dokumentation: Balance zwischen zu viel und zu wenig

📐**UX/Design:**

Attraktive GUI: Touch-freundliche Interfaces sind wichtig

Error Handling: Demo Daten einsetzten

🥏**​Fazit:** Externe Dependencies brauchen Fallbacks, frühe Tests sparen später Stress, und echte Datenbanken sind es Wert! Secrets am richtigen Ort halten.

## 6.4 Ausblick

***Zukünftige Entwicklungen und Verbesserungsmöglichkeiten...***

- Feature Ausbau: Neue Community Features hinzufügen
- User-Access und Security: Kompatibilität für Passwörter / Login Credentials einbauen
- User Feedback Funktion: Direkt über die Applikation Feedbacks an die Entwickler senden
- FAQ-Section hinzufügen
- Friends-Lists und Gamification
- Option zur Anpassung des Farben-Themes
- Personalisierung: Profilbilder und Benutzernamen
- Motivierende Push-Notifications oder erinnerungen
- Special Seasonal Events
- **Cloud Native First!** Zukünftige Entwicklung in Cloud-Native-Philosophie beibehalten

---

# 7. 📚 Anhang

## 7.1 Code-Repository

https://github.com/gitlilia-tbz/ICTNE24_Semesterarbeit3_L.M

## 7.2 Verwendete Technologien

![Anthropic Claude](https://img.shields.io/badge/Anthropic-Claude-orange) - ![Claude Sonnet 4](https://img.shields.io/badge/Claude-Sonnet%204-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3.3-black?logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker&logoColor=white)
![AWS EC2](https://img.shields.io/badge/Deployed%20on-AWS%20EC2-orange?logo=amazon-aws&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-green?logo=github&logoColor=white)
![Weather API](https://img.shields.io/badge/Weather-OpenWeatherMap-blue?logo=openweathermap&logoColor=white)


Dieses Projekt wurde in Zusammenarbeit mit Anthropic Claude (Sonnet 4) erstellt.

## 7.3 Quellen


[![Claude](https://img.shields.io/badge/AI-Claude-orange?style=for-the-badge)](https://claude.ai)

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://python.org)

[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

[![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)

[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)

[![AWS EC2](https://img.shields.io/badge/AWS%20EC2-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/ec2/).

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com)

[![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-%23FF6B35.svg?style=for-the-badge&logo=openweathermap&logoColor=white)](https://openweathermap.org)

[![Scrum](https://img.shields.io/badge/Methodology-Scrum-blue?style=for-the-badge)](https://scrum.org)

[![Agile](https://img.shields.io/badge/Development-Agile-brightgreen?style=for-the-badge)](https://agilemanifesto.org)

[![SWOT Analysis](https://img.shields.io/badge/Analysis-SWOT-purple?style=for-the-badge)](https://en.wikipedia.org/wiki/SWOT_analysis)

[![Jira](https://img.shields.io/badge/jira-%230A0FFF.svg?style=for-the-badge&logo=jira&logoColor=white)](https://www.atlassian.com/software/jira)

## 7.4 Glossar

Definitionen wichtiger Begriffe:


## A

**ACID-Transactions** - Datenbank-Eigenschaften für Datenintegrität (Atomicity, Consistency, Isolation, Durability)

**Agile** - Iterative Entwicklungsmethodik mit kurzen Zyklen

**API** - Schnittstelle zwischen Software-Komponenten

**AWS EC2** - Amazon Cloud-Service für virtuelle Server

## B

**Bootstrap** - CSS-Framework für responsive Web-Design

## C

**CI/CD** - Automatisierte Pipeline für Code-Integration und Deployment

**Container** - Portable Softwarepaketierung mit allen Abhängigkeiten

**CRUD** - Grundoperationen: Create, Read, Update, Delete

## D

**Docker** - Containerisierungs-Plattform

**Docker Compose** - Tool für Multi-Container-Anwendungen

## E

**Environment Variables** - Externe Konfigurationswerte (API-Keys, etc.)

## F

**Flask** - Python-Web-Framework

**Foreign Key** - Datenbankfeld für Tabellen-Beziehungen

## G

**GitHub Actions** - CI/CD-Service von GitHub

**Graceful Degradation** - Weiterbetrieb bei Komponentenausfall

## H

**Health Check** - Automatische Service-Statusüberwachung

## J

**JSON** - Datenformat für strukturierten Datenaustausch

## K

**KanBan** - Visuelle Projektmanagement-Methode

## M

**Microservices** - Architektur mit unabhängigen, kleinen Services

**Migration** - Datenübertragung zwischen Systemen

## N

**Nginx** - Webserver und Reverse Proxy

## O

**OpenWeatherMap** - API-Service für Wetterdaten

**ORM** - Verknüpfung objektorientierter Programmierung mit Datenbanken

## P

**PostgreSQL** - Open-Source relationale Datenbank

**PWA** - Webanwendung mit nativen App-Funktionen

## R

**Rate Limiting** - Begrenzung von API-Anfragen pro Zeitraum

**REST** - Architekturstil für Web-APIs mit HTTP-Methoden

**Responsive Design** - Layout-Anpassung an verschiedene Bildschirmgrössen

## S

**Scrum** - Agiles Framework mit Sprints und festen Rollen

**SQLAlchemy** - Python-ORM-Library für Datenbankzugriff

**Sprint** - Zeitlich begrenzte Entwicklungsperiode (1-4 Wochen)

**SWOT** - Analyse von Stärken, Schwächen, Chancen, Risiken

## T

**Template** - HTML-Vorlage mit dynamischen Platzhaltern

**Toast-Notification** - Kurze Benutzerbenachrichtigung

## U

**UI/UX** - Benutzeroberfläche und Benutzererlebnis

**Usability** - Mass für Benutzerfreundlichkeit

## V

**Validation** - Überprüfung von Eingabedaten auf Korrektheit

## W

**Workflow** - Automatisierte Arbeitsschrittabfolge

## Y

**YAML** - Menschenlesbare Datenformat für Konfigurationsdateien

## 7.5 Kontaktangaben

Projektteam und Ansprechpartner zum Projekt:

***Lilia Mechani*** - 
Studierende

- Email: lilia.mechani@edu.tbz.ch

- Technische Berufsschule Zürich TBZ HF

- Aktuelle Verfügbarkeit des Repository: **Public**

---

Ich bedanke mich bei meinen Sport-begeisterten Test-Probanten, bei meiner Lerngemeinschaft und meinen Dozenten.

![Language Count](https://img.shields.io/github/languages/count/gitlilia-tbz/ICTNE24_Semesterarbeit3_L.M)
