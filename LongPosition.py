
class LongPosition:
    def __init__(self, entry_price, acceptable_risk, rr_ratio, position_size):
        self.entry_price = entry_price
        self.acceptable_risk = acceptable_risk
        self.rr_ratio = rr_ratio
        self.position_size = position_size

    def calculate_stop_loss(self):
        risk_amount = self.acceptable_risk / self.position_size
        return self.entry_price - risk_amount

    def calculate_target_price(self, stop_loss):
        return self.entry_price + self.rr_ratio * (self.entry_price - stop_loss)

    def calculate_profit_loss(self, stop_loss, target_price):
        potential_profit = (target_price - self.entry_price) * self.position_size
        potential_loss = (self.entry_price - stop_loss) * self.position_size
        return potential_profit, potential_loss
