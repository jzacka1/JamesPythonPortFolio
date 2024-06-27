from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

# user following commands in the powershell prompt in order to run Flask
# venv\Scripts\activate
# $env:FLASK_APP = "server.py"
# flask run

# To run in development mode, add the following line of code
# $env:FLASK_DEBUG=1

# NOTE:  The server can only run when the .py file, 'server.py' is inside a venv directory

@app.route('/<username>/<int:post_id>')
def hello_world(username = None, post_id = None):
    return render_template('./index_copy.html', name = username, post_id = post_id)
#'Hello, World!  I\'m James!  This is my world.' 

@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name+'.html')

def write_to_file(data):
    with open('JamesPythonPortFolio/database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('JamesPythonPortFolio/database.csv', newline='', mode='a',encoding="utf8") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', lineterminator='\n', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou')
        except:
            return 'did not save to database'
    else:
        return request.method + ' You\'re a failure'

# @app.route('/about')
# def about():
#     return render_template('./about.html')
# #'Hello, World!  I\'m James!  This is my world.'

# @app.route('/works')
# def works():
#     return render_template('./works.html')

# @app.route('/contact')
# def contact():
#     return render_template('./contact.html')

# @app.route('/component')
# def component():
#     return render_template('./component.html')

# @app.route('/blog')
# def blog():
#     return 'Read my blog.  They\'re full of information!' 

# @app.route('/blog/2024/dogs')
# def blog2():
#     return 'Woof!  Woof!  I\'m a dog dudes!' 