def greedy_allocation(regions, depot):
# Allocate resources based on urgency (highest first).
    # Sort by urgency descending
    regions = sorted(regions, key=lambda r: r.urgency, reverse=True)
    allocation = {}
    remaining_supply = depot.supply

    for region in regions:
        if remaining_supply == 0:
            allocation[region.name] = 0
            continue

        allocated = min(region.need, remaining_supply)
        allocation[region.name] = allocated
        remaining_supply -= allocated

    return {
        "method": "greedy",
        "allocation": allocation,
        "remaining_supply": remaining_supply
    }
