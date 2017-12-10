import dataset_reader
import encoding
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder

excel_workbook_path = 'D:\PycharmProjects\PythonLabs\Нейронные сети\BackPropagation\\athero.xls'

input_dataset = dataset_reader.get_dataset(excel_workbook_path).values

x_vector = input_dataset[:, 1:24]
encoded_x_vector = encoding.x_encoding(x_vector)
y_vector = input_dataset[:, 0]
encoded_y_vector = encoding.y_encoding(y_vector)

# newDataset = []

# for datasetRow in x_vector:
#     print(datasetRow)

# print(x_vector[0])
# lc.fit(x_vector[0])

# for row in x_vector:
#     print(lc.fit(row))



# lc.fit(x_vector)

# X = lc.transform(x_vector)
# Y = lc.transform(y_vector)
# print(X)
# print(Y)
# print(lc.fit(inputDataset)[0][0])
# print(scaler.fit(inputDataset[0]))

# clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
# clf.fit(inputDataset, [0, 1])
