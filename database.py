import sqlite3


# cursor.execute('''
# create table if not exists User(
# mobile integer(10) primary key,
# name text,
# pass text)
# ''')
# connection.commit()

# cursor.execute('''
# insert into user
# values(8118050776,'happy','xyz')
# ''')
# connection.commit()

# mb=8118050776
# pas ='xyz'

# def check(mb,pas):
#     connection = sqlite3.connect('User.db')
#     cursor = connection.cursor()
#     cursor.execute('''
#     select pass from User where mobile = (?)
#     ''',[mb])
#     connection.commit()
#     rows = cursor.fetchall()
#     connection.close()
#     if rows[0][0] == pas :
#         print( f'Signed In successfully')
#     else:
#         print( f'Invalid mobile number or Password')

#     for row in rows:
#         print(type(row[0]))

#     connection.close()
#     print(type(pas))
#     print(rows[0][0])

# check(mb,pas)
def check(mb ,pas):
    try:
        connection = sqlite3.connect('User.db')
        cursor = connection.cursor()
        cursor.execute('''
        select pass from User where mobile = (?)
        ''',[mb])
        connection.commit()
        rows = cursor.fetchall()
        connection.close()
        if rows[0][0] == pas :
            return  1
        else:
            return  0

    except:
        return -1

def create(name,mobile,pas):
    try:
        connection = sqlite3.connect('User.db')
        cursor = connection.cursor()
        cursor.execute('''
        insert into User 
        values(?,?,?)
        ''',(mobile,name,pas))
        connection.commit()
        connection.close()
        return 1
    except:
        return 0



