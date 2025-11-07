def receive_new_shipments(shipments, new_shipments):
    for i in new_shipments:
        shipments.append(i)
    return shipments
def dispatch_shipments(shipments, num_to_dispatch):
    after_dispatch = shipments[:num_to_dispatch]
    if num_to_dispatch > len(shipments):
        after_dispatch = shipments[:]
    return after_dispatch
def recall_shipment(shipments, shipment_id):
    if shipment_id in shipments:
        shipments.remove(shipment_id)
        return True
    return False
def manage_shipments(initial_shipments, new_shipments_to_receive, shipments_to_dispatch, shipment_to_recall):
    current_shipments = initial_shipments[:]
    recall_shipment(current_shipments, shipment_to_recall)
    dispatched = dispatch_shipments(current_shipments, shipments_to_dispatch)
    return current_shipments, dispatched



initial = ["BOX-A1", "BOX-B2", "BOX-C3", "BOX-D4"]
new = ["BOX-E5", "BOX-F6"]
dispatch_count = 2
recall_id = "BOX-D4"

final_state, dispatched = manage_shipments(initial, new, dispatch_count, recall_id)

print("final_state:", final_state)
print("dispatched:", dispatched)
print("Original list unchanged:", initial)
