import getpass 
import pg8000.dbapi

user = input("Username: ") 
secret = getpass.getpass() 
db = pg8000.dbapi.connect(user=user, password=secret, host="codd.mines.edu", port=5433, database="csci403") 
cursor = db.cursor()
cursor.execute("SET SESSION search_path='%s'" % 'f22_group5')


def percentile(year=2020, percentile=0.75):
    num_above_query = """
        SELECT COUNT(*)
        FROM area_codes ac 
            JOIN area_birth_rates br ON ac.fips = br.fips
            JOIN education_less_hs ed1 ON br.fips = ed1.fips AND br.year = ed1.year
        WHERE
            br.year = %s AND 
            birth_rate IS NOT NULL AND percent_less_hs IS NOT NULL AND
            birth_rate > (SELECT percentile_disc(%s) WITHIN GROUP (ORDER BY birth_rate) 
                            FROM area_birth_rates
                            WHERE year = %s)
            AND
            percent_less_hs > (SELECT percentile_disc(%s) WITHIN GROUP (ORDER BY percent_less_hs) 
                            FROM education_less_hs
                            WHERE year = %s);
    """
    cursor.execute(num_above_query, (year, percentile, year, percentile, year))
    num_above_percentile = int(cursor.fetchone()[0])

    total_amount_query = """
        SELECT COUNT(*) * CAST(%s as numeric)
        FROM area_codes ac 
            JOIN area_birth_rates br ON ac.fips = br.fips
            JOIN education_less_hs ed1 ON br.fips = ed1.fips AND br.year = ed1.year
        WHERE 
            br.year = %s AND 
            birth_rate IS NOT NULL AND percent_less_hs IS NOT NULL;
    """
    cursor.execute(total_amount_query, (float(1-percentile), year))
    total_num = int(cursor.fetchone()[0])

    result = num_above_percentile / total_num
    print(f'For the year {year}:')
    print(f'Out of the {total_num} counties above the {percentile} percentile for high birth rates,')
    print(f'{num_above_percentile} of them ({round(result*100, 2)}%) also were above the {percentile} percentile for low education rates')
    return result


if __name__ == '__main__':
    
    percentile()