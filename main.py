import pandas as pd

gene_start = 21563
gene_stop = 25385
kmer_length = 14



def get_gene_from_file(file_name):
    with open(file_name) as file:
        return file.read()[gene_start:gene_stop]

def get_kmer_from_gene_str(gene_str):
    temp_dict = {}
    for i in range(0, len(gene_str) - kmer_length + 1):
        temp_dict[i] = gene_str[i:(i + kmer_length)]
    return temp_dict

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

kmer_alpha_dict = get_kmer_from_gene_str(alpha_str)
kmer_beta_dict = get_kmer_from_gene_str(beta_str)
kmer_delta_dict = get_kmer_from_gene_str(delta_str)
kmer_epsilon_dict = get_kmer_from_gene_str(epsilon_str)
kmer_eta_dict = get_kmer_from_gene_str(eta_str)
kmer_gamma_dict = get_kmer_from_gene_str(gamma_str)
kmer_iota_dict = get_kmer_from_gene_str(iota_str)
kmer_kappa_dict = get_kmer_from_gene_str(kappa_str)
kmer_lambda_dict = get_kmer_from_gene_str(lambda_str)
kmer_theta_dict = get_kmer_from_gene_str(theta_str)

print(kmer_alpha_dict)