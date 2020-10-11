from flask import Blueprint
from flask import jsonify
from flask import request
from TreasureHunt.treasureHunt import *

bp = Blueprint("TreasureHuntGame", __name__, url_prefix="/")

# 获得用户基本信息
@bp.route("/<username>/info", methods=['GET'])
def user(username):
    money, capability, fortune = get_user_info(username)
    return jsonify({
        "username": username,
        "money": money,
        "capability": capability,
        "fortune": fortune
    })

# 用户工作路由
@bp.route("/<username>/work", methods=['POST'])
def work_route(username):
    gain = work(username)
    return jsonify({'gain': gain})
