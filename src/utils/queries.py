from datetime import datetime

def find_maid_by_service(maids, service_name, location):
    return [maid for maid in maids if service_name in maid.services_available and maid.location == location]

def get_maid_schedule(schedules, maid_id):
    return [schedule for schedule in schedules if schedule.maid_id == maid_id]

def find_available_maid_for_service(maids, service_name, location, requested_date):
    available_maids = []
    
    # Filter maids based on the service and location
    for maid in maids:
        if service_name in maid.services_available and location in maid.location:
            for schedule in maid.schedule:
                if schedule['date'] == requested_date:
                    # Maid is available for the requested date
                    available_maids.append(maid)
    
    return available_maids

def schedule_maid(maids, service_name, location, requested_date, requested_time):
    available_maids = find_available_maid_for_service(maids, service_name, location, requested_date)
    
    if available_maids:
        for maid in available_maids:
            print(f"Maid {maid.name} is available for {service_name} on {requested_date} at {requested_time}")
            # Assign the maid to the requested schedule
            maid.schedule.append({'date': requested_date, 'time': requested_time})
            print(f"Schedule assigned: Maid {maid.name} | Date: {requested_date} | Time: {requested_time}")
            break
    else:
        print(f"No available maid for {service_name} in {location} on {requested_date}")

