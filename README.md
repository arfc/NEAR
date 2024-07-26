# NEAR
[![Changelog Check](https://github.com/nsryan2/NEAR/actions/workflows/changelog_test.yml/badge.svg)](https://github.com/nsryan2/NEAR/actions/workflows/changelog_test.yml)

NEAR (Non-Equilibrium Archetypes of Reactors): Houses cyclus archetypes for non-equilibrium reactors with core-loading and enrichment variability.

> [!Note]
> Cite this work as (pending)...

## Installing
Each of the archetypes in this repository can be installed using `install.sh`.
For the script to work, you must install Cycamore from source, as the install
script essentially copies the source files over to your Cycamore directory and
installs them from there.

Then, from the top-level of this repository, run
```
bash install.sh
```
Then you will be prompted to give the relative path from NEAR to Cycamore, and
asked which archetype you wish to install.

You can find installation instructions for  Cyclus, Cycamore, and Cymetric
online at [https://fuelcycle.org/user/install.html](https://fuelcycle.org/user/install.html).

## ./Baseline/
Contains a single deployment of a traditional Cycamore reactor archetype along with the corresponding analysis notebook and output file.

## ./EVER/
Houses the Enrichment Versatile non-Equilibrium Reactor (EVER), a generic Cyclus archetype that has the capability to update the recipe of fuel in a reactor.

## ./CLOVER/ (in progress)
Houses the Core LOading Versatile non-Equilibrium Reactor (CLOVER), a generic Cyclus archetype that has the capability to update the loading pattern of a reactor core.

## ./writing/
This folder contains the writing on this project, and is governed by the license therein.

> [!Important]
> This code is licensed under a BSD 3-Clause License, with the exception of the writing directory (which contains a separate license).
