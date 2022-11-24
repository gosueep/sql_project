import getpass
import pg8000
import matplotlib.pyplot as plt

user = input("Username: ")
secret = getpass.getpass()
db = pg8000.connect(user=user, password=secret, host="codd.mines.edu", port=5433, database="csci403")

cursor = db.cursor()

cursor.execute("SELECT DISTINCT br.birth_rate/1000 AS birth_rate, ed.percent_less_hs AS percent_less_hs, br.year, br.fips FROM f22_group5.birth br JOIN f22_group5.education_less_hs ed ON br.fips=ed.fips ORDER BY br.year DESC;")

results = cursor.fetchall()
x = []
y = []
for row in results:
	birth_rate, percent_less_hs, year, fips = row
	x.append(percent_less_hs)
	y.append(birth_rate)

plt.scatter(x, y, s=0.1, c="black", edgecolors=(0, 0, 0, 0.0))
plt.title("Correlation of people who have had teenage pregnancies and people who haven't graduated high school", fontdict={"fontsize":8})
plt.xlabel("Percent of people who haven't graduated high school")
plt.ylabel("Percent of people who have had teenage pregnancies")
plt.savefig("chart.png", dpi=1000)
