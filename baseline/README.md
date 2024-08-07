# Baseline Scenarios
These scenarios are designed to establish the existing capabilities of the
[Cycamore Reactor](https://fuelcycle.org/user/cycamoreagents.html#cycamore-reactor).

These capabilities are:
1. The ability to change a recipe with the `recipe_change` tag.
1. The ability to change the fuel preference with `fuel_prefs`.

## Base Single Reactor
In this scenario, a single reactor is deployed with a single fuel type over a
set deployment and decommissioning timeline.


## Cycamore Multiple Enrichment
In this scenario, we use the Cycamore Reactor's ability to change the
preference to change the fuel type twice. There are two fuel types, and the
reactor toggles twice:
```
Fuel A -> Fuel B -> Fuel A.
```


## Baseline Recycle Reactor
In this scenario two reactors are deployed in series:
```
Enrichment -> Base Reactor -> Separations Facility -> Fuel Fabrication-> Recycle Reactor.
```

The first reactor uses UOx fuel, and the second reactor uses MOx fuel, both
reactors are the Cycamore archetype.


## Mock CLOVER
In this scenario we employed one method of mimicking the effect of changing the
core loading over time by creating different recipes for assemblies at
different locations and matching preference changes to back-of-the-envelope
calculations.
