# Sprint 2 – Planung & Review

## Zeitraum

9.5. - 2.6.25

## Sprintziel

1. Wechsel / Migration des KanBan-Board
2. Start Entwicklung der Grundarchitektur
3. GUI Planung und erste Umsetzung

## User Stories mit Akzeptanzkriterien

## User Story 2:


| Title:                              | Priority: | Estimate: |
| ------------------------------------- | ----------- | ----------- |
| Wechsel / Migraton des KanBan Board | High      | 1h        |

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

```mermaid
graph TB
    %% Define the main container
    subgraph LocalMachine["Local Machine"]
        subgraph DockerEngine["Docker Engine"]
            subgraph DockerNetwork["Docker Network: fitness-network<br/>172.20.0.0/16"]
                
                %% Load Balancer Layer
                subgraph LoadBalancer["Load Balancer"]
                    Nginx["Nginx<br/>172.20.0.2<br/>Port 80"]
                end
                
                %% Application Services Layer
                subgraph ApplicationServices["Application Services"]
                    Frontend["Frontend Service<br/>172.20.0.3<br/>Port 5000"]
                    UserService["User Service<br/>172.20.0.4<br/>Port 5001"]
                    WorkoutService["Workout Service<br/>172.20.0.5<br/>Port 5002"]
                    StatsService["Stats Service<br/>172.20.0.6<br/>Port 5003"]
                end
                
                %% Data Storage Layer
                subgraph DataStorage["Data Storage"]
                    UserVolume["User Data Volume<br/>172.20.0.7<br/>JSON Storage"]
                    WorkoutVolume["Workout Data Volume<br/>172.20.0.8<br/>JSON Storage"]
                    StatsVolume["Stats Data Volume<br/>172.20.0.9<br/>JSON Storage"]
                end
                
            end
        end
    end
    
    %% External User
    User["User Browser<br/>External<br/>Port 80"]
    
    %% Connections
    User --> Nginx
    Nginx --> Frontend
    Nginx --> UserService
    Nginx --> WorkoutService
    Nginx --> StatsService
    
    Frontend -.-> UserService
    Frontend -.-> WorkoutService
    Frontend -.-> StatsService
    
    WorkoutService -.-> UserService
    StatsService -.-> WorkoutService

    UserService --> UserVolume
    WorkoutService --> WorkoutVolume
    StatsService --> StatsVolume

    %% Styling to match the provided example
    classDef containerStyle fill:#4a4a4a,stroke:#666,stroke-width:2px,color:#fff
    classDef loadBalancerGroup fill:#e8f4fd,stroke:#1976d2,stroke-width:2px
    classDef serviceGroup fill:#f0f8e8,stroke:#388e3c,stroke-width:2px
    classDef dataGroup fill:#fef7e0,stroke:#f57c00,stroke-width:2px
    classDef userNode fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#000
    classDef serviceNode fill:#2d2d2d,stroke:#555,stroke-width:2px,color:#fff
    classDef dataNode fill:#2d2d2d,stroke:#555,stroke-width:2px,color:#fff

    %% Apply styles
    class LocalMachine,DockerEngine,DockerNetwork containerStyle
    class LoadBalancer loadBalancerGroup
    class ApplicationServices serviceGroup
    class DataStorage dataGroup
    class User userNode
    class Nginx,Frontend,UserService,WorkoutService,StatsService serviceNode
    class UserVolume,WorkoutVolume,StatsVolume dataNode
```

### Herausforderungen

- Microsoft Lists bietet nicht alle benötigten Funktionen an. Es wurde am Anfang des 2. Sprints eine Ausweichmöglichkeit definiert
- Sprint 1 Zeitraum sehr klein

### Lessons Learned

- Mehr Austausch mit den Team-Kollegen und Collaboraters pflegen, um Lösungen zu vergleichen und voneinander zu profitieren. Durch einen Tipp von Teamkollegen, bin ich vollständig auf Visual-Studio gewechselt, da es wesentlich mehr Möglichkeiten anbietet, als Obsidian.

## Ausblick auf Sprint 3

- Wechsel / Migration des KanBan-Board
- Start Entwicklung der Grundarchitektur
- GUI Planung und erste Umsetzung
