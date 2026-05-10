"""
高级功能示例 - OpenClaw-Memory-Pro
"""

from claw_memory import MemoryDB, MemoryError

class MemoryManager:
    def __init__(self):
        self.db = MemoryDB.from_home_dir()
    
    def add_note(self, tag, content):
        """添加笔记"""
        try:
            self.db.add(tag, content)
            return True
        except MemoryError as e:
            print(f"添加失败：{e}")
            return False
    
    def search_tags(self, keyword, limit=10):
        """搜索笔记"""
        return self.db.recall(keyword, limit=limit)
    
    def get_work_notes(self):
        """获取所有工作笔记"""
        return [
            note for note in self.db.list()
            if "work" in note.path
        ]
    
    def delete_all(self, drawer):
        """清空某个抽屉"""
        # 实现逻辑
        pass

# 使用示例
manager = MemoryManager()

# 添加笔记
manager.add_note("work:notes", "今天学习了 OpenClaw")

# 搜索笔记
notes = manager.search_tags("学习")

# 获取工作笔记
work_notes = manager.get_work_notes()
for note in work_notes[:5]:
    print(note)
