from utils.loader import load_maids, load_services, load_schedules
from utils.queries import find_maid_by_service, get_maid_schedule

def main():
    # Load data
    maids = load_maids("data/maids.csv")
    services = load_services("data/services.csv")
    schedules = load_schedules("data/schedules.csv")

    # Example operations
    print("Loaded Maids:", maids[:2])
    print("Loaded Services:", services[:2])
    print("Loaded Schedules:", schedules[:2])

    # Query example
    available_maids = find_maid_by_service(maids, "broom", "Montreal")
    print("Available Maids for Broom in Montreal:", available_maids)

    maid_schedule = get_maid_schedule(schedules, "M001")
    print("Schedule for Maid M001:", maid_schedule)

if __name__ == "__main__":
    main()