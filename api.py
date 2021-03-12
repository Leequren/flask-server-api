import flask
from flask import jsonify
from first import Get_parse

blueprint = flask.Blueprint('api', __name__,
                            template_folder='templates')


@blueprint.route('/api/<id>', methods=["GET"])
def i_am_ok(id):
    res = Get_parse(f"https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString={id}&morphology=on")
    return jsonify(
        {
            'answer': res
        }
    )
