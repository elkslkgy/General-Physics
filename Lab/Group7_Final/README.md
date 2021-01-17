# Group 7 Final Project Readme

## Project Title: (請想出有趣的project名)

## Members

* 鄭百凱 B05902128
* 陳盈如 B05902118
* 馮永輝 B05902100

## Introduction



## Project Description



## Motivation



## Goals


# Progress

## Week 1

We considered using a microscopic spring-ball system to model the materials in the block. For simplicity, we assumed the bullet was a spherical projectile. We chose to use glass as the primary material in modeling the block. Other materials will be added later as the project goes on.

For the collision, we contemplated between 2 options; have the bullet collide into a spherical (glass) atom to stretch the bonds until its bonds break, or have the bullet collide into the spring, and break the spring if the bullet's kinetic energy exceeds the spring's potential energy.

## Week 2
  
Because the microscopic modeling via the an atom colliding with a spring was too complicated, we are no longer using microscopic particles to model the particle; instead, we are using macroscopic blocks.
  
Blocks are identical (for now) and are stored in lists for convenience.
  
We also made progress on the finding the minimum force required of the bullet to pass through (break) the block. We found out that we can  use a stress-strain curve to find such force:

![Stress-strain curve](https://upload.wikimedia.org/wikipedia/commons/1/15/StressStrainWEB.svg "Stress-strain curve")

However, since it would be impractical to plot the curve, we decided to use preexisting sources to find the Yield Strength; for simplicity, we also decided to use brittle materials in our experiment so that we do not have to account for plastic deformation, so that Yield Strength is close enough to Ultimate Tensile Strength (the stress required for the object to break).

Thus, the force required to pierce the block is F = A * UTS, where A is the surface area of the applied force. Assuming that the material is brittle, we can choose Yield Strength over UTS if the latter is not available.

We also plotted a graph to show the velocity over time, and solved a variety of bugs.

As of now, we have yet to apply air resistance into our equation thus dp/dt is still 0.
