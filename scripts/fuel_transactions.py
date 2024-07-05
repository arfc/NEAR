
def used_fuel_transactions(transactions, fuels):
    """
    Adds up all the used fuel transactions for each fuel type in a new column.

    Parameters
    ----------
    transactions: pd.DataFrame
        All the material exchanges across the simulation.
    fuels: list of strs
        The types of fuel traded.
    """
    for fuel in fuels:
        transactions[f'used_{fuel}_total'] = transactions.loc[
            transactions['Commodity'] == f'used_{fuel}']['Quantity'].cumsum()

    return transactions


def fresh_fuel_transactions(transactions, fuels):
    """
    Adds up all the fresh fuel transactions for each fuel type in a new column.

    Parameters
    ----------
    transactions: pd.DataFrame
        All the material exchanges across the simulation.
    fuels: list of strs
        The types of fuel traded.
    """
    for fuel in fuels:
        transactions[f'fresh_{fuel}_total'] = transactions.loc[
            transactions['Commodity'] == f'fresh_{fuel}']['Quantity'].cumsum()

    return transactions


def total_used_fr_fuel(transactions, fuels):
    """
    Adds the fresh fuel of each fuel type and total used fuel of each fuel
    type to a separate total for fresh and used fuel.

    Parameters
    ----------
    transactions: pd.DataFrame
        All the material exchanges across the simulation.
    fuels: list of strs
        The types of fuel traded.
    """
    transactions[f'total_fresh_fuel'] = 0
    transactions[f'total_used_fuel'] = 0

    for fuel in fuels:
        transactions.ffill(inplace=True)
        transactions[f'total_fresh_fuel'] += \
            transactions[f'fresh_{fuel}_total']
        transactions[f'total_used_fuel'] += \
            transactions[f'used_{fuel}_total']

    return transactions
