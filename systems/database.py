import subprocess
import os


def backup_table(table_name):
    if not os.path.exists("fetsim-logs"):
        os.makedirs("fetsim-logs")
    with open("fetsim-logs/db_{}_bkp.dmp".format(table_name), "wb") as file:
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


def restore_table(table_name):
    with open("fetsim-logs/db_{}_bkp.dmp".format(table_name), "r") as file:
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
