# Contributing to MLASTG

🌐 **We welcome contributors from around the world!**  
**我们欢迎来自世界各地的贡献者！**  
**Nous accueillons les contributeurs du monde entier !**

## What We Need

| Category | Description | Difficulty |
|----------|-------------|------------|
| **Test Cases** | New MLASTG-TEST-XXXX procedures | Medium |
| **Controls** | New MLASVS controls for emerging threats | Medium |
| **Weaknesses** | New MLASWE entries for uncovered attack types | Medium |
| **Scripts** | Python test harness improvements | Medium |
| **Demos** | Example vulnerable ML models | Hard |
| **🌐 Translations** | Docs translation (Chinese, Japanese, Korean, Spanish, etc.) | Easy |

## Translation / 翻译贡献

We especially welcome translation contributions:

1. **Chinese (中文):** Translations into Simplified/Traditional Chinese
2. **Other languages:** Japanese, Korean, Spanish, French, German, Arabic, etc.

**How to contribute translations:**

1. Copy the English `.md` file to `docs/{lang-code}/` directory (e.g., `docs/zh/`)
2. Translate the content while preserving all formatting and links
3. Keep technical terms (MLASTG, MLASVS, MLASWE, MITRE ATLAS) in English
4. Submit a pull request with `[i18n]` prefix in the title

**Translation directories:**
- `docs/zh/` — 简体中文 (Simplified Chinese)
- Add new directories for other languages

## How to Contribute

1. Open an issue to discuss your proposed change
2. Fork the repository
3. Create a feature branch
4. Submit a pull request with clear descriptions

## Standards

- Test cases must follow the MLASTG-TEST-XXXX template format
- Controls must cross-reference MITRE ATLAS and NIST AI RMF
- MLASWE entries must follow the structured template with all sections
- Translations must preserve technical accuracy of security terminology

## Code of Conduct

We are committed to providing a welcoming, inclusive experience for everyone. We follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you agree to uphold its standards of behavior.
