# -*- coding: utf-8 -*-
# Regressão linear por cultura (um modelo por Crop)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# === 1) Carregar dados ===
df = pd.read_csv("crop_yield.csv")  # ajuste o caminho se necessário

# === 2) Definir colunas numéricas preditoras (todas menos Yield e Crop) ===
num_cols = [
    "Precipitation (mm day-1)",
    "Specific Humidity at 2 Meters (g/kg)",
    "Relative Humidity at 2 Meters (%)",
    "Temperature at 2 Meters (C)",
]

# (se houver NaNs, você pode decidir imputar ou remover)
df = df.dropna(subset=num_cols + ["Yield", "Crop"]).copy()

# === 3) Loop por cultura ===
resultados = []          # métricas por cultura
coeficientes = []        # coeficientes por cultura

for crop, g in df.groupby("Crop"):
    # garantir um mínimo de amostras para treino/teste
    if len(g) < 8:
        # pula culturas com pouquíssimos dados
        resultados.append({
            "Crop": crop,
            "n_samples": len(g),
            "R2": np.nan,
            "MSE": np.nan,
            "MAE": np.nan,
            "Obs": "amostras insuficientes (<8)"
        })
        continue

    X = g[num_cols].values
    y = g["Yield"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
        # se a série temporal/importa a ordem, troque por uma separação temporal
    )

    # padronização (boa prática para comparar coeficientes entre features)
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s  = scaler.transform(X_test)

    # modelo
    model = LinearRegression()
    model.fit(X_train_s, y_train)

    # previsão e métricas
    y_pred = model.predict(X_test_s)
    r2  = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    resultados.append({
        "Crop": crop,
        "n_samples": len(g),
        "R2": r2,
        "MSE": mse,
        "MAE": mae,
        "Obs": ""
    })

    # guardar coeficientes + intercepto; com scaler, coeficientes são por desvio-padrão
    for feat, coef in zip(num_cols, model.coef_):
        coeficientes.append({
            "Crop": crop,
            "Variavel": feat,
            "Coeficiente": coef
        })
    coeficientes.append({
        "Crop": crop,
        "Variavel": "Intercepto",
        "Coeficiente": model.intercept_
    })

# === 4) DataFrames de saída ===
df_resultados = pd.DataFrame(resultados).sort_values(["R2", "MAE"], ascending=[False, True])
df_coef = pd.DataFrame(coeficientes)

# Exibir/resumir
print("\n=== Métricas por cultura ===")
print(df_resultados.to_string(index=False))

print("\n=== Coeficientes por cultura ===")
# se quiser ver só os top coeficientes por cultura:
for crop in df_coef["Crop"].unique():
    print(f"\n-- {crop} --")
    print(df_coef[df_coef["Crop"] == crop].to_string(index=False))
