# Trading Simulator Architecture

This document contains a visual representation of the Trading Simulator's architecture using Mermaid.js.

## Architecture Overview

The Trading Simulator is a Python-based application that provides two types of trading simulations:
- **Exponential Growth**: Compound interest-based growth simulation
- **Baseline Harvest Engine**: Accumulation and distribution phase simulation with vault allocation

## Architecture Diagram

```mermaid
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
```

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

Generated on: 2026-01-11 00:14:23
