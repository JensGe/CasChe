import psycopg2

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "UPG6qFAxJ8VPkQIfiRDf",
                                  host = "ows-frontier.chjdqlnmmy9n.eu-central-1.rds.amazonaws.com",
                                  port = "5432",
                                  database = "ows_db")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters())

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print("Error while connecting to PostgreSQL" + error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")