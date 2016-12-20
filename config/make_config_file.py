import os
import json
from  sync_gitlab import projects


config = {}
config["max-concurrent-indexers"] = 4
config["dbpath"] =  "data"
config["repos"] = {}

example = {"gitlab-hound" : {
            "url" : "git@github.com:townie/gitlab-hound.git",
            "ms-between-poll": 10000}
               }
            
    
config["repos"]['townie/gitlab-hound'] = example['gitlab-hound']

for p in projects:
    url = p.ssh_url_to_repo
    key = p.name_with_namespace
    print("adding project{}".format(key))
    config['repos'][key] =  { "url": url, "ms-between-poll": 10000}



with open('config.json', 'w') as f:
    f.write(json.dumps(config, indent=4))

