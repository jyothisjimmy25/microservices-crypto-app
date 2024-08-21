from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/payment')
def payment():
    order_id = request.args.get('order_id')
    name = request.args.get('name')
    address = request.args.get('address')
    quantity = request.args.get('quantity')
    product_id = request.args.get('product_id')
    return render_template('payment.html', order_id=order_id, name=name, address=address, quantity=quantity, product_id=product_id)

@app.route('/process_payment', methods=['POST'])
def process_payment():
    card_number = request.form['card_number']
    expiry_date = request.form['expiry_date']
    cvv = request.form['cvv']
    order_id = request.form['order_id']
    name = request.form['name']
    address = request.form['address']
    quantity = request.form['quantity']
    product_id = request.form['product_id']

    # Simulate payment processing
    payment_successful = True  # Replace with actual payment logic

    if payment_successful:
        return redirect(url_for('order_confirmation', name=name, address=address, quantity=quantity, product_id=product_id, order_id=order_id))
    else:
        return redirect(url_for('place_order', product_id=product_id))

@app.route('/order_confirmation')
def order_confirmation():
    name = request.args.get('name')
    address = request.args.get('address')
    quantity = request.args.get('quantity')
    product_id = request.args.get('product_id')
    order_id = request.args.get('order_id')
    return render_template('order_confirmation.html', name=name, address=address, quantity=quantity, product_id=product_id, order_id=order_id)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect("http://127.0.0.1:5000/")  # Redirect to the login service

if __name__ == '__main__':
    app.run(port=5002, debug=True)
