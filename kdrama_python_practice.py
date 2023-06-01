#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 13:05:44 2023

@author: alexchen
"""
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

import datetime as dt
import plotly.express as px

from plotly.offline import download_plotlyjs, init_notebook_mode,  plot
from plotly.graph_objs import *
init_notebook_mode()


init_notebook_mode(connected=True)

# Make recommendation system based on list of shows/movies/Genre

import random

number_of_colors = 12

color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
print(color)

k_drama = pd.read_csv('/Users/alexchen/Desktop/Python_practice/kdrama_data/top100_kdrama.csv')

k_drama.info()
k_drama.isna().sum() # No NA values


k_drama.groupby('Year of release').size().reset_index().rename(columns = {0:'Count'})
k_drama.head()


fig = px.bar(data_frame = k_drama.groupby('Year of release').size().reset_index().rename(columns = {0:'Count'}),
              x = 'Year of release',
              y = 'Count')



fig.update_traces(marker_color = color)

fig.update_layout(title = {'text':'Korean Drama released by year',
                           'font_size':20},
                  font = dict(family = "Times New Roman, monospace",
                              size = 15,
                              color = 'black'))

plot(fig)


num_episode = k_drama['Number of Episode'].value_counts().reset_index().rename(columns={'Number of Episode':'Num Ep','index':'count'})

#num_episode.rename(columns = {"Count": "Number of Episodes"})

fig = px.pie(data_frame = num_episode,
             values = 'count', names = 'Num Ep',
             color_discrete_sequence = px.colors.qualitative.Safe)

fig.update_traces(textposition = 'inside',
                  textinfo = 'label+percent',
                  pull = [0.05] * num_episode['count'].nunique(),
                  insidetextorientation='horizontal')

fig.update_layout(title = 'Distribution of Number of Episodes among Top 100',
                  legend_title = 'Number of Episodes',
                  uniformtext_minsize = 13,
                  uniformtext_mode = 'hide',
                  font = dict(family = 'Times New Roman, monospace',
                              size = 15,
                              color = 'black')
                  )

plot(fig)

from collections import Counter
networks = []
year_list = []
for index,row in k_drama.iterrows():
    for indiv in row['Network'].split(","):
        networks.append(indiv.strip())
        year_list.append(row['Year of release'])
        #year_list.append(year)

df = pd.DataFrame({'Network':networks,
                   'Year': year_list
                   })

df.groupby(['Network', 'Year']).size().reset_index().rename(columns = {index:'Count'})



fig = px.bar(data_frame = df.groupby(['Network', 'Year']).size().reset_index().rename(columns = {0:'Count'}),
             x = 'Year',
             y = 'Count',
             color = 'Network',
             barmode = 'stack',
             color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_layout(title = {'text':'Korean Drama released by Year and Aired On',
                           'y' : 0.95,
                           'x' : 0.45,
                           'xanchor' : 'center',
                           'yanchor' : 'top'},
                  legend_title = 'Aired On (Network)',
                  font = dict(family = 'Times New Roman, monospace',
                              size = 15,
                              color = 'black'
                  ))

plot(fig)


# Individual Genre
k_drama['Genre'] = k_drama['Genre'].str.strip()

genre_list = []
for genres in k_drama['Genre'].to_list():
    for gen in genres.split(","):
        genre_list.append(gen.strip())
        
genre_df = pd.DataFrame.from_dict(Counter(genre_list), orient = 'index').rename(columns = {0:'Count'})
genre_df.sort_values(by='Count',ascending = False, inplace = True)
genre_df.head()

# One hot encoding the columns with lists as entries
cast = k_drama['Cast'].str.split(', ').tolist()

flat_cast = [item for sublist in cast for item in sublist]
flat_cast = list(set(flat_cast))

k_drama_2 = k_drama.reindex(k_drama.columns.tolist() + flat_cast, axis=1, fill_value=0)
l = 0
for index, row in k_drama.iterrows():
    for val in row['Cast'].split(', '):
        l += 1
        #print(val)
        k_drama_2.loc[index, val] = 1
remove_columns = []
for i in range(14,len(k_drama_2.columns)):
    if sum(k_drama_2.iloc[:,i]) < 2:
        remove_columns.append(i)


k_drama_2 = k_drama_2.drop(k_drama_2.columns[remove_columns], axis = 1)


genre = k_drama['Genre'].str.split(', ').tolist()

flat_genre = [item for sublist in genre for item in sublist]
flat_genre = list(set(flat_genre))

k_drama_2 = k_drama_2.reindex(k_drama_2.columns.tolist() + flat_genre, axis=1, fill_value=0)
for index, row in k_drama.iterrows():
    for val in row['Genre'].split(', '):
        #print(val)
        k_drama_2.loc[index, val] = 1
remove_columns = []
for i in range(144,len(k_drama_2.columns)):
    if sum(k_drama_2.iloc[:,i]) < 2:
        remove_columns.append(i)


k_drama_2 = k_drama_2.drop(k_drama_2.columns[remove_columns], axis = 1)


tags = k_drama['Tags'].str.split(', ').tolist()

flat_tags = [item for sublist in tags for item in sublist]
flat_tags = list(set(flat_tags))

k_drama_2 = k_drama_2.reindex(k_drama_2.columns.tolist() + flat_tags, axis=1, fill_value=0)
for index, row in k_drama.iterrows():
    for val in row['Tags'].split(', '):
        #print(val)
        k_drama_2.loc[index, val] = 1
remove_columns = []
for i in range(179,len(k_drama_2.columns)):
    if sum(k_drama_2.iloc[:,i]) < 2:
        remove_columns.append(i)


k_drama_2 = k_drama_2.drop(k_drama_2.columns[remove_columns], axis = 1)
# Continue with recommendation system

k_drama['features'] = k_drama['Network'] + " " + k_drama["Content Rating"] + " " + k_drama['Synopsis'] + " " +  k_drama['Cast'] + " " + k_drama['Genre'] + " " + k_drama['Tags']

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn import preprocessing
from scipy import sparse

cv = CountVectorizer()
count_matrix = cv.fit_transform(k_drama['features'])

num_features = k_drama[['Year of release', 'Rating','Number of Episode']]
num_features = preprocessing.normalize(num_features)


count_mat_and_num = sparse.hstack((count_matrix, num_features))

cosine_sim = cosine_similarity(count_matrix)

cosine_sim_2 = cosine_similarity(count_mat_and_num)

# Function for movie recommendation
def kdrama_rec(mov,sim_num = 5):

    user = mov
    
    try:
        ref_index = k_drama_2[k_drama_2['Name'].str.contains(user, case = False)].index[0]

        similar_movies = list(enumerate(cosine_sim_2[ref_index]))

        sorted_similar_movies = sorted(similar_movies, key = lambda x: x[1], reverse = True)[1:]

        print('\nRecomended K Drama for [{}]'.format(user))
        print('-'*(30 + len(user)))

        for i, element in enumerate(sorted_similar_movies):
            similar_movie_id = element[0]
            similar_movie_title = k_drama_2['Name'].iloc[similar_movie_id]
            s_score = element[1]
            print('{:40} -> {:.3f}'.format(similar_movie_title, s_score))

            if i > sim_num:
                break
    except IndexError:
        print("\n[{}] is not in our database!".format(user))
        print("Unable to make recommendation")

kdrama_rec("My Mister")

# make a simple interface for this



# Trying the BERT transformer

import matplotlib.pyplot as plt
import numpy as np
from sentence_transformers import SentenceTransformer
import pandas as pd
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA


model = SentenceTransformer('distilbert-base-nli-mean-tokens')
embeddings = model.encode(k_drama['features'], show_progress_bar=True)

features = np.array(embeddings)
n_comp = 5
pca = PCA(n_components=n_comp)
pca.fit(features)
pca_data = pd.DataFrame(pca.transform(features))
pca_data.head()


sns.pairplot(pca_data)

cos_sim_data = pd.DataFrame(cosine_similarity(features))

def kdrama_rec_bert(mov,sim_num = 5):

    user = mov
    
    try:
        ref_index = k_drama_2[k_drama_2['Name'].str.contains(user, case = False)].index[0]

        similar_movies = list(enumerate(cos_sim_data[ref_index]))

        sorted_similar_movies = sorted(similar_movies, key = lambda x: x[1], reverse = True)[1:]

        print('\nRecomended K Drama for [{}]'.format(user))
        print('-'*(30 + len(user)))

        for i, element in enumerate(sorted_similar_movies):
            similar_movie_id = element[0]
            similar_movie_title = k_drama_2['Name'].iloc[similar_movie_id]
            s_score = element[1]
            print('{:40} -> {:.3f}'.format(similar_movie_title, s_score))

            if i > sim_num:
                break
    except IndexError:
        print("\n[{}] is not in our database!".format(user))
        print("Unable to make recommendation")

kdrama_rec_bert("My Mister")
