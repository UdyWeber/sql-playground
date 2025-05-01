from datetime import datetime


def info(msg: str):
    print(f"[TIME={datetime.now()}][INFO]: {msg:<12}")
