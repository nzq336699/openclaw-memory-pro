# 快速入门 - 30 分钟上手

> 零基础快速上手 OpenClaw-Memory-Pro！

## 📋 前提条件

- Python 3.9+
- pip 3.9+
- IDE（VSCode/PyCharm）

## 🚀 第一步：安装

```bash
pip install openclaw-memory-pro
```

## 🚀 第二步：初始化

```bash
claw-memory init
```

系统会创建：
- `~/.claw-memory/config` - 配置文件
- `~/.claw-memory/models` - 模型目录
- `~/.claw-memory/caches` - 缓存目录

## 🚀 第三步：创建记忆宫殿

```bash
# 工作记忆
claw-memory create --wing "work" --room "main" --drawer "notes"

# 学习记忆
claw-memory create --wing "learn" --room "study" --drawer "python"
```

## 🚀 第四步：添加记忆

```bash
# 方式 1：命令行
claw-memory add "work:notes" "今天学习了 AI 开发，很有收获！"

# 方式 2：Python 代码
from claw_memory import MemoryDB

db = MemoryDB.from_home_dir()
db.add("work:notes", "学习进度记录")
```

## 🚀 第五步：检索记忆

```bash
# 文本检索
claw-memory recall "今天学习"

# 智能检索
claw-memory recall "AI 开发"
```

---

## 🎯 完成！

恭喜！你已经完成了 OpenClaw-Memory-Pro 的基础安装和配置！

**下一步**: 查看 [记忆抽屉使用](memory-drawer.md)
