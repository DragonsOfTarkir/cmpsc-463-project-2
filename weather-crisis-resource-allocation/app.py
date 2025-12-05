from flask import Flask, request, jsonify, render_template
from models.data_models import Region, Depot
from algorithms.greedy import greedy_allocation
from algorithms.knapsack import knapsack_allocate
from algorithms.maxflow import max_flow

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Weather Crisis Resource Allocation API running!"}


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


@app.route("/route/maxflow", methods=["POST"])
def maxflow_api():
    data = request.json

    capacity = data["capacity"]
    source = data["source"]
    sink = data["sink"]

    result = max_flow(capacity, source, sink)
    return jsonify({"method": "max_flow", "max_flow": result})


if __name__ == "__main__":
    app.run(debug=True)
