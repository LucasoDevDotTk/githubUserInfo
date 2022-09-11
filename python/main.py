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

def create_element(element_id, inner_text, pos):
    element = document.createElement(element_id)
    element.innerText = inner_text
    document.getElementById(str(pos)).append(element)
    console.log(f"Made element: {element_id}, {inner_text} at {pos}")

def change_inner_text(element_id, inner_text):
    element = document.getElementById(element_id)
    element.innerText = inner_text
    console.log(f"Changed element: {element_id} with innerText of {inner_text}")

def run(*args, **kwargs):
    console.log("Function 'run' is running")

    console.log(f'args: {args}')
    console.log(f'kwargs: {kwargs}')

    username = Element("user_input").element.value
    console.log(f"Username entered: {username}")

    # Production code
    api = json.loads(get_userinfo(str(username)))

    # Api test for developing
    # api = json.loads(TEST_API)

    # OUTPUT

    change_inner_text("username", api["login"])

    change_inner_text("name", api["name"])

    avatar = document.getElementById("avatar")
    avatar.setAttribute("src", api['avatar_url'])

    change_inner_text("bio", api["bio"])

    change_inner_text("usr_type", f"type: {api['type']}")

    change_inner_text("usr_id", f"id: {api['id']}")

    change_inner_text("node_id", f"node id: {api['node_id']}")

    change_inner_text("site_admin", f"Site Admin: {api['site_admin']}")

    change_inner_text("created_at", f"Updated: {api['updated_at']}")

    change_inner_text("updated_at", f"Created: {api['created_at']}")

    change_inner_text("location", f"Location: {api['location']}")

    change_inner_text("company", f"Company: {api['company']}")

    change_inner_text("email", f"Email: {api['email']}")

    change_inner_text("hireable", f"Hireable: {api['hireable']}")


