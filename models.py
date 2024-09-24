from sqlalchemy import Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import relationship
from config import Base

class Band(Base):
    __tablename__ = "bands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    hometown = Column(String)

    concerts = relationship("Concert", back_populates="band")

    def venues(self):
        return list(set([concert.venue for concert in self.concerts]))

    def play_in_venue(self, venue, date):
        from models import Concert  # Import here to avoid circular import
        new_concert = Concert(date=date, band=self, venue=venue)
        self.concerts.append(new_concert)
        return new_concert

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]

    @classmethod
    def most_performances(cls, db):
        return db.query(cls).join(Concert).group_by(cls.id).order_by(func.count(Concert.id).desc()).first()

class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    city = Column(String)

    concerts = relationship("Concert", back_populates="venue")

    def bands(self):
        return list(set([concert.band for concert in self.concerts]))

    def concert_on(self, date):
        return next((concert for concert in self.concerts if concert.date == date), None)

    def most_frequent_band(self):
        band_counts = {}
        for concert in self.concerts:
            band_counts[concert.band] = band_counts.get(concert.band, 0) + 1
        return max(band_counts, key=band_counts.get) if band_counts else None

class Concert(Base):
    __tablename__ = "concerts"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    band_id = Column(Integer, ForeignKey("bands.id"))
    venue_id = Column(Integer, ForeignKey("venues.id"))

    band = relationship("Band", back_populates="concerts")
    venue = relationship("Venue", back_populates="concerts")

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"