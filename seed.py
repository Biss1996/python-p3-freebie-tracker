from lib.models import Base, Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lib/freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Clear tables (optional)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create sample companies
c1 = Company(name="Moringa", founding_year=1998)
c2 = Company(name="Citizen", founding_year=1975)

# Create sample devs
d1 = Dev(name="Keith")
d2 = Dev(name="Emily")

session.add_all([c1, c2, d1, d2])
session.commit()

# Create freebies
f1 = Freebie(item_name="T-shirt", value=20, dev=d1, company=c1)
f2 = Freebie(item_name="Sticker", value=5, dev=d2, company=c2)
f3 = Freebie(item_name="Hoodie", value=50, dev=d1, company=c2)

session.add_all([f1, f2, f3])
session.commit()

print("Seed data created!")
