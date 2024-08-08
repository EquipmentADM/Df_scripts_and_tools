import pandas as pd

def read_csv_get_nth_row(file_path, n):
    """
    读取CSV文件并获取第n行作为行索引
    """
    try:
        df = pd.read_csv(file_path)
        nth_row = df.iloc[n]
        return df, nth_row
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        raise

def read_xls_get_nth_row(file_path, n):
    """
    读取XLS文件并获取第n行作为行索引
    """
    try:
        df = pd.read_excel(file_path, engine='xlrd')
        nth_row = df.iloc[n]
        return df, nth_row
    except Exception as e:
        print(f"Error reading XLS file: {e}")
        raise

def read_xlsx_get_nth_row(file_path, n):
    """
    读取XLSX文件并获取第n行作为行索引
    """
    try:
        df = pd.read_excel(file_path)
        nth_row = df.iloc[n]
        return df, nth_row
    except Exception as e:
        print(f"Error reading XLSX file: {e}")
        raise


def iterate_df_and_modify(df, check_col_index, condition, modify_cols, modify_values):
    """
    遍历DataFrame的行，当该行的某列满足条件时变更其他几列的值

    参数:
    df (pd.DataFrame): 要遍历的DataFrame。
    check_col_index (int): 要检查条件的列的索引。
    condition (function): 一个函数，接受一个值并返回一个布尔值。
    modify_cols (list): 要修改的列索引列表。
    modify_values (list): 要在modify_cols中设置的值的列表。
    """
    try:
        for index, row in df.iterrows():
            # 检查指定列的值是否满足条件
            if condition(row.iloc[check_col_index]):
                # 修改指定列的值
                for col_index, value in zip(modify_cols, modify_values):
                    df.iat[index, col_index] = value
    except Exception as e:
        print(f"处理DataFrame时出错: {e}")
        raise