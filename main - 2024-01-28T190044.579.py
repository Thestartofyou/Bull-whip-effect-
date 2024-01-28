import numpy as np
import matplotlib.pyplot as plt

def simulate_bullwhip_effect(initial_demand, periods):
    consumer_demand = np.random.normal(initial_demand, 5, periods)
    retailer_orders = np.zeros(periods)
    distributor_orders = np.zeros(periods)
    manufacturer_orders = np.zeros(periods)
    
    retailer_inventory = np.zeros(periods)
    distributor_inventory = np.zeros(periods)
    manufacturer_inventory = np.zeros(periods)

    for i in range(periods):
        # Retailer
        retailer_orders[i] = consumer_demand[i] + np.random.normal(0, 3)
        retailer_inventory[i] = max(0, retailer_inventory[i-1] + retailer_orders[i] - consumer_demand[i])

        # Distributor
        distributor_orders[i] = retailer_orders[i] + np.random.normal(0, 2)
        distributor_inventory[i] = max(0, distributor_inventory[i-1] + distributor_orders[i] - retailer_orders[i])

        # Manufacturer
        manufacturer_orders[i] = distributor_orders[i] + np.random.normal(0, 1)
        manufacturer_inventory[i] = max(0, manufacturer_inventory[i-1] + manufacturer_orders[i] - distributor_orders[i])

    return consumer_demand, retailer_orders, distributor_orders, manufacturer_orders

def plot_results(consumer_demand, retailer_orders, distributor_orders, manufacturer_orders):
    plt.figure(figsize=(10, 6))
    plt.plot(consumer_demand, label='Consumer Demand', linestyle='dashed')
    plt.plot(retailer_orders, label='Retailer Orders')
    plt.plot(distributor_orders, label='Distributor Orders')
    plt.plot(manufacturer_orders, label='Manufacturer Orders')

    plt.title('Bullwhip Effect Simulation')
    plt.xlabel('Periods')
    plt.ylabel('Quantity')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    np.random.seed(42)  # Set a seed for reproducibility
    initial_demand = 50
    periods = 50

    consumer_demand, retailer_orders, distributor_orders, manufacturer_orders = simulate_bullwhip_effect(initial_demand, periods)
    plot_results(consumer_demand, retailer_orders, distributor_orders, manufacturer_orders)
