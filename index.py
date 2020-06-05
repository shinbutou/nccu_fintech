from flask import Flask, redirect, url_for, render_template, request
import json
import pandas as pd

app = Flask(__name__)
class Dstore():
    user = None
D = Dstore()

@app.route("/")
def main():
    return render_template('login.html')

@app.route("/login.html", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        global user
        user = request.values['usr']
        pwd = request.values['pwd']
        with open(f'./schema/Info.json', 'r') as json_file:
            data = json.load(json_file)
        if user not in data.keys():
            data.update({user:{}})
        with open(f'./schema/Info.json', 'w') as json_file:
            json.dump(data, json_file)
            json_file.close()
            
        default_year = '05/01/2020'
        top_news_1 = get_top_news(default_year, 1)
        top_news_2 = get_top_news(default_year, 2)
        top_news_3 = get_top_news(default_year, 3)
        return render_template("main.html",
                               top_news_list_1 = top_news_1,
                               top_news_list_2 = top_news_2,
                               top_news_list_3 = top_news_3,
                               stock_name='apple',
                               return_data= [1,2,3]
                               )
    
        
@app.route("/main.html", methods=["POST", "GET"])
def op():
    if request.method == "POST":
        year = request.values['datepicker']
        portfolio = request.values['portfolio']
        keyword = request.values['ikeyword']
        with open(f'./schema/Info.json', 'r') as json_file:
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
        with open(f'./schema/Info.json', 'w') as json_file:
           json.dump(data, json_file)
        
        
        top_news_1 = get_top_news(year, 1);top_news_2 = get_top_news(year, 2);top_news_3 = get_top_news(year, 3)

        return render_template("main.html",
                               top_news_list_1 = top_news_1,
                               top_news_list_2 = top_news_2,
                               top_news_list_3 = top_news_3
                               )

def get_top_news(which_year,num):
    which_year = pd.to_datetime(which_year).strftime('%Y-%m-%d')
    with open(f'./uidata/news/{which_year}_{num}.json')as f:
        news = json.load(f)
    return news


    
if __name__ == "__main__":
    app.run()