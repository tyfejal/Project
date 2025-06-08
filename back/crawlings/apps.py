from django.apps import AppConfig
from flask import Flask, jsonify
# from silver_crawler import get_silver_price

app = Flask(__name__)

@app.route("/api/silver-price")
def silver_price_api():
    price = get_silver_price()
    return jsonify({"silver_price": price})

if __name__ == "__main__":
    app.run(debug=True)

class CrawlingsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "crawlings"
