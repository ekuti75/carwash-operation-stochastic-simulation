
from distributions import customer_arrival, wash_time

def run_simulation(worker_count, avg_customers, avg_service_time):
    customers = customer_arrival(avg_customers)

    total_minutes = 10 * 60
    capacity_per_worker = total_minutes // wash_time(avg_service_time)

    total_capacity = capacity_per_worker * worker_count

    waiting_customers = max(0, customers - total_capacity)

    utilization = round((customers / max(total_capacity,1)) * 100, 2)

    return {
        "Toplam Müşteri": customers,
        "Toplam Kapasite": total_capacity,
        "Bekleyen Müşteri": waiting_customers,
        "Çalışan Kullanım Oranı (%)": utilization
    }
