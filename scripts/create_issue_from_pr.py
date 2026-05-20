#!/usr/bin/env python3
"""
OpenClaw-Memory-Pro Issue→教程自动化脚本
将热门 Issue 自动转换为教程
"""

import subprocess
import re
from datetime import datetime

def detect_tutorial_request(title, body):
    """检测 Issue 是否包含教程需求"""
    tutorial_keywords = [
        r'tutorial', r'guide', r'how to', r'使用', r'教程', r'指南',
        r'建议', r'优化', r'改进', r'功能', r'feature'
    ]
    
    content = (title + body).lower()
    for keyword in tutorial_keywords:
        if re.search(keyword, content):
            return True
    return False

def convert_issue_to_tutorial(issue_title, issue_body, issue_number):
    """将 Issue 转换为教程"""
    tutorial_content = f"""# 📚 教程：{issue_title}\n\n## 🎯 来源\n本教程基于 [GitHub Issue #{issue_number}] 创建\n\n## 📝 原始问题\n{issue_body[:500]}\n\n## 💡 解决方案\n[待填写]\n\n## 🚀 实践步骤\n[待填写]\n\n## 📤 分享报告\n生成使用报告并分享给社区：\n```bash\npython scripts/generate_usage_report.py --tutorial-{issue_number}\n```\n\n---\n**喜欢这个教程？**\n- ⭐ Star 项目支持开发\n- 🐙 Fork 并提出 PR 改进\n- 💬 在 Issues 中提出问题\n"""
    
    return tutorial_content

def main():
    print("🦞 OpenClaw-Memory-Pro Issue→教程转换器启动！")
    
    # 获取最新 Issues
    try:
        result = subprocess.run(
            ['curl', '-s', 'https://api.github.com/repos/nzq336699/openclaw-memory-pro/issues?state=open&sort=comments&direction=desc&per_page=10'],
            capture_output=True, text=True
        )
        issues = result.stdout
    except Exception as e:
        print(f"获取 Issues 失败：{e}")
        return
    
    # 处理每个 Issue
    for line in issues.split('\n'):
        if line.startswith('{'):
            try:
                import json
                issue = json.loads(line)
                title = issue.get('title', '')
                body = issue.get('body', '')
                number = issue.get('number', '')
                
                if detect_tutorial_request(title, body):
                    print(f"📝 检测到教程需求 Issue #{number}: {title}")
                    tutorial = convert_issue_to_tutorial(title, body, number)
                    
                    # 保存到 tutorials 目录
                    save_path = f"tutorials/{number}-Issue-{number}.md"
                    with open(save_path, 'w', encoding='utf-8') as f:
                        f.write(tutorial)
                    print(f"   → 已生成教程：{save_path}")
            
            except Exception as e:
                pass
    
    print("✅ Issue→教程转换完成！")

if __name__ == "__main__":
    main()
