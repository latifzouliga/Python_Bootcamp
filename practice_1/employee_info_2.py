"""
11. Create a python file named employee_info:
            Ask the user to enter the following info, and display the user entered info:
                        name (String)
                        age (integer)
                        gender (String)
                        company (String)
                        job title (String)
                        salary (float)

            Ex:
                Given Data:
                    name = "Daniel"
                    age = 28
                    gender = 'Male'
                    company_name = 'Google Inc'
                    job_title = "Scrum Master"
                    salary = 90000


                Output:
                    Daniel is 28 years old, gender is Male
                    Daniel works at Google Inc as a Scrum Master
                    Daniel makes $ 90000 per year
"""
name: str = input("Enter you name\n")
age: int = int(input("Enter you age\n"))
gender: str = input("Enter you gender\n")
company: str = input("Enter you company\n")
job_title: str = input("Enter you job title\n")
salary: float = float(input("Enter you salary\n"))

print(f'{name} is {age} years old, gender is {gender}')
print(f'{name} works at {company} Inc as a {job_title}')
print(f'{name} makes ${salary} per year')
