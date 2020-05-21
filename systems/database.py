import subprocess
import os


def backup_table(table_name):
    with open("backups/{}-bkp.dmp".format(table_name), "wb") as file:
        subprocess.run(
            args=[
                "pg_dump",
                "-h",
                "ows-frontier.chjdqlnmmy9n.eu-central-1.rds.amazonaws.com",
                "-U",
                "postgres",
                "-d",
                "ows_db",
                "-t", table_name,
                "-a",
                "-Fc"
            ],
            stdout=file
        )


# pg_dump -h ows-frontier.chjdqlnmmy9n.eu-central-1.rds.amazonaws.com -U postgres -d ows_db -t fqdn_frontiers -a -f fqdn_frontiers-bkp.sql


def restore_table(table_name):
    with open("backups/{}-bkp.dmp".format(table_name), "r") as file:
        subprocess.run(
            args=[
                "pg_restore",
                "-h",
                "ows-frontier.chjdqlnmmy9n.eu-central-1.rds.amazonaws.com",
                "-U",
                "postgres",
                "-d",
                "ows_db",
                "-t",
                table_name,
            ],
            stdin=file
        )
