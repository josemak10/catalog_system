from fastapi.exceptions import HTTPException
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from products.models import Product
from users.models import User


own_email = "pincheriaelvalle@gmail.com"
own_email_password = "zyvpctgtowfcqegd"
port = 465


def send_email(product: Product, send_user: User, users: []):
    try:
        for user in users:
            msg = MIMEText(f"sku: {product.sku} name: {product.name} price: {product.price} brand: {product.brand}")
            msg['Subject'] = f"Update Product by {send_user.email}"
            msg['From'] = f"Catalog System <{own_email}>"
            msg['To'] = user.email

            server = SMTP_SSL("smtp.gmail.com", port)
            server.login(own_email, own_email_password)
            server.send_message(msg)
            server.quit()

    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
