"""
数据分析模块
包含统计分析和可视化函数
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import Optional
from config.settings import COLORS


def create_bar_chart(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: str = "柱状图"
) -> go.Figure:
    """
    创建柱状图
    
    Args:
        df: DataFrame
        x_col: X轴列名
        y_col: Y轴列名
        title: 图表标题
    
    Returns:
        Plotly 图表对象
    """
    fig = px.bar(
        df,
        x=x_col,
        y=y_col,
        title=title,
        color_discrete_sequence=COLORS["chart_colors"],
        template="plotly_white"
    )
    fig.update_layout(
        xaxis_title=x_col,
        yaxis_title=y_col,
        showlegend=False
    )
    return fig


def create_line_chart(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: str = "折线图",
    color_col: Optional[str] = None
) -> go.Figure:
    """
    创建折线图
    
    Args:
        df: DataFrame
        x_col: X轴列名
        y_col: Y轴列名
        title: 图表标题
        color_col: 颜色分组列名
    
    Returns:
        Plotly 图表对象
    """
    fig = px.line(
        df,
        x=x_col,
        y=y_col,
        color=color_col,
        title=title,
        color_discrete_sequence=COLORS["chart_colors"],
        template="plotly_white"
    )
    fig.update_layout(
        xaxis_title=x_col,
        yaxis_title=y_col
    )
    return fig


def create_pie_chart(
    df: pd.DataFrame,
    names_col: str,
    values_col: str,
    title: str = "饼图"
) -> go.Figure:
    """
    创建饼图
    
    Args:
        df: DataFrame
        names_col: 类别列名
        values_col: 数值列名
        title: 图表标题
    
    Returns:
        Plotly 图表对象
    """
    fig = px.pie(
        df,
        names=names_col,
        values=values_col,
        title=title,
        color_discrete_sequence=COLORS["chart_colors"],
        template="plotly_white"
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    return fig


def create_histogram(
    df: pd.DataFrame,
    column: str,
    title: str = "直方图",
    nbins: int = 20
) -> go.Figure:
    """
    创建直方图
    
    Args:
        df: DataFrame
        column: 数据列名
        title: 图表标题
        nbins: 直方图箱数
    
    Returns:
        Plotly 图表对象
    """
    fig = px.histogram(
        df,
        x=column,
        nbins=nbins,
        title=title,
        color_discrete_sequence=COLORS["chart_colors"],
        template="plotly_white"
    )
    fig.update_layout(
        xaxis_title=column,
        yaxis_title="频数",
        showlegend=False
    )
    return fig


def aggregate_data(
    df: pd.DataFrame,
    group_col: str,
    agg_col: str,
    agg_func: str = "sum"
) -> pd.DataFrame:
    """
    数据聚合
    
    Args:
        df: DataFrame
        group_col: 分组列名
        agg_col: 聚合列名
        agg_func: 聚合函数 (sum, mean, count)
    
    Returns:
        聚合后的 DataFrame
    """
    agg_df = df.groupby(group_col).agg({agg_col: agg_func}).reset_index()
    return agg_df
