Here is a basic starter code for a Flask-based e-commerce web application. This code includes basic functionality such as product listing, adding to cart, and checking out. 

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart_item = Cart(product_id=product_id, quantity=1)
    db.session.add(cart_item)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/checkout')
def checkout():
    cart_items = Cart.query.all()
    total = sum([item.product.price * item.quantity for item in cart_items])
    return render_template('checkout.html', cart_items=cart_items, total=total)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

This is a very basic example and does not include user authentication, product categories, payment processing, etc. You would need to add these features to make a fully functional e-commerce website.

To deploy this to GitHub, you would need to:

1. Initialize a new Git repository in your project directory with `git init`.
2. Add all your files to the repository with `git add .`.
3. Commit your changes with `git commit -m "Initial commit"`.
4. Create a new repository on GitHub.
5. Link your local repository to the GitHub repository with `git remote add origin your-github-repo-url`.
6. Push your changes to GitHub with `git push -u origin master`.