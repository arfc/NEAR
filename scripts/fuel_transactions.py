
def spent_fuel_transactions(transactions, fuels):
    """
    Adds up all the spent fuel transactions for each fuel type in a new column.

    Parameters
    ----------
    transactions: pd.DataFrame
    fuels: list of strs
    """
    for fuel in fuels:
        transactions[f'spent_{fuel}_total'] = transactions.loc[transactions['Commodity'] == f'spent_{fuel}']['Quantity'].cumsum()

    return transactions


def fresh_fuel_transactions(transactions, fuels):
    """
    Adds up all the fresh fuel transactions for each fuel type in a new column.

    Parameters
    ----------
    transactions: pd.DataFrame
    fuels: list of strs
    """
    for fuel in fuels:
        transactions[f'fresh_{fuel}_total'] = transactions.loc[transactions['Commodity'] == f'fresh_{fuel}']['Quantity'].cumsum()

    return transactions


def total_sp_fr_fuel(transactions, fuels):
    """
    Adds the fresh fuel of each fuel type and total spent fuel of each fuel
    type to a separate total for fresh and spent fuel.
    """
    transactions[f'total_fresh_fuel'] = 0
    transactions[f'total_spent_fuel'] = 0
    
    for fuel in fuels:
        transactions.ffill(inplace=True)
        transactions[f'total_fresh_fuel'] += transactions[f'fresh_{fuel}_total']
        transactions[f'total_spent_fuel'] += transactions[f'spent_{fuel}_total']

    return transactions
