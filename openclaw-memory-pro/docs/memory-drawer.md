# 记忆抽屉使用指南

## 什么是记忆抽屉？

记忆抽屉是一个独立的记忆存储单元，用于分类管理不同主题的记忆。

## 创建策略示例

### 工作记忆策略

```bash
# 工作笔记
claw-memory create --wing "work" --room "main" --drawer "notes"

# 会议纪要
claw-memory create --wing "work" --room "main" --drawer "meeting"

# 项目文档
claw-memory create --wing "work" --room "projects" --drawer "docs"
```

### 学习记忆策略

```bash
# Python 学习笔记
claw-memory create --wing "learn" --room "python" --drawer "notes"

# 技术文档
claw-memory create --wing "learn" --room "docs" --drawer "python"
```

### 生活记忆策略

```bash
# 购物清单
claw-memory create --wing "life" --room "kitchen" --drawer "shopping"

# 旅行笔记
claw-memory create --wing "life" --room "travel" --drawer "diary"
```

## 记忆组织原则

### 🎯 单一职责原则

每个记忆抽屉只负责一个特定主题：
- ✅ `work:notes` - 工作笔记
- ❌ `work:notes:个人生活` - 混入了生活内容

### 📝 命名规范

```
wing:room:drawer:subdrawer

示例：
work:main:notes:20241001  # 2024 年 10 月 1 日的工作笔记
learn:python:pytorch:tutorial1  # PyTorch 教程 1
```

### 🏷️ 标签分类

```bash
# 添加标签
claw-memory tag "work:notes" "urgent" "meeting"

# 检索标签
claw-memory recall --tag "urgent"
```

## 最佳实践

### 1. 定期归档

```bash
# 将旧记忆归档
claw-memory archive "work:notes:2023" --to "work:archived:2023"
```

### 2. 批量创建

```bash
# 创建记忆抽屉模板
for topic in python go rust; do
    claw-memory create \
        --wing "learn" \
        --room "programming" \
        --drawer "$topic"
done
```

### 3. 设置索引

```bash
# 为重要记忆设置索引
claw-memory index "work:notes:important"
```

---

## 🎯 实际场景演示

### 场景 1: 项目管理

```bash
# 创建项目抽屉
claw-memory create \
    --wing "work" \
    --room "project-x" \
    --drawer "requirements"

# 添加项目文档
claw-memory add "work:project-x:requirements" \
    "项目需求：实现 AI 记忆增强系统"
claw-memory add "work:project-x:requirements" \
    "技术栈：OpenAI API + 记忆网络 + FastAPI"
```

### 场景 2: 学习笔记

```bash
# 创建技术笔记抽屉
claw-memory create \
    --wing "learn" \
    --room "ai" \
    --drawer "transformers"

# 添加学习内容
claw-memory add "learn:ai:transformers" \
    "了解 Transformer 架构原理"
```

### 场景 3: 任务追踪

```bash
# 创建任务抽屉
claw-memory create \
    --wing "work" \
    --room "todo" \
    --drawer "priority-high"

# 添加待办事项
claw-memory add "work:todo:priority-high" \
    "完成 OpenClaw-Memory-Pro 发布"
```

---

**下一步**: 查看 [记忆检索优化](memory-recall.md)
