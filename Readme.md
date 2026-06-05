# Visual Mathematics of Finance

Most finance courses teach the equations.

This repository focuses on the intuition behind those equations.

The goal is to visualize concepts from stochastic calculus, derivatives pricing, portfolio theory, and quantitative finance using animations built with **Manim**.

Instead of memorizing formulas, the idea is to see what those formulas are actually describing.

---

## Why I Started This Project

While studying quantitative finance, I realized that many concepts become much easier once you can visualize them.

Brownian Motion, Ito's Lemma, Delta Hedging, and the Black–Scholes equation are usually introduced through mathematical derivations. The mathematics is elegant, but it can be difficult to build intuition from symbols alone.

This repository is my attempt to make those ideas easier to understand through animation.

---

## Quick Start

Clone the repository:

```bash
git clone https://github.com/Fortnight-wow/Visual-Mathematics-of-Finance.git
cd Visual-Mathematics-of-Finance

## Current Animations

### Stochastic Processes

- Brownian Motion
- Geometric Brownian Motion

### Stochastic Calculus

- Ito's Lemma

### Derivatives Pricing

- Black-Scholes PDE
- Delta Hedging

---

## Repository Structure

```text
Visual-Mathematics-of-Finance/

├── animations/
│   ├── brownian_motion.py
│   ├── geometric_brownian_motion.py
│   ├── ito_lemma.py
│   ├── black_scholes_pde.py
│   └── delta_hedging.py
│
├── assets/
├── rendered_videos/
├── requirements.txt
└── README.md
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/Fortnight-wow/Visual-Mathematics-of-Finance.git

cd Visual-Mathematics-of-Finance
```

## Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install manim numpy
```

---

# Running Animations

## Preview Render

```bash
manim -pql animations/brownian_motion.py BrownianMotion
```

### Options

```text
-p    Open video after rendering

-ql   Low quality

-qm   Medium quality

-qh   High quality

-qk   4K quality
```

---

## High Quality Render

```bash
manim -pqh animations/geometric_brownian_motion.py GeometricBrownianMotion
```

---

## Render Ito's Lemma

```bash
manim -pqh animations/ito_lemma.py ItoLemma
```

---

## Render Black-Scholes PDE

```bash
manim -pqh animations/black_scholes_pde.py BlackScholesPDE
```

---

## Render Delta Hedging

```bash
manim -pqh animations/delta_hedging.py DeltaHedging
```

---

# Example Learning Path

If you're new to quantitative finance, I recommend viewing the animations in the following order:

1. Brownian Motion
2. Geometric Brownian Motion
3. Ito's Lemma
4. Black-Scholes PDE
5. Delta Hedging

This sequence follows the same progression used in many quantitative finance courses.

---

# Roadmap

## Stochastic Processes

- Brownian Motion
- Geometric Brownian Motion
- Mean Reversion
- Ornstein-Uhlenbeck Process

## Option Pricing

- Greeks Visualization
- Binomial Trees
- Monte Carlo Pricing
- Implied Volatility
- Volatility Smile
- Volatility Surface

## Interest Rate Models

- Vasicek Model
- CIR Model
- Hull-White Model
- Yield Curve Dynamics

## Portfolio Theory

- Efficient Frontier
- CAPM
- Risk vs Return
- Diversification

## Risk Management

- Value at Risk (VaR)
- Conditional VaR (CVaR)
- Stress Testing

## Advanced Quantitative Finance

- Heston Model
- SABR Model
- Risk-Neutral Measure
- Martingales
- Change of Measure

---

# Long-Term Goal

The long-term goal is to build a visual library of quantitative finance concepts.

If a student can watch an animation and immediately understand a concept that previously required several pages of notes, then the project has achieved its purpose.

---

# References

- John Hull — *Options, Futures, and Other Derivatives*
- Steven Shreve — *Stochastic Calculus for Finance*
- Sheldon Ross — *An Elementary Introduction to Mathematical Finance*
- Paul Wilmott — *Paul Wilmott on Quantitative Finance*

---

# License

MIT License

Copyright © Fortnight-wow

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.