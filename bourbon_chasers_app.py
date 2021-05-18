### Strava Competition -- Streamlit ### 
### Author: Steven Carter

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import warnings 
from IPython.display import display
import altair as alt
import pandas_profiling as pf
import streamlit.components.v1 as components
from streamlit_pandas_profiling import st_profile_report
import sweetviz as sv
import openpyxl
import sys
from streamlit import cli as stcli

st.set_page_config(
     page_title='Bourbon Chasers: STRAVA Competition',
     layout="wide"
    )

st.sidebar.title("Bourbon Chasers Hub")
select = st.sidebar.selectbox('Navigate the options below:', ["Home", "STRAVA Competition Rules","FAQs","Zone Times to Points Conversion", "Weekly & Overall Leaderboard", "Pictures", "Inspiration"])
if select == "Home":
    st.image(image= 'bc_home logo.png', use_column_width=True)
    st.image(image= 'bc2.png', use_column_width=False)
    st.write("""## Welcome all Bourbon Chasers!""")
    st.write("""How the Bourbon Chasers Application Works: """)
    st.info("""
        * Use the drop-down menu on the left side to navigate throughout the app.
        * View the rules of the competition & FAQs.
        * After your work-out, enter your times for a quick check at how many points you earned.
        * View the Weekly & Overall Leaderboard.
        * Not feeling motivated? Click on the 'Inspiration' tab to feel the wash of motivation!
    """)

elif select == "STRAVA Competition Rules":
    st.image(image= 'Strava rules_logo.png', use_column_width=True)
    st.subheader("The rules have been decreed as follows:")
    st.write(""" Competition Timeframe: May 1st 0000 - July 10th 2359""")
    st.write("""Exercises can be any kind but the intent must be to workout/train. AKA: Leisurely dog walk with the Mrs or bike ride with the kids wouldn't count. Any exercise can be vetoed by the group with a simple majority rules. 
    So keep your underwater basketweaving off Strava.""")
    st.write("""Scoring will be based on STRAVA defined heart rate zones. CAUTION: If using another heart rate monitor
    make sure the hr zones resemble the STRAVA defined hr zones. If there are issues with seeing the zones 
    it is most likely a watch setting that needs to be enabled.""")
    st.image(image= 'rules_example.png')

elif select == "FAQs":
    st.image(image= 'faq_logo.png', use_column_width=True)
    st.subheader('1. Am I man enough to be a Bourbon Chaser?')
    st.write('#### A. No')
    st.text("")
    st.subheader('2. Do I have any chance of winning the competition?')
    st.write('#### A. No')
    st.text("")
    st.subheader('3. If I cannot win, why I am even doing this?')
    st.write('#### A. To become a Spartan Warrior')
    st.text("")
    st.subheader('4. What is the difference between Spartan Warriors & Bourbon Chasers?')
    st.write('#### A. Nothing')

elif select == "Zone Times to Points Conversion":
    st.image(image= 'convert_times_logo.png', use_column_width=True)
    st.write('#### NOTE: Before entering your time, make sure to round up or down to the whole number.')
    st.write("""""")
    st.write("""""")
    z1number = st.number_input('Enter HR Zone 1 Time (x 1 multiplier):')
    st.write('### Your Zone 1 Points are: ', z1number)
    st.write("""""")
    st.write("""""")
    z2number = st.number_input('Enter HR Zone 2 Time (x 1.2 multiplier):')
    st.write('### Your Zone 2 Points are: ', z2number*1.2)
    st.write("""""")
    st.write("""""")
    z3number = st.number_input('Enter HR Zone 3 Time (x 1.5 multiplier):')
    st.write('### Your Zone 3 Points are: ', z2number*1.5)
    st.write("""""")
    st.write("""""")
    z4number = st.number_input('Enter HR Zone 4 Time (x 2 multiplier):')
    st.write('### Your Zone 4 Points are: ', z2number*2)
    st.write("""""")
    st.write("""""")
    z5number = st.number_input('Enter HR Zone 5 Time (x 3 multiplier):')
    st.write('### Your Zone 5 Points are: ', z2number*3)
    st.write("""""")
    st.write("""""")
    st.write('## Your **Total Points** for this activity are : ', z1number+z2number+z3number+z4number+z5number)
    
elif select == "Weekly & Overall Leaderboard":
    st.image(image= 'scoreboard_logo.png', use_column_width=True)
    st.subheader('Weekly Leaderboard')

    # Weekly data
    week_df = pd.read_excel('Master_comp.xlsx')
    week_df
    fig = px.bar(
        data_frame = week_df,
        x = "Athletes",
        y = "Week 2 -- May 9 - 15",
        title = "<b>Week 2 Leaderboard Barchart</b>"
    )
    st.plotly_chart(fig)

    # Overall Leaderboard
    st.subheader('Overall Leaderboard')
    overall_df = pd.read_excel('Master_comp1.xlsx')
    overall_df
    fig = px.bar(
        data_frame = overall_df,
        x = "Athletes",
        y = "Total Points",
        title = "<b>Overall Leaderboard Barchart</b>"
    )
    st.plotly_chart(fig)

elif select == "Pictures":
    st.image(image= 'pictures_logo.png', use_column_width=False)

elif select == "Inspiration":
    st.image(image= 'inspiration_logo.png', use_column_width=False)
    st.write('#### Your future if you win.....')
    st.image(image= '2.jpg', use_column_width=False)
    st.write("""""")
    st.write("""""")
    

