# import requests

# # url = 'http://dbpedia.org/data/Los_Angeles.json'
# # url = 'https://dbpedia.org/data/Computer_science.json'
# url = 'http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=select*%7Bdbr%3AComputer_science+rdfs%3Alabel+%3Flabel%7D&format=json'
# _params = {
#     "simple" : False
# }

# response = requests.get(url, params=_params)

# print(response.text)

import requests
import json
from SPARQLWrapper import SPARQLWrapper, JSON
sparql = SPARQLWrapper("http://dbpedia.org/sparql")

def get_taxonomy(results,entity,wikiPageWikiLink):

    '''This recursive function keeps on fetching the hypernyms of the 
    DBpedia resource recursively till the highest concept or root is reached'''

    if entity == 'null':
        return wikiPageWikiLink
    else :
        # query = ''' SELECT ?hypernyms WHERE {<'''+entity+'''> <http://purl.org/linguistics/gold/hypernym> ?hypernyms .}'''
        query = ''' SELECT * WHERE { ?s dbo:wikiPageWikiLink dbr:''' + entity +  '''}'''
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        for result in results["results"]["bindings"]:
            wikiPageWikiLink.append(result['s']['value'].replace('''http://dbpedia.org/resource/''', '').replace('_', ' '))
        # if len(results["results"]["bindings"]) == 0:
        #     return get_taxonomy(results,'null',wikiPageWikiLink)
        # return get_taxonomy(results,results["results"]["bindings"][0]['s']['value'],wikiPageWikiLink)
        return wikiPageWikiLink

def get_taxonomy_of_resource(dbpedia_resource):
    list_for_hypernyms=[]
    results = {}
    results["results"]={}
    results["results"]["bindings"]=[1,2,3]
    # dbpedia_resource = 'http://dbpedia.org/resource/' + dbpedia_resource.replace(' ', '_')
    dbpedia_resource = dbpedia_resource.replace(' ', '_')
    taxonomy_list = get_taxonomy(results,dbpedia_resource,list_for_hypernyms)
    return taxonomy_list

# get_taxonomy_of_resource('Barack Obama')
concept = ''
while(True):
    concept = input()
    if(concept == ''):
        break
    for _ in get_taxonomy_of_resource(concept):
        print(_)
    print("---------------")