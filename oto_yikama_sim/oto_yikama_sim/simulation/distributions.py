
import random

def customer_arrival(avg_customers):
    return random.randint(
        int(avg_customers * 0.8),
        int(avg_customers * 1.2)
    )

def wash_time(avg_minutes):
    return random.randint(
        int(avg_minutes * 0.7),
        int(avg_minutes * 1.3)
    )
