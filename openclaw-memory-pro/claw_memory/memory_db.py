"""
MemoryDB - 记忆数据库核心类
"""

import os
import json
import hashlib
from pathlib import Path


class MemoryDB:
    """记忆数据库核心类"""
    
    def __init__(self, db_path=None):
        """
        初始化记忆数据库
        
        Args:
            db_path: 数据库路径，默认为 ~/.claw-memory
        """
        if db_path is None:
            db_path = os.path.expanduser("~/.claw-memory")
        
        self.db_path = Path(db_path)
        self.db_path.mkdir(parents=True, exist_ok=True)
        
        # 配置文件
        self.config_file = self.db_path / "config.json"
        self.models_dir = self.db_path / "models"
        self.caches_dir = self.db_path / "caches"
        
        # 加载配置
        self.config = self._load_config()
    
    def _load_config(self):
        """加载配置文件"""
        default_config = {
            "cache": {
                "enabled": False,
                "ttl": 3600
            },
            "indexes": [],
            "archived": []
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        
        return default_config
    
    def create(self, wing, room, drawer, subdrawer=None):
        """
        创建记忆抽屉
        
        Args:
            wing: 内存区域 (work/learn/life)
            room: 房间 (main/study/kitchen)
            drawer: 抽屉 (notes/memos)
            subdrawer: 子抽屉 (可选)
            
        Returns:
            抽屉路径
        """
        path = f"{wing}:{room}:{drawer}"
        
        if subdrawer:
            path += f":{subdrawer}"
        
        return path
    
    def add(self, path, content):
        """
        添加记忆
        
        Args:
            path: 记忆路径 (wing:room:drawer)
            content: 记忆内容
            
        Returns:
            是否成功
        """
        try:
            # 简单实现：存储为文件
            import hashlib
            hash_value = hashlib.md5(content.encode()).hexdigest()
            file_path = self.db_path / f"{path}:{hash_value}.md"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        except Exception as e:
            print(f"添加失败：{e}")
            return False
    
    def delete(self, path):
        """
        删除记忆
        
        Args:
            path: 记忆路径
            
        Returns:
            是否成功
        """
        try:
            # 查找并删除文件
            import glob
            files = glob.glob(f"{self.db_path}/{path}:*.md")
            for file_path in files:
                os.remove(file_path)
            return True
        except Exception as e:
            print(f"删除失败：{e}")
            return False
    
    def recall(self, keyword, limit=10):
        """
        检索记忆
        
        Args:
            keyword: 检索关键词
            limit: 返回数量限制
            
        Returns:
            记忆列表
        """
        try:
            results = []
            
            # 遍历所有记忆文件
            for file_path in self.db_path.glob("*.md"):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # 简单文本匹配
                if keyword in content:
                    results.append({
                        "path": file_path.name,
                        "content": content
                    })
            
            return results[:limit]
        except Exception as e:
            print(f"检索失败：{e}")
            return []
    
    def list(self, prefix=None):
        """
        获取记忆列表
        
        Args:
            prefix: 路径前缀过滤
            
        Returns:
            记忆列表
        """
        try:
            results = []
            
            for file_path in self.db_path.glob("*.md"):
                path = file_path.name
                
                if prefix and not path.startswith(prefix):
                    continue
                
                results.append({
                    "path": path,
                    "size": file_path.stat().st_size
                })
            
            return results
        except Exception as e:
            print(f"列表获取失败：{e}")
            return []
    
    def export(self, output_path):
        """
        导出记忆数据
        
        Args:
            output_path: 输出路径
            
        Returns:
            是否成功
        """
        try:
            import json
            
            data = []
            for file_path in self.db_path.glob("*.md"):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                data.append({
                    "path": file_path.name,
                    "content": content
                })
            
            # 保存为 JSON
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            return True
        except Exception as e:
            print(f"导出失败：{e}")
            return False
    
    def import(self, input_path):
        """
        导入记忆数据
        
        Args:
            input_path: 输入路径
            
        Returns:
            是否成功
        """
        try:
            import json
            
            with open(input_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for item in data:
                self.add(item["path"], item["content"])
            
            return True
        except Exception as e:
            print(f"导入失败：{e}")
            return False
    
    @classmethod
    def from_home_dir(cls):
        """
        从主目录初始化
        
        Returns:
            MemoryDB 实例
        """
        return cls()