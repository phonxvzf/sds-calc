from flask import Flask, url_for
import os
import requests as req

app = Flask(__name__)

def get_add(a, b):
    res = req.get('http://app-add:5001/%d/%d/1' % (a, b))
    return int(res.text)

@app.route('/<lhs>/<rhs>/<n>')
def api_diff(lhs, rhs, n):
    a, b, n = int(lhs), int(rhs), int(n)
    s = a
    for i in range(n):
        s += get_add(0, -b)
    return str(s)

if __name__ == '__main__':
    port = int(os.getenv('PORT') or 5002)
    print('Starting app-diff at port %d.' % port)
    app.run(host='0.0.0.0', port=port)
