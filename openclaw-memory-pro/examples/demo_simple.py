"""
🔥 OpenClaw-Memory-Pro 演示代码
简单易懂，5 分钟上手！
"""

from claw_memory import MemoryDB

def demo_simple():
    """简单演示：添加和检索记忆"""
    
    print("=" * 50)
    print("🦞 OpenClaw-Memory-Pro - 简单演示")
    print("=" * 50)
    
    # 初始化
    db = MemoryDB.from_home_dir()
    
    # 添加记忆
    print("\n📝 添加记忆...")
    db.add("work:notes", "今天学习了 OpenClaw-Memory-Pro!")
    db.add("work:notes", "记忆宫殿真的很好用！")
    db.add("learn:python", "Python 学习笔记：装饰器")
    db.add("learn:python", "Python 学习笔记：类与对象")
    
    print("✅ 已添加 4 条记忆")
    
    # 检索记忆
    print("\n🔍 检索包含'Python'的记忆...")
    python_notes = db.recall("Python", limit=5)
    for note in python_notes:
        print(f"  - {note['path']}: {note['content'][:50]}...")
    
    # 查看所有记忆
    print("\n📂 查看所有记忆...")
    all_notes = db.list()
    for note in all_notes[:5]:  # 只显示前 5 条
        print(f"  - {note['path']} (大小：{note['size']} 字节)")
    
    print("\n" + "=" * 50)
    print("演示完成！快去试试自己的记忆宫殿吧！🚀")
    print("=" * 50)

def demo_advanced():
    """高级演示：批量操作和分类管理"""
    
    print("=" * 50)
    print("🦞 OpenClaw-Memory-Pro - 高级演示")
    print("=" * 50)
    
    # 初始化
    db = MemoryDB.from_home_dir()
    
    # 创建多个记忆抽屉
    print("\n🗂️ 创建记忆抽屉...")
    
    # 工作记忆
    work_notes = db.create(wing="work", room="main", drawer="notes")
    work_meetings = db.create(wing="work", room="main", drawer="meetings")
    work_projects = db.create(wing="work", room="projects", drawer="docs")
    
    # 学习记忆
    learn_python = db.create(wing="learn", room="python", drawer="notes")
    learn_github = db.create(wing="learn", room="github", drawer="tutorials")
    learn_ai = db.create(wing="learn", room="ai", drawer="research")
    
    print(f"✅ 已创建 {len([work_notes, work_meetings, work_projects, learn_python, learn_github, learn_ai])} 个记忆抽屉")
    
    # 批量添加记忆
    print("\n📝 批量添加记忆...")
    
    work_notes_content = [
        "周一：项目需求讨论",
        "周二：技术方案评审",
        "周三：代码审查",
        "周四：bug 修复",
        "周五：总结复盘"
    ]
    
    for i, content in enumerate(work_notes_content):
        db.add(work_notes, f"第{i+1}天：{content}")
    
    print(f"✅ 已添加到工作笔记：{len(work_notes_content)} 条")
    
    # 学习 Python 笔记
    python_notes = [
        "Python 基础语法",
        "函数定义与调用",
        "类和对象",
        "装饰器",
        "异常处理"
    ]
    
    for i, note in enumerate(python_notes):
        db.add(learn_python, f"第{i+1}章：{note}")
    
    print(f"✅ 已添加 Python 笔记：{len(python_notes)} 条")
    
    # 检索记忆
    print("\n🔍 检索工作笔记...")
    work_results = db.recall("周一", limit=3)
    for note in work_results:
        print(f"  - {note['path']}: {note['content'][:30]}...")
    
    print("\n🔍 检索 Python 笔记...")
    python_results = db.recall("基础语法", limit=2)
    for note in python_results:
        print(f"  - {note['path']}: {note['content'][:30]}...")
    
    # 导出记忆
    print("\n💾 导出记忆数据...")
    db.export("memory-export.json")
    print("✅ 已导出到 memory-export.json")
    
    print("\n" + "=" * 50)
    print("高级演示完成！去探索更多功能吧！🚀")
    print("=" * 50)

if __name__ == "__main__":
    print("\n" + "🦞" * 20)
    print("选择演示模式:")
    print("1. simple - 简单演示")
    print("2. advanced - 高级演示")
    print("3. both - 两个都运行")
    print("\n输入 1, 2, 3 或 both:")
    
    choice = input(">>> ").strip()
    
    if choice == "1":
        demo_simple()
    elif choice == "2":
        demo_advanced()
    elif choice == "3":
        print("\n📝 运行简单演示...")
        demo_simple()
        print("\n📝 运行高级演示...")
        demo_advanced()
    else:
        print("默认运行两个演示...")
        demo_simple()
        demo_advanced()
