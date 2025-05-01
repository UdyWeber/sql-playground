from db import aquire_connection, clean_db, create_default_tables, generate_seed_data


def main():
    conn = aquire_connection()

    clean_db(conn)
    create_default_tables(conn)
    generate_seed_data(conn)

    conn.close()


if __name__ == "__main__":
    main()
