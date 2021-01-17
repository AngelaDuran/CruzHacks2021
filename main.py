import json, time
import pyrebase
from flask import Flask, render_template, request 
app = Flask(__name__)

firebaseConfig = {
    "apiKey": "AIzaSyBcAcwWpcQPsGUzKfhtgeF0Io7lfWJ2n0U",
    "authDomain": "webtest-ba543.firebaseapp.com",
    "databaseURL": "https://webtest-ba543-default-rtdb.firebaseio.com",
    "projectId": "webtest-ba543",
    "storageBucket": "webtest-ba543.appspot.com",
    "messagingSenderId": "117806514902",
    "appId": "1:117806514902:web:fa40ed51bb3f5b4f297f77",
    "measurementId": "G-DETW1MTKNP"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db=firebase.database()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/inputbusiness')
def inputbusiness():
  return render_template('inputbusiness.html')
place =''
@app.route('/businessmode')
def businessmode():
  # name = db.child('name').get()
  # name1=repr(name.key())
  # name1 = 000
  datacur = db.child('RECENTB').child("Company").get().val()
  print("this: "+ datacur)
  name1= datacur
  return render_template('businessmode.html', name1=name1)

@app.route('/submitted', methods=['POST'])
def distanceSubmitted():
  data = request.data.decode()
  data_list = data.split(',')
  company = data_list[0]
  occupants = int(data_list[1])
  print(company)
  print(occupants)
  print("success")

  #Angela Added 2:03 AM
  store_data = {"Current Occupancy": occupants}
  db.child(company).set(store_data)

  #Will always contain most recently added company info
  db.child('RECENTB').update({"Occupants": occupants })
  db.child('RECENTB').update({"Company": company })

  # store_data = {"Company name": company}
  # db.child(company).set(occupants)
  time.sleep(5)
  print("Changes saved...")
  #company name and initial # of occupants in firebase
  return data


app.run('0.0.0.0',8080)



