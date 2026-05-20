#!/bin/bash
# 使用报告生成器
# 汇总项目进展和病毒传播效果

REPO_DIR="${REPO_DIR:-/Users/jacky/.openclaw/workspace}"
TUTORIALS_DIR="$REPO_DIR/tutorials"
MEMORY_DIR="$REPO_DIR/memory"
REPORTS_DIR="$REPO_DIR/reports"

mkdir -p "$REPORTS_DIR"

generate_report() {
    local report_date=$(date +%Y-%m-%d)
    local report_file="$REPORTS_DIR/report-$report_date.md"
    
    echo "# 📊 项目使用报告" > "$report_file"
    echo "" >> "$report_file"
    echo "## 📅 报告时间" >> "$report_file"
    echo "生成时间：$(date '+%Y-%m-%d %H:%M:%S')" >> "$report_file"
    echo "" >> "$report_file"
    
    echo "## 📈 教程统计" >> "$report_file"
    echo "" >> "$report_file"
    
    # 统计教程数量
    local tutorial_count=$(find "$TUTORIALS_DIR" -name "*.md" -type f | wc -l)
    echo "- **教程总数**: $tutorial_count" >> "$report_file"
    echo "- **教程目录**: $TUTORIALS_DIR" >> "$report_file"
    
    echo "" >> "$report_file"
    echo "## 📚 教程列表" >> "$report_file"
    echo "" >> "$report_file"
    
    # 列出教程
    for tutorial in $(find "$TUTORIALS_DIR" -name "*.md" -type f | sort); do
        local title=$(basename "$tutorial" .md)
        local size=$(stat -f%z "$tutorial" 2>/dev/null || stat -c%s "$tutorial" 2>/dev/null)
        echo "- [$title]($tutorial) ($size 字节)" >> "$report_file"
    done
    
    echo "" >> "$report_file"
    echo "## 💾 文件统计" >> "$report_file"
    echo "" >> "$report_file"
    
    echo "- **教程目录文件大小**: $(du -sh "$TUTORIALS_DIR" 2>/dev/null | cut -f1)" >> "$report_file"
    echo "- **教程数量**: $tutorial_count" >> "$report_file"
    
    echo "" >> "$report_file"
    echo "## 📝 内存记录" >> "$report_file"
    echo "" >> "$report_file"
    
    # 获取最新记忆
    if [ -f "$MEMORY_DIR/$report_date.md" ]; then
        echo "```markdown" >> "$report_file"
        cat "$MEMORY_DIR/$report_date.md" >> "$report_file"
        echo "```" >> "$report_file"
    else
        echo "暂无记忆记录" >> "$report_file"
    fi
    
    echo "" >> "$report_file"
    echo "---" >> "$report_file"
    echo "" >> "$report_file"
    echo "**报告生成于**: $(date)" >> "$report_file"
    
    echo "✅ 报告已生成：$report_file"
    cat "$report_file"
}

# 执行报告生成
generate_report
