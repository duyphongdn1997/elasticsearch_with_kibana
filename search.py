from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

resp = es.search(index="idx", query={"query":{"match":{"content":"1"}}})
print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])