# MLSec 应用安全测试指南

**面向企业及国防级机器学习系统的安全测试**

欢迎查阅 **MLASTG** 中文文档 — 机器学习安全测试的权威开源框架，覆盖传统机器学习、深度学习及大语言模型。

> 🌐 [English](../index.md) | [中文](index.md)

## 核心架构

MLASTG 采用三层架构，与 OWASP MASTG/MASVS/MASWE 模型保持一致：

### 🔷 MLASVS — 验证标准
定义**需要验证什么**，按 7 个控制类别组织，涵盖 168 个可验证控制项。

### 🔶 MLASTG — 测试指南
定义**如何验证**每个控制项，提供详细的逐步测试用例、技术和流程。

### 🔷 MLASWE — 弱点枚举
提供统一的机器学习/大语言模型安全弱点分类体系，用于标准化漏洞分类。

## 文档导航

| 章节 | 描述 |
|---------|-------------|
| [MLASVS 介绍](../MLASVS/0x00-Introduction.md) | 验证标准概述 |
| [测试方法论](../MLASTG/0x00-Testing-Methodology.md) | 如何开展机器学习安全评估 |
| [测试工具](../MLASTG/0x01-Testing-Tools.md) | 工具参考（ART、Giskard 等） |
| [弱点枚举](../MLASWE/0x00-Introduction-Weaknesses.md) | 常见机器学习安全弱点 |
| [检查清单](../checklist.md) | 跟踪评估进度 |

## 框架对齐

MLASTG 与以下行业框架交叉引用：
- **[MITRE ATLAS](https://atlas.mitre.org/)** — 对抗战术与技术
- **[NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)** — 风险管理框架
- **[OWASP AI Exchange](https://owaspai.org/)** — 人工智能安全最佳实践
- **[OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/)** — 大语言模型漏洞目录
- **[EU AI Act](https://artificialintelligenceact.eu/)** — 欧盟人工智能法案合规

## 参与翻译

欢迎中文社区成员参与文档翻译和审校！请查阅 [贡献指南](https://github.com/bb1nfosec/MLASTG/blob/main/CONTRIBUTING.md) 了解详情。
