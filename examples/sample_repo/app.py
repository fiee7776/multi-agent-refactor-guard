def process_orders(orders):
    result = []
    for order in orders:
        if not isinstance(order, dict):
            continue
        if "items" not in order:
            continue
        total = 0
        for item in order["items"]:
            if not isinstance(item, dict):
                continue
            if "price" in item and "qty" in item:
                if item["qty"] > 0:
                    total += item["price"] * item["qty"]
            else:
                total += 0
        if total > 1000:
            result.append({"id": order.get("id"), "tier": "vip", "total": total})
        elif total > 0:
            result.append({"id": order.get("id"), "tier": "normal", "total": total})
    return result


def normalize_usernames(values):
    out = []
    for v in values:
        if isinstance(v, str):
            out.append(v.strip().lower())
    return out
