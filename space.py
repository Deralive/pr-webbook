import re
import uuid

def format_math_spacing(text_content: str) -> str:
    """
    处理 Markdown 文本内容，确保成对的单美元符号 ($) 数学公式周围有空格，
    同时忽略双美元符号 ($$) 的块级公式。
    """
    # 使用一个唯一的占位符来保护双美元符号，避免被错误处理
    placeholder = f"__DOUBLE_DOLLAR_PLACEHOLDER_{uuid.uuid4().hex}__"
    text_with_placeholders = text_content.replace('$$', placeholder)

    def replacer(match):
        # 获取美元符号内的数学公式内容
        content = match.group(1)
        # 去除内容两端的任何已有空白
        content_stripped = content.strip()
        # 在公式两边添加单个空格后重新包裹美元符号
        return f' ${content_stripped}$ '

    # 使用正则表达式查找所有单美元符号包裹的内容，并应用上述替换逻辑
    # re.sub(pattern, repl, string)
    # pattern: r'\$(.+?)\$' 查找非贪婪匹配的 $...$
    processed_text = re.sub(r'\$(.+?)\$', replacer, text_with_placeholders)

    # 将之前保护的双美元符号还原
    final_text = processed_text.replace(placeholder, '$$')

    # 将文本中可能出现的多个连续空格合并为一个，以保持格式整洁
    final_text = re.sub(r' {2,}', ' ', final_text)

    return final_text.strip()


# --- 主程序执行部分 ---
if __name__ == '__main__':
    # 定义输入和输出文件名
    input_md_file = 'Chapter21Section02.md'
    output_md_file = 'Chapter21Section02.md'

    # 读取输入文件的内容
    with open(input_md_file, 'r', encoding='utf-8') as f:
        original_content = f.read()

    # 调用核心函数处理文本
    processed_content = format_math_spacing(original_content)

    # 将处理完成的内容写入到输出文件
    with open(output_md_file, 'w', encoding='utf-8') as f:
        f.write(processed_content)

    print(f"处理完成！结果已保存到 '{output_md_file}'。")

    # 打印处理后的内容以供预览
    print("\n--- 处理后的内容预览 ---\n")
    print(processed_content)