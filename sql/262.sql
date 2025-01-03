-- Write your PostgreSQL query statement below
with t1 as (
    select users_id from Users where banned = 'Yes'
),
t2 as (
    select
        id,
        status,
        request_at, 
        case when
            client_id in (select * from t1)
            or driver_id in (select * from t1)
            then 1 else 0
        end as req_banned
    from Trips
    where request_at between '2013-10-01' and '2013-10-03'
),
t3 as (
    select
        request_at as Day,
        case when sum(case when req_banned = 0 then 1 else 0 end) = 0 then -1 else
        round(
            sum(
                case when
                status in ('cancelled_by_driver', 'cancelled_by_client') and req_banned = 0
                then 1 else 0 end
            ) * 1.0 / sum(case when req_banned = 0 then 1 else 0 end)
            ,2
        )
        end as "Cancellation Rate"
    from t2
    group by request_at
)
select * from t3
where "Cancellation Rate" <> -1