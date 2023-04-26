from flask import Flask,render_template, request

from view import auth_bp

app= Flask(__name__)
app.register_blueprint(auth_bp)
if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True,host='0.0.0.0',port=80)
=======
    app.run(debug=True,host='0.0.0.0',port=80)
>>>>>>> df7da0ee2362274a995bc1b5e0db12e180d491d2
