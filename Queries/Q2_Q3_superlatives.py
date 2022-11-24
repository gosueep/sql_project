import getpass 
import pg8000.dbapi

user = input("Username: ") 
secret = getpass.getpass() 
db = pg8000.dbapi.connect(user=user, password=secret, host="codd.mines.edu", port=5433, database="csci403") 
cursor = db.cursor()
cursor.execute("SET SESSION search_path='%s'" % 'f22_group5')


def birth(year=2020):
    query = """
        SELECT birth_rate, state, county
        FROM area_codes ac JOIN area_birth_rates br ON ac.fips = br.fips
        WHERE
            year = %s AND
            birth_rate = (SELECT MAX(birth_rate) FROM area_birth_rates WHERE year = %s)
        ;
    """
    cursor.execute(query, (year, year))
    results = cursor.fetchall()
    print(results)
    return results


def birth_many(year=2020, amount=10):
    query = """
        SELECT birth_rate, state, county
        FROM area_codes ac JOIN area_birth_rates br ON ac.fips = br.fips
        WHERE
            year = %s
        ORDER BY birth_rate DESC NULLS LAST
        LIMIT %s;
    """
    cursor.execute(query, (year, amount))
    results = cursor.fetchall()
    for i in results:
        print(i)
    return results


def education(year=2020):
    query = """
        SELECT percent_less_hs, state, area
        FROM fips_state_area fsa JOIN education_less_hs br ON fsa.fips = br.fips
        WHERE
            year = %s AND
            percent_less_hs = (SELECT MAX(percent_less_hs) FROM education_less_hs WHERE year = %s)
        ;
    """
    cursor.execute(query, (year, year))
    results = cursor.fetchall()
    print(results)
    return results


def education_many(year=2020, amount=10):
    query = """
        SELECT percent_less_hs, state, area
        FROM fips_state_area fsa JOIN education_less_hs br ON fsa.fips = br.fips
        WHERE
            year = %s
        ORDER BY percent_less_hs DESC NULLS LAST
        LIMIT %s;
    """
    cursor.execute(query, (year, amount))
    results = cursor.fetchall()
    for i in results:
        print(i)
    return results


if __name__ == '__main__':
    
    birth()
    birth_many()

    print()

    education()
    education_many()