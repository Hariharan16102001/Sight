import pyodbc

# Establish a connection to your SQL Server database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-S0QIC03\MYPROJECT;'
                      'Database=Test;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()


# Function to fetch values from the database
def fetch_values(words):
    placeholders = ', '.join('?' for _ in words)
    query = f"SELECT value_column FROM Dbo.fashiontest WHERE word_column IN ({placeholders})"

    cursor.execute(query, words)
    rows = cursor.fetchall()

    values = [row[0] for row in rows]
    return values


# Take user input and split it into words
user_input = input("Enter a sentence: ")
user_words = user_input.split()

# Fetch values from the database for the words
result_values = fetch_values(user_words)

# Display the retrieved values
for word, value in zip(user_words, result_values):
    print(f"Word: {word}, Value: {value}")

# Close the database connection
cursor.close()
conn.close()
