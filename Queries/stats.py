import getpass 
import pg8000.dbapi

user = input("Username: ") 
secret = getpass.getpass() 
db = pg8000.dbapi.connect(user=user, password=secret, host="codd.mines.edu", port=5433, database="csci403") 
cursor = db.cursor()
cursor.execute("SET SESSION search_path='%s'" % 'f22_group5')


def change(start=2010, end=2020, state='Colorado', county='Jefferson'):
    query = """
        SELECT br.year, birth_rate, percent_less_hs, percent_hs, percent_associates, percent_bachelors
        FROM area_codes ac 
            JOIN area_birth_rates br ON ac.fips = br.fips
            JOIN education_less_hs ed1 ON br.fips = ed1.fips AND br.year = ed1.year
            JOIN education_hs ed2 ON br.fips = ed2.fips AND br.year = ed2.year
            JOIN education_associates ed3 ON br.fips = ed3.fips AND br.year = ed3.year
            JOIN education_bachelors ed4 ON br.fips = ed4.fips AND br.year = ed4.year
        WHERE
            br.year = %s AND  
            br.fips = (SELECT DISTINCT fips
                    FROM area_codes 
                    WHERE state = %s AND county = %s);
    """

    # PREPARED STATEMENT for the year range
    results = []
    for year in (start, end):
        cursor.execute(query, (year, state, county))
        results.append([float(x) for x in cursor.fetchone()])
    
    changes = [round(results[1][x] - results[0][x], 2) for x in range(len(results[0]))]
    
    print(f'{county} County, {state}')
    print(f'Changes over {changes[0]} years from {start}-{end}:')
    print(f'Birth rate: {changes[1]}')
    print(f'Percent Less than HS: {changes[2]}')
    print(f'Percent With HS Diploma: {changes[3]}')
    print(f'Percent With Associate\'s: {changes[4]}')
    print(f'Percent With Bachelor\'s: {changes[5]}')

    return changes


if __name__ == '__main__':
    
    if input('User input? (y/n) ') == 'y':
        state = input('State: ')
        county = input('County: ')
        start = input('Start year: ')
        end = input('End year: ')
        results = change(start, end, state, county)
    else:
        results = change()