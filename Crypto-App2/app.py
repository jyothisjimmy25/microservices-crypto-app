from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/products')
def products():
    return render_template('product.html')

@app.route('/place_order')
def place_order():
    product_id = request.args.get('product')
    return render_template('place_order.html', product_id=product_id)

@app.route('/submit_order', methods=['POST'])
def submit_order():
    # Simulate order submission
    name = request.form['name']
    address = request.form['address']
    quantity = request.form['quantity']
    product_id = request.form['product_id']
    # URL encode parameters to ensure safe transmission
    from urllib.parse import quote
    query_string = f"name={quote(name)}&address={quote(address)}&quantity={quote(quantity)}&product_id={quote(product_id)}"
    return redirect(f"http://127.0.0.1:5002/payment?{query_string}")

@app.route('/logout')
def logout():
    # Redirect to the login service to handle logout
    return redirect("http://127.0.0.1:5000")  # Change the URL to the login service

if __name__ == '__main__':
    app.run(port=5001, debug=True)
