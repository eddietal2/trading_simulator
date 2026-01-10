# 10K Baseline Harvest Engine Simulator

A Python project to simulate the 10K Baseline Harvest Engine with accumulation and distribution phases over 52 weeks.

## Description

This simulator models the 10K Baseline Harvest Engine strategy starting with $220, aiming for 25% weekly returns. It includes:
- **Accumulation Phase**: Reinvest profits until reaching $10,000 engine cap
- **Distribution Phase**: Withdraw excess profits above $10,000 (50% to vault, 50% to spend)
- **Deficit Protection**: No withdrawals if pot falls below $10,000

## Installation

1. Ensure you have Python 3.8+ installed.
2. Install the package:

```bash
pip install -e .
```

## Usage

Run the simulation:

```bash
exponential-growth-simulator
```

Or directly:

```bash
python -m options_simulator.main
```

## Parameters

- `initial_pot`: Starting amount ($220)
- `weekly_return_rate`: Weekly return rate (0.25 or 25%)
- `engine_cap`: Maximum pot size before distribution ($10,000)
- `total_weeks`: Number of weeks to simulate (52)

## Simulation Rules

1. **Starting Block**: Begin with $220
2. **Weekly Target**: 25% return on current pot
3. **Stage 1 (Weeks 1-18)**: Reinvest 100% of profits until $10,000
4. **Engine Cap**: Distribution starts when pot reaches $10,000
5. **Stage 2 (Weeks 19-52)**: Pot locked at $10,000, withdraw excess
6. **50/50 Split**: Withdrawals split equally to Vault and Spend
7. **Deficit Rule**: No distributions if pot < $10,000
8. **Risk Limit**: Max 5% of pot per trade (not implemented in simulation)

## Example Output

- **Initial Pot**: $220
- **Engine Hit**: Week 18
- **Final Pot**: $10,000
- **Total Vault**: $43,606.23
- **Total Spend**: $43,606.23

## Math Function

Weekly profit = current_pot × 0.25

Pot updates based on accumulation/distribution rules.