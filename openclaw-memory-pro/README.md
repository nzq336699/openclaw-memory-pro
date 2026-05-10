# OpenClaw-Memory-Pro 🦞

> 记忆宫殿 2.0 - 让 AI 拥有永久记忆的空间

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Latest Version](https://img.shields.io/badge/Version-v0.1.0-blue.svg)](../README.md)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![爱发电赞助](https://img.shields.io/badge/爱发电-支持-red.svg)](https://afdian.net/a/openclaw336699)

## 🌟 主要功能

- ✅ **记忆增强** - 永久记忆空间，再也不怕忘记
- ✅ **记忆检索** - 精准查找，智能搜索
- ✅ **记忆优化** - 自动整理，定期归档
- ✅ **开源免费** - 开源代码，支持爱发电赞助

## 🚀 快速开始

### 步骤 1：安装

```bash
pip install openclaw-memory-pro
```

### 步骤 2：初始化

```bash
claw-memory init
```

### 步骤 3：创建记忆宫殿

```bash
# 工作记忆
claw-memory create --wing "work" --room "main" --drawer "notes"

# 学习记忆
claw-memory create --wing "learn" --room "study" --drawer "python"
```

### 步骤 4：添加记忆

```bash
# 命令行方式
claw-memory add "work:notes" "今天学习了 AI 开发，很有收获！"

# Python 代码方式
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

## 📖 文档

- [快速入门教程](docs/quick-start.md)
- [记忆抽屉使用](docs/memory-drawer.md)
- [记忆检索优化](docs/memory-recall.md)
- [API 接口文档](docs/api.md)

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

## 📦 核心命令参考

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

## 🎯 项目仓库

1. **openclaw-memory-pro** - 记忆增强系统（高优先级）
2. **openclaw-30min-guide** - 入门指南（中优先级）
3. **openclaw** - 主框架（中优先级）
4. **claw-flow** - 工作流（低优先级）
5. **claw-studio** - 工作室（中优先级）
6. **claw-mind** - 记忆系统（低优先级）
7. **claw-academy** - 教程（低优先级）

## 💜 支持项目

- **GitHub Star**: 支持开源发展
- **爱发电赞助**: 支持持续开发
- **企业咨询**: 定制解决方案

## 📞 联系支持

- **GitHub Issues**: https://github.com/nzq336699/openclaw-memory-pro/issues
- **爱发电赞助**: https://afdian.net/a/openclaw336699
- **企业咨询**: contact@openclaw.ai

## 📚 贡献指南

1. Fork 本仓库
2. 创建特性分支
3. 提交 Pull Request
4. 等待维护者审查

## 📜 许可证

本仓库采用 MIT License 开源协议

---

Created by OpenClaw Team 🦞
