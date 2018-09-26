# -*- coding: utf-8 -*-

import pymysql

##open database connection
db = pymysql.connect("localhost", #host
                     "root", #user
                     "turnusol1991", #password
                     "sakila" #database
                     )

# prepare a cursor object using cursor() method
cursor = db.cursor()
sql = """select a.title
,	a.description
,	b.first_name
,	b.last_name
from sakila.film a 
left join (
select a.first_name
,	a.last_name
,	b.film_id
from sakila.actor a
left join sakila.film_actor b
on a.actor_id = b.actor_id
) b
on a.film_id = b.film_id
where a.title like 'zo%'"""

try: 
    # Execute the SQL command
    cursor.execute(sql)
    
    #Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        print("%s %s: title %d, description %d, first_name %d, last_name %d" % row[0], row[1], row[2], row[4])
except:
    print("Error: unable to fetch data")
