from flask import Flask, request, jsonify
from flask_cors import CORS

from algorithms.greedy import greedy_allocation
from algorithms.knapsack import knapsack_optimize
from algorithms.maxflow import compute_max_flow
from algorithms.mst import compute_mst

app = Flask(__name__)
CORS(app)

@app.route("/allocate", methods=["POST"])
def allocate():
    data = request.json
    regions = data["regions"]
    supplies = data["supplies"]
    capacity = data.get("capacity", 50)

    greedy = greedy_allocation(regions, supplies)
    knapsack = knapsack_optimize(supplies, capacity)
    maxflow = compute_max_flow()
    mst = compute_mst()

    return jsonify({
        "greedy": greedy,
        "knapsack": knapsack,
        "maxflow": maxflow,
        "mst": mst
    })

if __name__ == "__main__":
    app.run(debug=True)

