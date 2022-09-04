from get_userinfo import get_userinfo

from js import console, document
import json

console.log("main.py is running")

TEST_API = """ {
  "login": "LucasoDevDotTk",
  "id": 80215223,
  "node_id": "MDQ6VXNlcjgwMjE1MjIz",
  "avatar_url": "https://avatars.githubusercontent.com/u/80215223?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/LucasoDevDotTk",
  "html_url": "https://github.com/LucasoDevDotTk",
  "followers_url": "https://api.github.com/users/LucasoDevDotTk/followers",
  "following_url": "https://api.github.com/users/LucasoDevDotTk/following{/other_user}",
  "gists_url": "https://api.github.com/users/LucasoDevDotTk/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/LucasoDevDotTk/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/LucasoDevDotTk/subscriptions",
  "organizations_url": "https://api.github.com/users/LucasoDevDotTk/orgs",
  "repos_url": "https://api.github.com/users/LucasoDevDotTk/repos",
  "events_url": "https://api.github.com/users/LucasoDevDotTk/events{/privacy}",
  "received_events_url": "https://api.github.com/users/LucasoDevDotTk/received_events",
  "type": "User",
  "site_admin": false,
  "name": "Lucas Nguyen",
  "company": "@Avdan-OS",
  "blog": "https://lucasodev.tk/",
  "location": "localhost",
  "email": null,
  "hireable": null,
  "bio": "I am a beginner python developer wanting to make fun projects.",
  "twitter_username": null,
  "public_repos": 19,
  "public_gists": 1,
  "followers": 1,
  "following": 6,
  "created_at": "2021-03-07T17:08:58Z",
  "updated_at": "2022-08-31T08:55:43Z"
}

"""

def create_element(element_name, innerText, pos):
    element = document.createElement(element_name)
    element.innerText = innerText
    document.getElementById(str(pos)).append(element)
    console.log(f"Made element: {element_name}, {innerText} at {pos}")

def run(*args, **kwargs):
    console.log("Function 'run' is running")

    console.log(f'args: {args}')
    console.log(f'kwargs: {kwargs}')

    username = Element("user_input").element.value
    console.log(f"Username entered: {username}")

    # Production code
    # api = json.loads(get_userinfo(str(username)))

api = json.loads(TEST_API)

# OUTPUT

usr = document.getElementById("username")
usr.innerHTML = api["login"]

avatar = document.getElementById("avatar")
avatar.setAttribute("src", "https://avatars.githubusercontent.com/u/80215223?v=4")

usr_type = document.getElementById("usr_type")
usr_type.innerHTML = f"type: {api['type']}"

usr_id = document.getElementById("usr_id")
usr_id.innerHTML = f"id: {api['id']}"

node_id = document.getElementById("node_id")
node_id.innerHTML = f"node id: {api['node_id']}"

site_admin = document.getElementById("site_admin")
site_admin.innerHTML = f"Site Admin: {api['site_admin']}"



    