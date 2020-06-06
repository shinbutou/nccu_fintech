from flask import Flask, redirect, url_for, render_template, request
import json
import pandas as pd

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('login.html')

@app.route("/login.html", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        global user
        user = request.values['usr']
        pwd = request.values['pwd']
        with open(f'./Schema/Info.json', 'r') as json_file:
            data = json.load(json_file)
        if user not in data.keys():
            data.update({user:{}})
        with open(f'./Schema/Info.json', 'w') as json_file:
            json.dump(data, json_file)
            json_file.close()
            
        default_year = '05/01/2020'
        key1,top_news_1 = get_top_news(default_year, 1)
        key2,top_news_2 = get_top_news(default_year, 2)
        key3,top_news_3 = get_top_news(default_year, 3)
        return render_template("main.html",
                               key1 = key1,
                               top_news_list_1 = top_news_1,
                               key2 = key2,
                               top_news_list_2 = top_news_2,
                               key3 = key3,
                               top_news_list_3 = top_news_3,
                               )
    
        
@app.route("/main.html", methods=["POST", "GET"])
def op():
    if request.method == "POST":
        year = request.values['datepicker']
        portfolio = request.values['portfolio']
        keyword = request.values['ikeyword']
        with open(f'./Schema/Info.json', 'r') as json_file:
           data = json.load(json_file)
        int = 0
        try:
            while str(int) in data[user].keys():
                int = int + 1
        except:
            return render_template('login.html')
        data[user].update({int : {"date" : year,
                                    "pf" : portfolio,
                                    "kw" : keyword }})
        with open(f'./Schema/Info.json', 'w') as json_file:
           json.dump(data, json_file)
        
        
        top_news_1 = get_top_news(year, 1);top_news_2 = get_top_news(year, 2);top_news_3 = get_top_news(year, 3)

        return render_template("main.html",
                               top_news_list_1 = top_news_1,
                               top_news_list_2 = top_news_2,
                               top_news_list_3 = top_news_3
                               )

def get_top_news(which_year,num):
    which_year = pd.to_datetime(which_year).strftime('%Y-%m-%d')
    with open(f'./UIData/news/{which_year}_{num}.json')as f:
        file = json.load(f)
        key = file[0]
        news = file[1:]
    return key,news
@app.route("/log/create-entry", methods=["POST"])
def create_entry():
    req = request.get_json()
    print(req)
    with open(f'Info.json', 'r') as json_file:
        data = json.load(json_file)
    int = 0
    try:
        while str(int) in data[user].keys():
            int = int + 1
    except:
        return render_template('login.html')
    data[user].update({int: {"date": "",
                             "pf": "",
                             "kw": "",
                             "clc": {"url": req['url'], "title" : req['title'], "tab": req['tab']}}})
    with open(f'Info.json', 'w') as json_file:
        json.dump(data, json_file)
        json_file.close()
    res = make_response(jsonify({"message": "OK"}), 200)

    return res

    
if __name__ == "__main__":
    app.run()
    