# 文献计量研究

#### 项目简介：

对“工会维权”领域的文献进行文献计量，分析该领域文献在作者、期刊、研究方向上的分布情况，该领域文献的学科交叉情况，该领域研究方向的变化过程及发展趋势。

#### 研究过程：

从知网上抓取以“工会维权”为主题的文献，获取文献题名、主要责任者、发表杂志、关键词、文章分类号、引用文献和被引文献等数据；对低价值数据进行清洗；数据处理；对数据结果进行可视化呈现并加以分析。

#### 技术栈：

数据抓取：Python；数据存储：Mysql；数据处理：Python；可视化：Echarts（js）/Gephi（社会网络分析与可视化）；理论支撑：文献计量学相关理论。

#### 研究主要成果和结论：

* 研究过程中发现规模以上工业企业的亏损率与文献样本量有一定相关性。如果将亏损率滞后两年（见下图），两者的相关系数较高，约达 0.648。于是，笔者提出一个猜测：工业企业的亏损会影响到工人权利的保障，导致工人通过工会等渠道进行维权，进而使学者更加关注这一领域的研究，而这两次因果传递的时间大致为 2 年。

![样本文献的年代分布图](https://github.com/CnDouglasYoung/Bibliometrics_research/blob/master/%E5%9B%BE%E8%A1%A8/%E6%A0%B7%E6%9C%AC%E6%96%87%E7%8C%AE%E7%9A%84%E5%B9%B4%E4%BB%A3%E5%88%86%E5%B8%83%E5%9B%BE.PNG?raw=true)

* 分散有余而集中不足，期刊分布中相关区期刊的数量相对不足，而作者分布中集中程度严重不足，同时缺乏长期在本领域研究做出可观贡献的核心作者。

* 学科交叉现象明显，工会维权研究中政党及群众组织、劳动法和经济管理三大学科相互交叉、融合，在一定程度上推动了本领域研究的发展、深入。

#### 注：

* “the_main_crawler.py”为数据抓取的主要脚本，其余数据清洗和处理用的脚本在“处理过程”文件夹中。

* 女友是劳动与社会保障专业的，这篇文章来打算俩人共同发表，帮她丰富一下研究经历，但是后来并没有用上。

* 文章仅是从文献学的角度来考量，不清楚此研究中的具体情况，一定有不少错误或不严谨的地方，请大家多多包容。

#### 其他主要图片：

期刊整体分布图：

![期刊整体分布图](https://github.com/CnDouglasYoung/Bibliometrics_research/blob/master/%E5%9B%BE%E8%A1%A8/%E6%9C%9F%E5%88%8A%E6%95%B4%E4%BD%93%E5%88%86%E5%B8%83.png?raw=true)

学科分布旭日图：

![学科分布旭日图](https://github.com/CnDouglasYoung/Bibliometrics_research/blob/master/%E5%9B%BE%E8%A1%A8/%E5%AD%A6%E7%A7%91%E5%88%86%E5%B8%83_2.png?raw=true)

学科交叉情况桑基图：

![学科交叉情况桑基图](https://github.com/CnDouglasYoung/Bibliometrics_research/blob/master/%E5%9B%BE%E8%A1%A8/%E5%AD%A6%E7%A7%91%E4%BA%A4%E5%8F%89%E6%83%85%E5%86%B5%E6%A1%91%E5%9F%BA%E5%9B%BE.png?raw=true)

核心作者网络：

![核心作者网络](https://github.com/CnDouglasYoung/Bibliometrics_research/blob/master/%E5%9B%BE%E8%A1%A8/%E6%A0%B8%E5%BF%83%E4%BD%9C%E8%80%85%E7%BD%91%E7%BB%9C.PNG?raw=true)
