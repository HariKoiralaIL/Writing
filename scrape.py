import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore
slack = AppStore(country='us', app_name='netflix', app_id = '363590051')

slack.review(how_many=2000)

slackdf = pd.DataFrame(np.array(slack.reviews),columns=['review'])
slackdf2 = slackdf.join(pd.DataFrame(slackdf.pop('review').tolist()))
slackdf2.head()

slackdf2.to_csv('Netflix-app-reviews.csv')