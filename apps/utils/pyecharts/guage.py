from pyecharts.charts import Gauge
import os

gauge = Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 66.66)
# a=input("输入路径：")
# gauge.render(a)
# os.system(a)
gauge.render()
# os.system("render.html")