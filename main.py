import requests

# location of github https://github.com/api/v4
response = requests.get("https://api.github.com/users/RasmiJati/projects")
# print(response)
# print(response.text)  # give string
# print(response.json)  # give in dictionary / list
# print(type(response.text))

my_projects = response.json()

for project in my_projects:
    print(f"Project name: {project['name']} \n Project url : {project['https://github.com/RasmiJati/countdownapp']} \n")
