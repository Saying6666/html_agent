# Web Skill 重写计划

## 目标
完全重写 skills/web/，实现 4 个核心功能：

### 1. prompt 生成 (`scripts/generate_prompt.py`)
- 输入：taskid、网站类别、概念描述等参数
- 输出：4 轮格式化的 prompt.md（Round 1-4，格式与用户示例一致）
- 使用 AI API 生成 prompt 内容

### 2. HTML 生成 (`scripts/generate_html.py`)
- 读取 prompt.md，拼接所有 4 轮 prompt 为单次对话
- 在 prompt 前追加前端工程师系统提示 + 约束规则
- **单轮对话 + 流式响应**，直接生成 src/index.html
- API 配置读取 .env.local（X666_BASE_URL, X666_API_KEY, X666_MODEL_GEMINI）

### 3. 自动截图 (`scripts/capture_screenshot.py`)
- 使用 Playwright 打开 index.html
- 等待页面完全加载（字体、图片、动画）
- 全页长截图保存为 preview.png
- 依赖：playwright (pip install playwright && playwright install chromium)

### 4. 自动录屏 (`scripts/capture_video.py`)
- 使用 Playwright 打开 index.html
- 自动平滑滚动到底部，尝试点击可交互控件（tabs/accordion/modal）
- 录制 20-60 秒，24fps
- 输出 video.mp4
- 依赖：playwright

### 5. 工作流入口 (`scripts/run_pipeline.py`)
- 串联所有步骤：prompt → html → screenshot → video
- 支持单步或全流程执行

### 6. SKILL.md 重写
- 更新为新的工作流说明

## 文件结构
```
skills/web/
├── SKILL.md
├── scripts/
│   ├── generate_prompt.py
│   ├── generate_html.py
│   ├── capture_screenshot.py
│   ├── capture_video.py
│   └── run_pipeline.py
└── references/
    └── spec-summary.md (保留)
```
