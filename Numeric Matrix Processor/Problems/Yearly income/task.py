with open("salary.txt", "r") as f:
    salary = []
    for i in f:
        salary.append(int(i.strip("\n")))

with open("salary_year.txt", "w") as f2:
    for i in salary:
        f2.write(str(i * 12) + "\n")