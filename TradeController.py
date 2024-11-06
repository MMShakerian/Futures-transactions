import tkinter as tk
from LongPosition import LongPosition
from ShortPosition import ShortPosition


class TradeController:
    def __init__(self, trade_type, capital, leverage, entry_price, rr_ratio, acceptable_risk):
        self.trade_type = trade_type
        self.capital = capital
        self.leverage = leverage
        self.entry_price = entry_price
        self.rr_ratio = rr_ratio
        self.acceptable_risk = acceptable_risk

    def calculate_position_size(self):
        return (self.capital * self.leverage) / self.entry_price

    def perform_calculation(self):
        position_size = self.calculate_position_size()
        
        if self.trade_type == "long":
            position = LongPosition(self.entry_price, self.acceptable_risk, self.rr_ratio, position_size)
            stop_loss = position.calculate_stop_loss()
            target_price = position.calculate_target_price(stop_loss)
            potential_profit, potential_loss = position.calculate_profit_loss(stop_loss, target_price)
        else:  # trade_type == "short"
            position = ShortPosition(self.entry_price, self.acceptable_risk, self.rr_ratio, position_size)
            stop_loss = position.calculate_stop_loss()
            target_price = position.calculate_target_price(stop_loss)
            potential_profit, potential_loss = position.calculate_profit_loss(stop_loss, target_price)
        
        return {
            "position_size": position_size,
            "stop_loss": stop_loss,
            "target_price": target_price,
            "potential_profit": potential_profit,
            "potential_loss": potential_loss,
            "rr_ratio": self.rr_ratio
        }
    


