def receive_new_shipments(shipments, new_shipments):
    for i in new_shipments:
        shipments.append(i)
    return shipments
