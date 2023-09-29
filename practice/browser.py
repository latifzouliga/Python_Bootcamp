"""
20. Create a python file named browser. Write a program that can display the name of selected browser
        1. declare a String variable named browser_name
        2. Assume that the valid browsers are: chrome, firefox, opera, safari, edge.
        3. if the browser name does not match with the valid browser names, out put should be: Invalid Browser Name

        Ex:
            String browser = "chrome";

        Output:
            Chrome Browser is selected

        Note: MUST use nested if
"""

browser_name = 'chrome'

is_valid = 'chrome' or 'firefox' or 'opera' or 'safari' or 'edge'

if is_valid:
    if browser_name == 'chrome':
        print(f'{browser_name} Browser is selected')
    elif browser_name == 'firefox':
        print(f'{browser_name} Browser is selected')
    elif browser_name == 'opera':
        print(f'{browser_name} Browser is selected')
    elif browser_name == 'safari':
        print(f'{browser_name} Browser is selected')
    elif browser_name == 'edge':
        print(f'{browser_name} Browser is selected')
else:
    print('Invalid browser name')



