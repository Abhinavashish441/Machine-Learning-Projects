import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
# Code By Abhinav Ashish
url = 'https://raw.githubusercontent.com/Abhinavashish441/Machine-Learning-Projects/main/data/diabetes.csv'
diabetes_dataset = pd.read_csv(url)

X = diabetes_dataset.drop(columns = 'Outcome', axis =1)
y = diabetes_dataset.Outcome

scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)
standardized_data
X = standardized_data
y = diabetes_dataset.Outcome
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2,stratify=y,random_state=2)
classifier = svm.SVC(kernel = 'linear')
classifier.fit(X_train,y_train)
# accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, y_train)
print('Accuracy score of the training data : ', training_data_accuracy)
# accuracy score on the test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, y_test)
print('Accuracy score of the test data : ', test_data_accuracy)
print('Accuracy score of the test data : ', test_data_accuracy)
new_data = pd.DataFrame({
   'Pregnancies':5,
   'Glucose':166,
  'BloodPressure':72,
  	'SkinThickness':19,
    	'Insulin':175,
      	'BMI':25.8,
        	'DiabetesPedigreeFunction':0.587,
          	'Age':51, 
},index=[0])
import joblib
joblib.dump(classifier,'Diabetes')
model = joblib.load('Diabetes')
model.predict(new_data)


from tkinter import *
import joblib
def show_entry_fields():
    p1=int(e1.get())
    p2=int(e2.get())
    p3=int(e3.get())
    p4=int(e4.get())
    p5=int(e5.get())
    p6=int(e6.get())
    p7=int(e7.get())
    p8=int(e8.get())

    model = joblib.load('Diabetes')
    result=model.predict([[p1,p2,p3,p4,p5,p6,p7,p8]])
    
    if result == 0:
        Label(master, text="No Diabetes").grid(row=31)
    else:
        Label(master, text="Possibility of Diabetes").grid(row=31)
    
    
master = Tk()
master.title("Diabetes Prediction System ")


label = Label(master, text = "Diabetes Prediction System "
                          , bg = "black", fg = "white"). \
                               grid(row=0,columnspan=2)

#Code By Abhinav Ashish
Label(master, text="Pragnencies").grid(row=1)
Label(master, text="Glucose").grid(row=2)
Label(master, text="Blood Pressure").grid(row=3)
Label(master, text="Skin Thickness").grid(row=4)
Label(master, text="Insuline").grid(row=5)
Label(master, text="BMI").grid(row=6)
Label(master, text="Diabetes Pedigree Function").grid(row=7)
Label(master, text="Age").grid(row=8)




e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)


e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
e7.grid(row=7, column=1)
e8.grid(row=8, column=1)




Button(master, text='Predict', command=show_entry_fields).grid()

mainloop()
