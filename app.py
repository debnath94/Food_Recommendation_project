import streamlit as st
import pickle
import pandas as pd

def recommend(food):
    food_index = foods[foods['Breakfast'] == food].index[0]
    distances = similarity[food_index]
    foods_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    recommended_foods = []
    for i in foods_list:
        recommended_foods.append(foods.iloc[i[0]].Breakfast)
        return recommended_foods

foods_pikl = pickle.load(open('food_list.pkl', 'rb'))
foods = pd. DataFrame(foods_pikl)
similarity = pickle. load(open('food_similarity.pkl', 'rb'))


st. title('Breakfast Recommender System')
selected_Food_name = st.selectbox(
'How would you like to be contacted?',
foods['Breakfast']. values)

if st.button('Recommended'):
    recommendations = recommend(selected_Food_name)
    for i in recommendations:
        st. write(i)









