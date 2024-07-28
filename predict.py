import pickle
import streamlit as st
from streamlit_option_menu import option_menu


with open('hd.pkl','rb') as file:
  clf=pickle.load(file)
 
 
with st.sidebar:
    selected = option_menu('Heart Disease Predictor',

                           ['Welcome','Heart Disease Prediction',
                            'Review'],
                           
                          
                           default_index=0)


if selected=='Welcome':
    st.image("logo1.png")

if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')
    st.write(":blue[There are many types of heart disease, and each one has its own symptoms and treatment. For some, lifestyle changes and medicine can make a huge difference in improving your health. For others, you may need surgery to make your ticker work well again.]")
    st.image("heart1.jpeg")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

  
    heart_diagnosis = ''

   

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

       
        prediction= clf.predict([user_input])

        if prediction == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
if selected == 'Review':    
    st.title(":red[Review section]")
    st.write(":blue[Thank you for trying our app ,your every feedback matters]")
    st.text_area("Write your suggestions")
    st.write(":blue[how was your experience on a scale of 1 to 10.]")
    st.slider("",0,10)
