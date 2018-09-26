select a.title
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
where a.title like 'zo%'
