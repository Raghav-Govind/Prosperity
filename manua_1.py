import itertools
# Define the conversion rates as a dictionary
conversion_rates = {
    'Snowballs': {
        'Snowballs': 1,
        'Pizzas': 1.45,
        'Silicon Nuggets': 0.52,
        'SeaShells': 0.72
    },
    'Pizzas': {
        'Snowballs': 0.7,
        'Pizzas': 1,
        'Silicon Nuggets': 0.31,
        'SeaShells': 0.48
    },
    'Silicon Nuggets': {  # Note: Fixed typo from 'Nuggets' to match table
        'Snowballs': 1.95,
        'Pizzas': 3.1,
        'Silicon Nuggets': 1,
        'SeaShells': 1.49
    },
    'SeaShells': {
        'Snowballs': 1.34,
        'Pizzas': 1.98,
        'Silicon Nuggets': 0.64,
        'SeaShells': 1
    }
}

# Currencies available for trading
currencies = ['Snowballs', 'Pizzas', 'Silicon Nuggets', 'SeaShells']

def find_optimal_trades(max_trades):
    results = {}
    
    for num_trades in range(1, max_trades + 1):
        max_amount = 0
        best_sequence = []
        
        # Generate all possible sequences of length num_trades (intermediate trades)
        # We start and end with SeaShells, so the sequence is between
        for sequence in itertools.product(currencies, repeat=num_trades - 1):
            # Full sequence starts and ends with SeaShells
            full_sequence = ['SeaShells'] + list(sequence) + ['SeaShells']
            current_amount = 1.0  # Start with 1 SeaShell
            
            # Apply each trade in sequence
            for i in range(len(full_sequence) - 1):
                from_curr = full_sequence[i]
                to_curr = full_sequence[i + 1]
                current_amount *= conversion_rates[from_curr][to_curr]
            
            # Check if this sequence gives better result
            if current_amount > max_amount:
                max_amount = current_amount
                best_sequence = full_sequence
        
        results[num_trades] = {
            'max_amount': max_amount,
            'sequence': best_sequence
        }
    
    return results

# Find optimal trades for 1 to 5 trades
optimal_trades = find_optimal_trades(10)

# Print results
for num_trades, result in optimal_trades.items():
    print(f"After {num_trades} trades:")
    print(f"  Best sequence: {' → '.join(result['sequence'])}")
    print(f"  Final amount: {result['max_amount']:.4f} SeaShells")
    print()