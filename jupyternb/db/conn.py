import pandas as pd


def conn_pg(db):
    from psycopg2 import connect

    try:
        print("Connecting to Postgres...")
        dbname = db
        user = "filip"
        host = ""
        port = "5432"
        password = ""
        pg_conn = connect(dbname=dbname, user=user, host=host, port=port, password=password)

        print("Connected to Postgres!")

    except Exception as e:
        pg_conn = None
        raise ValueError(e)

    return pg_conn


def get_pandas_athena(query):
    from pyathena import connect

    conn = connect(s3_staging_dir="s3://project/folder/", region_name="ap-southeast-1")
    df = pd.read_sql_query(
        query,
        conn,
    )

    return df


def get_pandas_bq(query):
    from google.cloud import bigquery

    CREDS = "file.json"
    client = bigquery.Client.from_service_account_json(json_credentials_path=CREDS)
    job = client.query(query)
    df = job.to_dataframe()
    return df


def get_pandas_pg(query, db):
    conn = conn_pg(db)
    cursor = conn.cursor()
    # Execute the query
    cursor.execute(query)

    # Fetch the results of the query
    results = cursor.fetchall()

    # Convert the results to a DataFrame
    df = pd.DataFrame(results)
    df.columns = [column[0] for column in cursor.description]

    return df
