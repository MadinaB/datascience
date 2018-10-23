import csv
import matplotlib
import json
from flask import Flask, request, render_template
app = Flask(__name__)


def get_friends():
    with open('Somerville_High_School_YRBS_Raw_Data_2002-2016.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = -1
        friends = {}
        friends_index = 0
        for row in csv_reader:
            if line_count == -1:
                for index, quality in enumerate(row):
                    if quality =='friends':
                        friends_index = index
                    line_count += 1
                else:
                    type_of_friends = row[friends_index]
                    if not type_of_friends in friends:
                        friends[type_of_friends] = 0
                    friends[type_of_friends]+=1
        return friends


def get_genders():
    with open('Somerville_High_School_YRBS_Raw_Data_2002-2016.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = -1
        genders = {}
        genders_index = 0
        friends_index = 0
        for row in csv_reader:
            if line_count == -1:
                for index, quality in enumerate(row):
                    if quality =='gender':
                        genders_index = index
                    if quality =='friends':
                        friends_index = index
                    line_count += 1
            else:
                type_of_gender = row[genders_index]
                has_friends = row[friends_index]
                if not type_of_gender in genders:
                    genders[type_of_gender] = {}
                if not has_friends in genders[type_of_gender]:
                    genders[type_of_gender][has_friends] = 0
                genders[type_of_gender][has_friends] +=1
    return genders

def get_races():
    with open('Somerville_High_School_YRBS_Raw_Data_2002-2016.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = -1
        races = {}
        races_index = 0
        friends_index = 0
        for row in csv_reader:
            if line_count == -1:
                for index, quality in enumerate(row):
                    if quality =='race':
                        races_index = index
                    if quality =='friends':
                        friends_index = index
                    line_count += 1
            else:
                type_of_race = row[races_index]
                has_friends = row[friends_index]
                if not type_of_race in races:
                    races[type_of_race] = {}
                if not has_friends in races[type_of_race]:
                    races[type_of_race][has_friends] = 0
                races[type_of_race][has_friends] +=1
        return races


def show_genders_text(genders):
    for gender in genders:
        for type_of_friends in genders[gender]:
            print 'There are ', genders[gender][type_of_friends],' ',gender, ' people who have ', type_of_friends,' friends.'

def show_races_text(races):
    for race in races:
        for type_of_friends in races[race]:
             'There are ', races[race][type_of_friends],' ',race, ' people who have ', type_of_friends,' friends.'




@app.route('/')
def main():
    friends = get_friends()
    genders = get_genders()
    races = get_races()
    groups ={}
    
    show_genders_text(genders)
    show_races_text(races)
    dic ={'a': 10, 'b':20}
    return render_template("index.html", genders=genders,races=races, groups=groups )

@app.route('/handle_data', methods=['POST'])
def handle_data(genders,races):
    projectpath = request.form['projectFilepath']
    
    return render_template("index.html", genders=genders,races=races, groups=groups )

if __name__ == '__main__':
    app.secret_key = 'some_data'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)

