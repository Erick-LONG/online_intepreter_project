from django.db import models, IntegrityError # 查询失败时我们需要用到的模块
import subprocess # 用于运行代码
from django.http import Http404 # 当查询操作失败时返回404响应
