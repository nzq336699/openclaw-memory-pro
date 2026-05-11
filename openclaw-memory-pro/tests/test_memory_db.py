"""
单元测试 - OpenClaw-Memory-Pro 🦞
"""

import unittest
from pathlib import Path
from claw_memory import MemoryDB


class TestMemoryDB(unittest.TestCase):
    """记忆数据库测试类"""
    
    def setUp(self):
        """初始化测试环境"""
        self.db = MemoryDB()
    
    def test_add_memory(self):
        """测试添加记忆"""
        result = self.db.add("test:drawer", "测试记忆内容")
        self.assertTrue(result)
    
    def test_recall_memory(self):
        """测试检索记忆"""
        self.db.add("test:drawer", "测试记忆 1")
        self.db.add("test:drawer", "测试记忆 2")
        results = self.db.recall("测试", limit=2)
        self.assertEqual(len(results), 2)
    
    def test_create_drawer(self):
        """测试创建记忆抽屉"""
        path = self.db.create(wing="test", room="room1", drawer="drawer1")
        self.assertTrue(path.endswith("test:room1:drawer1"))
    
    def test_delete_memory(self):
        """测试删除记忆"""
        self.db.add("test:drawer", "要删除的记忆")
        result = self.db.delete("test:drawer:test")
        self.assertTrue(result)
    
    def test_export_memory(self):
        """测试导出记忆"""
        self.db.add("test:drawer", "导出测试")
        import os
        export_file = self.db.export("test_export.json")
        self.assertTrue(os.path.exists(export_file))
    
    def test_list_memory(self):
        """测试列出记忆"""
        self.db.add("test:list", "记忆 A")
        self.db.add("test:list", "记忆 B")
        notes = self.db.list()
        self.assertGreater(len(notes), 0)


if __name__ == '__main__':
    unittest.main()
