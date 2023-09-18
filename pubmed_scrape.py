#!/usr/bin/env python3

from metapub import PubMedFetcher
import logging
import time
import pandas as pd
import os
from tqdm import tqdm


logging.basicConfig(level=logging.DEBUG, 
                    filename='logs/script.log', 
                    filemode='w', 
                    format='%(name)s - %(levelname)s - %(message)s')

log = logging.getLogger()

fetch = PubMedFetcher()

num_of_articles = 10000

# get the  PMID for first 3 articles with keyword sepsis
pmids = fetch.pmids_for_query("ayurveda", retmax=num_of_articles)
# dois = fetch.article_by_doi("ayurveda", retmax=num_of_articles)

data = {'pmid': [], 'title': [], 'doi': [], 'scihub': [], 'abstract': [], 'year': [], 'fp': [], 'lp': []}

index = 1
for pmid in tqdm(pmids):
    try:
        article = fetch.article_by_pmid(pmid)
    except:
        print(pmid)
        pass
    data['pmid'].append(pmid)
    data['title'].append(str(article.title).replace(",", "").replace("\n", " "))
    data['doi'].append(article.doi)
    data['scihub'].append(f"https://sci-hub.hkvisa.net/{article.doi}")
    data['abstract'].append(str(article.abstract).replace(",", "").replace("\n", " "))
    data['year'].append(article.year)
    data['fp'].append(str(article.first_page).replace(",", "").replace("\n", " "))   
    data['lp'].append(str(article.last_page).replace(",", "").replace("\n", " "))
    index =  index + 1
    df = pd.DataFrame.from_dict(data)
    df.to_csv(f"data/out_{index}.csv", index=False)
    time.sleep(5)
