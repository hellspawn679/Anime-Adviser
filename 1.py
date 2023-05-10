import requests
import pandas as pd
ids=56
reply =requests.get('https://api.jikan.moe/v4/anime/'+str(ids))
data=reply.json()
df=pd.DataFrame.from_dict(data)
print(df['data'][11]['jpg']['large_image_url'])
#a=data['data']['images']['jpg']['large_image_url']
