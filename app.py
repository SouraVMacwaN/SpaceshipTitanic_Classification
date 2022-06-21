from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("space_ship.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("page.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        CryoSleep = request.form['CryoSleep']
        if CryoSleep == 'Yes':
            CryoSleep = 1

        else:
            CryoSleep = 0



        Destination = request.form['Destination']
        if Destination == "1":
            Destination = 0

        elif Destination == "2":
            Destination = 1

        else:
            Destination = 2

        print(Destination)
        
        VIP = request.form['VIP']
        if (VIP == 'Yes'):
            VIP = 1

        else:
            VIP = 0



        HomePlanet = request.form['HomePlanet']
        if (HomePlanet == 'Europa'):
            Europa = 1
            Mars = 0

        elif (HomePlanet == 'Mars'):
            Europa = 0
            Mars = 1

        else:
            Europa = 0
            Mars = 0




        Age = int(request.form["Destination"])
        RoomService = float(request.form["RoomService"])
        FoodCourt = float(request.form["FoodCourt"])
        ShoppingMall = float(request.form["ShoppingMall"])
        Spa = float(request.form["Spa"])
        VRDeck = float(request.form["VRDeck"])


        prediction = model.predict([[
            CryoSleep,
            Destination,
            Age,
            VIP,
            RoomService,
            FoodCourt,
            ShoppingMall,
            Spa,
            VRDeck,
            Europa,
            Mars
        ]])

        output = prediction[0]
        if output == 0:
            ans = 'No'
        else:
            ans = 'Yes'
        return render_template('page.html', prediction_text="Your Prediction is : {}".format(ans))

    return render_template("page.html")


if __name__ == "__main__":
    app.run(debug=True)