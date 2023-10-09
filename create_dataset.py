import pandas as pd

gene_start = 21563
gene_stop = 25385
kmer_length = 6
data_total = pd.DataFrame({
    'ref': [],
    'ref_index': [],
    'pos': [],
    'val': [],
})


def get_gene_from_file(file_name):
    with open(file_name) as file:
        return ''.join(file.read().splitlines())[gene_start:gene_stop]

def get_kmer_from_gene_str(gene_str, ref, ref_index):
    for i in range(0, len(gene_str) - kmer_length + 1):
        data_total.loc[len(data_total)] = {'ref': ref, 'ref_index': ref_index, 'pos': i, 'val': gene_str[i:(i + kmer_length)]}

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

data_total.to_csv('dataset.csv', index=False)
