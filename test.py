
import streamlit as st 
import pickle
import pandas  as pd
from sklearn.metrics.pairwise import sigmoid_kernel
import requests

image_link=[]

def give_rec(title, sig,anime_data,indices):
    
    idx = indices[title]
    sig_scores = list(enumerate(sig[idx]))
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
    sig_scores = sig_scores[1:11]

    # Movie indices
    anime_indices = [i[0] for i in sig_scores]

    # Top 10 most similar movies
    return pd.DataFrame({'Anime name': anime_data['name'].iloc[anime_indices].values,'Rating': anime_data['rating'].iloc[anime_indices].values})

def apis(ids):
      reply =requests.get('https://api.jikan.moe/v4/anime/56')
      meta_data=reply.json()
      try:
        df=pd.DataFrame(meta_data)

        image_url =str(df['data'][11]['jpg']['large_image_url'])
        print('1')
        return image_url
      except:
           return      
def id_of_anime(anime ,ans):
       for i in range(10):
            id_list=anime.loc[lambda anime:anime['name']==ans['Anime name'][i]]
            ids=id_list['anime_id']
            
            image_url=apis(ids)
            image_link.append(image_url)
       return

def recommended(name,anime):
        tfv=pickle.load(open('tfv.pk1','rb'))
        anime_data=pickle.load(open('anime_data.pk1','rb'))
        indices=pickle.load(open('indices.pk1','rb'))
        anime_data=pd.DataFrame(anime_data)
        indices = pd.Series(anime_data.index, index=anime_data['name']).drop_duplicates()
        # Compute the sigmoid kernel
        sig = sigmoid_kernel(tfv, tfv)
        
        ans=give_rec(name, sig,anime_data,indices)
        
        id_of_anime(anime,ans)
        return ans



anime_list=pickle.load(open('movie_dict.pk1','rb'))
anime=pd.DataFrame(anime_list)

return_form_model=recommended('Kimi no Na wa.',anime)
print(image_link[0])