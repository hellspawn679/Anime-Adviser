import streamlit as st 
import pickle
import pandas  as pd
from sklearn.metrics.pairwise import sigmoid_kernel




def give_rec(title, sig,anime_data,indices):
    
    idx = indices[title]
    sig_scores = list(enumerate(sig[idx]))
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
    sig_scores = sig_scores[1:11]

    # Movie indices
    anime_indices = [i[0] for i in sig_scores]

    # Top 10 most similar movies
    return pd.DataFrame({'Anime name': anime_data['name'].iloc[anime_indices].values,'Rating': anime_data['rating'].iloc[anime_indices].values})



def recommended(name,anime):
        tfv=pickle.load(open('tfv.pk1','rb'))
        anime_data=pickle.load(open('anime_data.pk1','rb'))
        indices=pickle.load(open('indices.pk1','rb'))
        anime_data=pd.DataFrame(anime_data)
        indices = pd.Series(anime_data.index, index=anime_data['name']).drop_duplicates()
        # Compute the sigmoid kernel
        sig = sigmoid_kernel(tfv, tfv)
        
        ans=give_rec(name, sig,anime_data,indices)
        
        return ans 

anime_list=pickle.load(open('movie_dict.pk1','rb'))
anime=pd.DataFrame(anime_list)
st.title('anime recommender system')
selected_anime_name = st.selectbox('anime list',(anime['name'].values))
if st.button('Recommend'):
    return_form_model=recommended(selected_anime_name,anime)
    st.write(return_form_model['Anime name'])
    
