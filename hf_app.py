# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:51:17 2020

@author: prachi
"""

import streamlit as st
import pickle
import numpy as np
model= pickle.load(open('model.pkl','rb'))


def predict_hf(serum_sodium,ejection_fraction,serum_creatinine,age):
    input=np.array([[serum_sodium,ejection_fraction,serum_creatinine,age]]).astype(np.float64)
    prediction=model.predict(input)
    
    return int(prediction)

def main():
    
    html_temp="""
    <div style="background-color:#004383 ;padding:10px">
    <h2 style="color:white;text-align:center;">HEART FAILURE PREDICTION  </h2>
    </div>
    """  
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://images.pexels.com/photos/965121/pexels-photo-965121.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940");
    background-size: cover;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    #st.markdown('<style>body{background-color: #fef0f1;}</style>',unsafe_allow_html=True)
    st.markdown(html_temp, unsafe_allow_html=True)
    
    a = st.slider('SERIUM SODIUM',100,150)
   
    b = st.slider("EJECTION FRACTION",0 , 80)
    c = st.slider("SERUM CERATINE",0.00, 10.00)
    d = st.slider("AGE",0, 100)
    
   
    
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;">Relax! You are not at risk! </h2>
       </div>
    """
    
    
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;">You are at high risk!! Consult the doctor soon!</h2>
       </div>
    """
    
    if st.button("Predict"):
        output=predict_hf(a,b,c,d)
        st.success('The OUTPUT is {}'.format(output))
        
        
        if output == 1:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)
     
            
if __name__=='__main__':
   main()
        