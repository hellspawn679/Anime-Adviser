import streamlit as st 
import pickle
import pandas  as pd
from sklearn.metrics.pairwise import sigmoid_kernel
import requests
from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from flask_cors import CORS  
import requests
import json

anime_list=pickle.load(open('model/movie_dict.pk1','rb'))
anime=pd.DataFrame(anime_list)
#API CALL FOR IMAGE OF ANIME 
image_link=[]
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
app = Flask(__name__)
# creating an API object 
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})
image_link=[]
#API CALL FOR IMAGE OF ANIME 
class recommend(Resource):
    def post(self):
        an_request = request.get_json()
        an_request=json.loads(an_request)
        return recommended(an_request["name"],anime,image_link).to_json()
        

# adding the defined resources along with their corresponding urls
api.add_resource(recommend, '/')


# driver function 
if __name__ == '__main__':
    app.run(debug=False)

