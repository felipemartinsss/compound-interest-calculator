import logging

from flask import jsonify

class CompoundInterestCalculator:

    def __init__(self, initial_value, interest_rate, time_unit, time, investment_frequency):
        self.logger = logging.getLogger(__name__)
        self.initial_value = initial_value
        self.interest_rate = interest_rate
        if not time_unit.upper() in ['PY', 'PM']:
            raise ValueError
        self.time_unit = time_unit
        self.time = time
        if not investment_frequency.lower() in ['unique', 'monthly']:
            raise ValueError
        self.investment_frequency = investment_frequency

    def calculate(self):
        final_value = 0.0
        revenue = 0.0
        if self.investment_frequency == 'unique':
            converted_interest_rate = self.interest_rate / 100.0
            final_value = self.initial_value * (1 + converted_interest_rate) ** self.time
            revenue = final_value - self.initial_value
        elif self.investment_frequency == 'monthly':
            converted_interest_rate = self.interest_rate / 100.0
            if self.time_unit == 'PY':
                months_in_time = 12 * self.time
                for i in range (0, int(months_in_time)):
                    self.logger.debug(f"{i}º valor aplicado: {self.initial_value}")
                    self.logger.debug(f"Tempo que renderá o {i}º: {(self.time - i / months_in_time)}")
                    final_value += self.initial_value * (1 + converted_interest_rate) ** (self.time - i / months_in_time)
                    self.logger.debug(f"Valor ao final do {i + 1}º periodo de tempo: {final_value}")
                revenue = final_value - (self.initial_value * self.time * 12)
            elif self.time_unit == 'PM':
                for i in range (0, int(self.time)):
                    self.logger.debug(f"Valor aplicado: {self.initial_value}")
                    self.logger.debug(f"Tempo que renderá: {(self.time - i)}")
                    final_value += self.initial_value
                    final_value = final_value * (1 + converted_interest_rate)
                    self.logger.debug(f"Valor ao final do {i + 1}º periodo de tempo: {final_value}")
                revenue = final_value - (self.initial_value * self.time)
        else:
            self.logger.debug("Opção desconhecida.")
        return jsonify(final_value=final_value, revenue=revenue)
