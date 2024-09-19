from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)  # Corrected __name_

# Load and prepare the dataset
data = pd.read_csv(r'C:\Users\sundarlal\Desktop\stock\New folder\archive (4)\NIFTY50_all.csv')

# Features and target (e.g., predict 'Close' price using other features)
X = data[['Open', 'High', 'Low', 'Volume']]
y = data['Close']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        # Capture input data from the form
        open_price = float(request.form['open'])
        high_price = float(request.form['high'])
        low_price = float(request.form['low'])
        volume = float(request.form['volume'])
        
        # Create a prediction based on input
        predicted_close = model.predict([[open_price, high_price, low_price, volume]])[0]
        
        return redirect(url_for('result', prediction=predicted_close))
    
    return render_template('prediction.html')

@app.route('/result')
def result():
    prediction = request.args.get('prediction', None)
    return render_template('result.html', prediction=prediction)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '_main':  # Corrected __name_
    app.run(debug=True)