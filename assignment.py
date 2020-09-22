###### Ignore this
import pytest
import hashlib
_ = 123456789  # just a wrong number, please ignore
###### Stop ignoring

# Some stuff you can/should use ...
# feel free to import additional things from those packages already imported
# or the Python Standard Library (https://docs.python.org/3/library/)
# (if it helps) but do not import other 3rd party packages.
import numpy as np
from cobra.io import read_sbml_model
from cobra.util import create_stoichiometric_matrix

# Read model (central metabolism model of Escherichia coli)
model = read_sbml_model('e_coli_core.xml')
# Create stoichiometric matrix
S = create_stoichiometric_matrix(model)


# 1. Binarize S

# replace _ with a binary representation of S.
# S_bin should only contain floating point numbers (either 0. or 1.)

S_bin = _

###### Don't touch
def test_binary_stoichiometry_matrix():
    assert hashlib.md5(S_bin).digest() == b'\xcd\xd3\x04N\x9e\xaf\x1f\xc5\xcb9\x9f\xaaa\x00\x06['
###### this


# 2. Compute reaction adjacency matrix A_v.

A_v = _

###### Don't touch
def test_reaction_adjacency_matrix():
    assert hashlib.md5(A_v).digest() == b'"TTS\xba\x07\xfa\x06m{\xa6\xbc^l\\.'
###### this


# 3. Compute compound adjacency matrix A_x.

A_x = _

###### Don't touch
def test_compound_adjacency_matrix():
    assert hashlib.md5(A_x).digest() == b'"\x1d_\\\x9a\xc3O\xfe0\x98\xf0\t3\xb8\x0e\x0c'
###### this


# 4. Based on A_x, which metabolite participates in the most reactions?

# Hints: model.metabolites behaves like a list or array so you can
# get a specific metabolite using an index e.g. model.metabolites[0]
# will give you the first metabolite

# replace _ with the most connected metabolite in the model;
# needs to be of type cobra.core.metabolite.Metabolite (you can check with type())
# e.g. type(model.metabolites[0]) == cobra.core.metabolite.Metabolite
most_connected_metabolite = _

###### Don't touch
def test_most_connected_metabolite():
    assert hashlib.md5(most_connected_metabolite.id.encode('utf-8')).digest() == b"\x90\xf7\xa1\xa0\x1a\x0e\x92'\x02\xd1\xdd.\xb6bu\x0e"
###### this


# 5. Based on A_x, how many reactions does metabolite atp_c participate in?

# Hints: You can retrieve a metabolite from the model using its ID
# using model.metabolites.get_by_id. For example, you could retrieve
# water inside the c(ytosol) compartment using model.metabolites.get_by_id('h2o_c')
# Furthermore, since model.metabolites behaves just like a list or array, it
# also supports model.metabolites.index(your_metabolite).

# Replace _ with the number of reactions apt_c participates in (should be a number).
atp_participation = _

###### Don't touch
def test_atp_participation():
    assert atp_participation == 13
###### this


# 6. How many metabolites do the reactions ACALD and ALCD2x share. Those IDs refer
# to Acetaldehyde dehydrogenase (acetylating) and Alcohol dehydrogenase (ethanol)
# respectively.

# Hints: similar to model.metabolites, model.reactions.get_by_id and
# model.reactions.index are available to retrieve a specific reaction
# and find the index of a specific reaction.


# Replace _ with number of metabolites ACALD and ALCD2x share (should be a number).
metabolites_in_common = _


###### Don't touch
def test_ACALD_ALCAD2x_metabolites_in_common():
    assert metabolites_in_common == 4
###### this


# 7. Find the top 10 most connected metabolites.
# Hint:
# 1. You can use `zip` to zip two lists together. zip(['a', 'b', 'c'], [1, 2, 3]) => zip([['a', 1], ...]) 
# 2. You can use Python's `sorted` function to sort a list or a list of lists. You can provide
#    a function to `sorted`'s `key=` argument to let `sorted` know on what element to sort.
#    For example `sorted(zip([['a', 1], ...]), key=lambda item: item[1])` will sort based on the 2nd
#    element of each sublist (i.e. the numbers, not the letters).

# Replace _ with a list of metabolites (all of type cobra.core.metabolite.Metabolite) that
# correspond to the top 10 most connected metabolites (in ascending order)
top10 = [item[0] for item in metabolite_degree_zip][0:10]

###### Don't touch
def test_top10():
	truth = ['h_c', 'h2o_c', 'h_e', 'atp_c', 'adp_c', 'nad_c', 'nadh_c', 'pi_c', 'pyr_c', 'co2_c']
	assert [metabolite.id for metabolite in top10] == truth
###### this




