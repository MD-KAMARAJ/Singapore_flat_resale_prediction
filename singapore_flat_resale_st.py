import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import joblib
import base64

st.set_page_config(layout = "wide")

def set_bg_hack(main_bg):
          main_bg_ext = "jpg"
          st.markdown(f"""<style>.stApp {{
             background: url(data:image/{main_bg_ext};base64,{main_bg});
             background-size: cover}}</style>""",unsafe_allow_html=True)
          
st.title(":red[Singapore Flat Resale Price Prediction]")
with st.sidebar:
     selection=option_menu(menu_title= 'Main menu',
                         options=['Home','Prediction'],
                         icons=['home', 'analysis' ])

if selection == 'Home':
     
     with open(r"D:\\GUVI_projects\\05_Singapore flat price\\singapore_pic.jpg", "rb") as image_file:
               image_bytes = image_file.read()
               encoded_image = base64.b64encode(image_bytes).decode()

     set_bg_hack(encoded_image)

     st.markdown('''<h5 style='color: white;'>This Singapore flat resale price prediction predicts the flat resale price if you have provided the sufficient inputs to this model</h5>''',unsafe_allow_html=True)
     st.markdown('''<h6 style='color: white;'>The inputs to be provided are as follows:</h6>''',unsafe_allow_html=True)
     st.markdown('''<h3 style='color: white;text-decoration: underline;'>Year</h3>''',unsafe_allow_html=True)
     st.markdown('''<h5 style='color: white;'>This year refers to the year on which the resale price is predicted</h5>''',unsafe_allow_html=True)
     st.markdown('''<h3 style='color: white;text-decoration: underline;'>Flat Type:</h3>''',unsafe_allow_html=True)
     st.markdown('''<h5 style='color: white;'>This flat type indicated whether the flat is, 1 Room, 2 Rooms, 3 Rooms, 4 Rooms, 5 Rooms, Executive and Multi-Generation. 
                 These types are mapped to numbers</h5>''',unsafe_allow_html=True)
     st.markdown('''<h6 style='color: white;'>1 Room - 1,</h6>''',unsafe_allow_html=True)
     st.markdown('''<h6 style='color: white;'>2 Rooms - 2,</h6>''',unsafe_allow_html=True)
     st.markdown('''<h6 style='color: white;'>3 Rooms - 3,</h6>''',unsafe_allow_html=True)
     st.markdown('''<h6 style='color: white;'>4 Rooms - 4,</h6>''',unsafe_allow_html=True)
     st.markdown('''<h6 style='color: white;'>5 Rooms - 5,</h6>''',unsafe_allow_html=True)
     st.markdown('''<h6 style='color: white;'>Executive - 6 and</h6>''',unsafe_allow_html=True)
     st.markdown('''<h6 style='color: white;'>Multi-Generation - 7</h6>''',unsafe_allow_html=True)
     st.markdown('''<h3 style='color: white;text-decoration: underline;'>Town:</h3>''',unsafe_allow_html=True)
     st.markdown('''<h5 style='color: white;'>This feature tells about the town in which flat is located, as location also makes an effect in the resale price of flat.
               This feature is also mapped to numbers from 1 to 27</h5>''',unsafe_allow_html=True)
     st.markdown('''<h3 style='color: white;text-decoration: underline;'>Floor area square metre:</h3>''',unsafe_allow_html=True)
     st.markdown('''<h5 style='color: white;'>This feature tells about the floor area of the flat as area is the most important feature for the fixation of resale price of the flat</h5>''',unsafe_allow_html=True)
     st.markdown('''<h3 style='color: white;text-decoration: underline;'>Remaining Lease:</h3>''',unsafe_allow_html=True)
     st.markdown('''<h5 style='color: white;'>This feature gives the information about the lease year remaining for that flat, as in Singapore HDB (Housing Development Board) regualtes flats.
              The maximum lease year for a flat is 99 years. This feature tells the remaining year left over from 99 years</h5>''',unsafe_allow_html=True)
     st.markdown('''<h3 style='color: white;text-decoration: underline;'>Mid Storey:</h3>''',unsafe_allow_html=True)
     st.markdown('''<h5 style='color: white;'>This features tells us about the number floors that the flat has, normally it is shown in range format, then from that range the number of floor is arrived</h5>''',unsafe_allow_html=True)



if selection == 'Prediction':

     with open(r"D:\\GUVI_projects\\05_Singapore flat price\\analysis.jpg", "rb") as pic_file:
               pic_bytes = pic_file.read()
               encoded_pic = base64.b64encode(pic_bytes).decode()

     set_bg_hack(encoded_pic)

     col1,col2 = st.columns(2)
     df_features = pd.read_csv ("singapore_flat_resale_combined.csv")
     df_features['flat_type']=df_features['flat_type'].str.replace('-', ' ')
     df_features['month']=pd.to_datetime(df_features['month'])
     st.markdown('''<h5 style='color: white;'>Year</h5>''', unsafe_allow_html=True)
     Year = int(st.number_input('Enter year'))
     st.markdown('''<h5 style='color: white;'>Floor area sqm</h5>''', unsafe_allow_html=True)
     Floor_area_sqm = int(st.number_input("Enter floor_area_sqm"))
     st.markdown('''<h5 style='color: white;'>Remaining Lease</h5>''', unsafe_allow_html=True)
     Remaining_lease = Remaining_lease = int(st.selectbox("Enter remaining_lease", (i for i in range(1, 100))))
     st.markdown('''<h5 style='color: white;'>Flat Type</h5>''', unsafe_allow_html=True) 
     Flat_type = st.selectbox("Enter flat_type",df_features['flat_type'].unique())
     st.markdown('''<h5 style='color: white;'>Mid Storey</h5>''', unsafe_allow_html=True)
     Mid_storey = st.selectbox("Enter mid_storey",set(df_features['mid_storey'].unique()))
     st.markdown('''<h5 style='color: white;'>Town</h5>''', unsafe_allow_html=True)
     Town = st.selectbox("Enter town",df_features['town'].unique())
               
     Resale_prediction = {
                         "town": Town, 
                         "flat_type":  Flat_type,
                         "year": Year,
                         "floor_area_sqm": Floor_area_sqm,
                         "remaining_lease": Remaining_lease,
                         "mid_storey": Mid_storey}
          
     df_resale = pd.DataFrame([Resale_prediction]) 
     flat_type_map={'1 ROOM' :1 , '2 ROOM': 2, '3 ROOM': 3, '4 ROOM': 4, '5 ROOM': 5,  'EXECUTIVE':6,
       'MULTI GENERATION': 7}
     df_resale["flat_type_encoded"] = df_resale['flat_type'].map(flat_type_map)
     town_encoded={'ANG MO KIO':1, 'BEDOK':2, 'BISHAN':3, 'BUKIT BATOK':4, 'BUKIT MERAH':5,
       'BUKIT TIMAH':6, 'CENTRAL AREA':7, 'CLEMENTI':8, 'GEYLANG':9, 'HOUGANG':10,
       'JURONG EAST':11, 'JURONG WEST':12, 'KALLANG/WHAMPOA':13, 'MARINE PARADE':14,
       'QUEENSTOWN':15, 'SERANGOON':16, 'TAMPINES':17, 'TOA PAYOH':18, 'WOODLANDS':19,
       'YISHUN':20, 'CHOA CHU KANG':21, 'BUKIT PANJANG':22, 'PASIR RIS':23,
       'SENGKANG':24, 'SEMBAWANG':25, 'LIM CHU KANG':26, 'PUNGGOL':27}
     df_resale['town_encoded']=df_resale['town'].map(town_encoded)
     df_resale['year_log'] = np.log(df_resale["year"])
     df_resale["floor_area_sqm_log"] = np.log(df_resale["floor_area_sqm"])
     df_resale['remaining_lease_log'] = np.log(df_resale["remaining_lease"])
     df_resale['mid_storey_log'] = np.log(df_resale["mid_storey"])

     
     df1_resale = df_resale.copy()
     data = joblib.load("D:\GUVI_projects\model_RF.joblib", mmap_mode='r')
     model = data['model']
     selected_features_AS=['town_encoded','flat_type_encoded','year_log', 'floor_area_sqm_log', 'remaining_lease_log','mid_storey_log']
     
     scaler = data['scaler']
     scaler_target=data['scaler_target']
     df2_resale=df1_resale[selected_features_AS]
     
     col2.markdown('''<h3 style='color: white;'>Resale Flat Price Prediction</h3>''', unsafe_allow_html=True)
     
     if np.isinf(df2_resale).values.any():
          col2.container(border=True).markdown("***The input contains infinite values. Please provide valid input values.***")    
     else:        
          scaled_data = scaler.transform(df2_resale)
          predictions = np.exp(scaler_target.inverse_transform(pd.DataFrame(model.predict(scaled_data))))
          col2.container(border=True).text(predictions[0][0])