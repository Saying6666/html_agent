---
name: web
description: 半自动 Web Design 数据集流水线。prompt 默认由当前 agent 手工生成；HTML 默认手工生成，也支持在用户明确要求时通过外部 API 流式生成；最后自动截图和录屏。
---

# Web Design Dataset Pipeline

## Prompt Length Rule (English Override)

- Every rewritten `prompt.md` should default to **at least 150 lines** unless the user explicitly asks for a shorter version.
- Do **not** reach the line target with blank lines, filler, or empty padding.
- Use the added length for stronger content coverage, interaction detail, responsive behavior, accessibility requirements, state design, and differentiation checks.
- If the prompt is long but still reads like a reusable batch template, rewrite it again until it becomes case-specific.

这个 skill 用来生成高质量单文件 HTML 网页设计数据集。

当前工作流是半自动的：

```text
Brief -> agent-authored prompt.md -> HTML(manual or streaming API) -> preview.png -> video.mp4
```

其中：

- `prompt.md` 不再由 API 或脚本模型生成
- `prompt.md` 必须由当前读取本 skill 的 agent 手工编写
- `src/index.html` 默认由当前读取本 skill 的 agent，根据 `prompt.md` 并结合 `frontend-design` skill 直接编写
- 只有当用户明确要求时，才允许切换到外部 API 生成模式
- 一旦使用外部 API 生成模式，必须使用流式调用，不能改成非流式一次性返回

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

### 1. 先由当前 agent 编写 prompt

当前 agent 必须：

- 按下面的“Prompt 格式（4 轮）”手工编写 `fdu_xxx/prompt.md`
- 保持 prompt 的结构与要求不变
- 写完后再用脚本做校验

可用下面的命令做存在性与结构校验：

```bash
python skills/web/scripts/generate_prompt.py --task fdu_012
```

### 2. 由当前 agent 生成 HTML

当前 agent 必须：

- 阅读 `fdu_xxx/prompt.md`
- 同时遵守本 skill 的 HTML 约束
- 使用 `frontend-design` skill 的设计标准
- 默认直接将最终结果写入 `fdu_xxx/src/index.html`

默认校验命令：

```bash
python skills/web/scripts/generate_html.py --task fdu_012
```

这会检查 `prompt.md` 和 `src/index.html` 是否已经就绪，不会主动调用外部 API。

### 2.1 在用户明确要求时使用外部 API 流式生成 HTML

仅当用户明确要求“调用外部 API 生成 HTML”时，才允许这样做。

要求：

- 仅支持显式 API 模式，不自动偷偷切换
- 必须使用流式调用
- 当前默认支持 OpenAI 兼容接口
- 从项目根目录 `.env.local` 读取配置
- 默认读取以下变量名：
  - `X666_BASE_URL`
  - `X666_API_KEY`
  - `X666_MODEL_GEMINI`

命令示例：

```bash
python skills/web/scripts/generate_html.py --task fdu_012 --mode api
```

这个命令会：

- 读取 `fdu_xxx/prompt.md`
- 以 `stream=true` 调用外部 API
- 边接收边写入临时文件
- 最终清洗结果并写入 `fdu_xxx/src/index.html`

### 2.2 长文件写入规范

当 `src/index.html` 很长、直接一次性写入容易失败时，允许采用下面的方式：

- 先写入紧凑版内容，保证文件不为空且结构完整
- 写入完成后，必须立刻把 `src/index.html` 格式化回正常的多行可读结构
- 紧凑到十几行的压缩形态只能作为临时落盘手段，不能作为最终交付
- 最终交付前必须重新检查：
  - 文件不是 0 字节
  - HTML 结构完整
  - 没有因为临时写入而引入额外的 `style=""`、坏标签、缺失闭合或乱码
  - 文件可读，可维护，便于后续人工检查

推荐做法：

-先写入紧凑版：
- 若本机有格式化能力，落盘后立即格式化 `src/index.html`
- 再运行 `generate_html.py` 做存在性校验，必要时再做浏览器截图烟测

### 3. 生成截图和录屏

```bash
python skills/web/scripts/run_pipeline.py --task fdu_012 --steps screenshot,video
```

### 4. 批量校验 prompt / HTML

```bash
python skills/web/scripts/run_pipeline.py --range 12-20 --steps prompt,html
python skills/web/scripts/run_pipeline.py --batch fdu_012,fdu_013 --steps prompt,html
python skills/web/scripts/run_pipeline.py --task fdu_012 --steps html --html-mode api
```

## 流水线步骤

| 步骤 | 脚本 | 输入 | 输出 |
|------|------|------|------|
| 1. Prompt | 当前 agent + `generate_prompt.py` | brief / 原有 prompt 要求 | `prompt.md` |
| 2. HTML | 当前 agent 或外部 API(流式) | `prompt.md` + `frontend-design` skill + HTML 约束 | `src/index.html` |
| 3. 截图 | `capture_screenshot.py` | `index.html` | `preview.png` |
| 4. 录屏 | `capture_video.py` | `index.html` | `video.mp4` |

## Prompt 格式（4 轮）

| Round | 内容 |
|-------|------|
| 1 | 角色 + 设计系统（CSS `:root` 变量） + 页面板块（10+ sections） |
| 2 | 交互 + 动效（8+ 功能交互 + Default/Hover/Active/Focus 四态） |
| 3 | 响应式（4 断点） + 无障碍（ARIA + 键盘 + reduced-motion） |
| 4 | 最终打磨 + 验收清单 + `GENERATE THE FINAL CODE NOW` |

## Prompt 生成约束

生成 `prompt.md` 时必须满足：

- 保持 4 轮渐进式结构不变
- `prompt.md` 必须是高密度可执行文档，默认不少于 **150 行**；不要用空行硬凑，应该通过更具体的结构约束、内容覆盖、交互说明、响应式要求、无障碍细节、状态设计、差异化测试等把信息写实写满。
- **允许并鼓励拥抱现代高级 Web App 风格 (Modern Premium Glassmorphism & Glo UI)**：例如 Vercel、Linear 或 Apple 官网级别的高级质感。允许在 prompt 中使用相关的视觉约束词（如：`glassmorphism`、`backdrop-filter`、`glowing gradient borders`、`ambient orbs`）。
- **要求精细化的 CSS 工艺约束，而非堆砌空泛词汇**：如果想要毛玻璃效果，必须在 prompt 中同时规定“内阴影高光边缘 (`inset box-shadow`)”或“极光背景动画 (`conic-gradient`)”以确保质感，而不仅是抛出一个 `luxury` 或 `cinematic` 词汇盲目指望大模型发挥。
- Round 1 中的 section / block 描述应结合创意布局（例如：巨型 Mac-OS 视窗结构、全屏暗黑网格、居中悬浮控制台等），不要写成“老旧的从上往下铺满的 SaaS 模版（如：Hero -> 3个Feature -> Pricing网格 -> FAQ）”。
- Round 1 必须包含角色定义、设计系统、CSS `:root` 变量、10+ 页面 sections（或深度的信息展现区域）。
- Round 2 必须包含 8+ 功能交互，并覆盖 Modal、Accordion、Toast、Tabs、Scroll Reveal、Stagger Animation、Count-up、Navbar scroll transition，但交互方式要求**现代化、丝滑（基于 cubic-bezier 的动画）**。
- Round 3 必须包含 4 个断点、ARIA、键盘导航、`prefers-reduced-motion`。
- Round 4 必须包含最终打磨、验收清单（重点检查：玻璃特效是否通透、阴影材质是否高级、边框是否发光等），并以 `GENERATE THE FINAL CODE NOW` 收尾。
- 技术约束必须继续要求单文件 `index.html`、内联 CSS/JS、禁止框架、禁止本地图片资源。
- **排版要求必须对标 2025-2026 真实的顶级产品站**，绝对不要看起来像 bootstrap 时代的廉价 Demo。

### 为什么要修改旧的 Prompt 禁令？

- 之前在旧版本中禁止大模型使用毛玻璃、大圆角和暗黑发光风格，是因为大模型如果缺乏具体的 CSS 约束，往往只会写出**“廉价的黑底白字加一个灰色圆角框”**（即所谓的“同质化模版味”）。
- 但实际上，现代前端真正的高级感恰恰来源于**对玻璃态（Glassmorphism）、微边框（Micro-borders / inset box-shadows）、弥散光（Ambient Orbs）以及平滑动画（Smooth Transitions）的极致工艺（Craft）**。
- 所以新的指导思想是：**不避讳高级潮流特效，而是通过 Prompt 强迫模型运用真正的高级 CSS 技巧**。
- 例如：如果写“请生成一个好看的深色卡片”，结果总是失败的；但如果写“在一个带有 `blur(30px)` 的深色卡片周围包裹一层利用 `conic-gradient` 且含有内高光 `inset 0 1px rgba(255,255,255,0.15)` 的物理边框”，页面立刻就会展现出现代 Web App 的质感。
- **核心逻辑：用硬性的工程约束手法（指名道姓要哪些 CSS 属性和 DOM 结构层级），去确保“高级感”落地，而不是去封杀“高级感”本身。**

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
- 最终文件必须是正常多行、可读、可维护的 HTML，不交付临时压缩版
- **【重要】HTML 内容必须极其丰满与完整（推荐 600-1200+ 行）**：
  - 绝对禁止输出任何形式的占位符（如 `<!-- content goes here -->`、`<!-- 更多内容 -->`、`// JS 代码省略`）。
  - 所有定义的区块（如 12+ 个 Layout sections）必须在 HTML 中完全展开并在相关结构中塞满针对业务的真实文案。页面布局必须足够长，具有完整的产品站纵深。
  - 所有需要交互的组件（如 Tabs 切换、Modals 弹窗、Accordions 手风琴、Toast 通知、滚动的 Count-ups 数值等），**必须在底部的 `<script>` 中使用纯原生 JavaScript 严格绑定真实的逻辑和事件监听**。确保页面在浏览器中实际可点击、响应、并有完美的真实功能反馈，绝不能只做静态 UI 摆设。
- 若使用外部 API 生成，必须由用户明确要求且必须使用流式调用

## 环境要求

### 依赖

```bash
pip install playwright && playwright install chromium
```

`ffmpeg` 需要在 PATH 中，用于录屏转码。

如果本机安装了 HTML 格式化相关依赖，也建议在写完 `src/index.html` 后立即格式化，再进入截图和录屏阶段。
