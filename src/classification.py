import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import sklearn.model_selection as model_selection
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import confusion_matrix

from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier


def calculate_features(array):
    points_centered = array - np.mean(array, axis=0)
    pca = PCA(n_components=3)
    pca.fit(points_centered)
    eigenvalues = pca.explained_variance_

    relative_height = np.max(array[:, 2]) - np.min(array[:, 2])

    width_temp = np.max(array[:, 0]) - np.min(array[:, 0])
    length_temp = np.max(array[:, 1]) - np.min(array[:, 1])
    width = min(width_temp, length_temp)
    length = max(width_temp, length_temp)

    bbox_vol = width * relative_height * length

    return np.array([relative_height, length, width, bbox_vol, eigenvalues[0], eigenvalues[1]])


def calculate_matric(ylabel, ypred):
    OA = accuracy_score(ylabel, ypred)
    mA = balanced_accuracy_score(ylabel, ypred)
    class_names = [0, 1, 2, 3, 4]
    disp_names = ['building', 'car', 'fence', 'pole', 'tree']
    conf = confusion_matrix(ylabel, ypred, labels=class_names)
    disp = ConfusionMatrixDisplay(confusion_matrix=conf, display_labels = disp_names)
    disp.plot()
    plt.show()
    return OA, mA, conf

def main():
    # loop over the 500 files to generate input datasets
    l1 = []
    for i in range(500):
        file_name = '../data/{:03d}.xyz'.format(i)
        # print(file_name)
        data = np.genfromtxt(file_name, usecols=[0, 1, 2])
        features = calculate_features(data)
        l1.append(features)

    data_list = np.array(l1)

    # read data and calculate features

    # create ground truth label set
    b = np.repeat(0, 100)  # 1-building
    c = np.repeat(1, 100)  # 2-car
    f = np.repeat(2, 100)  # 3-fence
    p = np.repeat(3, 100)  # 4-pole
    t = np.repeat(4, 100)  # 5-tree
    label = np.concatenate((b, c, f, p, t))

    # breakpoint()
    # SVM classification
    X_train, X_test, y_train, y_test = model_selection.train_test_split(data_list, label,
                                                                        train_size=0.60, test_size=0.4,
                                                                        random_state=101)

    svm = SVC(kernel='linear', C=100).fit(X_train, y_train)
    rf = RandomForestClassifier(max_depth=20, min_samples_leaf=2, min_samples_split=10, n_estimators=50,
                                random_state=42).fit(X_train, y_train)

    svm_pred = svm.predict(X_test)
    rf_pred = rf.predict(X_test)
    OA_svm, mA_svm, conf_svm = calculate_matric(y_test, svm_pred)
    OA_rf, mA_rf, conf_rf = calculate_matric(y_test, rf_pred)

    print("For SVM, Overall Accuracy: {0}, Mean Accuracy: {1}".format(OA_svm, mA_svm))
    print("For RF, Overall Accuracy: {0}, Mean Accuracy: {1}".format(OA_rf, mA_rf))

if __name__ == '__main__':
    main()
