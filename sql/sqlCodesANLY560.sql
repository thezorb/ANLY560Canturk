/*First Day*/

describe sakila.actor;

SELECT * FROM sakila.actor;

select "Hello, World!" as data from dual;

/*Joins*/

select a.first_name as first
,	a.last_name
,	f.title
from actor a
left join film_actor fa
on (a.actor_id = fa.actor_id)
join film f
on (f.film_id = fa.film_id)
