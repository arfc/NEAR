import numpy as np
import matplotlib
matplotlib.use
import matplotlib.pyplot as plt
plt.style.use('../../plotting.mplstyle')

import requests
from collections import defaultdict

def read_reactor_data(url):
    """
    Reads NRC reactor data from a given URL and returns a dictionary with reactor names as keys and lists of power values as values.

    Parameters:
        url: str
            The URL of the NRC reactor data file.

    Returns:
        reactor_data: dict
            A dictionary where keys are reactor names and values are lists of power values.
    """
    reactor_data = {}

    reactor_data = defaultdict(list)

    response = requests.get(url)
    response.raise_for_status()
    lines = response.text.strip().split('\n')

    next(iter(lines))  # Skip the header line
    for line in lines[1:]:
        parts = line.strip().split('|')
        if len(parts) == 3:
            _, reactor, power = parts
            reactor_data[reactor].append(int(power))

    return reactor_data

def list_to_string(l):
    """
    Converts a list of values to a string in XML format.
    Parameters:
        l: list
            The list of values to be converted.
    Returns:
        string: str
            The XML string representation of the list.
    """
    # Convert the list to a string in XML format
    string = ''.join(
        [f"""<val>{i}</val>\n""" for i in l]
        )
    return string

# Save the string as an XML file
def save_as_xml(string, filename):
    """
    Saves a string as an XML file.

    Parameters:
        string: str
            The string to be saved.
        filename: str
            The name of the XML file.
    Returns:
        None:
            The function does not return anything, it outputs the XML file to the current directory.
    """
    with open(f'{filename}.xml', 'w') as f:
        f.write(list_to_string(string))


if __name__ == '__main__':
    # We will pull in data from the Clinton Power Plant over a 4-year period.
    url_2024 = "https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2024/2024powerstatus.txt"

    url_2023 = "https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2023/2023powerstatus.txt"

    url_2022 = "https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2022/2022powerstatus.txt"

    url_2021 = "https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2021/2021powerstatus.txt"

    # Now use the read_reactor_data function for each year.abs
    reactor_2024 = read_reactor_data(url_2024)
    reactor_2023 = read_reactor_data(url_2023)
    reactor_2022 = read_reactor_data(url_2022)
    reactor_2021 = read_reactor_data(url_2021)

    # Create empty dictionaries to store the data.
    reactor_power_2024 = {}
    reactor_power_2023 = {}
    reactor_power_2022 = {}
    reactor_power_2021 = {}

    # Convert lists to decimal form of a percent.
    for reactor, power_list in reactor_2024.items():
        power_list = np.array(power_list)/100
        reactor_power_2024[reactor] = list(map(float, power_list))

    for reactor, power_list in reactor_2023.items():
        power_list = np.array(power_list)/100
        reactor_power_2023[reactor] = list(map(float, power_list))

    for reactor, power_list in reactor_2022.items():
        power_list = np.array(power_list)/100
        reactor_power_2022[reactor] = list(map(float, power_list))

    for reactor, power_list in reactor_2021.items():
        power_list = np.array(power_list)/100
        reactor_power_2021[reactor] = list(map(float, power_list))

    # Now we will create a list of the power values for the Clinton Power Plant.
    clinton_power = []

    for i in range(len(reactor_power_2021['Clinton'])):
        clinton_power.append(reactor_power_2021['Clinton'][i])

    for i in range(len(reactor_power_2022['Clinton'])):
        clinton_power.append(reactor_power_2022['Clinton'][i])

    for i in range(len(reactor_power_2023['Clinton'])):
        clinton_power.append(reactor_power_2023['Clinton'][i])

    for i in range(len(reactor_power_2024['Clinton'])):
        clinton_power.append(reactor_power_2024['Clinton'][i])

    # Convert the list to a numpy array.
    clinton_power = np.array(clinton_power)

    # Create a list of days for the x-axis.
    days = np.arange(0,len(clinton_power)).tolist()

    # Create an example based on how the Cycamore reactor would model the power
    # output.
    cycamore_power = [1]*len(days)

    for i in range(812, 842):
        cycamore_power[i] = 0

    for i in range(66, 96):
        cycamore_power[i] = 0

    cycamore_power = np.array(cycamore_power)

    # Now we will create a plot of the power values for the Clinton Power Plant.
    plt.plot(days, clinton_power*100, label='Clinton')
    plt.plot(days, cycamore_power*100, label='Cycamore', linestyle='--')

    plt.xlabel('Time [Days]')
    plt.ylabel('Power Percent [%]')

    plt.legend()

    plt.savefig('power_percent_clinton_cycamore.pdf')
    plt.clf()
    plt.close()  # Clear the figure


    # Now we will evaluate the cumulative difference between the two.
    # Calculate the area under the curve using the trapezoidal rule
    clinton_power_cap = 1.062
    real_area = np.trapezoid(clinton_power*clinton_power_cap, days)
    cycamore_area = np.trapezoid(cycamore_power*clinton_power_cap, days)


    # Now we will save the data as an XML file.
    save_as_xml(clinton_power, 'clinton_output')

    ## Now we will zoom in on the data for 2024.

    days_2024 = np.arange(0, len(reactor_power_2024['Clinton']))
    clinton_power_2024 = clinton_power[365*3:]
    cycamore_power_2024 = cycamore_power[365*3:]

    plt.plot(days_2024, clinton_power_2024*100, label='Clinton')
    plt.plot(days_2024, cycamore_power_2024*100, label='Cycamore', linestyle='--')

    plt.xlabel('Time [Days]')
    plt.ylabel('Power Percent [%]')

    plt.legend()

    plt.savefig('power_percent_clinton_cycamore_2024.pdf')
    plt.clf()
    plt.close()  # Clear the figure

    # Calculate the area under the curve using the trapezoidal rule
    real_area_2024 = np.trapezoid(clinton_power_2024*clinton_power_cap, days_2024)
    cycamore_area_2024 = np.trapezoid(cycamore_power_2024*clinton_power_cap, days_2024)

    save_as_xml(clinton_power_2024, 'clinton_2024_output')


    with open("stats.txt", "a") as f:
        print('Let\'s look at the entire 4-year period.', file=f)
        print('real [GWe]', real_area, 'cycamore [GWe]', cycamore_area, 'difference [GWe]', cycamore_area - real_area, file=f)
        print('percent difference', np.abs(real_area-cycamore_area)/real_area, file=f)
        print('number of days cycamore reactor was off:', len(np.where(clinton_power == cycamore_area)[0]), file=f)

        print('\nNow let\'s look at 2024.', file=f)
        print('real [GWe] for 2024', real_area_2024, 'cycamore [GWe] for 2024', cycamore_area_2024, file=f)
        print('difference in power [GWe] for 2024', np.abs(real_area_2024-cycamore_area_2024), file=f)

        print('percent difference for 2024', np.abs(real_area_2024-cycamore_area_2024)/real_area_2024, file=f)

        print('number of days cycamore reactor was off in 2024:', len(np.where(clinton_power_2024 == cycamore_power_2024)[0]), file=f)