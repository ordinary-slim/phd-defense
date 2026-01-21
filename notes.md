# Storyline for PhD defense slides

# Introduction

# Substepping

## Slide: TOC

Around the time we were writing this last paper (Slimani 2024),
Professor Hodge published a paper where they were adressing
time-scale disparity in LPBF via a method called *substepping*,
and they were claiming speed-ups of up to 100x.

Recall that we did all this work and we just got a speed-up of 3
in a somewhat favorable scenario. So when we read the paper,
we thought we definitely had to have look.

## Slide: Schematic

Substepping (also known as multi-timestepping or subcyling),
is again a Domain Decomposition method; the domain is partitioned
into fast and slow partitions that employ different time-steps,
and are glued via Domain Decomposition.

As shown on the schematic here, the goal is to take small time-steps
close to the heat source and larger time-steps further away:
since the heat source only constraints time-step
size in its immediate vicinity, this method is very much adapted
to the localized nature of the problem.

## Slide: SOA

We started off studying the State Of the Art; pretty much
all the substepping references I know off in the litterature
are recompiled in this table.

The publication we were just mentioning is Puso 2023;
they were able to print a centimer-scale cantilever part
[...]

## Slide: Big lines of Slimani (2025)

So we set off to write a substepping paper.
