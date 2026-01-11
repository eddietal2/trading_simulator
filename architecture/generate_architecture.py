#!/usr/bin/env python3
"""
Trading Simulator Architecture Generator

This script generates a Mermaid.js graph representing the architecture
of the Trading Simulator application.
"""

import os
import json
from pathlib import Path
from datetime import datetime


def generate_architecture_graph():
    """Generate a Mermaid.js graph of the trading simulator architecture."""

    mermaid_graph = '''```mermaid
graph TB
    %% User Interface Layer
    subgraph "User Interface Layer"
        CLI["CLI Interface<br/>main.py"]
        ANIM["ASCII Animation<br/>animate_ascii_art()"]
        MENU["Menu System<br/>Parameter Input"]
    end

    %% Core Logic Layer
    subgraph "Core Logic Layer"
        MAIN["Main Controller<br/>main()"]
        PARAM["Parameter Handler<br/>Input Validation"]
        OUTPUT["Output Generator<br/>Reports & Charts"]
    end

    %% Simulation Engine Layer
    subgraph "Simulation Engine Layer"
        EXP["Exponential Growth<br/>simulate_exponential_growth()"]
        BASE["Baseline Harvest Engine<br/>simulate_baseline_harvest_engine()"]
    end

    %% Data Management Layer
    subgraph "Data Management Layer"
        JSON["Parameter Persistence<br/>last_simulation_params.json"]
        REPORTS["Report Generation<br/>simulation.txt + plot.png"]
        HISTORY["Simulation History<br/>Weekly Data Points"]
    end

    %% Testing Layer
    subgraph "Testing Layer"
        UNIT["Unit Tests<br/>test_simulation.py"]
        PYTEST["pytest Framework"]
    end

    %% External Dependencies
    subgraph "External Dependencies"
        NUMPY["numpy<br/>Numerical Computing"]
        MATPLOTLIB["matplotlib<br/>Chart Generation"]
        COLORAMA["colorama<br/>Terminal Colors"]
    end

    %% Flow Connections
    CLI --> ANIM
    ANIM --> MENU
    MENU --> MAIN
    MAIN --> PARAM
    PARAM --> EXP
    PARAM --> BASE
    EXP --> OUTPUT
    BASE --> OUTPUT
    OUTPUT --> JSON
    OUTPUT --> REPORTS
    OUTPUT --> HISTORY

    %% Testing Connections
    UNIT --> PYTEST
    PYTEST -.-> EXP
    PYTEST -.-> BASE

    %% Dependency Connections
    EXP -.-> NUMPY
    BASE -.-> NUMPY
    OUTPUT -.-> MATPLOTLIB
    CLI -.-> COLORAMA
    MENU -.-> COLORAMA

    %% Styling
    classDef uiLayer fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef logicLayer fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef engineLayer fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    classDef dataLayer fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef testLayer fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    classDef depLayer fill:#f5f5f5,stroke:#424242,stroke-width:2px

    class CLI,MENU,ANIM uiLayer
    class MAIN,PARAM,OUTPUT logicLayer
    class EXP,BASE engineLayer
    class JSON,REPORTS,HISTORY dataLayer
    class UNIT,PYTEST testLayer
    class NUMPY,MATPLOTLIB,COLORAMA depLayer
```'''

    return mermaid_graph


def generate_detailed_architecture():
    """Generate a detailed Mermaid.js graph with more technical details."""

    detailed_graph = '''```mermaid
graph TB
    %% Entry Point
    subgraph "Entry Point"
        MAIN_PY["main.py<br/>if __name__ == '__main__'"]
    end

    %% CLI Components
    subgraph "CLI Components"
        ASCII_ART["animate_ascii_art()<br/>ASCII Banner Display"]
        MENU_SYSTEM["Menu System<br/>Simulation Type Selection"]
        INPUT_HANDLER["Input Handler<br/>Parameter Collection"]
        VALIDATION["Input Validation<br/>Type & Range Checking"]
    end

    %% Simulation Types
    subgraph "Simulation Types"
        EXP_SIM["Exponential Growth<br/>simulate_exponential_growth()"]
        BASE_SIM["Baseline Harvest Engine<br/>simulate_baseline_harvest_engine()"]
    end

    %% Core Algorithms
    subgraph "Core Algorithms"
        COMPOUND["Compound Interest<br/>A = P(1+r)^n"]
        HARVEST_LOGIC["Harvest Logic<br/>Growth vs Distribution Phase"]
        VAULT_ALLOCATION["Vault Allocation<br/>Percentage-based Savings"]
        ENGINE_CAP["Engine Cap Logic<br/>Maximum Pot Size Control"]
    end

    %% Data Processing
    subgraph "Data Processing"
        WEEKLY_CALC["Weekly Calculations<br/>Profit & Growth"]
        HISTORY_BUILDER["History Builder<br/>Time Series Data"]
        MONTHLY_REPORTS["Monthly Reports<br/>Aggregated Statistics"]
    end

    %% Output Generation
    subgraph "Output Generation"
        TEXT_REPORT["Text Report<br/>simulation.txt"]
        CHART_GEN["Chart Generation<br/>plot.png via matplotlib"]
        CONSOLE_OUTPUT["Console Output<br/>Terminal Display"]
    end

    %% File Management
    subgraph "File Management"
        PARAM_SAVE["Parameter Save<br/>JSON Persistence"]
        OUTPUT_DIR["Output Directory<br/>run_*/ Structure"]
        TIMESTAMP["Timestamp Naming<br/>YYYY-MM-DD_HH-MM-SS"]
    end

    %% Testing Framework
    subgraph "Testing Framework"
        EXP_TESTS["Test Exponential Growth<br/>Multiple Scenarios"]
        BASE_TESTS["Test Baseline Engine<br/>Edge Cases & Logic"]
        ASSERTIONS["Assertion Checks<br/>Numerical Accuracy"]
    end

    %% Flow
    MAIN_PY --> ASCII_ART
    ASCII_ART --> MENU_SYSTEM
    MENU_SYSTEM --> INPUT_HANDLER
    INPUT_HANDLER --> VALIDATION

    VALIDATION --> EXP_SIM
    VALIDATION --> BASE_SIM

    EXP_SIM --> COMPOUND
    BASE_SIM --> HARVEST_LOGIC
    HARVEST_LOGIC --> VAULT_ALLOCATION
    HARVEST_LOGIC --> ENGINE_CAP

    COMPOUND --> WEEKLY_CALC
    HARVEST_LOGIC --> WEEKLY_CALC
    WEEKLY_CALC --> HISTORY_BUILDER
    HISTORY_BUILDER --> MONTHLY_REPORTS

    HISTORY_BUILDER --> TEXT_REPORT
    HISTORY_BUILDER --> CHART_GEN
    HISTORY_BUILDER --> CONSOLE_OUTPUT

    VALIDATION --> PARAM_SAVE
    TEXT_REPORT --> OUTPUT_DIR
    CHART_GEN --> OUTPUT_DIR
    TIMESTAMP --> OUTPUT_DIR

    EXP_TESTS --> EXP_SIM
    BASE_TESTS --> BASE_SIM
    ASSERTIONS --> EXP_TESTS
    ASSERTIONS --> BASE_TESTS

    %% Styling
    classDef entry fill:#ffebee,stroke:#b71c1c
    classDef cli fill:#e3f2fd,stroke:#1976d2
    classDef sim fill:#e8f5e8,stroke:#388e3c
    classDef algo fill:#fff3e0,stroke:#f57c00
    classDef data fill:#f3e5f5,stroke:#7b1fa2
    classDef output fill:#e0f2f1,stroke:#00695c
    classDef file fill:#fafafa,stroke:#424242
    classDef test fill:#fce4ec,stroke:#c2185b

    class MAIN_PY entry
    class ASCII_ART,MENU_SYSTEM,INPUT_HANDLER,VALIDATION cli
    class EXP_SIM,BASE_SIM sim
    class COMPOUND,HARVEST_LOGIC,VAULT_ALLOCATION,ENGINE_CAP algo
    class WEEKLY_CALC,HISTORY_BUILDER,MONTHLY_REPORTS data
    class TEXT_REPORT,CHART_GEN,CONSOLE_OUTPUT output
    class PARAM_SAVE,OUTPUT_DIR,TIMESTAMP file
    class EXP_TESTS,BASE_TESTS,ASSERTIONS test
```'''

    return detailed_graph


def save_architecture_graph(filename="architecture.md", detailed=False):
    """Save the architecture graph to a markdown file."""

    if detailed:
        graph = generate_architecture_graph()
        title = "# Trading Simulator Architecture (Detailed)"
    else:
        graph = generate_architecture_graph()
        title = "# Trading Simulator Architecture"

    content = f"""{title}

This document contains a visual representation of the Trading Simulator's architecture using Mermaid.js.

## Architecture Overview

The Trading Simulator is a Python-based application that provides two types of trading simulations:
- **Exponential Growth**: Compound interest-based growth simulation
- **Baseline Harvest Engine**: Accumulation and distribution phase simulation with vault allocation

## Architecture Diagram

{graph}

## Key Components

### User Interface Layer
- **CLI Interface**: Command-line interface with colored output
- **ASCII Animation**: Welcome banner display
- **Menu System**: Interactive parameter input with validation

### Core Logic Layer
- **Main Controller**: Application flow orchestration
- **Parameter Handler**: Input validation and default value management
- **Output Generator**: Report and chart generation

### Simulation Engine Layer
- **Exponential Growth**: Compound interest calculations
- **Baseline Harvest Engine**: Multi-phase simulation with growth/harvest logic

### Data Management Layer
- **Parameter Persistence**: JSON-based configuration saving
- **Report Generation**: Text and graphical output
- **Simulation History**: Time-series data storage

### Testing Layer
- **Unit Tests**: Comprehensive test coverage for all algorithms
- **pytest Framework**: Test execution and reporting

### External Dependencies
- **numpy**: Numerical computing for calculations
- **matplotlib**: Chart generation and visualization
- **colorama**: Cross-platform colored terminal output

## Data Flow

1. User selects simulation type via CLI menu
2. Parameters are collected and validated
3. Simulation runs using appropriate algorithm
4. Results are processed and formatted
5. Output is generated (console, text file, chart)
6. Parameters are saved for future re-runs

## File Structure

```
trading_simulator/
├── src/simulator/
│   ├── main.py              # CLI interface and main logic
│   └── simulation.py        # Core simulation algorithms
├── tests/
│   └── test_simulation.py   # Unit tests
├── architecture/
│   └── generate_architecture.py  # This script
├── output/                  # Generated reports and charts
├── pyproject.toml          # Project configuration
└── last_simulation_params.json  # Parameter persistence
```

## Usage

To regenerate this architecture diagram, run:

```bash
python architecture/generate_architecture.py
```

Or for detailed view:

```bash
python architecture/generate_architecture.py --detailed
```

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

    # Get the directory of this script
    script_dir = Path(__file__).parent
    output_path = script_dir / filename

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Architecture diagram saved to: {output_path}")
    return output_path


def main():
    """Main function to generate architecture documentation."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate Trading Simulator Architecture Diagram')
    parser.add_argument('--detailed', action='store_true', help='Generate detailed architecture diagram')
    parser.add_argument('--output', '-o', default='architecture.md', help='Output filename')

    args = parser.parse_args()

    save_architecture_graph(args.output, args.detailed)


if __name__ == "__main__":
    main()