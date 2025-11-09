## Probability Theory and Mathematical Statistics Web-book

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

