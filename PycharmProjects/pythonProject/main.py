from flask import Flask, render_template, request

app= Flask(__name__)

import cx_Oracle

# Establish the database con    nection and define table_name
connection = cx_Oracle.connect('system/Meena@123@localhost:1521/orcl')
# table_name = "HOMEAPPLIANCE_DETAILS"
table_name = "ORDER_DETAILS"

# Function to execute a query
def execute_query(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    finally:
        cursor.close()

# Function to fetch data as a dictionary
def fetch_data_as_dict(connection, table_name):
    cursor = connection.cursor()
    query_rows = f"SELECT * FROM {table_name}"
    cursor.execute(query_rows)
    rows = cursor.fetchall()

    column_names = [desc[0] for desc in cursor.description]

    data_details = []
    for row in rows:
        data = dict(zip(column_names, row))
        data_details.append(data)
    cursor.close()

    return data_details

# Function to get column values
def get_column_values(data_details, column_name):
    column_values = [row.get(column_name, None) for row in data_details]
    return column_values

# Function to get rows by a specific value
def get_rows_by_value(data_details, column_name, column_value):
    matching_rows = []
    for row in data_details:
        stored_value = str(row.get(column_name, '')).upper()
        if column_value in stored_value:
            matching_rows.append(row)
    return matching_rows

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html', data_details=data_details, columns=columns)

# Route for handling the search
@app.route('/search', methods=['POST'])
# ...

@app.route('/search', methods=['POST'])
def search():
    user_input = request.form['user_input'].upper()

    if user_input == 'EXIT':
        return "THANK YOU, VISIT AGAIN"
    if user_input =='HAI' :
        return "how are you! how can I help you"
    if user_input == 'appliance details':
        return "ENTER THE APPLIANCE ID OR WHATEVER YOU WANT"

    digit_matching_rows = []

    try:
        appliance_id = int(user_input)
        digit_matching_rows = [row for row in data_details if str(row.get('APPLIANCE_ID')).upper() == user_input]
        if digit_matching_rows:
            print(f"Row with Appliance ID '{appliance_id}': {digit_matching_rows}")
            return render_template('search_results.html', matching_rows=digit_matching_rows)
        else:
            print(f"No rows found with Appliance ID '{appliance_id}'")
    except ValueError:
        pass  # Ignore if the input is not a valid integer

    # Check for multiple values input
    search_terms = user_input.split()
    search_terms = user_input.split()
    if len(search_terms) == 2 and search_terms[0] in columns:
        column_name, column_value = search_terms
        matching_rows_column_value = [row for row in data_details if
                                      str(row.get(column_name, '')).upper().startswith(column_value.upper())]
        if matching_rows_column_value:
            print(f"Rows matching the criteria: {matching_rows_column_value}")
            return render_template('search_results.html', matching_rows=matching_rows_column_value)
        else:
            print(f"No rows found with {column_name} starting with '{column_value}'")
            return render_template('index.html', data_details=data_details, columns=columns)
    else:
        # Check for multiple values input
        partial_matching_rows = [row for row in data_details if
                                         all(term in str(row.values()).upper() for term in search_terms)]

        if partial_matching_rows:
            print(f"Rows matching the criteria: {partial_matching_rows}")
            return render_template('search_results.html', matching_rows=partial_matching_rows)
        else:
            print(f"No rows found partially matching the criteria")
            return render_template('index.html', data_details=data_details, columns=columns)

# Route for serving favicon.ico
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

# Fetch the column names before the loop
cursor = connection.cursor()
query_columns = f"SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = '{table_name}'"
cursor.execute(query_columns)
columns = [col[0] for col in cursor.fetchall()]
cursor.close()

# Move the definition of data_details outside the function
data_details = fetch_data_as_dict(connection, table_name)

if _name_ == "_main_":
    app.run(debug=True)