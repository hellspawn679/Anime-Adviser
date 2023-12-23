import streamlit as st 
import pickle
import pandas  as pd
from sklearn.metrics.pairwise import sigmoid_kernel
import requests
import json

anime_list=pickle.load(open('movie_dict.pk1','rb'))
anime=pd.DataFrame(anime_list)
st.title('anime recommender system')
selected_anime_name = st.selectbox('anime list',(anime['name'].values))
an_request = {'name': selected_anime_name}
an_request=json.dumps(an_request, indent=4)  


if st.button('Recommend'):
    return_from_api=requests.post("http://my-api.dev:5000", json = an_request)
    json_data=json.loads(return_from_api.json())
    rearranged_data = [{'Anime name': anime, 'Rating': rating} for anime, rating in zip(json_data['Anime name'].values(), json_data['Rating'].values())]
    df = pd.DataFrame(rearranged_data)
    st.write(df)
    

    
    
