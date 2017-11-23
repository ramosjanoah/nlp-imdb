import read_dataset
from sklearn import svm

vector_train_neg = read_dataset.load('data/structured/vector/train/neg.pkl')
vector_train_pos = read_dataset.load('data/structured/vector/train/pos.pkl')

vector_neg_len = len(vector_train_neg)
vector_pos_len = len(vector_train_pos)

train_percent = 0.5
test_percent = 0.2

train_num = int(train_percent * vector_neg_len)
test_num = int(test_percent * vector_neg_len)

vector_train = vector_train_neg[:train_num] + vector_train_pos[:train_num]
vector_test = vector_train_neg[train_num : test_num + train_num] + vector_train_pos[train_num : test_num + train_num]

clf = svm.SVC()

class_vector_neg = []
for i in range (0,train_num):
    class_vector_neg.append(0)

class_vector_pos = []
for i in range (0,train_num):
    class_vector_pos.append(1)

class_vector = class_vector_pos + class_vector_neg

class_vector_neg_test = []
for i in range (0,test_num):
    class_vector_neg_test.append(0)

class_vector_pos_test = []
for i in range (0,test_num):
    class_vector_pos_test.append(1)

class_vector_test = class_vector_pos_test + class_vector_neg_test


clf.fit(vector_train, class_vector)
results = clf.predict(vector_test)

cnt_true = 0
for i, result in enumerate(results):
    if result == class_vector_test[i]:
        cnt_true = cnt_true + 1

accuracy = cnt_true / float(len(results))
print(accuracy)
# clf_pos = svm.SVC()
# clf_pos.fit(vector_train_pos,[1])