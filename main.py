
# Imports
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from stripe import Stripe
import stripe

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SECRET_KEY'] = 'supersecretkey'
db = SQLAlchemy(app)

# Stripe configuration
stripe_keys = {
    'secret_key': 'sk_test_...',
    'publishable_key': 'pk_test_...'
}
stripe = Stripe(stripe_keys['secret_key'])

# Database models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(120), nullable=False)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Routes
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_details(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_details.html', product=product)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity')
    # Check if product exists
    product = Product.query.get_or_404(product_id)
    # Check if item already in cart
    cart_item = CartItem.query.filter_by(product_id=product_id).first()
    if cart_item:
        cart_item.quantity += int(quantity)
    else:
        cart_item = CartItem(product_id=product_id, quantity=int(quantity))
    db.session.add(cart_item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart_items = CartItem.query.all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/checkout')
def checkout():
    cart_items = CartItem.query.all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, total=total, stripe_publishable_key=stripe_keys['publishable_key'])

@app.route('/process_checkout', methods=['POST'])
def process_checkout():
    cart_items = CartItem.query.all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    stripe_token = request.form.get('stripeToken')
    customer = stripe.Customer.create(
        email=request.form.get('email'),
        source=stripe_token,
    )
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=int(total * 100),
        currency='usd',
        description='Flask Ecommerce Purchase',
    )
    # Clear cart
    CartItem.query.delete()
    db.session.commit()
    return render_template('order_confirmation.html')

# Initialize database
db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
