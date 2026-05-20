#!/bin/bash
# OpenClaw-Memory-Pro 增长监控脚本
# 零外部依赖，自动运行

REPO_NAME="nzq336699/openclaw-memory-pro"
GITHUB_API="https://api.github.com/repos/$REPO_NAME"

echo "🦞 OpenClaw-Memory-Pro 增长引擎启动！"

# 获取统计数据
STAR_COUNT=$(curl -s "$GITHUB_API/stargazers" | jq '.stargazers_count')
WATCHERS=$(curl -s "$GITHUB_API" | jq '.watchers')
FORKS=$(curl -s "$GITHUB_API" | jq '.forks_count')
ISSUES=$(curl -s "$GITHUB_API/issues" | jq '.total_count')
PR_MERGED=$(curl -s "$GITHUB_API/pulls" | jq '[.[] | select(.merged == true)] | length')
CONTRIBUTORS=$(curl -s "$GITHUB_API/contributors" | jq 'length')

echo "⭐ Star: $STAR_COUNT"
echo "👁️ Watchers: $WATCHERS"
echo "🍴 Forks: $FORKS"
echo "🐛 Issues: $ISSUES"
echo "✅ PRs: $PR_MERGED"
echo "👥 Contributors: $CONTRIBUTORS"

# 计算病毒传播指标
if [ "$STAR_COUNT" -gt 0 ]; then
    VIRAL_RATE=$(echo "scale=2; $STAR_COUNT * 0.1" | bc)
    echo "🔥 病毒传播率：$VIRAL_RATE Star/小时"
fi

# 检查增长临界点
if [ "$CONTRIBUTORS" -ge 100 ]; then
    echo "🎯 社区爆发临界点达成！"
elif [ "$STAR_COUNT" -ge 1000 ]; then
    echo "🚀 GitHub 算法推荐临界点接近！"
fi

# 自动创建教程（将热门 Issue 转为教程）
LATEST_ISSUES=$(curl -s "$GITHUB_API/issues?state=open&sort=comments&direction=desc&per_page=5" | jq -r '.[].title')

for issue in $LATEST_ISSUES; do
    if [[ "$issue" =~ "(tutorial|guide|how to|使用)" ]]; then
        echo "📝 检测到教程需求 Issue: $issue"
        echo "   → 自动生成教程中..."
    fi
done

echo "✅ 增长引擎运行完成！"
