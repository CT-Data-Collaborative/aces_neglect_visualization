import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd 
import chart_studio.tools as tls
import chart_studio.plotly as py

#hide the plotly logo
config = {'displaylogo': False}

#Create Dataframe for the visuals
df = pd.DataFrame({
                   "data_values":[10.4, 4.4, 15, 13.6, 7.3, 9.9, 11, 11.4, 12.6, 8.8],
                   "bottom_error": [2.5, 2.9, 5.6, 2.3, 2.3, 2.7, 2.6, 3.7, 7.1, 2.3],
                   "top_error": [2.5, 8.1, 8, 2.7, 3.2, 3.5, 3.2, 5.2, 13.8, 3],
                   
                   "breakdown":["Lack of a parent or caregiver who tried to provide basic needs including safety, clothes, and food",
                                "Lack of a parent or caregiver who tried to provide basic needs including safety, clothes, and food",
                                "Lack of a parent or caregiver who tried to provide basic needs including safety, clothes, and food",
                                "Lack of a parent or caregiver who tried to provide basic needs including safety, clothes, and food",
                                "Lack of a parent or caregiver who tried to provide basic needs including safety, clothes, and food",
                                "Lack of a parent or caregiver who tried to provide basic needs including safety, clothes, and food",
                                "Lack of a parent or caregiver who tried to provide basic needs including safety, clothes, and food",
                                "Lack of a parent or caregiver who tried to provide basic needs including safety, clothes, and food",
                                "Lack of a parent or caregiver who tried to provide basic needs including safety, clothes, and food",
                                "Lack of a parent or caregiver who tried to provide basic needs including safety, clothes, and food"
                                ]
                   })

# print(df)


#Set paramaters for Bar charts
fig = go.Figure()
fig.add_trace(go.Bar(
        y=df.data_values,
        x=df.breakdown[0:1],
        error_y=dict(
            type='data',
            symmetric=False,
            array=df.top_error,
            arrayminus=df.bottom_error)
        ))

fig.update_traces( selector=dict(type='bar'))


cols =["data_values"]

statewide = [list(df[item][0:1]) for item in cols]
asian = [list(df[item][1:2])  for item in cols]
black = [list(df[item][2:3])  for item in cols]
hispa = [list(df[item][3:4])  for item in cols]
white = [list(df[item][4:5])  for item in cols]
female = [list(df[item][5:6])  for item in cols]
male = [list(df[item][6:7])  for item in cols]
lgbt = [list(df[item][7:8])  for item in cols]
unsure = [list(df[item][8:9])  for item in cols]
hetero = [list(df[item][9:10])  for item in cols]

# print("statewide: ", statewide)
# print("asian: ", asian)
# print("black: ", black)
# print("hispa: ", hispa)
# print("white: ", white)
# print("female: ", female)
# print("male: ", male)
# print("lgbt: ", lgbt)
# print("unsure: ", unsure)
# print("hetero: ", hetero)

# Chart should display only the chart for the specified button, and can toggle between other charts, going back to the original 
dropdown1 =  dict(method = "update", 
                args = [{'y': statewide}],
                label = "Statewide")

dropdown2 =  dict(method = "update",
                args = [{'y': asian}],
                label = "Asian")

dropdown3 =  dict(method = "update",
                args = [{'y': black}],
                label = "Black")

dropdown4 =  dict(method = "update",
                args = [{'y': hispa}],
                label = "Hispanic")

dropdown5 =  dict(method = "update",
                args = [{'y': white}],
                label = "White")

dropdown6 =  dict(method = "update",
                args = [{'y': female}],
                label = "Female")
dropdown7 =  dict(method = "update",
                args = [{'y': male}],
                label = "Male")

dropdown8 =  dict(method = "update",
                args = [{'y': lgbt}],
                label = "Gay/Lesbian/Bisexual")

dropdown9 =  dict(method = "update",
                args = [{'y': unsure}],
                label = "Unsure")

dropdown10 =  dict(method = "update",
                args = [{'y': hetero}],
                label = "Heterosexual")


fig.update_layout(height=450,width=700,bargap=0.2, title="Neglect", title_x=0.5,
                  updatemenus=[dict(active=0,
                                    buttons=[dropdown1, dropdown2, dropdown3, dropdown4,
                                             dropdown5, dropdown6, dropdown7 ,dropdown8 ,
                                             dropdown9, dropdown10])
                               
                              ])

# fig.show()

# fig.write_html("index.html", auto_open=True)

pio.write_html(fig, config=config, file='index.html', auto_open=True)

# tls.get_embed('https://ct-data-collaborative.github.io/aces_visuals/')