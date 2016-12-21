# from flask import Flask
# from flask import render_template
#
# app = Flask(__name__)
#
# @app.route('/index')
# def index():
#     user = {'nickname': 'Sasha'}  # fake user
#     return render_template('index.html',
#                            title='Secret',
#                            user=user)
#     # '''
#                # <html>
#                #     <head>
#                #         <title>Home Page</title>
#                #     </head>
#                #     <body>
#                #         <h1>Hello, ''' + user['nickname'] + '''</h1>
#                #     </body>
#                # </html>'''
#
# if __name__ == '__main__':
#     app.run(debug=True)
#


from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
