import numpy as np

def simulate_exponential_growth(P, r=0.25, periods=52):
    """
    Simulate exponential growth over a number of periods using compound interest.
    Each period adds a 25% gain to the principal amount.

    Parameters:
    P (float): Principal amount
    r (float): Growth rate per period (decimal, default 0.25 for 25% weekly gain)
    periods (int): Number of periods (default 52 for weeks)

    Returns:
    list: List of amounts at the end of each period
    """
    amounts = [P]
    for n in range(1, periods + 1):
        A = P * (1 + r) ** n
        amounts.append(A)
    return amounts

def simulate_10K_baseline_harvest_engine(initial_pot=220, weekly_return_rate=0.25, engine_cap=10000, total_weeks=52, initial_vault=0.0):
    """
    Simulate the 10K Baseline Harvest Engine with accumulation and distribution phases.

    Rules:
    - Start with initial_pot and initial_vault
    - Weekly target: weekly_return_rate on current pot
    - Stage 1 (Weeks 1-18): Reinvest 100% until pot reaches engine_cap
    - Stage 2: Lock pot at engine_cap, withdraw excess profits (50% to vault, 50% to spend)
    - Deficit rule: If pot < engine_cap, no withdrawals until repaired

    Parameters:
    initial_pot (float): Starting trading pot amount
    weekly_return_rate (float): Weekly return rate (decimal)
    engine_cap (float): Maximum pot size before distribution
    total_weeks (int): Total weeks to simulate
    initial_vault (float): Starting vault/savings amount

    Returns:
    list: List of dicts with weekly results
    """
    pot = initial_pot
    vault = initial_vault
    spend = 0.0
    history = []

    for week in range(1, total_weeks + 1):
        # Calculate weekly profit
        profit = pot * weekly_return_rate
        pot += profit

        withdrawal = 0.0

        # Check if in accumulation phase
        if pot < engine_cap:
            # Accumulation: keep all, no withdrawal
            pass
        else:
            # Distribution: withdraw excess
            excess = pot - engine_cap
            if excess > 0:
                withdrawal = excess
                vault += withdrawal * 0.5
                spend += withdrawal * 0.5
                pot = engine_cap
            # If excess <=0, pot is below cap, no withdrawal

        history.append({
            'week': week,
            'pot': pot,
            'vault': vault,
            'spend': spend,
            'profit': profit,
            'withdrawal': withdrawal
        })

    return history