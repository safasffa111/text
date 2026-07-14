# TreeTalk

一个以“问题链路 + 树状结构”组织 AI 对话的桌面应用，帮助用户在追问过程中保留上下文、回溯思路，并将有价值的内容沉淀到知识仓库。

> TreeTalk is a desktop interface for structured AI conversations, question branching, context tracing, and knowledge collection.

## 功能概览

- 以栈和树的方式管理主问题、追问和问题链路
- 支持框选文本后基于父回答继续追问
- 工作台与知识仓库分离，便于探索和沉淀知识
- 支持图片、文件和富文本附件
- 支持 API 模式与浏览器桥接模式
- Electron 桌面应用，当前提供 Windows 与 macOS 构建

## 下载

请前往仓库的 [Releases](../../releases/tag/v0.1.0) 页面下载 `v0.1.0`。

| 平台 | 文件 | SHA-256 |
| --- | --- | --- |
| Windows x64 | `TreeTalk-win-x64-0.1.0.zip` | `48c5e4716656c9f221b8fca99c3a9d435996884b211bfd05b1a66b142cc6fea5` |
| macOS Apple Silicon | `TreeTalk-macOS-Apple-Silicon-0.1.0.zip` | `7aff33888dc152d95dc785b6296b8d6408565ecc6b66f526232e2bdac25154c8` |
| macOS Intel | `TreeTalk-macOS-Intel-0.1.0.zip` | `dac19acc3b7602981149d28e50d2b37e4853e5ab728f3977a889923c56f172d1` |

## 安装

### Windows

1. 下载并解压 `TreeTalk-win-x64-0.1.0.zip`。
2. 运行目录中的 `TreeTalk.exe`。
3. 建议保留整个解压目录，不要只移动单个 EXE 文件。

### macOS

1. 根据 Mac 处理器下载 Apple Silicon 或 Intel 版本。
2. 解压后将 `TreeTalk.app` 拖入“应用程序”。
3. 当前构建未使用 Apple 开发者证书签名，首次启动请右键应用并选择“打开”。
4. 仍被系统拦截时，可运行：

```bash
xattr -dr com.apple.quarantine /Applications/TreeTalk.app
```

macOS 主窗口使用无边框设计，因此不会显示左上角红、黄、绿三个系统按钮；ChatGPT 登录窗口保留原生窗口按钮。

## 从源码构建

当前公开源码是根据 Windows 发布包中保留的应用代码、源码映射和资源恢复出的可构建工程。它完整保留了运行所需的 Electron 主进程、预加载脚本、前端构建产物、测试与 macOS 打包脚本，但不等同于最初开发阶段的 TypeScript/React 原始工程。

环境要求：

- Node.js 20 或更高版本
- npm
- 构建 macOS 应用时需要 macOS

```bash
git clone https://github.com/safasffa111/text.git
cd text/app
npm ci --ignore-scripts
npm test
npm run build:mac
```

macOS 构建结果默认生成在：

```text
release/TreeTalk-darwin-universal/TreeTalk.app
```

## 项目结构

```text
app/                 恢复后的可构建 Electron 工程
docs/                构建、安装与发布说明
checksums/           发布包 SHA-256 校验文件
.github/workflows/   自动测试与 macOS 构建工作流
```

## 数据与隐私

TreeTalk 的工作台、知识仓库和设置数据默认保存在本机。使用第三方模型 API 或浏览器桥接模式时，发送给模型服务的内容受相应服务提供商的条款和隐私政策约束。请不要在未确认服务策略的情况下提交密码、密钥或其他敏感信息。

## 开源协议

本项目以 [MIT License](LICENSE) 开源。打包应用包含 Electron 及其他第三方依赖，这些依赖仍分别遵循其自身许可证。

## 免责声明

TreeTalk 是独立项目，与 OpenAI、ChatGPT 或其他模型服务提供商不存在隶属、授权或背书关系。产品名称和商标归各自权利人所有。

## 参与贡献

欢迎通过 Issue 提交问题、改进建议和兼容性反馈。提交代码前请运行：

```bash
npm test
```
