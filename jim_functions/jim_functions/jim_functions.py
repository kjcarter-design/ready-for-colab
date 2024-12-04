import pandas as pd
import numpy as np

def change_df_column_names(names):
    title=[]
    for name in names: 
        title.append(name.lower())
    return title

def split_columns(data):
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    integer_columns = df.select_dtypes(include=['int']).columns.tolist()
    float_columns = df.select_dtypes(include=['float']).columns.tolist()
    boolean_columns = df.select_dtypes(include=['bool']).columns.tolist()
    object_columns = df.select_dtypes(include=['object']).columns.tolist()
    return numeric_columns, integer_columns, float_columns, boolean_columns, object_columns