from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__, template_folder='templates')

# Connect to the MySQL database
mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="password",
#   database="crm_db"

  host="database-1.cnqllsk6icp0.eu-north-1.rds.amazonaws.com",
  user="admin",
  password="test_123",
  database="database-1"
)

# Define a cursor object to interact with the database
mycursor = mydb.cursor()

# Route to display the form to create a new customer
@app.route('/')
def new_customer():
    return render_template('index.html')

# Route to process the form data and insert a new customer record into the database
@app.route('/create_customer', methods=['POST'])
def create_customer():
    name = request.form['name']
    address = request.form['address']
   
    sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
    val = (name, address)
    mycursor.execute(sql, val)
    mydb.commit()
    return redirect('/customers')

# Route to display a list of all customers
@app.route('/customers')
def customer_list():
    mycursor.execute("SELECT * FROM customer")
    results = mycursor.fetchall()
    return render_template('index.html', customers=results)

# Route to delete a customer record from the database
@app.route('/delete_customer/<int:id>')
def delete_customer(id):
    sql = "DELETE FROM customers WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    return redirect('/customers')

if __name__ == '__main__':
    app.run(debug=True)
