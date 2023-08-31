import streamlit as st 
import pickle
import pandas  as pd
from sklearn.metrics.pairwise import sigmoid_kernel
import requests

image_link=[]
#API CALL FOR IMAGE OF ANIME 
def apis(ids):
      reply =requests.get('https://api.jikan.moe/v4/anime/'+str(ids))
      meta_data=reply.json()
      try:
        df=pd.DataFrame(meta_data)
        image_url =str(df['data'][11]['jpg']['large_image_url'])
        return image_url
      except:
           return

def give_rec(title, sig,anime_data,indices):
    
    idx = indices[title]
    sig_scores = list(enumerate(sig[idx]))
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
    sig_scores = sig_scores[1:11]

    # Movie indices
    anime_indices = [i[0] for i in sig_scores]

    # Top 10 most similar movies
    return pd.DataFrame({'Anime name': anime_data['name'].iloc[anime_indices].values,'Rating': anime_data['rating'].iloc[anime_indices].values})

def id_of_anime(anime,ans,image_link):
       for i in range(5):
            id_list=anime.loc[lambda anime:anime['name']==ans['Anime name'][i]]
            ids=id_list['anime_id']
            image_url=apis(ids)
            image_link.append(image_url)

       return 

def recommended(name,anime,image_link):
        tfv=pickle.load(open('model/tfv.pk1','rb'))
        anime_data=pickle.load(open('model/anime_data.pk1','rb'))
        indices=pickle.load(open('model/indices.pk1','rb'))
        anime_data=pd.DataFrame(anime_data)
        indices = pd.Series(anime_data.index, index=anime_data['name']).drop_duplicates()
        # Compute the sigmoid kernel
        sig = sigmoid_kernel(tfv, tfv)
        ans=give_rec(name, sig,anime_data,indices)
        id_of_anime(anime,ans,image_link)
        return ans 

anime_list=pickle.load(open('model/movie_dict.pk1','rb'))
anime=pd.DataFrame(anime_list)
st.title('anime recommender system')
selected_anime_name = st.selectbox('anime list',(anime['name'].values))
if st.button('Recommend'):
    return_form_model=recommended(selected_anime_name,anime,image_link)
    st.write(return_form_model['Anime name'])
    
    col1,col2,col3=st.columns(3)
    with col1:
                 st.text(return_form_model['Anime name'][0])
                 st.image(image_link[0])
    with col2:
                 st.text(return_form_model['Anime name'][1])
                 st.image(image_link[1])
    with col3:
                 st.text(return_form_model['Anime name'][2])
                 st.image(image_link[2])
    
