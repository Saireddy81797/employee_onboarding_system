import pandas as pd

def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["EmployeeID", "Name", "Department", "Role", "Email", "JoinDate"])

def save_data(df, file_path):
    df.to_csv(file_path, index=False)
