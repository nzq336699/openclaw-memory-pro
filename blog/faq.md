# 🦞 OpenClaw 常见问题 (FAQ)

## 安装相关

### Q: 如何在 macOS 上安装 OpenClaw？

A: 运行以下命令：
```bash
openclaw onboard --install-daemon
```

或者使用 Homebrew：
```bash
brew install openclaw
```

### Q: 如何在 Linux 上安装？

A: 运行：
```bash
curl -sSf https://openclaw.ai/install.sh | sh
```

或者从源码安装：
```bash
git clone https://github.com/nzq336699/openclaw.git
cd openclaw
pip install -e .
```

### Q: 如何在 Windows 上运行？

A: 目前主要支持 macOS、Linux 和 Android。Windows 支持正在开发中！

### Q: 安装失败怎么办？

A: 检查：
1. Python 版本（建议 3.9+）
2. 系统依赖
3. 网络连接
4. 查看日志：`openclaw gateway logs`

## 渠道连接

### Q: 如何连接 Discord？

A: 
1. 获取 Bot Token
2. 运行：
```bash
openclaw channel connect \
  --platform discord \
  --token $DISCORD_TOKEN
```
3. 授权 Bot 到你的服务器

### Q: 如何连接 Telegram？

A: 
1. 通过 @BotFather 创建 Bot
2. 获取 Token
3. 运行：
```bash
openclaw channel connect \
  --platform telegram \
  --token $TELEGRAM_TOKEN
```

### Q: 支持多少渠道？

A: 目前支持 15+ 渠道：
- Discord, Slack, Telegram
- Signal, iMessage, WhatsApp
- 和更多...

### Q: 可以手动连接渠道吗？

A: 是的！访问 `openclaw channel list` 查看所有可用渠道。

## 语音唤醒

### Q: 语音唤醒不工作怎么办？

A: 检查：
1. macOS/iOS 系统权限（麦克风）
2. 唤醒词配置正确
3. 系统音量足够
4. 重启 OpenClaw

### Q: 如何在 Android 上使用语音唤醒？

A: 使用配套 APP 扫描配对二维码。

### Q: 唤醒词可以自定义吗？

A: 可以！运行：
```bash
openclaw voice-wake configure \
  --wake-word "Hey OpenClaw"
```

## Canvas

### Q: Canvas 不显示？

A: 确保：
1. macOS/iOS 平台
2. A2UI 已启用
3. 网络连接正常

### Q: 如何截图 Canvas？

A: 运行：
```bash
openclaw canvas snapshot --output screenshot.png
```

## 多智能体

### Q: 如何创建子智能体？

A: 运行：
```bash
openclaw subagent spawn \
  --task "分析这份文档" \
  --label "文档分析"
```

### Q: 如何查看子智能体状态？

A: 运行：
```bash
openclaw subagent list
```

### Q: 如何停止子智能体？

A: 运行：
```bash
openclaw subagent kill --target <agent-id>
```

## 安全

### Q: 数据是否存储在云端？

A: 不！OpenClaw 本地优先，数据存储在本地设备。

### Q: 如何配置安全设置？

A: 运行：
```bash
openclaw gateway config patch \
  --path channels.discord.dm.policy \
  --value "pairing"
```

### Q: 如何禁用遥测？

A: OpenClaw 默认不收集遥测数据。

### Q: 如何查看安全日志？

A: 运行：
```bash
openclaw gateway logs --level security
```

## 性能

### Q: OpenClaw 处理消息的速度如何？

A: 本地处理，响应时间 < 1 秒。

### Q: 支持多少并发会话？

A: 单设备支持 50+ 并发会话。

### Q: 如何处理大量消息？

A: OpenClaw 使用多智能体路由，可处理 500+ 消息/分钟。

## 贡献

### Q: 如何贡献代码？

A: 
1. Fork 仓库
2. 创建特性分支
3. 提交 Pull Request
4. 等待审查

### Q: 如何报告 Bug？

A: 在 [GitHub Issues](https://github.com/nzq336699/openclaw/issues) 创建 Issue。

### Q: 如何提交功能请求？

A: 在 [GitHub Discussions](https://github.com/nzq336699/openclaw/discussions) 创建讨论。

## 故障排查

### Q: `openclaw` 命令找不到？

A: 确保已安装并添加到 PATH：
```bash
export PATH="$HOME/.openclaw/bin:$PATH"
```

### Q: Gateway 无响应？

A: 重启 Gateway：
```bash
openclaw gateway restart
```

### Q: 如何查看日志？

A: 
```bash
openclaw gateway logs --tail 50
```

### Q: 如何诊断问题？

A: 运行：
```bash
openclaw doctor
```

## 升级

### Q: 如何升级到最新版本？

A: 
```bash
# macOS/Linux
openclaw update

# 或从源码
git pull origin main
```

### Q: 升级会丢失数据吗？

A: 不会！数据存储在本地，升级是安全的。

## 其他

### Q: OpenClaw 是开源的吗？

A: 是的！采用 MIT 许可证。

### Q: 如何支持项目？

A: 
- Star 仓库
- 提交 PR
- 爱发电赞助
- GitHub Sponsors

### Q: 商业使用是否允许？

A: 允许！MIT 许可证允许商业使用。

### Q: 如何引用 OpenClaw？

A: 
```bibtex
@software{openclaw,
  author = {OpenClaw Team},
  title = {OpenClaw: Your Personal AI Assistant},
  year = {2026},
  url = {https://github.com/openclaw/openclaw}
}
```

---

🦞 *小蜗方式*

更多问题？查看 [GitHub Discussions](https://github.com/nzq336699/openclaw/discussions)！
