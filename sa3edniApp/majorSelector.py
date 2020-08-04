import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

def predict(data):
    dataset = pd.read_csv("/home/sa3edni/mysite/sa3edniApp/majors.csv")
    properties = dataset.drop("Major",axis = 1)
    results = dataset.Major
    properties_train, properties_test, results_train, results_test = train_test_split(properties, results, test_size = 0.28, random_state = 42)
    model = SVC(kernel='linear')
    model.fit(properties_train, results_train)
    return model.predict([data])[0]
