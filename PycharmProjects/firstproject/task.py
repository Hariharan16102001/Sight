import pyodbc


# Function to get column names and values from a table
def get_columns_and_values(table_name, conn):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    columns = [column[0] for column in cursor.description]

    column_values_dict = {}
    for col in columns:
        cursor.execute(f"SELECT {col} FROM {table_name}")
        values = [row[0] for row in cursor.fetchall()]
        column_values_dict[col] = values

    return column_values_dict

# Function to fetch all values for a given column
def get_all_values_for_column(table_name, column_name, conn):
    cursor = conn.cursor()
    cursor.execute(f"SELECT {column_name} FROM {table_name}")
    return cursor.fetchall()


# Function to fetch rows for a given column and value
def fetch_rows_for_values(table_name, conn, column_name, value):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name} WHERE {column_name} = ?", value)
    return cursor.fetchall()


if __name__ == "__main__":
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-S0QIC03\\MYPROJECT;'
                          'Database=Test;'
                          'Trusted_Connection=yes;')

    table_name = 'fashiontest'
    column_values_dict = get_columns_and_values(table_name, conn)
    column_names = list(column_values_dict.keys())

    while True:
        user_input = input("Enter your statement (or 'exit' to stop): ")

        if user_input.lower() == 'exit':
            break

        selected_columns = []
        selected_values = []

        # Extracting column names and values from user input
        user_input_lower = user_input.lower()
        input_words = user_input_lower.split()

        for word in input_words:
            if word in map(str.lower, column_names):
                selected_columns.append(word)
                for new in input_words:
                    if new in map(str.lower, column_values_dict):
                        selected_values.append(new)

        if  selected_columns and selected_values:
            user_value = ' '.join(selected_values)
            for column_name in column_names:
                rows = fetch_rows_for_values(table_name, conn, column_name, user_value)
                if rows:
                    print(f"Rows for '{column_name}' with value '{user_value}':")
                    for row in rows:
                        print(row)

        elif selected_columns and not selected_values:
            for user_column in selected_columns:
                column_values = column_values_dict[user_column]
                print(f"All values in column {user_column}:")
                for val in column_values:
                    print(val)

    conn.close()
