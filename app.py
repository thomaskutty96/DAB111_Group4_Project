from flask import Flask, render_template
import sqlite3
import pathlib 

base_path = pathlib.Path(r'C:\Users\sachi\OneDrive\Documents\group_project')
db_name = "coviddata.db"
db_path = base_path / db_name
print(db_path)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    coviddata = cursor.execute("SELECT * FROM covid_data_table limit 20").fetchall()
    con.close()

    return render_template("data_table.html", coviddata=coviddata)

if __name__=="__main__":
    app.run(debug=True)
