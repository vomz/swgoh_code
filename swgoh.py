from flask import Flask,request,render_template,session,redirect
import pandas as pd
import numpy as np

mine=pd.read_csv('mine.csv')
mine.set_index(['Unnamed: 0'],inplace=True)
mine.index.name=None
chars=pd.read_csv('all.csv')
chars.set_index(['Unnamed: 0'],inplace=True)
chars.index.name=None


app = Flask(__name__)

@app.route('/',methods=("POST","GET"))
def character():
    return render_template('char.html')

@app.route('/gear',methods=("POST","GET"))
def gear_table():
    char=request.form.get("Character")
    g1=pd.DataFrame(chars[char][(chars.index>=1)&(chars.index<2)])
    g2=pd.DataFrame(chars[char][(chars.index>=2)&(chars.index<3)])
    g3=pd.DataFrame(chars[char][(chars.index>=3)&(chars.index<4)])
    g4=pd.DataFrame(chars[char][(chars.index>=4)&(chars.index<5)])
    g5=pd.DataFrame(chars[char][(chars.index>=5)&(chars.index<6)])
    g6=pd.DataFrame(chars[char][(chars.index>=6)&(chars.index<7)])
    g7=pd.DataFrame(chars[char][(chars.index>=7)&(chars.index<8)])
    g8=pd.DataFrame(chars[char][(chars.index>=8)&(chars.index<9)])
    g9=pd.DataFrame(chars[char][(chars.index>=9)&(chars.index<10)])
    g10=pd.DataFrame(chars[char][(chars.index>=10)&(chars.index<11)])
    g11=pd.DataFrame(chars[char][(chars.index>=11)&(chars.index<12)])
    g12=pd.DataFrame(chars[char][(chars.index>=12)&(chars.index<13)])

    return render_template('simple.html', tables=[g1.to_html(header=False),g2.to_html(header=False),g3.to_html(header=False),g4.to_html(header=False),g5.to_html(header=False),g6.to_html(header=False),g7.to_html(header=False),g8.to_html(header=False),g9.to_html(header=False),g10.to_html(header=False),g11.to_html(header=False),g12.to_html(header=False)], titles=['','Gear Level 1','Gear Level 2','Gear Level 3','Gear Level 4','Gear Level 5','Gear Level 6','Gear Level 7','Gear Level 8','Gear Level 9','Gear Level 10','Gear Level 11','Gear Level 12'], toon=char)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
