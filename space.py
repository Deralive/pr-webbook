import re
import uuid
import os


def process_text_content(text_content: str) -> str:
    """
    处理文本内容，在成对的单美元符号周围添加空格，
    同时忽略双美元符号('$$')作为分隔符。
    '$$'序列被视为文字文本，并且可以出现在有效的'$...$'对内部。
    """

    # 生成一个不太可能出现在文本中的唯一占位符。
    # 此占位符临时替换'$$'，以防止它们被误解为分隔符。
    placeholder = f"__DOUBLE_DOLLAR_PLACEHOLDER_{uuid.uuid4().hex}__"

    # 步骤 1: 通过用占位符替换所有'$$'来保护它们。
    text_with_placeholders = text_content.replace('$$', placeholder)

    # 步骤 2: 查找'$...$'对并在它们周围添加空格。
    # 模式 r'\$(.+?)\$' 匹配:
    #   \$ : 字面美元符号 (起始分隔符)。
    #   (.+?) : 捕获组 1。匹配一个或多个字符，非贪婪。
    #           这是美元符号之间的内容。它必须非空。
    #   \$ : 字面美元符号 (结束分隔符)。
    # 由于'$$'已被占位符替换，此处匹配的任何'$'
    # 在形成对的上下文中实际上都是“单个”美元符号。
    # 内容(.+?)可以包含占位符，允许'$...$'内部有'$$'。
    # 替换字符串 r' $\1$ '在匹配到的对周围添加空格。
    processed_text = re.sub(r'\$(.+?)\$', r' $\1$ ', text_with_placeholders)

    # 步骤 3: 从占位符恢复原始的'$$'序列。
    final_text = processed_text.replace(placeholder, '$$')
    return final_text


def main():
    for file in os.listdir('.'):
        if file.endswith('.md'):
            with open(file, 'r', encoding='utf-8') as infile:
                content = infile.read()
                processed_content = process_text_content(content)
            with open(file, 'w', encoding='utf-8') as outfile:
                outfile.write(processed_content)


if __name__ == '__main__':
    main()
