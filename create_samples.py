import pandas as pd

kmer_length = 21
data_total = pd.DataFrame({
    'pos': [],
    'val': [],
    'val_num': []
})

def get_gene_from_file(file_name):
    with open(file_name) as file:
        return ''.join(file.read().splitlines())


def get_kmer_from_gene_str(gene_str):
    for i in range(0, len(gene_str) - kmer_length + 1):
        data_total.loc[len(data_total)] = {'pos': i, 'val': gene_str[i:(i + kmer_length)]}


get_kmer_from_gene_str(get_gene_from_file("R.csv"))

values = pd.read_csv("keys.csv", delimiter=",")
values.set_index('val', inplace=True)

lst = list()
values2 = data_total['val']
for v in values2:
    try:
        lst.append(values.loc[v][0])
    except:
        lst.append(None)

data_total['val_num'] = pd.Series(lst)
data_total = data_total.dropna()
data_total.to_csv('samples.csv', index=False)