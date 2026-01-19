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

-- Consider including this video schematic:
https://commons.wikimedia.org/wiki/File:Build_chamber_process_animation.webm

## What's special about LPBF

| Parameter      | WAAM                        | DED                         | LPBF                        |
|-------------   |-----------------------------|-----------------------------|-----------------------------|
| Radius R       | ~2–4 mm bead radius         | ~0.5–1.5 mm track radius    | ~25–100 µm track radius      |
| Laser speed V  | ~3–10 mm/s (torch)          | ~5–20 mm/s scan speed       | ~400–1400 mm/s scan speed   |


So LPBF is small and fast

## Part scale simulation, why

Many reasons to do simulation. Many things can go wrong and many things can be improved upon
- Part failure
- Desirable microstructure
- Process parameter optimization

(image of build failure)

Simulation can help on these things

## Part scale simulation, why not

Simulation is too slow, because the process is extremely ``multiscale'' (Hodge, 2021)

## LPBF: extremely multiscale 1

<!-- todo -->

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

## Next slide

### Option 1:
Talk about challenges when modelling now 

### Option 2:
Introduce modelling first

## Cube example

**TODO**

## 15/01/2025

Notes on mock presentation:
- [x] Larger videos + weird black margin in all videos
- [x] Overlay manufactured play symbol with actual play / pause symbol
- [ ] Establish better the layer / hatch nature in MAM
  [ ]   - Maybe go part -> gcode?
- [ ] Better transition into "Extremely multiscale" (slide 4)
- [ ] Phase change missing!
- [ ] Slide 15 extra label
- [x] Zoom-in slide 21 temperatures
- [ ] Include figure for quasy-steadiness of thermal profile
- [ ] Arrow for speed in 31
- [ ] 34: Add other metric
  [ ]   - Add image for Omega_m resizing
- [ ] 36: Zoom in
- [ ] Two tails, superposition
- [ ] Add slides explaining why Hodge is getting 100x
  [ ]   - Make this into SOA slide: DD Speedup dt_f dt_s
- [ ] Zoom-in 46
- [ ] Establish Hodge <-> Dirichlet and Robin-Robin <-> Robin
- [ ] Leave last frame at end of video

## 18/01/2025

- [ ] Substepping diffusion time scale: reorganize slide
- [ ] Substepping: add table
