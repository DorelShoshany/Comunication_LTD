from application.routers import sectorController
from config import Config
from application import app
from flask import  request, jsonify
roles = Config.ROLE

# TODO: only user as admin
@app.route("/api/addSector", methods=['POST'])
def add_sector():
    res = sectorController.create_sector(request)
    if res:
        return jsonify(message="Sector created successfully. "), 201
    else:
        return jsonify(message="Sector created failed"), 201


@app.route("/api/getSectors", methods=['GET'])
def get_sectors():
    sectors = sectorController.get_all_sectors()
    return jsonify(sectors), 200

