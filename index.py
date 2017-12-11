import dataset_reader
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

excel_workbook_path = 'D:\PycharmProjects\PythonLabs\Нейронные сети\BackPropagation\\athero.xls'

input_dataset = dataset_reader.get_dataset(excel_workbook_path).values

x_vector = input_dataset[:, 1:23]
y_vector = input_dataset[:, 0]

x_train, x_test, y_train, y_test = train_test_split(x_vector, y_vector, test_size=0.30)

mlp_classifier = MLPClassifier(hidden_layer_sizes=(6, 1),
                               max_iter=100,
                               alpha=1e-5,
                               solver='lbfgs',
                               activation='logistic',
                               learning_rate_init=.5)

mlp_classifier.fit(x_train, y_train)

print("Training set accuracy: %f" % mlp_classifier.score(x_train, y_train))
print("Test set accuracy: %f" % mlp_classifier.score(x_test, y_test))

seed = 2605
estimators = []
estimators.append(('mlp', mlp_classifier))
pipeline = Pipeline(estimators)
kfold = KFold(shuffle=True, random_state=seed)
results = cross_val_score(pipeline, x_vector, y_vector, cv=kfold, pre_dispatch='5')
print("Result: %.2f%% +-(%.2f%%)" % (results.mean() * 100, results.std() * 100))
