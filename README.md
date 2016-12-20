# Gitlab Hound Auto Sync Config


## Usage:


```shell
# git it
git clone git@github.com:townie/gitlab_hound.git && cd gitlab_hound

# build it
docker build -t gitlab_hound . 

# secure it
echo 'HOST=<http://github.com> \nUSER=<townie> \nPASSWORD=<secret>' > .env

# config it
docker run  --net=host -v $PWD/config/:/config gitlab_hound python make_config_file.py

# hount it
docker run --net=host -d -p 6080:6080 --name hound -v $PWD/config:/data etsy/hound

```
