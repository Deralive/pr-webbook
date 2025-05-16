import os
import re
import uuid


def process_text_content(text_content: str) -> str:
    """
    处理文本内容，在成对的单美元符号周围保证正好一个空格，
    忽略双美元符号($$)，双美元符号保持原样。
    """

    placeholder = f"__DOUBLE_DOLLAR_PLACEHOLDER_{uuid.uuid4().hex}__"
    # 保护所有双美元符号
    text_with_placeholders = text_content.replace('$$', placeholder)

    def replacer(match):
        content = match.group(1)
        # 去除内容两端空白
        content_stripped = content.strip()
        return f' ${content_stripped}$ '

    processed_text = re.sub(r'\$(.+?)\$', replacer, text_with_placeholders)

    # 将双美元符号还原
    final_text = processed_text.replace(placeholder, '$$')

    # 用正则替换所有公式外两边连续空格为1个空格
    final_text = re.sub(r'(?<=\S) {2,}(?=\S)', ' ', final_text)
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
