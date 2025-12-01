## Pakkauskaavio
Ohjelman yleinen rakenne.

```mermaid
flowchart TD
    %% UI Layer
    UI[UI Package]

    %% Service Layer
    Services[Services Package]

    %% Repository Layer
    Repositories[Repositories Package]

    %% Entities
    Entities[Entities Package]

    %% Connections
    UI --> Services
    Services --> Repositories
    Services --> Entities
    Repositories --> Entities
```

## Tämän hetken luokkakaavio
En ole vielä päättänyt miten toteutan pelihistorian.

```mermaid
classDiagram
    UI --> MenuPage
    UI --> GamePage
    UI --> RatingPage
    
    UI --> UserService
    UI --> GameService

    GamePage --> ChessGame

    UserService --> UserRepository
    GameService --> UserRepository

    UserRepository ..> User
```

## Voittavan siirron sekvenssikaavio
Tämä kuvaa voittavaa siirtoa, jolloin peli päättyy ja pelaajien ELO-rating päivitetään.

```mermaid
sequenceDiagram
    actor Kayttaja
    participant UI as GamePage
    participant Service as GameService
    participant Repo as UserRepository

    Kayttaja->>UI: Tekee voittavan siirron
    activate UI
    
    UI->>Service: record_game_result(white, black, "1-0")
    activate Service
    
    Service->>Repo: update_elo(white)
    activate Repo
    Repo-->>Service: (tallennettu)
    deactivate Repo

    Service->>Repo: update_elo(black)
    activate Repo
    Repo-->>Service: (tallennettu)
    deactivate Repo

    Service-->>UI: return
    deactivate Service

    UI-->>Kayttaja: Näyttää "Game Over" -ilmoituksen
    deactivate UI
```