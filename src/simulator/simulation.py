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

def simulate_baseline_harvest_engine(initial_pot=0, weekly_return_rate=0, engine_cap=0, total_weeks=0, initial_vault=0, growth_vault_pct=50, harvest_vault_pct=25):
    """
    Simulate the Baseline Harvest Engine with accumulation and distribution phases.

    Rules:
    - Start with initial_pot and initial_vault
    - Weekly target: weekly_return_rate on current pot
    - Stage 1 (Growth Phase): Reinvest until pot reaches engine_cap
      - When pot < engine_cap and profit pushes pot above cap, allocate excess using growth_vault_pct
    - Stage 2 (Harvest Phase): Lock pot at engine_cap, withdraw excess profits using harvest_vault_pct
    - Deficit rule: If pot < engine_cap, no withdrawals until repaired

    Parameters:
    initial_pot (float): Starting trading pot amount
    weekly_return_rate (float): Weekly return rate (decimal)
    engine_cap (float): Maximum pot size before distribution
    total_weeks (int): Total weeks to simulate
    initial_vault (float): Starting vault/savings amount
    growth_vault_pct (float): Percentage to vault during growth phase (default 50)
    harvest_vault_pct (float): Percentage to vault during harvest phase (default 25)

    Returns:
    list: List of dicts with weekly results
    """
    pot = initial_pot
    vault = initial_vault
    spend = 0.0
    history = []
    in_harvest_phase = False

    for week in range(1, total_weeks + 1):
        # Calculate weekly profit
        profit = pot * weekly_return_rate
        pot += profit

        withdrawal = 0.0

        # Check if in accumulation phase
        if pot < engine_cap:
            # Below cap - back to growth phase
            in_harvest_phase = False
        else:
            # Pot has reached or exceeded cap
            excess = pot - engine_cap
            if excess > 0:
                withdrawal = excess
                
                # Determine which phase we're in
                if not in_harvest_phase:
                    # First time reaching cap (growth phase)
                    vault_allocation = growth_vault_pct / 100.0
                    in_harvest_phase = True
                else:
                    # Already in harvest phase
                    vault_allocation = harvest_vault_pct / 100.0
                
                vault += withdrawal * vault_allocation
                spend += withdrawal * (1 - vault_allocation)
                pot = engine_cap

        history.append({
            'week': week,
            'pot': pot,
            'vault': vault,
            'spend': spend,
            'profit': profit,
            'withdrawal': withdrawal
        })

    return history