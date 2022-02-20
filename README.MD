### Fremgangsmåte (foreløpig)

#### Last ned og installer mariadb

https://mariadb.org/download/?t=mariadb&p=mariadb&r=10.7.3&os=windows&cpu=x86_64&pkg=msi&m=dotsrc

#### Endre til ditt brukernavn og passord i mariaDB

I app.py, skriv om linje 7 fra
```app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tresko@localhost/kongle_db'```

Skriv om til ditt oppsett
```mysql+pymysql://username:password@localhost/db_name```

#### i Terminal i pycharm:

```pip install flask, flask_sqlalchemy pymysql```

#### kjør sysut_template

Kjør sysut_template og klikk på linken som peker til https://127.0.0.1:5000/

#### Opprett database fra terminalen i pycharm:

```flask create_db```

#### TODO:

- Sett opp script som oppretter database schema og gi den et navn
- Foreløpig prøver app.py å koble opp mot databasenavnet kongle_db som er en prøvedatabase jeg lagde
- Bruk navn på schema i app.py for å spesifisere lokasjon
