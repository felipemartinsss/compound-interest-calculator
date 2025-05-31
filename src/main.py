from flask import Flask, jsonify, request
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
from compound_interest_calculator import CompoundInterestCalculator

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify(message = "I'm healthy")

@app.route('/api/v1/calculate', methods=['POST'])
def calculate():
    json_body = request.json
    initial_capital = json_body['initial_capital']
    interest_rate = json_body['interest_rate']
    time_unit = json_body['time_unit']
    time = json_body['time']
    investment_frequency = json_body['investment_frequency']
    try:
        calculator = CompoundInterestCalculator(initial_capital, interest_rate, time_unit, time, investment_frequency)
        result = calculator.calculate()
        logger.debug(f'result: {result}')
    except ValueError:
        result = jsonify(message='Ocorreu um erro ao realizar o cálculo dos juros do investimento/empréstimo.')
        return result, 400
    return result, 200

if __name__ == '__main__':
    app.run(debug=True)
