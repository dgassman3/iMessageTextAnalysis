select 
--select fields
m.text, 
datetime(substr(m.date, 1, 9) + 978307200, 'unixepoch', 'localtime') as message_date,
(select case strftime('%m', datetime(substr(m.date, 1, 9) + 978307200, 'unixepoch', 'localtime')) when '01' then 'January' when '02' then 'February'
when '03' then 'March' when '04' then 'April' when '05' then 'May' when '06' then 'June' when '07' then 'July' when '08' then 'August'
when '09' then 'September' when '10' then 'October' when '11' then 'November' when '12' then 'December' end) as month,
strftime('%d', datetime(substr(m.date, 1, 9) + 978307200, 'unixepoch', 'localtime')) as DayOfMonth,
strftime('%m', datetime(substr(m.date, 1, 9) + 978307200, 'unixepoch', 'localtime')) as MonthNumber,
strftime('%Y', datetime(substr(m.date, 1, 9) + 978307200, 'unixepoch', 'localtime')) as Year,
strftime('%H', datetime(substr(m.date, 1, 9) + 978307200, 'unixepoch', 'localtime')) as HourOfDay,
date(substr(m.date, 1, 9) + 978307200, 'unixepoch', 'localtime') as MessageDate,
time(substr(m.date, 1, 9) + 978307200, 'unixepoch', 'localtime') as MessageTime,
h.id 
--joins
from message m 
inner join handle h on m.handle_id = h.ROWID
--where clause
where h.id = '+15618099059'