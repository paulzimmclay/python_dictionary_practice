stock_dict = {
  'GM': 'General Motors',
  'AAPL': 'Apple',
  'WU': "Western Union"
}

purchases = [
  ('GM', 800, '10-sep-2003', 50),
  ('AAPL', 190, '15-jun-2014', 21),
  ('AAPL', 190, '15-jun-2014', 4),
  ('AAPL', 190, '15-jun-2014', 8),
  ('WU', 20, '15-jul-2010', 49)
]

for purchase in purchases:
    print(f'{stock_dict[purchase[0]]}, total value: {purchase[1] * purchase[3]}')

for purchase in purchases:
    cumulative_purchases = {}
    
    cumulative_purchases.update({purchase[0]:"test"})
    print(cumulative_purchases)