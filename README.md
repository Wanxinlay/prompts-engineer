# 提示词工程师 Skill

基于 [PromptingGuide.ai](https://www.promptingguide.ai/zh) 提示词工程指南构建的提示词生成技能。

## 功能

用户用简单的自然语言输入需求后，Agent 能够：
1. 分析用户需求
2. 在指令不够明确时追问相关细节
3. 基于提示词工程最佳实践，撰写结构清晰、内容完备的专业提示词

## 文件说明

- `prompt-engineer.skill.md` - 完整的 Skill 定义，可以导入到支持 Skill 系统中使用
- `system-prompt.txt` - 独立的系统提示词，可直接作为 Agent 的系统提示使用
- `prompt-engineer-skill.md` - 详细的技能说明文档

## 使用方式

### 在 Claude Code Skill 系统中使用

将 `prompt-engineer.skill.md` 添加到你的 Skill 目录，然后可以通过以下方式调用：

```
/prompt-engineer 帮我生成一个用于...的提示词
```

### 独立使用

直接将 `system-prompt.txt` 的内容作为系统提示词给 AI，然后输入你的需求即可。

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

## 参考资料

- [提示词工程指南 - PromptingGuide.ai](https://www.promptingguide.ai/zh)
