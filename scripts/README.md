# Scripts

These functions have the narrow purpose of the specific analysis we are doing
to compare features for these archetypes. They are collected here to increase
consistency and reproducibility of the analysis done in this repository.

We direct you to ARFC's
[transition-scenarios](https://github.com/arfc/transition-scenarios) and
[cymetric](https://github.com/cyclus/cymetric) to perform analysis on your own
results as those tools are intended to be more generally applicable.

## Quirks
I will try to list the assumptions and quirks made in the scripts for posterity.

### fuel_transactions.py
1. All fuels are assumed to have `fresh_<fuelname>` and `used_<fuelname>` as quantities of interest.