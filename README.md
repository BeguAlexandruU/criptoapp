
# env

-- run in /cripto-app

source env/bin/activate


# run app

poetry run uvicorn api_data_drive.main:app --reload --host 0.0.0.0 --port 5001

ls
# Database

--important run comanda in /cripto_app

1. init alembic, run only on initializaton
    ```
    poetry run alembic init [migrations/alembic]
    ```
    
    1.1 config file alembic.ini
        change line 63
        sqlalchemy.url = mysql+pymysql://%(MYSQL_USER)s:%(MYSQL_PASSWORD)s@%(MYSQL_HOST)s:%(MYSQL_PORT)s/%(MYSQL_DATABASE)s

    1.2 config file env.py on migrations folder
        - imports 
            from cripto_app.settings import mysql_db, mysql_host, mysql_password, mysql_port, mysql_user
            from cripto_app.db.models import metadata
        - code after config variable declaration
            section = config.config_ini_section
            config.set_section_option(section, 'MYSQL_USER', mysql_user)
            config.set_section_option(section, 'MYSQL_PASSWORD', mysql_password)
            config.set_section_option(section, 'MYSQL_HOST', mysql_host)
            config.set_section_option(section, 'MYSQL_PORT', mysql_port)
            config.set_section_option(section, 'MYSQL_DATABASE', mysql_db)
        - line 33
            target_metadata = metadata

//after update
2. poetry run alembic revision --autogenerate -m 'migration name'

3. poetry run alembic upgrade head[/id last revision]

--secondary
4. poetry run alembic downgrade id_lasr_revisino
5. poetry run alembic history //the rest on alembic.com
