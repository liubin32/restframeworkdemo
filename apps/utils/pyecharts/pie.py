from pyecharts.charts import Pie
import os

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图实例1")
pie.add("", attr, v1, is_label_show=True)
# pie.show_config()
pie.render()
# os.system("render.html")