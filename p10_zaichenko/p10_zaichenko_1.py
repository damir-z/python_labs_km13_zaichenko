salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]

new_salary_list = list(map(lambda x: 1.3 * x, salary_list))
indexation_list = list(map(lambda x: 0.3 * x, salary_list))

def c_round(num):
    """function that correctly rounds number"""
    return round(num + 10 ** (-10), 2)

print("Salary table:")
for i in range(len(salary_list)):
    print(" ".join(
        list(map(lambda x: str(c_round(x)).ljust(6), [salary_list[i], new_salary_list[i], indexation_list[i]]))))
