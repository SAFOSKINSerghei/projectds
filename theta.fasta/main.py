from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

data = pd.read_csv('dataset.csv')

y = data[['ref_index']]
x = data[['val_num', 'pos']]
x_tr, x_ts, y_tr, y_ts = train_test_split(x, y, test_size=0.1, shuffle=True)
model = RandomForestClassifier(n_estimators=200, max_depth=28, max_features='log2')
model.fit(x_tr, y_tr)
y_pr = model.predict(x_ts)

print(confusion_matrix(y_ts, y_pr))
print('Accurency score is ', str(round(accuracy_score(y_ts, y_pr) * 100, 2)) + '%')


