brojevi = [10, 5, 12, 15, 20]

transform = dict(map(lambda x: (x, x ** 2), brojevi))

print(transform)  # {10: 100, 5: 25, 12: 144, 15: 225, 20: 400}