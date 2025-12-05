def greedy_allocation(regions, supplies):
    sorted_regions = sorted(regions, key=lambda r: r["urgency"], reverse=True)

    allocation = {}
    remaining = supplies

    for r in sorted_regions:
        need = r["need"]
        sent = min(need, remaining)
        remaining -= sent
        allocation[r["name"]] = sent

    return {"allocation": allocation, "remaining": remaining}
