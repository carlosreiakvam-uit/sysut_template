### Fremgangsmåte (foreløpig)

### Last ned og installer pycharm

https://www.jetbrains.com/pycharm/download/#section=windows

Registrer deg med uit-epost og be til gudene om at du har fått gratis tilgang

#### Last ned og installer mariadb

https://mariadb.org/download/?t=mariadb&p=mariadb&r=10.7.3&os=windows&cpu=x86_64&pkg=msi&m=dotsrc

#### Endre til ditt brukernavn og passord i mariaDB

I personal_db_user.py endre username og password til det du valgte under installasjon av mariaDB.  
Username er root om du ikke har endret dette.

NB: Når du commiter filer til prosjektet: Ikke legg ved din personal_db_user.py 

#### Installer requirements 

Installer med pip ved hjelp av requirements.txt

#### Kjør sysut_template

Kjør sysut_template og klikk på linken som peker til https://127.0.0.1:5000/

#### Opprett database fra terminalen i pycharm:

```flask create_db```

#### TODO:

- Sett opp script som oppretter database schema og gi den et navn
- Foreløpig prøver app.py å koble opp mot databasenavnet kongle_db som er en prøvedatabase jeg lagde
- Bruk navn på schema i app.py for å spesifisere lokasjon
