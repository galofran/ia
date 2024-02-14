import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
import joblib

data = pd.read_csv('dataset.csv')

X = data[['total_bill', 'day', 'time', 'size']]
y = data['propina']

encoder = OneHotEncoder(drop='first')
X_encoded = encoder.fit_transform(X[['day', 'time']])
feature_names = encoder.get_feature_names_out(['day', 'time'])
X_encoded_df = pd.DataFrame(X_encoded.toarray(), columns=feature_names)  # Convertir a matriz densa

X_encoded_df.reset_index(drop=True, inplace=True)  # Reiniciar índices para asegurar alineación
X.reset_index(drop=True, inplace=True)

X = pd.concat([X.drop(['day', 'time'], axis=1), X_encoded_df], axis=1)

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'tip_prediction_model.pkl')

loaded_model = joblib.load('tip_prediction_model.pkl')

new_data = pd.DataFrame({
    'total_bill': [30.00],
    'day': ['sunday'],
    'time': ['dinner'],
    'size': [4]
})

new_data_encoded = encoder.transform(new_data[['day', 'time']])
new_data_encoded_df = pd.DataFrame(new_data_encoded.toarray(), columns=feature_names)  # Convertir a matriz densa
new_data_encoded_df.reset_index(drop=True, inplace=True)
new_data.reset_index(drop=True, inplace=True)

new_data_final = pd.concat([new_data.drop(['day', 'time'], axis=1), new_data_encoded_df], axis=1)

predicted_tip = loaded_model.predict(new_data_final)

formatted_tip = "{:.2f}".format(predicted_tip[0])
print('Predicted Tip: ', formatted_tip)

if float(formatted_tip) > 5:
    print("Tienes buena propina we")
else:
    print("No tengo ni para pipas")

