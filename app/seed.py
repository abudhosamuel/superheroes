# app/seed.py

from .models import db, Hero, Power

def seed_data():
    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")
    hero3 = Hero(name="Jean Grey", super_name="Dark Phoenix")

    power1 = Power(name="Super Strength", description="Gives the wielder super-human strengths")
    power2 = Power(name="Flight", description="Gives the wielder the ability to fly through the skies at supersonic speed")

    db.session.add_all([hero1, hero2, hero3, power1, power2])
    db.session.commit()
