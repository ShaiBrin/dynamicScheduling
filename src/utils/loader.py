import pandas as pd
from src.models.maid import Maid
from src.models.service import Service
from src.models.schedule import Schedule

def load_maids(csv_path):
    df = pd.read_csv(csv_path)
    return [
        Maid(row["maid_id"], row["maid_name"], row["services"], row["locations"],
             row["rating"], row["phone"], row["email"])
        for _, row in df.iterrows()
    ]

def load_services(csv_path):
    df = pd.read_csv(csv_path)
    return [
        Service(row["service_id"], row["service_name"], row["description"])
        for _, row in df.iterrows()
    ]

def load_schedules(csv_path):
    df = pd.read_csv(csv_path)
    return [
        Schedule(row["maid_id"], row["date"], row["start_time"], row["end_time"])
        for _, row in df.iterrows()
    ]