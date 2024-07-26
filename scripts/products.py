import pandas as pd


def energy_supply(cursor):
    """
    This function will pull the energy supply data from the database
    and return it as a pandas dataframe.

    Parameters
    ----------
    cursor: sqlite3.cursor
        The cursor for the sqlite database.

    Returns
    -------
    switch_energy_supply: pd.DataFrame
        The energy supply data for the simulation.
    """
    # Now we will pull the supplied power to get the amount of
    # power from each reactor at every time step.
    cursor.execute("SELECT * FROM TimeSeriessupplyPOWER")
    supply_rows = cursor.fetchall()

    # Create an empty dictionary that mirrors the format of
    # the PowerSupply table.
    energy_supply = {
        'id': [],
        'time': [],
        'energy': []
    }

    # Next we will pull the power at each time step for each reactor.
    for row in range(len(supply_rows)):
        energy_supply['id'].append(str(supply_rows[row][1]))
        energy_supply['time'].append(supply_rows[row][2])
        energy_supply['energy'].append(supply_rows[row][3])

    # Make the dictionary into a pandas DataTrame to match the type of the
    # other data we've been working with.
    energy_supply_df = pd.DataFrame.from_dict(energy_supply)

    # We will turn the ids into columns of energy and make the index time
    switch_energy_supply = energy_supply_df.pivot_table(
        index='time', columns='id', values='energy', fill_value=0)

    # Now we will add a total_energy column.
    switch_energy_supply['total_energy'] = \
        switch_energy_supply.iloc[:, 0:].sum(axis=1)

    return switch_energy_supply


def swu_supply(cursor):
    """
    This function will pull the swu supply data from the database
    and return it as a pandas DataFrame.

    Parameters
    ----------
    cursor: sqlite3.cursor
        The cursor for the sqlite database.

    Returns
    -------
    switch_swu_supply: pd.DataFrame
        The swu supply data for the simulation.
    """
    # Now we will pull the supplied swu to get the amount of swu from each
    # facility at every time step.
    cursor.execute("SELECT * FROM TimeSeriesEnrichmentSWU")
    swu_rows = cursor.fetchall()

    # Create an empty dictionary that mirrors the format of the
    # TimeSeriesEnrichmentSWU table.
    swu_supply = {
        'id': [],
        'Time': [],
        'SWU': []
    }

    # Next we will pull the swu at each time step for each facility.
    for row in range(len(swu_rows)):
        swu_supply['id'].append(str(swu_rows[row][1]))
        swu_supply['Time'].append(swu_rows[row][2])
        swu_supply['SWU'].append(swu_rows[row][3])

    # Make the dictionary into a pandas DataFrame to match the type of the
    # other data we've been working with.
    swu_supply_df = pd.DataFrame.from_dict(swu_supply)

    # We will turn the ids into columns of energy and make the index time.
    switch_swu_supply = swu_supply_df.pivot_table(
        index='Time', columns='id', values='SWU', fill_value=0)

    # Now we will add a total_energy column.
    switch_swu_supply['total_swu'] = \
        switch_swu_supply.iloc[:, 0:].sum(axis=1)

    return switch_swu_supply
