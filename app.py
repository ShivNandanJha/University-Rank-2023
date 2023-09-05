import streamlit as st
import pandas as pd
import plotly.express as px




# Sample data
df = pd.read_csv('./final dataset.csv')
df = df.drop(df.columns[0], axis=1)

st.sidebar.image('Bro_code logo.png', width=150)
st.sidebar.title('World University Rankings 2023')
# Create a Streamlit app
st.image('./university.png')
st.title('Top Ranked Universities Stats')

# Display the subheader
st.subheader('''About Dataset
The World University Rankings 2023 dataset includes 1,799 universities across 104 countries and regions, making it the largest and most diverse university rankings to date. The table is based on 13 carefully calibrated performance indicators that measure an institution's performance across four areas: teaching, research, knowledge transfer, and international outlook. This year's ranking analyzed over 121 million citations across more than 15.5 million research publications and included survey responses from 40,000 scholars globally. Overall, we collected over 680,000 datapoints from more than 2,500 institutions that submitted data.

Features:
1. University Rank
2. Name of University
3. Location
4. No of student (Present students enrolled in university)
5. No of student per staff (Students under 1 Professor)
6. International Student ( % of Total number of International Students)
7. Female : Male Ratio
8. Overall Score
9. Teaching Score
10. Research Score
11. Citations Score (CiteScore is the number of citations received by a journal in one year to documents published in the three previous years,)
12. Industry Income Score (how much money a university receives from the working industry in exchange for its academic expertise. Out of 100)
13. International Outlook Score (the ability of a university to attract undergraduates, postgraduates and faculty from all over the world)
''')

# Display the data table
st.write('### University Data')
st.dataframe(df)





# Create and display a grouped bar chart
st.write('### University Statistics')
location_trends = df.groupby('Location')['No of student'].sum().reset_index().sort_values(by='No of student', ascending=False)
custom_color_scale = [
    (0.0, 'red'),  # Low value color
    (0.5, 'yellow'),  # Mid value color
    (1.0, 'green'),
    # High value color
]
fig1 = px.scatter_geo(
    data_frame=location_trends,
    # Column containing location names
    locations='Location',
    # Set the location mode to 'country names'
    locationmode='country names',
    # Color based on the number of students
    color                  = 'No of student',
    color_continuous_scale = custom_color_scale,
    # Customize axis label
    labels={'No of student': 'Number of Students'},
    # Set the title of the plot
    title = 'Number of Students Trends by Location (Geo Map)',
    # Set the height of the plot
    height=500,
    size='No of student',
    size_max=50,
)
col1,col2= st.columns([3,3])
with col1: 
    st.dataframe(location_trends)
with col2:
     st.plotly_chart(fig1)
     
    
 
Top_10_rank = df.groupby('Name of University')['University Rank'].sum().reset_index().sort_values(by='University Rank').head(10)
custom_color = [
   2,4,6,8,10,12,14,16,18,20
]
fig2=px.bar(
    Top_10_rank,
    x      = 'Name of University',
    y      = 'University Rank',
    text   = 'University Rank',
    title  = 'Top 10 Universities by Ranking',
    labels = {'Name of University': 'University', 'University Rank': 'ranking'},
    color=custom_color,
    # height  = 700,
    barmode = 'stack',
    category_orders={'University Rank': 'category ascending'} 
)

fig2.update_layout(coloraxis_showscale=False)
st.plotly_chart(fig2)





stdnt_rank = df.sort_values(by='No of student', ascending=False).head(10)
# Create a bar chart with two columns
fig3 = px.bar(
    stdnt_rank,
    x      = 'Name of University',
    y      = ['No of student', 'No of Int Students'],
    title  = 'Top 10 Universities with most Number of Students',
    labels = {'Name of University': 'University', 'No of student': 'Number of Students', 'International Student': 'Int Student'},
    height = 700,
    barmode='group'
)

# Rotate x-axis labels for better readability
fig3.update_xaxes(tickangle=45)
# Show the plot
st.plotly_chart(fig3)


top_staff_ranking    = df.groupby("Name of University",as_index=True)['No of student per staff'].sum().reset_index().sort_values(by='No of student per staff', ascending=False).head(10)
custom_color = [
   2,4,6,8,10,12,14,16,18,20
]
fig4=px.bar(
    top_staff_ranking,
    x = 'Name of University',
    y = 'No of student per staff',

    title  = 'Top 10 Universities according number of students per Staff',
    labels = {'Name of University': 'University', 'No of student per staff': 'Staff'},
    color=custom_color,
    template='plotly'

    )
fig4.update_layout(coloraxis_showscale=False)
col1,col2= st.columns(2)
with col1: 
    st.dataframe(top_staff_ranking)
with col2: 
    st.plotly_chart(fig4)


sorted_df = df.head(10)

fig5       = px.bar(sorted_df, x='Name of University',y=['Female','Male'],
             labels={'Name of University': 'University Name', 'value': 'Number of Students'},
             title='Female:Male ratio of top 10 ranked universities', barmode="group")
st.plotly_chart(fig5)




sorted_rank = df.head(10)
fig6=px.bar(
    sorted_rank,
    x = 'Name of University',
    y = ['Research Score','Teaching Score' ,'Citations Score','Industry Income Score','International Outlook Score'],
    title    = 'Top 10 ranked Universities\' different score criteria',
    labels   = {'Name of University': 'University', 'Research Score': 'ranking'},
    height   = 700,
width=900,
    template = 'plotly',
    barmode='group'

    )
st.plotly_chart(fig6)




st.sidebar.markdown(
    """
    <div style = "position: absolute; display:flex; top:250px;">
    <a   href  = "https://www.datascienceportfol.io/brocode_shivnandan" target                                      = "_blank">
    <img src   = "https://portfolio-shivi.netlify.app/assets/man-3224c7f9.png" width = 60 />
    </a>
    <p style = "font-size: 15px; color: #3aff13;">Bro_CODE <br  style="margin-top:0;"/>Shivnandan Jha</p>   </div>
    <div style = "position: absolute; display:flex; gap:20px; top:300px;  margin-left:21px;">
    <a   href  = "https://www.linkedin.com/in/shiv-nandan-jha-4179a4251" target                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               = "_blank">
    <img src   = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFwAAABcCAMAAADUMSJqAAAAYFBMVEUAd7f///8AcbQAdbYAa7KXu9nP4O3M3OsAc7Xl7/YAbrOQttdzpc5MjcH0+fuuyOBnnMkog73s9Pm0zeN9rNK80+aIsdQAaLFYlcbc5vGfv9s/icDF2uode7kof7sAYq7hDdldAAACZklEQVRoge2a27KjIBBF5RKDreL9njj//5djkokjIIZTaR5OlbsqDwFdhW2zG0ICskhmeREgqsgz+eAGy6cKQDBMOBMQVC94yzHBb/H2Aa+8sBd6RQLpB/2QDDLwxYYsyIUvuMiDAjVPtmKo6e0gARyAUx8PJLo+G6JoGKcOHQ99RP4pLCgum1/IRjlqloLCXuiIYxc90XTHg9NIhzdovsNynU3IjJUyUJnwGivqnRGVpY5gJUwnTfjtd8AHE47m9pCZ8ATrhYrUhOPNIjDiglgDxaSxJaarQ63CU9T6Csl23BOyodPiusb7jr4uYHyOmzCsauFnPUOBc/BSoL2KbfShlT0fcZHjczKY0lUFsDfFbF3Ic5uFUSllOTSX1IF/Vyz99kpFNit2GT42CpTFqvuX4/whA3TrSp7JCI3aWlPGk9L0oQscDp5ftcufQ+eh2hrTvYK4aDicGY7wP7dd9hIbdjB2N3i74/vvsR9s3Nzg2ldFmX2h4wY/VG8NOwI8tCYkApxMtqhjwK2VEQMuO49wa1x+AC8v/TT1444LtJbi6A6PORWMCdqNRldjCbozvF7nCr/ofYNlHrnCt/Ow03ttBuMK3zqIsZGS81cjV1KZGTspS7o4wtW79VpC0m/gpeqrtNXgFu9yg1/VXBOJ2k0sv+C4wTX3MN5o8g08Vqcg0/cMJ/yEn/ATfsJP+Ak/4S+4tjVGhesrs9fCjI57rf/hQoPb9i0wRhu9f2uFatva6jsHkQ57d+3Qga7i61WbRgrmveJDvyd5PfjzemTp9bDV3zExk34PuP0ezRNSMX9/KvD3d4i/QB8pnxFRoRMAAAAASUVORK5CYII=" alt = "LinkedIn", width = 30/>
    </a>
     <a   href = "https://github.com/ShivNandanJha" target                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               = "_blank">
<img src="data:image/png;base64,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", width=30/>
    </a>
    </div>
   
    """,
    unsafe_allow_html=True,
)
hide_streamlit_style = """
            <style>
             footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("Made with `♥`  by `Bro_CODE` Shivnandan Jha")