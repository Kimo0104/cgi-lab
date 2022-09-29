#!/usr/bin/env python3
import os
import json
from templates import login_page, secret_page
import cgi 

env_vars = {key:val for key,val in os.environ.items()}

'''
print("Content-Type: application/json\n")   
print(json.dumps(env_vars))
print(env_vars["HTTP_USER_AGENT"]) # printing browser.
'''
#https://github.com/aianta/cgi-lab/blob/master/login.py#:~:text=def%20parse_cookies(,%22HTTP_COOKIE%22%5D)
def parse_cookies(cookie_string):
    result = {}
    if cookie_string == "":
        return result
        
    cookies = cookie_string.split(";")
    for cookie in cookies:
        split_cookie = cookie.split("=")
        result[split_cookie[0]] = split_cookie[1]

    return result

cookies = parse_cookies(os.environ["HTTP_COOKIE"])
##########################################################################################################

form = cgi.FieldStorage()
username = form.getfirst("username")
password = form.getfirst("password")
header = "Content-Type: text/html\r\n"
body = ""

if username is not None or ('logged' in cookies and cookies['logged'] == "true"): 
    body += secret_page(username, password)
    header += "Set-Cookie: logged=true; Max-Age=30\r\n"
else:
    body += login_page()

print(header)
print(body)
#print(cookies)