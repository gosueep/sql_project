import getpass
import pg8000
import matplotlib.pyplot as plt

user = input("Username: ")
secret = getpass.getpass()
db = pg8000.connect(user=user, password=secret, host="codd.mines.edu", port=5433, database="csci403")

cursor = db.cursor()

query = """
SELECT ed1.year, percent_less_hs, percent_hs, percent_associates, percent_bachelors
        FROM f22_group5.area_codes ac 
            JOIN f22_group5.education_less_hs ed1 ON ac.fips = ed1.fips
            JOIN f22_group5.education_hs ed2 ON ed1.fips = ed2.fips AND ed1.year = ed2.year
            JOIN f22_group5.education_associates ed3 ON ed1.fips = ed3.fips AND ed1.year = ed3.year
            JOIN f22_group5.education_bachelors ed4 ON ed1.fips = ed4.fips AND ed1.year = ed4.year
        WHERE
            ed1.fips = 8059
        ORDER BY ed1.year;
"""
cursor.execute(query)

results = cursor.fetchall()
x = []
y1 = []
y2 = []
y3 = []
y4 = []
for row in results:
	year, percent_less_hs, percent_hs, percent_associates, percent_bachelors = row
	x.append(year)
	y1.append(percent_less_hs)
	y2.append(percent_hs)
	y3.append(percent_associates)
	y4.append(percent_bachelors)

fig, ax = plt.subplots()
ax.plot(x, y1, c="red", label="Percent without a high school diploma")
ax.plot(x, y2, c="green", label="Percent with only a high school diploma")
ax.plot(x, y3, c="blue", label="Percent with only an associates degree")
ax.plot(x, y4, c="orange", label="Percent with a bachelor's degree or higher")
ax.legend(loc="upper left")

plt.title("Education rates in Jefferson County over time", fontdict={"fontsize":16})
plt.xlabel("Year")
plt.xticks(range(2007, 2021, 2))
#plt.ylabel("Percent of people who have had teenage pregnancies")
plt.savefig("jefferson2.png")
