import pyodbc
from datetime import datetime

def get_column_names(table_name, conn):
    cursor = conn.cursor()
    cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'")
    columns = [row.COLUMN_NAME for row in cursor.fetchall()]
    return columns


def get_all_values_for_columns(table_name, conn):
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


def get_columns_and_values(table_name, conn):
    columns = get_column_names(table_name, conn)
    values = get_all_values_for_columns(table_name, conn)
    column_values_dict = {column: [] for column in columns}

    for row in values:
        for idx, value in enumerate(row):
            column_values_dict[columns[idx]].append(value)

    return column_values_dict


def fetch_rows_for_values(table_name, conn, user_column, user_value):
    cursor = conn.cursor()

    valid_columns = get_column_names(table_name, conn)
    if user_column not in valid_columns:
        print(f"'{user_column}' is not a valid column name.")
        return []

    query = f"SELECT * FROM {table_name} WHERE [{user_column}] = ?"

    try:
        cursor.execute(query, user_value)
    except Exception as ex:
        print(ex)
        return []

    rows = cursor.fetchall()
    return rows



def handle_product_discovery(conn, table_name, column_names, column_values_dict):
    while True:
        user_input = input("Enter your statement (or 'exit' to stop): ")

        if user_input.lower() == 'exit':
            break




        words = user_input.lower().split()
        columns = []
        conditions = []
        values = []
        conjunctions = ['give','me','the', 'and', 'with', 'for', 'of', 'i', 'need', 'want', 'deatils', 'informations']

        if 'date_range' in user_input.lower():
            if 'date' in map(str.lower, column_names):
                cursor = conn.cursor()
                try:
                    start_date_input = input("Enter start date in 'YYYY-MM-DD' format: ")
                    end_date_input = input("Enter end date in 'YYYY-MM-DD' format: ")

                    start_date = datetime.strptime(start_date_input, '%Y-%m-%d').date()
                    end_date = datetime.strptime(end_date_input, '%Y-%m-%d').date()

                    condition = f"date >= '{start_date}' AND date <= '{end_date}'"
                    query = f"SELECT * FROM {table_name} WHERE {condition}"

                    cursor.execute(query)
                    rows = cursor.fetchall()

                    if rows:
                        for row in rows:
                            print(row)
                    else:
                        print("No records found within the specified date range.")

                except ValueError:
                    print("Invalid date format. Please enter dates in 'YYYY-MM-DD' format.")
                except Exception as ex:
                    print("An error occurred:", ex)

            else:
                print("No 'date' column found in the table.")

        for idx, word in enumerate(words):
            if word in map(str.lower, column_names):
                columns.append(word)
            if word in map(str.lower,column_values_dict):
                values.append(word)
            elif word not in conjunctions:
                conditions.append(f"{columns[-1]} = '{word}'")
                values.append(word)
            else:
                split_word = word.split('=')
                if len(split_word) == 2:
                    key = split_word[0].strip()
                    value = split_word[1].strip("'")
                    conditions.append(f"{key} = '{value}'")

        if columns and conditions and values:
            quer = f"SELECT * FROM {table_name} WHERE {' AND '.join(conditions)}"
            cursor = conn.cursor()
            cursor.execute(quer)
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("No matching records found.")


        if columns and conditions:
            query = f"SELECT {', '.join(columns)} FROM {table_name} WHERE {' AND '.join(conditions)}"
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

            if rows:
                for row in rows:
                    print(row)
            else:
                print("No matching records found.")

        if columns and not conditions:
            column_to_fetch = columns[0]
            column_values = column_values_dict.get(column_to_fetch)
            if column_values:
                print(f"All values in column {column_to_fetch}:")
                for value in column_values:
                    print(value)
            else:
                print(f"No valid input found: {column_to_fetch}")

        if conditions and not columns:
            condition_column = conditions[0].split(' = ')[0]
            condition_value = conditions[0].split(' = ')[1].strip("'")
            rows = fetch_rows_for_values(table_name, conn, condition_column, condition_value)

            if rows:
                print(f"Rows where {condition_column} = {condition_value}:")
                for row in rows:
                    print(row)
            else:
                print(f"No matching records found for {condition_column} = {condition_value}")

        else:
            pass



if __name__ == "__main__":
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-S0QIC03\\MYPROJECT;'
                              'Database=Test;'
                              'Trusted_Connection=yes;')

        table_name = 'ordertest'
        column_values_dict = get_columns_and_values(table_name, conn)
        column_names = list(column_values_dict.keys())

        handle_product_discovery(conn, table_name, column_names, column_values_dict)

        conn.close()

    except Exception as e:
        print("ended")
