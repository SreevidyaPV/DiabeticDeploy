#importing the lib
from flask import Flask, render_template,request
import joblib
app = Flask(__name__)

#load the model
model = joblib.load('model/diabetic_80.pkl')
@app.route('/')
def home():
    return render_template('home.html')
# @app.route('/images')
# def images():
#     return 'this is the image'
# @app.route('/contacts')
# def contacts():
#     return 'this is my contact'
# @app.route('/aboutus')
# def aboutus():
#     return 'this is about us'
#@app.route('/data', methods=['post'])
#def data():
 #   return 'data received'

# @app.route('/data', methods=['post'])
# def data():
#     firstname = request.form.get('first_name')
#     secondname = request.form.get('second_name')
#     phonenumber = request.form.get('phone_number')
#     email = request.form.get('email')

#     print(firstname , secondname, phonenumber, email)
#     return 'data received'
    #return render_template('test.html')
@app.route('/data', methods=['post'])
def data():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    print(type(preg))
    result = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])

    if result[0]==1:

        data = 'person is diabatic'
    else:
        data = 'person is not diabatic'

    print(data)
    
    # return 'data received'
    return render_template('predict.html',data=data)

app.run(debug=True) #should be always at the end