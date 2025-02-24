# Dynamic Power Reactor (DPR)
DPR is a Cyclus reactor archetype based on Cycamore's Reactor, except that it has the ability to update the power output over time.

## power_percent_list
Outside of refueling, the power output of the reactor can be modified by a percentage in the Tock phase of each time step. This feature is optional, and will default to 100% of the power_cap variable the user identifies. At each time step, the reactor will progress through the percentages; as such, there must be a percentage for each time step (if the length of the power_percent_list is shorter than the number of time steps, the reactor will default to 100%).

To simulate 10 time steps, a user could provide a list like:
```
<power_percent_list>
    <val>0.3</val>
    <val>1</val>
    <val>1</val>
    <val>1</val>
    <val>1</val>
    <val>1</val>
    <val>0.9</val>
    <val>0.5</val>
    <val>1</val>
    <val>1</val>
</power_percent_list>
```
If the simulation was extended to 11 time steps with out the list changing, the 11th time step would have a power output of 1 (or 100%).

> [!Important]
> When the reactor is refueling, the power output will be overwritten to 0, so
> we recommend that you ensure your outages align with when the reactor goes
> into outage if you are modeling a historical example.

