from flask import Flask, url_for
import os

app = Flask(__name__)

@app.route('/<lhs>/<rhs>/<n>')
def api_add(lhs, rhs, n):
    a, b, n = int(lhs), int(rhs), int(n)
    s = a
    for i in range(n):
        s += b
    return str(s)

if __name__ == '__main__':
    port = int(os.getenv('PORT') or 5001)
    print('Starting app-add at port %d.' % port)
    app.run(host='0.0.0.0', port=port)
