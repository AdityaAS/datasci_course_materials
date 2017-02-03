import sys
 
from MapReduce import MapReduce
 
mr = MapReduce()
 
def mapper(record):
    doc, content = record
    for word in content.split():
        mr.emit_intermediate(word, doc)
 
def reducer(key, value):
    mr.emit((key, list(set(value))))
 
def main():
    data = open(sys.argv[1])
    mr.execute(data, mapper, reducer)

if __name__ == '__main__':
    main()