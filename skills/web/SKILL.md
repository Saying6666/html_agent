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
Brief -> agent-authored prompt.md -> HTML(manual or streaming API) -> preview.png -> video.mp4 -> agent-authored description
```

其中：

- `prompt.md` 不再由 API 或脚本模型生成
- `prompt.md` 必须由当前读取本 skill 的 agent 手工编写
- `src/index.html` 默认由当前读取本 skill 的 agent，根据 `prompt.md` 并结合 `frontend-design` skill 直接编写
- 自然语言描述不通过脚本生成，必须由当前读取本 skill 的 agent 手工编写
- 只有当用户明确要求时，才允许切换到外部 API 生成模式
- 一旦使用外部 API 生成模式，必须使用流式调用，不能改成非流式一次性返回

## 交付物结构与严格规范

```text
descriptions/
└── fdu_xxx.md          # 由当前 agent 手工编写的自然语言描述，统一集中存放

fdu_xxx/
├── prompt.md          # 4 轮渐进式提示词
├── preview.png        # 全页长截图
├── src/
│   └── index.html     # 由当前 agent 编写的单文件 HTML（CSS/JS 内联）
└── video.mp4          # 自动录屏（严格 24fps，时长 4-60 秒）
```

### 【绝对强制的打包与提交规范】

1. **命名必须绝对一致**：顶级压缩包文件名、ZIP 内的文件夹名、内部数据/任务 ID，三者必须统一为 `fdu_001` 这类格式。严禁使用 `fd_001`、`fudan_001` 或其他变种。
2. **不允许有多余的文件夹层级**：正确做法：把 `prompt.md`、`src`文件夹、`preview.png`、`video.mp4` 放在一个叫 `fdu_xxx` 的文件夹里，然后**直接压缩这个 `fdu_xxx` 文件夹**。解压后应该直接看到 `fdu_xxx/` 目录，绝对不能在外面再套一层导致解压出 `fdu_xxx/fdu_xxx/` 这类结构。
3. **禁止混入系统隐藏文件**：直接右键压缩极易带入 `__MACOSX` 和 `.DS_Store`。Mac 用户务必使用终端打包以保持纯净：
   `zip -r fdu_xxx.zip fdu_xxx/ -x "*/.DS_Store" -x "*/__MACOSX/*"`
4. **视频硬性参数**：视频帧率**必须是 24fps**（提交 30fps、60fps 等全部判定不合格），运行时长在 4 - 60 秒之间。
   - 验证命令：`ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate video.mp4`
   - 转换修正命令：`ffmpeg -i video.mp4 -r 24 -c:v libx264 -pix_fmt yuv420p video_24fps.mp4`
5. **四件套缺一不可**：`prompt.md` + `src/index.html` + `preview.png` + `video.mp4` 必须齐全。
6. **彻底禁用 Tailwind CDN**：HTML 代码内严禁出现 `cdn.tailwindcss.com`，样式必须全部老老实实写在 `<style>` 内联标签里。

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

### 4. 由当前 agent 手工编写自然语言描述

当前 agent 必须：

- 阅读 `fdu_xxx/src/index.html`，必要时结合 `preview.png` 和 `video.mp4` 理解页面行为
- 按“从页面顶部到底部”的真实浏览顺序撰写描述
- 将结果统一写入项目根目录下的 `descriptions/fdu_xxx.md`
- 不新增脚本；描述步骤完全由当前 agent 手工完成

推荐交付形式：

```text
descriptions/
├── fdu_001.md
├── fdu_002.md
├── fdu_003.md
└── ...
```

### 5. 由质检 subagent 做最终复核

每个 case 在 prompt、HTML、截图、录屏、描述完成后，**必须额外启动一个质检 subagent** 做最终复核。

质检 subagent 必须极其严格地排查（只要不合格直接打回）：

- **交付四件套存在性与目录校验**：检查是否存在且命名恰为 `fdu_xxx`（严禁 `fd_xxx`），并且目录下 `prompt.md`、`src/index.html`、`preview.png`、`video.mp4` 四者缺一不可。
- **24fps与视频合法性强制验证**：必须能断言 `video.mp4` 时长 4-60秒并且帧率是 `24fps`！如果违规，必须退回或用命令修好。
- **彻底封杀 Tailwind CDN**：通过审查 `src/index.html` 排查是否出现了 `https://cdn.tailwindcss.com` 或者别的 CDN 外部库文件，如果有必须以“通过老旧的 CDN 作弊”为由打回。
- `prompt.md` 是否大于 150 行，是不是在硬水字数，是否仍符合 4 轮结构。
- `src/index.html` 是否足够完整非空，有没有出现残缺的报错闭合。

质检 subagent 的结论必须明确分成两类：

- 通过：说明该 case 可以进入交付
- 不通过：明确指出哪一项失败，并要求生成 agent 返工后再次送检

### 6. 批量校验 prompt / HTML

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
| 5. 描述 | 当前 agent（手工） | `src/index.html` + `preview.png` + `video.mp4` | `descriptions/fdu_xxx.md` |
| 6. 质检 | 质检 subagent（手工复核） | `prompt.md` + `src/index.html` + 相关交付物 | pass / fail + 返工意见 |

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
- **放飞自我的创意布局（极其重要）**：彻底打破“趋同感”！Round 1 中的 section / block 描述必须极其狂野与现代，例如：横向平移的页面区块、完全非对称的 Bento Box（便当盒网格）、占据全屏的悬浮毛玻璃层、Z轴透视的三维卡片翻转效果、侵入全屏的超级大 Typography 等体验，绝对不要写成旧时代从上到下的 SaaS 纯色区块流（Hero -> 3个Feature -> Pricing -> FAQ）。
- **完全释放真实的图片占位符**：不仅要通过代码做排版，必须在 Prompt 中显式要求模型使用诸如 `https://source.unsplash.com/random/800x600/?cyberpunk` 或 `https://picsum.photos/` 这类远程 URL 作为大型 Background 背景、满屏卡片 cover 等撑满版面。这能极大降低页面的“代码干瘪味”，显著提升视觉张力。
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
- **严禁**使用外部前端框架和库的 CDN：彻底禁止出现诸如 `<script src="https://cdn.tailwindcss.com"></script>` 的操作，更不许出现 React/Vue 等。HTML 的 `style` 必须完全手工内联。
- 禁止加载任何本地图片资源（因为要打包单文件），但是**必须极其主动且大胆地在页面背景或大型插图卡片中放开使用高质量的远程占位图**（如 `https://source.unsplash.com/random/xx/?nature`），这是解决页面干瘪同质化的关键。
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

## 自然语言描述模块

自然语言描述是强制补充模块，但**不通过脚本生成**，而是由当前 agent 手工撰写。

### 输出位置

- 所有 case 的描述文件统一放在项目根目录 `descriptions/` 下
- 每个 case 一个文件，命名为 `descriptions/fdu_xxx.md`
- 不要把描述文件散落到各自任务目录中

### 写作目标

- 描述要自然、流畅、具体，有画面感，但不能浮夸失真
- 语言可以更丰富、更生动，不要写成机械的操作清单
- 要像一个认真观察页面的人在复述页面体验，而不是在堆砌模板句

### 描述顺序

- **必须严格按照页面从上到下的真实浏览顺序来写**
- 先写首屏，再写首屏之后的区块，再继续往下
- 不允许跳着写，不允许把底部交互提前塞到前面
- 如果页面存在吸顶导航、滚动切换、滚动驱动动画，也要放在它实际会被注意到的位置描述

### 描述边界

- 不要为了显得丰富而捏造页面里并不存在的动效、反馈或交互
- 不要把多个交互揉成无法逐一对应页面的空泛总结
- 对静态可见内容，除非与任务理解强相关，否则不要过度展开文案细节
- 不必逐字复述标题、段落或图片中的所有内容
- 描述重点应放在浏览过程中的结构推进、视觉变化、悬停反馈、展开收起、切换、弹层、滚动触发、数值变化等真实体验

### 推荐写法

- 从进入页面时首先看到什么开始写
- 然后按继续向下浏览的顺序，描述各区块如何出现、如何变化、可以如何操作
- 写到交互时，要交代“怎么触发”和“触发后发生了什么”
- 写到动效时，要尽量对应真实表现，例如滑入、展开、淡入、位移、数值增长、指示器滑动，而不是泛泛地说“有很酷的动画”
- 可以适当使用更生动的措辞去表现节奏、质感和层次，但必须以页面真实存在的现象为基础

### 简单示例要求

- 好的描述应当让人顺着文字就能大致还原浏览路径
- 好的描述应当能区分“直接可见的内容”和“需要操作后才出现的变化”
- 好的描述应当保留网页本身的真实性，不夸张，不虚构，不混乱

## 大规模批量并发跑单规范 (Batch Execution Workflow)

在面对包含 50+ 个甚至更多目标文件夹的生成任务时，为确保执行的稳定性和高效率并避免网络掉线（如 `ERR_CONNECTION_CLOSED`），必须采取以下 **Subagent 并发执行标准**：

### 1. 严格 5 并发限制 (Batch of 5)
- 严禁一条条串行执行（因上下文及时间消耗太大）。
- 严禁一次性并行呼叫 10 个以上（容易导致后端 API 并发超限断连或文件系统冲突）。
- **必须维持“每批次5个任务” (5 concurrent `runSubagent` calls)**，跑完一批，打印一条通知，再跑下一批。如果有失败的（比如网络断开），在下一批次中对失败项进行自动重试。

### 2. 生成 subagent 与质检 subagent 必须成对出现

- 不能只让生成 subagent 写完就结束
- 每个生成 subagent 完成后，必须再起一个质检 subagent 单独复核
- 质检 subagent 不负责美化表达，只负责按规则挑错、拦截问题、给出是否通过的结论
- 若质检不通过，生成 subagent 必须返工，返工后再次送交质检 subagent

### 3. 传递给生成 Subagent 的指令（Delegation Prompt）
唤起 Subagent 的 prompt 不能仅仅是“去完成 fdu_xxx 任务”。为了抵御模型偷懒，**必须在呼叫 Subagent 的 prompt 中带上硬性指标的浓缩版**。例如：
```text
Task for fdu_xxx:
1. REWRITE `fdu_xxx/prompt.md` to >160 lines. Target "Modern Premium Glassmorphism & Glo UI". Define 12+ sections.
2. OVERWRITE `fdu_xxx/prompt.md`.
3. GENERATE COMPLETE HTML inside `fdu_xxx/src/index.html` (>600 lines).
4. NO PLACEHOLDERS. Fill all 12+ sections with real SaaS/product text.
5. Wire all micro-interactions (blur, scroll reveal, mouse-glow) with REAL Vanilla JS.
6. Return success.
```

### 4. 传递给质检 Subagent 的指令（QC Prompt）

唤起质检 subagent 时，prompt 必须要求它只做检查，不做主观宽松放行。至少覆盖以下核查点：

```text
QC task for fdu_xxx:
1. CHECK whether `fdu_xxx/prompt.md` follows the required 4-round structure.
2. CHECK whether `prompt.md` has at least 150 meaningful lines.
3. CHECK whether `prompt.md` contains forbidden task placeholders such as `fdu_xxx`, `fdu_012`, `fdu_001`.
4. CHECK whether `fdu_xxx/src/index.html` exists, is non-empty, and looks complete.
5. CHECK whether HTML contains placeholders, broken structure, truncated output, or obvious generation failure.
6. Return PASS or FAIL with concrete reasons.
```

### 5. 文件写入策略
对于 1000+ 行级别的大型 HTML：
- 建议 Subagents 优先使用 Python 脚本挂载 `with open('...', 'w')` 来写入大段代码，或合理使用环境自带的文件编辑 Tool，**严防使用 Terminal/PowerShell Echo 导致单双引号及转义符报错断流**。

## 环境要求

### 依赖

```bash
pip install playwright && playwright install chromium
```

`ffmpeg` 需要在 PATH 中，用于录屏转码。

如果本机安装了 HTML 格式化相关依赖，也建议在写完 `src/index.html` 后立即格式化，再进入截图和录屏阶段。
