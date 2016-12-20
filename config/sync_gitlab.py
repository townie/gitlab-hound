import gitlab
import os

# private token authentication
# gl = gitlab.Gitlab('http://10.0.0.1', 'JVNSESs8EwWRx5yDxM5q')

# or username/password authentication
host = os.environ['HOST']
user = os.environ['USER']
password = os.environ['PASSWORD']
gl = gitlab.Gitlab(host, email=user, password=password)
# make an API request to create the gl.user object. This is mandatory if you
# use the username/password authentication.
gl.auth()


projects = []
def all_projects(gl):
    projects = []
    page_index = 0 
    while True:
        page_result = gl.projects.all(page=page_index)
        if len(page_result) == 0: break
        projects.extend(page_result)
        page_index = page_index + 1
    return projects


projects = all_projects(gl)

ids = []
for pj in projects:
    ids.append(pj.ssh_url_to_repo)


