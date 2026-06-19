"""
配置文件
包含页面设置、主题颜色等配置
"""

import os

current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 页面配置
PAGE_CONFIG = {
    "page_title": "数据看板",
    "page_icon": "📊",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# 主题颜色
COLORS = {
    "primary": "#2563eb",
    "secondary": "#7c3aed",
    "success": "#10b981",
    "warning": "#f59e0b",
    "danger": "#ef4444",
    "chart_colors": [
        "#2563eb",
        "#7c3aed",
        "#10b981",
        "#f59e0b",
        "#ef4444",
        "#06b6d4",
        "#84cc16",
        "#f97316"
    ]
}

# 数据路径
DATA_PATH = os.path.join(current_dir, "data", "sample.csv")

# 缓存配置
CACHE_CONFIG = {
    "ttl": 3600,
    "max_entries": 5
}
