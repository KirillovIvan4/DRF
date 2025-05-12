import stripe
from config.settings import SECRET_API_KEY

stripe.api_key = SECRET_API_KEY


def create_stripe_product(name, description):
    """Создает продукт в страйпе"""
    product = stripe.Product.create(
        name=name,
        description=description
    )
    return product.get("id")

def create_stripe_price(amount, product_id):
    """Создает цену в страйпе"""
    price = stripe.Price.create(
        currency="rub",
        unit_amount=amount*100,
        product=product_id,
    )
    return price

def create_stripe_session(price):
    """Создает цену в страйпе"""
    session = stripe.checkout.Session.create(
      success_url="http://127.0.0.1:8000/",
      line_items=[{"price": price, "quantity": 1}],
      mode="payment",
    )
    return session.get("id"), session.get("url")