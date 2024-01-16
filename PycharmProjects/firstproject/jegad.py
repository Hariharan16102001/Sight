import pyodbc
import re

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

def get_all_values_for_column(table_name, column_name, conn):
    cursor = conn.cursor()
    query = f"SELECT [{column_name}] FROM {table_name}"
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
def fetch_specific_info(table_name, conn, user_input,column_names_fashiontest,column_values_dict):
    cursor = conn.cursor()

    words = user_input.lower().split()
    columns = []
    conditions = []
    conjunctions = ['and', 'with', 'for', 'of']

    for idx, word in enumerate(words):
        if word in map(str.lower, column_names_fashiontest):
            columns.append(word)
        elif word not in conjunctions:
            conditions.append(f"{columns[-1]} = '{word}'")
        else:
            split_word = word.split('=')
            if len(split_word) == 2:
                key = split_word[0].strip()
                value = split_word[1].strip("'")
                conditions.append(f"{key} = '{value}'")

    if columns and conditions:
        print("Requested details:")
        query = f"SELECT {', '.join(columns)} FROM {table_name} WHERE {' AND '.join(conditions)}"
        cursor.execute(query)
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)

        else:
            print("No matching records found.")
    else:
        print("Please provide a valid request with specific details.")

    if columns and not conditions:
        # Fetch the specified column
        column_to_fetch = columns[0]
        column_values = column_values_dict.get(column_to_fetch)
        if column_values:
            print(f"All values in column {column_to_fetch}:")
            for value in column_values:
                print(value)
        else:
            print(f"No valid input found: {column_to_fetch}")

    if conditions and not columns:
        # Retrieve the entire row matching the value in the specified column
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
        # print("Please provide a valid request with specific details.")
        pass

# def fetch_specific_info_ordertest(table_name, conn, user_input):
#     cursor = conn.cursor()
#
#     words = user_input.lower().split()
#     columns = []
#     conditions = []
#     conjunctions = ['and', 'with', 'for', 'of']
#
#     for idx, word in enumerate(words):
#         if word in map(str.lower, column_names_ordertest):
#             columns.append(word)
#         elif word not in conjunctions:
#             conditions.append(f"{columns[-1]} = '{word}'")
#         else:
#             split_word = word.split('=')
#             if len(split_word) == 2:
#                 key = split_word[0].strip()
#                 value = split_word[1].strip("'")
#                 conditions.append(f"{key} = '{value}'")
#
#     if columns and conditions:
#         print("Requested details from ordertest:")
#         query = f"SELECT {', '.join(columns)} FROM {table_name} WHERE {' AND '.join(conditions)}"
#         cursor.execute(query)
#         rows = cursor.fetchall()
#
#         if rows:
#             for row in rows:
#                 print(row)
#         else:
#             print("No matching records found in ordertest.")
#     else:
#         print("Please provide a valid request with specific details for ordertest.")


if __name__ == "__main__":
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-S0QIC03\\MYPROJECT;'
                          'Database=Test;'
                          'Trusted_Connection=yes;')

    table_name_fashiontest = 'fashiontest'
    column_values_dict_fashiontest = get_columns_and_values(table_name_fashiontest, conn)
    column_names_fashiontest = list(column_values_dict_fashiontest.keys())

    # table_name_ordertest = 'ordertest'
    # column_values_dict_ordertest = get_columns_and_values(table_name_ordertest, conn)
    # column_names_ordertest = list(column_values_dict_ordertest.keys())

    while True:
        user_input = input("Enter your statement (or 'exit' to stop): ")

        if user_input.lower() == 'exit':
            break

        selected_columns = []
        selected_values = []


        user_input_lower = user_input.lower()
        input_words = user_input_lower.split()

        for word in input_words:
            if word in map(str.lower, column_names_fashiontest):
                selected_columns.append(word)
                for new in input_words:
                    if word in map(str.lower, column_values_dict_fashiontest):
                        selected_values.append(new)

        for word in input_words:
            if word in map(str.lower, column_names_fashiontest):
                selected_columns.append(word)
            else:
                selected_values.append(word)


        if not selected_columns and selected_values:
            user_value = ' '.join(selected_values)
            for column_name in column_names_fashiontest:
                rows = fetch_rows_for_values(table_name_fashiontest, conn, column_name, user_value)
                if rows:
                    print(f"Rows for '{column_name}' with value '{user_value}' in fashiontest:")
                    for row in rows:
                        print(row)

        elif selected_columns and not selected_values:
            for user_column in selected_columns:
                column_values = get_all_values_for_column(table_name_fashiontest, user_column, conn)
                print(f"All values in column {user_column} in fashiontest:")
                for row in column_values:
                    print(row[0])

        elif selected_columns and selected_values:
            for user_column in selected_columns:
                for user_value in selected_values:
                    rows = fetch_rows_for_values(table_name_fashiontest, conn, user_column, user_value)
                    if rows:
                        print(f"Rows for '{user_column}' with value '{user_value}' in fashiontest:")
                        for row in rows:
                            print(row)

        else:
            print(f"No valid input found for fashiontest: {user_input}")

        fetch_specific_info(table_name, conn, user_input, column_names_fashiontest, column_values_dict)

        # fetch_specific_info_ordertest(table_name_ordertest, conn, user_input)


    conn.close()