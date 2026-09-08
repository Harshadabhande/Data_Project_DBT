{{
config(
    materialized='incremental',
    unique_key='employee_id'
)
}}
select *,
      current_timestamp() as updated_at
from
     {{ source('walmart_databricks', 'employees') }}


{% if is_incremental() %}
    where updated_timestamp > (select COALESCE(max(updated_at),'2001-01-01') from {{ this }})
{% endif %}