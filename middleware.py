
from flask import Request
import jwt

def decodetoken(token :str):
    try:
        token = jwt.decode(token, 'MEHDI' ,algorithms=['HS256'])
    except Exception:
        token = None
    return token
    
class Middleware:

    def __init__(self, app):
        self.app=app

    def __call__(self, environ, start_response) :
        request=Request(environ)
        Authtoken = request.headers['x-access-token'] if 'x-access-token' in request.headers else None
        print(request.headers)

        if Authtoken is not None:
            mytoken = decodetoken(Authtoken)
            if mytoken:
                print("TOKEN VALID")
            else:
                print("TOKEN INVALID")
        else:
            print("TOKEN IS MISSING")

        return self.app(environ,start_response)