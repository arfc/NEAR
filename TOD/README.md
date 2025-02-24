# Trading On-Demand (TOD) Reactor
TOD is a Cyclus reactor archetype based on Cycamore's Reactor, except that it
has the ability to update the power output over time. TOD achieves this by
creating a private variable that is updated at the end of the Tock phase when
the reactor refuels. Each intervening step checks if the current time step
equals this private variable.

> [!Note]
> The user does not need to do anything to take advantage of this
> functionality, and it cannot be turned off.

## Cite this work
Pending...
