
# docker

Connect to app environment  
-- run in /cripto-app

```
sudo systemctl status docker
```
```
sudo systemctl start docker
```

# env

Connect to app environment  
-- run in /cripto-app ?? /back

```
source env/bin/activate
```

Exit from app environment  
-- run in (env)

```
deactivate
```

# run app(restapi)

-- run comanda in /cripto-app (env)

```
poetry run uvicorn cripto_app.main:app --reload --host 0.0.0.0 --port 5001
```

# Database
## DB design
https://drawsql.app/teams/indigital/diagrams/criptoapp

## init database
-- run comanda in /cripto_app

1.  init alembic, run only on initializaton  
    ```
    poetry run alembic init [migrations/alembic]
    ```

2. config file alembic.ini   

    - change line 63  

    ```
    sqlalchemy.url = mysql+pymysql://%(MYSQL_USER)s:%(MYSQL_PASSWORD)s@%(MYSQL_HOST)s:%(MYSQL_PORT)s/%(MYSQL_DATABASE)s
    ```

3. config file env.py on migrations folder  
    - add imports   

        ```
        from cripto_app.settings import mysql_db, mysql_host, mysql_password, mysql_port, mysql_user
        from cripto_app.db.models import metadata
        ```

    - code after config variable declaration

        ```
        section = config.config_ini_section
        config.set_section_option(section, 'MYSQL_USER', mysql_user)
        config.set_section_option(section, 'MYSQL_PASSWORD', mysql_password)
        config.set_section_option(section, 'MYSQL_HOST', mysql_host)
        config.set_section_option(section, 'MYSQL_PORT', mysql_port)
        config.set_section_option(section, 'MYSQL_DATABASE', mysql_db)
        ```

    - change on line 33
        ```
        target_metadata = metadata
        ```

## Update database

### Before run update

### Before run update
1. Drop all tables in db
2. Clear folder /alembic/versions
3. Delete file __pycache__ in alembic folder

### After update (code update)
-- run comanda in /cripto_app

1. Generate new migration
    ```
    poetry run alembic revision --autogenerate -m 'migration name'
    ```
2. Unpack and implement new migration version
    ```
    poetry run alembic upgrade head[/id last revision]
    ```

## Secondary
1.   
    ```
    poetry run alembic downgrade id_lasr_revisino
    ```
2.   
    ```
    poetry run alembic history //the rest on alembic.com
    
    ```

## Deploy production

1. 
    - Stop stack back-compose 
    ```
        cd ~/docker/composes/
        docker compose -f back-compose.yml down
    ```

2. 
    - Update image backend
    ```
        cd ~/app/criptoapp/
        bash update_back_img.sh
    ```

3. 
    - Stop stack back-compose 
    ```
        cd ~/docker/composes/
        docker compose -f back-compose.yml up -d
    ```
