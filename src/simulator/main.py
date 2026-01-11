import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os
from colorama import init, Fore, Back, Style

from simulator.simulation import simulate_baseline_harvest_engine, simulate_exponential_growth

# Initialize colorama
init(autoreset=True)

def main():
    print(f"{Fore.CYAN}{Style.BRIGHT}🚀 === Trading Simulator === 🚀{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Available simulation types:{Style.RESET_ALL}")
    print(f"1. 📈 Exponential Growth")
    print(f"2. 💰 Baseline Harvest Engine")
    print(f"3. ❌ Exit")
    
    # Get simulation type
    while True:
        sim_choice = input(f"{Fore.YELLOW}Select simulation type (1, 2, or 3) [2]: {Style.RESET_ALL}").strip()
        if sim_choice == "":
            sim_choice = "2"
        if sim_choice in ["1", "2", "3"]:
            break
        print(f"{Fore.RED}❌ Invalid choice. Please enter 1, 2, or 3.{Style.RESET_ALL}")
    
    if sim_choice == "3":
        print(f"{Fore.GREEN}👋 Exiting program. Goodbye!{Style.RESET_ALL}")
        return
    
    simulation_type = "exponential" if sim_choice == "1" else "baseline"
    
    # Get principal
    while True:
        principal_input = input(f"{Fore.YELLOW}💵 Enter principal/initial amount [1000]: {Style.RESET_ALL}").strip()
        if not principal_input:
            initial_pot = 1000.0
            break
        try:
            initial_pot = float(principal_input)
            break
        except ValueError:
            print(f"{Fore.RED}❌ Invalid input. Please enter a valid number (e.g., 1000).{Style.RESET_ALL}")
    
    if simulation_type == "exponential":
        # Get weekly return rate for exponential growth
        while True:
            rate_input = input(f"{Fore.YELLOW}💹 Enter weekly return rate (percentage, e.g., 25 for 25%) [25]: {Style.RESET_ALL}").strip()
            if not rate_input:
                weekly_return_rate = 0.25
                break
            try:
                weekly_return_rate = float(rate_input) / 100.0
                break
            except ValueError:
                print(f"{Fore.RED}❌ Invalid input. Please enter a valid number (e.g., 25).{Style.RESET_ALL}")
        
        # Parameters for exponential growth
        while True:
            periods_input = input(f"{Fore.YELLOW}📅 Enter number of periods/weeks [52]: {Style.RESET_ALL}").strip()
            if not periods_input:
                total_weeks = 52
                break
            try:
                total_weeks = int(periods_input)
                break
            except ValueError:
                print(f"{Fore.RED}❌ Invalid input. Please enter a valid integer (e.g., 52).{Style.RESET_ALL}")
        
        # Simulate exponential growth
        amounts = simulate_exponential_growth(initial_pot, weekly_return_rate, total_weeks)
        history = [{'week': i, 'amount': amount} for i, amount in enumerate(amounts)]
        title = "Exponential Growth Simulation"
        plot_title = f"Exponential Growth Simulation over {total_weeks} Weeks ({weekly_return_rate*100:.1f}% Weekly Gain)"
        
    else:  # 10k_baseline
        # Parameters for 10K baseline
        weekly_return_rate = 0.25  # Default weekly return rate
        
        while True:
            cap_input = input(f"{Fore.YELLOW}🎯 Enter engine cap [Example: 10000]: {Style.RESET_ALL}").strip()
            if not cap_input:
                engine_cap = 10000.0
                break
            try:
                engine_cap = float(cap_input)
                break
            except ValueError:
                print(f"{Fore.RED}❌ Invalid input. Please enter a valid number (e.g., 10000).{Style.RESET_ALL}")
        
        while True:
            weeks_input = input(f"{Fore.YELLOW}📅 Enter total weeks [Example: 52]: {Style.RESET_ALL}").strip()
            if not weeks_input:
                total_weeks = 52
                break
            try:
                total_weeks = int(weeks_input)
                break
            except ValueError:
                print(f"{Fore.RED}❌ Invalid input. Please enter a valid integer (e.g., 52).{Style.RESET_ALL}")
        
        while True:
            vault_input = input(f"{Fore.YELLOW}🏦 Enter initial vault/savings amount [300]: {Style.RESET_ALL}").strip()
            if not vault_input:
                initial_vault = 300.0
                break
            try:
                initial_vault = float(vault_input)
                break
            except ValueError:
                print(f"{Fore.RED}❌ Invalid input. Please enter a valid number (e.g., 300).{Style.RESET_ALL}")
        
        while True:
            growth_pct_input = input(f"{Fore.YELLOW}📊 Enter vault allocation % during growth phase (e.g., 50 for 50%) [50]: {Style.RESET_ALL}").strip()
            if not growth_pct_input:
                growth_vault_pct = 50.0
                break
            try:
                growth_vault_pct = float(growth_pct_input)
                if 0 <= growth_vault_pct <= 100:
                    break
                print(f"{Fore.RED}❌ Percentage must be between 0 and 100.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}❌ Invalid input. Please enter a valid number (e.g., 50).{Style.RESET_ALL}")
        
        while True:
            harvest_pct_input = input(f"{Fore.YELLOW}🌾 Enter vault allocation % during harvest phase (e.g., 25 for 25%) [25]: {Style.RESET_ALL}").strip()
            if not harvest_pct_input:
                harvest_vault_pct = 25.0
                break
            try:
                harvest_vault_pct = float(harvest_pct_input)
                if 0 <= harvest_vault_pct <= 100:
                    break
                print(f"{Fore.RED}❌ Percentage must be between 0 and 100.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}❌ Invalid input. Please enter a valid number (e.g., 25).{Style.RESET_ALL}")
        
        # Simulate Baseline Harvest Engine
        history = simulate_baseline_harvest_engine(initial_pot, weekly_return_rate, engine_cap, total_weeks, initial_vault, growth_vault_pct, harvest_vault_pct)
        title = "Baseline Harvest Engine Simulation"
        plot_title = f"Baseline Harvest Engine Simulation over {total_weeks} Weeks"

    # Generate dates starting from Monday, January 5, 2026
    start_date = datetime(2026, 1, 5)  # Monday
    dates = [start_date + timedelta(weeks=i) for i in range(len(history))]

    # Create output directory if it doesn't exist
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Generate timestamp for run directory
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_dir_name = f"run_{simulation_type}_{timestamp}"
    run_dir = os.path.join(output_dir, run_dir_name)
    os.makedirs(run_dir, exist_ok=True)

    # File paths
    txt_filepath = os.path.join(run_dir, "simulation.txt")
    plot_filepath = os.path.join(run_dir, "plot.png")

    # Prepare output content
    output_lines = []
    output_lines.append(f"{title}:")
    if simulation_type == "exponential":
        output_lines.append("Week | Date (Monday) | Amount")
        output_lines.append("-" * 40)
        for entry, date in zip(history, dates):
            output_lines.append(f"{entry['week']:2d} | {date.strftime('%Y-%m-%d %A')} | ${entry['amount']:,.2f}")
        output_lines.append("")
        output_lines.append(f"Initial amount: ${initial_pot:,.2f}")
        output_lines.append(f"Final amount after {total_weeks} weeks: ${history[-1]['amount']:,.2f}")
        output_lines.append("")
        output_lines.append("Simulation Parameters:")
        output_lines.append(f"Weekly return rate: {weekly_return_rate*100:.1f}%")
        
        # Add monthly report for exponential growth
        output_lines.append("")
        output_lines.append("=" * 80)
        output_lines.append("MONTHLY REPORT")
        output_lines.append("=" * 80)
        output_lines.append("Month          | End Date   | Amount                | Monthly Growth        | Weekly Growth")
        output_lines.append("-" * 110)
        
        current_month = start_date.month
        current_year = start_date.year
        month_start_idx = 0
        
        for i, (entry, date) in enumerate(zip(history, dates)):
            # Check if we've reached end of month or end of simulation
            is_month_end = (i == len(history) - 1) or (dates[i + 1].month != current_month or dates[i + 1].year != current_year)
            
            if is_month_end:
                month_start_amount = history[month_start_idx]['amount']
                month_end_amount = entry['amount']
                monthly_growth = month_end_amount - month_start_amount
                
                # Calculate number of weeks in this month
                weeks_in_month = i - month_start_idx + 1
                weekly_growth = monthly_growth / weeks_in_month if weeks_in_month > 0 else 0
                
                month_name = date.strftime('%B %Y')
                output_lines.append(f"{month_name:14s} | {date.strftime('%Y-%m-%d'):10s} | ${entry['amount']:>19,.2f} | ${monthly_growth:>19,.2f} | ${weekly_growth:>13,.2f}")
                
                # Update for next month
                if i < len(history) - 1:
                    current_month = dates[i + 1].month
                    current_year = dates[i + 1].year
                    month_start_idx = i + 1
    else:
        output_lines.append("Week | Date (Monday) | Pot | Vault | Spend | Weekly Profit | Withdrawal")
        output_lines.append("-" * 80)
        for entry, date in zip(history, dates):
            output_lines.append(f"{entry['week']:2d} | {date.strftime('%Y-%m-%d %A')} | ${entry['pot']:,.2f} | ${entry['vault']:,.2f} | ${entry['spend']:,.2f} | ${entry['profit']:,.2f} | ${entry['withdrawal']:,.2f}")
        output_lines.append("")
        output_lines.append(f"Initial pot: ${initial_pot:,.2f}")
        output_lines.append(f"Initial vault: ${initial_vault:,.2f}")
        output_lines.append(f"Final pot: ${history[-1]['pot']:,.2f}")
        output_lines.append(f"Total vault: ${history[-1]['vault']:,.2f}")
        output_lines.append(f"Total spend: ${history[-1]['spend']:,.2f}")
        output_lines.append("")
        output_lines.append("Simulation Parameters:")
        output_lines.append(f"Growth phase vault allocation: {growth_vault_pct:.1f}%")
        output_lines.append(f"Harvest phase vault allocation: {harvest_vault_pct:.1f}%")
        
        # Add monthly report
        output_lines.append("")
        output_lines.append("=" * 80)
        output_lines.append("MONTHLY REPORT")
        output_lines.append("=" * 80)
        output_lines.append("Month          | End Date   | Pot Value            | Vault Savings         | Monthly Spending    | Weekly Spending")
        output_lines.append("-" * 130)
        
        current_month = start_date.month
        current_year = start_date.year
        month_start_idx = 0
        
        for i, (entry, date) in enumerate(zip(history, dates)):
            # Check if we've reached end of month or end of simulation
            is_month_end = (i == len(history) - 1) or (dates[i + 1].month != current_month or dates[i + 1].year != current_year)
            
            if is_month_end:
                month_start_spend = history[month_start_idx]['spend']
                month_end_spend = entry['spend']
                monthly_spend_increase = month_end_spend - month_start_spend
                
                # Calculate number of weeks in this month
                weeks_in_month = i - month_start_idx + 1
                spending_per_week = monthly_spend_increase / weeks_in_month if weeks_in_month > 0 else 0
                
                month_name = date.strftime('%B %Y')
                output_lines.append(f"{month_name:14s} | {date.strftime('%Y-%m-%d'):10s} | ${entry['pot']:>19,.2f} | ${entry['vault']:>19,.2f} | ${monthly_spend_increase:>21,.2f} | ${spending_per_week:>19,.2f}")
                
                # Update for next month
                if i < len(history) - 1:
                    current_month = dates[i + 1].month
                    current_year = dates[i + 1].year
                    month_start_idx = i + 1

    # Write text file
    with open(txt_filepath, 'w') as f:
        f.write("\n".join(output_lines))
    print(f"{Fore.GREEN}✅ Results saved to {run_dir}{Style.RESET_ALL}")

    # Print to console
    for line in output_lines:
        print(line)

    # Plot based on type
    weeks = [entry['week'] for entry in history]
    if simulation_type == "exponential":
        amounts = [entry['amount'] for entry in history]
        plt.plot(weeks, amounts)
    else:
        pots = [entry['pot'] for entry in history]
        vaults = [entry['vault'] for entry in history]
        spends = [entry['spend'] for entry in history]
        plt.plot(weeks, pots, label='Trading Pot', color='blue', linewidth=2)
        plt.plot(weeks, vaults, label='Vault', color='green', linewidth=2)
        plt.plot(weeks, spends, label='Spend', color='red', linewidth=2)
        plt.legend(loc='upper left')

    plt.title(plot_title)
    plt.xlabel('Weeks')
    plt.ylabel('Amount ($)')
    plt.grid(True)
    plt.savefig(plot_filepath)
    plt.close()  # Close the plot to allow program to exit

if __name__ == "__main__":
    main()