import getpass
import pg8000
import matplotlib.pyplot as plt
import re

user = input("Username: ")
secret = getpass.getpass()
db = pg8000.connect(user=user, password=secret, host="codd.mines.edu", port=5433, database="csci403")

type_person = input("View less than high school diploma (lhsd), only high school diploma (hsd), only associates (ad) and bachelors or above (bad): ")

if type_person == "lhsd":
	chosen_table = "education_less_hs"
	chosen_column = "percent_less_hs"
elif type_person == "hsd":
	chosen_table = "education_hs"
	chosen_column = "percent_hs"
elif type_person == "ad":
	chosen_table = "education_associates"
	chosen_column = "percent_associates"
elif type_person == "bad":
	chosen_table = "education_bachelors"
	chosen_column = "percent_bachelors"
else:
	print("Invalid choice chosen")
	exit(1)

year = input("Year: ")
cleaned_year = re.sub(r'[^0-9]', '', year)
if len(cleaned_year) > 4:
	print("Invalid year chosen")
	exit(1)

cursor = db.cursor()

cursor.execute("SELECT DISTINCT br.birth_rate/1000 AS birth_rate, ed.%s AS %s, br.year, br.fips FROM f22_group5.birth br JOIN f22_group5.%s ed ON br.fips=ed.fips WHERE br.year=%s;" % (chosen_column, chosen_column, chosen_table, cleaned_year))

results = cursor.fetchall()
x = []
y = []
for row in results:
	birth_rate, percent_less_hs, year, fips = row
	x.append(percent_less_hs)
	y.append(birth_rate)

plt.scatter(x, y, s=0.4, c="black", edgecolors=(0, 0, 0, 0.0))
plt.title("Correlation of people who have had teenage pregnancies and people who have achieved the chosen degree in %s" % (cleaned_year), fontdict={"fontsize":7})
plt.xlabel("Percent of people who have achieved degree")
plt.ylabel("Percent of people who have had teenage pregnancies")
plt.savefig("chart2.png", dpi=1000)
