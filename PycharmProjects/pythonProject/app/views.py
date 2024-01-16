from flask import Flask, render_template, request
import pyodbc
from datetime import datetime

# app = Flask(__name__)
app = Flask(__name__, template_folder='templates', static_folder='static')


# Database-related functions
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


# Route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html', rows=None, column_names=None)


@app.route('/search', methods=['POST'])
def search():
    rows = None
    column_names = None

    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-S0QIC03\\MYPROJECT;'
                              'Database=Test;'
                              'Trusted_Connection=yes;')

        table_name = 'ordertest'

        column_values_dict = get_columns_and_values(table_name, conn)
        column_names = list(column_values_dict.keys())

        user_input = request.form['user_input']  # Get user input from form
        # if rows:
        #     # Instead of printing, assign 'rows' to the 'data' variable in render_template
        #     return render_template('results.html', data=rows)  # Here, 'data=rows' passes the 'rows' to the template
        words = user_input.lower().split()
        columns = []
        conditions = []
        values = []
        conjunctions = ['give', 'me', 'the', 'and', 'with', 'for', 'of', 'i', 'need', 'want', 'deatils', 'informations',
                        'and', 'or', 'but', 'yet', 'for', 'nor', 'so', 'although', 'because', 'since', 'while',
                        'after', 'before', 'once', 'since', 'until', 'when', 'whenever', 'whereas', 'wherever',
                        'though', 'whether', 'even', 'if', 'unless', 'however', 'therefore', 'moreover', 'furthermore',
                        'meanwhile', 'nonetheless', 'besides', 'hence', 'thus', 'henceforth', 'thusly', 'consequently',
                        'accordingly', 'otherwise', 'finally', 'additionally', 'similarly', 'indeed', 'subsequently',
                        'nevertheless', 'yet', 'regardless', 'hitherto', 'conversely', 'instead', 'moreover',
                        'hence', 'meanwhile', 'further', 'otherwise', 'consequently', 'thus', 'otherwise', 'still',
                        'therefore', 'furthermore', 'moreover', 'but', 'however', 'while', 'although', 'though',
                        'unless',
                        'notwithstanding', 'yet', 'besides', 'indeed', 'hence', 'thus', 'conversely', 'likewise',
                        'thereupon', 'yet', 'still', 'then', 'further', 'finally', 'therefore', 'accordingly',
                        'consequently', 'in addition', 'plus', 'moreover', 'likewise', 'similarly', 'as well as',
                        'with', 'for', 'and', 'nor', 'but', 'or', 'yet', 'so', 'after', 'although', 'as', 'as if',
                        'as long as', 'because', 'before', 'even if', 'even though', 'if', 'in order that',
                        'provided that', 'since', 'so that', 'than', 'that', 'though', 'till', 'unless', 'until',
                        'when', 'whenever', 'where', 'whereas', 'wherever', 'whether', 'while', 'though', 'what',
                        'whatever', 'which', 'whichever', 'who', 'whoever', 'whom', 'whomever', 'whose', 'how',
                        'fetch', 'retrieve', 'return', 'show', 'display', 'list', 'give', 'provide', 'present',
                        'print', 'output', 'produce', 'render', 'bring', 'deliver', 'find', 'obtain', 'acquire',
                        'supply', 'offer', 'generate', 'issue', 'uncover', 'reveal', 'expose', 'disclose', 'unearth',
                        'tell', 'me'
                                'available'
                        ]

        # Checking for date input
        if 'date' in user_input.lower() and 'date' in map(str.lower, column_names):
            start_date_input = input("Enter start date in 'YYYY-MM-DD' format: ")
            end_date_input = input("Enter end date in 'YYYY-MM-DD' format: ")

            start_date = datetime.strptime(start_date_input, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_input, '%Y-%m-%d').date()

            condition = f"date >= '{start_date}' AND date <= '{end_date}'"
            query = f"SELECT * FROM {table_name} WHERE {condition}"

            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

            if rows:
                for row in rows:
                    print(row)
            else:
                print("No records found within the specified date range.")

        for idx, word in enumerate(words):
            if word in map(str.lower, column_names):
                columns.append(word)
            if word in map(str.lower, column_values_dict):
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

        # Perform query based on conditions and columns
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

        conn.close()



    except Exception as e:
        print("An error occurred:", e)
        return render_template('error.html')

    return render_template('index.html', rows=rows, column_names=column_names)


if __name__ == "__main__":
    app.run(debug=True)
