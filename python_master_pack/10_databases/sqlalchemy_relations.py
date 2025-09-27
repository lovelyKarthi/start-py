"""SQLAlchemy example: one-to-many relation and transaction handling"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///10_databases/demo_rel.db', echo=False)
Session = sessionmaker(bind=engine)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer = Column(String)
    items = relationship('OrderItem', back_populates='order')

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product = Column(String)
    order = relationship('Order', back_populates='items')

def init():
    Base.metadata.create_all(engine)

def demo():
    s = Session()
    o = Order(customer='Karthi')
    o.items = [OrderItem(product='Book'), OrderItem(product='Pen')]
    s.add(o)
    s.commit()
    print('order id', o.id)
    s.close()

if __name__ == '__main__':
    init()
    demo()
