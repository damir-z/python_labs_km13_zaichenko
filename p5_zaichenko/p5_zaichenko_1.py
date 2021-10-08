salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
new_salary, indexation = list(), list()

for i in range(len(salary_list)):
    new_salary.append(salary_list[i] * 1.3)
    indexation.append(new_salary[i] - salary_list[i])

print("Old Salary:    New Salary:    Indexation: ")
for i in range(len(salary_list)):
    print(str(salary_list[i]).ljust(14), str(round(new_salary[i], 2)).ljust(14), str(round(indexation[i], 2)))
