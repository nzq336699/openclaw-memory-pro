# 🦞 OpenClaw-Memory-Pro

基于记忆宫殿的 AI 记忆增强系统 - 开源 + 爱发电双轨制

[![PyPI](https://img.shields.io/pypi/v/openclaw-memory-pro)](https://pypi.org/project/openclaw-memory-pro/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/nzq336699/openclaw-memory-pro?style=social)](https://github.com/nzq336699/openclaw-memory-pro)
[![爱发电](https://img.shields.io/badge/爱发电-赞助-orange)](https://afdian.net/a/openclaw336699)

## ⚡️ 核心特性

- ✨ **永久记忆** - AI 不再遗忘重要信息
- 🏰 **记忆宫殿架构** - 高效的记忆组织与检索
- ⚡️ **毫秒级检索** - 超快的记忆查询速度
- 🔒 **本地优先** - 数据存储在本地，安全可靠
- 💎 **开源免费** - 欢迎 Star 支持！
- 🎯 **结构化记忆** - 支持多维度记忆分类

## 🎯 应用场景

### 个人 AI 助手
- 记住你的偏好设置
- 跟踪你的学习进度
- 管理你的项目文档
- 记录你的日常反思
- 保存重要的对话内容

### 团队协作
- 团队知识库
- 会议纪要管理
- 项目进度追踪
- 成员能力档案

### 企业级应用
- 客服对话记忆
- 销售线索管理
- 客户偏好记录
- 产品培训材料

## 🚀 快速开始

### 安装

```bash
# 使用 pip
pip install openclaw-memory-pro

# 或使用 requirements.txt
pip install -r requirements.txt
```

### 初始化

```bash
# 初始化记忆数据库
python -m claw_memory.init

# 或从 home 目录初始化
from claw_memory import MemoryDB
db = MemoryDB.from_home_dir()
```

### 基本使用

```python
from claw_memory import MemoryDB

# 1. 初始化记忆数据库
db = MemoryDB.from_home_dir()

# 2. 创建记忆抽屉（Memory Palace）
wing = "work"      # 记忆宫殿的翼
room = "main"      # 记忆宫殿的房间
drawer = "notes"   # 抽屉名称

memory_drawer = db.create(wing=wing, room=room, drawer=drawer)

# 3. 添加记忆
db.add("work:main:notes", "今天学会了 Python 的列表推导式", 
       tags=["programming", "python", "learning"],
       importance="high")

# 4. 检索记忆
results = db.recall("Python 技巧", limit=10)
for item in results:
    print(f"记忆：{item.content}")

# 5. 删除记忆
db.delete("work:main:notes:20241025")
```

## 📚 记忆宫殿架构

### 概念理解

```
┌─────────────────────────────────────────┐
│           记忆宫殿 (Memory Palace)       │
│                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
│  │  Wing 1 │  │  Wing 2 │  │  Wing 3 │ │
│  │ (工作)  │  │ (个人)  │  │ (学习)  │ │
│  └────┬────┘  └────┬────┘  └────┬────┘ │
│       │            │              │    │
│  ┌────┴────┐  ┌────┴────┐  ┌────┴────┘ │
│  │  Room 1 │  │  Room 2 │  │  Room 3   │ │
│  │ (文档)  │  │ (笔记)  │  │ (代码)   │ │
│  └────┬────┘  └────┬────┘  └───────────┘ │
│       │            │                     │
│  ┌────┴────┐  ┌────┴────┐                │
│  │ Drawer 1│  │ Drawer 2│                │
│  │ (重要)  │  │ (一般)  │                │
│  └─────────┘  └─────────┘                │
│                                         │
│  记忆抽屉支持：                          │
│  - 分类标签 (tags)                      │
│  - 优先级标记 (importance)              │
│  - 时间戳 (timestamp)                   │
│  - 来源追踪 (source)                    │
│  - 置信度 (confidence)                  │
└─────────────────────────────────────────┘
```

### API 参考

#### MemoryDB 类

```python
from claw_memory import MemoryDB

# 从主目录初始化
db = MemoryDB.from_home_dir()

# 从自定义路径初始化
db = MemoryDB(path="/path/to/memory")
```

#### create() - 创建记忆抽屉

```python
drawer = db.create(
    wing="work",      # 记忆宫殿的翼
    room="main",      # 记忆宫殿的房间
    drawer="notes",   # 抽屉名称
    capacity=1000     # 容量（可选）
)
```

#### add() - 添加记忆

```python
db.add(
    location="work:main:notes",  # 记忆位置
    content="记忆内容",           # 记忆内容
    tags=["tag1", "tag2"],       # 标签
    importance="high",           # 优先级：high/medium/low
    source="user_input",         # 来源
    confidence=0.95,             # 置信度
    metadata={}                  # 额外元数据（可选）
)
```

#### recall() - 检索记忆

```python
# 按关键词检索
results = db.recall("Python", limit=10)

# 按位置检索
results = db.recall(location="work:main:notes", limit=20)

# 按标签检索
results = db.recall(tags=["python"], limit=10)
```

#### delete() - 删除记忆

```python
db.delete(location="work:main:notes:20241025")
```

#### export() - 导出记忆

```python
# 导出为 JSON
json_data = db.export(format="json")

# 导出为 Markdown
md_data = db.export(format="markdown")
```

#### get_statistics() - 获取统计信息

```python
stats = db.get_statistics()
print(f"总记忆数：{stats.total}")
print(f"今日新增：{stats.today}")
```

## 📊 使用示例

### 示例 1: 学习记录

```python
from claw_memory import MemoryDB

db = MemoryDB.from_home_dir()

# 创建学习记录抽屉
learning = db.create(wing="learning", room="python", drawer="basics")

# 添加学习进度
db.add(
    "learning:python:basics",
    "今天完成了 Python 基础语法学习",
    tags=["learning", "python", "grammar"],
    importance="high"
)

# 定期回顾
progress = db.recall("学习进度")
```

### 示例 2: 文档管理

```python
# 创建文档抽屉
docs = db.create(wing="work", room="docs", drawer="technical")

# 添加技术文档
db.add(
    "work:docs:technical",
    "OpenClaw 架构设计文档",
    tags=["documentation", "architecture", "openclaw"],
    importance="high",
    metadata={"author": "Jacky", "version": "0.1.0"}
)
```

### 示例 3: 对话记忆

```python
# 创建对话记忆抽屉
conversations = db.create(wing="personal", room="chat", drawer="recent")

# 添加重要对话
db.add(
    "personal:chat:recent",
    "与用户的商业计划讨论",
    tags=["business", "planning"],
    importance="high",
    source="conversation"
)
```

## 🎨 高级功能

### 批量操作

```python
# 批量添加记忆
locations = [
    "work:docs:api",
    "work:docs:workflow"
]
contents = [
    "OpenClaw Memory API 文档",
    "工作流定义 API 文档"
]

for loc, content in zip(locations, contents):
    db.add(
        location=loc,
        content=content,
        tags=["api", "documentation"],
        importance="medium"
    )
```

### 记忆检索优化

```python
# 使用模糊匹配
results = db.recall("记忆", fuzzy=True, limit=10)

# 按重要性排序
results = db.recall(sort="importance", order="desc")

# 按时间排序
results = db.recall(sort="timestamp", order="desc")
```

### 记忆过期处理

```python
# 删除过期记忆（30 天未访问）
old_memories = db.expired(days=30)
for memory in old_memories:
    db.delete(memory.location)
```

## 🔧 配置选项

```python
from claw_memory import MemoryDB

# 自定义配置
config = {
    "default_capacity": 1000,      # 默认抽屉容量
    "max_tags": 10,                # 最大标签数
    "enable_autotag": True,        # 自动打标签
    "retention_days": 365,         # 记忆保留天数
    "compression": True,           # 启用压缩
}

db = MemoryDB(config=config)
```

## 📦 项目结构

```
openclaw-memory-pro/
├── README.md                    # 项目说明
├── requirements.txt             # Python 依赖
├── src/
│   ├── __init__.py
│   ├── memory_db.py            # 主记忆数据库类
│   ├── memory_palace.py        # 记忆宫殿实现
│   ├── retriever.py            # 检索器
│   ├── tags.py                 # 标签管理
│   └── storage/
│       ├── __init__.py
│       ├── base.py
│       ├── json.py
│       └── sqlite.py
├── tests/
│   ├── test_memory_db.py
│   ├── test_memory_palace.py
│   └── test_retriever.py
└── docs/
    ├── api.md                  # API 文档
    ├── examples.md             # 使用示例
    └── architecture.md         # 架构说明
```

## 🛠️ 开发指南

### 环境设置

```bash
# 克隆仓库
git clone https://github.com/nzq336699/openclaw-memory-pro.git
cd openclaw-memory-pro

# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 查看代码覆盖率
coverage report
```

### 添加新功能

1. 在 `src/` 目录创建新模块
2. 编写单元测试（`tests/`）
3. 更新 API 文档（`docs/api.md`）
4. 提交 PR

### CI/CD

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          pip install -e ".[dev]"
      - name: Run tests
        run: pytest
```

## 🌟 贡献指南

### 代码风格

```python
# 遵循 PEP 8
from typing import Optional, List

class MemoryDB:
    """记忆数据库类"""
    
    def __init__(self, config: Optional[dict] = None):
        """初始化记忆数据库"""
        self.config = config or {}
    
    def add(self, location: str, content: str, ...) -> bool:
        """添加记忆"""
        ...
```

### 提交规范

```
type(scope): subject

例：
feat(memory_db): 添加批量检索功能
fix(retriever): 修复模糊匹配 bug
docs(api): 更新 API 文档
test(storage): 添加 SQLite 测试
```

### 代码审查

- [ ] 代码风格符合 PEP 8
- [ ] 单元测试覆盖率 > 80%
- [ ] 添加了必要的文档
- [ ] 没有破坏现有 API
- [ ] PR 描述清晰

## 🤝 社区

### Star 支持

欢迎 Star 支持！🌟

[![Star History Chart](https://api.star-history.com/svg?repos=nzq336699/openclaw-memory-pro&type=Date)](https://star-history.com/#nzq336699/openclaw-memory-pro&Date)

### Discord

加入我们的 Discord 社区：
- `#openclaw-memory-pro` 频道
- `#general` 通用讨论
- `#help` 技术支持

### 爱发电赞助

支持项目开发：https://afdian.net/a/openclaw336699

赞助档位：
- ❤️ 支持者：5-10 RMB
- 🌟 贡献者：20-50 RMB  
- 🚀 核心贡献者：100+ RMB

## 📧 联系

- 邮箱：eeton750903@outlook.com
- GitHub Issues：[问题反馈](https://github.com/nzq336699/openclaw-memory-pro/issues)
- Discord: `#feedback` 主题

## 📜 许可证

MIT License

## 🦞 关于小龙

> "全力以赴，10000 Stars 必达！"
> - 小龙 🦞

## 📊 项目路线图

### v0.1.0 (已完成)
- [x] 核心 API
- [x] 记忆宫殿架构
- [x] 基础检索功能
- [x] 标签系统

### v0.2.0 (规划中)
- [ ] 模糊检索优化
- [ ] 记忆关联推荐
- [ ] 可视化界面
- [ ] 插件系统

### v0.3.0 (长期目标)
- [ ] 多模型支持
- [ ] 分布式存储
- [ ] 企业级功能
- [ ] 商业化版本
