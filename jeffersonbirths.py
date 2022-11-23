import getpass
import pg8000
import matplotlib.pyplot as plt

user = input("Username: ")
secret = getpass.getpass()
db = pg8000.connect(user=user, password=secret, host="codd.mines.edu", port=5433, database="csci403")

cursor = db.cursor()

cursor.execute("SELECT DISTINCT year, birth_rate/10 FROM f22_group5.area_birth_rates where fips=8059 ORDER BY year;")

results = cursor.fetchall()
x = []
y = []
for row in results:
	year, birth_rate = row
	x.append(year)
	y.append(birth_rate)

plt.plot(x, y, c="black")
plt.title("Teenage birth rates in Jefferson County over time", fontdict={"fontsize":16})
plt.xlabel("Year")
plt.xticks(range(2000, 2021, 2))
plt.ylabel("Percent of people who have had teenage pregnancies")
plt.savefig("jefferson1.png")
