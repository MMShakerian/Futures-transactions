import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from TradeController import TradeController


class TradingCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Futures Trading Calculator")

        # انتخاب نوع معامله (لانگ یا شورت)
        self.trade_type = tk.StringVar(value="long")
        tk.Radiobutton(root, text="Long", variable=self.trade_type, value="long").grid(row=0, column=0)
        tk.Radiobutton(root, text="Short", variable=self.trade_type, value="short").grid(row=0, column=1)

        # فیلدهای ورودی و برچسب‌ها
        tk.Label(root, text="Initial Capital:").grid(row=1, column=0)
        self.capital_entry = tk.Entry(root)
        self.capital_entry.grid(row=1, column=1)

        tk.Label(root, text="Leverage:").grid(row=2, column=0)
        self.leverage_entry = tk.Entry(root)
        self.leverage_entry.grid(row=2, column=1)

        tk.Label(root, text="Entry Price:").grid(row=3, column=0)
        self.entry_price_entry = tk.Entry(root)
        self.entry_price_entry.grid(row=3, column=1)

        tk.Label(root, text="Risk/Reward Ratio (R/R):").grid(row=4, column=0)
        self.rr_ratio_entry = tk.Entry(root)
        self.rr_ratio_entry.grid(row=4, column=1)

        tk.Label(root, text="Acceptable Risk (percentage):").grid(row=5, column=0)
        self.acceptable_risk_entry = tk.Entry(root)
        self.acceptable_risk_entry.grid(row=5, column=1)

        # دکمه محاسبه
        calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        calculate_button.grid(row=6, column=0, columnspan=2)

        # نمایش نتایج
        self.result_text = tk.StringVar()
        result_label = tk.Label(root, textvariable=self.result_text, justify="left")
        result_label.grid(row=7, column=0, columnspan=2)

    def calculate(self):
        try:
            capital = float(self.capital_entry.get())
            leverage = float(self.leverage_entry.get())
            entry_price = float(self.entry_price_entry.get())
            rr_ratio = float(self.rr_ratio_entry.get())
            acceptable_risk = float(self.acceptable_risk_entry.get())

            # ساختن TradeController برای انجام محاسبات
            controller = TradeController(
                self.trade_type.get(), capital, leverage, entry_price, rr_ratio, acceptable_risk
            )
            result = controller.perform_calculation()

            # نمایش نتایج
            self.result_text.set(f"Position Size: {result['position_size']:.2f}\n"
                                 f"Stop Loss: {result['stop_loss']:.2f}\n"
                                 f"Target Price: {result['target_price']:.2f}\n"
                                 f"Potential Profit: {result['potential_profit']:.2f}\n"
                                 f"Potential Loss: {result['potential_loss']:.2f}\n"
                                 f"Risk/Reward Ratio (R/R): {result['rr_ratio']:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter all values correctly.")
