from flask import Blueprint, request, jsonify
from .models import db, Hero, Power, HeroPower

api_bp = Blueprint('api', __name__)

# GET /heroes
@api_bp.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

# GET /heroes/<int:id>
@api_bp.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        hero_data = hero.to_dict()
        hero_data['hero_powers'] = [hp.to_dict() for hp in hero.hero_powers]
        return jsonify(hero_data)
    else:
        return jsonify({"error": "Hero not found"}), 404

# GET /powers
@api_bp.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

# GET /powers/<int:id>
@api_bp.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict())
    else:
        return jsonify({"error": "Power not found"}), 404

# PATCH /powers/<int:id>
@api_bp.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if power:
        data = request.get_json()
        try:
            power.description = data['description']
            db.session.commit()
            return jsonify(power.to_dict())
        except ValueError as e:
            return jsonify({"errors": [str(e)]}), 422
    else:
        return jsonify({"error": "Power not found"}), 404

# POST /hero_powers
@api_bp.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        hero_power = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        db.session.add(hero_power)
        db.session.commit()
        return jsonify(hero_power.to_dict()), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 422
