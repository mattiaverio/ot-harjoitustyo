# OT-Chess

Tämä on ohjelmistotekniikan harjoitustyö, jossa toteutan **shakkipelin**. Peliä voi pelata kahden, ehkä jotain kirjastoa vastaan ja se voisi pitää pelaajanimien perusteella jotain *ELO ratingia* tietokannassa.

## Dokumentaatio

[Vaatimusmäärittely](./dokumentaatio/vaatimusmäärittely.md)
[Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
[Changelog](./dokumentaatio/changelog.md)
[Kielimalliselvitys](./dokumentaatio/kielimalliselvitys.md)
[Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
**[Ylimääräinen koodikatselmointi](https://github.com/Victheliar/Aineopintojen-harjoitusty-Ohjelmistotekniikka/issues/1)**


## Asennus

1. Asenna riippuvuudet:

```bash
poetry install
```

2. Alusta tietokanta:

```bash
poetry run invoke db-init
```

3. Käynnistä sovellus:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

Testien suorittaminen:

```bash
poetry run invoke test
```

Testikattavuusraportin generointi:

```bash
poetry run invoke coverage-report
```

Pylint:

```bash
poetry run invoke lint
```