# Minecraft Bedrock 主基地查找器

从 `.mcworld` 存档中扫描玩家长期活动留下的方块组合，并给出可能的主基地坐标。程序只读取存档，不会修改原文件。

## 运行

需要 Python 3.11+、Amulet Core 和 NumPy。先在所使用的 Python 环境中安装依赖：

```bash
cd /Users/dirlt/Downloads
python3 -m pip install amulet-core==1.9.42 numpy
python3 mc_base_finder.py your-world.mcworld
```

### 网页界面

```bash
cd /Users/dirlt/Downloads
python3 mc_base_finder.py --serve
```

浏览器会自动打开 `http://127.0.0.1:8765/`。在页面中选择 `.mcworld`、调整最低分数和聚类间距，然后查看候选基地热力图。文件只在本机临时处理，不上传互联网。

如果不希望自动打开浏览器：

```bash
python3 mc_base_finder.py --serve --no-browser
```

如果依赖已经安装在 `/opt/miniconda3/bin/python3` 中，也可以让 uv 使用这个 Python。脚本不再包含 PEP 723 元数据，uv 不会根据脚本重新安装依赖：

```bash
uv run --python /opt/miniconda3/bin/python3 mc_base_finder.py your-world.mcworld
```

常用参数：

```bash
# 显示前 30 个候选
python3 mc_base_finder.py your-world.mcworld --top 30

# 没找到时降低过滤门槛
python3 mc_base_finder.py your-world.mcworld --min-chunk-score 8

# 输出 JSON，后续可供网页读取
python3 mc_base_finder.py your-world.mcworld --json > candidates.json
```

默认只扫描主世界。程序根据箱子、床、熔炉、工作台、附魔台、酿造台、漏斗、红石、传送门、照明等方块的数量和组合评分，然后合并相邻候选区块。

## 局限

- 自然村庄、林地府邸、矿井等结构可能成为误报；应结合证据列表和游戏记忆判断。
- 被彻底拆除或位于从未保存成功的区块中的基地无法找到。
- 当前版本先定位候选区域，不分析箱内物品、玩家路径或区块最后更新时间。
- 不同 Bedrock 版本的存档格式可能存在兼容性差异；若有区块解析失败，程序会跳过并报告数量。
