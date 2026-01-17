from flask import Flask, request, jsonify

from flask_cors import CORS

app = Flask(__name__)

CORS(app) 


# Sample rent data (same as frontend logic)
RENT_DATA = [
    {"locality": "dwarka", "bhk": "1BHK", "rent": 15000},
    {"locality": "dwarka", "bhk": "2BHK", "rent": 25000},
    {"locality": "dwarka", "bhk": "3BHK", "rent": 32000},

    {"locality": "rohini", "bhk": "1BHK", "rent": 14000},
    {"locality": "rohini", "bhk": "2BHK", "rent": 22000},
    {"locality": "rohini", "bhk": "3BHK", "rent": 30000},

    {"locality": "saket", "bhk": "1BHK", "rent": 18000},
    {"locality": "saket", "bhk": "2BHK", "rent": 28000},
    {"locality": "saket", "bhk": "3BHK", "rent": 38000},

    {"locality": "vasant kunj", "bhk": "4BHK", "rent": 75000}
]

@app.route("/api/rent", methods=["GET"])
def get_rent():
    """
    Example request:
    /api/rent?locality=dwarka&bhk=2BHK
    """

    print("Received request for rent estimation")

    locality = request.args.get("locality", "").lower()
    bhk = request.args.get("bhk", "")

    print(f"locality: {locality}, bhk: {bhk}")

    if not locality or not bhk:
        data = {"success": False, "message": "locality and bhk are required"}
        print
        return jsonify(data), 400

    for item in RENT_DATA:
        if item["locality"] == locality and item["bhk"] == bhk:
            rent_data = {
                "success": True,
                "locality": locality.title(),
                "bhk": bhk,
                "estimated_rent": item["rent"],
                "currency": "INR",
                "period": "per month"
            }
            print(f"Returning rent data: {rent_data}")
            return jsonify(rent_data)

    n_data = {
        "success": False,
        "message": "No rent data found for given search"
    }
    print
    return jsonify(n_data), 404


if __name__ == "__main__":
    app.run(debug=True)
