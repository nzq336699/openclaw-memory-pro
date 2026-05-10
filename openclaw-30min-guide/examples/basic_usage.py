"""
基础使用示例 - OpenClaw-Memory-Pro
"""

from claw_memory import MemoryDB

def basic_usage():
    """基础使用示例"""
    
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

if __name__ == "__main__":
    basic_usage()
