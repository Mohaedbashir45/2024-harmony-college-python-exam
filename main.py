from config import get_db, Base, engine
from models import Band, Venue, Concert

# Create tables
Base.metadata.create_all(bind=engine)

def main():
    db = next(get_db())
    
    # Example usage
    band1 = Band(name="The Rockers", hometown="New York")
    band2 = Band(name="Jazz Ensemble", hometown="Chicago")
    db.add_all([band1, band2])
    
    venue1 = Venue(title="Madison Square Garden", city="New York")
    venue2 = Venue(title="Chicago Theater", city="Chicago")
    db.add_all([venue1, venue2])
    
    concert1 = Concert(date="2023-07-15", band=band1, venue=venue1)
    concert2 = Concert(date="2023-08-20", band=band2, venue=venue2)
    db.add_all([concert1, concert2])
    
    db.commit()
    
    # Test some methods
    print("Band1 venues:", [venue.title for venue in band1.venues()])
    print("Venue1 bands:", [band.name for band in venue1.bands()])
    print("Is concert1 a hometown show?", concert1.hometown_show())
    print("Concert1 introduction:", concert1.introduction())
    
    band1.play_in_venue(venue2, "2023-09-10")
    db.commit()
    
    most_performances_band = Band.most_performances(db)
    print("Band with most performances:", most_performances_band.name if most_performances_band else "No performances yet")
    
    most_frequent_band = venue2.most_frequent_band()
    print("Most frequent band at venue2:", most_frequent_band.name if most_frequent_band else "No performances yet")

if __name__ == "__main__":
    main()