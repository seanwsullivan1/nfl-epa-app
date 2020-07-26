# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:16:49 2020

@author: Sean Sullivan
"""

import streamlit as st
import pandas as pd


#Load data
df = pd.read_csv('nfl - cleaned.csv')

st.title('Expected Points Added Calculator Tool')


st.write("""
Quickly calculate EPA and a 4th down "go for it" confidence calculation for your armchair analysis! 
""")
st.write('')
st.write("""
How to use:
Enter the previous and next play down, yards to go, and yardline to calculate the Expected Points Added.
""")


st.subheader('Expected Points Added Calculator (EPA)')  
#down1 = st.number_input('Enter the previous down:')
down1 = st.slider('Previous down', 1, 4)
togo1 = st.number_input('Enter the previous yards to go for first down:')
yardline1 = st.number_input('Enter the previous yardline:')
#yardline1 = st.slider('Previous Yardline', 0, 50)
side_of_field1 = st.selectbox(
        'Side of the field', 
        ('Own', 'Opponent')
)

st.write('')
st.write('')

#down2 = st.number_input('Enter the new down:')
down2 = st.slider('Next down', 1, 4)
togo2 = st.number_input('Enter the new yards to go for first down:')
yardline2 = st.number_input('Enter the new yardline:')
#yardline2 = st.slider('New Yardline', 0, 50)
side_of_field2 = st.selectbox(
        'New side of the field', 
        ('Own', 'Opponent')
)


if side_of_field1 == 'Opponent':
    yardline1 = 100 - yardline1
else:
    yardline1

if side_of_field2 == 'Opponent':
    yardline2 = 100 - yardline2
else:
    yardline2 
    

ep1 =  df.loc[((df['Down'] == down1) & (df['ToGo'] == togo1) & (df['YardLine'] == yardline1))].values[0][3]
ep2 = df.loc[((df['Down'] == down2) & (df['ToGo'] == togo2) & (df['YardLine'] == yardline2))].values[0][3]


if st.button('Calculate Expected Points Added!'):
    
    epa = ep2 - ep1
    st.write('The Previous Expected Points:', round(ep1,2))
    st.write('The Current Expected Points:', round(ep2,2))
    st.write('The Expected Points Added is:', round(epa,2))


st.write('')
st.write('')
st.write('')
st.write('')



#Now for the Confidence Calculator
st.subheader('4th Down "Go For It" Confidence Calculator') 
st.write('Enter the safe option, likely failed outcome, and minimum successful outcome to generate the % of how confident you would need to be to go for it!')

safe = st.number_input('Expected Points for safe option:')
gamble_f = st.number_input('Expected Points for most likely failed outcome:')
gamble_s = st.number_input('Expected Points for minimum successful outcome:')

safe, gamble_f, gamble_s = safe, gamble_f, gamble_s
#safe, gamble_f, gamble_s = -0.3, -1.5, 2.7

def confidence_calculator(safe, gamble_f, gamble_s):
    '''Takes safe bet, gamble failed outcome, gamble success outcome
    and determines % of confidence needed to go for the successful gamble'''
    
    denom = gamble_s + (-1*gamble_f)
    
    if gamble_f <= 0:
        numer = safe + (-1*gamble_f)
        
    if gamble_f >= 0:
        numer = safe - gamble_f
    
    if denom == 0:
        return('Enter some values to produce a confidence calculation!')
    else:
        percentage = numer/denom
    
    return(percentage)

conf = confidence_calculator(safe, gamble_f, gamble_s)
   
try:
    st.write('The confidence calculated is (%):', round(conf*100,2))
except TypeError:
    print('Enter some values to produce a confidence caluclation!')
















