"""
工具函数模块
包含通用的数据处理和辅助函数
"""

import pandas as pd
import numpy as np
from typing import Optional, Tuple


def load_data(file_path: str) -> pd.DataFrame:
    """
    加载 CSV 数据
    
    Args:
        file_path: CSV 文件路径
    
    Returns:
        加载后的 DataFrame
    """
    df = pd.read_csv(file_path, encoding='utf-8')
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    数据清洗
    
    Args:
        df: 原始 DataFrame
    
    Returns:
        清洗后的 DataFrame
    """
    df_clean = df.copy()
    
    # 删除重复值
    df_clean = df_clean.drop_duplicates()
    
    # 处理缺失值
    for col in df_clean.columns:
        try:
            # 尝试转换为数值类型
            df_clean[col] = pd.to_numeric(df_clean[col], errors='ignore')
            
            # 如果是数值类型，用均值填充
            if pd.api.types.is_numeric_dtype(df_clean[col]):
                df_clean[col] = df_clean[col].fillna(df_clean[col].mean())
            else:
                # 否则用'未知'填充
                df_clean[col] = df_clean[col].fillna('未知')
        except Exception as e:
            df_clean[col] = df_clean[col].fillna('未知')
    
    return df_clean


def filter_data(
    df: pd.DataFrame,
    column: str,
    min_value: Optional[float] = None,
    max_value: Optional[float] = None,
    categories: Optional[list] = None
) -> pd.DataFrame:
    """
    数据筛选
    
    Args:
        df: 原始 DataFrame
        column: 筛选列名
        min_value: 数值型数据最小值
        max_value: 数值型数据最大值
        categories: 类别型数据筛选列表
    
    Returns:
        筛选后的 DataFrame
    """
    df_filtered = df.copy()
    
    if column in df_filtered.columns:
        if pd.api.types.is_numeric_dtype(df_filtered[column]):
            if min_value is not None:
                df_filtered = df_filtered[df_filtered[column] >= min_value]
            if max_value is not None:
                df_filtered = df_filtered[df_filtered[column] <= max_value]
        else:
            if categories is not None and len(categories) > 0:
                df_filtered = df_filtered[df_filtered[column].isin(categories)]
    
    return df_filtered


def get_statistics(df: pd.DataFrame) -> dict:
    """
    获取基本统计信息
    
    Args:
        df: DataFrame
    
    Returns:
        统计信息字典
    """
    stats = {
        "总行数": len(df),
        "总列数": len(df.columns),
        "内存占用": round(df.memory_usage(deep=True).sum() / 1024 / 1024, 2),
        "数值列数": len(df.select_dtypes(include=[np.number]).columns),
        "类别列数": len(df.select_dtypes(include=['object']).columns)
    }
    
    # 数值列统计
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        stats["数值列统计"] = df[numeric_cols].describe().to_dict()
    
    return stats
