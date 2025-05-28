from lib.models import Company, Dev, Freebie, Base
from sqlalchemy.orm import sessionmaker
from lib.database import engine

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

oldest = Company.oldest_company(session)
print("Oldest company:", oldest.name if oldest else "None")

# Create tables (run once or during setup)
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add seed data if needed
# Run this only once or protect with `if not session.query(...).first():`
# Example:
# google = Company(name="Google", founding_year=1998)
# alice = Dev(name="Alice")
# session.add_all([google, alice])
# session.commit()

# Test oldest company
print("Oldest company:", Company.oldest_company(session).name)

# Test dev received_one
dev = session.query(Dev).filter_by(name="Alice").first()
print("Alice received T-shirt?", dev.received_one("T-shirt"))

# Test print_details
freebie = session.query(Freebie).first()
print(freebie.print_details())

# Test give_freebie
company = session.query(Company).filter_by(name="Google").first()
new_freebie = company.give_freebie(dev, "Cap", 15)
session.add(new_freebie)
session.commit()

print(new_freebie.print_details())

# Test give_away
bob = session.query(Dev).filter_by(name="Bob").first()
dev.give_away(bob, new_freebie)
session.commit()
print(new_freebie.print_details())  # Should now show Bob as the owner
