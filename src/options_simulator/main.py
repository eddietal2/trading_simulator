import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

from options_simulator.simulation import simulate_10K_baseline_harvest_engine, simulate_exponential_growth

def main():
    print("=== Options Simulator ===")
    print("Available simulation types:")
    print("1. Exponential Growth")
    print("2. 10K Baseline Harvest Engine")
    print("3. Exit")
    
    # Get simulation type
    while True:
        sim_choice = input("Select simulation type (1, 2, or 3) [2]: ").strip()
        if sim_choice == "":
            sim_choice = "2"
        if sim_choice in ["1", "2", "3"]:
            break
        print("Invalid choice. Please enter 1, 2, or 3.")
    
    if sim_choice == "3":
        print("Exiting program. Goodbye!")
        return
    
    simulation_type = "exponential" if sim_choice == "1" else "10k_baseline"
    
    # Get principal
    principal_input = input("Enter principal/initial amount [220]: ").strip()
    initial_pot = float(principal_input) if principal_input else 1000 
    
    if simulation_type == "exponential":
        # Parameters for exponential growth
        rate_input = input("Enter weekly growth rate (decimal, e.g., 0.25 for 25%) [0.25]: ").strip()
        weekly_return_rate = float(rate_input) if rate_input else 0.25
        
        periods_input = input("Enter number of periods/weeks [52]: ").strip()
        total_weeks = int(periods_input) if periods_input else 52
        
        # Simulate exponential growth
        amounts = simulate_exponential_growth(initial_pot, weekly_return_rate, total_weeks)
        history = [{'week': i, 'amount': amount} for i, amount in enumerate(amounts)]
        title = "Exponential Growth Simulation"
        plot_title = f"Exponential Growth Simulation over {total_weeks} Weeks ({weekly_return_rate*100:.1f}% Weekly Gain)"
        
    else:  # 10k_baseline
        # Parameters for 10K baseline
        rate_input = input("Enter weekly return rate (decimal, e.g., 0.25 for 25%): ").strip()
        weekly_return_rate = float(rate_input) if rate_input else 0.25
        
        cap_input = input("Enter engine cap [Example: 10000]: ").strip()
        engine_cap = float(cap_input) if cap_input else 10000
        
        weeks_input = input("Enter total weeks [Example: 52]: ").strip()
        total_weeks = int(weeks_input) if weeks_input else 52
        
        vault_input = input("Enter initial vault/savings amount [300]: ").strip()
        initial_vault = float(vault_input) if vault_input else 300.0
        
        # Simulate 10K baseline
        history = simulate_10K_baseline_harvest_engine(initial_pot, weekly_return_rate, engine_cap, total_weeks, initial_vault)
        title = "10K Baseline Harvest Engine Simulation"
        plot_title = f"10K Baseline Harvest Engine Simulation over {total_weeks} Weeks"

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

    # Write text file
    with open(txt_filepath, 'w') as f:
        f.write("\n".join(output_lines))
    print(f"\nResults saved to {run_dir}")

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

if __name__ == "__main__":
    main()