from app import normalize_usernames, process_orders


def test_normalize_usernames():
    assert normalize_usernames([" Alice ", "BOB"]) == ["alice", "bob"]


def test_process_orders():
    orders = [{"id": 1, "items": [{"price": 100, "qty": 2}]}]
    result = process_orders(orders)
    assert result[0]["tier"] == "normal"
