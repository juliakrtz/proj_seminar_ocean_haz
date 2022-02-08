fname = shark_attacks

def transformation(config: dict) -> None:
    """Runs transformation

    Args:
        config (dict): [description]
    """
    fname = config["fname"]
    df = e.read_csv(f"{DOWNLOAD_DIR}/{fname}")

    