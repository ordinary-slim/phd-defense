# Storyline for PhD defense slides

## TITLE CARD!!!!

Hello everyone, the tile of my phd is Computational strategies for time-accurate simulation of part-scale LPBF
there are many things to unpack in this sentence alone, let's start with the application

## LPBF as a technology

first and foremost, what are we working on ? What is LPBF ?

LPBF or ISO name PBF-xx is a type of metal AM. the main types of MAM are WAAM (bam!), DED and LPBF

in all of these we're melting metal in-situ to build a part
**WAAM**:  we're melting wire
**DED**: we're melting blown powder
**LPBF**: we place a whole powder layer above the build and then we melt it

## What's special about LPBF

| Parameter      | WAAM                        | DED                         | LPBF                        |
|-------------   |-----------------------------|-----------------------------|-----------------------------|
| Radius R       | ~2–4 mm bead radius         | ~0.5–1.5 mm track radius    | ~25–100 µm track radius      |
| Laser speed V  | ~3–10 mm/s (torch)          | ~5–20 mm/s scan speed       | ~400–1400 mm/s scan speed   |


So LPBF is small and fast

## Modelling challenge

Big disparity in both *spatial* and *temporal* scales.


|             | Spatial scale              | Temporal scales                               |
|-------------|-------------------         |----------------------                         |
| Heat source | 100 µm (R)                 | $T_{hs} = \frac{R}{V}$ =                        |
|             |                            | := time it takes the heat source to move by R |
| Part        | Decimeters (length of part) | $T_{print} := net printing time              |
|             |                             | (cumulative laser-on time                    |


The contrast of spatial scales can be upwards of 10⁶.
It is similarly large in time: T_{hs} = O(10⁻⁴ s) while
T_{print} = O(tens of minutes), so the contrast of time scales is upwards of 10⁸

## How do these things come up

We want to cover something large/slow (spatial or temporal domain i.e part and build interval)
while resolving something small/fast (laser radius / motion).

## Cube example

**TODO**
