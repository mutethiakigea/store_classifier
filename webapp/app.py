from flask import Flask, render_template, request, redirect
from db_config import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']
    phone = request.form['phone']
    gender = request.form['gender']  # Get the gender from the form
    region = request.form['region']  # Get the region from the form

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (name, age, email, phone, gender, region) VALUES (%s, %s, %s, %s, %s, %s)', (name, age, email, phone, gender, region))
    connection.commit()
    cursor.close()
    connection.close()

    # Optionally push data to Power BI (if applicable)
    # push_data_to_power_bi(name, age, email, phone, gender, region)

    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
