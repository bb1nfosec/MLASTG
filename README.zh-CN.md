# MLSec 应用安全测试指南 (MLASTG)

**面向企业及国防级机器学习系统的安全测试框架**

> **状态:** 积极开发中 — 版本 0.1（草案）
> 
> [![Version](https://img.shields.io/badge/version-0.1--draft-orange)](https://github.com/bb1nfosec/MLASTG)
> [![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE)
> [![Documentation](https://img.shields.io/badge/docs-live-green)](https://mlastg.vercel.app/)

---

[![English](https://img.shields.io/badge/lang-en-blue.svg)](README.md)
[![中文](https://img.shields.io/badge/lang-zh-red.svg)](README.zh-CN.md)

**🌐 我们欢迎国际贡献者！翻译工作正在进行中。**

---

## 概述

**MLSec 应用安全测试指南 (MLASTG)** 是一个全面、开源的安全测试框架，覆盖从传统机器学习分类器到深度神经网络及大语言模型（LLM）的完整威胁全景。

受 **[OWASP 移动应用安全测试指南 (MASTG)](https://github.com/OWASP/MASTG)** 启发，并与 **[MITRE ATLAS](https://atlas.mitre.org/)**、**[NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)** 和 **[OWASP AI Exchange](https://owaspai.org/)** 保持一致，MLASTG 提供：

- **验证标准 (MLASVS)** — 验证什么，按控制类别组织，分为 L1（标准）和 L2（深度防御）两个级别
- **测试指南 (MLASTG)** — 如何测试，提供详细的逐步测试用例映射到对应控制项
- **弱点枚举 (MLASWE)** — 机器学习/大语言模型系统特有的常见安全弱点
- **可执行的测试脚本** — 使用业界标准工具（ART、SecML 等）的 Python 测试工具

---

## 为什么选择 MLASTG？

| 问题 | MLASTG 解决方案 |
|---------|----------------|
| 机器学习安全缺乏标准化、可测试的验证框架 | MLASVS 提供清晰、可验证的控制项，映射到 MITRE ATLAS 技术 |
| 现有指南分散在 OWASP、NIST 和供应商文档中 | 统一的参考框架，整合所有主要框架并添加交叉引用 |
| 对抗性机器学习的测试流程文档不足 | 详细的逐步测试用例配备配套 Python 脚本 |
| 企业/国防环境需要深度防御 | 两层验证体系（L1 标准 / L2 深度防御） |
| 机器学习供应链缺乏 SBOM/SCA 标准 | ML-SBOM 要求和供应链验证控制项 |

---

## 架构

```
MLASVS（标准）                   ─── 验证什么
    │
    ├── 映射至 ───► MITRE ATLAS 战术与技术
    ├── 对齐 ──► NIST AI RMF、OWASP AI Exchange
    └── 被引用 ──► MLASWE 弱点 ID
            │
            ▼
MLASTG（测试指南）               ─── 如何测试
    │
    ├── 测试用例 ──► MLASTG-TEST-XXXX（逐步流程）
    ├── 技术 ──► MLASTG-TECH-XXXX（工具与方法）
    └── 配套脚本 ──► tests/*.py（可执行测试工具）
            │
            ▼
MLASWE（弱点枚举）               ─── 可能出什么问题
    │
    └── 每种弱点类别的 MLASWE-XXXX 标识符
```

---

## 控制类别

| 类别 | ID | 覆盖范围 | L1 控制数 | L2 控制数 |
|----------|----|----------|-------------|--------------|
| 数据安全与隐私 | **MLASVS-DATA** | 数据溯源、清洗、差分隐私、访问控制 | 18 | 12 |
| 模型安全 | **MLASVS-MODEL** | 对抗鲁棒性、模型窃取/反转防护、后门检测 | 15 | 15 |
| 大语言模型安全 | **MLASVS-LLM** | 提示注入、输出处理、代理权限、上下文隔离 | 14 | 10 |
| 供应链安全 | **MLASVS-SUPPLY** | ML-SBOM、基础模型审查、依赖扫描 | 12 | 10 |
| 流水线与 MLOps | **MLASVS-PIPELINE** | CI/CD、特征存储、模型注册库、制品完整性 | 10 | 10 |
| 运行时与基础设施 | **MLASVS-INFRA** | 模型服务安全、API 安全、监控、事件响应 | 12 | 10 |
| 治理与合规 | **MLASVS-GOV** | 风险治理、偏差/公平性、审计日志、法规遵从 | 10 | 10 |

**控制项总数:** 91 L1 + 77 L2 = **168 个可验证控制项**

---

## 快速开始

### 安全测试人员
1. 查阅 **MLASVS** 以确定适用的控制项
2. 使用 **MLASTG 测试方法论** 规划评估
3. 执行映射到目标控制项的测试用例
4. 引用 **MLASWE** 对发现进行弱点分类
5. 运行配套 **测试脚本** 进行自动化验证

### 组织机构
1. 采用 **MLASVS** 作为内部机器学习安全标准
2. 将现有控制项映射到 MLASVS 类别
3. 使用 **MLASTG 检查清单** 进行差距分析
4. 以 L1 为最低标准实施缺失的控制项

---

## 参与贡献

本项目处于积极开发阶段。欢迎各类贡献：
- 新的测试用例和逐步流程
- Python 测试脚本实现（参见 `tests/` 目录）
- 大语言模型安全测试方法和数据集
- 案例研究和真实世界攻击演示
- **翻译和国际化（欢迎中文贡献者！）**（参见 `docs/zh/`）
- 覆盖更多 MLASVS 控制类别的内容

参见 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献指南。

---

## 许可证

本作品采用 **知识共享署名-相同方式共享 4.0 国际许可协议 (CC BY-SA 4.0)**。

---

## 致谢

- **OWASP MASTG** — 本项目灵感和结构模型
- **MITRE ATLAS** — 对抗威胁分类基础
- **NIST AI RMF** — 风险管理框架对齐
- **OWASP AI Exchange** — 交叉引用的威胁与控制矩阵
- **IBM ART** — 对抗鲁棒性测试工具
- 所有人工智能/机器学习安全社区的贡献者
