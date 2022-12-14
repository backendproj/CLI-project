from sqlite3 import connect


test = connect('USERS.db')
cursor = test.cursor()

# cursor.execute('''
#      CREATE TABLE users(
#          FISH TEXT,
#          email TEXT,
#          tel INT
#      );
#  ''')

cursor.execute('''
    INSERT INTO users VALUES(
        'Bakhodirov Mirafzal',
        'mirafzaaal2698@gmail.com',
        '942182609'
    );
''')

# cursor.execute('''
#     SELECT email FROM users;
# ''')
# print(cursor.fetchall())
test.commit()
test.close()

