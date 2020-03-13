from flask import Flask
from flask import render_template,request,send_file
import model as mp
import pandas as pd


app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template("index.html",out="")

@app.route("/test",methods=["GET","POST"])
def test():
    if (request.method == "POST"):
        val = list(request.form.values())
        _input_ = [eval(i) for i in val]
        print(_input_)
        output = mp.f_model(_input_)
        # rp.reporter(_input_)
        df = pd.DataFrame()
        df['Field'] = ['age', 'bp', 'sg', 'al', 'su', 'rbc_normal', 'pc_normal', 'pcc_present','ba_present', 'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wc', 'rc', 'htn_yes', 'dm_yes', 'cad_yes', 'appet_poor', 'pe_yes', 'ane_yes']
        df['Response'] = _input_
        # df.to_csv("static/data/report.csv",index = False)
        df.to_excel(r'static/data/report.xlsx', index = False)
        print("______DONE_____")
        
        return render_template("index.html",out=output,msgg="")
    else:
        return render_template("index.html",out="",msgg="")

# @app.route("/report")
# def report_():
#     return send_file("static/data/report.xlsx")

@app.route("/report")
def reportt():
    return render_template('report.html')



if __name__ == "__main__":
    app.run(host='0,0,0,0',port=8080)
