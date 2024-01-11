import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_icon='⚔️', layout='wide', page_title='Project DS. Распознование вирусни по отдельным подцепочкам РНК')
data_viruses = pd.DataFrame({
        'ref': [],
        'ref_index': []
    })


str_test = 'CTCAATTACCCCCTGCATACACTAATTCTTTCACACGTGGTGTTTATTACCCTGACAAAGTTTTCAGATCCTCAGTTTTACATTCAACTCAGGACTTGTTCTTACCTTTCTTTTTGTTTGTTTTTCTTGTTTTATTGCCACTAGTCTCTAGTCAGTGTGTTAATCTTACAACCAGAACTCAATTACCCCCTGCATACACTAATTCTTTCACACGTGGTGTTTATTACCCTGACAAAGTTTTCAG'


test_genes = st.text_area(label='Введите тестовые цепочки:  ', value=str_test)
button_create_dataset = st.button('Создание датасетов и классификация')
if button_create_dataset:

    gene_start = 21563
    gene_stop = 25385
    kmer_length = 21

    data_total = pd.DataFrame({
        'ref': [],
        'ref_index': [],
        'pos': [],
        'val': [],
        'val_num': []
    })


    def get_gene_from_file(file_name):
        with open(file_name) as file:
            return ''.join(file.read().splitlines())[gene_start:gene_stop]


    def get_kmer_from_gene_str(gene_str, ref, ref_index):
        for i in range(0, len(gene_str) - kmer_length + 1):
            data_total.loc[len(data_total)] = {'ref': ref, 'ref_index': ref_index, 'pos': i,
                                               'val': gene_str[i:(i + kmer_length)]}


    alpha_str = get_gene_from_file('alpha.fasta')
    beta_str = get_gene_from_file('beta.fasta')
    delta_str = get_gene_from_file('delta.fasta')
    epsilon_str = get_gene_from_file('epsilon.fasta')
    eta_str = get_gene_from_file('eta.fasta')
    gamma_str = get_gene_from_file('gamma.fasta')
    iota_str = get_gene_from_file('iota.fasta')
    kappa_str = get_gene_from_file('kappa.fasta')
    lambda_str = get_gene_from_file('lambda.fasta')
    theta_str = get_gene_from_file('theta.fasta')

    get_kmer_from_gene_str(alpha_str, 'alpha', 0)
    get_kmer_from_gene_str(beta_str, 'beta', 1)
    get_kmer_from_gene_str(delta_str, 'delta', 2)
    get_kmer_from_gene_str(epsilon_str, 'epsilon', 3)
    get_kmer_from_gene_str(eta_str, 'eta', 4)
    get_kmer_from_gene_str(gamma_str, 'gamma', 5)
    get_kmer_from_gene_str(iota_str, 'iota', 6)
    get_kmer_from_gene_str(kappa_str, 'kappa', 7)
    get_kmer_from_gene_str(lambda_str, 'lambda', 8)
    get_kmer_from_gene_str(theta_str, 'theta', 9)

    values = pd.DataFrame(data_total[['val']].drop_duplicates(subset='val'))
    values.reset_index(inplace=True, drop=True)
    col_t = pd.Series(list(round(i) for i in range(0, len(values), 1)))
    values['index'] = col_t
    values.set_index('val', inplace=True, drop=True)

    values.to_csv('keys.csv')
    lst = list()
    values2 = data_total['val']
    for v in values2:
        lst.append(values.loc[v][0])

    data_total['val_num'] = pd.Series(lst)
    data_viruses = data_total[['ref', 'ref_index']].drop_duplicates(inplace=False)
    data_viruses.set_index('ref_index', inplace=True, drop=True)
    data_total.to_csv('dataset.csv', index=False)

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


    get_kmer_from_gene_str(test_genes)

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


    data = pd.read_csv('dataset.csv')

    y = data[['ref_index']]
    x = data[['val_num', 'pos']]
    model = RandomForestClassifier(n_estimators=200, max_depth=28, max_features='log2')
    model.fit(x, y)

    data_viruses3 = pd.DataFrame(data=[], columns=['virus', 'percent'])
    data_ts = pd.read_csv('samples.csv')
    x_ts = data_ts[['val_num', 'pos']]
    y_pr = pd.DataFrame(model.predict(x_ts))
    for i in range(0, len(y_pr)):
        y_pr.iloc[i] = data_viruses.iloc[y_pr.iloc[i][0]][0]
    data_ts['y_pred'] = y_pr
    st.dataframe(data_ts.round(0))
    data_viruses2 = pd.DataFrame(data_ts[['y_pred']].drop_duplicates(subset='y_pred'))
    data_viruses3['virus'] = data_viruses2['y_pred']
    ldv = 0
    len2 = len(data_viruses2)
    for i in range(0, len2):
        data_viruses2.iloc[i]['y_pred'] = (data_ts['y_pred'].value_counts()[data_viruses2.iloc[i][0]] / len(y_pr)) * 100
    data_viruses3['percent'] = data_viruses2['y_pred']
    st.dataframe(data_viruses3)

    #data_ts.to_csv('samples_pred.csv')
