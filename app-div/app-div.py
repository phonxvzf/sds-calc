from flask import Flask, url_for
import os
import requests as req

app = Flask(__name__)

def get_diff(a, b, n):
    res = req.get('http://app-diff:5002/%d/%d/%d' % (a, b, n))
    return int(res.text)

@app.route('/<lhs>/<rhs>')
def api_div(lhs, rhs):
    a, b = int(lhs), int(rhs)
    if b == 0: return 'inf'
    ret = 0

    a_abs, b_abs = abs(a), abs(b)
    while a_abs > 0:
        a_abs = get_diff(a_abs, b_abs, 1)
        if a_abs >= 0: ret += 1

    if (a < 0 and b > 0) or (a > 0 and b < 0): ret = -ret
    return str(ret)

if __name__ == '__main__':
    port = int(os.getenv('PORT') or 5004)
    print('Starting app-add at port %d.' % port)
    app.run(host='0.0.0.0', port=port)
