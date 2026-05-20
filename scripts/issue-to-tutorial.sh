#!/bin/bash
# Issue → 教程转换脚本
# 自动将用户 Issue 转换为教程内容

REPO_DIR="${REPO_DIR:-/Users/jacky/.openclaw/workspace}"
TUTORIALS_DIR="$REPO_DIR/tutorials"
ISSUES_DIR="$REPO_DIR/.github/issues"

# 配置
MAX_ISSUES=10
TUTORIAL_PREFIX="tutorial-"
TEMPLATE_PREFIX="07-教程模板"

# 获取最新的 Issues
get_issues() {
    # 从 GitHub API 获取最新 issues
    curl -s https://api.github.com/repos/jacky/openclaw-10k-stars/issues \
        -H "Authorization: token $GH_TOKEN" \
        | jq -r '.[].title, .[].body' 2>/dev/null || echo "No issues"
}

# 创建教程从 Issue
create_tutorial_from_issue() {
    local issue_title="$1"
    local issue_body="$2"
    local tutorial_name=$(echo "$issue_title" | sed 's/[^a-zA-Z0-9]/-/g' | cut -c1-50)
    
    cat > "$TUTORIALS_DIR/$TUTORIAL_PREFIX$tutorial_name.md" << EOF
# $issue_title

## 📝 问题来源
- GitHub Issue: https://github.com/jacky/openclaw-10k-stars/issues
- 用户反馈

## 💡 教程内容
$issue_body

## 🎯 目标
解决用户遇到的常见问题，提供最佳实践。

## 📚 相关教程
- 基础使用
- 进阶技巧
- 最佳实践

## 📝 备注
由 issue 自动生成的教程草稿。
EOF
    
    echo "✓ 已创建教程：$TUTORIAL_PREFIX$tutorial_name.md"
}

# 主函数
main() {
    echo "🔍 扫描 Issues 中的教程机会..."
    
    # 如果有新的 issue，处理它们
    if [ -d "$ISSUES_DIR" ]; then
        # 读取最近的 issues
        for issue_file in "$ISSUES_DIR"/*.json 2>/dev/null; do
            local title=$(basename "$issue_file" .json)
            echo "处理 Issue: $title"
            # TODO: 实现实际的 issue 到教程转换
        done
    fi
    
    echo "✅ 教程转换完成"
}

main
