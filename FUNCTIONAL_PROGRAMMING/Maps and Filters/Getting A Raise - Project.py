# You are working on a payroll program.
# Given a list of salaries, you need to take the bonus everybody is getting as input
# and increase all the salaries by that amount.
# Output the resulting list

# You can use the map() to increase all the values of the list

"""Named function"""
bonus = int(input("Enter the bonus: "))
def increase(salary):
    return salary + bonus

salaries = [2000, 1800, 3100, 4400, 1500]
new_salaries = list(map(increase, salaries))
print(new_salaries)


"""Lambda function"""
# bonus = int(input("Enter the bonus: "))
# salaries = [2000, 1800, 3100, 4400, 1500]

# new_salaries = list(map(lambda x: x + bonus, salaries))
# print(new_salaries)