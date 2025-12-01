# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät voivat pelata shakkia toista pelaajaa vastaan samalla tietokoneella. Mahdollisesti myöhemmin voi pelata myös tietokonetta vastaan. Käyttäjätunnistautuminen tapahtuu käyttäjänimellä ilman salasanaa. Käyttäjillä on mahdollisuus lisätä profiiliinsa lyhyt kuvaus itsestään. Sovellus ylläpitää pelaajien ELO-rankingia pelattujen pelien perusteella.

## Käyttäjät

Sovelluksessa on yksi käyttäjärooli, normaali käyttäjä. Tyypillisesti sovellusta käyttää kaksi käyttäjää yhtä aikaa.

## Suunnitellut toiminnallisuudet

### Ennen pelin aloittamista

- &#9745; Käyttäjä kirjautuu antamalla käyttäjänimen

### Kirjautuneena

- &#9745; Käyttäjä voi aloittaa uuden shakkipelin 
  - &#9745; Toinen käyttäjä kirjautuu, jos kaksinpeli
  - Tietokonetta vastaan (mikäli aika riittää)

- Pelin aikana
  - &#9745; Käyttäjä voi siirtää nappuloitaan
  - Käyttäjä voi luovuttaa tai ehdottaa tasapeliä
  - &#9745; Peli etenee ja päättyy shakin sääntöjen mukaisesti

- Pelitulosten päivitys
  - &#9745; Pelin päätyttyä pelaajien ELO päivitetään tuloksen perusteella

- Tulosten tarkastelu
  - &#9745; Käyttäjä voi tarkastella omia ja muiden pelaajien ELO-ranking-arvoja
  - Käyttäjä voi nähdä pelihistorian, johon sisältyy pelitulokset

## Jatkokehitysideoita

Peliä voisi jatkokehittää esimerkiksi seuraavilla toiminnallisuuksilla:

- Mahdollisuus pelata tietokonetta vastaan
- Pelien siirtohistorian tallennus ja selaaminen