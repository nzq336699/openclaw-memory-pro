# 快速入门 - 5 分钟上手

> 零基础快速上手 OpenClaw-Memory-Pro！

本指南将帮助您：
- ✅ 30 分钟完成安装配置
- ✅ 掌握核心功能使用
- ✅ 快速创建记忆抽屉
- ✅ 检索和整理记忆

## 🚀 快速开始

### 步骤 1：安装

```bash
pip install openclaw-memory-pro
```

### 步骤 2：初始化

```bash
claw-memory init
```

系统会创建：
- `~/.claw-memory/config` - 配置文件
- `~/.claw-memory/models` - 模型目录
- `~/.claw-memory/caches` - 缓存目录

### 步骤 3：创建记忆宫殿

```bash
# 工作记忆
claw-memory create --wing "work" --room "main" --drawer "notes"

# 学习记忆
claw-memory create --wing "learn" --room "study" --drawer "python"
```

### 步骤 4：添加记忆

```bash
# 方式 1：命令行
claw-memory add "work:notes" "今天学习了 AI 开发，很有收获！"

# 方式 2：Python 代码
from claw_memory import MemoryDB

db = MemoryDB.from_home_dir()
db.add("work:notes", "学习进度记录")
```

### 步骤 5：检索记忆

```bash
# 文本检索
claw-memory recall "今天学习"

# 智能检索
claw-memory recall "AI 开发"
```

---

## 🎯 核心命令参考

```bash
# 查看所有记忆宫殿
claw-memory list

# 查看记忆列表
claw-memory ls work:notes

# 删除记忆
claw-memory delete work:notes:meeting2024

# 导出记忆
claw-memory export work:notes

# 同步记忆
claw-memory sync
```

## 🐍 Python API 快速示例

```python
from claw_memory import MemoryDB

# 初始化
db = MemoryDB.from_home_dir()

# 创建记忆
db.add("work:notes", "今天学习了 OpenClaw-Memory-Pro")
db.add("work:memos", "待办事项列表")

# 检索记忆
results = db.recall("会议", limit=2)
print(results)

# 删除记忆
db.delete("work:notes:meeting2024")
```

---

## ❓ 常见问题

### Q1: 安装报错？
**A**: 确保安装了 Python 3.9+ 和 pip

### Q2: 中文报错？
**A**: 设置 `LANG=zh_CN.UTF-8`

### Q3: 如何卸载？
**A**: `pip uninstall openclaw-memory-pro`

---

**下一步**: 查看 [记忆抽屉使用](memory-drawer.md)
