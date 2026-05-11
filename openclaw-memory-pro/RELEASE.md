# 发布指南 🦞

## 发布流程

### 1. 更新版本

```bash
# 更新 CHANGELOG.md
echo "## [0.2.0] - 2026-05-XX" >> CHANGELOG.md
echo "" >> CHANGELOG.md
echo "### 新增功能" >> CHANGELOG.md
echo "- 新功能描述" >> CHANGELOG.md
```

### 2. 提交代码

```bash
git add .
git commit -m "chore: release v0.2.0"
git push origin main
```

### 3. 发布到 PyPI

```bash
pip install build twine
python -m build --outdir dist/
twine upload dist/*
```

### 4. GitHub Release

```bash
# 创建 Release
gh release create v0.2.0 dist/*
```

## 版本管理

- v0.1.0 - 初始版本（记忆宫殿架构）
- v0.2.0 - 计划：增加高性能检索、缓存优化
- v1.0.0 - 计划：稳定版、企业级功能

---

**更新流程**: 遵循语义化版本控制 (SemVer)
