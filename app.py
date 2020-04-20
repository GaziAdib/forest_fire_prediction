from flask import Flask, flash, url_for, request, render_template, redirect
import pickle
import numpy as np

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('forest_fire.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output > str(0.5):
        return render_template("forest_fire.html",pred_text='Your forest is in Danger.\n Probability of fire occuring is {}'.format(output))
    else:
        return render_template("forest_fire.html",pred_text='Your forest is Safe.\n Probability of fire occuring is {}'.format(output))
 


if __name__ ==' __main__':
    app.run(debug=True)


