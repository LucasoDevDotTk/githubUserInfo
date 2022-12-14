from js import XMLHttpRequest
from js import console


def get_userinfo(user):
    request = XMLHttpRequest.new()
    request.open("GET", f"https://api.github.com/users/{user}", False)
    request.send(None)
    output = str(request.response)

    console.log(f"API is running: {output}")

    return output