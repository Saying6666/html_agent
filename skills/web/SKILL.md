---
name: web
description: 半自动 Web Design 数据集流水线。从 brief 到 prompt，再由当前 agent 生成 HTML，最后自动截图和录屏。
---

# Web Design Dataset Pipeline

这个 skill 用来生成高质量单文件 HTML 网页设计数据集。

当前工作流是半自动的：

```text
Brief -> prompt.md -> agent-authored index.html -> preview.png -> video.mp4
```

其中：

- `prompt.md` 可以由脚本自动生成
- `src/index.html` 不再由 API 或脚本模型生成
- `src/index.html` 必须由当前读取本 skill 的 agent，根据 `prompt.md` 并结合 `frontend-design` skill 直接编写

## 交付物结构

```text
fdu_xxx/
├── prompt.md          # 4 轮渐进式提示词
├── preview.png        # 全页长截图
├── src/
│   └── index.html     # 由当前 agent 编写的单文件 HTML（CSS/JS 内联）
└── video.mp4          # 自动录屏（20-60秒，24fps）
```

## 推荐使用方式

### 1. 先生成 prompt

自动生成网站 brief 和 prompt：

```bash
python skills/web/scripts/run_pipeline.py --task fdu_012 --steps prompt --auto
```

或者手动指定参数生成 prompt：

```bash
python skills/web/scripts/run_pipeline.py --task fdu_012 --steps prompt \
    --category "SaaS Landing Page" \
    --concept "AI-powered code review tool" \
    --audience "Engineering managers" \
    --style "Modern Minimal" \
    --site-name "CodeSight"
```

### 2. 由当前 agent 生成 HTML

当前 agent 必须：

- 阅读 `fdu_xxx/prompt.md`
- 同时遵守本 skill 的 HTML 约束
- 使用 `frontend-design` skill 的设计标准
- 直接将最终结果写入 `fdu_xxx/src/index.html`

可用下面的命令做存在性校验：

```bash
python skills/web/scripts/generate_html.py --task fdu_012
```

这个脚本不会生成 HTML，只会检查 `prompt.md` 和 `src/index.html` 是否已经就绪。

### 3. 生成截图和录屏

```bash
python skills/web/scripts/run_pipeline.py --task fdu_012 --steps screenshot,video
```

### 4. 批量生成 prompt

```bash
python skills/web/scripts/run_pipeline.py --range 12-20 --steps prompt --auto
python skills/web/scripts/run_pipeline.py --batch fdu_012,fdu_013 --steps prompt --auto
```

## 流水线步骤

| 步骤 | 脚本 | 输入 | 输出 |
|------|------|------|------|
| 1. Prompt | `generate_prompt.py` | brief 参数 / `--auto` | `prompt.md` |
| 2. HTML | 当前 agent | `prompt.md` + `frontend-design` skill | `src/index.html` |
| 3. 截图 | `capture_screenshot.py` | `index.html` | `preview.png` |
| 4. 录屏 | `capture_video.py` | `index.html` | `video.mp4` |

## Prompt 格式（4 轮）

| Round | 内容 |
|-------|------|
| 1 | 角色 + 设计系统（CSS `:root` 变量） + 页面板块（10+ sections） |
| 2 | 交互 + 动效（8+ 功能交互 + Default/Hover/Active/Focus 四态） |
| 3 | 响应式（4 断点） + 无障碍（ARIA + 键盘 + reduced-motion） |
| 4 | 最终打磨 + 验收清单 + `GENERATE THE FINAL CODE NOW` |

## HTML 生成约束

生成 `src/index.html` 时必须满足：

- 单文件，CSS/JS 内联，使用 `<style>` + `<script>`
- 禁止 React/Vue/Svelte/jQuery/Tailwind CDN
- 禁止本地资源，图片用远程 URL 或内联 SVG
- `backdrop-filter` 必须有 `-webkit-backdrop-filter`，且前缀在前
- 禁止 `style=""` 内联样式
- 表单控件必须有可访问名称
- 图标按钮必须有 `aria-label`
- 至少 5 种真实交互，优先实现 prompt 中要求的功能交互
- 对标 2025-2026 真实产品站，不做课堂 demo
- 设计质量遵循 `frontend-design` skill，避免通用化 AI 页面风格

## 环境要求

### `.env.local`

如果需要自动生成 `prompt.md`，需要：

```bash
X666_BASE_URL=https://your-api-endpoint/v1
X666_API_KEY=sk-your-key
X666_MODEL_GEMINI=gemini-3.1-pro-preview
```

注意：这些配置现在只用于 `prompt` 生成，不再用于 `index.html` 生成。

### 依赖

```bash
pip install playwright && playwright install chromium
```

`ffmpeg` 需要在 PATH 中，用于录屏转码。
