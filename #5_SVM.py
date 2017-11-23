import read_dataset
from sklearn.externals import joblib 
from sklearn import svm
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.model_selection import GridSearchCV

size = 100
window = 7
min_count = 7

vector_train_neg_fname = 'data/structured/vector{}_{}_{}/train/neg.pkl'.format(size,window,min_count)
# print(vector_train_neg_fname)
vector_train_neg = read_dataset.load(vector_train_neg_fname)

vector_train_pos_fname = 'data/structured/vector{}_{}_{}/train/pos.pkl'.format(size,window,min_count)
# print(vector_train_pos_fname)
vector_train_pos = read_dataset.load(vector_train_pos_fname)

vector_neg_len = len(vector_train_neg)
vector_pos_len = len(vector_train_pos)

train_percent = 0.1
test_percent = 0.05

train_num = int(train_percent * vector_neg_len)
test_num = int(test_percent * vector_neg_len)

vector_train = vector_train_neg[:train_num] + vector_train_pos[:train_num]
vector_test = vector_train_neg[train_num : test_num + train_num] + vector_train_pos[train_num : test_num + train_num]

svm = svm.SVC()

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


# svm.fit(vector_train, class_vector)


parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}

clf = GridSearchCV(svm, parameters, cv=3, n_jobs=4)
clf.fit(vector_train, class_vector)
sorted(clf.cv_results_.keys())

results = clf.predict(vector_test)

cnt_true = 0
for i, result in enumerate(results):
    if result == class_vector_test[i]:
        cnt_true = cnt_true + 1

accuracy = cnt_true / float(len(results))
precision = precision_score(class_vector_test, results)
recall = recall_score(class_vector_test, results)
f1score = f1_score(class_vector_test, results)

print("Accuracy = " + str(accuracy))
print("Precision = " + str(precision))
print("Recall = " + str(recall))
print("F1 = " + str(f1score))

# clf_pos = svm.SVC()
# clf_pos.fit(vector_train_pos,[1])

def saveModel(clf, filename):
    joblib.dump(clf,"model/" + filename)

saveModel(clf, "model_svm_sampling_train_{}_{}_{}.pkl".format(size,window,min_count))