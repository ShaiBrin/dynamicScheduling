def find_maid_by_service(maids, service_name, location):
    return [maid for maid in maids if service_name in maid.services_available and maid.location == location]

def get_maid_schedule(schedules, maid_id):
    return [schedule for schedule in schedules if schedule.maid_id == maid_id]
