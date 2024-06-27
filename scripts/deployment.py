from cymetric import tools
import pandas as pd


def comm_by_prototype(evaler, time):
    """
    Track the number of commissions by prototype.

    Parameters
    ----------
    evaler: cymetric.evaluator.Evaluator
        The object that takes in the sqlite database and can create DataFrames.
    time: pd.DataFrame
        The time steps in the simulation.

    Returns
    -------
    commission_by_prototype: pd.DataFrame
        DataFrame that tracks the commissioning of reactors
        throughout the simulation.
    commission_df: pd.DataFrame
        Dataframe that pulls the 'BuildSeries' table from the database.
    """
    commission_df = evaler.eval('BuildSeries')

    commission_df = commission_df.rename(
        index=str,
        columns={'EnterTime': 'Time'})
    commission_df = tools.add_missing_time_step(commission_df, time)
    commission_by_prototype = pd.pivot_table(
            commission_df,
            values='Count',
            index='Time',
            columns='Prototype',
            fill_value=0)

    return commission_by_prototype, commission_df


def decom_by_prototype(evaler, commission_df, time):
    """
    Track the number of decommissions by prototype.

    Parameters
    ----------
    evaler: cymetric.evaluator.Evaluator
        The object that takes in the sqlite database and can create DataFrames.
    commission_df: pd.DataFrame
        Dataframe that pulls the 'BuildSeries' table from the database.
    time: pd.DataFrame
        The time steps in the simulation.

    Returns
    -------
    decommission_by_prototype: pd.DataFrame
        DataFrame that tracks the decommissioning of reactors
        throughout the simulation.
    """
    decommission_df = evaler.eval('DecommissionSeries')
    decommission_df = decommission_df.rename(
        index=str,
        columns={'ExitTime': 'Time'})
    decommission_df = tools.add_missing_time_step(decommission_df, time)
    decommission_by_prototype = pd.pivot_table(
            commission_df,
            values='Count',
            index='Time',
            columns='Prototype',
            fill_value=0)
    negative_count = -decommission_df['Count']
    decommission_df = decommission_df.drop('Count', axis=1)
    decommission_df = pd.concat([decommission_df, negative_count], axis=1)
    decommission_df.rename(columns={'ExitTime': 'Time'}, inplace=True)
    decommission_by_prototype = \
        decommission_df.pivot(
            index='Time',
            columns='Prototype')['Count'].reset_index()
    decommission_by_prototype = decommission_by_prototype.fillna(0)

    return decommission_by_prototype


def depl_by_prototype(
        commission_by_prototype,
        decommission_by_prototype,
        reactor_list):
    """
    Track deployments by prototype.

    Parameters
    ----------
    commission_by_prototype: pd.DataFrame
        All of the commission events, output of comm_by_prototype().
    decommission_by_prototype: pd.DataFrame
        All of the decommission events, output of decom_by_prototype().
    reactor_list: list of strs
        The list of reactors deployed in the simulation.

    Returns
    -------
    deployment_by_prototype: pd.DataFrame
        DataFrame that tracks the deployment and decommissioning of reactors
        throughout the simulation.
    """
    deployment_by_prototype = commission_by_prototype.copy()

    for reactor in reactor_list:
        dep_react = decommission_by_prototype[reactor] + \
            commission_by_prototype[reactor]
        deployment_by_prototype[reactor] = dep_react

    return deployment_by_prototype


def total_reactor(deployment_by_prototype, reactor_list):
    """
    Add up the total reactors of each type.

    Returns
    -------
    deployment_by_prototype: pd.DataFrame
        DataFrame that tracks the deployment and decommissioning of reactors
        throughout the simulation.
    """
    for reactor in reactor_list:
        deployment_by_prototype[f'{reactor}_total'] = 0
        deployment_by_prototype[f'{reactor}_total'] += \
            deployment_by_prototype[reactor].cumsum()

    return deployment_by_prototype
