from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

data = pd.read_csv('dataset.csv')

y = data[['ref_index']]
x = data[['val_num', 'pos']]
model = RandomForestClassifier(n_estimators=200, max_depth=28, max_features='log2')
model.fit(x, y)

data_ts = pd.read_csv('samples.csv')
x_ts = data_ts[['val_num', 'pos']]
y_pr = model.predict(x_ts)
data_ts['y_pred'] = y_pr
data_ts.to_csv('samples_pred.csv')
