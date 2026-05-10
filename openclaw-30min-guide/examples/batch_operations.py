"""
批量操作示例 - OpenClaw-Memory-Pro
"""

from claw_memory import MemoryDB

def batch_operations():
    """批量操作示例"""
    
    # 初始化
    db = MemoryDB.from_home_dir()
    
    # 批量添加记忆
    tags = ["work:notes", "learn:python", "life:diary"]
    for i, tag in enumerate(tags):
        db.add(tag, f"第{i+1}条记忆内容")
    
    # 批量检索
    keywords = ["work", "python", "笔记"]
    for keyword in keywords:
        results = db.recall(keyword, limit=10)
        print(f"关键词：{keyword}, 找到 {len(results)} 条")

if __name__ == "__main__":
    batch_operations()
