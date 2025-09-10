import my_utils as mu
country = 'Algeria'
county_column = 1
fires_column = 4
file_name = 'Agrofood_co2_emission.csv'
fires = mu.get_column(file_name,
                      county_column,
                      country,
                      result_column=fires_column)
print(fires)
