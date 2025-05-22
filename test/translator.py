import uuid
import re


def envs_cover(line: str) -> str:
    """
    将 LaTeX 环境转换为 Markdown 环境
    """
    patterns = {
        # Math Environments
        # Definition
        r'\\begin\{definition\}\s*\{(.+?)\}\s*\\label\s*\{(.+?)\}': r'\1\n:label: \2',  
        r'\\begin\{definition\}\s*\\label\s*\{(.+?)\}': r'`````{prf:definition} \n:label: \1',  
        r'\\begin\{definition\}\s*\{(.+?)\}': r'\1',  
        r'\\begin\{definition\}': '',  
        r'\\end\{definition\}': '',

        # Example
        r'\\begin\{example\}\s*\{(.+?)\}\s*\\label\s*\{(.+?)\}': r'`````{prf:example} \1\n:label: \2',  
        r'\\begin\{example\}\s*\{(.+?)\}': r'`````{prf:example} \1',  
        r'\\begin\{example\}\s*\\label\s*\{(.+?)\}': r'`````{prf:example} \n:label: \1',  
        r'\\begin\{example\}': '`````{prf:example}',  
        r'\\end\{example\}': '`````',

        # Property
        r'\\begin\{property\}\s*\{(.+?)\}\s*\\label\s*\{(.+?)\}': r'`````{prf:property} \1\n:label: \2',  
        r'\\begin\{property\}\s*\\label\s*\{(.+?)\}': r'`````{prf:property} \n:label: \1',  
        r'\\begin\{property\}\s*\{(.+?)\}': r'`````{prf:property} \1',  
        r'\\begin\{property\}': '`````{prf:property}',  
        r'\\end\{property\}': '`````',

        # Problem
        r'\\begin\{problem\}\s*\{(.+?)\}\s*\\label\s*\{(.+?)\}': r'```{admonition} Question \1\n:label: \2',  
        r'\\begin\{problem\}\s*\\label\s*\{(.+?)\}': r'`````{prf:problem} \n:label: \1',  
        r'\\begin\{problem\}\s*\{(.+?)\}': r'```{admonition} Question \1',  
        r'\\begin\{problem\}': '```{admonition} Question',  
        r'\\end\{problem\}': '```',

        # Lemma
        r'\\begin\{lemma\}\s*\{(.+?)\}\s*\\label\s*\{(.+?)\}': r'````` \1\n:label: \2',  
        r'\\begin\{lemma\}\s*\\label\s*\{(.+?)\}': r'`````{prf:lemma} \n:label: \1',  
        r'\\begin\{lemma\}\s*\{(.+?)\}': r'````` \1',  
        r'\\begin\{lemma\}': '`````',  
        r'\\end\{lemma\}': '`````',

        # Theorem
        r'\\begin\{theorem\}\{(.+?)\}\\label\{(.+?)\}': r'``````{prf:theorem} \1' + f'\n' + r':label: \2',
        r'\\begin\{theorem\}\s*\\label\s*\{(.+?)\}': r'`````{prf:theorem} \n:label: \1',  
        r'\\begin\{theorem\}\{(.+?)\}': r'``````{prf:theorem} \1',
        r'\\begin\{theorem\}': '``````{prf:theorem}',
        r'\\end\{theorem\}': '``````',

        # Solve
        r'\\begin\{proof\}': '```{dropdown} Proof',
        r'\\end\{proof\}': '```',
        r'\\begin\{solution\}': '```{dropdown} Solution',
        r'\\end\{solution\}': '```',
        r'\\begin\{remark\}': '```{admonition} Remark',
        r'\\end\{remark\}': '```',

        # Enumerate and Itemize
        r'\\begin\{enumerate\}': '',
        r'\\end\{enumerate\}': '',
        r'\\begin\{itemize\}': '',
        r'\\end\{itemize\}': '',
        r'\\item': '- ',

        # Section
        r'\\section\{(.+?)\}': r'# \1',
        r'\\subsection\{(.+?)\}': r'## \1',
        r'\\subsubsection\{(.+?)\}': r'### \1',

        # Note
        r'\\begin\{note\}': '',
        r'\\end\{note\}': '',

        # Vpsace
        r'\\vspace\{(.+?)\}': '',

        # Bold
        r'\\textbf\{(.+?)\}': r'**\1**',

        # Eqnarray
        r'\\begin\{eqnarray\*\}': r'$$' + f'\n' + r'\\begin\{eqnarray*\}',
        r'\\end\{eqnarray\*\}': r'\\end\{eqnarray*\}' + f'\n' + r'$$',
    }

    for pattern, replacement in patterns.items():
        line = re.sub(pattern, replacement, line)

    return line


def tex_spliter(file_path: str) -> list:
    """
    将 LateX 文件的每一行分割开，以便后续处理，返回一个列表
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip()]


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


def two_dollar(cont: str) -> str:
    """
    为 Markdown 内容中的 $$...$$ 数学公式块前后添加空行。
    确保公式块上下各有一个空行。
    """
    # 1. 在每个匹配的数学公式块（$$...$$）前后插入两个换行符
    # 2. 将三个或更多连续的换行符替换为两个（即一个空行），以整理格式
    # 3. 移除字符串首尾可能存在的多余换行符
    content = re.sub(r"(\$\$.*?\$\$)", r"\n\n\1\n\n", cont, flags=re.DOTALL)
    content = re.sub(r"\n{3,}", r"\n\n", content)
    content = content.strip('\n')
    return content


def main():
    file_name = "Lect07.tex"
    lines = tex_spliter(file_name)
    processed_lines = []
    for line in lines:
        processed_line = envs_cover(line)
        processed_lines.append(processed_line)

    # 先转为 Markdown 格式
    output_md_file = "../Chapter07.md"
    with open(output_md_file, "w", encoding="utf-8") as md_file:
        for proc_line in processed_lines:
            md_file.write(proc_line + "\n")

    # 处理美元符号，保证左右两边有一个空格
    with open("../Chapter07.md", 'r', encoding='utf-8') as infile:
        content = infile.read()
        processed_content = process_text_content(content)
    with open("../Chapter07.md", 'w', encoding='utf-8') as outfile:
        outfile.write(processed_content)

    # 处理双美元符号，保证双美元符号的上下具有一个空行
    with open("../Chapter07.md", 'r', encoding='utf-8') as infile:
        content = infile.read()
        processed_content = two_dollar(content)
    with open("../Chapter07.md", 'w', encoding='utf-8') as outfile:
        outfile.write(processed_content)

    
if __name__ == '__main__':
    main()
