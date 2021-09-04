from github import Github
import requests
from pprint import pprint
from random import randint
import base64

#username = 'exploreGithub'
#passwd = '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'
g = Github()
#user = g.get_user()

#def view_repo():
#    repos = user.get_repos()

#    for repo in repos:
#        print(repo.name)

#def create_repo():
#   try:
#        name = input('Give repo name :')
#        repo = user.create_repo(name)
#    except :
#        print('not possible')

def user_info():
    id = input("user id : ")
    url = f'''https://api.github.com/users/{id}'''
    data = requests.get(url).json()
    pprint(data)
    for repo in Github().get_user(id).get_repos():
     print(repo.name)

def repo_info():
    id = input("User/RepoName  :")
    try:
    	repo = g.get_repo(id)
    	print(f'''url: {repo.url}\nid: {repo.id}\n''')
    except:
     	print('no repo found')
     
def random():
	f=0
	while True:	
		try:
			r = randint(1000000,3999999)
			repo = g.get_repo(r)
			print(repo.url)
			f=f+1
		except:
			pass
		if f==3:
			break

def main():
    op = input('operation :')
    
#    if op == 'ls':
#        view_repo()
#    elif op == 'mkdir':
#        create_repo()
    if op == 'find user':
        user_info()
    elif op == 'find repo':
    	repo_info()
    elif op == 'random':
    	random()
    else:
        print('sorry')

main()   
