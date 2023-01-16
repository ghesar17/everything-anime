from flask import Blueprint,render_template, jsonify, request, redirect, url_for
from data import getAnime

# all routes in this file using a blueprint

views = Blueprint(__name__,"views")

@views.route("/",methods=['GET','POST'])
def home():
    if request.method == 'POST':
        year = request.form['year']
        season = request.form['season'].upper()
        dict = getAnime(season,year)
        return render_template('anime.html',anime=dict)
    return render_template('index.html')

# @views.route('/anime',methods=['POST','GET'])
# def anime():
#     if request.method == 'POST':
#         year = request.form['year']
#         season = request.form['season'].upper()
#         dict = getAnime(year,season)
#         return render_template('anime.html',anime=dict)
        



@views.route('/json') #adding another slash at the end of '/json' makes it so both /json and /json/ work 
def get_json():
    return jsonify([1,2,3])

@views.route('/data')
def get_data():
    data = request.json
    return jsonify(data)

@views.route('/go-to-home')
def go_to_home():
    return redirect(url_for('views.home'))