import psycopg2
from  random import randint 
from faker import Faker #pip install faker
from random import choice

fake = Faker()
#print(fake.date_between(start_date='-3y', end_date='today'))


conn = psycopg2.connect(
    host="localhost",
    database="wib",
    user="user_",
    password="abc123")

cursor = conn.cursor()


def insert_db_data1(n):

    for i in range(n):
        cursor.execute(f'INSERT INTO public."Users"(age) VALUES ({randint(14, 80)};')
        cursor.execute(f'INSERT INTO public."Items"(price) VALUES ({randint(100, 100000)});')
       
    conn.commit()
    

# print('------')
sel = cursor.execute('select "userId" from "public"."Users"')
usersIds = [i[0] for i in cursor.fetchall()]
# print('------')
sel = cursor.execute('select "itemId" from "public"."Items"')
itemsIds = [i[0] for i in cursor.fetchall()]



def insert_db_data2(n):
    for i in range(n):
        cursor.execute(f"""INSERT INTO public."Purchases"("userId", "itemId", "date") 
                       VALUES ({choice(usersIds)}, {choice(itemsIds)}, 
                      '{fake.date_between(start_date="-3y", end_date="today").strftime('%Y-%m-%d')}'); """)
                               
    conn.commit()
    
#insert_db_data2(1000)

sel = cursor.execute('select * from public."Purchases"')
print(cursor.fetchall())
















