import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
# from xgboost import plot_importance, XGBRegressor, XGBClassifier
from sklearn.model_selection import train_test_split, KFold
from sklearn.linear_model import LinearRegression, ElasticNet
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor


def lr(X_train, X_validation, y_train, y_validation, pred):
    '''
    This function is for Linear regression.

    :param X_train: After split to train data
    :param X_validation: Train data's label
    :param y_train: After split to validation data
    :param y_validation: Validation data's label
    :param pred: Test data
    :return: Test data result
    '''
    lr = LinearRegression()  # navie # xgb # svm
    lr.fit(X_train, y_train)

    # # predict
    y_pred = lr.predict(pred)
    print('Training Score: ', lr.score(X_train, y_train))
    print('Target Score: ', lr.score(X_validation, y_validation))
    # print(y_pred)
    return y_pred


def Svr(X_train, X_validation, y_train, y_validation, pred, kernel):
    '''
    This function is for SVR.

    :param X_train: After split to train data
    :param X_validation: Train data's label
    :param y_train: After split to validation data
    :param y_validation: Validation data's label
    :param pred: Test data
    :param kernel: kernel type
    :return: Test data result
    '''
    svm = SVR(kernel=kernel, C=1, gamma='auto')  # choose the different kernel, penalty coefficient, and gamma
    # svm = SVR(degree=3) # Polynomial
    svm.fit(X_train, y_train.ravel())
    y_pred = svm.predict(pred)
    # print('Kernel: ', kernel)
    # print('Polynomial:')
    print('Training Score: ', svm.score(X_train, y_train))
    print('Target Score: ', svm.score(X_validation, y_validation))
    return y_pred


def Elastnet(X_train, X_validation, y_train, y_validation, pred):
    '''
    This function is for ElastNet.

    :param X_train: After split to train data
    :param X_validation: Train data's label
    :param y_train: After split to validation data
    :param y_validation: Validation data's label
    :param pred: Test data
    :return: Test data result
    '''
    ela = ElasticNet()
    ela.fit(X_train, y_train)
    y_pred = ela.predict(pred)
    print('Training Score: ', ela.score(X_train, y_train))
    print('Target Score: ', ela.score(X_validation, y_validation))
    return y_pred


def xgboost(X_train, X_validation, y_train, y_validation, pred):
    '''
    This function is for xgboost. But I can't use it on mac.

    :param X_train: After split to train data
    :param X_validation: Train data's label
    :param y_train:  After split to validation data
    :param y_validation: Validation data's label
    :param pred: Test data
    :return: Test data result
    '''
    # model = XGBRegressor(max_depth=5, learning_rate=0.1, n_estimators=160, silent=False, objective='reg:gamma')
    # model.fit(X_train, y_train)
    xgc = XGBClassifier()
    xgc.fit(X_train, y_train)
    y_pred = xgc.predict(pred)
    print('Training Score: ', xgc.score(X_train, y_train))
    print('Target Score: ', xgc.score(X_validation, y_validation))
    # plot_importance(model)
    # plt.show()
    return y_pred


def KFOLD(kf, X, y):
    '''
    This function is for Linear Regression K-Fold.

    :param kf: Amount of k want to split
    :param X: Training data
    :param y: Label
    :return: MSE, RMSE
    '''
    # K-fold
    mses = []
    rmses = []
    for train_indices, validation_indices in kf.split(X):
        X_train, X_validation, y_train, y_validation = X[train_indices, :], X[validation_indices, :], y[train_indices], \
                                                       y[validation_indices]
        lr = LinearRegression()
        lr.fit(X_train, y_train)
        y_pred = lr.predict(X_validation)
        mses.append(mean_squared_error(y_validation, y_pred))
        rmses.append(np.sqrt(metrics.mean_squared_error(y_validation, y_pred)))
        # print(y_pred)
    print('MSES:\n', mses)
    print('Average MSE:\n', sum(mses) / len(mses))
    print('RMSES:\n', rmses)
    print('Average RMSES:\n', sum(rmses) / len(rmses))


def RF(X_train, X_validation, y_train, y_validation, pred):
    '''
    This function is for Random Forest Regression.

    :param X_train: After split to train data
    :param X_validation: Train data's label
    :param y_train: After split to validation data
    :param y_validation: Validation data's label
    :param pred: Test data
    :return: Test data result
    '''
    rf = RandomForestRegressor()
    rf.fit(X_train, y_train)
    y_pred = rf.predict(pred)
    print('Training Score: ', rf.score(X_train, y_train))
    print('Target Score: ', rf.score(X_validation, y_validation))
    return y_pred


def evaluate(x_train, y_train, x_test, y_test):
    '''
    This function can predict 6 models and compare each other, and return the mae, rmse.

    :param x_train: After split to train data
    :param y_train: Train data's label
    :param x_test: After split to validation data
    :param y_test: Validation data's label
    :return: Test data result
    '''
    model_name_list = ['Linear Regression', 'SVR', 'ElasticNet', 'Random Forest', 'Extra Tree', 'Gradient Boost']

    model1 = LinearRegression()
    model2 = SVR(degree=3)
    model3 = ElasticNet()
    model4 = RandomForestRegressor()
    model5 = ExtraTreesRegressor()
    model6 = GradientBoostingRegressor()

    # Evaluate the models performance
    results = pd.DataFrame(index=model_name_list, columns=['mae', 'rmse'])

    for i, model in enumerate([model1, model2, model3, model4, model5, model6]):
        model.fit(x_train, y_train.ravel())
        predictions = model.predict(x_test)

        mae = np.mean(abs(predictions - y_test))
        rmse = np.sqrt(np.mean((predictions - y_test) ** 2))

        model_name = model_name_list[i]
        results.iloc[i, :] = [mae, rmse]

    # 建立基本盤 如果比基本盤爛的model就沒必要看了
    baseline = np.median(y_train)
    baseline_mae = np.mean(abs(baseline - y_test))
    baseline_rmse = np.sqrt(np.mean((baseline - y_test) ** 2))

    results.loc['baseline', :] = [baseline_mae, baseline_rmse]
    return results
