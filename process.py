#!/usr/bin/env python3
import csv
from pathlib import Path

def read_raw_data(data_path):
    with data_path.open() as f:
        for row in csv.reader(f, delimiter=' '):
            doc, word, count = row
            yield 'd' + doc, 'w' + word, count

def write_graph(data, graph_path):
    with graph_path.open('w') as f:
        writer = csv.writer(f, delimiter='\t')
        for doc, word, count in data:
            writer.writerow(['hasWord', doc, word])
            writer.writerow(['inDoc', word, doc])

def read_raw_labels(labels_path):
    with labels_path.open() as f:
        doc = 1
        for line in f:
            label = line.strip()
            yield 'w' + str(doc), 'l' + label
            doc += 1

def write_labels(data, data_path, labels):
    with data_path.open('w') as f:
        for doc, label in data:
            f.write('predict(%s,Y)\t' % doc + '\t'.join(
                '%spredict(%s,%s)' % (
                    '+' if label == l else '-',
                    doc,
                    l) for l in labels) + '\n')


if __name__ == '__main__':
    write_graph(read_raw_data(Path('data/test.data')), Path('test.graph'))
    write_graph(read_raw_data(Path('data/train.data')), Path('train.graph'))
    labels = ['l' + str(i) for i in range(1,21)]
    write_labels(read_raw_labels(Path('data/test.label')), Path('test.data'), labels)
    write_labels(read_raw_labels(Path('data/train.label')), Path('train.data'), labels)
