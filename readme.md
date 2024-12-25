# 高性能资源使用情况雷达图绘制

## 简介

本项目是一个基于Python的雷达图绘制工具，用于展示资源使用情况。它使用`matplotlib`库来绘制雷达图，并提供了多种配置选项，包括颜色、标签、数据点等。用户可以根据自己的需求，自定义雷达图的样式和内容。
有两个版本：
1. hpc_resource_radar.py：将所有指标统一缩放到同一尺度，在同一坐标系下使用不同比例尺进行展示，方便不同指标之间进行比较。
2. hpc_resource_radar_split.py：将雷达图由内到外分为若干层，每层展示一个指标，方便单个指标的分析。

## 使用方法

1. 安装依赖库

   numpy
   matplotlib

2. 运行脚本

   在自己的Python脚本中导入函数：

   ```python
   from hpc_resource_radar import hpc_resource_radar
   ```

   然后调用函数：

   ```python
   hpc_resource_radar(cpu,ram,pfs_recv,pfs_send,power)
   ```
   其中，cpu、ram、pfs_recv、pfs_send、power分别为CPU使用率、内存使用量（单位GB）、文件系统接收带宽（IO读带宽，单位GB）、文件系统发送带宽（IO写带宽，单位GB）、功耗（单位W）。
   读取监控文件，将每一帧的上述指标分别存放到对应名称的列表中，然后调用上述函数绘制雷达图。