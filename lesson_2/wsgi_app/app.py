import random
import string
import time
from wsgiref.simple_server import make_server

def generate_password():
    length = random.randint(8, 16)
    chars = string.ascii_letters + string.digits + "#.,!@&^%*"
    
    while True:
        password = ''.join(random.choice(chars) for _ in range(length))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in "#.,!@&^%*" for c in password)):
            return password

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)

    # Засыпаем 50ms
    time.sleep(0.05)

    password = generate_password()
    return [password.encode('utf-8')]

# Для локального теста
if __name__ == "__main__":
    with make_server('', 8000, application) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()