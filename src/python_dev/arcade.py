customer_name = "Igris"
passes_bought = 10
tokens_per_pass = 20
pass_price = 10.50
tokens_per_game = 2

total_tokens = passes_bought * tokens_per_pass
total_cost = passes_bought * pass_price
games_available = total_tokens // tokens_per_game

print("===== ARCADE DAY PASS =====")
print("Customer:", customer_name)
print("Passes:", passes_bought)
print("Tokens:", total_tokens)
print("Total Cost: $" + str(total_cost))
print("Games Available: " + str(games_available))
