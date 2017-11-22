import dill
polarity = 'pos'
testtrain = 'test'
prefix = 'filtered'

data = []
load_file_path = 'structured/{}/{}/{}.pkl'.format(testtrain, prefix ,polarity)
with open(load_file_path, 'rb') as fi:
	data = dill.load(fi)

print('Loading	:', load_file_path)

new_data = []
for datum in data:
	words, tags = zip(*datum)
	words = list(words)
	new_data.append(words)

save_prefix = 'filtered/words'
save_file_path = 'structured/{}/{}/{}.pkl'.format(testtrain, save_prefix ,polarity)

with open(save_file_path, 'wb') as fo:
	dill.dump(new_data, fo)

print('Saved in	:', save_file_path)
print(new_data[0])