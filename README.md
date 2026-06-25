# Windows 开机静默启动 BAT

一个适用于 Windows 的轻量 Python 程序。它会运行 `script` 文件夹中的所有 `.bat`
批处理文件，运行过程中不显示命令行窗口，并通过 Windows 通知显示启动结果。

用法很简单：将需要开机静默启动的 `.bat` 文件放到程序的 `script` 目录下即可。
适合平时喜欢随手写一些脚本，并希望它们在开机后自动静默运行的人。

## 功能

- 批量运行 `script` 目录中的 `.bat` 文件
- 运行时隐藏命令行窗口
- 显示托盘图标与 Windows 通知
- 支持通过 Windows 启动目录实现开机自动运行

## 环境要求

- Windows 10 或 Windows 11
- Python 3.8 或更高版本

安装 Python 时建议勾选 **Add Python to PATH**。

## 安装依赖

在项目目录中打开 PowerShell，执行：

```powershell
python -m pip install -r requirements.txt
```

## 使用

1. 把需要运行的 `.bat` 文件放入项目的 `script` 文件夹。
2. 双击 `startup.pyw`，确认程序能够正常启动批处理文件。

## 设置开机启动

1. 右键单击 `startup.pyw`，选择 **创建快捷方式**。
2. 按 `Win + R` 打开“运行”窗口。
3. 输入 `shell:startup` 并按回车。
4. 将刚刚创建的 `startup.pyw` 快捷方式放入打开的启动文件夹。

以后登录 Windows 时，系统就会自动运行本程序。

如果不再需要开机启动，从 `shell:startup` 打开的文件夹中删除该快捷方式即可。

## 项目结构

```text
.
├── startup.pyw       # 程序入口
├── requirements.txt  # Python 依赖
└── script/           # 存放需要启动的 .bat 文件
```

`script` 目录中的 `.bat` 文件默认被 Git 忽略，避免误传私人命令、令牌或本机路径。

## 注意事项

- 程序只扫描 `script` 文件夹的第一层，不会扫描其子文件夹。
- 每次启动都会运行 `script` 文件夹中的全部 `.bat` 文件。
- 批处理文件具有执行系统命令的能力。只运行你了解并信任的脚本。

## 许可证

[MIT](LICENSE)
