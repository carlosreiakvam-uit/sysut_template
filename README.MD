## Fremgangsmåte (foreløpig)

#### Last ned og installer pycharm

https://www.jetbrains.com/pycharm/download/#section=windows

Registrer deg med uit-epost og be til gudene om at du har fått gratis tilgang

#### Last ned og installer mariadb

https://mariadb.org/download/?t=mariadb&p=mariadb&r=10.7.3&os=windows&cpu=x86_64&pkg=msi&m=dotsrc

#### Oppdater personlig info fra MariaDB

I db_user_info.py: 

endre username og password til det du valgte under installasjoenen av mariaDB.  

Username er root om du ikke har endret dette.

NB: Når du commiter filer til prosjektet: Ikke legg ved din personal_db_user.py

#### Installer requirements

Installer requirements med pip ved hjelp av requirements.txt

#### Kjør sysut_template

Kjør sysut_template ved å klikke på den grønne pilen oppe til høyre i Pycharm.

Du får da opp en link som peker til https://127.0.0.1:5000/

Klikk på linken og verifiser at du får opp "Hello Munchies" i nettleseren din

#### Oppdater database med kolonen "Users" fra terminalen i pycharm:

```flask create_db```