# Probability Theory and Mathematical Statistics Web-book

# ⚠️ 此仓库已迁移

> - **注意：** 本项目已不再在此处维护。所有后续维护都已迁移至新仓库。
> - 👉 **新仓库地址：**[LyuNi-ECNU/pr-webbook](https://github.com/LyuNi-ECNU/pr-webbook)

---

## 版权说明

本项目及其所有相关内容，包括但不限于文本、代码、图像及构建的网站，其版权均归作者所有。

如果您希望使用、复制、修改或分发本项目的任何部分，请务必事先通过电子邮件联系 [lni@dase.ecnu.edu.cn](mailto:lni@dase.ecnu.edu.cn) 以获取授权。

未经许可，任何个人或组织不得将本项目用于商业目的或进行未经授权的传播。

Copyright © 2024 [倪葎]. All rights reserved.

## 环境配置

本项目使用 [uv](https://github.com/astral-sh/uv) 进行包管理，项目基于 Windows 平台构建，若未安装 [uv](https://github.com/astral-sh/uv)，可以使用以下命令一键安装：

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

请在根目录下执行以下命令同步环境：

```bash
uv sync
```

## Build

本项目基于 Jupyter-book V1.0.4 进行构建。

```bash
uv run jupyter-book build docs # 增量构建
uv run jupyter-book build docs --all # 强制重新构建
```

要托管至 Github 平台，请使用以下命令：

```bash
uv run ghp-import -n -p -f docs/_build/html 
```

在 Github 的 Pages 页面应该要选择从分支进行部署，选根目录：

<img src="assets/README/Pasted%20image%2020250708164611.png" width="600" alt="Pasted image 20250708164611.png">


