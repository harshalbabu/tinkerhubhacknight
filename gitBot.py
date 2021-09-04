from github import Github
import requests
from pprint import pprint
import base64

username = 'exploreGithub'
passwd = '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'
g = Github(username, passwd)
user = g.get_user()

def view_repo():
    repos = user.get_repos()

    for repo in repos:
        print(repo.name)

def create_repo():
    try:
        name = input('Give repo name :')
        repo = user.create_repo(name)
    except :
        print('not possible')

def user_info():
    id = input("user id : ")
    url = f'''https://api.github.com/users/{id}'''
    data = requests.get(url).json()
    pprint(data)
    for repo in Github().get_user(id).get_repos():
     print(repo.name)

def main():
    op = input('operation :')
    
    if op == 'ls':
        view_repo()
    elif op == 'mkdir':
        create_repo()
    elif op == 'find user':
        user_info()
    else:
        print('sorry')

main()   
