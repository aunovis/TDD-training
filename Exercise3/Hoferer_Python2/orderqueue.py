class OrderQueue:
    def __init__(self, order):
        self.queue = []
        self.add_order_to_queue(order)

    def add_order_to_queue(self, order):
        self.queue.append(order)

    def remove_order_from_queue(self, order):
        self.queue.remove(order)

    def get_queue(self):
        return self.queue
