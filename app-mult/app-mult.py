from flask import Flask, url_for
import os
import requests as req

app = Flask(__name__)

def get_add(a, b, n):
    res = req.get('http://app-add:5001/%d/%d/%d' % (a, b, n))
    return int(res.text)

@app.route('/<lhs>/<rhs>')
def api_mult(lhs, rhs):
    a, b = int(lhs), int(rhs)
    if a == 0 or b == 0: return '0'
    ret = abs(get_add(0, a, abs(b)))
    if (a < 0 and b > 0) or (a > 0 and b < 0): ret = -ret
    return str(ret)

if __name__ == '__main__':
    port = int(os.getenv('PORT') or 5003)
    print('Starting app-add at port %d.' % port)
    app.run(host='0.0.0.0', port=port)
