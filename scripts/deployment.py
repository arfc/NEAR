from cymetric import tools
import pandas as pd


def comm_by_prototype(evaler, time):
    """
    Track the number of commissions by prototype.
    """
    commission_df = evaler.eval('BuildSeries')

    commission_df = commission_df.rename(index=str, columns={'EnterTime': 'Time'})
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
    """
    decommission_df = evaler.eval('DecommissionSeries')
    decommission_df = decommission_df.rename(index=str, columns={'ExitTime': 'Time'})
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
    decommission_by_prototype = decommission_df.pivot(index='Time', columns='Prototype')['Count'].reset_index()
    decommission_by_prototype = decommission_by_prototype.fillna(0)

    return decommission_by_prototype


def depl_by_prototype(commission_by_prototype, decommission_by_prototype, reactor_list):
    """
    Track deployments by prototype.
    """
    deployment_by_prototype = commission_by_prototype.copy()

    for reactor in reactor_list:
        dep_react = decommission_by_prototype[reactor] + commission_by_prototype[reactor]
        deployment_by_prototype[reactor] = dep_react

    return deployment_by_prototype


def total_reactor(deployment_by_prototype, reactor_list):
    """
    Add up the total reactors of each type.
    """
    for reactor in reactor_list:
        deployment_by_prototype[f'{reactor}_total'] = 0
        deployment_by_prototype[f'{reactor}_total'] += deployment_by_prototype[reactor].cumsum()

    return deployment_by_prototype