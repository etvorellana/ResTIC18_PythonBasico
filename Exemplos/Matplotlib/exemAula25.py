import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
plt.style.use('classic') 

def regressao_linear(x, y):
    # Vamos criar um modelo de regressão linear
    model = LinearRegression()
    # Vamos treinar o modelo
    model.fit(x, y)
    # Vamos fazer a predição
    y_pred = model.predict(x)
    return y_pred


def main():
    # Quarteto de Anscombe
    QA_x1 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
    QA_y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

    QA_x2 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
    QA_y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]

    QA_x3 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
    QA_y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]

    QA_x4 = [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 19.0, 8.0, 8.0, 8.0]
    QA_y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

    # Vamos converter cada quarteto em um ndarray
    QA_x1 = np.array(QA_x1)
    QA_y1 = np.array(QA_y1)
    QA_x2 = np.array(QA_x2)
    QA_y2 = np.array(QA_y2)
    QA_x3 = np.array(QA_x3)
    QA_y3 = np.array(QA_y3)
    QA_x4 = np.array(QA_x4)
    QA_y4 = np.array(QA_y4)

    # Vamos criar um DataFrame com os dados
    colunas = pd.MultiIndex.from_product((['I', 'II', 'III', 'IV'], ['x', 'y']), 
                                         names=['Quarteto', 'Coordenada'])
    index = [str(i) for i in range(1,12)]
    index = pd.Index(index, name="Obs. ")
    QA = np.array([QA_x1, QA_y1, QA_x2, QA_y2, 
                   QA_x3, QA_y3, QA_x4, QA_y4]).T
    QA = pd.DataFrame(QA, columns=colunas, index=index)
    # Adicionando a média o desvio padrão e a variância
    QA.loc["Mean", :] = QA.mean() 
    QA.loc["Std", :] = QA.std()
    QA.loc["Var", :] = QA.var()
    # Adicionando a correlação
    # Corr(x, y) = cov(x, y) / (std(x) * std(y))
    QA.loc["Corr", ('I', 'x')] = np.corrcoef(QA.loc['1':'11', ('I', 'x')], QA.loc['1':'11', ('I', 'y')])[0,1]
    QA.loc["Corr", ('II', 'x')] = np.corrcoef(QA.loc['1':'11', ('II', 'x')], QA.loc['1':'11', ('II', 'y')])[0,1]
    QA.loc["Corr", ('III', 'x')] = np.corrcoef(QA.loc['1':'11', ('III', 'x')], QA.loc['1':'11', ('III', 'y')])[0,1]
    QA.loc["Corr", ('IV', 'x')] = np.corrcoef(QA.loc['1':'11', ('IV', 'x')], QA.loc['1':'11', ('IV', 'y')])[0,1]
    QA.loc["Corr", ('I', 'y')] = np.corrcoef(QA.loc['1':'11', ('I', 'y')], QA.loc['1':'11', ('I', 'x')])[0,1]
    QA.loc["Corr", ('II', 'y')] = np.corrcoef(QA.loc['1':'11', ('II', 'y')], QA.loc['1':'11', ('II', 'x')])[0,1]
    QA.loc["Corr", ('III', 'y')] = np.corrcoef(QA.loc['1':'11', ('III', 'y')], QA.loc['1':'11', ('III', 'x')])[0,1]
    QA.loc["Corr", ('IV', 'y')] = np.corrcoef(QA.loc['1':'11', ('IV', 'y')], QA.loc['1':'11', ('IV', 'x')])[0,1]

    # Ajustando os modelos de regressão linear
    modelos = []
    QA.loc["Regressão R2", :] = np.zeros(8)
    QA.loc["Regressão a", :] = np.zeros(8)
    QA.loc["Regressão b", :] = np.zeros(8)
    for i in range(4):
        x = QA.values[0:11, 2*i].reshape(-1, 1)
        y = QA.values[0:11, 2*i + 1]
        modelos.append(LinearRegression())
        modelos[i].fit(x, y)
        r2 = modelos[i].score(x, y)
        b = modelos[i].intercept_
        a = modelos[i].coef_
        QA.loc["Regressão R2", colunas[2*i]] = r2
        QA.loc["Regressão a", colunas[2*i]] = a
        QA.loc["Regressão b", colunas[2*i]] = b


    print("Quarteto de Anscombe")
    print(QA)

    # Vamos escolher o menor e o maior valor de x de todas as series
    x_min = QA.values[0:11, 0::2].min()
    x_max = QA.values[0:11, 0::2].max()
    # gerar um conjunto de valores de x para predizer os valores de y
    QA_x_pred = np.linspace(x_min - 1, x_max + 1, 20).reshape(-1, 1)
    QA_y_pred = np.zeros((20, 4))
    for i in range(4):
        QA_y_pred[:, i] = modelos[i].predict(QA_x_pred)
    
    # Vamos plotar os dados
    fig = plt.figure()
    plt.plot(QA_x_pred, QA_y_pred[:, 0], '-', label='QA1_model')
    plt.plot(QA_x_pred, QA_y_pred[:, 1], '-', label='QA2_model')
    plt.plot(QA_x_pred, QA_y_pred[:, 2], '-', label='QA3_model')
    plt.plot(QA_x_pred, QA_y_pred[:, 3], '-', label='QA4_model')
    plt.show()


    
    

if __name__ == "__main__":
    main()