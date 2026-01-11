import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from simulator.simulation import simulate_exponential_growth, simulate_baseline_harvest_engine

class TestSimulateExponentialGrowth:
    def test_default_parameters(self):
        """Test exponential growth with default parameters."""
        amounts = simulate_exponential_growth(1000)
        assert len(amounts) == 53  # initial + 52 weeks
        assert amounts[0] == 1000
        # Check compound growth
        expected_final = 1000 * (1 + 0.25) ** 52
        assert abs(amounts[-1] - expected_final) < 1e-6

    def test_custom_parameters(self):
        """Test with custom principal, rate, and periods."""
        P = 500
        r = 0.1
        periods = 10
        amounts = simulate_exponential_growth(P, r, periods)
        assert len(amounts) == 11  # initial + 10
        assert amounts[0] == 500
        expected_final = 500 * (1 + 0.1) ** 10
        assert abs(amounts[-1] - expected_final) < 1e-6

    def test_zero_growth(self):
        """Test with zero growth rate."""
        amounts = simulate_exponential_growth(1000, r=0, periods=5)
        assert len(amounts) == 6
        assert all(amount == 1000 for amount in amounts)

    def test_single_period(self):
        """Test with single period."""
        amounts = simulate_exponential_growth(1000, r=0.2, periods=1)
        assert len(amounts) == 2
        assert amounts[0] == 1000
        assert amounts[1] == 1000 * 1.2

class TestSimulate10KBaselineHarvestEngine:
    def test_accumulation_phase_only(self):
        """Test when pot never reaches cap - all accumulation."""
        history = simulate_baseline_harvest_engine(
            initial_pot=1000, weekly_return_rate=0.1, engine_cap=10000, total_weeks=10, initial_vault=0
        )
        assert len(history) == 10
        # Pot should grow but stay below cap
        for entry in history:
            assert entry['pot'] < 10000
            assert entry['withdrawal'] == 0
            assert entry['vault'] == 0
            assert entry['spend'] == 0
        # Check growth
        assert history[0]['pot'] == 1000 * 1.1
        assert history[1]['pot'] == history[0]['pot'] * 1.1

    def test_distribution_phase(self):
        """Test when pot reaches cap and starts distributing."""
        history = simulate_baseline_harvest_engine(
            initial_pot=9000, weekly_return_rate=0.2, engine_cap=10000, total_weeks=5, initial_vault=100
        )
        assert len(history) == 5
        # Find when pot reaches cap
        cap_reached = False
        for entry in history:
            if entry['pot'] >= 10000:
                cap_reached = True
                assert entry['pot'] == 10000  # Should be capped
                assert entry['withdrawal'] > 0
                assert entry['vault'] > 100  # Initial vault plus half withdrawal
                assert entry['spend'] > 0
            else:
                assert entry['withdrawal'] == 0
        assert cap_reached  # Should have reached cap

    def test_deficit_repair(self):
        """Test deficit rule - no withdrawals when below cap."""
        # Test case where pot grows but stays below cap
        history = simulate_baseline_harvest_engine(
            initial_pot=9000, weekly_return_rate=0.05, engine_cap=10000, total_weeks=1, initial_vault=0
        )
        assert len(history) == 1
        entry = history[0]
        assert entry['pot'] == 9000 * 1.05  # 9450
        assert entry['pot'] < 10000
        assert entry['withdrawal'] == 0
        assert entry['vault'] == 0
        assert entry['spend'] == 0

    def test_initial_values(self):
        """Test that initial values are set correctly."""
        history = simulate_baseline_harvest_engine(
            initial_pot=500, weekly_return_rate=0.1, engine_cap=1000, total_weeks=1, initial_vault=50
        )
        assert len(history) == 1
        entry = history[0]
        assert entry['week'] == 1
        assert entry['pot'] == 500 * 1.1
        assert entry['vault'] == 50  # No withdrawal yet
        assert entry['spend'] == 0
        assert entry['profit'] == 50
        assert entry['withdrawal'] == 0

    def test_zero_weeks(self):
        """Test with zero weeks - should return empty list."""
        history = simulate_baseline_harvest_engine(total_weeks=0)
        assert len(history) == 0

    def test_high_return_rate(self):
        """Test with high return rate to ensure capping works."""
        history = simulate_baseline_harvest_engine(
            initial_pot=5000, weekly_return_rate=1.0, engine_cap=6000, total_weeks=2, initial_vault=0
        )
        # First week: 5000 * 2 = 10000 > 6000, so cap at 6000, withdraw 4000, vault +=2000, spend +=2000
        assert history[0]['pot'] == 6000
        assert history[0]['withdrawal'] == 4000
        assert history[0]['vault'] == 2000
        assert history[0]['spend'] == 2000
        # Second week: 6000 * 2 = 12000 > 6000, withdraw 6000, etc.
        assert history[1]['pot'] == 6000
        assert history[1]['withdrawal'] == 6000
        assert history[1]['vault'] == 2000 + 3000 == 5000
        assert history[1]['spend'] == 2000 + 3000 == 5000