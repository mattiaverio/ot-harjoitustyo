# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät voivat pelata shakkia toista pelaajaa vastaan samalla tietokoneella. Mahdollisesti myöhemmin voi pelata myös tietokonetta vastaan. Käyttäjätunnistautuminen tapahtuu käyttäjänimellä ilman salasanaa. Käyttäjillä on mahdollisuus lisätä profiiliinsa lyhyt kuvaus itsestään. Sovellus ylläpitää pelaajien ELO-rankingia pelattujen pelien perusteella.

## Käyttäjät

Sovelluksessa on yksi käyttäjärooli, normaali käyttäjä. Tyypillisesti sovellusta käyttää kaksi käyttäjää yhtä aikaa.

## Suunnitellut toiminnallisuudet

### Ennen pelin aloittamista

- Käyttäjä kirjautuu antamalla käyttäjänimen

### Kirjautuneena

- Käyttäjä voi aloittaa uuden shakkipelin
  - Toinen käyttäjä kirjautuu, jos kaksinpeli
  - Tietokonetta vastaan (mikäli aika riittää)

- Pelin aikana
  - Käyttäjä voi siirtää nappuloitaan
  - Käyttäjä voi luovuttaa tai ehdottaa tasapeliä
  - Peli etenee ja päättyy shakin sääntöjen mukaisesti

- Pelitulosten päivitys
  - Pelin päätyttyä pelaajien ELO päivitetään tuloksen perusteella

- Tulosten tarkastelu
  - Käyttäjä voi tarkastella omia ja muiden pelaajien ELO-ranking-arvoja
  - Käyttäjä voi nähdä pelihistorian, johon sisältyy pelitulokset

- Käyttäjä voi kirjautua ulos

## Jatkokehitysideoita

Peliä voisi jatkokehittää esimerkiksi seuraavilla toiminnallisuuksilla:

- Mahdollisuus pelata tietokonetta vastaan
- Pelien siirtohistorian tallennus ja selaaminen