# 全国疫情地图可视化开发
import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("D:/编程数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()  # 全部数据
f.close()

data_dict = json.loads(data)   # 将字符串json转化为python字典(基础字典数据)
province_data_list = data_dict["areaTree"][0]["children"]   # 从字典中取出省份的数据
data_list = []    # 绘图需要用的数据列表
for province_data in province_data_list:
    province_name = province_data["name"]    # 省份名称
    province_confirm = province_data["total"]["confirm"]   # 确诊人数
    data_list.append((province_name, province_confirm))  # 以元组的形式插入列表

China_map = Map()  # 创建地图对象
China_map.add("各省份确诊人数", data_list, "china")   # 添加数据
China_map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 0, "max": 99, "lable": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000-4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "lable": "5000-9999人", "color": "#FF6666"},
            {"min": 10000,  "lable": "10000+人", "color": "#CC3333"},
        ]
    )
)

China_map.render("全国疫情地图.html")







