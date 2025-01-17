# conf.py
 
# 项目基本信息
project = 'Sphinx 文档项目'
copyright = '2023, 作者名'
author = '作者名'
 
# 版本信息
version = '1.0'
release = '1.0.0'
 
# 扩展配置
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]
 
# 排除构建目录
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
