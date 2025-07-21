import os
import uuid
import re


def envs_cover(line: str) -> str:
    """
    将 LaTeX 环境转换为 Markdown 环境

    Notice: 这个环境替换是逐行检测的，这里定义的都是逐行替换的 Pattern.
    """
    patterns = {
        # Comment Ignore
        r'^%.*': '',

        # Math Environments
        # Definition
        r'\\begin\{definition\}\s*\{(.+?)\}\s*\\label\s*\{(.+?)\}': r'\n\1\n: ',
        r'\\begin\{definition\}\s*\\label\s*\{(.+?)\}': r'\n\1\n: ',
        r'\\begin\{definition\}\s*\{(.+?)\}': r'\n\1\n: ',
        r'\\begin\{definition\}': '',
        r'\\end\{definition\}': '',

        # Example
        r'\\begin\{example\}\s*\{(.+?)\}\s*\\label\s*\{(.+?)\}': r'\n`````{prf:example} \1\n:label: \2',
        r'\\begin\{example\}\s*\[(.+?)\]': r'\n`````{prf:example} \1',
        r'\\begin\{example\}\s*\{(.+?)\}': r'\n`````{prf:example} \1',
        r'\\begin\{example\}\s*\\label\s*\{(.+?)\}': r'\n`````{prf:example} \n:label: \1',
        r'\\begin\{example\}': r'\n`````{prf:example}',
        r'\\end\{example\}': r'`````\n',

        # Property
        r'\\begin\{property\}\s*\{(.+?)\}\s*\\label\s*\{(.+?)\}': r'\n`````{prf:property} \1\n:label: \2',
        r'\\begin\{property\}\s*\\label\s*\{(.+?)\}': r'\n`````{prf:property} \n:label: \1',
        r'\\begin\{property\}\s*\{(.+?)\}': r'\n`````{prf:property} \1',
        r'\\begin\{property\}': '\n`````{prf:property}',
        r'\\end\{property\}': '`````\n',

        # Problem
        r'\\begin\{problem\}\s*\{(.+?)\}\s*\\label\s*\{(.+?)\}': r'\n```{admonition} Question \1\n:label: \2',
        r'\\begin\{problem\}\s*\\label\s*\{(.+?)\}': r'\n`````{prf:problem} \n:label: \1',
        r'\\begin\{problem\}\s*\{(.+?)\}': r'\n```{admonition} Question \1',
        r'\\begin\{problem\}': '\n```{admonition} Question',
        r'\\end\{problem\}': '```\n',

        # Lemma
        r'\\begin\{lemma\}\s*\{(.+?)\}\s*\\label\s*\{(.+?)\}': r'\n````` \1\n:label: \2',
        r'\\begin\{lemma\}\s*\\label\s*\{(.+?)\}': r'\n`````{prf:lemma} \n:label: \1',
        r'\\begin\{lemma\}\s*\{(.+?)\}': r'\n````` \1',
        r'\\begin\{lemma\}': '\n`````{prf:lemma}',
        r'\\end\{lemma\}': '`````\n',

        # Theorem
        r'\\begin\{theorem\}\{(.+?)\}\\label\{(.+?)\}': r'\n``````{prf:theorem} \1' + f'\n' + r':label: \2',
        r'\\begin\{theorem\}\s*\\label\s*\{(.+?)\}': r'\n`````{prf:theorem} \n:label: \1',
        r'\\begin\{theorem\}\[(.+?)\]': r'\n``````{prf:theorem} \1',
        r'\\begin\{theorem\}\{(.+?)\}': r'\n``````{prf:theorem} \1',
        r'\\begin\{theorem\}': '\n``````{prf:theorem}',
        r'\\end\{theorem\}': '``````\n',

        # Solve
        r'\\begin\{proof\}': '\n```{dropdown} Proof',
        r'\\end\{proof\}': '```',
        r'\\begin\{solution\}\s*(.*)': '\n```{dropdown} Solution\n\1',
        r'\\end\{solution\}': '```',
        r'\\begin\{remark\}': '\n```{admonition} Remark',
        r'\\end\{remark\}': '```\n',

        # Instance
        r'\\begin\{instance\}': '',
        r'\\end\{instance\}': '',
        r'\\begin\{conclusion\}': '',
        r'\\end\{conclusion\}': '',

        # Cross-ref
        r'\\ref\{(thm:.+?)\}': r' {prf:ref} `\1` ',
        r'\\ref\{(lem:.+?)\}': r' {prf:ref} `\1` ',
        r'\\ref\{(ex:.+?)\}': r' {prf:ref} `\1` ',
        r'\\ref\{(fig:.+?)\}': r' {numref}`\1` ',
        r'\\ref\{(tab:.+?)\}': r' {numref}`\1` ',

        # Enumerate and Itemize
        r'\\begin\{enumerate\}': '',
        r'\\end\{enumerate\}': '',
        r'\\begin\{itemize\}': '',
        r'\\end\{itemize\}': '',
        r'\\item': '- ',

        # Section
        r'\\chapter\{(.+?)\}': r'# \1',
        r'\\section\{(.+?)\}': r'# \1',
        r'\\subsection\{(.+?)\}': r'## \1',
        r'\\subsubsection\{(.+?)\}': r'### \1',

        # Note
        r'\\begin\{note\}': '',
        r'\\end\{note\}': '',

        # Vpsace
        r'\\vspace\{(.+?)\}': '',

        # Newpage
        r'\\newpage': '',

        # Bold
        r'\\textbf\{(.+?)\}': r'**\1**',
        r'\\bm\{(.+?)\}': r'\\mathbf{\1}',

        # Eqnarray
        r'\\begin\{eqnarray\*\}': r'$$' + f'\n' + r'\\begin{eqnarray*}',
        r'\\end\{eqnarray\*\}': r'\\end{eqnarray*}' + f'\n' + r'$$',

        # Introduction
        r'\\begin\{introduction}': r'```{admonition} 教材索引',
        r'\\end\{introduction}': '```',
        r'Intro to Prob': 'Introduction to Probability ',
        r'Prob\s+\\\&\s+Stat': '概率论与数理统计教程',
        r'Prob\s+\$\\\&\$\s+Stat': '概率论与数理统计教程',

        # 中文和英文单词之间添加空格
        r'([\u4e00-\u9fff])([A-Za-z0-9]+)': r'\1 \2',
        r'([A-Za-z0-9]+)([\u4e00-\u9fff])': r'\1 \2',
    }

    for pattern, replacement in patterns.items():
        line = re.sub(pattern, replacement, line)

    if 'Introduction to Probability' in line or '概率论与数理统计教程' in line:
        line = line.replace('\\quad', ' ')

    return line


def tex_spliter(file_path: str) -> list:
    """
    将 LateX 文件的每一行分割开，以便后续处理，返回一个列表
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip()]


def one_dollar_replacer(text_content: str) -> str:
    """
    处理文本内容，在成对的单美元符号周围保证正好一个空格，
    忽略双美元符号($$)，双美元符号保持原样。

    Tips: 由于建立的数学环境通常有多行，故不能使用 Line Pattern 处理。
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


def two_dollar_replacer(cont: str) -> str:
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

def merge_solution_or_proof_into_example_or_theorem(content: str) -> str:
    merge_rules = [
        {
            # 匹配 {prf:example} 块，其后紧跟着一个 Solution 或 Proof 的 dropdown
            "pattern": re.compile(r"(`````\{prf:example\}.*?)\n`````\s*(```\{dropdown\} (?:Solution|Proof).*?\n```)", re.DOTALL),
            "replacement": r"\1\n\2\n`````"
        },
        {
            # 匹配 {prf:theorem} 块，其后紧跟着一个 Solution 或 Proof 的 dropdown
            "pattern": re.compile(r"(``````\{prf:theorem\}.*?)\n``````\s*(```\{dropdown\} (?:Solution|Proof).*?\n```)", re.DOTALL),
            "replacement": r"\1\n\2\n``````"
        },
        {
            # 匹配 {prf:definition} 块，其后紧跟着一个 Solution 或 Proof 的 dropdown
            "pattern": re.compile(r"(`````\{prf:definition\}.*?)\n`````\s*(```\{dropdown\} (?:Solution|Proof).*?\n```)", re.DOTALL),
            "replacement": r"\1\n\2\n`````"
        },
        {
            # 匹配 {prf:property} 块，其后紧跟着一个 Solution 或 Proof 的 dropdown
            "pattern": re.compile(r"(`````\{prf:property\}.*?)\n`````\s*(```\{dropdown\} (?:Solution|Proof).*?\n```)", re.DOTALL),
            "replacement": r"\1\n\2\n`````"
        },
        {
            # 匹配 {prf:problem} 块，其后紧跟着一个 Solution 或 Proof 的 dropdown
            "pattern": re.compile(r"(```\{admonition\} Question.*?)\n```.*?\s*(```\{dropdown\} (?:Solution|Proof).*?\n```)", re.DOTALL),
            "replacement": r"\1\n\2\n```"
        },
    ]

    # 使用 while 循环，反复应用规则，直到内容不再发生变化。
    # 这可以正确处理一个环境块后面跟着多个下拉块的情况 (例如，先 Proof，再 Solution)。
    while True:
        original_content = content
        for rule in merge_rules:
            content = rule["pattern"].sub(rule["replacement"], content)

        if content == original_content:
            break

    return content

def fix_definition_format(content: str) -> str:
    """
    后处理函数，用于修复 definition 环境的格式。
    将 "Title\n: \nContent" 模式转换为 "Title\n: Content"。
    """
    content = re.sub(r'(.*?)\n\s*:\s*\n\s*(.+)', r'\1\n: \2', content, flags=re.DOTALL)
    return content


def process_figure_environments(content: str) -> str:
    """
    处理 LaTeX 的 figure 环境，转换为 Jupyter Book 的 {figure} 指令。
    【已修正】可以处理 \label 在 \caption 内部或外部的情况，并强制要求标签以 "fig:" 开头。
    """
    # 匹配整个 figure 环境块
    figure_block_pattern = re.compile(
        r'(\\begin\{figure\}.*?\\end\{figure\})',
        re.DOTALL
    )

    def replace_figure_block(match):
        figure_block = match.group(1)

        # 1. 从块中独立提取图片路径、标题和标签
        image_match = re.search(r'\\includegraphics(?:\[.*?\])?\{(.+?)\}', figure_block, re.DOTALL)
        caption_match = re.search(r'\\caption\{(.*?)\}', figure_block, re.DOTALL)
        # 【关键修改】在这里的正则表达式中，我们强制要求 label 必须以 "fig:" 开头
        label_match = re.search(r'\\label\{(fig:.+?)\}', figure_block, re.DOTALL)

        # 如果缺少任何关键部分，则不进行转换，返回原文
        if not image_match or not caption_match or not label_match:
            return figure_block

        image_path_raw = image_match.group(1).strip()
        full_caption_content = caption_match.group(1)
        label_name = label_match.group(1)  # 例如 "fig:myfigure"

        # 2. 清理数据
        # 从标题中移除 \label 命令
        caption_text = full_caption_content.replace(f'\\label{{{label_name}}}', '').strip()
        # 不要为 :name: 指令移除 'fig:' 前缀
        transformed_label_name = label_name

        # 处理图片路径
        transformed_image_path = image_path_raw.replace('image/', '/fig/')
        if transformed_image_path.lower().endswith('.pdf'):
            transformed_image_path = transformed_image_path[:-4] + '.png'

        # 3. 构建 figure 指令
        markdown_figure = (
            f'```{{figure}} {transformed_image_path}\n'
            f':name: {transformed_label_name}\n\n'
            f'{caption_text}\n'
            f'```'
        )
        return markdown_figure

    return figure_block_pattern.sub(replace_figure_block, content)


def process_table_environments(content: str) -> str:
    """
    处理 LaTeX 的 table 环境，转换为 Jupyter Book 的 {list-table} 指令。
    【最终修正版】
    1. 可处理 \label 在 \caption 内部或外部的情况，并强制要求 "tab:" 前缀。
    2. 可清理 \toprule, \multicolumn, \cline 等高级 LaTeX 表格命令。
    """
    # 匹配整个 table 环境块
    table_block_pattern = re.compile(
        r'(\\begin\{table\}.*?\\end\{table\})',
        re.DOTALL
    )

    def replace_table_block(match):
        table_block = match.group(1)

        # 1. 从块中独立提取标题、标签和内容
        caption_match = re.search(r'\\caption\{(.*?)\}', table_block, re.DOTALL)
        label_match = re.search(r'\\label\{(tab:.+?)\}', table_block, re.DOTALL)
        tabular_match = re.search(r'\\begin\{tabular\}.*?\}(.*?)\\end\{tabular\}', table_block, re.DOTALL)

        if not caption_match or not label_match or not tabular_match:
            return table_block

        full_caption_content = caption_match.group(1)
        label_name = label_match.group(1)
        tabular_content_raw = tabular_match.group(1).strip()

        # 2. 清理标题和标签 (解决问题1)
        caption_text = full_caption_content.replace(f'\\label{{{label_name}}}', '').strip()
        transformed_label_name = label_name[4:] if label_name.startswith('tab:') else label_name

        # 3. 清理表格内容中的高级 LaTeX 命令 (解决问题2)
        # 移除 \toprule, \midrule, \bottomrule
        cleaned_content = re.sub(r'\\(top|mid|bottom)rule', '', tabular_content_raw)
        # 移除 \cline{...}
        cleaned_content = re.sub(r'\\cline\{.*?\}', '', cleaned_content)
        # 将 \multicolumn{...}{...}{...} 替换为其内容
        cleaned_content = re.sub(r'\\multicolumn\{.+?\}\{.+?\}\{(.+?)\}', r'\1', cleaned_content)
        # 移除遗留的 \hline
        cleaned_content = re.sub(r'\\hline', '', cleaned_content).strip()

        # 4. 解析表格的行和列
        rows = [row.strip() for row in cleaned_content.split(r'\\') if row.strip()]

        markdown_table_rows = []
        header_rows_count = 1

        for row_str in rows:
            # {..} 在 LaTeX 中用于分组，但在我们的内容中不需要，直接移除
            cleaned_row_str = row_str.replace('{', '').replace('}', '')
            cols = [col.strip() for col in cleaned_row_str.split('&')]
            formatted_cols = []
            if cols:
                formatted_cols.append(f'* - {cols[0]}')
                for col in cols[1:]:
                    formatted_cols.append(f'  - {col}')
            markdown_table_rows.append('\n'.join(formatted_cols))

        markdown_table_content = '\n'.join(markdown_table_rows)

        # 5. 构建最终的 list-table
        markdown_table = (
            f'```{{list-table}} {caption_text}\n'
            f':header-rows: {header_rows_count}\n'
            f':name: tab:{transformed_label_name}\n'
            f'{markdown_table_content}\n'
            f'```'
        )
        return markdown_table

    return table_block_pattern.sub(replace_table_block, content)

def process_single_tex_file(input_filename: str, output_dir: str) -> dict:
    """
    处理单个 .tex 文件，将其拆分为章节和节，并返回用于生成目录的文件结构。
    【V3 版逻辑】:
    - 如果有小节，第一个小节的内容写入 ChapterXX.md。
    - 后续小节写入 ChapterXXSectionYY.md。
    - 如果没有小节，所有内容写入 ChapterXX.md。
    """
    if not os.path.exists(input_filename):
        print(f" 文件不存在，跳过: {input_filename}")
        return None

    match = re.search(r'Lect(\d+)', input_filename)
    if not match:
        print(f" 文件名格式不符，跳过: {input_filename}")
        return None
    base_output_name = f"Chapter{match.group(1)}"

    generated_files = []

    lines = tex_spliter(input_filename)
    processed_lines = [envs_cover(line) for line in lines]
    full_content = "\n".join(processed_lines)

    full_content = fix_definition_format(full_content)
    full_content = process_figure_environments(full_content)
    full_content = process_table_environments(full_content)

    section_heading_pattern = r'\n(?=#\s[^#])'
    sections = re.split(section_heading_pattern, full_content)

    preamble_content = ""
    if sections and sections[0].strip() and not sections[0].startswith('# '):
        preamble_content = sections.pop(0).strip()

    if not sections:
        # 情况1: 文件中没有一级标题 (没有小节)
        # 所有内容（包括可能的序言）都写入主文件
        if full_content.strip():
            filepath = f"{output_dir}{base_output_name}.md"
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(full_content)
            generated_files.append(filepath)
        chapter_toc_data = {"file": base_output_name}
    else:
        # 情况2: 文件中有一个或多个一级标题 (有小节)
        # 第一个小节的内容（加上序言）写入主文件
        first_section_content = sections.pop(0)
        main_file_content = (preamble_content + "\n\n" + first_section_content).strip()

        main_filepath = f"{output_dir}{base_output_name}.md"
        with open(main_filepath, "w", encoding="utf-8") as f:
            f.write(main_file_content)
        generated_files.append(main_filepath)

        # 剩余的小节从 Section01 开始命名
        section_files_for_toc = []
        for i, section_content in enumerate(sections, 1):
            if section_content.strip():
                section_base_name = f"{base_output_name}Section{i:02d}"
                section_filepath = f"{output_dir}{section_base_name}.md"
                with open(section_filepath, "w", encoding="utf-8") as f:
                    f.write(section_content.strip())
                generated_files.append(section_filepath)
                section_files_for_toc.append({"file": section_base_name})

        chapter_toc_data = {"file": base_output_name}
        if section_files_for_toc:
            chapter_toc_data["sections"] = section_files_for_toc

    # 对所有生成的文件进行最终的格式化处理
    for file_path in generated_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = one_dollar_replacer(content)
        content = two_dollar_replacer(content)
        content = merge_solution_or_proof_into_example_or_theorem(content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f"  -> 已处理 {len(generated_files)} 个文件。")
    return chapter_toc_data


def generate_toc_yml(chapters_data: list, output_file: str):
    """
    根据处理好的章节数据，生成完整的 _toc.yml 文件。
    """
    # 基于用户示例，硬编码第1-7章的结构
    yml_content = """# 目录
# Learn more at [https://jupyterbook.org/customize/toc.html](https://jupyterbook.org/customize/toc.html)

format: jb-book
root: intro
parts:
  - caption: 概率部分
    numbered: True
    chapters:
    - file: Chapter01
      sections:
      - file: Chapter01Section01
      - file: Chapter01Section02
      - file: Chapter01Section03
      - file: Chapter01Section04
      - file: Chapter01Section05
      - file: Chapter01Section06
    - file: Chapter02
      sections:
      - file: Chapter02Section01
      - file: Chapter02Section02
      - file: Chapter02Section03
      - file: Chapter02Section04
      - file: Chapter02Section05
      - file: Chapter02Section06
      - file: Chapter02Section07
    - file: Chapter03
      sections:
      - file: Chapter03Section01
      - file: Chapter03Section02
    - file: Chapter04
      sections:
      - file: Chapter04Section01
      - file: Chapter04Section02
      - file: Chapter04Section03
      - file: Chapter04Section04
      - file: Chapter04Section05
      - file: Chapter04Section06
    - file: Chapter05
      sections:
      - file: Chapter05Section01
      - file: Chapter05Section02
      - file: Chapter05Section03
      - file: Chapter05Section04
    - file: Chapter06
      sections:
      - file: Chapter06Section01
      - file: Chapter06Section02
      - file: Chapter06Section03
      - file: Chapter06Section04
      - file: Chapter06Section05
      - file: Chapter06Section06
      - file: Chapter06Section07
      - file: Chapter06Section08
"""

    # 动态构建并追加新处理的章节 (07-24)
    for chapter in chapters_data:
        yml_content += f"    - file: {chapter['file']}\n"
        if "sections" in chapter and chapter["sections"]:
            yml_content += "      sections:\n"
            for section in chapter["sections"]:
                yml_content += f"      - file: {section['file']}\n"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(yml_content)

    print(f"\n✅ 成功生成目录文件: {output_file}")


def process_simple_tex_file(input_filename: str, output_filename: str):
    """
    对单个简单的 .tex 文件进行基础处理，并保存为 .md 文件。
    处理流程:
    1. 逐行应用 envs_cover 中的正则替换。
    2. 对全文应用 one_dollar_replacer。
    3. 对全文应用 two_dollar_replacer。
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"  ❌ 文件未找到: {input_filename}")
        return

    # 1. 逐行应用基础正则替换
    processed_lines = [envs_cover(line.strip()) for line in lines]
    full_content = "\n".join(processed_lines)

    # 2. & 3. 应用美元符号格式化
    content_after_one_dollar = one_dollar_replacer(full_content)
    final_content = two_dollar_replacer(content_after_one_dollar)

    # 确保输出目录存在
    output_dir = os.path.dirname(output_filename)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # 写入到输出文件
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(final_content)

    print(f"  ✅ 简单处理完成，已保存至: {output_filename}")


# ---------------------------------------------------------------------------
# Part 3: 主函数 - 流程控制器
# ---------------------------------------------------------------------------

def main():
    """
    主函数，用于批量处理 Lect08.tex 到 Lect24.tex，并生成 _toc.yml。
    """
    output_dir = "../"
    toc_file_path = f"{output_dir}_toc.yml"
    all_chapters_data = []

    for i in range(7, 25):
        input_filename = f"Lect{i:02d}.tex"
        print(f"🚀 正在处理 {input_filename}...")

        chapter_data = process_single_tex_file(input_filename, output_dir)

        if chapter_data:
            all_chapters_data.append(chapter_data)

    if all_chapters_data:
        generate_toc_yml(all_chapters_data, toc_file_path)
    else:
        print("️ 没有文件被成功处理，无法生成 _toc.yml。")

def main2():
    """
    主函数 2，用于处理单个文件
    """
    input_filename = "temp.tex"
    output_dir = "../temp.md"
    print(f"🚀 正在处理 {input_filename}...")

    process_simple_tex_file(input_filename, output_dir)


if __name__ == '__main__':
    main2()