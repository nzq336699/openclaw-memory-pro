# API 文档

## MemoryDB 核心类

### 初始化

```python
from claw_memory import MemoryDB

# 使用默认路径 ~/.claw-memory
db = MemoryDB.from_home_dir()

# 自定义路径
db = MemoryDB(db_path="/path/to/memory")
```

### 创建记忆抽屉

```python
# 创建记忆抽屉
path = db.create(wing="work", room="main", drawer="notes")
# 返回："work:main:notes"

# 创建子抽屉
path = db.create(wing="work", room="main", drawer="notes", subdrawer="2024")
# 返回："work:main:notes:2024"
```

### 添加记忆

```python
# 添加记忆
success = db.add("work:notes", "今天的笔记内容")
# 返回：True 或 False

# 批量添加
db.add("work:notes", "笔记 1")
db.add("work:notes", "笔记 2")
```

### 检索记忆

```python
# 文本检索
results = db.recall("关键词", limit=10)
# 返回：[(path, content, timestamp), ...]

# 精确检索
results = db.recall("exact:content", limit=5)
```

### 删除记忆

```python
# 删除指定记忆
success = db.delete("work:notes:meeting2024")
# 返回：True 或 False
```

### 导出记忆

```python
# 导出为 JSON
file_path = db.export("memory-export.json")
# 返回：导出文件路径
```

### 列出记忆

```python
# 列出所有记忆
notes = db.list()
# 返回：[(path, size), ...]

# 按抽屉过滤
notes = db.list(wing="work")
```

### 配置管理

```python
# 加载配置
config = db.config

# 保存配置
db.save_config(config)

# 配置示例
config = {
    "cache": {
        "enabled": False,
        "ttl": 3600
    },
    "indexes": [],
    "archived": []
}
```

## 命令行工具

```bash
# 初始化
claw-memory init

# 创建记忆宫殿
claw-memory create --wing "work" --room "main" --drawer "notes"

# 添加记忆
claw-memory add "work:notes" "今天的笔记"

# 检索记忆
claw-memory recall "关键词"

# 列出记忆
claw-memory list

# 删除记忆
claw-memory delete "work:notes:meeting"

# 导出记忆
claw-memory export output.json

# 归档记忆
claw-memory archive "work:notes:old" --to "work:archived:old"

# 同步记忆
claw-memory sync
```

## 示例代码

### 示例 1：添加笔记

```python
from claw_memory import MemoryDB

db = MemoryDB.from_home_dir()

# 添加工作笔记
db.add("work:notes", "今天学习了 OpenClaw-Memory-Pro")

# 添加学习笔记
db.add("learn:python", "Python 装饰器：@装饰器 是一种语法糖")
```

### 示例 2：检索笔记

```python
from claw_memory import MemoryDB

db = MemoryDB.from_home_dir()

# 检索包含"Python"的笔记
results = db.recall("Python", limit=5)

for path, content, timestamp in results:
    print(f"{path}: {content}")
```

### 示例 3：项目管理

```python
from claw_memory import MemoryDB

db = MemoryDB.from_home_dir()

# 创建项目抽屉
project_requirements = db.create(
    wing="work",
    room="project-x",
    drawer="requirements"
)

# 添加项目文档
db.add(project_requirements, "项目需求：实现 AI 记忆增强系统")
db.add(project_requirements, "技术栈：OpenAI API + 记忆网络 + FastAPI")

# 检索项目文档
results = db.recall("技术栈", limit=3)
```

## 错误处理

```python
from claw_memory import MemoryDB

db = MemoryDB.from_home_dir()

try:
    db.add("work:notes", "笔记内容")
except Exception as e:
    print(f"添加失败：{e}")
```

## 性能提示

- 批量添加比单次添加更快
- 使用索引加速检索
- 定期归档旧记忆
- 合理设置缓存 TTL

---

**最后更新**: 2026-05-11
