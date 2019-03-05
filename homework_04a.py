import urllib.request
import urllib.error
import json
from collections import defaultdict

def Github(*args):
    dd = defaultdict(int)
    if not args:
        userID = input('please input your ID: ')
    else:
        userID = args[0]
    try:
        website_respond_repo = urllib.request.urlopen(f'https://api.github.com/users/{userID}/repos')
    
    except urllib.error.HTTPError:   # raise an error if the user input the non_exist ID
    
        raise urllib.error.HTTPError('this ID is wrong, please try again')
    
    else:
        js_dict = json.loads(website_respond_repo)
        for i in js_dict:        
            repo = i["name"]
            
            website_respond_commit = urllib.request.urlopen(f'https://api.github.com/repos/{userID}/{repo}/commits')
            js_dict_commit = json.loads(website_respond_commit)
            for n in js_dict_commit:
                dd[repo] += 1
    result_list = []
    for key in dd.keys():
        result_list.append(f'Repo: {key}  Number of commits: {dd[key]}')
    
    return(result_list)

