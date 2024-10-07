from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# def home():
#     return 'hello home!'


# @app.route('/hello')
# @app.route('/hello/<name>')
# def google(name=None):
#     return render_template('button.html', person=name)


def index():
    first_name='dheman'
    stuff='this is Bold text'
    favourite_colors=["yellow", "blue", "purple", "pink", 100]
    
    return render_template('render_function.html', first_name=first_name, stuff=stuff,
    favourite_colors = favourite_colors)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500






# @app.route('/<name>')
# def user_name(name):
#     return render_template('render_function.html', user_name=name)
    
if __name__=='__main__':
    app.run(debug=True)  # port can be change like : port=8000  








