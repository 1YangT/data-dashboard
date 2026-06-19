# 数据看板

基于 Streamlit 框架开发的数据可视化看板，支持 CSV 数据加载、清洗、统计和可视化展示。

## 技术栈

- Python 3.10+
- Streamlit 1.28+
- Pandas
- Matplotlib

## 功能特点

- 📊 **数据概览** - 展示数据基本信息
- 📈 **统计指标** - 关键指标统计展示
- 📉 **柱状图** - 产品销量对比
- 📊 **折线图** - 销售额趋势
- 🥧 **饼图** - 类别占比分析
- 🔧 **侧边栏筛选** - 交互式数据筛选
- ⚡ **缓存加速** - 数据加载缓存

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行应用

```bash
streamlit run main.py
```

### 访问地址

- 本地访问：http://localhost:8501

## 项目结构

```
.
├── main.py                   # 主程序文件
├── requirements.txt          # 依赖包列表
├── .gitignore               # Git 忽略文件
├── config/
│   └── settings.py          # 配置文件
├── utils/
│   └── common.py            # 工具函数
├── src/
│   └── analysis.py          # 分析模块
├── data/
│   └── sample.csv           # 示例数据
└── assets/
    └── style.css            # 样式文件
```

## 部署到 Streamlit Community Cloud

1. 登录 [Streamlit Community Cloud](https://share.streamlit.io/)
2. 点击 "New app"
3. 选择 GitHub 仓库：`1YangT/data-dashboard`
4. 分支：`main`
5. 主文件路径：`main.py`
6. 点击 "Deploy"

## 许可证

MIT License
