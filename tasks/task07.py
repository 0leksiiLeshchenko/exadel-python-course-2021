from typing import List
import uuid
from datetime import datetime


class Good:
    def __init__(self, name: str, price: int):
        self.__id = str(uuid.uuid4())
        self.name = name
        self.price = price

    @property
    def id(self):
        return self.__id

    def __repr__(self):
        return f"<Good(id={self.id}, name={self.name}, price={self.price})>"


class Order:
    def __init__(self, client_id: int, goods: List[Good]):
        self._id = str(uuid.uuid4())
        self.order_date = datetime.now()
        self.client_id = client_id
        self.goods = goods

    @property
    def id(self):
        return self._id

    @property
    def price(self):
        order_price = 0
        for good in self.goods:
            order_price += good.price
        return order_price

    def __repr__(self):
        return (
            f"<Order(id={self.id}, order_date={self.order_date}, client_id={self.client_id}, "
            f"contains {len(self.goods)} good(s))>"
        )


class OrderRepository:
    def __init__(self, client_id: str):
        self._repo = []
        self.client_id = client_id

    def add(self, order: Order):
        self._repo.append(order)

    def get(self, order_id: str) -> Order:
        for order in self._repo:
            if order.id == order_id:
                return order

    def list(self, n_latest: int = None):
        if n_latest:
            assert n_latest > 0
        if n_latest is None:
            return self._repo
        else:
            return self._repo[-n_latest:]

    def delete(self, order_id: str):
        for index in range(len(self._repo) - 1):
            if self._repo[index].id == order_id:
                self._repo.pop(index)

    def __repr__(self):
        return f"<OrderRepository(contains {len(self._repo)} order(s), has add, get, list, detete methods)>"


good1 = Good("car", 500)
print(good1.id, type(good1.id))
good2 = Good("cup", 5)
good3 = Good("phone", 100)
print(good3)
assert good3.name == "phone"
assert good3.price == 100

order1 = Order(1, [good2, good3])
order2 = Order(2, [good1, good2])
order3 = Order(3, [good1, good2, good3])
print(order3)
assert len(order2.goods) == 2
assert order2.price == 505

repository = OrderRepository("123")
repository.add(order1)
repository.add(order2)
repository.add(order3)
print(repository)
assert len(repository.list()) == 3
assert repository.client_id == "123"

all_orders = repository.list()
one_order = repository.list(1)
two_orders = repository.list(2)
print(two_orders)

order_one = repository.get(order1.id)
order_three = repository.get(order3.id)
print(order_three)

repository.delete(order2.id)
assert len(repository.list()) == 2
print(repository)
