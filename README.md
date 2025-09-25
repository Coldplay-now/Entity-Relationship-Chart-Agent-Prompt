# 画大图智能体系统提示词使用指南

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![GitHub release](https://img.shields.io/github/v/release/Coldplay-now/Entity-Relationship-Chart-Agent-Prompt)](https://github.com/Coldplay-now/Entity-Relationship-Chart-Agent-Prompt/releases) [![GitHub last commit](https://img.shields.io/github/last-commit/Coldplay-now/Entity-Relationship-Chart-Agent-Prompt)](https://github.com/Coldplay-now/Entity-Relationship-Chart-Agent-Prompt/commits/main) [![GitHub issues](https://img.shields.io/github/issues/Coldplay-now/Entity-Relationship-Chart-Agent-Prompt)](https://github.com/Coldplay-now/Entity-Relationship-Chart-Agent-Prompt/issues) [![GitHub pull requests](https://img.shields.io/github/issues-pr/Coldplay-now/Entity-Relationship-Chart-Agent-Prompt)](https://github.com/Coldplay-now/Entity-Relationship-Chart-Agent-Prompt/pulls) [![Mermaid](https://img.shields.io/badge/Mermaid-FF6F00?style=flat&logo=mermaid&logoColor=white)](https://mermaid.js.org) [![Markdown](https://img.shields.io/badge/Markdown-000000?style=flat&logo=markdown&logoColor=white)](https://daringfireball.net/projects/markdown/) [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com) [![TRAE IDE](https://img.shields.io/badge/TRAE_IDE-FF6F00?style=flat&logo=visualstudiocode&logoColor=white)](https://trae.com) [![Version](https://img.shields.io/badge/Version-V0.1-blue)](https://github.com/Coldplay-now/Entity-Relationship-Chart-Agent-Prompt) [![TRAE IDE](https://img.shields.io/badge/TRAE_IDE-FF6F00?style=flat&logo=visualstudiocode&logoColor=white)](https://trae.com) [![DeepSeek 3.1](https://img.shields.io/badge/DeepSeek_3.1-000000?style=flat&logo=openai&logoColor=white)](https://deepseek.com) [![Prompt Engineering](https://img.shields.io/badge/Prompt_Engineering-8A2BE2?style=flat&logo=bookstack&logoColor=white)](https://github.com/Coldplay-now/Entity-Relationship-Chart-Agent-Prompt)

## 📋 系统概述

本项目是一个提示词工程项目。利用系统提示词构建智能体。画大图智能体是个业务协作关系可视化工具。你与该智能体对话，可以将模糊的业务场景描述，转化为清晰的可视化图表。通过静态关系拓扑图和动态时序交互图，你能更好地理解和分析业务协作关系。

## 🎯 核心功能

- **业务场景分析**：系统化分析复杂业务场景、代码逻辑、业务流程等
- **实体关系梳理**：识别和拆解关键实体和角色
- **Mermaid可视化**：使用Mermaid Graph和Sequence两种语法生成图表
- **双图输出**：同时提供静态拓扑图和动态时序图

### 系统工作流程
```mermaid
graph LR 
     A[用户] -->|1.输入需求| B(画大图智能体) 
     B -->|2.解析业务场景| C[识别关键实体] 
     B -->|3.分析协作关系| D[梳理交互时序] 
     B -->|4.生成双图| E[Graph + Sequence] 
     E -->|5.输出文档| F[Markdown文件] 
     F -->|6.展示结果| A
```

*图：画大图智能体系统工作流程图，展示从用户输入到结果展示的完整交互过程*

## 🚀 快速开始
### 【方法1】在TRAE中配置智能体
![TRAE智能体导入示例](pic/8.png)
*图：在TRAE平台中导入画大图智能体系统的配置界面*

### 系统提示词的安装
拷贝下述内容，在IDE（TRAE ）的智能体中粘贴
```
# 角色定位：您是专业的业务协作关系图专家，专注于将复杂业务场景可视化
## 核心目标：通过系统化分析为用户生成清晰的可视化协作关系图
##能力范围：精通业务场景分析、实体关系梳理、Mermaid语法可视化
## 工作限制：仅使用Mermaid语法，不涉及其他绘图工具或编程语言。不要使用mermaid中ER图格式。
## 执行步骤：
###第一步：主动询问用户具体的业务场景和协作需求
###第二步：首先识别并拆解场景中的关键实体和角色。停下来与用户进行确认。
###第三步：根据用户调整意见，分析实体间的协作关系和交互顺序。与用户进行确认。
###第四步：根据用户的建议和你的分析，你用Mermaid Graph语法绘制静态关系拓扑图，包括实体、关系描述、关系序号
###第五步：用Mermaid Sequence语法绘制动态时序交互图。 
###第六步：将内容输出到项目根目录下md文档中，Relationship_[场景缩写]_v[0.1].md

##输出标准：每次必须同时提供Graph和Sequence两种可视化图表。按照如下章节进行输出
“
1. 业务场景综述
2. 关键实体描述
3. 静态拓扑图
4. 时序图
5. 关节业务关系说明
6. 流程流程描述”
##交互要求：在图表后简要解释关键关系和时序逻辑。主动跟用户澄清实体、关系。
##质量保证：确保图表逻辑清晰、关系准确、布局合理、关系有描述、有序号。
##边界限制：不提供业务建议，仅专注于关系可视化
##启动方式：每次会话首先询问"请描述您需要分析的业务协作场景"
```

### 【方法2】在AI助手中配置智能体
在豆包中，你可以创建「智能体」，拷贝上面的系统提示词即可。
在元宝中，你可创建分组，在分组「指令」中，拷贝上面的系统提示词即可。
![在豆包中示例](pic/7.png)


### 启动方式
每次会话开始时，系统会自动询问：
> "请描述您需要分析的业务协作场景"

或者，如下图，这样开启智能体：
> "请一步步引导我完成画大图的过程"

![画大图智能体启动示例](pic/6.png)
*图：画大图智能体的启动界面，展示如何开始业务协作关系分析*


### 使用步骤

1. **描述业务场景**：详细描述您需要分析的业务协作场景
2. **实体确认**：系统会识别关键实体并与您确认
3. **关系分析**：系统分析实体间的协作关系和交互顺序
4. **图表生成**：系统生成Graph静态拓扑图和Sequence时序图
5. **文档输出**：结果保存为Markdown文档

### 示例输入
```
请分析瑞幸咖啡的线上点单业务流程，包括用户、APP、门店POS系统、咖啡师、取餐柜台之间的协作关系
```


## 📊 输出格式

系统会生成包含以下章节的Markdown文档：

### 1. 业务场景综述
概述分析的业务场景和核心目标

### 2. 关键实体描述
识别并描述场景中的所有关键实体和角色

### 3. 静态拓扑图（Graph）
使用Mermaid Graph语法展示实体间的静态关系，包含：
- 所有业务实体
- 关系描述
- 关系序号

### 4. 时序图（Sequence）
使用Mermaid Sequence语法展示动态交互时序

### 5. 关键业务关系说明
详细解释每个编号关系的具体含义

### 6. 业务流程描述
分阶段描述完整的业务流程

## 📁 文件命名规范

输出文件按照以下格式命名：
```
Relationship_[场景缩写]_v[版本号].md
```

示例：
- `Relationship_LuckinBiz_v0.1.md`
- `Relationship_Meituan_v0.1.md`

## 🛠️ 技术限制

- **仅使用Mermaid语法**：不涉及其他绘图工具或编程语言
- **不包含ER图**：专注于业务协作关系，不使用实体关系图格式
- **业务可视化专注**：不提供业务建议，仅专注于关系可视化

## ✅ 质量保证

系统确保生成的图表具备：
- **逻辑清晰**：关系流向明确易懂
- **关系准确**：真实反映业务协作
- **布局合理**：图表结构美观有序
- **描述完整**：每个关系都有详细说明
- **序号规范**：关系编号系统化

## 📝 交互要求

系统会主动：
- 在关键步骤与用户确认实体和关系
- 澄清模糊或不明确的业务概念
- 简要解释图表中的关键关系和时序逻辑

## 🎨 示例文件

项目包含多个示例文件，可供参考：

### 业务场景示例
- **`Relationship_LuckinBiz_v0.1.md`** - 瑞幸咖啡线上点单业务分析
  - 分析用户、APP、门店POS系统、咖啡师、取餐柜台之间的协作关系
  - 包含完整的下单、制作、取餐业务流程可视化

- **`Relationship_Meituan_v0.1.md`** - 美团外卖业务流程分析  
  - 分析用户、美团APP、商家、骑手、配送系统的多方协作
  - 涵盖下单支付、订单分配、餐品制作、配送送达完整流程

### 技术场景示例
- **`Relationship_QLearning_v0.1.md`** - Q-learning强化学习训练流程分析
  - 可视化GridWorld环境中智能体与环境的协作关系
  - 展示ε-greedy策略、Q表更新、经验收集等技术流程

### 创意场景示例  
- **`Relationship_RNBFuturistic_v0.1.md`** - 未来超现实RNB网页交互分析
  - 分析未来科技风格网页的用户交互和视觉效果协作
  - 包含导航菜单、功能按钮、视觉反馈、动态效果等实体关系

### 示例特点
所有示例文档均遵循标准化输出格式，包含：
- 📋 业务场景综述和核心目标说明
- 👥 关键实体描述和角色定义  
- 🔗 Graph静态拓扑图（含关系描述和序号）
- ⏱️ Sequence动态时序交互图
- 🔑 关键业务关系详细说明
- 📝 完整业务流程分阶段描述

这些示例展示了系统处理不同类型场景的能力，从传统业务到技术算法，再到创意交互场景。

## 🔧 文件结构

```
画大图智能体系统提示词/
├── README.md                          # 本使用指南
├── LICENSE                            # 开源许可证
├── .gitignore                         # Git忽略文件配置
├── 画大图智能体系统提示词.md             # 系统核心提示词
├── example/                          # 示例代码和文档目录
│   ├── q_learning_example.py         # Q学习算法示例代码
│   ├── Relationship_LuckinBiz_v0.1.md    # 瑞幸咖啡业务关系分析
│   ├── Relationship_Meituan_v0.1.md      # 美团业务关系分析
│   ├── Relationship_QLearning_v0.1.md    # Q学习算法关系分析
│   └── Relationship_RNBFuturistic_v0.1.md # 未来主义RNB关系分析
└── pic/                              # 图片资源目录
```


### 成果示例
![画大图生成文档示例](pic/1.png)
![画大图生成文档示例](pic/3.PNG)
![画大图生成文档示例](pic/4.png)


## 💡 最佳实践

1. **详细描述**：提供尽可能详细的业务场景描述
2. **关键实体**：明确场景中的所有参与者和系统
3. **交互流程**：描述完整的业务流程和交互顺序
4. **版本管理**：使用版本号管理不同迭代的分析结果

## 🆘 常见问题

### Q: 系统支持哪些类型的业务场景？
A: 支持任何需要分析协作关系的业务场景，包括但不限于：
- 电商业务流程
- 餐饮点单系统
- 金融服务流程
- 物流配送系统
- 算法协作流程

### Q: 输出的图表如何查看？
A: 生成的Markdown文件支持在支持Mermaid的Markdown查看器中直接渲染图表，如：
- VS Code with Mermaid插件
- GitHub/GitLab
- Typora等Markdown编辑器

### Q: 在AI IDE中如何预览Mermaid图表？
A: 如果您使用AI IDE（如TRAE IDE），可以在IDE的插件市场中搜索安装 **Markdown Preview Mermaid Support** 插件。该插件可以在Markdown预览中直接渲染Mermaid图表，支持几乎所有Mermaid语法，且与VS Code原生Markdown预览无缝集成。

![示例](pic/5.png)

### Q: 是否可以自定义输出格式？
A: 系统采用标准化的输出格式以确保一致性和可读性，但您可以根据需要调整生成文档的具体内容。

## 📞 支持

如有问题或建议，请参考示例文件或提供更详细的业务场景描述。系统会尽力为您生成准确、清晰的可视化分析。

---

*最后更新: 2025/9/25年*  
*画大图智能体系统 - 让复杂业务协作一目了然*