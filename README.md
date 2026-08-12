# anycap-skills

面向 [AnyCap](https://anycap.ai)（agent 能力运行时）的 Claude Code skill 集。由 [@kevinten10](https://github.com/kevinten10) 维护的个人项目，归属 [convergeai-labs](https://github.com/convergeai-labs)。

[English version → README.en.md](README.en.md)

每个 skill 都是 `skills/<name>/` 下的自包含包——按需安装单个即可，互不影响。

<p align="center">
  <img src="assets/pipeline.png" width="640" alt="从草图堆到定稿 logo 的流水线">
</p>

## Skills

### 🎨 [anycap-brand-mark-lab](skills/anycap-brand-mark-lab/SKILL.md)

用 AnyCap 产出经得起真实展示场景考验的品牌标 / 头像——从 brief 到决策板的完整流水线：

```
brief ──▶ 4–6 个构图候选 ──▶ 无文字 vision 门禁
   │              │
   │              └─ 整轮被否？──▶ 换概念空间（绝不打磨被否元素）
   ▼
i2i 换色（一次只动一个变量）
   ▼
64/44/32px 决策板 ──▶ 定稿 ──▶ 交付处理 ──▶ provenance 存档
```

沉淀的实战教训：

- **i2i 换色保构图**——只改颜色时绝不要从文本重抽
- **hex 锚点胜过形容词**——`#22D3EE → #2563EB` 言听计从，"蓝一点"随心所欲
- **整轮被否就换概念空间**，不是换 seed
- **图标模板描边也是门禁失败**——squircle 细边属于 UI trace，必须重生成
- **32px 才是真画布**——只在 1024px 下好看的标不是 logo
- **白角会意外出厂**——发布前把角部 flood-fill 成透明
- **GitHub camo 会缓存图片**——替换 README 图片后记得 `?v=` 破除

已在两个真实定稿上验证：[convergeai-labs 彩虹环](https://github.com/convergeai-labs/anycap-examples/tree/main/entries/2026-08-convergeai-labs-avatar) 与 [kt-aicoding 像素星芒](https://github.com/convergeai-labs/anycap-examples/tree/main/entries/2026-08-kt-aicoding-pixel-spark)。

### 🏗 [anycap-architecture-diagrams](skills/anycap-architecture-diagrams/SKILL.md)

用 AnyCap 产出架构图 / 系统图——事实图优先、标签白名单审计、公开安全前置：

```
事实图脱敏（内部名→公开角色）──▶ 冻结契约（节点/边/标签白名单）
   ▼
选分支：T1 全生成 / 混合（无字底板+确定性标注）/ 退回 Mermaid
   ▼
生成（事实图写进 prompt）──▶ image-read 逐标签审计（不是看感觉）
   ▼
provenance 存档
```

核心纪律：

- **先脱敏事实图再生成**——架构图是浓缩的系统地图，扫描器看不见的泄露它全有
- **审计标签而非氛围**——逐字核对白名单、逐条核对箭头方向
- **一次失败点名重修，两次失败换分支**——别在同一分支上反复抽卡
- 教学/示例图用**合成参考系统**，不用任何真实部署

实证：[RAG 参考架构图](https://github.com/convergeai-labs/anycap-examples/tree/main/entries/2026-08-rag-reference-architecture)（一次生成即通过审计）。

## 安装

把 skill 目录复制到 `~/.claude/skills/`，或者软链：

```bash
ln -s "$PWD/skills/anycap-brand-mark-lab" ~/.claude/skills/anycap-brand-mark-lab
```

## 相关

- 用这些 skill 做出的作品：[anycap-examples](https://github.com/convergeai-labs/anycap-examples)
- 许可证：MIT
