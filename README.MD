## Fremgangsmåte for å kjøre prosjekt lokalt (foreløpig)



#### Last ned og installer pycharm

https://www.jetbrains.com/pycharm/download/#section=windows

Registrer deg med uit-epost og be til gudene om at du har fått gratis tilgang

#### Last ned og installer mariadb

https://mariadb.org/download/?t=mariadb&p=mariadb&r=10.7.3&os=windows&cpu=x86_64&pkg=msi&m=dotsrc

Velg passord "munchies"  
![mariaDB_install_1](https://user-images.githubusercontent.com/98937880/154868769-7f317a29-1109-45bd-a5e2-23c48ac878d3.png)

Behold alt som default her  
![mariaDB_install_2](https://user-images.githubusercontent.com/98937880/154868776-a0fa6d99-c317-4a4d-8d16-9dbc74a318ad.png)

#### Installer requirements

Installer requirements med pip ved hjelp av requirements.txt

#### Opprett database

Opprett databasen ved å kjøre local_db_create.py



#### Koble til database i pycharm
I Database helt til høyre i pycharm, trykk på plusstegnet og velg Data Source -> MariaDB

![image](https://user-images.githubusercontent.com/98937880/155078882-e6703b48-cc59-4e17-9a93-0ed4974cf2a3.png)

Brukernavn: Root
Passord: Munchies
Database: Se etter DB_NAME i local_db_create.py

![image](https://user-images.githubusercontent.com/98937880/155079370-15fb5189-1e55-45c5-8c3e-b7b6c31de745.png)


#### Oppdater database med verdier

Oppdater databasen med siste verdier ved å kjøre local_db_update.py

Trykk på refresh tegnet for få inn de siste endringene i pycharm
![image](https://user-images.githubusercontent.com/98937880/155079077-c04face6-e9b9-4d25-bfec-95b26865c1af.png)



#### Kjør sysut_template

Kjør sysut_template ved å klikke på den grønne pilen oppe til høyre i Pycharm.

Du får da opp en link som peker til 127.0.0.1:5000/

Klikk på linken og verifiser at du får opp "Hello Munchies" i nettleseren din


#### Kilder
https://flask-sqlalchemy.palletsprojects.com/en/2.x/ 

https://www.mariadbtutorial.com/

https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications

https://docs.sqlalchemy.org/en/14/dialects/mysql.html

https://stackoverflow.com/questions/43713124/creating-a-database-in-flask-sqlalchemy
