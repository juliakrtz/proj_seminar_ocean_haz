from .logs import die
import requests
import pandas as pd
import geopandas as gpd
import csv


def download_data(url: str, fname: str) -> None:
    try:
        r = requests.get(url, allow_redirects=True)
        with open(fname, "wb") as f:
            f.write(r.content)
    except Exception as e:
        e.die(f"{e}")


def 'read_csv'(
    fname: str,
    sep: str = ",",
) -> pd.DataFrame:
    """Reads a CSV into a Pandas dataframe

    Args:
        fname (str): the name of the CSV file
        indicators (pd.DataFrame): the indicators we want
        sep (str, optional): the character separator. Defaults to ",".

    Returns:
        pd.DataFrame: [description]
    """
    try:
        df = pd.read_csv(fname, encoding= "cp1252", sep=sep)
    except Exception as e:
        die(f"read_csv: {e}")
    return df

def read_shp(
    fname: str
) -> gpd.GeoDataFrame:
    """Reads a SHP into a GeoPandas dataframe

    Args:
        fname (str): the name of the SHP file
        indicators (gpd.GeoDataFrame): the indicators we want
        sep (str, optional): the character separator. Defaults to ",".

    Returns:
        gpd.GeoDataFrame: [description]
    """
    try:
        gdf = gpd.read_file(fname)
    except Exception as e:
        die(f"read_shp: {e}")
    return gdf


def write_csv(
    df: pd.DataFrame,
    fname: str,
    sep: str = ",",
    quotechar: str = '"',
) -> None:
    """ Writes a Pandas dataframe into a CSV

    Args:
        df (pd.DataFrame): the dataframe
        fname (str): the file name
        sep (str, optional): the character delimiter. Defaults to ",".
        quotechar (str, optional): the character for quotes. Defaults to '"'.
    """
    try:
        df.to_csv(
            fname,
            sep=sep,
            quotechar=quotechar,
            header=True,
            index=False,
            index_label=False,
            quoting=csv.QUOTE_NONNUMERIC,
        )
    except Exception as e:
        die(f"write_csv: {e}")
