import get_userinfo
from js import console

console.log("main.py is running")

def run(*args, **kwargs):
    console.log("Function 'run' is running")

    console.log(f'args: {args}')
    console.log(f'kwargs: {kwargs}')

    username = Element("user_input").element.value
    console.log(f"Username entered: {username}")

    api = get_userinfo.get_userinfo(str(username))

    Element("output").element.innerText = api