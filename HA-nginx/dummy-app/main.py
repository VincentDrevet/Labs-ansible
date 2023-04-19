from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def index():
    loadbalancer = request.remote_addr
    client = request.headers.get('X-Forwarded-For', request.remote_addr)
    return "Loadbalancer IP : {0}\nClient IP : {1}".format(loadbalancer, client)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)