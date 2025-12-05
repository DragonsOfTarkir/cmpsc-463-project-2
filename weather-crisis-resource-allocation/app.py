from flask import Flask, request, jsonify, render_template
from models.data_models import Region, Depot
from algorithms.greedy import greedy_allocation
from algorithms.knapsack import knapsack_allocate

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/web")
def web_home():
    return render_template("index.html")

@app.route("/allocate/greedy", methods=["POST"])
def greedy_api():
    data = request.json
    regions = [Region(**r) for r in data["regions"]]
    depot = Depot(**data["depot"])

    result = greedy_allocation(regions, depot)
    return jsonify(result)


@app.route("/allocate/knapsack", methods=["POST"])
def knapsack_api():
    data = request.json
    regions = [Region(**r) for r in data["regions"]]
    depot = Depot(**data["depot"])

    result = knapsack_allocate(regions, depot.supply)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
