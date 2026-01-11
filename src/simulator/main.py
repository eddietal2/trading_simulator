import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os
import time
import json
from colorama import init, Fore, Back, Style

from .simulation import simulate_baseline_harvest_engine, simulate_exponential_growth

# Initialize colorama
init(autoreset=True)

def animate_ascii_art():
    """Animate the ASCII art banner with sliding and color cycling"""
    trading_art = [
        "████████╗██████╗ █████╗ ██████╗ ██╗███╗   ██╗ ██████╗",
        "╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝",
        "   ██║   ██████╔╝███████║██║  ██║██║██╔██╗ ██║██║  ███╗",
        "   ██║   ██╔══██╗██╔══██║██║  ██║██║██║╚██╗██║██║   ██║",
        "   ██║   ██║  ██║██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝",
        "   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝"
    ]
    
    simulator_art = [
        "███████╗██╗███╗   ███╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗",
        "██╔════╝██║████╗ ████║██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗",
        "███████╗██║██╔████╔██║██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝",
        "╚════██║██║██║╚██╔╝██║██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗",
        "███████║██║██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║",
        "╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝"
    ]
    
    # Slide in TRADING from left to right
    max_slide = 40
    for slide_pos in range(max_slide + 1):
        print(f"\033[2J\033[H", end="")  # Clear screen
        spaces = " " * (max_slide - slide_pos)
        print(f"{Fore.CYAN}{Style.BRIGHT}")
        for line in trading_art:
            print(f"{spaces}{line}")
        time.sleep(0.02)  # Fast slide
    
    time.sleep(0.3)  # Pause before SIMULATOR
    
    # Slide in SIMULATOR from left to right
    for slide_pos in range(max_slide + 1):
        print(f"\033[2J\033[H", end="")  # Clear screen
        spaces = " " * (max_slide - slide_pos)
        print(f"{Fore.CYAN}{Style.BRIGHT}")
        # Print TRADING (already in position)
        for line in trading_art:
            print(line)
        print()
        # Print SIMULATOR sliding in
        for line in simulator_art:
            print(f"{spaces}{line}")
        time.sleep(0.02)  # Fast slide
    
    time.sleep(0.5)  # Pause before color cycling
    
    # Color cycling animation
    colors = [Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.RED, Fore.MAGENTA]
    
    # Animate for 2 seconds (4 cycles)
    for cycle in range(4):
        color = colors[cycle % len(colors)]
        print(f"\033[2J\033[H", end="")  # Clear screen and move cursor to top
        print(f"{color}{Style.BRIGHT}")
        
        # Print TRADING
        for line in trading_art:
            print(line)
        print()
        
        # Print SIMULATOR
        for line in simulator_art:
            print(line)
        
        print(f"{Style.RESET_ALL}")
        time.sleep(0.5)  # Half second delay
    
    # Final static display
    print(f"\033[2J\033[H", end="")  # Clear screen
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    for line in trading_art:
        print(line)
    print()
    for line in simulator_art:
        print(line)
    print(f"{Style.RESET_ALL}")
    print()

def main():
    # ASCII Art Banner Animation
    animate_ascii_art()
    
    print(f"{Fore.CYAN}{Style.BRIGHT}💻 === Trading Simulator === 💻{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Available simulation types:{Style.RESET_ALL}")
    print(f"1. 📈 Exponential Growth")
    print(f"2. 💰 Baseline Harvest Engine")
    
    # Load and display last simulation parameters for option 3
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    last_params_file = os.path.join(project_root, "last_simulation_params.json")
    
    last_sim_info = ""
    if os.path.exists(last_params_file):
        try:
            with open(last_params_file, 'r') as f:
                params = json.load(f)
            
            sim_type = params['simulation_type']
            if sim_type == "exponential":
                last_sim_info = f" | Last: Exponential, ${params['initial_pot']:,.0f}, {params['weekly_return_rate']*100:.1f}%, {params['total_weeks']} weeks"
            else:  # baseline
                last_sim_info = f" | Last: Baseline, ${params['initial_pot']:,.0f}, ${params['engine_cap']:,.0f} cap, ${params['initial_vault']:,.0f} vault, {params['total_weeks']} weeks"
        except:
            last_sim_info = ""
    
    print(f"3. 🔄 Re-do Last Simulation{last_sim_info}")
    print(f"4. ❌ Exit")
    
    # Get simulation type
    while True:
        sim_choice = input(f"{Fore.YELLOW}Select simulation type (1, 2, 3, or 4) [2]: {Style.RESET_ALL}").strip()
        if sim_choice == "":
            sim_choice = "2"
        if sim_choice in ["1", "2", "3", "4"]:
            break
        print(f"{Fore.RED}❌ Invalid choice. Please enter 1, 2, 3, or 4.{Style.RESET_ALL}")
    
    if sim_choice == "4":
        print(f"{Fore.GREEN}👋 Exiting program. Goodbye!{Style.RESET_ALL}")
        return
    
    # Handle re-do last simulation
    if sim_choice == "3":
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)  # Go up one level from src/simulator to project root
        last_params_file = os.path.join(project_root, "last_simulation_params.json")
        if not os.path.exists(last_params_file):
            print(f"{Fore.RED}❌ No previous simulation found. Please run a simulation first.{Style.RESET_ALL}")
            return
        
        try:
            with open(last_params_file, 'r') as f:
                params = json.load(f)
            
            print(f"{Fore.GREEN}✅ Loaded last simulation parameters. Running simulation...{Style.RESET_ALL}")
            
            # Load all parameters and run simulation immediately
            simulation_type = params['simulation_type']
            initial_pot = params['initial_pot']
            weekly_return_rate = params['weekly_return_rate']
            total_weeks = params['total_weeks']
            
            if simulation_type == "baseline":
                engine_cap = params['engine_cap']
                initial_vault = params['initial_vault']
                growth_vault_pct = params['growth_vault_pct']
                harvest_vault_pct = params['harvest_vault_pct']
            
            # Skip to simulation
            skip_input = True
            
        except (json.JSONDecodeError, KeyError) as e:
            print(f"{Fore.RED}❌ Error loading last simulation parameters: {e}{Style.RESET_ALL}")
            return
    else:
        skip_input = False
        simulation_type = "exponential" if sim_choice == "1" else "baseline"
    
    # Get principal
    if not skip_input:
        default_principal = prev_initial_pot if 'prev_initial_pot' in locals() else 1000.0
        while True:
            principal_prompt = f"{Fore.YELLOW}💵 Enter principal/initial amount [{default_principal}]: {Style.RESET_ALL}"
            principal_input = input(principal_prompt).strip()
            if not principal_input:
                initial_pot = default_principal
                break
            try:
                initial_pot = float(principal_input)
                break
            except ValueError:
                print(f"{Fore.RED}❌ Invalid input. Please enter a valid number (e.g., {default_principal}).{Style.RESET_ALL}")
    else:
        print(f"{Fore.MAGENTA}💵 Using principal: ${initial_pot:,.2f}{Style.RESET_ALL}")
    
    if simulation_type == "exponential":
        if not skip_input:
            # Get weekly return rate for exponential growth
            default_rate_pct = (prev_weekly_return_rate * 100) if 'prev_weekly_return_rate' in locals() else 25
            while True:
                rate_prompt = f"{Fore.YELLOW}💹 Enter weekly return rate (percentage, e.g., 25 for 25%) [{default_rate_pct}]: {Style.RESET_ALL}"
                rate_input = input(rate_prompt).strip()
                if not rate_input:
                    weekly_return_rate = default_rate_pct / 100.0
                    break
                try:
                    weekly_return_rate = float(rate_input) / 100.0
                    break
                except ValueError:
                    print(f"{Fore.RED}❌ Invalid input. Please enter a valid number (e.g., {default_rate_pct}).{Style.RESET_ALL}")
            
            # Parameters for exponential growth
            default_weeks = prev_total_weeks if 'prev_total_weeks' in locals() else 52
            while True:
                periods_prompt = f"{Fore.YELLOW}📅 Enter number of periods/weeks [{default_weeks}]: {Style.RESET_ALL}"
                periods_input = input(periods_prompt).strip()
                if not periods_input:
                    total_weeks = default_weeks
                    break
                try:
                    total_weeks = int(periods_input)
                    break
                except ValueError:
                    print(f"{Fore.RED}❌ Invalid input. Please enter a valid integer (e.g., {default_weeks}).{Style.RESET_ALL}")
        else:
            print(f"{Fore.MAGENTA}💹 Using weekly return rate: {weekly_return_rate*100:.1f}%{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}📅 Using weeks: {total_weeks}{Style.RESET_ALL}")
        
        # Simulate exponential growth
        amounts = simulate_exponential_growth(initial_pot, weekly_return_rate, total_weeks)
        history = [{'week': i, 'amount': amount} for i, amount in enumerate(amounts)]
        title = "Exponential Growth Simulation"
        plot_title = f"Exponential Growth Simulation over {total_weeks} Weeks ({weekly_return_rate*100:.1f}% Weekly Gain)"
        
    else:  # 10k_baseline
        if not skip_input:
            # Parameters for 10K baseline
            weekly_return_rate = 0.25  # Default weekly return rate
            
            default_cap = prev_engine_cap if 'prev_engine_cap' in locals() else 10000.0
            while True:
                cap_prompt = f"{Fore.YELLOW}🎯 Enter engine cap [Example: {default_cap}]: {Style.RESET_ALL}"
                cap_input = input(cap_prompt).strip()
                if not cap_input:
                    engine_cap = default_cap
                    break
                try:
                    engine_cap = float(cap_input)
                    break
                except ValueError:
                    print(f"{Fore.RED}❌ Invalid input. Please enter a valid number (e.g., {default_cap}).{Style.RESET_ALL}")
            
            default_weeks = prev_total_weeks if 'prev_total_weeks' in locals() else 52
            while True:
                weeks_prompt = f"{Fore.YELLOW}📅 Enter total weeks [Example: {default_weeks}]: {Style.RESET_ALL}"
                weeks_input = input(weeks_prompt).strip()
                if not weeks_input:
                    total_weeks = default_weeks
                    break
                try:
                    total_weeks = int(weeks_input)
                    break
                except ValueError:
                    print(f"{Fore.RED}❌ Invalid input. Please enter a valid integer (e.g., {default_weeks}).{Style.RESET_ALL}")
            
            default_vault = prev_initial_vault if 'prev_initial_vault' in locals() else 300.0
            while True:
                vault_prompt = f"{Fore.YELLOW}🏦 Enter initial vault/savings amount [{default_vault}]: {Style.RESET_ALL}"
                vault_input = input(vault_prompt).strip()
                if not vault_input:
                    initial_vault = default_vault
                    break
                try:
                    initial_vault = float(vault_input)
                    break
                except ValueError:
                    print(f"{Fore.RED}❌ Invalid input. Please enter a valid number (e.g., {default_vault}).{Style.RESET_ALL}")
            
            default_growth_pct = prev_growth_vault_pct if 'prev_growth_vault_pct' in locals() else 50.0
            while True:
                growth_pct_prompt = f"{Fore.YELLOW}📊 Enter vault allocation % during growth phase (e.g., 50 for 50%) [{default_growth_pct}]: {Style.RESET_ALL}"
                growth_pct_input = input(growth_pct_prompt).strip()
                if not growth_pct_input:
                    growth_vault_pct = default_growth_pct
                    break
                try:
                    growth_vault_pct = float(growth_pct_input)
                    if 0 <= growth_vault_pct <= 100:
                        break
                    print(f"{Fore.RED}❌ Percentage must be between 0 and 100.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}❌ Invalid input. Please enter a valid number (e.g., {default_growth_pct}).{Style.RESET_ALL}")
            
            default_harvest_pct = prev_harvest_vault_pct if 'prev_harvest_vault_pct' in locals() else 25.0
            while True:
                harvest_pct_prompt = f"{Fore.YELLOW}🌾 Enter vault allocation % during harvest phase (e.g., 25 for 25%) [{default_harvest_pct}]: {Style.RESET_ALL}"
                harvest_pct_input = input(harvest_pct_prompt).strip()
                if not harvest_pct_input:
                    harvest_vault_pct = default_harvest_pct
                    break
                try:
                    harvest_vault_pct = float(harvest_pct_input)
                    if 0 <= harvest_vault_pct <= 100:
                        break
                    print(f"{Fore.RED}❌ Percentage must be between 0 and 100.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}❌ Invalid input. Please enter a valid number (e.g., {default_harvest_pct}).{Style.RESET_ALL}")
        else:
            print(f"{Fore.MAGENTA}🎯 Using engine cap: ${engine_cap:,.2f}{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}📅 Using weeks: {total_weeks}{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}🏦 Using initial vault: ${initial_vault:,.2f}{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}📊 Using growth vault %: {growth_vault_pct:.1f}%{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}🌾 Using harvest vault %: {harvest_vault_pct:.1f}%{Style.RESET_ALL}")
        
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

    # Save parameters for re-do functionality
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    params_file = os.path.join(project_root, "last_simulation_params.json")
    
    params = {
        'simulation_type': simulation_type,
        'initial_pot': initial_pot,
        'weekly_return_rate': weekly_return_rate,
        'total_weeks': total_weeks
    }
    
    if simulation_type == "baseline":
        params.update({
            'engine_cap': engine_cap,
            'initial_vault': initial_vault,
            'growth_vault_pct': growth_vault_pct,
            'harvest_vault_pct': harvest_vault_pct
        })
    
    with open(params_file, 'w') as f:
        json.dump(params, f, indent=2)
    print(f"{Fore.MAGENTA}💾 Simulation parameters saved for re-do functionality.{Style.RESET_ALL}")

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