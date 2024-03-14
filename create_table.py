from test import Database

def table():
    phone_table = f"""
        CREATE TABLE phone(
        phone_id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        create_date TIMESTAMP DEFAULT now());
    """

    noutbook_table = f"""
        CREATE TABLE noutbook(
        menu_id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        create_date TIMESTAMP DEFAULT now());
    """

    data = {
        "phone_table": phone_table,
        "noutbook_table": noutbook_table
    }

    for i in data:
        print(f"{i} - {Database.connect(data[i], "insert")}")

if __name__ == "__main__":
    table()