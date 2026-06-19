"""
Streamlit 数据看板主程序
包含数据加载、处理、可视化和交互功能
"""

import streamlit as st
import pandas as pd
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from config.settings import PAGE_CONFIG, DATA_PATH
from utils.common import load_data, clean_data, filter_data, get_statistics
from src.analysis import create_bar_chart, create_line_chart, create_pie_chart, aggregate_data


def main():
    # 页面配置
    st.set_page_config(**PAGE_CONFIG)
    
    # 加载自定义样式
    css_path = os.path.join(current_dir, "assets", "style.css")
    if os.path.exists(css_path):
        with open(css_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    # 标题
    st.title("📊 数据看板")
    st.markdown("---")
    
    # 侧边栏
    st.sidebar.header("🔧 筛选控制")
    
    # 加载数据
    @st.cache_data(ttl=3600)
    def get_data():
        df = load_data(DATA_PATH)
        df_clean = clean_data(df)
        return df_clean
    
    try:
        df = get_data()
        
        # 侧边栏筛选
        # 产品筛选
        products = sorted(df["产品"].unique())
        selected_products = st.sidebar.multiselect(
            "选择产品",
            options=products,
            default=products
        )
        
        # 类别筛选
        categories = sorted(df["类别"].unique())
        selected_categories = st.sidebar.multiselect(
            "选择类别",
            options=categories,
            default=categories
        )
        
        # 地区筛选
        regions = sorted(df["地区"].unique())
        selected_regions = st.sidebar.multiselect(
            "选择地区",
            options=regions,
            default=regions
        )
        
        # 销量范围筛选
        min_sales = float(df["销量"].min())
        max_sales = float(df["销量"].max())
        sales_range = st.sidebar.slider(
            "销量范围",
            min_value=min_sales,
            max_value=max_sales,
            value=(min_sales, max_sales)
        )
        
        # 应用筛选
        df_filtered = df[
            (df["产品"].isin(selected_products)) &
            (df["类别"].isin(selected_categories)) &
            (df["地区"].isin(selected_regions)) &
            (df["销量"] >= sales_range[0]) &
            (df["销量"] <= sales_range[1])
        ]
        
        # 主内容区域
        if len(df_filtered) == 0:
            st.warning("⚠️ 没有符合条件的数据，请调整筛选条件！")
            return
        
        # 1. 数据概览
        st.header("📈 数据概览")
        
        # 统计指标
        col1, col2, col3, col4 = st.columns(4)
        stats = get_statistics(df_filtered)
        
        with col1:
            st.metric(
                "总记录数",
                f"{stats['总行数']}"
            )
        
        with col2:
            total_sales = df_filtered["销售额"].sum()
            st.metric(
                "总销售额",
                f"¥{total_sales:,.0f}"
            )
        
        with col3:
            total_profit = df_filtered["利润"].sum()
            st.metric(
                "总利润",
                f"¥{total_profit:,.0f}"
            )
        
        with col4:
            total_quantity = df_filtered["销量"].sum()
            st.metric(
                "总销量",
                f"{total_quantity:,.0f}"
            )
        
        st.markdown("---")
        
        # 数据表格
        with st.expander("📋 查看详细数据"):
            st.dataframe(df_filtered, use_container_width=True)
        
        st.markdown("---")
        
        # 2. 可视化图表
        st.header("📊 数据可视化")
        
        # 产品销量柱状图
        st.subheader("📦 产品销量对比")
        sales_by_product = aggregate_data(df_filtered, "产品", "销量", "sum")
        fig_bar = create_bar_chart(sales_by_product, "产品", "销量", "各产品销量对比")
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # 销售额趋势折线图
        st.subheader("📉 销售额趋势")
        df_filtered_sorted = df_filtered.sort_values("日期")
        fig_line = create_line_chart(
            df_filtered_sorted,
            "日期",
            "销售额",
            "每日销售额趋势",
            "产品"
        )
        st.plotly_chart(fig_line, use_container_width=True)
        
        # 类别占比饼图
        st.subheader("🥧 销售额类别占比")
        sales_by_category = aggregate_data(df_filtered, "类别", "销售额", "sum")
        fig_pie = create_pie_chart(sales_by_category, "类别", "销售额", "各类别销售额占比")
        st.plotly_chart(fig_pie, use_container_width=True)
        
        # 地区销售对比
        st.subheader("🌍 地区销售对比")
        sales_by_region = aggregate_data(df_filtered, "地区", "销售额", "sum")
        fig_region = create_bar_chart(sales_by_region, "地区", "销售额", "各地区销售额对比")
        st.plotly_chart(fig_region, use_container_width=True)
        
    except Exception as e:
        st.error(f"❌ 发生错误: {str(e)}")
        st.info("请确保数据文件存在且格式正确！")


if __name__ == "__main__":
    main()
