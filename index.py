from flask import Flask, redirect, url_for, render_template, request
import json
import pandas as pd

app = Flask(__name__)
method_list = {'pph_1':'news_PortfolioList_AbovePositive5',
               'pph_2':'news_PortfolioList_BelowNegative5',
               'pph_3':'news_PortfolioList_WeekAbovePositive10',
               'pph_4':'news_PortfolioList_WeekBelowNegative10'
               }
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
            
        default_year = '05/06/2020'
        selected = {'pph_1':'selected','pph_2':'','pph_3':'','pph_4':''}
        default_method = 'pph_1'
        key1,top_news_1 = get_top_news(default_year, 1,'')
        key2,top_news_2 = get_top_news(default_year, 2,'')
        key3,top_news_3 = get_top_news(default_year, 3,'')
        portfolio_list,portfolio_news = get_portfolio_news(default_year,default_method)
        return render_template("main.html",
                               date = default_year,
                               selected = selected,
                               portfolio = portfolio_list,
                               portfolio_news = portfolio_news,
                               keyword = '',
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
        keyword = request.form['ikeyword']
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
        selected = {'pph_1':'','pph_2':'','pph_3':'','pph_4':''}
        selected[portfolio]='selected'
        date = pd.to_datetime(year).strftime('%m/%d/%Y')
        key1,top_news_1 = get_top_news(year, 1,keyword)
        key2,top_news_2 = get_top_news(year, 2,keyword)
        key3,top_news_3 = get_top_news(year, 3,keyword)
        portfolio_list,portfolio_news = get_portfolio_news(year,portfolio)
        return render_template("main.html",
                               date = date,
                               selected = selected,
                               portfolio = portfolio_list,
                               portfolio_news = portfolio_news,
                               keyword = keyword,
                               key1 = key1,
                               top_news_list_1 = top_news_1,
                               key2 = key2,
                               top_news_list_2 = top_news_2,
                               key3 = key3,
                               top_news_list_3 = top_news_3,
                               )

def get_top_news(which_day,num,keyword):
    which_day = pd.to_datetime(which_day).strftime('%Y%m%d')
    with open(f'./UIData/news/{which_day}_{num}.json')as f:
        file = json.load(f)
        key = file[0]
        news = file[1:]
    if keyword != '':
        keyword = keyword.upper()
        choose = []
        for i in news:
            title = i['title'].upper().split()
            if keyword in title:
                choose.append(i)
        news = choose
    return key,news
            
def get_portfolio_news(which_day,method):
    which_day = pd.to_datetime(which_day).strftime('%Y%m%d')
    method = method_list[method]
    try:
        with open(f'./UIData/news/{method}_{which_day}.json')as f:
            file = json.load(f)
        if len(file)>1:
            portfolio = file[0]
            news = file[1:]
        else :
            portfolio = file[0]
            news = [{'title':'No news recently'}]
        return portfolio,news
    except:
        portfolio = ['no stocks choosed by this method on this date']
        news = [{'title':'no stocks choosed by this method on this date'}]
        return portfolio,news
    
@app.route("/log/create-entry", methods=["POST"])
def create_entry():
    req = request.get_json()
    print(req)
    with open(f'./schema/Info.json', 'r') as json_file:
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
    with open(f'./schema/Info.json', 'w') as json_file:
        json.dump(data, json_file)
        json_file.close()
    res = make_response(jsonify({"message": "OK"}), 200)

    return res

    
if __name__ == "__main__":
    app.run()
    