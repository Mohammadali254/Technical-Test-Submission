/* Write a query that will display the results below (Note: some columns might be renamed
but use the column names above). It should only show 2020 data and order by driver
points. */

SELECT 
    driver_name,       
    team_name,          
    race_date,         
    driver_points       
FROM 
    race_results        
WHERE 
    YEAR(race_date) = 2020   
ORDER BY 
    driver_points DESC;  
