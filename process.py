#!/usr/bin/env python
import csv
import random

def read_raw_data(data_path, offset=0):
    with open(data_path) as f:
        for row in csv.reader(f, delimiter=' '):
            doc, word, count = row
            yield 'd' + str(offset + int(doc)), 'w' + word, count

def write_graph(data, graph_path):
    with open(graph_path, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        for doc, word, count in data:
            writer.writerow(['hasWord', doc, word])
            writer.writerow(['inDoc', word, doc])

def read_raw_labels(labels_path, offset=0):
    with open(labels_path) as f:
        doc = offset+1
        for line in f:
            label = line.strip()
            yield 'w' + str(doc), 'l' + label
            doc += 1

def write_labels(data, data_path, labels):
    with open(data_path, 'w') as f:
        for doc, label in data:
            f.write('predict(%s,Y)\t' % doc + '\t'.join(
                '%spredict(%s,%s)' % (
                    '+' if label == l else '-',
                    doc,
                    l) for l in labels) + '\n')

def write_seeds(doc_labels, graph_path, seed_prop=0.05):
    with open(graph_path, 'a') as f:
        for doc, label in doc_labels:
            if random.random() < seed_prop:
                f.write('labeled\t%s\t%s\n' % (doc, label))

            
if __name__ == '__main__':
    write_graph(read_raw_data('data/test.data', 11269), 'test.graph')
    write_graph(read_raw_data('data/train.data'), 'train.graph')
    labels = ['l' + str(i) for i in range(1,21)]
    write_labels(read_raw_labels('data/test.label', 11269), 'test.data', labels)
    write_labels(read_raw_labels('data/train.label'), 'train.data', labels)
    write_seeds(read_raw_labels('data/test.label', 11269), 'test.graph')
    write_seeds(read_raw_labels('data/train.label'), 'train.graph')
