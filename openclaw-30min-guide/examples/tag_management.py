"""
标签管理示例 - OpenClaw-Memory-Pro
"""

from claw_memory import MemoryDB

def tag_management():
    """标签管理示例"""
    
    # 初始化
    db = MemoryDB.from_home_dir()
    
    # 创建多个记忆抽屉
    work_notes = db.create(wing="work", room="main", drawer="notes")
    python_notes = db.create(wing="learn", room="python", drawer="notes")
    
    # 添加标签
    db.add(work_notes, "重要会议记录")
    db.add(work_notes, "日常笔记")
    
    # 检索特定标签
    results = db.recall("重要", limit=5)
    print(results)

if __name__ == "__main__":
    tag_management()
