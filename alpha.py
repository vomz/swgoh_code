from flask import Flask,request,render_template,session,redirect
import pandas as pd
import numpy as np

mine=pd.read_csv('mine.csv')
chars=pd.read_csv('all.csv')
char='Jedi Master Luke Skywalker'
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

print(g1)
