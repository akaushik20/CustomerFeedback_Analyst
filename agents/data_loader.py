import pandas as pd

class DataLoader:
    """
    A class to load data from various file formats into pandas DataFrames.
    """
    def __init__(self):
        self.data = None

    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load data from a CSV file into a pandas DataFrame.

        Args:
            file_path (str): The path to the CSV file.
TypeError: DataLoader.__init__() missing 1 required positional argument: 'file_path'
        Returns:
            pd.DataFrame: The loaded data as a pandas DataFrame.
        """
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            print(f"Error loading data from {file_path}: {e}")
            return pd.DataFrame()

    def load_json(self, file_path: str) -> pd.DataFrame:
        """
        Load data from a JSON file into a pandas DataFrame.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            pd.DataFrame: The loaded data as a pandas DataFrame.
        """
        try:
            data = pd.read_json(file_path, lines=True)
            return data
        except Exception as e:
            print(f"Error loading data from {file_path}: {e}")
            return pd.DataFrame()