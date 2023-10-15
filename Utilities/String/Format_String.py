# Format the title in a graph; show the message or error; pass the statement into a function

# Method 1: positional formatting
# 'text{}'.format(value)
# The format method replaces the placeholders using the values.
print('{} helps prevent side effects due to drug reactions and toxic chemicals'.format('Cystein'))
# Cystein helps prevent side effects due to drug reactions and toxic chemicals

str1 = '{} helps prevent side effects due to drug reactions and toxic chemicals'
amino_acid = 'Cystein'
str1.format(amino_acid)
# 'Cystein helps prevent side effects due to drug reactions and toxic chemicals'

# Reorder the placeholder
str2 = '{1} helps {0} side effects due to drug reactions and toxic chemicals'
amino_acid = 'Cystein'
function = 'prevent'
str2.format(function, amino_acid)
# 'Cystein helps prevent side effects due to drug reactions and toxic chemicals'

# Specify the name for the placeholder
str3 = '{amino_acid} helps {function} side effects due to drug reactions and toxic chemicals'
str3.format(amino_acid=amino_acid, function=function)
# 'Cystein helps prevent side effects due to drug reactions and toxic chemicals'

# Pair up the girl and boy names: pairs
pairs = zip(gene_names, protein_names)

# Iterate over pairs
for rank, pair in enumerate(pairs):
    # Unpack pair: gene_names, protein_names
    gene_names, protein_names = pair
    # Print the rank and names associated with each rank
    print(f'Rank {rank+1}: gene_name} and {protein_name}')

