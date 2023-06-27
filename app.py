import streamlit as st
import pickle
import pandas as pd

# BACKGROUND IMAGE
st.markdown(
    """
    <style>
    body {
        background-image: url("https://www.pexels.com/photo/woman-pouring-juice-on-glass-3184192/");
        background-repeat: no-repeat;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
order = pickle.load(open("order.pkl","rb"))
tab1, tab2 = st.tabs(["Premium Customer", "New Customer"])


with tab1:
    id = order["user_id"].values
    user_id = [*set(id)]
    st.title("Dish Recommendation System")
    option = st.selectbox("Enter your User_ID",user_id)


    # For showing previous order of a user
    dishes = order.loc[order['user_id'] == option, 'dish'].tolist()
    if st.button("Previous Order"):
        for i in dishes:
            st.write(i)



    # For the recommendation part
    recommended_dishes = pickle.load(open("recommendations.pkl","rb"))
    def recommendations(id):
      point =recommended_dishes[recommended_dishes.values == id].values.tolist()
      a1=point[0][2:]
      return a1
    if st.button("Recommendations for you"):
        recommend = recommendations(option)
        for i in recommend:
            st.write(i)




with tab2:
    st.title('Dish Recommendation System')

    food_list = pickle.load(open('food.pkl', 'rb'))
    # food_list = food_list['DishName'].values
    data = pd.DataFrame(food_list)
    similarity = pickle.load(open('similarity.pkl', 'rb'))



    def recommend(food):
        food_index = data[data["DishName"] == food].index[0]
        distances = similarity[food_index]
        food_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

        recommended_foods = []
        for i in food_list:
            recommended_foods.append(data.iloc[i[0]].DishName)
        return recommended_foods

    selected_food = st.selectbox('What would you like to Order?', food_list)
    if st.button('Recommend'):
        recommendations = recommend(selected_food)
        st.subheader("Also try this")
        for i in recommendations:
            st.write(i)

