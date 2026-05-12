# 🦞 OpenClaw 演示 GIF 录制指南

## 🎬 录制目标

为博客和 GitHub 页面创建高质量演示 GIF，展示 OpenClaw 核心功能。

## 📋 录制清单

### 1. 快速上手 GIF (15 秒)

**场景：** 安装和连接第一个渠道

**步骤：**
1. 终端打开
2. 运行安装命令
3. 连接 Discord/Telegram
4. 显示成功消息

**工具：**
- QuickTime (Mac)
- ScreenFlow
- OBS

**尺寸：** 1280x720

### 2. 语音唤醒 GIF (10 秒)

**场景：** 语音唤醒和任务执行

**步骤：**
1. 说"Hell, OpenClaw"
2. 显示唤醒成功
3. 执行任务
4. 显示结果

### 3. Canvas 工作区 GIF (20 秒)

**场景：** Canvas 可视工作区

**步骤：**
1. 打开 Canvas
2. 展示节点
3. 拖放任务
4. 执行任务

### 4. 多智能体协作 GIF (25 秒)

**场景：** 多智能体路由

**步骤：**
1. 创建任务
2. 显示子智能体
3. 执行任务
4. 显示结果

### 5. 多平台支持 GIF (30 秒)

**场景：** 多平台消息聚合

**步骤：**
1. 连接多个渠道
2. 显示统一 inbox
3. 处理消息
4. 自动化回复

## 🎨 优化建议

### 尺寸
- 宽度：800-1280px
- 高度：自适应（4:3 或 16:9）
- 文件大小：< 5MB

### 帧率
- 10-15 fps（节省文件大小）
- 或 24 fps（高质量）

### 压缩
- 使用 GIF 优化工具
- 减少颜色数量（256 色）
- 启用透明度

### 工具推荐
- **QuickTime** (Mac 内置)
- **ScreenFlow** (专业录制)
- **OBS** (免费开源)
- **Giphy** (上传分享)

## 📤 发布位置

### GitHub
- 添加到 README
- 添加到博客文章
- 添加到 Releases

### 博客
- Medium
- Dev.to
- 个人博客

### 社交媒体
- Twitter
- Reddit
- Discord

## 📊 示例代码

### Python 生成 GIF

```python
from PIL import Image
import os

# 录制 GIF
frames = []
for i in range(num_frames):
    # 捕获屏幕
    frame = capture_screen()
    frames.append(frame)

# 保存 GIF
frames[0].save(
    'output.gif',
    save_all=True,
    append_images=frames[1:],
    duration=100,  # 每帧 100ms
    loop=0
)
```

### Bash 脚本

```bash
#!/bin/bash
# 录制 GIF

rec() {
    local output=$1
    local duration=$2
    
    # 录制
    quicktimectrl record "$output" "$duration"
}

# 录制快速上手 GIF
rec "quickstart.gif" 15
```

## 🔧 自动化录制

### 脚本示例

```bash
#!/bin/bash
# openclaw-record.sh

record_gif() {
    local name=$1
    local duration=$2
    
    # 执行命令并录制
    echo "Recording $name for $duration seconds..."
    # 录制逻辑
}

# 录制所有 GIF
record_gif "quickstart.gif" 15
record_gif "voice.gif" 10
record_gif "canvas.gif" 20
```

## 💡 提示

1. **保持简洁：** 每个 GIF 专注于一个功能
2. **添加标注：** 在 GIF 中添加文字说明
3. **优化大小：** 确保 GIF 文件大小合理
4. **测试播放：** 确保在移动设备上正常显示
5. **版本控制：** 保存原始视频和不同版本

---

🦞 *小蜗方式*
