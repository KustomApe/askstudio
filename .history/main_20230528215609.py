from flask import Flask, request, jsonify

app = Flask(__name__)


# @app.route('/')
# def home():
#     return 'Home'

@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_data = {
        'user_id': user_id,
        'name': 'Eisuke Nakanishi',
        'email': 'kustomape@gmail.com',
    }

if __name__ == '__main__':
    app.run(debug=True)