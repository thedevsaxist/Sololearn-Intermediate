# You are working on a recruitment platform, 
# which should match the available jobs and the candidates based on their skills.
# The skills required for the job, and the candidate's skills are stored in sets.
# Complete the program to output the matched skills

# You can use the & to get the values present in both sets.

skills = {'Python', 'HTML', 'SQL', 'C++', 'Scala', 'Java'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

print(list(skills & job_skills)[0])  # First convert it to a list then print the first index/iteration of the list
print(skills & job_skills)