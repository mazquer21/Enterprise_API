from flask import Blueprint, render_template,request,redirect,url_for
from datetime import date
import requests

api1 = requests.get("https://covid19.th-stat.com/api/open/today")
api2 = requests.get("https://covid19.th-stat.com/api/open/timeline")

data_api1 = api1.json()
data_api2 = api2.json()

views = Blueprint('views', __name__)

@views.route('/',methods=['GET', 'POST'])
def index():
     if request.method == 'POST':
          Getdate = request.form.get('selectedDate')
          day = Getdate[8:10]
          month =  Getdate[5:7]
          year =  Getdate[0:4]
          date0 = month+"/"+day+"/"+year
          return redirect(url_for('views.timeline',Date = date0))

     return render_template("index.html")
                    

@views.route('/today',methods=['GET', 'POST'])
def today():
     temp = data_api1['UpdateDate']
     Date = temp[0:10]
     return render_template("today.html",data = data_api1,Date = Date)
          

@views.route('/timeline',methods=['GET', 'POST'])
def timeline():
     url = request.values
     date = url['Date']
     day = date[3:5]+"/"+date[0:2]+"/"+date[6:10]
     for _all in data_api2['Data']:
          if _all['Date'] == date:
               timeline_data = _all              
               return render_template("timeline.html",data = timeline_data,Date = day)
     return render_template("index.html")