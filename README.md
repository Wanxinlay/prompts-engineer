# 提示词工程师 Skill

基于 [PromptingGuide.ai](https://www.promptingguide.ai/zh) 提示词工程指南构建的提示词生成技能。

## 功能

用户用简单的自然语言输入需求后，Agent 能够：
1. 分析用户需求
2. 在指令不够明确时追问相关细节
3. 基于提示词工程最佳实践，撰写结构清晰、内容完备的专业提示词

## 文件说明

- `prompt-engineer.skill.md` - 完整的 Skill 定义，可以导入到支持 Skill 的系统中使用
- `examples/` - 不同任务类型的生成示例（周报、代码审查、数据分析、创意写作等）
- `prompt-cli.py` - 命令行工具，可直接输入需求生成提示词

## 使用方式

### 1. 在 Claude Code Skill 系统中使用

将 `prompt-engineer.skill.md` 添加到你的 Skill 目录，然后调用：

```
/prompt-engineer 帮我生成一个用于...的提示词
```

### 2. 作为系统提示词使用

将 `prompt-engineer.skill.md` 中"系统提示词"部分的内容复制，作为 AI 的系统提示，然后输入你的需求。

### 3. 使用命令行工具

```bash
# 安装依赖
pip install openai  # 或其他支持的 provider

# 运行工具
python prompt-cli.py

# 或者直接传入需求
python prompt-cli.py "帮我生成一个写周报的提示词"
```

工具会交互式地追问必要信息，然后输出生成的提示词。

## 工作流程

1. **需求分析** → 解析用户需求，识别任务类型
2. **信息收集** → 关键信息不完整时主动追问
3. **提示词构建** → 按照最佳实践生成结构化提示词

## 生成的提示词结构

生成的提示词包含：
- 角色定位
- 任务目标
- 背景信息（可选）
- 输出要求（格式、长度、风格）
- 约束规则
- 示例（可选）

## 技术选择指南

| 任务类型 | 推荐技术 |
|---------|---------|
| 数学/逻辑推理 | Chain-of-Thought (CoT) |
| 需要事实依据 | Retrieval-Augmented Generation (RAG) |
| 复杂决策问题 | Tree of Thoughts (ToT) |
| 需要调用工具 | ReAct |
| 需要一致性 | Self-Consistency |
| 代码生成/调试 | 结构化输出 + 示例 |
| 创意写作 | 角色扮演 + 风格指定 |

## 示例

详见 `examples/` 目录：
- `weekly-report.md` - 周报生成
- `code-review.md` - 代码审查
- `data-analysis.md` - 数据分析报告
- `creative-writing.md` - 创意写作

## 参考资料

- [提示词工程指南 - PromptingGuide.ai](https://www.promptingguide.ai/zh)
