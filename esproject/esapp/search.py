from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.configure(
    default={
        'hosts': ['elk:9200'],
        'sniff_on_start': True
    }
)
connections.create_connection(hosts='elk:9200')


def bulk_indexing():
    BlogPostIndex.init()
    es = Elasticsearch(['elk:9200'])
    bulk(client=es, actions=(b.indexing() for b in models.BlogPost.objects.all().iterator()))


class BlogPostIndex(DocType):
    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()

    class Meta:
        index = 'blogpost-index'

def search(author):
	s = Search().filter('term', author=author)
	response = s.execute()
	return response


