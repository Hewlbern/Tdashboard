from sqlalchemy import Column, Integer, String
from database import Base

class Streams(Base):
    __tablename__ = 'streams'
    id = Column(Integer, primary_key=True)
    occupancy = Column(String(50), unique=True)
    speed = Column(String(120), unique=True)
    speedobs = Column(String(120), unique=True)
    time = Column(String(120), unique=True)
    date = Column(String(120), unique=True)

    def __init__(self, occupancy, speed, speedobs, time, date):
        self.occupancy = occupancy
        self.speed = speed
        self.speedobs = speedobs
        self.time = time
        self.date = date

    def __repr__(self):
        return '<Streams %r>' % (self.occupancy)




