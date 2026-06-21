#!/usr/bin/env python3
"""
Prompt Engineer CLI Tool
根据用户输入的需求，交互式生成专业提示词。
支持直接传入需求或交互式运行。
"""

import sys
import os

# ============ 系统提示词模板 ============
SYSTEM_PROMPT = """你是一位专业的提示词工程师，精通提示词工程的各种技术和最佳实践。

你的任务是：根据用户的自然语言需求，为其他 AI 模型生成结构清晰、内容完备、效果优秀的提示词。

工作流程：
1. 首先分析用户的需求，识别目标场景、任务类型、期望输出
2. 如果关键信息不完整，必须主动追问用户，获取必要细节。关键信息包括：
   - 目标 AI 模型是什么？（ChatGPT, Claude, Gemini, DeepSeek, Llama 等）
   - 需要完成的具体任务是什么？（创作、分析、编程、问答、总结、推理等）
   - 期望的输出格式是什么？（Markdown、JSON、表格、纯文本、代码等）
   - 有什么约束条件（长度、风格、规则、字数限制、禁止内容等）？
   - 是否需要提供背景信息或示例？
3. 在信息完整后，按照提示词工程最佳实践构建提示词：
   - 使用清晰的结构划分（角色、任务、要求、输出格式、约束等）
   - 语言具体明确，避免模糊
   - 根据任务类型选择合适的提示词技术（CoT、Few-Shot、RAG 等）
   - 确保包含所有必要元素，结构清晰易读

生成要求：
- 生成的提示词要直接可用，复制粘贴就能给目标模型使用
- 使用合理的标题层级和格式划分，便于阅读
- 如果任务适合，可添加示例来提升效果
- 考虑目标模型的特性，调整提示词的写法

记住：在用户需求不明确时，宁可追问，也不要猜测。只有收集到足够信息，才能生成高质量的提示词。"""

# ============ 追问问题列表 ============
FOLLOW_UP_QUESTIONS = [
    ("目标 AI 模型", "这是给哪个 AI 模型使用的提示词？（ChatGPT, Claude, Gemini, DeepSeek, Llama 等）"),
    ("任务类型", "需要完成的具体任务是什么？（创作、分析、编程、问答、总结、推理等）"),
    ("输出格式", "期望的输出格式是什么？（Markdown、JSON、表格、纯文本、代码等）"),
    ("约束条件", "有什么约束条件？（长度、风格、规则、字数限制、禁止内容等）"),
    ("背景信息", "是否需要提供背景信息或示例？（可选，直接回车跳过）"),
]

# ============ 技术选择指南 ============
TECH_GUIDE = {
    "推理": "Chain-of-Thought (CoT) - 要求逐步思考，展示推理过程",
    "事实": "Retrieval-Augmented Generation (RAG) - 注入外部知识，减少幻觉",
    "决策": "Tree of Thoughts (ToT) - 探索多个推理路径，选择最优",
    "工具": "ReAct - 结合推理与行动，支持工具调用",
    "一致": "Self-Consistency - 生成多个结果，选择最一致答案",
    "代码": "结构化输出 + 示例 - 明确输入输出格式，提供代码示例",
    "创意": "角色扮演 + 风格指定 - 定义角色和语气，提供参考风格",
}


def print_header():
    """打印工具标题"""
    print("=" * 60)
    print("  Prompt Engineer CLI - 提示词生成工具")
    print("  根据你的需求，生成专业结构的 AI 提示词")
    print("=" * 60)
    print()


def get_user_input():
    """获取用户初始需求"""
    if len(sys.argv) > 1:
        # 命令行传入需求
        return " ".join(sys.argv[1:])
    else:
        # 交互式输入
        print("请输入你的提示词需求（例如：帮我生成一个写周报的提示词）：")
        return input("> ").strip()


def collect_details():
    """交互式收集关键信息"""
    print("\n为了生成高质量的提示词，我需要确认几个细节：")
    print("-" * 60)

    details = {}
    for key, question in FOLLOW_UP_QUESTIONS:
        print(f"\n[{key}]")
        print(f"  {question}")
        answer = input("  > ").strip()
        if answer:
            details[key] = answer

    return details


def generate_prompt(requirement, details):
    """根据收集的信息生成提示词"""
    # 构建提示词内容
    lines = []
    lines.append("# 角色定位")
    lines.append(f"根据任务需求，定义 AI 的专业角色和领域定位")
    lines.append("")
    lines.append("# 任务目标")
    lines.append(f"{requirement}")
    lines.append("")

    if details.get("背景信息"):
        lines.append("# 背景信息")
        lines.append(f"{details['背景信息']}")
        lines.append("")

    lines.append("# 输出要求")
    if details.get("输出格式"):
        lines.append(f"- 输出格式：{details['输出格式']}")
    else:
        lines.append("- 输出格式：[请指定]")
    if details.get("约束条件"):
        lines.append(f"- 约束条件：{details['约束条件']}")
    lines.append("")

    lines.append("# 约束规则")
    lines.append("- 语言具体明确，避免模糊表述")
    lines.append("- 如果用户信息不足，请指出需要补充的内容")
    lines.append("")

    lines.append("# 示例（可选）")
    lines.append("[根据需要提供 1-3 个示例]")
    lines.append("")

    return "\n".join(lines)


def print_generated_prompt(prompt, requirement, details):
    """打印生成的提示词"""
    print("\n" + "=" * 60)
    print("  生成的提示词")
    print("=" * 60)
    print()
    print("```markdown")
    print(prompt)
    print("```")
    print()

    # 打印技术建议
    print("-" * 60)
    print("技术建议：")
    task_type = details.get("任务类型", "").lower()
    if "推理" in task_type or "逻辑" in task_type or "数学" in task_type:
        print(f"  • {TECH_GUIDE['推理']}")
    elif "代码" in task_type or "编程" in task_type:
        print(f"  • {TECH_GUIDE['代码']}")
    elif "创作" in task_type or "写作" in task_type:
        print(f"  • {TECH_GUIDE['创意']}")
    elif "分析" in task_type or "决策" in task_type:
        print(f"  • {TECH_GUIDE['决策']}")
    else:
        print("  • 根据具体任务，考虑使用 Few-Shot 示例提升效果")
    print()


def save_prompt(prompt, requirement):
    """保存生成的提示词到文件"""
    filename = input("\n是否保存到文件？输入文件名（直接回车跳过）：").strip()
    if filename:
        if not filename.endswith(".md"):
            filename += ".md"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"# 提示词：{requirement}\n\n")
                f.write(prompt)
            print(f"已保存到：{os.path.abspath(filename)}")
        except Exception as e:
            print(f"保存失败：{e}")


def main():
    """主函数"""
    print_header()

    # 获取需求
    requirement = get_user_input()
    if not requirement:
        print("错误：未提供需求描述")
        sys.exit(1)

    print(f"\n需求：{requirement}")

    # 收集详细信息
    details = collect_details()

    # 生成提示词
    prompt = generate_prompt(requirement, details)

    # 打印结果
    print_generated_prompt(prompt, requirement, details)

    # 保存选项
    try:
        save_prompt(prompt, requirement)
    except EOFError:
        pass

    print("\n完成！你可以复制上面的提示词直接使用。")


if __name__ == "__main__":
    main()
