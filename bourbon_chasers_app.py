### Strava Competition -- Streamlit ### 
### Author: Steven Carter

from typing import Container
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
import statistics
from statistics import mean

st.set_page_config(
     page_title='Bourbon Chasers: STRAVA Competition',
     layout="wide"
    )

st.sidebar.title("Bourbon Chasers Hub")
select = st.sidebar.selectbox('Navigate the options below:', ["Home", "STRAVA Competition Rules","FAQs","Zone Times to Points Conversion", "Weekly & Overall Leaderboard", "Pictures", "Inspiration"])

if select == "Home":
    st.image(image= 'bc_home logo.png', use_column_width=True)
    col1, col2 = st.beta_columns(2)
    col1.image(image= 'bc2.png', use_column_width=True)
    
    col2.markdown("""# Welcome all Bourbon Chasers!""")
    col2.write("""How the Bourbon Chasers Application Works: """)
    col2.info("""
        * Use the drop-down menu on the left side to navigate throughout the app.
        * View the rules of the competition & FAQs.
        * After your work-out, enter your times for a quick check at how many points you earned.
        * View the Weekly & Overall Leaderboard.
        * Check out Bourbon Chasers pictures from previous events!
        * Not feeling motivated? Click on the 'Inspiration' tab to feel the wash of motivation!
    """)

elif select == "STRAVA Competition Rules":
    st.image(image= 'Strava rules_logo.png', use_column_width=True)
    st.subheader("The rules have been decreed as follows:")
    st.write(""" Competition Timeframe: **May 1st (0000) - July 10th (2359)**""")
    st.write("""Exercises can be any kind but the intent must be to **workout/train**. For example: 
    Leisurely dog walk with the Mrs or bike ride with the kids wouldn't count. Any exercise can be 
    vetoed by the group with a simple majority rules. So keep your underwater basketweaving off Strava.""")
    st.write("""Scoring will be based on STRAVA defined heart rate zones. **CAUTION:** If using another heart rate monitor
    make sure the hr zones resemble the STRAVA defined hr zones. If there are issues with seeing the zones 
    it is most likely a watch setting that needs to be enabled. Additionally if you capture your hr zones 
    using another tool or app other than STRAVA, the group has decided to average the hr and use that
    zone's multiplier.""")
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
    st.text("")
    st.subheader('5. What should I do if I do not want to workout?')
    st.write('#### A. Schedule naval piercing.')
    st.text("")
    st.subheader('6. What will I look like with a belly button piercing?')
    st.write('#### A. ')
    st.text("")
    st.image(image= 'piercing.jpg', use_column_width=False)

elif select == "Zone Times to Points Conversion":
    st.image(image= 'convert_times_logo.png', use_column_width=True)
    st.write('#### NOTE: Before entering your time, make sure to round up or down to the whole number.')
    st.write("""""")
    st.write("""""")
    z1number = st.number_input('Enter HR Zone 1 Time (x 1 multiplier):')
    z1_total = z1number
    st.write('### Your Zone 1 Points are: ', z1_total)
    st.write("""""")
    st.write("""""")
    z2number = st.number_input('Enter HR Zone 2 Time (x 1.2 multiplier):')
    z2_total = z2number*1.2
    st.write('### Your Zone 2 Points are: ', z2_total)
    st.write("""""")
    st.write("""""")
    z3number = st.number_input('Enter HR Zone 3 Time (x 1.5 multiplier):')
    z3_total = z3number*1.5
    st.write('### Your Zone 3 Points are: ', z3_total)
    st.write("""""")
    st.write("""""")
    z4number = st.number_input('Enter HR Zone 4 Time (x 2 multiplier):')
    z4_total = z4number*2
    st.write('### Your Zone 4 Points are: ', z4_total)
    st.write("""""")
    st.write("""""")
    z5number = st.number_input('Enter HR Zone 5 Time (x 3 multiplier):')
    z5_total = z5number*3
    st.write('### Your Zone 5 Points are: ', z5_total)
    st.write("""""")
    st.write("""""")
    st.write('## Your **Total Points** for this activity are : ', z1_total+z2_total+z3_total+z4_total+z5_total)
    
elif select == "Weekly & Overall Leaderboard":
    st.image(image= 'scoreboard_logo.png', use_column_width=True)
    st.subheader('Weekly Leaderboard')

    # Weekly data
    week_df = pd.read_excel('Master_comp.xlsx')
    week_df
    fig = px.bar(
        data_frame = week_df,
        x = "Athletes",
        y = "Week 10 -- July 4 - 10"
    )
    fig.update_layout(
    title={
        'text': "<b> Week 10 Leaderboard </b>",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    st.plotly_chart(fig)

    col1, col2 = st.beta_columns(2)

    # Overall Leaderboard
    col1.subheader('Overall Points')
    overall_df = pd.read_excel('Master_comp1.xlsx')
    col1.write(overall_df)
    fig = px.bar(
        data_frame = overall_df,
        x = "Athletes",
        y = "Total Points"
    )
    fig.update_layout(
    title={
        'text': "<b> Overall Leaderboard </b>",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    col2.plotly_chart(fig)

    col1, col2 = st.beta_columns(2)
    col1.subheader('More Stats:')
    col1.write('#### Weekly Points Average Among the Bourbon Chasers')
    col1.write(week_df.mean())

    week_df_indexmod = week_df.set_index([pd.Index([1,2,3,4,5,6,7,8,9,10])])
    fig = px.scatter(
        data_frame = week_df_indexmod,
        y = week_df_indexmod.mean(),
        labels = {
            "y" : "Weekly Points Average",
            "index" : "Weeks 1 - 10"
        },
        title = "<b> Bourbon Chaser Points -- Weekly Average </b>"
    )
    col2.plotly_chart(fig)

    # Compare each athlete
    # Create a list of possible values and multiselect menu with them in it
    st.subheader('Athlete Weekly Comparison')
    st.write('#### Are you leaning towards Whisky Tumbler or Belly-Button Piercing?')
    athletes = week_df['Athletes'].unique()
    athletes_selected = st.multiselect('Select the Bourbon Chasers to compare:', athletes)

    # Mask to filter dataframe
    mask_athletes = week_df['Athletes'].isin(athletes_selected)
    week_df1 = week_df[mask_athletes]
    week_df1
        
elif select == "Pictures":
    st.image(image= 'pictures_logo.png', use_column_width=False)
    col1, col2 = st.beta_columns(2)
    col1.image(image= 'tri_pic.png', use_column_width=True)
    col2.image(image= 'tri1.png', use_column_width=True)
    col2.image(image= 'tri2.png', use_column_width=True)
    col1.image(image= 'tri3.png', use_column_width=True)
    col1.image(image= 'tri4.jpg', use_column_width=True)
    col2.image(image= 'tri5.jpg', use_column_width=False)
    col1.image(image= 'tri6.jpg', use_column_width=True)
    col2.image(image= 'tri7.jpg', use_column_width=True)
    col2.image(image= 'tri8.jpg', use_column_width=True)
    col2.image(image= 'tri9.jpg', use_column_width=True)
    col1.image(image= 'af_logo.png', use_column_width=True)
    col2.image(image= 'af1.jpg', use_column_width=True)
    col1.write('#### Look at that Mile 26 form! What a boss Todd!!')
    col1.video('toddrun.mp4', start_time=0)
    col2.image(image= 'af2.jpg', use_column_width=True)
    col1.image(image= 'af3.jpg', use_column_width=True)
    col1.image(image= 'af4.jpg', use_column_width=True)
    col2.image(image= 'af5.jpg', use_column_width=True)
    col1.image(image= 'af6.jpg', use_column_width=True)
    st.subheader('More pics on the way!!')

elif select == "Inspiration":
    st.image(image= 'inspiration_logo.png', use_column_width=False)
    st.image(image= '2.jpg', use_column_width=True)
    
    

