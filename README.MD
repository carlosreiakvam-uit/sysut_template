### Fremgangsmåte (foreløpig)

#### Last ned og installer mariadb
https://mariadb.org/download/?t=mariadb&p=mariadb&r=10.7.3&os=windows&cpu=x86_64&pkg=msi&m=dotsrc

#### i Terminal i pycharm:
pip install flask_sqlalchemy pymysql

#### kjør sysut_template
Kjør sysut_template og klikk på linken som peker til https://127.0.0.1:5000/

#### TODO:
- Sett opp script som oppretter database schema og gi den et navn
- Bruk navn på schema i app.py for å spesifisere lokasjon

#### Opprett database fra terminalen i pycharm:
flask create_db