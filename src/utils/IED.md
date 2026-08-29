# 电动力学导论

INTRODUCTION TO ELECTRODYNAMICS (4th Edition)

![](images/7d6826fea511063733793db49a1075c572c65f050b1809855b4836d0435fe3e9.jpg)

（美）大卫·J.格里菲斯（David J. Griffiths）著

贾瑜 张鹏飞 译

## 矢量微分

## 直角坐标系

$$
\mathrm{d} \pmb {l} = \mathrm{d} x \hat {\pmb {x}} + \mathrm{d} y \hat {\pmb {y}} + \mathrm{d} z \hat {\pmb {z}}; \quad \mathrm{d} \tau = \mathrm{d} x \mathrm{d} y \mathrm{d} z
$$

梯度：

$$
\nabla t = \frac {\partial t}{\partial x} \hat {\pmb {x}} + \frac {\partial t}{\partial y} \hat {\pmb {y}} + \frac {\partial t}{\partial z} \hat {\pmb {z}}
$$

散度：

$$
\nabla \cdot \boldsymbol {v} = \frac {\partial v _ {x}}{\partial x} + \frac {\partial v _ {y}}{\partial y} + \frac {\partial v _ {z}}{\partial z}
$$

旋度：

$$
\nabla \times \boldsymbol {v} = \left(\frac {\partial v _ {z}}{\partial y} - \frac {\partial v _ {y}}{\partial z}\right) \hat {\boldsymbol {x}} + \left(\frac {\partial v _ {x}}{\partial z} - \frac {\partial v _ {z}}{\partial x}\right) \hat {\boldsymbol {y}} + \left(\frac {\partial v _ {y}}{\partial x} - \frac {\partial v _ {x}}{\partial y}\right) \hat {\boldsymbol {z}}
$$

拉普拉斯算子：

$$
\nabla^ {2} t = \frac {\partial^ {2} t}{\partial x ^ {2}} + \frac {\partial^ {2} t}{\partial y ^ {2}} + \frac {\partial^ {2} t}{\partial z ^ {2}}
$$

球坐标系

$$
\mathrm{d} \pmb {l} = \mathrm{d} r \hat {\pmb {r}} + r \mathrm{d} \theta \hat {\pmb {\theta}} + r \sin \theta \mathrm{d} \phi \hat {\phi}; \quad \mathrm{d} \tau = r ^ {2} \sin \theta \mathrm{d} r \mathrm{d} \theta \mathrm{d} \phi
$$

梯度：

$$
\nabla t = \frac {\partial t}{\partial r} \hat {\pmb {r}} + \frac {1}{r} \frac {\partial t}{\partial \theta} \hat {\pmb {\theta}} + \frac {1}{r \sin \theta} \frac {\partial t}{\partial \phi} \hat {\phi}
$$

散度：

$$
\nabla \cdot \boldsymbol {v} = \frac {1}{r ^ {2}} \frac {\partial}{\partial r} \left(r ^ {2} v _ {r}\right) + \frac {1}{r \sin \theta} \frac {\partial}{\partial \theta} \left(\sin \theta v _ {\theta}\right) + \frac {1}{r \sin \theta} \frac {\partial v _ {\phi}}{\partial \phi}
$$

旋度：

$$
\nabla \times \boldsymbol {v} = \frac {1}{r \sin \theta} \left[ \frac {\partial}{\partial \theta} (\sin \theta v _ {\phi}) - \frac {\partial v _ {\theta}}{\partial \phi} \right] \hat {\boldsymbol {r}} +
$$

$$
\frac {1}{r} \left[ \frac {1}{\sin \theta} \frac {\partial v _ {r}}{\partial \phi} - \frac {\partial}{\partial r} (r v _ {\phi}) \right] \hat {\pmb {\theta}} + \frac {1}{r} \left[ \frac {\partial}{\partial r} (r v _ {\theta}) - \frac {\partial v _ {r}}{\partial \theta} \right] \hat {\pmb {\phi}}
$$

拉普拉斯算子：

$$
\nabla^ {2} t = \frac {1}{r ^ {2}} \frac {\partial}{\partial r} \left(r ^ {2} \frac {\partial t}{\partial r}\right) + \frac {1}{r ^ {2} \sin \theta} \frac {\partial}{\partial \theta} \left(\sin \theta \frac {\partial t}{\partial \theta}\right) + \frac {1}{r ^ {2} \sin^ {2} \theta} \frac {\partial^ {2} t}{\partial \phi^ {2}}
$$

柱坐标系

$$
\mathrm{d} \pmb {l} = \mathrm{d} s \hat {\pmb {s}} + s \mathrm{d} \phi \hat {\phi} + \mathrm{d} z \hat {\pmb {z}}; \qquad \mathrm{d} \tau = s \mathrm{d} s \mathrm{d} \phi \mathrm{d} z
$$

梯度：

$$
\nabla t = \frac {\partial t}{\partial s} \hat {s} + \frac {1}{s} \frac {\partial t}{\partial \phi} \hat {\phi} + \frac {\partial t}{\partial z} \hat {z}
$$

散度：

旋度：

$$
\nabla \cdot \boldsymbol {v} = \frac {1}{s} \frac {\partial}{\partial s} (s v _ {s}) + \frac {1}{s} \frac {\partial v _ {\phi}}{\partial \phi} + \frac {\partial v _ {z}}{\partial z}
$$

$$
\nabla \times \pmb {v} = \left[ \frac {1}{s} \frac {\partial v _ {z}}{\partial \phi} - \frac {\partial v _ {\phi}}{\partial z} \right] \hat {s} + + \left[ \frac {\partial v _ {s}}{\partial z} - \frac {\partial v _ {z}}{\partial s} \right] \hat {\phi} + \frac {1}{s} \left[ \frac {\partial}{\partial s} (s v _ {\phi}) - \frac {\partial v _ {s}}{\partial \phi} \right] \hat {z}
$$

拉普拉斯算子：

$$
\nabla^ {2} t = \frac {1}{s} \frac {\partial}{\partial s} \left(s \frac {\partial t}{\partial s}\right) + \frac {1}{s ^ {2}} \frac {\partial^ {2} t}{\partial \phi^ {2}} + \frac {\partial^ {2} t}{\partial z ^ {2}}
$$

真空介电常数： $\varepsilon_0 = 8.85\times 10^{-12}\mathrm{C}^2 /\left(\mathrm{N}\cdot \mathrm{m}^2\right)$

真空磁导率： $\mu_0 = 4\pi \times 10^{-7}\mathrm{N / A^2}$

光速： $c = 3.00\times 10^{8}\mathrm{m / s}$

电子电荷： $e=1.60\times10^{-19}C$

电子质量： $m = 9.11\times 10^{-31}\mathrm{kg}$

球坐标系与柱坐标系

球坐标系

$$
\left\{ \begin{array}{l l} x = r \sin \theta \cos \phi \\ y = r \sin \theta \sin \phi \\ z = r \cos \theta \\ \left\{ \begin{array}{l l} r = \sqrt {x ^ {2} + y ^ {2} + z ^ {2}} \\ \theta = \arctan \left(\sqrt {x ^ {2} + y ^ {2}} / z\right) \\ \phi = \arctan (y / x) \end{array} \right. \end{array} \right.
$$

$$
\left\{ \begin{array}{l l} \hat {\pmb {x}} = \sin \theta \cos \phi \hat {\pmb {r}} + \cos \theta \cos \phi \hat {\pmb {\theta}} - \sin \phi \hat {\pmb {\phi}} \\ \hat {\pmb {y}} = \sin \theta \sin \phi \hat {\pmb {r}} + \cos \theta \sin \phi \hat {\pmb {\theta}} + \cos \phi \hat {\pmb {\phi}} \\ \hat {\pmb {z}} = \cos \theta \hat {\pmb {r}} - \sin \theta \hat {\pmb {\theta}} \\ \left\{ \begin{array}{l l} \hat {\pmb {r}} = \sin \theta \cos \phi \hat {\pmb {x}} + \sin \theta \sin \phi \hat {\pmb {y}} + \cos \theta \hat {\pmb {z}} \\ \hat {\pmb {\theta}} = \cos \theta \cos \phi \hat {\pmb {x}} + \cos \theta \sin \phi \hat {\pmb {y}} - \sin \theta \hat {\pmb {z}} \\ \hat {\phi} = - \sin \phi \hat {\pmb {x}} + \cos \phi \hat {\pmb {y}} \end{array} \right. \end{array} \right.
$$

柱坐标系

$$
\left\{ \begin{array}{l l} x = s \cos \phi \\ y = s \sin \phi \\ z = z \\ \left\{ \begin{array}{l l} s = \sqrt {x ^ {2} + y ^ {2}} \\ \phi = \arctan (y / x) \\ z = z \end{array} \right. \end{array} \right.
$$

$$
\left\{ \begin{array}{l l} \hat {\pmb {x}} = \cos \phi \hat {\pmb {s}} - \sin \phi \hat {\phi} \\ \hat {\pmb {y}} = \sin \phi \hat {\pmb {s}} + \cos \phi \hat {\phi} \\ \hat {\pmb {z}} = \hat {\pmb {z}} \\ \left\{ \begin{array}{l l} \hat {\pmb {s}} = \cos \phi \hat {\pmb {x}} + \sin \phi \hat {\pmb {y}} \\ \hat {\phi} = - \sin \phi \hat {\pmb {x}} + \cos \phi \hat {\pmb {y}} \\ \hat {\pmb {z}} = \hat {\pmb {z}} \end{array} \right. \end{array} \right.
$$

## 矢量恒等式

## 三重积

(1) $A \cdot (B \times C) = B \cdot (C \times A) = C \cdot (A \times B)$

(2) $A \times (B \times C) = B(C \cdot A) - C(A \cdot B)$

## 积规则

(3) $\nabla (fg) = f(\nabla g) + g(\nabla f)$

(4) $\nabla (\mathbf{A}\cdot \mathbf{B}) = \mathbf{A}\times (\nabla \times \mathbf{B}) + \mathbf{B}\times (\nabla \times \mathbf{A}) + (\mathbf{A}\cdot \nabla)\mathbf{B} + (\mathbf{B}\cdot \nabla)\mathbf{A}$

(5) $\nabla \cdot (f\mathbf{A}) = f(\nabla \cdot \mathbf{A}) + \mathbf{A} \cdot (\nabla f)$

(6) $\nabla \cdot (\mathbf{A} \times \mathbf{B}) = \mathbf{B} \cdot (\nabla \times \mathbf{A}) - \mathbf{A} \cdot (\nabla \times \mathbf{B})$

(7) $\nabla \times (f\mathbf{A}) = f(\nabla \times \mathbf{A}) - \mathbf{A} \times (\nabla f)$

(8) $\nabla \times (\mathbf{A} \times \mathbf{B}) = (\mathbf{B} \cdot \nabla) \mathbf{A} - (\mathbf{A} \cdot \nabla) \mathbf{B} + \mathbf{A}(\nabla \cdot \mathbf{B}) - \mathbf{B}(\nabla \cdot \mathbf{A})$

二阶导数

(9) $\nabla \cdot (\nabla \times \mathbf{A}) = 0$

(10) $\nabla \times (\nabla f) = 0$

(11) $\nabla \times (\nabla \times A) = \nabla (\nabla \cdot A) - \nabla^2 A$

## 基本定理

梯度定理： $\int_{a}^{b}(\nabla f)\cdot \mathrm{d}\pmb {l} = f(\pmb {b}) - f(\pmb {a})$

散度定理： $\int (\nabla \cdot A)\mathrm{d}\tau = \oint A\cdot \mathrm{d}a$

旋度定理： $\int (\nabla \times \mathbf{A})\cdot \mathrm{d}\mathbf{a} = \oint \mathbf{A}\cdot \mathrm{d}\mathbf{l}$

麦克斯韦方程组

一般形式

介质中

$$
\left\{ \begin{array}{l l} \nabla \cdot \pmb {E} = \frac {1}{\varepsilon_ {0}} \rho \\ \nabla \times \pmb {E} = - \frac {\partial \pmb {B}}{\partial t} \\ \nabla \cdot \pmb {B} = 0 \\ \nabla \times \pmb {B} = \mu_ {0} \pmb {J} + \mu_ {0} \varepsilon_ {0} \frac {\partial \pmb {E}}{\partial t} \end{array} \right. \quad \left\{ \begin{array}{l l} \nabla \cdot \pmb {D} = \rho_ {\mathrm{f}} \\ \nabla \times \pmb {E} = - \frac {\partial \pmb {B}}{\partial t} \\ \nabla \cdot \pmb {B} = 0 \\ \nabla \times \pmb {H} = J _ {\mathrm{f}} + \frac {\partial \pmb {D}}{\partial t} \end{array} \right.
$$

辅助场

$$
\left\{ \begin{array}{l l} {{\boldsymbol {D} = \varepsilon_ {0} \boldsymbol {E} + \boldsymbol {P}}} \\ {{\boldsymbol {H} = \frac {1}{\mu_ {0}} \boldsymbol {B} - \boldsymbol {M}}} \end{array} \right. \quad \left\{ \begin{array}{l l} {{\boldsymbol {P} = \varepsilon_ {0} \chi_ {\mathrm{e}} \boldsymbol {E}, \quad \boldsymbol {D} = \varepsilon \boldsymbol {E}}} \\ {{\boldsymbol {M} = \chi_ {\mathrm{m}} \boldsymbol {H}, \quad \boldsymbol {H} = \frac {1}{\mu} \boldsymbol {B}}} \end{array} \right.
$$

势

$$
\boldsymbol {E} = - \nabla V - \frac {\partial \boldsymbol {A}}{\partial t}, \quad \boldsymbol {B} = \nabla \times \boldsymbol {A}
$$

洛伦兹力定律

$$
\boldsymbol {F} = q (\boldsymbol {E} + \boldsymbol {v} \times \boldsymbol {B})
$$

能量、动量和功率

能量：

$$
U = \frac {1}{2} \int \left(\varepsilon_ {0} E ^ {2} + \frac {1}{\mu_ {0}} B ^ {2}\right) \mathrm{d} \tau
$$

动量：

$$
\pmb {P} = \varepsilon_ {0} \int (\pmb {E} \times \pmb {B}) \mathrm{d} \tau
$$

坡印亭矢量：

$$
\boldsymbol {S} = \frac {1}{\mu_ {0}} (\boldsymbol {E} \times \boldsymbol {B})
$$

拉莫尔公式：

$$
P = \frac {\mu_ {0}}{6 \pi c} q ^ {2} a ^ {2}
$$

# 时代教育·国外高校优秀教材精选

# 电动力学导论

(翻译版·原书第4版)

[美]大卫·J. 格里菲斯（David J. Griffiths）著
贾瑜 张鹏飞 译

![](images/9619e07531733275d39f5d314694d2982480a35ad78d2549bafda4c09a6af16f.jpg)

机械工业出版社

本书是一本立足本科生水平的电动力学教材，主要阐述电磁场理论，分析各个实验定律，从中总结出电磁场的普遍规律，建立麦克斯韦方程组和洛伦兹力公式，讨论恒定电磁场问题，说明一些恒定场的基本性质和求解电场、磁场问题的一些基本方法，讨论电磁波的传播与辐射，介绍一般情况下势的概念和辐射电磁场的计算方法，最后将电动力学的参考系引入相对论时空观，导出电磁场量在不同参考系间的变换，并且说明相对论力学的基本概念。本书注重把现代物理前沿引入教学，把电动力学问题扩展到多个前沿的研究领域，如固体物理、天体物理、核物理、计算物理等。

本书涵盖我国高校物理学专业电动力学课程的基本内容，可作为高等学校物理学相关专业低年级学生学习电动力学课程的教材或参考书，也可作为电子、材料、通信等专业高年级学生的教学参考书。

This is a Simplified Chinese Translation of the following title published by Cambridge University Press:

Introduction to Electrodynamics, Fourth edition, 9781108420419

© Cambridge University Press 2017

This Simplified Chinese Translation for the People's Republic of China (excluding Hong Kong, Macau and Taiwan) is published by arrangement with the Press Syndicate of the University of Cambridge, Cambridge, United Kingdom.

© China Machine Press 2025

This Simplified Chinese Translation is authorized for sale in the People's Republic of China (excluding Hong Kong, Macau and Taiwan) only. Unauthorized export of this Simplified Chinese Translation is a violation of the Copyright Act. No part of this publication may be reproduced or distributed by any means, or stored in a database or retrieval system, without the prior written permission of Cambridge University Press and China Machine Press.

Copies of this book sold without a Cambridge University Press sticker on the cover are unauthorized and illegal.

本书封面贴有 Cambridge University Press 防伪标签，无标签者不得销售。

北京市版权局著作权合同登记 图字：01-2019-7255 号。

图书在版编目（CIP）数据

电动力学导论：翻译版：原书第4版 / (美) 大卫·J. 格里菲斯 (David J. Griffiths)

著；贾瑜，张鹏飞译.--北京：机械工业出版社,2025.4.--(时代教育).

ISBN 978-7-111-77810-3

I. O442

中国国家版本馆 CIP 数据核字第 2025EF3948 号

机械工业出版社（北京市百万庄大街22号 邮政编码100037）

策划编辑：张金奎 责任编辑：张金奎 汤嘉

责任校对：张爱妮 刘雅娜 责任印制：任维东

北京瑞禾彩色印刷有限公司印刷

2025年5月第1版第1次印刷

184mm×260mm·34.5印张·2插页·753千字

标准书号：ISBN 978-7-111-77810-3

定价：168.00元

电话服务

网络服务

客服电话：010-88361066

机工官网：www.cmpbook.com

010-88379833

机工官博：weibo.com/cmp1952

010-68326294

金书网：www.golden-book.com

封底无防伪标均为盗版

机工教育服务网：www.cmpedu.com

## 译者序

本书译自大卫·J. 格里菲斯教授所著《电动力学导论》(第 4 版)。格里菲斯教授是美国著名物理教育学家，他善于以风趣而睿智的风格结合实际问题讲述知识要点，曾编写了多部优秀的本科生教材。这些教材被许多美国著名高校以及其他国家的高校所使用。格里菲斯教授所著《电动力学导论》以清晰易懂的方式介绍了经典电动力学的基本理论，其基本内容十分契合我国高校本科物理学专业电动力学课程的教学要求，非常适合作为我国高校物理学及相关专业的电动力学课程的教材。《电动力学导论》(第 4 版)的英文注释版已在我国发行，深受广大读者的欢迎，许多读者希望见到中译本，应读者的要求，机械工业出版社在第 3 版中译本的基础上再次组织了翻译书版。

电动力学是介绍电磁场基本规律的理论课程，不仅是大学本科物理学及相关专业的一门核心课程，也是电子类工科各专业的基础课程，在通信、微电子、超导、电工等许多领域有具体实际的应用。因此，适当引进翻译适合我国本科教学的国外著名教材对促进我国本科教学的现代化和新工科的建设是十分必要的。

格里菲斯教授所著《电动力学导论》有如下特点：

（1）立足于“电磁理论的入门水平”，不仅包含了电动力学主要的内容，而且融合了物理学专业“电磁学”课程的部分基础内容，使读者对电磁场理论的发展由来有更清晰的把握。本书强调对实验基础和基本概念的理解，而不是把物理概念湮灭在复杂的数学公式推导之中；作者在叙述上采用对话式的语言，叙述简明，文笔流畅，十分有利于初学者自学。

（2）作者不仅仅局限于基本内容的讲授，如同他的另一部著作《量子力学概论》一样，精选了很多具体实际问题，通过这些问题的讨论让读者从中真正体会到电动力学的精髓，掌握电动力学的基本概念和基本理论。比如作者对磁力不做功、电磁场动量等的解释，以及通过大量例题对泊松方程、镜像法求解方法的讲述都独具特色，这样的处理能够引导学生迅速地“入门上手”。

（3）作者精选了大量有启发性的习题来训练学生，这些习题源自目前研究领域前沿的一些新进展和新发现，体现了教材的现代性。特别是通过把一些新的电动力学的内容在习题中加以体现，使得本书在充分考虑了电动力学内容现代化的同时，也保证了电动力学的主线更加清晰，同时前后内容的连接更加密切。这不仅可以培养学生独立思考和独立解决问题的能力，而且能更好地培养学生的创新思维。此外，作者在习题选择上特别下功夫。习题分为基本和深入两个层次，可供不同目的和基础的学生选择，有利于学生的学习。

尽管目前我国已经出版有不少优秀的电动力学教材，也有一些翻译的国外优秀名著，但是译者认为，格里菲斯教授《电动力学导论》的翻译出版还是十分有益的，它可以开阔我们的眼界，从风格各异的教材中取长补短，深化我们对电动力学课程学习及教学的改进。

本书的 1～6 章由郑州大学贾瑜教授翻译，7～12 章由中国科学技术大学张鹏飞教授翻译。附录、索引等由贾瑜翻译整理。在翻译过程中，对书中的物理学名词术语按照 2019 年出版的《物理学名词》译出，对我国读者熟悉的科学家人名直接给出中译名，对某些不常见的外国人名采取音译并给出英文名。作者给出了很多有教益的脚注，为了使读者能够方便地查阅脚注所给出的参考文献，脚注中的人名、期刊名称和出版社名称不做翻译。由于时间非常紧，加之译者水平有限，不妥或错误之处，敬请广大读者批评指正，以便重印时改正。

本书从翻译策划到最后完稿，机械工业出版社张金奎编审给予了很大的帮助和支持。在翻译成稿过程中，贾瑜得到了郑州大学物理工程学院陈刚教授、王杰芳教授、胡行教授、孙强教授以及河南大学纳米科学与材料工程学院杜祖亮教授多次给予的帮助和指导；张鹏飞得到了中国科学技术大学多位老师的帮助。在此，对他们表示感谢！

译者

2024年11月

这是一本关于电磁的教科书，适合于大学本科三年级或四年级的学生。教师可以在两个学期内轻松讲完，甚至还可以有一些剩余时间讲授其他专题（如 AC 电路、数值方法、等离子体物理、传输线、天线理论等）。若该课程仅为一个学期的，可以只讲前七章的内容。与量子力学或热物理不同，电动力学的教学有相当普遍一致的共识。例如，应当包含什么内容，甚至连讲解的次序，都没有什么分歧，教科书的区别仅在于各自的风格和基调上。与大多数人相比，我的写法更加自由一些；我认为这可使难点变得更加有趣和易接受。

我在本书第 4 版中做了大量的小的修改，以使内容更清晰和优美。我纠正了书中一些地方明显的错误，添加了一些问题和例子（并删除了一些效果不佳的例子）。我也增加了更多的可查参考文献（特别是发表在 American Journal of Physics 期刊上的）。当然，我知道大多数的读者没有时间或者不喜欢去查阅这些文献，但是我还是认为这是值得的。要强调的是，尽管电动力学历史悠久，但它仍然是一门非常有活力的学科，有趣的新发现层出不穷。我希望也许有些问题可以激发你的好奇心，促使你查阅文献——其中一些确实是珍宝。

我保留了三个不太规范的记号：

\- 直角坐标系的单位矢量写作 $\hat{x},\hat{y},\hat{z}$ （一般来说，所有单位矢量都由相应坐标的粗体字母表示）。

\- 用 $s$ 表示柱坐标系下点到 $z$ 轴的距离，以便和 $r$ （表示球坐标系下到原点的距离）所表示的含义区分开来。

\- 字母 $\pmb{z}$ 记作从源点 $r'$ 到场点 $r$ 的矢量。一些作者倾向于用更加明显的量 $r - r'$ 表示。但这将使很多方程变得很烦琐，特别是涉及单位矢量 $\hat{\pmb{z}}$ 时。我自己意识到粗心的学生总把 $\pmb{z}$ 当作 $r$ ——这显然会使积分容易！请记住： $\pmb{z} \equiv r - r'$ ，它与 $r$ 不一样。我认为它是一个好符号，但必须要细心对待 $^1$ 。

在前面的版本中，我区分了两类不同类型的习题。其中一些具有特定的教学目的，在学习完相关章节后应立即演做；这些习题我放在章节的相关知识点中。（在少数情况下，习题的结论会在后面章节中用到；这些习题的左边空白处用圆点符号（·）表示。）较长的习题或更一般性质的习题将放在每一章的后面。在我授课时，我会布置它们中的一些题目，少数也会在课堂上演算。极具挑战性的习题在页边的空白处用（！）标记。许多读者曾要求在书后附上习题解答；遗憾的是，也有许多人强烈反对。我取折中方案，对有些特别适当的题目提供答案。出版商提供完整的习题解答手册（供教师使用）；可以去剑桥大学出版社官网申请。

![](images/fcee6778909ae355a9ea60cb18e015dba42559926160f85dd9a01982d6317d9d.jpg)  
从与许多同事的讨论中我受益匪浅——这里我无法一一列出他们的名字。但是我想要感谢对本书第4版做出了贡献的人，他们是：Burton Brody（Bard）、Catherine Crouch（Swarthmore）、Joel Franklin（Reed）、Ted Jacobson（Maryland）、Don Koks（Adelaide）、Charles Lane（Berry）、Kirk Mcdonald $^{2}$ （Princeton）、Jim McTavish（Liverpool）、Rich Saenz（Cal Poly）、Darrel Schroeter（Reed）、Herschel Snodgrass（Lewis和Clark）以及Larry Tankersley（Naval Academy）。实际上，我对电动力学每部分内容的了解——当然也包括如何讲授电动力学——都归功于爱德华·珀塞尔。

大卫·J. 格里菲斯

## 关于本书

# 电动力学是什么？它如何融入物理学的一般框架中？

力学的四个领域

我在下表中简述出力学的四大领域：

<table><tr><td>经典力学(牛顿)</td><td>量子力学(玻尔、海森伯、薛定谔等)</td></tr><tr><td>狭义相对论(爱因斯坦)</td><td>量子场理论(狄拉克、泡利、费曼、施温格等)</td></tr></table>

在大多数的“日常生活”中牛顿力学是正确的，但是对高速运动（接近光速）的物体，它是不正确的，必须用狭义相对论（由爱因斯坦在1905年建立）代替；对于非常小的物体（接近原子尺寸），牛顿力学则由于另外的原因而失效，而由量子力学取代（由玻尔、薛定谔、海森伯及许多其他人在20世纪初发展起来的）。对于（在现代粒子物理学中非常普遍）非常小而又高速运动的物体，需要发展相对论与量子力学结合的力学；这个相对论量子力学称为量子场论——它在20世纪30年代和40年代开始建立，但是即便是到现在也不能认为它是一个完全令人满意的理论。尽管电动力学可以非常简单地扩展到其他三个领域，但在本书中除了最后一章，我们将只研究经典力学的范畴。（事实上，电动力学的大部分内容自动地与相对论相容，这是历史上相对论发展的主要动力。）

## 四种类型的力

力学告诉我们，当一个系统受到一给定力的作用时，它是如何变化的。到目前为止，自然界中已知仅有四种基本力：按强度逐渐减弱的顺序我把它们列出：

1. 强力

2. 电磁力

3. 弱力

4. 引力

这种简洁列法可能会使你们感到吃惊。摩擦力在哪里？维持使你不从地板掉下去的“法向力”在哪里？把分子结合在一起的化学力在哪里？两个相互碰撞台球间的碰撞力又是什么？

答案是，所有这些力都是电磁的。毫不夸张地说，我们的确是生活在一个电磁的世界里——除了引力外，在日常生活中我们所遇到的每一个力都源于电磁作用。

原子核中把质子、中子结合在一起的力是强力（Strong Force），作用距离非常之短；尽管它的强度要比电磁力强百倍以上，但我们无法“感受到”它们。与辐射衰变有关的弱力（Weak Force）不仅作用距离短，也比电磁力弱很多。至于引力，（与其他力相比）更是极其微弱，所以除非质量巨大（比如地球和太阳），否则我们也很难注意到它。两个电子间的静电排斥力是其之间相互引力的 $10^{42}$ 倍，如果原子是（替代电磁力）靠引力结合在一起的，那么一个氢原子将会比已知的宇宙还要大很多。

电磁力不仅在日常生活中占据绝对主导地位，而且也是目前唯一被完全认识的力。当然，我们也有引力的经典理论（牛顿的万有引力定律）和相对论理论（爱因斯坦的广义相对论），但是还没有令人完全满意的有关引力的量子理论（尽管很多人都在努力做这件事）。目前，对弱相互作用已经建立起了非常成功（有点繁杂）的理论，对强相互作用也有引人注目的候选理论（称为色动力学，chromodynamics）。所有这些理论的灵感都来自电动力学；在目前阶段，没有人能声称这些理论得到了确凿的实验验证。因此，电动力学这一优美完整且成功的理论成为物理学家的一个范例：一个其他理论模仿的理想模型。

经典电动力学的规律是由富兰克林、库仑、安培、法拉第以及其他一些人零碎地发现的，并由麦克斯韦完成了最后的工作，把它表述成现今这样紧凑优美协调的形式。这个理论现在已有百年的历史。

## 物理理论的统一

起初，电学和磁学是完全独立的学科。电学研究的是玻璃棒、猫皮、验电球、电池、电流、电解和电灯；而磁学研究的是条形磁铁、铁钉、指南针和地磁极。但在1820年，奥斯特注意到电流可以使磁罗盘针发生偏转。不久之后，安培正确地推测出所有的磁现象都是由于运动中的电荷引起的。然后，在1831年，法拉第发现运动的磁铁会产生电流。当麦克斯韦和洛伦兹对该理论进行最后的润色时，电和磁已是完全交织在一起密不可分。它们不能再被视为单独的学科，而是一个学科的两个方面：电磁学（electromagnetism）。

法拉第推测，光在本质上也是电的。麦克斯韦的理论为这一假设提供了有力的证明，很快，对光学（optics）中透镜、平面镜、棱镜、干涉和衍射的研究——被纳入电磁学。赫兹在1888年为麦克斯韦理论提出了关键的实验证明，他这样说：“光和电之间的联系现在已经建立……在每一个闪电、每一个发光粒子中，我们都看到了一个电的发生……因此，电学的领域范围延伸到整个自然界。它甚至最终影响到我们自身：我们感知到我们拥有……一个电的器官——眼睛。”到了1990年，物理的三大分支：电、磁、光，合并成一个单一的统一理论。（很快就发现可见光只是从无线电波到微波、红外线和紫外线，再到X射线和伽马射线的大量的电磁辐射光谱中的一个很小的“窗口”。）

像一个世纪前将电和磁统一起来一样，爱因斯坦梦想着将引力和电动力学进一步统一起来。他的统一场理论（unified field theory）不是特别成功，但近年来，同样的冲动催生了一系列越来越雄心勃勃（和推测性）的统一场方案，从20世纪60年代的格拉肖、温伯格和萨拉姆弱电统一（electroweak）理论（将弱力和电磁力结合起来）开始，到20世纪80年代的超弦（superstring）理论（据其支持者称，该理论将所有四种力整合到一个“万物理论”中）达到顶峰。在这些方案的每一步，数学难度都在增加，理论猜想和实验验证之间的差距也在扩大。然而，毫无疑问，电动力学引发的力的统一的愿景已经成为物理学发展进步的主旋律。

## 电动力学的场表述

电磁学理论希望解决的基本问题是：我在某处举着一些电荷（也许可以摇晃它们），那么在另外地方上的一些电荷会发生什么？经典解采用场论（field theory）的形式：我们说电荷周围的空间充满了电场和磁场（可以说是电荷的电磁“气味”）。在这些场存在的情况下，另一个电荷会受到一个力；电场将此影响从一个电荷传递到另一个电荷——场是相互作用的“媒介”。

当一个电荷加速运动时，从某种意义上说，场的一部分会自行“分离”，并以光速传播，携带有能量、动量和角动量，我们称之为电磁辐射（electromagnetic radiation）。它的存在使我们（如果不是强迫的话）把场自身看作独立存在的实体，像原子和棒球一样“真实”。因此，我们的兴趣从研究电荷之间的力转向到场本身的理论。但是产生电磁场需要电荷，探测电磁场也需要电荷，所以我们最好从研究电荷的基本性质开始。

## 电荷

1. 电荷有“正”和“负”两种类型，由于它们的影响相互抵消（如果 +q 和 -q 都在某点同一位置，这与该点不存在电荷完全一样）。这似乎显而易见，不值一提。但是我鼓励你们考虑其他的可能性：如果有 8 种或 10 种不同种类的电荷，又会如何呢？（事实上，在色动力学中，与电荷类似的物理量有三种，每一种又分别有正负之分。）或者两类电荷不倾向于相互抵消，又会如何？一个非同寻常的事实是，在块状物体中，正负电荷以惊人的精度表现为数量上完全相等，因此，它们的影响几乎完全被抵消了。若非如此，我们将会受到巨大的力的作用：如果一个土豆中正负电荷仅有 $1/10^{10}$ 没有被相互抵消，它就会发生剧烈的爆炸。

2. 电荷守恒：电荷不能被产生也不能被消灭——一旦存在将永远存在。(一个正电荷可以“湮灭”掉一个等量的负电荷，但正电荷不能简单地自行消失——一定有什么东西会吸收这种电荷。)所以宇宙中的总电荷量是不变的。这称为全（global）电荷守恒。实际上，我们可以表述地更强烈一些：全电荷守恒允许一个电荷在纽约消失而同时在旧金山出现（这不会影响总电荷），但我们知道这是不会发生的。如果这个电荷是在纽约并跑到旧金山，则它必须沿着某条连续的路径，这称为局域电荷守恒。后面我们将会看到如何给出一个精确的数学定律去表示局域电荷守恒——它称为连续性方程（continuity equation）。

3. 电荷的量子化。尽管在经典电动力学中没有任何要求电荷必须是量子化的，事实上电荷仅以分立量的形式出现——电荷基本单位的整数倍。如果我们让质子的电量为 $+e$ ，则电子的电量为 $-e$ ，中子的为零， $\pi$ 介子的为 $+e,0,-e$ ，碳原子核的为 $+6e$ ，等等（绝不会是 $7.392e$ ，或 $\frac{1}{2}e)^{1}$ 。这个电荷基本单位非常之小，所以出于实际的目的，通常完全忽略电荷的量子化是合适的。水，确实也由分立量（分子）组成，但是，如果我们是处理大量的水就可以把它作为连续的流体。这事实上非常接近麦克斯韦本人的观点；他对电子和质子一无所知——他一定把电荷想象成一种“果冻”，可以分成任何大小的部分，随意涂抹。

## 单位制

电动力学的研究常被使用不同的单位制所困扰，这有时候会使物理学家难以交流。这个问题比在力学中更严重，尼安德特人仍然在使用磅和英尺；在力学中，除了单位制的不同，至少所有的方程看起来都是一样的。不管单位制是英尺-磅-秒，还是千克-米-秒，或者任何其他单位制，牛顿第二定律仍是 $F = ma$ 。但是，在电动力学中情况就不是如此了，库仑定律可能的形式为

$$
\frac {q _ {1} q _ {2}}{\pmb {\mathscr {r}} ^ {2}} \hat {\pmb {\mathscr {r}}} (\text {高斯制}), \text {或者} \frac {1}{4 \pi \varepsilon_ {0}} \frac {q _ {1} q _ {2}}{\pmb {\mathscr {r}} ^ {2}} \hat {\pmb {\mathscr {r}}} (\text {国际单位制}), \text {或者} \frac {1}{4 \pi} \frac {q _ {1} q _ {2}}{\pmb {\mathscr {r}} ^ {2}} \hat {\pmb {\mathscr {r}}} (\text {HL制})
$$

最常用的两个单位制是高斯制（cgs）和国际单位制（mks）。基本粒子工作者喜欢用第三种单位制：赫维塞德-洛伦兹单位（HL）制。尽管高斯制具有简洁的理论优点，大多数教授本科生的教师更喜欢国际单位制（SI），因为它包含了所熟悉的日常生活单位（伏特、安培、瓦特）。因此，本书将使用国际单位制。附录 C 提供了把主要结果转化为高斯制的表格。

## 目录

## 译者序

## 作者序

## 关于本书

第1章 矢量分析 …… 1  
1.1 矢量代数 …… 1  
1.1.1 矢量运算 …… 1  
1.1.2 矢量代数：分量形式 …… 4  
1.1.3 混合积 …… 6  
1.1.4 位置、位移与间隔矢量 …… 8  
1.1.5 矢量如何变换 …… 9  
1.2 微分运算 …… 12  
1.2.1 “常”微分 …… 12  
1.2.2 梯度 …… 12  
1.2.3 ∇算符 …… 14  
1.2.4 散度 …… 15  
1.2.5 旋度 …… 16  
1.2.6 乘积定则 …… 17  
1.2.7 二阶导数 …… 19  
1.3 积分运算 …… 21  
1.3.1 线、面和体积分 …… 21  
1.3.2 积分基本定理 …… 25  
1.3.3 梯度基本定理 …… 26  
1.3.4 散度基本定理 …… 28  
1.3.5 旋度基本定理 …… 30  
1.3.6 分部积分 …… 32

1.4 曲线坐标系 …… 33
1.4.1 球坐标系 …… 33
1.4.2 柱坐标系 …… 37
1.5 狄拉克 δ 函数 …… 39
1.5.1 $\hat{r}/r^{2}$ 的散度 …… 39
1.5.2 一维狄拉克 δ 函数 …… 40
1.5.3 三维 δ 函数 …… 43
1.6 矢量场理论 …… 45
1.6.1 亥姆霍兹定理 …… 45
1.6.2 势函数 …… 46
第 1 章补充习题 …… 47

第 2 章 静电学 …… 51
2.1 电场 …… 51
2.1.1 引言 …… 51
2.1.2 库仑定律 …… 52
2.1.3 电场 …… 52
2.1.4 连续电荷分布 …… 54
2.2 静电场的散度和旋度 …… 57
2.2.1 场线、通量和高斯定理 …… 57
2.2.2 E 的散度 …… 61
2.2.3 高斯定理的应用 …… 61
2.2.4 E 的旋度 …… 66
2.3 电势 …… 67
2.3.1 引言 …… 67
2.3.2 有关势的评注 …… 68
2.3.3 泊松方程和拉普拉斯方程 …… 71
2.3.4 局域电荷分布的势 …… 72
2.3.5 边界条件 …… 75
2.4 静电学中的功和能 …… 77
2.4.1 移动电荷所需做的功 …… 77
2.4.2 点电荷分布的能量 …… 78
2.4.3 连续电荷分布的能量 …… 80
2.4.4 关于静电场能量的评注 …… 82
2.5 导体 …… 83
2.5.1 基本性质 …… 83

2.5.2 感生电荷....85
2.5.3 表面电荷和导体受力....87
2.5.4 电容....89
第2章补充习题....91

第3章 势....95
3.1 拉普拉斯方程....95
3.1.1 引言....95
3.1.2 一维拉普拉斯方程....96
3.1.3 二维拉普拉斯方程....97
3.1.4 三维拉普拉斯方程....98
3.1.5 边界条件和唯一性定理....100
3.1.6 导体和第二唯一性定理....102
3.2 镜像法....104
3.2.1 典型镜像问题....104
3.2.2 表面感应电荷....105
3.2.3 力和能....106
3.2.4 其他镜像问题....107
3.3 分离变量法....109
3.3.1 直角坐标系....110
3.3.2 球坐标系....118
3.4 多极矩展开....125
3.4.1 远距离近似电势....125
3.4.2 单极项和偶极项....128
3.4.3 多极展开中的坐标原点....130
3.4.4 偶极子的电场....131
第3章补充习题....133

第4章 介质中的电场....139
4.1 极化....139
4.1.1 电介质....139
4.1.2 诱导偶极子....139
4.1.3 极性分子的排列....142
4.1.4 极化....144
4.2 极化物体的场....144
4.2.1 束缚电荷....144

4.2.2 束缚电荷的物理诠释 …… 147
4.2.3 电介质内部的场 …… 150
4.3 电位移 …… 151
4.3.1 有电介质时的高斯定理 …… 151
4.3.2 误导性的类比 …… 154
4.3.3 边界条件 …… 155
4.4 线性电介质 …… 155
4.4.1 电极化率、介电常数和相对介电常数 …… 155
4.4.2 线性电介质的边界值问题 …… 161
4.4.3 介电系统的能量 …… 164
4.4.4 电介质上的力 …… 169
第 4 章补充习题 …… 171

第 5 章 静磁学 …… 177
5.1 洛伦兹力定律 …… 177
5.1.1 磁场 …… 177
5.1.2 磁力 …… 179
5.1.3 电流 …… 182
5.2 毕奥-萨伐尔定律 …… 188
5.2.1 稳恒电流 …… 188
5.2.2 稳恒电流的磁场 …… 189
5.3 直线电流 B 的散度和旋度 …… 193
5.3.1 直线电流 …… 193
5.3.2 B 的散度和旋度 …… 195
5.3.3 安培定律 …… 197
5.3.4 静磁学与静电学的比较 …… 203
5.4 磁矢势 …… 205
5.4.1 矢势 …… 205
5.4.2 边界条件 …… 210
5.4.3 矢势的多极展开 …… 212
第 5 章补充习题 …… 215

第 6 章 介质中的磁场 …… 223
6.1 磁化 …… 223
6.1.1 抗磁体、顺磁体和铁磁体 …… 223
6.1.2 磁偶极矩上的力和力矩 …… 223

6.1.3 磁场对原子轨道的影响 …… 227
6.1.4 磁化强度 …… 229
6.2 磁化介质的场 …… 229
6.2.1 束缚电流 …… 229
6.2.2 束缚电流的物理诠释 …… 232
6.2.3 介质内的磁场 …… 234
6.3 辅助场 H …… 234
6.3.1 磁介质中的安培定律 …… 234
6.3.2 误导性的类比 …… 237
6.3.3 边界条件 …… 238
6.4 线性和非线性介质 …… 238
6.4.1 磁化率与磁导率 …… 238
6.4.2 铁磁性 …… 241
第 6 章补充习题 …… 245

第 7 章 电动力学 …… 249
7.1 欧姆定律 电动势 …… 249
7.1.1 欧姆定律 …… 249
7.1.2 电动势 …… 254
7.1.3 动生电动势 …… 256
7.2 电磁感应 …… 262
7.2.1 法拉第定律 …… 262
7.2.2 感生电场 …… 266
7.2.3 电感 …… 270
7.2.4 磁场的能量 …… 275
7.3 麦克斯韦方程组 …… 279
7.3.1 麦克斯韦之前的电动力学 …… 279
7.3.2 麦克斯韦如何修正安培定律 …… 280
7.3.3 麦克斯韦方程组 …… 283
7.3.4 磁荷 …… 284
7.3.5 介质中的麦克斯韦方程组 …… 285
7.3.6 边界条件 …… 287
第 7 章补充习题 …… 290

第 8 章 守恒律 …… 299
8.1 电荷和能量 …… 299

8.1.1 连续性方程 …… 299
8.1.2 坡印亭定理 …… 300
8.2 动量 …… 303
8.2.1 电动力学中的牛顿第三定律 …… 303
8.2.2 麦克斯韦应力张量 …… 304
8.2.3 动量守恒 …… 308
8.2.4 角动量 …… 311
8.3 磁场力不做功 …… 313
第8章补充习题 …… 317
第9章 电磁波 …… 321
9.1 一维波 …… 321
9.1.1 波动方程 …… 321
9.1.2 正弦波 …… 324
9.1.3 边界条件：反射与透射 …… 326
9.1.4 偏振 …… 329
9.2 真空中的电磁波 …… 331
9.2.1 E与B的波动方程 …… 331
9.2.2 单色平面波 …… 332
9.2.3 电磁波的能量与动量 …… 335
9.3 物质中的电磁波 …… 337
9.3.1 线性介质中的传播 …… 337
9.3.2 垂直入射时的反射与透射 …… 338
9.3.3 斜入射时的反射与透射 …… 341
9.4 吸收与色散 …… 346
9.4.1 导体中的电磁波 …… 346
9.4.2 导体表面的反射 …… 349
9.4.3 介电常数对频率的依赖 …… 351
9.5 导波 …… 357
9.5.1 波导 …… 357
9.5.2 矩形波导中的TM波 …… 359
9.5.3 共轴传输线 …… 362
第9章补充习题 …… 363
第10章 势与场 …… 367
10.1 势表述 …… 367

10.1.1 标势与矢势 …… 367
10.1.2 规范变换 …… 369
10.1.3 库仑规范与洛伦茨规范 …… 371
10.1.4 势形式的洛伦兹力定律 …… 372
10.2 连续分布 …… 374
10.2.1 推迟势 …… 374
10.2.2 Jefimenko's 方程 …… 378
10.3 点电荷 …… 380
10.3.1 李纳-维谢尔势 …… 380
10.3.2 运动点电荷的场 …… 385
第 10 章补充习题 …… 390

第 11 章 辐射 …… 393
11.1 偶极辐射 …… 393
11.1.1 什么是辐射 …… 393
11.1.2 电偶极子辐射 …… 394
11.1.3 磁偶极子辐射 …… 399
11.1.4 任意源的辐射 …… 403
11.2 点电荷的辐射 …… 407
11.2.1 点电荷的辐射功率 …… 407
11.2.2 辐射反作用 …… 411
11.2.3 相应于辐射反作用的机制 …… 415
第 11 章补充习题 …… 418

第 12 章 电动力学与相对论 …… 423
12.1 狭义相对论 …… 423
12.1.1 爱因斯坦的假设 …… 423
12.1.2 相对论几何学 …… 428
12.1.3 洛伦兹变换 …… 436
12.1.4 时空结构 …… 442
12.2 相对论力学 …… 448
12.2.1 固有时和固有速度 …… 448
12.2.2 相对论能量和动量 …… 451
12.2.3 相对论运动学 …… 452
12.2.4 相对论动力学 …… 456
12.3 相对论电动力学 …… 462

12.3.1 相对论中的磁现象 …… 462
12.3.2 场如何变换 …… 464
12.3.3 场张量 …… 472
12.3.4 张量形式的电动力学 …… 475
12.3.5 相对论势 …… 478
第 12 章补充习题 …… 480
附录 …… 483
附录 A 曲线坐标系中的矢量微积分 …… 485
A.1 引言 …… 485
A.2 标记法 …… 485
A.3 梯度 …… 485
A.4 散度 …… 486
A.5 旋度 …… 489
A.6 拉普拉斯算子 …… 491
附录 B 亥姆霍兹定理 …… 493
附录 C 单位制 …… 497
索引 …… 501

## 第 1 章 矢量分析

## 1.1 矢量代数

## 1.1.1 矢量运算

如果你向北走 4 英里然后再向东走 3 英里（图 1.1），你总共走了 7 英里，但你距出发点的距离仅有 5 英里，而不是 7 英里。我们需要一个算法来描述这样的量，这显然不是普通的加法。它们不遵从普通加法的原因是位移（displacements，从一点到另一点的直线段）除了有大小（长度）外还包含有方向，当结合两个位移时它们的方向和大小都必须考虑在内。像位移这样的物理量称为矢量（vectors）：其他的例子还有速度、加速度、力和动量等。相比而言，仅有大小而没有方向的量称为标量（scalars）：诸如质量、电荷、密度和温度等。

我将用黑体字母（A, B 等）表示矢量，而用普通类型字母表示标量。一个矢量 A 的大小用 $|A|$ 表示，或简单地用 A 表示。在作图时，矢量用一个箭矢表示，箭矢的长度正比于矢量的大小，箭头指向矢量的方向。负 A（-A）是一个与 A 大小相同，方向相反的矢量（图 1.2）。注意矢量有大小和方向，但位置不确定：一个从华盛顿向北 4 英里的位移和一个从巴尔的摩向北 4 英里的位移由同样的矢量表示（当然，我们忽略了地球是弯曲的）。因此，在作图时，只要不改变它的长度和方向，你可以移动任意一个矢量。

![](images/1c268475adcd726789ce78e6bbb0f59660d219765c56a42b920a0a4778a55af6.jpg)  
图1.1

![](images/53ebc122be91874ea8726a4462105e63e6a303638646a1e0e867a7e6353ddd82.jpg)  
图1.2

我们定义四种矢量运算：矢量加法和三种乘法。

（i）两个矢量的加法（Addition of two vectors）。把矢量 B 的尾部放在 A 的头部；矢量之和是一个从 A 的尾部到 B 的头部的矢量（图 1.3）。（这个规则概括两个位移结合的

过程。）矢量加法满足交换律：

$$
\boldsymbol {A} + \boldsymbol {B} = \boldsymbol {B} + \boldsymbol {A}
$$

先向东3英里然后再向北4英里，与先向北4英里然后再向东3英里最后到达的位置是一样的。矢量加法也满足结合律：

$$
(A + B) + C = A + (B + C)
$$

减去一个矢量等于加上它的一个方向相反的矢量（图1.4）：

$$
\boldsymbol {A} - \boldsymbol {B} = \boldsymbol {A} + (- \boldsymbol {B})
$$

![](images/19fc8087b6c76fb867460188b884109408d012df4002bafe962493d7c4c9e6a0.jpg)  
图1.3

![](images/29108a15bcad3af8745ab243837b10f04c922d3ba0941e5dfece4f58caa7c93a.jpg)  
图1.4

（ii）标量与矢量相乘（Multiplication by a scalar）。矢量与正的标量 $a$ 相乘，是把矢量的模与 $a$ 相乘，方向不变（图1.5）。（如果是负的，矢量的方向颠倒。）矢量与标量相乘满足分配律：

$$
a (\boldsymbol {A} + \boldsymbol {B}) = a \boldsymbol {A} + a \boldsymbol {B}
$$

（iii）两个矢量的点积（Dot product of two vectors）。两个矢量点积定义为

$$
\boldsymbol {A} \cdot \boldsymbol {B} \equiv A B \cos \theta\tag{1.1}
$$

式中， $\theta$ 是两个矢量的尾部对尾部放在一起时它们之间的夹角（图1.6）。注意 $\mathbf{A} \cdot \mathbf{B}$ 是一个标量（所以又称为标积，scalar product）。矢量的点积满足交换律

$$
\boldsymbol {A} \cdot \boldsymbol {B} = \boldsymbol {B} \cdot \boldsymbol {A}
$$

和分配律

$$
\boldsymbol {A} \cdot (\boldsymbol {B} + \boldsymbol {C}) = \boldsymbol {A} \cdot \boldsymbol {B} + \boldsymbol {A} \cdot \boldsymbol {C}\tag{1.2}
$$

从几何上讲， $A \cdot B$ 是 $A$ 乘以 $B$ 沿 $A$ 方向投影大小（或 $B$ 乘以 $A$ 沿 $B$ 方向投影大小）。如果两矢量平行，则有 $A \cdot B = AB$ 。特别是，对任意的矢量 $A$ 都有

$$
\boldsymbol {A} \cdot \boldsymbol {A} = A ^ {2}\tag{1.3}
$$

如果 A 和 B 是相互垂直的，则 $A \cdot B = 0$ 。

![](images/41e592c1c068f6b191d36f3e5ca78cc8acb2edc18f76962e35de4d30e6d00ed6.jpg)  
图1.5

![](images/efd0b28c8d6d749c3afd2c39a160a138198bfd63f8c2f6cd662f935e17687a67.jpg)  
图1.6

例题1.1 设 $C = A - B$ （图1.7），计算 $C$ 与它自身的点积。[解答]

$$
C \cdot C = (A - B) \cdot (A - B) = A \cdot A - A \cdot B - B \cdot A + B \cdot B
$$

$$
C ^ {2} = A ^ {2} + B ^ {2} - 2 A B \cos \theta
$$

这就是余弦定理（law of cosines）。

$^{1}$ $^{2}$ $^{3}$ $^{4}$ $^{5}$ $^{6}$ $^{7}$ $^{8}$ $^{9}$ $^{10}$ $^{11}$ $^{12}$ $^{13}$ $^{14}$ $^{15}$ $^{16}$ $^{17}$ $^{18}$ $^{19}$ $^{20}$ $^{21}$ $^{22}$ $^{23}$ $^{24}$ $^{25}$ $^{26}$ $^{27}$ $^{28}$ $^{29}$ $^{30}$ $^{31}$ $^{32}$ $^{33}$ $^{34}$ $^{35}$ $^{36}$ $^{37}$ $^{38}$ $^{39}$ $^{40}$ $^{41}$ $^{42}$ $^{43}$ $^{44}$ $^{45}$ $^{46}$ $^{47}$ $^{48}$ $^{49}$ $^{50}$ $^{51}$ $^{52}$ $^{53}$ $^{54}$ $^{55}$ $^{56}$ $^{57}$ $^{58}$ $^{59}$ $^{60}$ $^{61}$ $^{62}$ $^{63}$ $^{64}$ $^{65}$ $^{66}$ $^{67}$ $^{68}$ $^{69}$ $^{70}$ $^{71}$ $^{72}$ $^{73}$ $^{74}$ $^{75}$ $^{76}$ $^{77}$ $^{78}$ $^{79}$ $^{80}$ $^{81}$ $^{82}$ $^{83}$ $^{84}$ $^{85}$ $^{86}$ $^{87}$ $^{88}$ $^{89}$ $^{90}$ $^{91}$ $^{92}$ $^{93}$ $^{94}$ $^{95}$ $^{96}$ $^{97}$ $^{98}$ $^{99}$ $^{100}$

(iv) 两个矢量的叉积。两个矢量的叉积定义为

$$
\boldsymbol {A} \times \boldsymbol {B} \equiv A B \sin \theta \hat {\boldsymbol {n}}\tag{1.4}
$$

式中， $\hat{n}$ 是垂直于由 $A$ 和 $B$ 所组成平面的一个单位矢量（长度为 1 的矢量）。（我将用一个帽标（^）表示单位矢量。）当然，垂直任何一个平面都有两个方向：“向里”和“向外”。我们用右手定则（right-hand rule）来消除这个模棱两可的不确定性：让四指指向第一个矢量的方向，然后（沿小角度）四指弯曲朝向第二个矢量的方向，那么，大拇指所指就是 $\hat{n}$ 的方向。（在图 1.8 中， $A \times B$ 指向纸面内， $B \times A$ 指出纸面外。）注意 $A \times B$ 本身是一个矢量（所以又称为矢量积，vector product）。矢量叉积满足分配律：

$$
\boldsymbol {A} \times (\boldsymbol {B} + \boldsymbol {C}) = \boldsymbol {A} \times \boldsymbol {B} + \boldsymbol {A} \times \boldsymbol {C}\tag{1.5}
$$

![](images/c183c773d4bd5af2b3aac63f442c57c4f3dd5a94bcd3b3fe998579a9894cc9a3.jpg)  
图1.7

![](images/bda4067de3464cf373cb13f7ce57f1e0371ecd7f9e7a3a956b94d777bf49e9e0.jpg)  
图1.8

但是不满足交换律。事实上有

$$
(\boldsymbol {A} \times \boldsymbol {B}) = - (\boldsymbol {B} \times \boldsymbol {A})\tag{1.6}
$$

从几何上讲， $|A \times B|$ 是由 A 和 B 所构成的平行四边形的面积（图 1.8）。如果两个矢量平行，则它们的叉积为零。特别是，对任意矢量 A 都有

$$
\boldsymbol {A} \times \boldsymbol {A} = \boldsymbol {0}
$$

（这里称为零矢量（zero vector），它的模为零。）

习题1.1 利用式（1.1）和式（1.4）的定义以及适当的作图，证明点积和叉积满足分配律，a）同一个平面内的三个矢量。

b）一般情况。

习题1.2 矢量叉积满足结合律吗？即

$$
(A \times B) \times C \stackrel {?} {=} A \times (B \times C)
$$

如果满足，请给出证明；如果不满足，请给出一个反例（越简单越好）。

## 1.1.2 矢量代数：分量形式

在上一节中，我以一种“抽象”的形式定义了四种矢量运算（加法、标量与矢量相乘、点积和叉积），即与任何特定的坐标系无关。在实际运算中，选用直角坐标系 $x, y, z$ ，用矢量的分量（components）来计算将会更方便。设 $\hat{x}, \hat{y}, \hat{z}$ 分别为平行 $x, y, z$ 坐标轴的单位矢量（图1.9a）。一个任意矢量 $A$ 都可以用这些基矢量（basis vectors）展开（图1.9b）：

$$
\boldsymbol {A} = A _ {x} \hat {\boldsymbol {x}} + A _ {y} \hat {\boldsymbol {y}} + A _ {z} \hat {\boldsymbol {z}}
$$

![](images/c4a4e8bf64542ef5940a52023413324a4d134005bd866c86a0bf88bd0212389c.jpg)

![](images/89f84b41cac1969caffd1d0c7624b8e267a6a661c8dc5d06655a8638ed27531a.jpg)  
图1.9

$A_{x}, A_{y}, A_{z}$ 称为矢量 $\mathbf{A}$ 的分量；从几何上讲，它们是矢量 $\mathbf{A}$ 沿三个坐标轴的投影（ $A_{x} = \mathbf{A} \cdot \hat{\mathbf{x}}, A_{y} = \mathbf{A} \cdot \hat{\mathbf{y}}, A_{z} = \mathbf{A} \cdot \hat{\mathbf{z}}$ ）。我们可以把四种矢量运算中的每一个重新表示为分量运算形式：

$$
\begin{array}{r l} \boldsymbol {A} + \boldsymbol {B} & = (A _ {x} \hat {\boldsymbol {x}} + A _ {y} \hat {\boldsymbol {y}} + A _ {z} \hat {\boldsymbol {z}}) + (B _ {x} \hat {\boldsymbol {x}} + B _ {y} \hat {\boldsymbol {y}} + B _ {z} \hat {\boldsymbol {z}}) \\ & = (A _ {x} + B _ {x}) \hat {\boldsymbol {x}} + (A _ {y} + B _ {y}) \hat {\boldsymbol {y}} + (A _ {z} + B _ {z}) \hat {\boldsymbol {z}} \end{array}\tag{1.7}
$$

规则（i）：矢量相加，把对应分量相加。

$$
a \boldsymbol {A} = (a A _ {x}) \hat {\boldsymbol {x}} + (a A _ {y}) \hat {\boldsymbol {y}} + (a A _ {z}) \hat {\boldsymbol {z}}\tag{1.8}
$$

规则（ii）：矢量与标量相乘，把每个分量与标量相乘。

由于 $\hat{x},\hat{y},\hat{z}$ 是相互垂直的单位矢量，所以

$$
\hat {\boldsymbol {x}} \cdot \hat {\boldsymbol {x}} = \hat {\boldsymbol {y}} \cdot \hat {\boldsymbol {y}} = \hat {\boldsymbol {z}} \cdot \hat {\boldsymbol {z}} = 1; \quad \hat {\boldsymbol {x}} \cdot \hat {\boldsymbol {y}} = \hat {\boldsymbol {x}} \cdot \hat {\boldsymbol {z}} = \hat {\boldsymbol {y}} \cdot \hat {\boldsymbol {z}} = 0\tag{1.9}
$$

相应地，

$$
\begin{array}{r l} \boldsymbol {A} \cdot \boldsymbol {B} & = (A _ {x} \hat {\boldsymbol {x}} + A _ {y} \hat {\boldsymbol {y}} + A _ {z} \hat {\boldsymbol {z}}) \cdot (B _ {x} \hat {\boldsymbol {x}} + B _ {y} \hat {\boldsymbol {y}} + B _ {z} \hat {\boldsymbol {z}}) \\ & = A _ {x} B _ {x} + A _ {y} B _ {y} + A _ {z} B _ {z} \end{array}\tag{1.10}
$$

规则（iii）：计算矢量点积时，把对应分量相乘后再相加在一起。

特别有，

$$
\boldsymbol {A} \cdot \boldsymbol {A} = A _ {x} ^ {2} + A _ {y} ^ {2} + A _ {z} ^ {2}
$$

所以

$$
A = \sqrt {A _ {x} ^ {2} + A _ {y} ^ {2} + A _ {z} ^ {2}}\tag{1.11}
$$

（换句话说，这是勾股定理在三维情况下的推广。）

类似有 $^{1}$ ，

$$
\begin{array}{l} \hat {\boldsymbol {x}} \times \hat {\boldsymbol {x}} = \hat {\boldsymbol {y}} \times \hat {\boldsymbol {y}} = \hat {\boldsymbol {z}} \times \hat {\boldsymbol {z}} = 0 \\ \hat {\boldsymbol {x}} \times \hat {\boldsymbol {y}} = - \hat {\boldsymbol {y}} \times \hat {\boldsymbol {x}} = \hat {\boldsymbol {z}} \\ \hat {\boldsymbol {y}} \times \hat {\boldsymbol {z}} = - \hat {\boldsymbol {z}} \times \hat {\boldsymbol {y}} = \hat {\boldsymbol {x}} \\ \hat {\boldsymbol {z}} \times \hat {\boldsymbol {x}} = - \hat {\boldsymbol {x}} \times \hat {\boldsymbol {z}} = \hat {\boldsymbol {y}} \end{array}\tag{1.12}
$$

所以

$$
\begin{array}{r l} \boldsymbol {A} \times \boldsymbol {B} & = (A _ {x} \hat {\boldsymbol {x}} + A _ {y} \hat {\boldsymbol {y}} + A _ {z} \hat {\boldsymbol {z}}) \times (B _ {x} \hat {\boldsymbol {x}} + B _ {y} \hat {\boldsymbol {y}} + B _ {z} \hat {\boldsymbol {z}}) \\ & = (A _ {y} B _ {z} - A _ {z} B _ {y}) \hat {\boldsymbol {x}} + (A _ {z} B _ {x} - A _ {x} B _ {z}) \hat {\boldsymbol {y}} + (A _ {x} B _ {y} - A _ {y} B _ {x}) \hat {\boldsymbol {z}} \end{array}\tag{1.13}
$$

这个烦琐的表达式可以更简洁地写成行列式形式：

$$
\boldsymbol {A} \times \boldsymbol {B} = \left| \begin{array}{c c c} \hat {\boldsymbol {x}} & \hat {\boldsymbol {y}} & \hat {\boldsymbol {z}} \\ A _ {x} & A _ {y} & A _ {z} \\ B _ {x} & B _ {y} & B _ {z} \end{array} \right|\tag{1.14}
$$

规则（iv）：计算矢量叉积时，可以构造一个行列式，第一行是 $\hat{x}, \hat{y}, \hat{z}$ ，第二行是 A 的分量，第三行是 B 的分量。

例题 1.2 求出一立方体两个面的对角线之间夹角。

[解答] 我们不妨设立方体边长为 1，放置如图（图 1.10）所示的位置，其中的一个角位于坐标原点。面对角线 A 可表示为

$$
A = 1 \hat {x} + 0 \hat {y} + 1 \hat {z}, \quad B = 0 \hat {x} + 1 \hat {y} + 1 \hat {z}
$$

![](images/9482da5e5514ab9430982e963cddac092787f4eb81ff14d58560a4f756e5706c.jpg)  
图1.10

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •

因此，在以分量形式中，

$$
\boldsymbol {A} \cdot \boldsymbol {B} = 1 \cdot 0 + 0 \cdot 1 + 1 \cdot 1 = 1
$$

另一方面，在“抽象”形式中，

$$
\boldsymbol {A} \cdot \boldsymbol {B} = A B \cos \theta = \sqrt {2} \cdot \sqrt {2} \cos \theta = 2 \cos \theta
$$

$$
\cos \theta = 1 / 2, \quad \text {或者} \quad \theta = 6 0 ^ {\circ}
$$

当然，你也可以在立方体顶面上画出连接 $A, B$ 头部的另一条面对角线，形成一个等边三角形，这样更容易得到答案。但是，如果所给几何不是如此简单的情况下，这种比较点积的抽象形式和分量形式得到夹角的计算方法是非常有效的。

习题 1.3 求出立方体体对角线之间的夹角 $^{2}$ 。

习题 1.4 利用矢量叉积求出垂直于如图 1.11 所示阴影平面的单位矢量 $\hat{n}$ 的分量。

![](images/f294bb9e8e45dcad91f39e0de87760a10ae01393ce8f29a030e45dc670003557.jpg)  
图1.11

## 1.1.3 混合积

由于两个矢量的叉积本身是一个矢量，它可以通过点积或叉积与第三个矢量形成混合积。

(i) 标量混合积 (Scalar triple product): $A \cdot (B \times C)$ 。从几何上讲, $|A \cdot (B \times C)|$ 是由 $A, B$ 和 $C$ 所形成平行六面体的体积, 因为 $|B \times C|$ 是平行六面体基底的面积, $|A \cos \theta|$ 是它的高 (图 1.12)。显然有,

$$
\boldsymbol {A} \cdot (\boldsymbol {B} \times \boldsymbol {C}) = \boldsymbol {B} \cdot (\boldsymbol {C} \times \boldsymbol {A}) = \boldsymbol {C} \cdot (\boldsymbol {A} \times \boldsymbol {B})\tag{1.15}
$$

因为它们都对应着同一个平行六面体。注意上式是按“字母”顺序轮换的——考虑到式（1.6），不按“字母”顺序的混合积

$$
\boldsymbol {A} \cdot (\boldsymbol {C} \times \boldsymbol {B}) = \boldsymbol {B} \cdot (\boldsymbol {A} \times \boldsymbol {C}) = \boldsymbol {C} \cdot (\boldsymbol {B} \times \boldsymbol {A})
$$

与式（1.15）具有相反的符号。在分量的形式中

$$
\boldsymbol {A} \cdot (\boldsymbol {B} \times \boldsymbol {C}) = \left| \begin{array}{l l l} A _ {x} & A _ {y} & A _ {z} \\ B _ {x} & B _ {y} & B _ {z} \\ C _ {x} & C _ {y} & C _ {z} \end{array} \right|\tag{1.16}
$$

注意到矢量点积和叉积是可互换的：

$$
\boldsymbol {A} \cdot (\boldsymbol {B} \times \boldsymbol {C}) = (\boldsymbol {A} \times \boldsymbol {B}) \cdot \boldsymbol {C}
$$

[这可由式（1.15）直接给出]；然而，括弧的位置至关重要： $(\boldsymbol{A}\cdot\boldsymbol{B})\times\boldsymbol{C}$ 是一个无意义的表示式——你不能用一个标量和一个矢量做叉积。

![](images/a263461e75b0a6c6d4462715ffe52c959ed0e5ef6bc180fc5ac6e77b9bdcfe25.jpg)  
图1.12

（ii）矢量混合积（Vector triple product）： $A \times (B \times C)$ 。矢量混合积可由所谓的 BAC-CAB 规则进行化简：

$$
\boldsymbol {A} \times (\boldsymbol {B} \times \boldsymbol {C}) = \boldsymbol {B} (\boldsymbol {A} \cdot \boldsymbol {C}) - \boldsymbol {C} (\boldsymbol {A} \cdot \boldsymbol {B})\tag{1.17}
$$

注意

$$
(A \times B) \times C = - C \times (A \times B) = - A (B \cdot C) + B (A \cdot C)
$$

是一个完全不同的矢量（叉积不满足结合律）。顺便提及，更高次的矢量积都可以反复应用类似式（1.17）的方法进行化简，所以一般情况下表达式中都不含有两个以上叉积。例如，

$$
(A \times B) \cdot (C \times D) = (A \cdot C) (B \cdot D) - (A \cdot D) (B \cdot C)
$$

$$
\boldsymbol {A} \times [ \boldsymbol {B} \times (\boldsymbol {C} \times \boldsymbol {D}) ] = \boldsymbol {B} [ \boldsymbol {A} \cdot (\boldsymbol {C} \times \boldsymbol {D}) ] - (\boldsymbol {A} \cdot \boldsymbol {B}) (\boldsymbol {C} \times \boldsymbol {D})\tag{1.18}
$$

习题 1.5 写出式（1.17）两边的分量形式并证明 BAC-CAB 规则。

习题1.6 证明

$$
[ \boldsymbol {A} \times (\boldsymbol {B} \times \boldsymbol {C}) ] + [ \boldsymbol {B} \times (\boldsymbol {C} \times \boldsymbol {A}) ] + [ \boldsymbol {C} \times (\boldsymbol {A} \times \boldsymbol {B}) ] = 0
$$

$A \times (B \times C) = (A \times B) \times C$ 在什么条件下成立？

## 1.1.4 位置、位移与间隔矢量

空间中的一个点的位置可由直角坐标系中 $(x,y,z)$ 值来表示。从坐标原点指向该点的矢量称为位置矢量（position vector）（图 1.13）：

$$
\boldsymbol {r} \equiv x \hat {\boldsymbol {x}} + y \hat {\boldsymbol {y}} + z \hat {\boldsymbol {z}}\tag{1.19}
$$

在本书中我保留用 r 来表示位置矢量。它的大小

$$
r = \sqrt {x ^ {2} + y ^ {2} + z ^ {2}}\tag{1.20}
$$

是离开原点的距离，

$$
\hat {\boldsymbol {r}} = \frac {\boldsymbol {r}}{r} = \frac {x \hat {\boldsymbol {x}} + y \hat {\boldsymbol {y}} + z \hat {\boldsymbol {z}}}{\sqrt {x ^ {2} + y ^ {2} + z ^ {2}}}\tag{1.21}
$$

是指向径向的单位矢量。从点 $(x,y,z)$ 到点 $(x+\mathrm{d}x,y+\mathrm{d}y,z+\mathrm{d}z)$ 的无限小位移矢量（infinitesimal displacement vector）是

$$
\mathrm{d} \boldsymbol {l} = \mathrm{d} x \hat {\boldsymbol {x}} + \mathrm{d} y \hat {\boldsymbol {y}} + \mathrm{d} z \hat {\boldsymbol {z}}\tag{1.22}
$$

（我们可以称它为 $\mathrm{d}\pmb{r}$ ，因为这正是它的含义，不过为无限小位移矢量保留一个特殊的符号还是有用的。）

在电动力学中,我们会经常遇到涉及两点的问题——典型的有,一个源点（source point） $r'$ ，即电荷所处的位置，及场点（field point）r，这是我们要计算电场和磁场的地方（图1.14）。很值得在一开始就引入一个表示从源点到场点的间隔矢量（separation vector）的简短标记，为此我将用斜体字母z：

$$
r \equiv r - r ^ {\prime}\tag{1.23}
$$

它的大小是

$$
\iota \equiv | \pmb {r} - \pmb {r} ^ {\prime} |\tag{1.24}
$$

沿 $r'$ 到 $\pmb{r}$ 方向的单位矢量是

$$
\hat {\mathbf {r}} = \frac {\mathbf {r}}{\mathbf {r}} = \frac {\mathbf {r} - \mathbf {r} ^ {\prime}}{| \mathbf {r} - \mathbf {r} ^ {\prime} |}\tag{1.25}
$$

在直角坐标系

$$
\boldsymbol {z} = (x - x ^ {\prime}) \hat {\boldsymbol {x}} + (y - y ^ {\prime}) \hat {\boldsymbol {y}} + (z - z ^ {\prime}) \hat {\boldsymbol {z}}\tag{1.26}
$$

$$
r = \sqrt {(x - x ^ {\prime}) ^ {2} + (y - y ^ {\prime}) ^ {2} + (z - z ^ {\prime}) ^ {2}}\tag{1.27}
$$

$$
\hat {\boldsymbol {z}} = \frac {(x - x ^ {\prime}) \hat {\boldsymbol {x}} + (y - y ^ {\prime}) \hat {\boldsymbol {y}} + (z - z ^ {\prime}) \hat {\boldsymbol {z}}}{\sqrt {(x - x ^ {\prime}) ^ {2} + (y - y ^ {\prime}) ^ {2} + (z - z ^ {\prime}) ^ {2}}}\tag{1.28}
$$

(由此你可以感受到使用这个标记的简练之处。)

![](images/4f69a36038f0504173fb62018ea5d10cfcb2e24d49fbedd3f2d7abce8dd2f403.jpg)  
图1.13

![](images/91429e42c8b26bc05b922ee0eaee94863b8e6d5225b5f0a7a93b2264ec4489b5.jpg)  
图1.14

习题 1.7 求出从源点（2,8,7）到场点（4,6,8）的间隔矢量 z，求出它的大小 z，给出单位矢量 $\hat{z}$ 。

## 1.1.5 矢量如何变换 $^{3}$

将向量定义为“具有大小和方向的量”并不完全令人满意：方向的精确含义是什么？这听起来有点玄学的味道，但是我们很快会遇到一类微商看起来很像矢量，我们想确定它们究竟是不是矢量。

你们可能会说只要具有三个分量且在做加法时可以适当地合并就是一个矢量。那么好吧，想一想如下问题：假设我们有一桶水果，里面有 $N_{x}$ 个梨、 $N_{y}$ 个苹果、 $N_{z}$ 个香蕉。 $N = N_{x}\hat{x} + N_{y}\hat{y} + N_{z}\hat{z}$ 是一个矢量吗？它具有三个分量，当你与装有 $M_{x}$ 个梨、 $M_{y}$ 个苹果、 $M_{z}$ 个香蕉的另一桶水果相加，结果是 $(N_{x} + M_{x})$ 个梨、 $(N_{y} + M_{y})$ 个苹果和 $(N_{z} + M_{z})$ 个香蕉，这同矢量相加确实很像。但是在物理的意义上它显然不是矢量，因为它根本没有方向。错误究竟出在什么地方呢？

答案是，当你做变换坐标系时，N 不能够正确地（像一个矢量）那样变换。当然，我们用来描述空间中位置的坐标系是完全任意的，但是当从一个坐标系变换到另一个坐标系时，矢量的分量有着特定的变换规律。假设， $\bar{x},\bar{y},\bar{z}$ 坐标系是相对于 x,y,z 坐标系统共同坐标轴 $x=\bar{x}$ 旋转一个角度 $\phi$ 得到的。由图 1.15 得

$$
A _ {y} = A \cos \theta , \quad A _ {z} = A \sin \theta
$$

![](images/89db5d8229678db1529c0a2b78cc1081daac5271eae38c36182301d1ee79a116.jpg)  
图1.15

而

$$
\begin{array}{r l} & {\bar {A} _ {y} = A \cos \bar {\theta} = A \cos (\theta - \phi) = A \left(\cos \theta \cos \phi + \sin \theta \sin \phi\right)} \\ & {\qquad = \cos \phi A _ {y} + \sin \phi A _ {z}} \\ & {\bar {A} _ {z} = A \sin \bar {\theta} = A \sin (\theta - \phi) = A \left(\sin \theta \cos \phi - \cos \theta \sin \phi\right)} \\ & {\qquad = - \sin \phi A _ {y} + \cos \phi A _ {z}} \end{array}
$$

我们可以利用矩阵表示法来表达这些结论：

$$
\binom{\bar {A} _ {y}}{\bar {A} _ {z}} = \left( \begin{array}{c c} \cos \phi & \sin \phi \\ - \sin \phi & \cos \phi \end{array} \right) \binom{A _ {y}}{A _ {z}}\tag{1.29}
$$

更一般地说，对绕三维空间中一个任意轴的转动，变换规律为

$$
\left( \begin{array}{l} \bar {A} _ {x} \\ \bar {A} _ {y} \\ \bar {A} _ {z} \end{array} \right) = \left( \begin{array}{l l l} R _ {x x} & R _ {x y} & R _ {x z} \\ R _ {y x} & R _ {y y} & R _ {y z} \\ R _ {z x} & R _ {z y} & R _ {z z} \end{array} \right) \left( \begin{array}{l} A _ {x} \\ A _ {y} \\ A _ {z} \end{array} \right)\tag{1.30}
$$

或者，更紧凑地，

$$
\bar {A} _ {i} = \sum_ {j = 1} ^ {3} R _ {i j} A _ {j}\tag{1.31}
$$

这里指标 1 对应 x，2 对应 y，3 对应 z。对于给定的转动，矩阵 R 的元素可以通过与我们上面求解绕 x 轴旋转的三角函数类似方法来确定。

到现在为止：N 的分量是按这种方式变换的吗？当然不是——它与你选用什么坐标系表示空间位置无关，无论用什么坐标系桶里的苹果数目是不变的。你不能由选择不同的坐标轴把梨变为香蕉，但是你可以把 $A_{x}$ 转换为 $\bar{A}_{y}$ 。那么，从形式上讲，当你改变坐标系时，任何矢量的三个分量都是以与位移矢量相同的方式进行变换的。总而言之，位移矢量是所有矢量的范本 $^{4}$ 。

顺便提及，一个（二阶）张量是一个具有9个分量的量，即 $T_{xx}, T_{xy}, T_{xz}, T_{yx}, \cdots, T_{zz}$ ，它的变换含有两个R因子：

$$
\begin{array}{r l} & {\bar {T} _ {x x} = R _ {x x} \left(R _ {x x} T _ {x x} + R _ {x y} T _ {x y} + R _ {x z} T _ {x z}\right)} \\ & {\qquad + R _ {x y} \left(R _ {x x} T _ {y x} + R _ {x y} T _ {y y} + R _ {x z} T _ {y z}\right)} \\ & {\qquad + R _ {x z} \left(R _ {x x} T _ {z x} + R _ {x y} T _ {z y} + R _ {x z} T _ {z z}\right), \dots} \end{array}
$$

或者，更紧凑地，

$$
\bar {T} _ {i j} = \sum_ {k = 1} ^ {3} \sum_ {l = 1} ^ {3} R _ {i k} R _ {j l} T _ {k l}\tag{1.32}
$$

更一般地，一个 n 阶张量有 n 个指标和 $3^{n}$ 个分量，变换包含有 n 个 R 因子。按照这种分法，矢量是 1 阶张量，标量是 0 阶张量 $^{5}$ 。

习题1.8

(a) 证明点积在二维转动矩阵变换 [式（1.29）] 下不变。（即证明 $\bar{A}_x\bar{B}_x + \bar{A}_y\bar{B}_y = A_xB_x + A_yB_y$ 。）

（b）为使矢量 A 的长度在三维转动矩阵变换下保持不变（对所有矢量 A），三维转动矩阵元 $(R_{ij})$ [式（1.30）] 必须满足什么约束条件？

习题1.9 求绕通过原点及点（1,1,1）的转轴旋转 $120^{\circ}$ 的变换矩阵 $\pmb{R}$ 。当你沿轴向下看向原点时，旋转是顺时针的。

习题1.10

（a）矢量的分量 $^{6}$ 在坐标平移变换下（图 1.16a）是如何变换的？

（b）矢量的分量在坐标反演变换下（图1.16b）是如何变换的？

(c) 在坐标反演变换下，矢量的叉积的分量是如何变换的 [式（1.13）]？（由于这个“反常”行为，两个矢量叉积习惯称为赝矢量。）两个赝矢量的叉积是一个矢量，还是一个赝矢量？给出力学中的两个赝矢量例子。

(d) 三个矢量的标量混合积在坐标反演变换下如何？（这样的标量称为赝标量。）

![](images/51404884c831d232833ef138534d1a3a420ee8351c86981a3b24c86874726459.jpg)  
图1.16

## 1.2 微分运算

## 1.2.1 “常”微分

假定我们有一个单变量函数 $f(x)$ 。问：它的导数 $\mathrm{df} / \mathrm{dx}$ 对我们有什么作用？答案：它告诉我们，当自变量 $x$ 有一个很小的改变 $\mathrm{dx}$ 时， $f(x)$ 的变化有多快：

$$
\mathrm{d} f = \left(\frac {\mathrm{d} f}{\mathrm{d} x}\right) \mathrm{d} x\tag{1.33}
$$

总之：如果我们使 $x$ 增加一个无限小量 $\mathrm{dx}$ ，则 $f$ 的变化量为 $\mathrm{df}$ ；导数是比例因子。例如，在图1.17a中，函数随 $x$ 的变化很缓慢，相应的导数较小。在图1.17b中，当远离点时， $f$ 随 $x$ 的增加很快，相应的导数较大。

几何解释：导数 $\mathrm{df} / \mathrm{dx}$ 是 $f$ 与 $x$ 关系图形的斜率。

![](images/ed3a5c3273f4106e1818143b9777928adebb8939f56a72582d5624a1fb2337c9.jpg)

![](images/22a90bdc68ddf14bc7e75a3319204291630304b7468d82156d3760ad7de3b724.jpg)  
图1.17

## 1.2.2 梯度

现在我们假定有一三个变量的函数——比如，这个房间的温度 $T(x, y, z)$ 。（以房间一个角落为原点建立坐标系；则对房间内任何一点 $(x, y, z)$ ， $T$ 给出此点温度。）我们想将“导数”的概念推广到像这样的函数，它不依赖于一个变量，而是依赖于三个变量。

若我们移动一个很小的距离，导数告诉我们温度变化得有多快。但现在情况变得更复杂，因为这取决于我们运动的方向：如果我们垂直向上走，温度也许会增加很快，但如果我们水平运动，温度可能没有变化。确切地讲，“温度 T 变化有多快？”的答案有无限多个，对我们想要探讨的每个方向都会有一个答案。

还好，问题并不像看上去那样糟糕。偏导数的定理指出

$$
\mathrm{d} T = \left(\frac {\partial T}{\partial x}\right) \mathrm{d} x + \left(\frac {\partial T}{\partial y}\right) \mathrm{d} y + \left(\frac {\partial T}{\partial z}\right) \mathrm{d} z\tag{1.34}
$$

这个定理告诉我们当所有三个变量分别改变无限小量 $\mathrm{dx},\mathrm{dy},\mathrm{dz}$ 时 $T$ 的变化情况。注意到我们并不需要无限多个导数——分别沿坐标轴方向的三个偏导数就足够了。

式（1.34）点积的形式为

$$
\begin{array}{r l} \mathrm{d} T & = \left(\frac {\partial T}{\partial x} \hat {\boldsymbol {x}} + \frac {\partial T}{\partial y} \hat {\boldsymbol {y}} + \frac {\partial T}{\partial z} \hat {\boldsymbol {z}}\right) \cdot (\mathrm{d} x \hat {\boldsymbol {x}} + \hat {\mathrm{d}} y \hat {\boldsymbol {y}} + \mathrm{d} z \hat {\boldsymbol {z}}) \\ & = (\nabla T) \cdot (\mathrm{d} \boldsymbol {l}) \end{array}\tag{1.35}
$$

式中，

$$
\nabla T \equiv \frac {\partial T}{\partial x} \hat {\pmb {x}} + \frac {\partial T}{\partial y} \hat {\pmb {y}} + \frac {\partial T}{\partial z} \hat {\pmb {z}}\tag{1.36}
$$

是 $T$ 的梯度（gradient）。 $\nabla T$ 是一具有三个分量的矢量；它就是我们要找的广义导数。式（1.35）是式（1.33）在三维情况下的推广。

梯度的几何解释：同任何矢量一样，梯度有大小和方向。为给出它的几何意义，利用式（1.1）重新把点积[式（1.35）]写为

$$
\mathrm{d} T = (\nabla T) \cdot (\mathrm{d} \boldsymbol {l}) = | \nabla T | | \mathrm{d} \boldsymbol {l} | \cos \theta\tag{1.37}
$$

其中 $\theta$ 是 $\nabla T$ 与 $\mathrm{d}l$ 之间的夹角。现在，我们若固定 $|\mathrm{d}l|$ 值的大小来考察 $\mathrm{d}T$ 随方向的改变（变化 $\theta$ ），显然 $T$ 改变最大的方向是在 $\theta = 0 (\cos \theta = 1)$ 处。也就是说，当 $|\mathrm{d}l|$ 固定时，我沿 $\nabla T$ 方向运动时 $\mathrm{d}T$ 变化最大。所以，

梯度 $\nabla T$ 指向函数 T 增加最大的方向。

进一步有

$\left|\nabla T\right|$ 给出沿该最大方向变化的斜率的大小（增长率）。

假设你站在一个山坡上，环顾四周，找到最陡的爬坡方向，这就是梯度的方向。现在测量沿这个方向的斜率（上升运行），就得到梯度的大小。（这里我们讨论的函数是山的高度，所依赖的坐标是位置——比如说，纬度和经度。这个函数仅依赖两个变量，而不是三个，不过在二维情况下梯度的几何意义更容易理解。）由式（1.37）可以看出最大下降的方向与最大上升的方向刚好相反，而在为直角时 $(\theta = 90^{\circ})$ ，斜率为零（梯度垂直于等值线）。你可以想象不具有该特性的表面，但它们一定存在有“折”点，并对应着不可微分的函数。

梯度为零意味着什么？如果在点 $(x, y, z) \nabla T = 0$ ，则在发生很小的位移时都有 $\mathrm{d}T = 0$ 。这说明该点是函数 $T(x, y, z)$ 的稳定点（stationary point）。它可以是极大点（山峰），也可以是极小点（山谷），或鞍点（对某个方向是最大点，对另外的方向是最小点），或“肩点”（上升或下降中的平坦处）。这同单变量函数的情况类似，导数为零处表明该点存在极大、极小或平直。特别是，如果你想求出有三变量函数的极值位置，令它的梯度为零。

方向的增加率是1。

习题1.11 求出下列函数的梯度：

(a) $f(x,y,z) = x^{2} + y^{3} + z^{4}$ .

(b) $f(x,y,z) = x^{2}y^{3}z^{4}$ .

(c) $f(x,y,z) = \mathrm{e}^{x}\sin (y)\ln (z).$

习题 1.12 某座山上每处的高度（以英尺计量）由函数

$$
h (x, y) = 1 0 \left(2 x y - 3 x ^ {2} - 4 y ^ {2} - 1 8 x + 2 8 y + 1 2\right)
$$

给出，式中 $x$ 代表距南哈德利以东的距离， $y$ 是距它以北的距离（以英里为单位）。

(a) 山顶位于何处?

(b) 山的高度是多少?

（c）在距南哈德利东1英里、北1英里的点陡坡的斜率是多少（以英尺/每英里表示）？在这点的什么方向最陡？

\- 习题1.13 设 $\pmb{\nu}$ 是从固定点 $(x', y', z')$ 到固定点 $(x, y, z)$ 的间隔矢量，并设 $\pmb{\nu}$ 是它的长度。证明 (a) $\nabla (\nu^2) = 2\pmb{\nu}$ .

(b) $\nabla (1 / 2) = -\frac{\hat{n}}{r^2}.$

(c) $\nabla (z^n)$ 的一般表达式是什么？

!习题 1.14 设 f 仅是两个变量 $(y,z)$ 的函数。证明梯度 $\nabla f = (\partial f/\partial y)\hat{y} + (\partial f/\partial z)\hat{z}$ 在转动变换下变换为一个矢量，式（1.29）。[提示： $(\partial f/\partial\bar{y}) = (\partial f/\partial y)(\partial y/\partial\bar{y}) + (\partial f/\partial z)(\partial z/\partial\bar{y})$ ，对 $\partial f/\partial\bar{z}$ 有类似的表达式。已知 $\bar{y} = y\cos\phi + z\sin\phi, \bar{z} = -y\sin\phi + z\cos\phi$ ；由此求出 y, z （作为 $\bar{y}, \bar{z}$ 的函数），然后计算出所需的导数 $\partial y/\partial\bar{y}, \partial z/\partial\bar{y}$ 等。]

## 1.2.3 $\nabla$ 算符

梯度 $\nabla$ 的形式看起来像一个矢量，它与一个标量 T“相乘”：

$$
\nabla T = \left(\hat {\boldsymbol {x}} \frac {\partial}{\partial x} + \hat {\boldsymbol {y}} \frac {\partial}{\partial y} + \hat {\boldsymbol {z}} \frac {\partial}{\partial z}\right) T\tag{1.38}
$$

（这一次，我把单位矢量写在左边，这样就没有人会认为是 $\partial \hat{x} / \partial x$ ，以此类推—— $\partial \hat{x} / \partial x$ 将是零，因为 $\hat{x}$ 是常矢量。）式（1.38）括号中的项称为“del”：

$$
\boxed {\nabla = \hat {x} \frac {\partial}{\partial x} + \hat {y} \frac {\partial}{\partial y} + \hat {z} \frac {\partial}{\partial z}}\tag{1.39}
$$

当然，在通常意义上， $\nabla$ 并不是个矢量。事实上，除非我们把它作用在一个函数上，否则它没有多大的含义。此外，它也不是与 $T$ “相乘”，而是对跟在它后面标量进行求导数的一个指令。那么，准确地说，我们说 $\nabla$ 是作用于 $T$ 的矢量算符（vector operator），而不是乘以 $T$ 的矢量。

然而，有了这个性质， $\nabla$ 几乎在所有方面都像一般矢量；如果我们仅仅将“乘法”理解为“作用”，那么几乎任何用其他矢量可以完成的事情也可以用 $\nabla$ 完成。所以一定要认真对待 $\nabla$ 的矢量特征：它是一个了不起的简化符号，如果你读过麦克斯韦没有使用 $\nabla$ 写的电磁学原著，你就会深深感受到使用它的好处。

一般的矢量有三种乘法：

1. 与一个标量 a 相乘：Aa;

2. 与矢量 B 点乘: $A \cdot B$ ;

3. 与矢量 B 叉乘： $A \times B$ .
相应的， $\nabla$ 也有三种作用方式：

1. 作用在一个标量函数 T 上： $\nabla T$ （梯度）；

2. 通过点积形式作用在一个矢量函数 v 上： $\nabla \cdot v$ （散度）；

3. 通过叉积形式作用在一个矢量函数 $\pmb{v}$ 上： $\nabla \times \pmb{v}$ （旋度）. 梯度前面我们已经讨论过了。在接下来的部分中，我们将研究另外两个矢量导数：散度和旋度。

## 1.2.4 散度

根据 $\nabla$ 的定义，我们构造散度：

$$
\begin{array}{r l} \nabla \cdot \boldsymbol {v} & = \left(\hat {\boldsymbol {x}} \frac {\partial}{\partial x} + \hat {\boldsymbol {y}} \frac {\partial}{\partial y} + \hat {\boldsymbol {z}} \frac {\partial}{\partial z}\right) \cdot (v _ {x} \hat {\boldsymbol {x}} + v _ {y} \hat {\boldsymbol {y}} + v _ {z} \hat {\boldsymbol {z}}) \\ & = \frac {\partial v _ {x}}{\partial x} + \frac {\partial v _ {y}}{\partial y} + \frac {\partial v _ {z}}{\partial z} \end{array}\tag{1.40}
$$

注意到矢量函数 $v^{7}$ 的散度本身 $\nabla \cdot v$ 是标量。

几何解释：散度这个名字选的很好，因为 $\nabla \cdot v$ 是矢量 v 从所讨论点向外扩散（发散）程度的量度。例如，图 1.18a 所给矢量函数有很大的（正值）散度（若箭头指向里面，它的散度是负值）；图 1.18b 所给函数的散度为零；同样，图 1.18c 所给函数的散度为正值。（请大家明白这里的 v 是一个函数——空间中的每个点都有一个不同的向量。当然，我只能在图中几个代表性的位置画上箭头。）

![](images/fe8ea60dd7359a870dbb182b439e95463b37da290bf57ec9341da1d7f64906a8.jpg)  
a)

![](images/eadb715a5b4cd067bd8aa4a5bfd2f668513b1bd73a6f703157cc9a91ccf4111d.jpg)  
b)  
图1.18

![](images/6bfd769afc7f7b706fb778679dab9c7ae3d65814cea040e77a07bbf310a15a26.jpg)  
c)

假设你站在池塘的边上，往水面上撒些锯末或松针。如果这些材料扩散开；你就把它放在了散度为正的点上；如果它们聚集起来，你就把它扔在了散度为负的点上。[在这个模型中，矢量函数 v 是表面水流的速度——这是一个二维情况的例子，但是它有助于让我们感受散度的含义。散度为正值的点称为源点，或者龙头，散度为负值的点称为渊点（流入）。]

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
例题1.4 假设图1.18中的函数为 $v_{a} = r = x\hat{x} +y\hat{y} +z\hat{z}, v_{b} = \hat{z}, v_{c} = z\hat{z}$ 。计算其散度。[解答] $\nabla \cdot \pmb {v}_{a} = \frac{\partial}{\partial x}(x) + \frac{\partial}{\partial y}(y) + \frac{\partial}{\partial z}(z) = 1 + 1 + 1 = 3$ 正如预期的那样，该函数有正的散度。$\nabla \cdot \pmb {v}_b = \frac{\partial}{\partial x}(0) + \frac{\partial}{\partial y}(0) + \frac{\partial}{\partial z}(1) = 0 + 0 + 0 = 0$ 果不其然。$\nabla \cdot \pmb {v}_c = \frac{\partial}{\partial x}(0) + \frac{\partial}{\partial y}(0) + \frac{\partial}{\partial z}(z) = 0 + 0 + 1 = 1$
</div>

习题1.15 计算下列矢量函数的散度：

(a) $v_{a}=x^{2}\hat{x}+3xz^{2}\hat{y}-2xz\hat{z}.$

(b) $v_{b}=xy\hat{x}+2yz\hat{y}+3xz\hat{z}.$

(c) $v_{c}=y^{2}\hat{x}+(2xy+z^{2})\hat{y}+2yz\hat{z}.$

习题1.16 画出矢量函数

$$
\boldsymbol {v} = \frac {\hat {\boldsymbol {r}}}{r ^ {2}}
$$

的草图，并计算它的散度。答案会使你大吃一惊……你能解释一下吗？

！习题1.17在二维情况下，证明在转动变换下的散度为标量。[提示：利用式（1.29）求出 $\bar{v}_y,\bar{v}_z$ ，利用习题1.14的方法计算出导数。你的目的是证明 $\partial \bar{v}_y / \partial \bar{y} +\partial \bar{v}_z / \partial \bar{z} = \partial v_y / \partial y + \partial v_z / \partial z$ 。]

## 1.2.5 旋度

根据 $\nabla$ 的定义，我们可构造旋度：

$$
\begin{array}{r l} \nabla \times \boldsymbol {v} = & \left| \begin{array}{c c c} \hat {\boldsymbol {x}} & \hat {\boldsymbol {y}} & \hat {\boldsymbol {z}} \\ \partial / \partial x & \partial / \partial y & \partial / \partial z \\ v _ {x} & v _ {y} & v _ {z} \end{array} \right| \\ & = \hat {\boldsymbol {x}} \left(\frac {\partial v _ {z}}{\partial y} - \frac {\partial v _ {y}}{\partial z}\right) + \hat {\boldsymbol {y}} \left(\frac {\partial v _ {x}}{\partial z} - \frac {\partial v _ {z}}{\partial x}\right) + \hat {\boldsymbol {z}} \left(\frac {\partial v _ {y}}{\partial x} - \frac {\partial v _ {x}}{\partial y}\right) \end{array}\tag{1.41}
$$

请注意：矢量函数的旋度同任何叉积一样 $^{8}$ ，仍然是一个矢量。

几何解释：旋度这个名字也是精心选择的，因为 $\nabla \times \boldsymbol{v}$ 是矢量 $\boldsymbol{v}$ 在所讨论点涡旋程度的量度。这样图1.18所给的三个函数旋度都为零（你可以很容易验证它们），而图1.19所给函数有一个很大的旋度，根据右手规则，它旋度的方向指向 z 轴方向。再一次假设你站在池塘边，水面上漂浮一个小桨轮（一个软木塞沿其径向插几个牙签就行）；若它开始旋转，那么你就把它放在旋度不为零的位置上了。漩涡是具有较大旋度的区域。

![](images/79e4e10ce77bf8cd2cf18488cb1fba45ba63aed8d04bb4d14b15bad2cb24f505.jpg)  
图1.19

例题1.5 假设图1.19a中所画的矢量函数为 $v_{a} = -y\hat{x} + x\hat{y}$ ，且图1.19b中为 $v_{b} = x\hat{y}$ 。计算它们的旋度。

[解答]

$$
\nabla \times \boldsymbol {v} _ {a} = \left| \begin{array}{c c c} \hat {\boldsymbol {x}} & \hat {\boldsymbol {y}} & \hat {\boldsymbol {z}} \\ \partial / \partial x & \partial / \partial y & \partial / \partial z \\ - y & x & 0 \end{array} \right| = 2 \hat {\boldsymbol {z}}
$$

和

$$
\nabla \times \boldsymbol {v} _ {b} = \left| \begin{array}{c c c} \hat {\boldsymbol {x}} & \hat {\boldsymbol {y}} & \hat {\boldsymbol {z}} \\ \partial / \partial x & \partial / \partial y & \partial / \partial z \\ 0 & x & 0 \end{array} \right| = \hat {\boldsymbol {z}}
$$

果不其然，这些旋度的方向指向 +z 方向。（顺便说一句，正如你从图片中可以猜到的那样，他们的散度为零：它们没有“扩散”，只是“打旋”。）

习题 1.18 计算习题 1.15 中矢量函数的旋度。

习题1.19 在 $xy$ 平面上画一个圆。在几个代表点处绘制与圆相切的矢量 $\pmb{v}$ ，方向指向顺时针方向。通过比较相邻向量，确定 $\partial v_{x} / \partial y$ 和 $\partial v_{y} / \partial x$ 的正负号。那么，根据方程（1.41），给出 $\nabla \times \pmb{v}$ 的方向？阐明这个例子如何说明旋度的几何解释。

习题1.20 构造一个处处具有零散度和零旋度的矢量函数。（当然，常矢量可以满足这些要求，但要构造比它更有趣的。）

## 1.2.6 乘积定则

许多定则有利于一般导数的运算，比如求和定则：

$$
{\frac {\mathrm{d}}{\mathrm{d} x}} (f + g) = {\frac {\mathrm{d} f}{\mathrm{d} x}} + {\frac {\mathrm{d} g}{\mathrm{d} x}}
$$

乘以常数的定则：

$$
{\frac {\mathrm{d}}{\mathrm{d} x}} (k f) = k {\frac {\mathrm{d} f}{\mathrm{d} x}}
$$

乘积定则：

$$
{\frac {\mathrm{d}}{\mathrm{d} x}} (f g) = f {\frac {\mathrm{d} g}{\mathrm{d} x}} + g {\frac {\mathrm{d} f}{\mathrm{d} x}}
$$

以及商定则：

$$
{\frac {\mathrm{d}}{\mathrm{d} x}} \left({\frac {f}{g}}\right) = {\frac {g {\frac {\mathrm{d} f}{\mathrm{d} x}} - f {\frac {\mathrm{d} g}{\mathrm{d} x}}}{g ^ {2}}}
$$

对矢量导数也有类似的关系，因此，

$$
\nabla (f + g) = \nabla f + \nabla g, \quad \nabla \cdot (\boldsymbol {A} + \boldsymbol {B}) = (\nabla \cdot \boldsymbol {A}) + (\nabla \cdot \boldsymbol {B})
$$

$$
\nabla \times (\boldsymbol {A} + \boldsymbol {B}) = (\nabla \times \boldsymbol {A}) + (\nabla \times \boldsymbol {B})
$$

以及

$$
\nabla (k f) = k \nabla f, \quad \nabla \cdot (k \boldsymbol {A}) = k (\nabla \cdot \boldsymbol {A}), \quad \nabla \times (k \boldsymbol {A}) = k (\nabla \times \boldsymbol {A})
$$

你可以自己验证它们。不过乘积定则就没有那么简单了。有两种方法通过两个函数的乘积来构造一个标量：

$$
f g \quad (\text { 两个标量函数的乘积 })
$$

$$
\pmb {A} \cdot \pmb {B} (\text {两个矢量函数的点积})
$$

同样，也有两种方法去构造一个矢量：

$$
f A \text {(标量乘以矢量)}
$$

$$
\pmb {A} \times \pmb {B} (\text {两个矢量的叉积})
$$

相应地，有六条乘积定则，其中两条用于梯度：

(i)

$$
\nabla (f g) = f \nabla g + g \nabla f
$$

(ii)

$$
\nabla (\boldsymbol {A} \cdot \boldsymbol {B}) = \boldsymbol {A} \times (\nabla \times \boldsymbol {B}) + \boldsymbol {B} \times (\nabla \times \boldsymbol {A}) + (\boldsymbol {A} \cdot \nabla) \boldsymbol {B} + (\boldsymbol {B} \cdot \nabla) \boldsymbol {A}
$$

两条用于散度：

(iii)

$$
\nabla \cdot (f \boldsymbol {A}) = f (\nabla \cdot \boldsymbol {A}) + \boldsymbol {A} \cdot (\nabla f)
$$

(iv)

$$
\nabla \cdot (\boldsymbol {A} \times \boldsymbol {B}) = \boldsymbol {B} \cdot (\nabla \times \boldsymbol {A}) - \boldsymbol {A} \cdot (\nabla \times \boldsymbol {B})
$$

两条用于旋度：

(v)

$$
\nabla \times (f \boldsymbol {A}) = f (\nabla \times \boldsymbol {A}) - \boldsymbol {A} \times (\nabla f)
$$

(vi)

$$
\nabla \times (\boldsymbol {A} \times \boldsymbol {B}) = (\boldsymbol {B} \cdot \nabla) \boldsymbol {A} - (\boldsymbol {A} \cdot \nabla) \boldsymbol {B} + \boldsymbol {A} (\nabla \cdot \boldsymbol {B}) - \boldsymbol {B} (\nabla \cdot \boldsymbol {A})
$$

你将经常使用这些乘积定则，所以我将它们放在文前环衬以便参考。这些公式的证明直接由一般导数的积定则给出。例如，

$$
\nabla \cdot (f \boldsymbol {A}) = \frac {\partial}{\partial x} (f A _ {x}) + \frac {\partial}{\partial y} (f A _ {y}) + \frac {\partial}{\partial z} (f A _ {z})
$$

$$
\begin{array}{l} = \left(\frac {\partial f}{\partial x} A _ {x} + f \frac {\partial A _ {x}}{\partial x}\right) + \left(\frac {\partial f}{\partial y} A _ {y} + f \frac {\partial A _ {y}}{\partial y}\right) + \left(\frac {\partial f}{\partial z} A _ {z} + f \frac {\partial A _ {z}}{\partial z}\right) \\ = (\nabla f) \cdot \boldsymbol {A} + f (\nabla \cdot \boldsymbol {A}) \end{array}
$$

还可以制定三个商定则：

$$
\nabla \left(\frac {f}{g}\right) = \frac {g \nabla f - f \nabla g}{g ^ {2}}
$$

$$
\nabla \cdot \left(\frac {\boldsymbol {A}}{g}\right) = \frac {g (\nabla \cdot \boldsymbol {A}) - \boldsymbol {A} \cdot (\nabla g)}{g ^ {2}}
$$

$$
\nabla \times \left(\frac {\pmb {A}}{g}\right) = \frac {g (\nabla \times \pmb {A}) - \pmb {A} \times (\nabla g)}{g ^ {2}}
$$

然而，由于这些公式可以从相应的乘积定则中得到，因此不再单独将他们列出。

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
习题 1.21 证明乘积定则 (i), (iv) 和 (v)。

习题 1.22

(a) 如果 A, B 是两个矢量函数， $(A \cdot \nabla) B$  的含义是什么？（即，以 A, B,  $\nabla$  的直角分量，给出  $(A \cdot \nabla) B$  的 x, y 和 z 分量。）

(a) 计算  $(\hat{r} \cdot \nabla) \hat{r}$ ，其中  $\hat{r}$  是由式（1.21）定义的单位矢量。

(b) 对习题 1.15 中的矢量函数，计算  $(v_{a} \cdot \nabla) v_{b}$ 。

习题 1.23 （仅对喜欢刷题者）证明乘积定则 (ii) 和 (vi)。关于  $(A \cdot \nabla) B$  的定义，请参考习题 1.22。

习题 1.24 推导三个商运算定则。

习题 1.25

(a) 对函数

[ A = x\hat{x} + 2y\hat{y} + 3z\hat{z}; \quad B = 3y\hat{x} - 2x\hat{y} ] 

验证乘积定则 (iv)（分别计算每一项）。

(b) 对乘积定则 (ii) 做上述同样的计算。

(c) 对乘积定则 (vi) 做同样的计算。
</div>

## 1.2.7 二阶导数

梯度、散度和旋度仅是我们用 $\nabla$ 做的一阶导数；通过 $\nabla$ 作用两次可以构造五类的二阶导数。梯度 $\nabla T$ 是个矢量，因此我们可以取它的散度和旋度：

(1) 梯度的散度: $\nabla \cdot (\nabla T)$

(2) 梯度的旋度: $\nabla \times (\nabla T)$

散度 $\nabla \cdot v$ 是个标量——我们仅能对它求梯度：

(3) 散度的梯度: $\nabla (\nabla \cdot \boldsymbol{v})$

旋度 $\nabla \times \pmb{v}$ 是个矢量，因此我们可以求它的散度和旋度：

(4) 旋度的散度: $\nabla \cdot (\nabla \times \boldsymbol{v})$

(5) 旋度的旋度: $\nabla \times (\nabla \times \boldsymbol{v})$

这穷尽了所有的可能性，事实上，并不是所有的可能性都能带来新东西。让我们逐一讨论它们：

(1)

$$
\begin{array}{r l} \nabla \cdot (\nabla T) & = \left(\hat {\boldsymbol {x}} \frac {\partial}{\partial x} + \hat {\boldsymbol {y}} \frac {\partial}{\partial y} + \hat {\boldsymbol {z}} \frac {\partial}{\partial z}\right) \cdot \left(\frac {\partial T}{\partial x} \hat {\boldsymbol {x}} + \frac {\partial T}{\partial y} \hat {\boldsymbol {y}} + \frac {\partial T}{\partial z} \hat {\boldsymbol {z}}\right) \\ & = \frac {\partial^ {2} T}{\partial x ^ {2}} + \frac {\partial^ {2} T}{\partial y ^ {2}} + \frac {\partial^ {2} T}{\partial z ^ {2}} \end{array}\tag{1.42}
$$

这个表示项，我们简写为 $\nabla^2 T$ ，称为 $T$ 的拉普拉斯算子；稍后我们将非常详细地讨论它。注意到标量 $T$ 的拉普拉斯仍是标量。我们偶尔会讨论矢量的拉普拉斯 $\nabla^2 v$ ，我们指的是其矢量的大小，其 $x$ 分量是 $v_x$ 的拉普拉斯算子，以此类推9：

$$
\nabla^ {2} \pmb {v} \equiv (\nabla^ {2} v _ {x}) \hat {\pmb {x}} + (\nabla^ {2} v _ {y}) \hat {\pmb {y}} + (\nabla^ {2} v _ {z}) \hat {\pmb {z}}\tag{1.43}
$$

这只不过是 $\nabla^{2}$ 含义方便实用的扩展。

(2) 梯度的旋度始终为零:

$$
\nabla \times (\nabla T) = \mathbf {0}\tag{1.44}
$$

这是一个很重要的事实，我们会经常用到；你可以很容易地利用 $\nabla$ 的定义式[式（1.39）]证明这一点。请留意，你也许认为式（1.44）是显而易见的——它不就是 $(\nabla \times \nabla)T$ 吗，任何矢量（现在矢量为 $\nabla$ ）与自身的叉积不都是零吗？这种推理是有启发性的，但不是完全决定性的，因为 $\nabla$ 是一个算符，它不是按通常的意义来“相乘”的。事实上，式（1.44）的证明取决于交叉导数的等同性：

$$
{\frac {\partial}{\partial x}} \left({\frac {\partial T}{\partial y}}\right) = {\frac {\partial}{\partial y}} \left({\frac {\partial T}{\partial x}}\right)\tag{1.45}
$$

如果你们认为我过分挑剔，请通过下面一点来验证你的直觉：

$$
(\nabla T) \times (\nabla S)
$$

它总是为零吗？（当然，如果你用一个普通矢量代替 $\nabla$ 的话。）

（3） $\nabla (\nabla \cdot \boldsymbol{v})$ 很少在物理中用到，所以除了散度的梯度（the gradient of the divergence）外它也没有特殊的名称。注意 $\nabla (\nabla \cdot \boldsymbol{v})$ 和矢量的拉普拉斯算子不一样： $\nabla^2 \boldsymbol{v} = (\nabla \cdot \nabla) \boldsymbol{v} \neq \nabla (\nabla \cdot \boldsymbol{v})$ 。

（4）同梯度的旋度一样，旋度的散度也始终为零：

$$
\nabla \cdot (\nabla \times \boldsymbol {v}) = 0\tag{1.46}
$$

你们自己可以证明它。[同样，利用矢量等式 $A \cdot (B \times C) = (A \times B) \cdot C$ ，还有一种非常简洁的证明方法。]

(5) 由 $\nabla$ 的定义，你们可以验证

$$
\nabla \times (\nabla \times \boldsymbol {v}) = \nabla (\nabla \cdot \boldsymbol {v}) - \nabla^ {2} \boldsymbol {v}\tag{1.47}
$$

所以旋度的旋度没有任何新内容；右边第一项正是（3）中所讨论，第二项是一个矢量的拉普拉斯算子。[事实上，式（1.47）通常用于定义矢量的拉普拉斯算子，而不是用式（1.43），式（1.47）明确必须使用直角坐标系。]

实际上，只有两种二阶导数：拉普拉斯算子（这是至关重要的）和散度的梯度（我们很少遇到）。我们可以通过类似的程序来计算三阶导数，但幸运的是，二阶导数对所有物理学需求已经满足了。

导数运算归根到底就是一句话：所有一切都是源于 $\nabla$ 算符，以及对其矢量特性的重视。即使仅记住 $\nabla$ 的定义，你也很容易把其余的一切构造出来。

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
习题 1.26 计算下列函数的拉普拉斯算符：
(a)  $T_{a} = x^{2} + 2xy + 3z + 4$ .
(b)  $T_{b} = \sin x \sin y \sin z$ .
(c)  $T_{c} = e^{-5x} \sin 4y \cos 3z$ .
(d)  $v = x^{2}\hat{x} + 3xz^{2}\hat{y} - 2xz\hat{z}$ .
习题 1.27 证明旋度的散度始终为零，并用习题 1.15 中的函数  $v_{a}$  验证它。
习题 1.28 证明梯度的旋度始终为零，并用习题 1.11 中的函数（b）验证它。
</div>

## 1.3 积分运算

## 1.3.1 线、面和体积分

在电动力学中，我们常遇到几种不同类型的积分，其中最重要的是线（或路径）积分 [line (or path) integrals]、面积分（或通量）(surface integrals) 和体积积分（volume integrals）。

（a）线积分。线积分是由下列形式的表达式表示：

$$
\int_ {a} ^ {b} \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {l}\tag{1.48}
$$

式中， $\pmb{v}$ 是矢量函数， $\mathrm{d}l$ 是无限小位移矢量[式（1.22）]，积分是沿着从 $\pmb{a}$ 点到 $\pmb{b}$ 点的规定路径 $\mathcal{P}$ 进行（图1.20）。如果所讨论的路径形成闭环（即 $a = b$ ），我将在积分号上画一个圆圈表示：

$$
\oint \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {l}\tag{1.49}
$$

在路径上的每一点，我们取 v（在这一点取值）与从该点指向路径上下一点的位移 dl 的点积。对于物理学家而言，线积分最熟悉的例子就是力 F 所做的功： $W = \int F \cdot dl$ 。

![](images/de87563d91787c8c288c79d146f416563cfdb9de2a5ec6b96d61ceafb36c4940.jpg)  
图1.20

通常线积分的值在很大程度上取决于 a 到 b 的路径，但有一类重要的特殊矢量函数，其线积分与路径无关，完全由端点决定。在适当的时候，我们将会讨论这类特殊的矢量。（具有这种性质的力称作保守力。）

例题1.6 沿图1.21中的路径（1）和（2）分别计算函数 $v = y^2\hat{x} + 2x(y + 1)\hat{y}$ 从点 $a = (1,1,0)$ 到点 $b = (2,2,0)$ 的线积分。对沿（1）从 $\pmb{a}$ 点到 $\pmb{b}$ 点并沿（2）回到 $\pmb{a}$ 点的回路，积分 $\oint v\cdot dl$ 是多少？

![](images/299359c3301aea38aad1faf8cb1106af4b298aa6b5e8233f74d9e347a23d5303.jpg)  
图1.21

[解答] 如所定义的那样， $\mathrm{d}l = \mathrm{d}x\hat{x} + \mathrm{d}y\hat{y} + \mathrm{d}z\hat{z}$ 。路径（1）含有两个部分。沿水平方向线段有 dy = dz = 0，所以
(i) $dl = dx \hat{x}, y = 1, v \cdot dl = y^{2} dx = dx,$ 即 $\int v \cdot dl = \int_{1}^{2} dx = 1.$ 沿竖直线段，dx=dz=0，所以

(ii) $\mathrm{d}\pmb {l} = \mathrm{d}y\hat{\pmb{y}},\quad x = 2,\quad \pmb {v}\cdot \mathrm{d}\pmb {l} = 2x(y + 1)\mathrm{d}y = 4(y + 1)\mathrm{d}y$ ，所以

$$
\int \boldsymbol {v} \cdot \mathrm{d} l = 4 \int_ {1} ^ {2} (y + 1) \mathrm{d} y = 1 0
$$

沿路径（1），所以有

$$
\int_ {a} ^ {b} \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {l} = 1 + 1 0 = 1 1
$$

同样，对于沿路径（2）有， $x = y, \mathrm{d}x = \mathrm{d}y$ 及 $\mathrm{d}z = 0$ ，所以

$$
\mathrm{d} \boldsymbol {l} = \mathrm{d} x \hat {\boldsymbol {x}} + \mathrm{d} y \hat {\boldsymbol {y}}, \quad \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {l} = x ^ {2} \mathrm{d} x + 2 x (x + 1) \mathrm{d} x = (3 x ^ {2} + 2 x) \mathrm{d} x
$$

以及

$$
\int_ {a} ^ {b} \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {l} = \int_ {1} ^ {2} (3 x ^ {2} + 2 x) \mathrm{d} x = (x ^ {3} + x ^ {2}) \Big | _ {1} ^ {2} = 1 0
$$

（这里的策略是用一个变量来表示一切，也可以去掉 $x$ ，改成 $y_{0}$ ）

对于沿（1）出发再沿（2）返回的回路，有

$$
\oint \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {l} = 1 1 - 1 0 = 1
$$

（b）面积分。面积分由下列形式表达式表示：

$$
\int_ {\mathcal {S}} \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {a}\tag{1.50}
$$

其中 v 是某个矢量函数，积分在特定曲面 S 上。这里 da 是无限小面元，它的方向垂直于表面（图 1.22）。当然，对任何面元都有两个（方向相反的）方向和它垂直，因此面积分值的符号本身不是很明确。如果表面是闭合的（比如一个气球的表面），在这种情况下，我将在积分符号上再次画一个圆：

$$
\oint \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {a}
$$

则习惯规定“向外”为正，但是对于非闭合曲面其方向是任意的。如果 v 表示流体的流量（单位时间单位面积流过的质量），则 $\int v \cdot da$ 表示单位时间内通过被积表面积的总质量——因此有另外的名字“通量”。

通常，曲面积分的值取决于所选的特定曲面，但有一类特殊的矢量函数，它不依赖曲面的选择，完全由其边界线决定。下面一个重要的任务就是描述这类特殊的函数。

![](images/d3e483e79037911593f9506902012807a64a7bf110ebad58a237fb9db17fc904.jpg)  
图1.22

(ii) $x = 0, \mathrm{d}a = -\mathrm{d}y\mathrm{d}z\hat{x}, v \cdot \mathrm{d}a = -2xz\mathrm{d}y\mathrm{d}z = 0$ ，所以

$$
\int \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {a} = 0
$$

(iii) $y = 2, \quad \mathrm{d}\pmb {a} = \mathrm{d}x\mathrm{d}z\hat{\pmb{y}},\quad \pmb {v}\cdot \mathrm{d}\pmb {a} = (x + 2)\mathrm{d}x\mathrm{d}z,$ 所以

$$
\int \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {a} = \int_ {0} ^ {2} (x + 2) \mathrm{d} x \int_ {0} ^ {2} \mathrm{d} z = 1 2
$$

（iv） $y = 0$ ， $\mathrm{d}\pmb {a} = -\mathrm{d}x\mathrm{d}z\hat{\pmb{y}},\quad \pmb {v}\cdot \mathrm{d}\pmb {a} = -(x + 2)\mathrm{d}x\mathrm{d}z,$ 所以

$$
\int \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {a} = - \int_ {0} ^ {2} (x + 2) \mathrm{d} x \int_ {0} ^ {2} \mathrm{d} z = - 1 2
$$

(v) $z = 2, \mathrm{d}a = \mathrm{d}x\mathrm{d}y\hat{z}, v \cdot \mathrm{d}a = y(z^2 - 3)\mathrm{d}x\mathrm{d}y = y\mathrm{d}x\mathrm{d}y$ ，所以

$$
\int \pmb {v} \cdot \mathrm{d} \pmb {a} = \int_ {0} ^ {2} \mathrm{d} x \int_ {0} ^ {2} y \mathrm{d} y = 4
$$

![](images/f01305e6ae36d46fb9848a9ed03401bc71b174632e5eb9e36057fde4837414ff.jpg)  
图1.23

（c）体积分。体积分由下列形式的表达式表示：

$$
\int_ {\mathcal {V}} T \mathrm{d} \tau\tag{1.51}
$$

式中， $T$ 是一个标量函数， $\mathrm{d}\tau$ 是一无限小体积元。在直角坐标系中

$$
\mathrm{d} \tau = \mathrm{d} x \mathrm{d} y \mathrm{d} z\tag{1.52}
$$

例如，如果 $T$ 是一个物体的密度（可能是逐点变化的），则体积分给出这个物体的总质量。有时我们也会遇到矢量函数的体积分：

$$
\begin{array}{r l} \int \boldsymbol {v} \mathrm{d} \tau & = \int (v _ {x} \hat {\boldsymbol {x}} + v _ {y} \hat {\boldsymbol {y}} + v _ {z} \hat {\boldsymbol {z}}) \mathrm{d} \tau \\ & = \hat {\boldsymbol {x}} \int v _ {x} \mathrm{d} \tau + \hat {\boldsymbol {y}} \int v _ {y} \mathrm{d} \tau + \hat {\boldsymbol {z}} \int v _ {z} \mathrm{d} \tau \end{array}\tag{1.53}
$$

因为直角坐标系的单位矢量（ $\hat{x}, \hat{y}, \hat{z}$ ）是常数，它们可以移至积分号外。

例题1.8 计算图1.24中三棱体上函数 $T = xyz^2$ 的体积分。

[解答] 你可以按照任何顺序做这个三重积分。让我们先对 $x$ 做积分：区间需从0积到 $(1 - y)$ ；然后对 $y$ 积分（从0到1）；最后对 $z$ 积分（从0到3）；

$$
\begin{array}{r l} & {\int T \mathrm{d} \tau = \int_ {0} ^ {3} z ^ {2} \left\{\int_ {0} ^ {1} y \left[ \int_ {0} ^ {1 - y} x \mathrm{d} x \right] \mathrm{d} y \right\} \mathrm{d} z} \\ & {\qquad = \frac {1}{2} \int_ {0} ^ {3} z ^ {2} \mathrm{d} z \int_ {0} ^ {1} (1 - y) ^ {2} y \mathrm{d} y = \frac {1}{2} (9) \left(\frac {1}{1 2}\right) = \frac {3}{8}} \end{array}
$$

![](images/1c648d92005efc734b839d0b87366782df29cf0538fd2ba48d06c7659a73c0aa.jpg)  
图1.24

习题1.29 从原点到点（1,1,1）沿所给出三种不同路径对函数 $v = x^{2}\hat{x} + 2yz\hat{y} + y^{2}\hat{z}$ 进行线积分：

(a) $(0,0,0)\rightarrow (1,0,0)\rightarrow (1,1,0)\rightarrow (1,1,1)$ 。

(b) $(0,0,0)\rightarrow (0,0,1)\rightarrow (0,1,1)\rightarrow (1,1,1)$ 。

(c) 两点的直线。

(d) 沿着路径（a）出发并沿路径（b）返回的闭环路径的线积分是多少？

习题 1.30 计算例题 1.7 中函数在立方体的底面的表面积分。为了保持一致性，取“向上”为正方向。曲面积分是否仅取决于此函数的边界？该立方体的闭合面的总通量是什么（包括底面）？[提示：对闭合曲面，正方向指向外，所以底面的正方向朝下。]

习题1.31 计算函数 $T = z^2$ 在正四面体上的体积分，四面体的顶角位于 $(0,0,0), (1,0,0), (0,1,0), (0,0,1)$ 。

## 1.3.2 积分基本定理

设 $f(x)$ 是单变量函数。积分的基本定理（fundamental theorem of calculus）指出：

$$
\int_ {a} ^ {b} \frac {\mathrm{d} f}{\mathrm{d} x} \mathrm{d} x = f (b) - f (a)\tag{1.54}
$$

如果这个形式你看起来不熟悉，我把它写成另一种形式：

$$
\int_ {a} ^ {b} F (x) \mathrm{d} x = f (b) - f (a)
$$

式中， $\mathrm{df} / \mathrm{dx} = F(x)$ 。基本定理告诉你如何对 $F(x)$ 求积分：想出一个导数为 $F$ 的函数 $f(x)$ 。几何解释：根据式（1.33）， $\mathrm{df} = (\mathrm{df} / \mathrm{dx}) / \mathrm{dx}$ 是从 $x$ 变到 $(x + \mathrm{dx})$ 时 $f$ 的无限小变化。基本定理[式（1.54）]是说，如果你把从 $a$ 到 $b$ 的区间（图1.25）分割成许多小间隔dx，并把每个间隔的增量 df 加起来，结果（不出所料）等于 f 的总变化： $f(b)-f(a)$ 。换句话说，有两种方法决定函数的总变化：要么是减去末端的值，要么一步一步地进行，将所有微小的增量加起来。无论哪种方法结果是一样的。

![](images/70e49595bde657355bce68719206ee67ef9c6be69375d1b9125a256706351918.jpg)  
图1.25

请注意基本定理的基本形式：某个区域上导数的积分由端点（边界）处的函数值给出。在矢量积分中有三类导数（梯度、散度和旋度），每个都有自己的“基本定理”，形式基本相同。这里我不打算去证明这些定理，而仅解释它们的含义，力图使它们更容易理解。有关的证明在附录 A 中给出。

## 1.3.3 梯度基本定理

假设我们有一个三变量 $T(x,y,z)$ 的标量函数。从 $\pmb{a}$ 点开始，我们移动一个小的位移 $\mathrm{d}l_{1}$ （图1.26）。根据式（1.37），函数 $T$ 将改变一个量

$$
\mathrm{d} T = (\nabla T) \cdot \mathrm{d} l _ {1}
$$

现在我们再向前移动一个小的位移 $\mathrm{d}l_{2}$ , $T$ 的增量为 $(\nabla T) \cdot \mathrm{d}l_{2}$ 。通过这种方式, 我们一步一步到达 $\pmb{b}$ 点。在每一步中我们计算 $T$ 的梯度与无限小位移的点积, 从而给出函数的增量 $\mathrm{d}T$ 。很显然, (沿所选路径) 从 $\pmb{a}$ 点到 $\pmb{b}$ 点, $T$ 总的变化为

$$
\boxed {\int_ {a} ^ {b} (\nabla T) \cdot \mathrm{d} \boldsymbol {l} = T (\boldsymbol {b}) - T (\boldsymbol {a})}\tag{1.55}
$$

这是梯度的基本定理（fundamental theorem for gradients）；同“一般的”基本定理一样，它指出导数（现在是梯度）的积分（这里是线积分）是由函数在边界（a 和 b）的数值所确定的。

![](images/6506a72944b20f5d7c4e16abf676ebf3eb497fda9609287a4b594b5ae2fe2538.jpg)  
图1.26

几何解释：假设你想确定埃菲尔铁塔的高度。你可以攀爬塔梯，用尺子测量每个台阶的高度，然后把它们加在一起[这就是式（1.55）的左边]，你也可以用一个测高仪测出塔顶和塔底的读数，然后把两个读数相减[这就是式（1.55）的右边]；不论哪种方法，你都得到同样的结果（这就是基本定理）。

顺便提及，正如我们在例题1.6发现的那样，线积分通常取决于从 $\pmb{a}$ 和 $\pmb{b}$ 的路径。但式（1.55）右边没有提到路径，只与端点有关。显然梯度具有其线积分与路径无关的特性：推论 $1: \int_{a}^{b} (\nabla T) \cdot \mathrm{d}l$ 与从 $\pmb{a}$ 到 $\pmb{b}$ 的路径无关。

推论2：由于起点和终点重合， $T(\pmb {b}) - T(\pmb {a}) = 0$ ，因此 $\oint (\nabla T)\cdot \mathrm{d}\pmb {l} = 0$

例题1.9 令 $T = xy^2$ ，并假设 $\pmb{a}$ 点为原点 $(0,0,0)$ ， $\pmb{b}$ 点为 $(2,1,0)$ ，验证梯度的基本定理。[解答] 尽管梯度的积分与路径无关，计算时我们仍需选定一条具体路径。设先沿 $x$ 轴出发（步骤i），然后向上（步骤ii）（图1.27）。和以前一样， $\mathrm{d}\pmb{l} = \mathrm{d}x\hat{x} + \mathrm{d}y\hat{y} + \mathrm{d}z\hat{z}$ ； $\nabla T = y^2\hat{x} + 2xy\hat{y}$ 。（i） $y = 0$ ； $\mathrm{d}\pmb{l} = \mathrm{d}x\hat{x}$ ， $\nabla T \cdot \mathrm{d}\pmb{l} = y^2\mathrm{d}x = 0$ ，所以 $\int_{\mathrm{i}} (\nabla T) \cdot \mathrm{d}\pmb{l} = 0$ （ii） $x = 2$ ； $\mathrm{d}\pmb{l} = \mathrm{d}y\hat{y}$ ， $\nabla T \cdot \mathrm{d}\pmb{l} = 2xy\mathrm{d}y = 4y\mathrm{d}y$ ，所以 $\int_{\mathrm{ii}} (\nabla T) \cdot \mathrm{d}\pmb{l} = \int_{0}^{1} 4y\mathrm{d}y = 2y^2\bigg|_0^1 = 2$ 总的线积分是2。这与基本定理一致吗？当然一致： $T(\pmb{b}) - T(\pmb{a}) = 2 - 0 = 2$ 。

![](images/ce889fb666412a52a3b62766bac9f65c9191abc4fc0c0d4c27f99899e06914d3.jpg)  
图1.27

现在，为了让你们相信答案与路径无关，让我沿路径iii（从 $\pmb{a}$ 点到 $\pmb{b}$ 点的直线）重新计算该积分：（iii） $y = \frac{1}{2} x;\quad \mathrm{d}y = \frac{1}{2}\mathrm{d}x,\quad \nabla T\cdot \mathrm{d}l = y^2\mathrm{d}x + 2xy\mathrm{d}y = \frac{3}{4} x^2\mathrm{d}x$ ，所以 $\int_{\mathrm{iii}}(\nabla T)\cdot \mathrm{d}l = \int_0^2\frac{3}{4} x^2\mathrm{d}x = \left.\frac{1}{4} x^3\right|_0^2 = 2$

习题1.32 利用 $T = x^{2} + 4xy + 2yz^{3}$ ，点 $a = (0,0,0)$ ， $b = (1,1,1)$ 和图1.28中的三条路径验证梯度基本定理。

(a) $(0,0,0)\to (1,0,0)\to (1,1,0)\to (1,1,1);$

(b) $(0,0,0)\rightarrow (0,0,1)\rightarrow (0,1,1)\rightarrow (1,1,1);$

(c) 抛物线路径 $z = x^{2}$ ; y = x。

![](images/e74cc63dcb5d82b6b711b1aa6ecaace0a3c55e2628da4db94a24c978bd0b2093.jpg)  
图1.28

## 1.3.4 散度基本定理

散度基本定理指出：

$$
\boxed {\int_ {\mathcal {V}} (\nabla \cdot \boldsymbol {v}) \mathrm{d} \tau = \oint_ {\mathcal {S}} \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {a}}\tag{1.56}
$$

我想，为了纪念它的重要性，这个定理至少有三个特殊的名字：高斯定理（Gauss's theorem），格林定理（Green's theorem），或者简称为散度定理（divergence theorem）。同其他基本定理一样，它指出一个区域上的函数导数（这里指散度）（在这种情况下为体积 $\mathcal{V}$ ）的积分等于该函数在边界处上的值（这里为包围体积的表面 $S$ ）。请注意，边界项本身也是一个积分（具体讲是一个面积分）。这是合理的：一条线段的“边界”只是两个端点，而一个体积的边界是一个（闭合）曲面。

几何解释：如果 v 代表一个不可压缩流体的流，则 v 的流量 [式（1.56）的等号右侧] 是单位时间通过表面流出的流体总量。现在，散度是矢量从某点“散出”的量度——一个具有高散度的地方像一个“水龙头”，向外流出液体。现在，散度测量的是矢量上某点的“扩散”程度——散度大的点就像一个“水龙头”，倾泻出液体。如果在一个充满不可压缩流体的区域有一堆水龙头，那么等量的液体将被迫通过该区域的边界流出。事实上，我们有两种方法可以确定总的流量：（a）计算所有水龙头的数量，并记录每个水龙头的流量，或者（b）可以环绕边界，测量每个点的流量，并将其加起来。无论哪种方式，都会得到同样的结果：

$$
\int (\text { 体积内所有水龙头数 }) = \oint (\text { 流出表面的流量 })
$$

本质上，这就是散度定理所表述的。

## 例题1.10 利用函数

$$
\pmb {v} = y ^ {2} \hat {\pmb {x}} + (2 x y + z ^ {2}) \hat {\pmb {y}} + (2 y z) \hat {z}
$$

和位于原点处的单位立方体（图 1.29）验证散度定理。

[解答] 在这种情况下，

$$
\nabla \cdot \boldsymbol {v} = 2 (x + y)
$$

2.1.05

以及

$$
\int_ {\mathcal {V}} 2 (x + y) \mathrm{d} \tau = 2 \int_ {0} ^ {1} \int_ {0} ^ {1} \int_ {0} ^ {1} (x + y) \mathrm{d} x \mathrm{d} y \mathrm{d} z
$$

$$
\int_ {0} ^ {1} (x + y) \mathrm{d} x = \frac {1}{2} + y, \quad \int_ {0} ^ {1} \left(\frac {1}{2} + y\right) \mathrm{d} y = 1, \quad \int_ {0} ^ {1} 1 \mathrm{d} z = 1\tag{因此}
$$

$$
\int_ {\mathcal {V}} \nabla \cdot \boldsymbol {v} \mathrm{d} \tau = 2
$$

散度定理的左侧就讨论至此。为了计算表面积分，我们必须分别考虑立方体的六个面：

(i)

$$
\int \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {a} = \int_ {0} ^ {1} \int_ {0} ^ {1} y ^ {2} \mathrm{d} y \mathrm{d} z = \frac {1}{3}\tag{ii}
$$

$$
\int \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {a} = - \int_ {0} ^ {1} \int_ {0} ^ {1} y ^ {2} \mathrm{d} y \mathrm{d} z = - \frac {1}{3}\tag{iii}
$$

$$
\int \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {a} = \int_ {0} ^ {1} \int_ {0} ^ {1} (2 x + z ^ {2}) \mathrm{d} x \mathrm{d} z = \frac {4}{3}\tag{iv}
$$

$$
\int \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {a} = - \int_ {0} ^ {1} \int_ {0} ^ {1} z ^ {2} \mathrm{d} x \mathrm{d} z = - \frac {1}{3}\tag{v}
$$

$$
\int \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {a} = \int_ {0} ^ {1} \int_ {0} ^ {1} 2 y \mathrm{d} x \mathrm{d} y = 1\tag{vi}
$$

$$
\int \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {a} = - \int_ {0} ^ {1} \int_ {0} ^ {1} 0 \mathrm{d} x \mathrm{d} y = 0
$$

正如预期的那样，所以总通量为

$$
\oint_ {S} \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {a} = \frac {1}{3} - \frac {1}{3} + \frac {4}{3} - \frac {1}{3} + 1 + 0 = 2
$$

![](images/350d59337b35a6dd0a05e479ef282ce597952c0977a6f96d2f555cd34322c25f.jpg)  
图1.29

习题1.33 验证函数 $\pmb{v} = (xy)\hat{\pmb{x}} + (2yz)\hat{\pmb{y}} + (3xz)\hat{\pmb{z}}$ 的散度定理，取体积大小为图1.30所示边长为2的立方体。

![](images/4ff100dc50f1cc0a3b79d44ce6a8f9ff124f31f616164d52cf67c8962082c64d.jpg)  
图1.30

## 1.3.5 旋度基本定理

旋度基本定理，是斯托克斯定理的一个特殊名称，它指出

$$
\boxed {\int_ {\mathcal {S}} (\nabla \times \boldsymbol {v}) \cdot \mathrm{d} \boldsymbol {a} = \oint_ {\mathcal {P}} \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {l}}\tag{1.57}
$$

与前面一样，一个区域（这里是一个曲面，S）上的函数导数（这里是旋度）的积分等于该区域边界处的函数值（这里是曲面的周长，P）。与散度定理的情况一样，边界项本身是一个积分——具体讲是一个闭合曲积分。

几何解释：回想一下，旋度是矢量 v “扭曲”的量度；旋度大的区域就是漩涡——如果你在这里放一个小桨轮，它就会旋转。那么，对某个表面上的旋度积分（或者，更精确地说，旋度通过该表面的通量）代表了“涡流总量”，我们可以通过绕过边缘并找出有多少涡流沿着边界流动来确定它（图 1.31）。事实上， $v \cdot dl$ 有时被称为 v 的环流（circulation）。

你也许注意到斯托克斯定理中的一个明显的歧义：当涉及边界线积分时，我们应该沿哪个路径呢（顺时针还是逆时针）？如果我们沿“错误”路径，会发现整体上存在一个符号错误。答案是，只要你保持一致，沿哪个路径都无关紧要，因为在面积分中也存在这样一个符号不确定的补偿：面元 $\mathrm{da}$ 的指向哪里？对闭合曲面（如散度定理） $\mathrm{da}$ 的方向为外法线方向；但是对非闭合曲面，哪个方向是“外法线”方向？斯托克斯定理的一致性（与所有此类问题一样）由右手规则给出；如果你的四指指向线积分的方向，则大拇指所指的方向就是 $\mathrm{da}$ 的方向（图1.32）。

![](images/2fbcc9b82bce47302052856192f3f9ea373649a0c2c9e53d88f5ae76f0ff88c6.jpg)  
图1.31

![](images/b44ff81d3b35f2f71c3ea3e55e69197bc15544c91d426b0548befcb79c5ffca0.jpg)  
图1.32

到现在为止，对任何给定的边界线都存在有许多曲面（无数）共享它。把曲别针拧成一个圈，然后蘸些肥皂水。肥皂膜构成一个表面，以金属丝环为边界。如果你吹它，肥皂膜会膨胀，形成一个更大的表面，具有相同的边界。一般来讲，通量积分很大程度上取决于你在哪个曲面上积分，但对旋度的情况显然并非如此。斯托克斯定理指出 $\int \nabla \times \boldsymbol{v} \cdot \mathrm{d}\boldsymbol{a}$ 等于 $\boldsymbol{v}$ 在绕边界周围的线积分，而该积分与你所选择的具体曲面无关。

推论1： $\int \nabla \times \pmb {v}\cdot \mathrm{d}\pmb{a}$ 仅与曲线边界有关，而与所选择的具体曲面无关。

推论2：对任何闭合曲面， $\oint \nabla \times \pmb {v}\cdot \mathrm{d}\pmb {a} = 0$ ，这是因为闭合曲面的边界线就像气球的开口一样，可以收缩为一点；因此式（1.57）右边为零。

这些推论和梯度定理的推论类似。我们将在适当的时候对两者做进一步讨论。

例题1.11 设 $\pmb{v} = (2xz + 3y^2)\hat{\pmb{y}} + (4yz^2)\hat{\pmb{z}}$ ，验证图1.33所示的方形曲面的斯托克斯定理。[解答] 这里，

$$
\nabla \times \boldsymbol {v} = (4 z ^ {2} - 2 x) \hat {\boldsymbol {x}} + 2 z \hat {\boldsymbol {z}}, \quad \mathrm{d} \boldsymbol {a} = \mathrm{d} y \mathrm{d} z \hat {\boldsymbol {x}}
$$

（在说 $\mathrm{d}\pmb{a}$ 指向 $x$ 正方向时，我们致力于求逆时针方向的线积分。我们也可以写 $\mathrm{d}\pmb{a} = -\mathrm{dy}\mathrm{dz}\hat{\pmb{x}}$ ，但那样我们就不得不选择顺时针方向。）对于这个曲面 $x = 0$ ，所以

$$
\int \nabla \times \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {a} = \int_ {0} ^ {1} \int_ {0} ^ {1} 4 z ^ {2} \mathrm{d} y \mathrm{d} z = \frac {4}{3}
$$

现在，线积分是多少？我们把它分成4段：

$$
\text {(i)} x = 0, \quad z = 0, \quad \boldsymbol {v} \cdot \mathrm{d} l = 3 y ^ {2} \mathrm{d} y, \quad \int \boldsymbol {v} \cdot \mathrm{d} l = \int_ {0} ^ {1} 3 y ^ {2} \mathrm{d} y = 1.
$$

$$
\text { (ii) } x = 0, \quad y = 1, \quad \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {l} = 4 z ^ {2} \mathrm{d} z, \quad \int \boldsymbol {v} \cdot \mathrm{d} l = \int_ {0} ^ {1} 4 z ^ {2} \mathrm{d} z = \frac {4}{3}.
$$

(iii) $x = 0, \quad z = 1, \quad v \cdot \mathrm{d}l = 3y^2\mathrm{d}y,\quad \int v \cdot \mathrm{d}l = \int_1^0 3y^2\mathrm{d}y = -1.$

$$
\text {(iv)} x = 0, \quad y = 0, \quad \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {l} = 0, \quad \int \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {l} = \int_ {1} ^ {0} 0 \mathrm{d} z = 0.
$$

![](images/d78bcbd562d3b8f52d0b9664ff6391e0c41e937a7e4df7396586c0ab2a6c795f.jpg)  
图1.33

解题要点：注意我是如何处理步骤（iii）的。因为路径是向左的，这里有一种想将 $\mathrm{d}l$ 写成 $\mathrm{d}l = -\mathrm{d}y\hat{y}$ 的诱惑。如果你非要这样，可以通过从 $0 \rightarrow 1$ 进行积分来逃脱惩罚。但更安全的做法总是让 $\mathrm{d}l = \mathrm{d}x\hat{x} + \mathrm{d}y\hat{y} + \mathrm{d}z\hat{z}$ （永远不要有任何负号），让积分的极限来决定方向。

习题1.34 利用图1.34的三角形阴影区域，验证函数 $\pmb{v} = (xy)\hat{\pmb{x}} + (2yz)\hat{\pmb{y}} + (3xz)\hat{\pmb{z}}$ 的斯托克斯定理。

![](images/0fa3c85dd3c46796bde19479a719a8e6bcccfe9766b24382119b6fc44df43892.jpg)  
图1.34

习题1.35 使用与例1.11中相同的函数和边界线验证推论1，不过现在要对图1.35中立方体的5

个表面做积分。立方体的背面是敞开的。

![](images/aab9b7a745c043e10022bf13b784268b331f8457c17fe5cda25cf0c3a8cefd3a.jpg)  
图1.35

## 1.3.6 分部积分

分部积分技巧是运用导数的乘法定则

$$
\frac {\mathrm{d}}{\mathrm{d} x} (f g) = f \left(\frac {\mathrm{d} g}{\mathrm{d} x}\right) + g \left(\frac {\mathrm{d} f}{\mathrm{d} x}\right)
$$

两边分别进行积分，并调用积分基本定理：

$$
\int_ {a} ^ {b} \frac {\mathrm{d}}{\mathrm{d} x} (f g) \mathrm{d} x = f g | _ {a} ^ {b} = \int_ {a} ^ {b} f \left(\frac {\mathrm{d} g}{\mathrm{d} x}\right) \mathrm{d} x + \int_ {a} ^ {b} g \left(\frac {\mathrm{d} f}{\mathrm{d} x}\right) \mathrm{d} x
$$

或

$$
\int_ {a} ^ {b} f \left(\frac {\mathrm{d} g}{\mathrm{d} x}\right) \mathrm{d} x = - \int_ {a} ^ {b} g \left(\frac {\mathrm{d} f}{\mathrm{d} x}\right) \mathrm{d} x + f g | _ {a} ^ {b}\tag{1.58}
$$

这就是分部积分。它适用于你对一个函数（f）和另一个函数的导数（g）的乘积进行积分的情况；分布积分指出你可以将 g 的导数转换到对 f 的导数，代价是多出一个减号和一个边界项。

## 例题1.12 计算积分

$$
\int_ {0} ^ {\infty} x \mathrm{e} ^ {- x} \mathrm{d} x
$$

[解答] 指数函数可以表示为导数

$$
\mathrm{e} ^ {- x} = \frac {\mathrm{d}}{\mathrm{d} x} (- \mathrm{e} ^ {- x})
$$

在这种情况下， $f(x) = x$ ， $g(x) = -\mathrm{e}^{-x},\quad \mathrm{d}f / \mathrm{d}x = 1$ ，因此

$$
\int_ {0} ^ {\infty} x \mathrm{e} ^ {- x} \mathrm{d} x = \int_ {0} ^ {\infty} \left. \mathrm{e} ^ {- x} \mathrm{d} x - (x \mathrm{e} ^ {- x}) \right| _ {0} ^ {\infty} = (- \mathrm{e} ^ {- x}) \Big | _ {0} ^ {\infty} = 1
$$

我们可以利用矢量积分的乘积规则以及适当的基本定理以相同的方法进行分部积分。例如，调用散度定理，对

$$
\nabla \cdot (f \mathbf {A}) = f \nabla \cdot \mathbf {A} + \mathbf {A} \cdot (\nabla f)
$$

进行一定体积分，得到

$$
\int \nabla \cdot (f \boldsymbol {A}) \mathrm{d} \tau = \int f (\nabla \cdot \boldsymbol {A}) \mathrm{d} \tau + \int \boldsymbol {A} \cdot (\nabla f) \mathrm{d} \tau = \oint f \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {a}
$$

或者

$$
\int_ {\mathcal {V}} f (\nabla \cdot \boldsymbol {A}) \mathrm{d} \tau = - \int_ {\mathcal {V}} \boldsymbol {A} \cdot (\nabla f) \mathrm{d} \tau + \oint_ {\mathcal {S}} f \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {a}\tag{1.59}
$$

这里，被积函数仍是一个函数（f）和另一个函数的导数（在这种情况下是散度）A 的乘积；通过分部积分，我们可以把对 A 求导数转换为对 f 的求导（在那里它变成梯度），代价是多出一个负号和一个边界项（在这种情况下是曲面积）。

你们可能想知道我们会经常遇到一个函数与另一个函数导数乘积的积分吗？回答是肯定的，所以，分部积分是矢量积分中最强大的工具之一。

习题1.36

(a) 证明

$$
\int_ {\mathcal {S}} f (\nabla \times \boldsymbol {A}) \cdot \mathrm{d} \boldsymbol {a} = \int_ {\mathcal {S}} [ \boldsymbol {A} \times (\nabla f) ] \cdot \mathrm{d} \boldsymbol {a} + \oint_ {\mathcal {P}} f \boldsymbol {A} \cdot \mathrm{d} l\tag{1.60}
$$

(b) 证明

$$
\int_ {\mathcal {V}} \boldsymbol {B} \cdot (\nabla \times \boldsymbol {A}) \cdot \mathrm{d} \tau = \int_ {\mathcal {V}} \boldsymbol {A} \cdot (\nabla \times \boldsymbol {B}) \mathrm{d} \tau + \oint_ {\mathcal {S}} (\boldsymbol {A} \times \boldsymbol {B}) \cdot \mathrm{d} \boldsymbol {a}\tag{1.61}
$$

## 1.4 曲线坐标系

## 1.4.1 球坐标系

你可以用直角坐标 $(x, y, z)$ 来标记点 $P$ ，但有时使用球坐标（spherical） $(r, \theta, \phi)$ 更为方便； $r$ 是距原点的距离（位置矢量 $r$ 的大小）， $\theta$ （ $z$ 轴向下转过的角度）称为极角（polar angle）， $\phi$ （位置矢量在 $xy$ 平面投影与 $x$ 轴的夹角）是方位角（azimuthal angle）。由图1.36可以给出球坐标与直角坐标之间的关系：

$$
x = r \sin \theta \cos \phi , \quad y = r \sin \theta \sin \phi , \quad z = r \cos \theta\tag{1.62}
$$

![](images/462af2c052212dbdf54355f4538d1224487ad31d976c6ccc00b709c4a719b936.jpg)  
图1.36

图1.36还给出了三个单位矢量， $\hat{r},\hat{\theta},\hat{\phi}$ ，指向相应坐标的增加方向。它们构成一个正交（相互垂直）基组，任何矢量 $A$ 通常都可以用它们来表示：

$$
\boldsymbol {A} = A _ {r} \hat {\boldsymbol {r}} + A _ {\theta} \hat {\boldsymbol {\theta}} + A _ {\phi} \hat {\boldsymbol {\phi}}\tag{1.63}
$$

$A_{r}, A_{\theta}, A_{\phi}$ 分别是 $\mathbf{A}$ 的径向、极向和方位角分量。依据直角系中的单位矢量，有

$$
\left. \begin{array}{l} \hat {\boldsymbol {r}} = \sin \theta \cos \phi \hat {\boldsymbol {x}} + \sin \theta \sin \phi \hat {\boldsymbol {y}} + \cos \theta \hat {\boldsymbol {z}} \\ \hat {\boldsymbol {\theta}} = \cos \theta \cos \phi \hat {\boldsymbol {x}} + \cos \theta \sin \phi \hat {\boldsymbol {y}} - \sin \theta \hat {\boldsymbol {z}} \\ \hat {\boldsymbol {\phi}} = - \sin \phi \hat {\boldsymbol {x}} + \cos \phi \hat {\boldsymbol {y}} \end{array} \right\}\tag{1.64}
$$

上面关系你可以自己验证（习题1.38）。为了便于参考，我把这些公式放在本书的后环衬。我最好提醒你一下，但这里潜伏着危险： $\hat{r}, \hat{\theta}, \hat{\phi}$ 与特定的 $P$ 点相关，并且随着 $P$ 点的移动它们会改变方向。例如， $\hat{r}$ 总是沿径向向外，但“径向向外”可以是 $x$ 方向、 $y$ 方向，或者其他方向，具体取决于所考虑的点在何处。在图1.37中， $A = \hat{y}$ 和 $B = -\hat{y}$ ，但他们在球坐标系中都写作 $\hat{r}$ 。当然，我们可以通过指定一个明确的参考点， $\hat{r}(\theta, \phi), \hat{\theta}(\theta, \phi), \hat{\phi}(\theta, \phi)$ ，来考虑这一点；但这确实有点麻烦，只要你注意到了这个问题，我想是不会有任何困难的 $^{10}$ 。尤其是不要想当然地将不同点矢量的径向分量相加（在图1.37中， $A + B = 0$ ，而不是 $2\hat{r}, A \cdot B = -1$ ，而不是 $+1$ ）。由于在球坐标系中单位矢量自身就是位置的函数，要注意矢量的微分运算（例如 $\partial \hat{r} / \partial \theta = \hat{\theta}$ ）。不要像我在方程（1.53）中对 $x, y, z$ 所处理的那样，不要把 $\hat{r}, \hat{\theta}, \hat{\phi}$ 放到积分符号外。一般来说，如果你不能确定一种运算是否正确，你可以把这个问题在直角系中重新写出来这样就不会出现这种困难。

![](images/58e92f8abe6617d67991d51ccc0ad89455596cc1b23ba6d19ac2f079939cccff.jpg)  
图1.37

正如 $x$ 方向长度的无限小位移是 $\mathrm{dx}$ 一样，自然在 $\hat{r}$ 方向上的无限小位移就是 $\mathrm{dr}$ （图1.38a）：

$$
\mathrm{d} l _ {r} = \mathrm{d} r\tag{1.65}
$$

另一方面，在 $\hat{\theta}$ 方向无限小位移元不是 dθ （这仅是一个角度，它不具有长度的量纲），而是 r dθ （图 1.38b）：

$$
\mathrm{d} l _ {\theta} = r \mathrm{d} \theta\tag{1.66}
$$

类似地，在 $\hat{\phi}$ 方向无限小位移元是（图 1.38c）

$$
\mathrm{d} l _ {\phi} = r \sin \theta \mathrm{d} \phi\tag{1.67}
$$

![](images/4194bb4ddfc757430e6cde1c7bc052d86edfa8f71a62acba8e9d96be4fa18aaf.jpg)  
a)

![](images/9a6de7dd4c6be1967659b624afce4216ffaf6bdeeaf01aa01c9106bcd8bb79ac.jpg)  
图1.38

![](images/c1c5865eda7e6a3e5902dc4dc391ba2cfd5634200c3d58e3acef7f305f156d67.jpg)  
c)

这样，总的无限小位移元 $\mathrm{d}l$ 是

$$
\mathrm{d} \pmb {l} = \mathrm{d} r \hat {\pmb {r}} + r \mathrm{d} \theta \hat {\pmb {\theta}} + r \sin \theta \mathrm{d} \phi \hat {\phi}\tag{1.68}
$$

这个与（例如，在线积分中） $\mathrm{d}\pmb {l} = \mathrm{d}x\hat{\pmb{x}} +\mathrm{d}y\hat{\pmb{y}} +\mathrm{d}z\hat{\pmb{z}}$ 在直角坐标系中扮演相同的角色。

在球坐标系中，无限小体积元 $\mathrm{d}\tau$ 是三个无限小位移元的乘积：

$$
\mathrm{d} \tau = \mathrm{d} l _ {r} \mathrm{d} l _ {\theta} \mathrm{d} l _ {\phi} = r ^ {2} \sin \theta \mathrm{d} r \mathrm{d} \theta \mathrm{d} \phi\tag{1.69}
$$

我无法给出无限小面元 $\mathrm{da}$ 的一般表达式，因为这依赖于曲面的方向。你只需分析任何给定情况下的几何图形（直角坐标系和曲线坐标系都是如此）。例如，如果你在球面上积分，那么 $r$ 是常数，而 $\theta$ 和 $\phi$ 是变化的（图1.39），所以

$$
\mathrm{d} \boldsymbol {a} _ {1} = \mathrm{d} l _ {\theta} \mathrm{d} l _ {\phi} \hat {\boldsymbol {r}} = r ^ {2} \sin \theta \mathrm{d} \theta \mathrm{d} \phi \hat {\boldsymbol {r}}
$$

另一方面，如果曲面位于 $xy$ 平面内，则 $\theta$ 是常数（即 $\pi /2$ ）， $r, \phi$ 是变化的，那么

$$
\mathrm{d} \pmb {a} _ {2} = \mathrm{d} l _ {r} \mathrm{d} l _ {\phi} \hat {\pmb {\theta}} = r \mathrm{d} r \mathrm{d} \phi \hat {\pmb {\theta}}
$$

最后，请注意：r 的变化范围是从 0 到 $\infty$ ， $\phi$ 是从 0 到 $2\pi$ ， $\theta$ 是从 0 到 $\pi$ （不是 $2\pi$ ——这将每个点计数两次） $^{11}$ 。

![](images/2a92ea4be2d54d7b1c4d4b3f86d6e6f90b253b9b8ad4217ec33ed9e9e1ea3bb6.jpg)  
图1.39

例题1.13 求半径为 $R$ 的球体的体积。

[解答]

$$
V = \int \mathrm{d} \tau = \int_ {r = 0} ^ {R} \int_ {\theta = 0} ^ {\pi} \int_ {\phi = 0} ^ {2 \pi} r ^ {2} \sin \theta \mathrm{d} r \mathrm{d} \theta \mathrm{d} \phi
$$

$\frac{1}{2}$ $\frac{1}{2}$ $\frac{1}{2}$ $\frac{1}{2}$ $\frac{1}{2}$ $\frac{1}{2}$ $\frac{1}{2}$ $\frac{1}{2}$ $\frac{1}{2}$ $\frac{1}{2}$ $\frac{1}{2}$

$$
\begin{array}{l} = \left(\int_ {0} ^ {R} r ^ {2} \mathrm{d} r\right) \left(\int_ {0} ^ {\pi} \sin \theta \mathrm{d} \theta\right) \left(\int_ {0} ^ {2 \pi} \mathrm{d} \phi\right) \\ = \left(\frac {R ^ {3}}{3}\right) (2) (2 \pi) = \frac {4}{3} \pi R ^ {3} \end{array}
$$

(这并不奇怪。)

到目前为止，我们仅讨论了球坐标的几何表示。现在，我想把矢量导数（梯度、散度、旋度、拉普拉斯算符）“变为”由 $r, \theta, \phi$ 表示。原则上，这一点也不复杂：对于梯度的情况，

$$
\nabla T = \frac {\partial T}{\partial x} \hat {\pmb {x}} + \frac {\partial T}{\partial y} \hat {\pmb {y}} + \frac {\partial T}{\partial z} \hat {\pmb {z}}
$$

例如，我们首先用链式法则（chain rule）来展开偏导数，

$$
\frac {\partial T}{\partial x} = \frac {\partial T}{\partial r} \left(\frac {\partial r}{\partial x}\right) + \frac {\partial T}{\partial \theta} \left(\frac {\partial \theta}{\partial x}\right) + \frac {\partial T}{\partial \phi} \left(\frac {\partial \phi}{\partial x}\right)
$$

括号中的项可由式（1.62）——或者更准确说是它们的逆变换式（习题1.37）求出。然后我们对 $\partial T / \partial y, \partial T / \partial z$ 做同样的处理。最后，我们将在公式中用 $\hat{r}, \hat{\theta}, \hat{\phi}$ 替换 $\hat{x}, \hat{y}, \hat{z}$ （习题1.38）。用这种蛮力法计算出球坐标中的梯度估计就要一个小时。我想最初就是这样做的，但在附录A中我们给出一种更有效的间接方法，该方法具有同时处理所有坐标系的额外优点。我这里介绍这个“直接”方法只是想告诉你，变换到球坐标并没有什么微妙或神秘的地方：就是用不同的符号来表示相同的量（梯度、散度或者其他），仅此而已。

下面是球坐标系中的矢量导数：

梯度：

$$
\nabla T = \frac {\partial T}{\partial r} \hat {\pmb {r}} + \frac {1}{r} \frac {\partial T}{\partial \theta} \hat {\pmb {\theta}} + \frac {1}{r \sin \theta} \frac {\partial T}{\partial \phi} \hat {\phi}\tag{1.70}
$$

散度：

$$
\nabla \cdot \pmb {v} = \frac {1}{r ^ {2}} \frac {\partial}{\partial r} (r ^ {2} v _ {r}) + \frac {1}{r \sin \theta} \frac {\partial}{\partial \theta} (\sin \theta v _ {\theta}) + \frac {1}{r \sin \theta} \frac {\partial v _ {\phi}}{\partial \phi}\tag{1.71}
$$

旋度：

$$
\begin{array}{l} \nabla \times \boldsymbol {v} = \frac {1}{r \sin \theta} \left[ \frac {\partial}{\partial \theta} (\sin \theta v _ {\phi}) - \frac {\partial v _ {\theta}}{\partial \phi} \right] \hat {\boldsymbol {r}} + \frac {1}{r} \left[ \frac {1}{r \sin \theta} \frac {\partial v _ {r}}{\partial \phi} - \frac {\partial}{\partial r} (r v _ {\phi}) \right] \hat {\boldsymbol {\theta}} + \\ \frac {1}{r} \left[ \frac {\partial}{\partial r} (r v _ {\theta}) - \frac {\partial v _ {r}}{\partial \theta} \right] \hat {\boldsymbol {\phi}} \end{array}\tag{1.72}
$$

拉普拉斯算符：

$$
\nabla^ {2} T = \frac {1}{r ^ {2}} \frac {\partial}{\partial r} \left(r ^ {2} \frac {\partial T}{\partial r}\right) + \frac {1}{r ^ {2} \sin \theta} \frac {\partial}{\partial \theta} \left(\sin \theta \frac {\partial T}{\partial \theta}\right) + \frac {1}{r ^ {2} \sin^ {2} \theta} \frac {\partial^ {2} T}{\partial \phi^ {2}}\tag{1.73}
$$

作为参考，这些公式附在前环衬内。

习题 1.37 给出以 x, y, z 表示的 r, $\theta$ , $\phi$ 的表示式 [换句话说，是式（1.62）的逆变换式]。

•习题 1.38 用单位矢量 $\hat{x}, \hat{y}, \hat{z}$ 表示单位矢量 $\hat{r}, \hat{\theta}, \hat{\phi}$ [即推导式（1.64）]。用几种方法验证你的结果 $(\hat{r} \cdot \hat{r} \stackrel{?}{=} 1, \quad \hat{\theta} \cdot \hat{\phi} \stackrel{?}{=} 0, \quad \hat{r} \times \hat{\theta} \stackrel{?}{=} \hat{\phi}, \cdots)$ 。同时，用 $\hat{r}, \hat{\theta}, \hat{\phi}$ 求出 $\hat{x}, \hat{y}, \hat{z}$ 的逆变换式。

习题1.39

(a) 利用以原点为中心、半径为 $R$ 的球体作为体积，验证函数 $\pmb{v}_{1} = r^{2}\hat{\pmb{r}}$ 的散度定理。

(b) 对函数 $v_{2}=(1/r^{2})\hat{r}$ 进行同样验证。(如果你对结果感到惊讶，请回顾一下习题 1.16。)

习题1.40 求函数

$$
\pmb {v} = (r \cos \theta) \hat {\pmb {r}} + (r \sin \theta) \hat {\pmb {\theta}} + (r \sin \theta \cos \theta) \hat {\pmb {\phi}}
$$

的散度。并使用以原点为中心、半径为 R、位于 xy 平面上的倒置半球形碗作为体积，验证该函数验证散度定理（图 1.40）。

习题1.41 求函数 $T = r(\cos \theta + \sin \theta \cos \phi)$ 的梯度和拉普拉斯算符。通过将 $T$ 变换到直角系并利式（1.42）验证拉普拉斯算符。利用图1.41所给路径，从点（0,0,0）到点（0,0,2）检验该函数梯度定理。

![](images/34881c8d14fd0a089e75244039ec143cc586213acbab5e8d95c39e052c6e253a.jpg)  
图1.40

![](images/bd956028050afc85a44bb62f812d172d43e2da85bddfc9affe244105cbdb3e9a.jpg)  
图1.41

## 1.4.2 柱坐标系

P 点的柱坐标 $(s, \phi, z)$ 的定义如图 1.42 所示。请注意， $\phi$ 的含义与球坐标中的相同，z 的含义与直角坐标相同；s 是 P 点到 z 轴的距离，而在球坐标中 r 是 P 点到原点的距离。与直角坐标的关系是

$$
x = s \cos \phi , \quad y = s \sin \phi , \quad z = z\tag{1.74}
$$

单位矢量是（习题1.42）

$$
\left. \begin{array}{l} \hat {\boldsymbol {s}} = \cos \phi \hat {\boldsymbol {x}} + \sin \phi \hat {\boldsymbol {y}} \\ \hat {\phi} = - \sin \phi \hat {\boldsymbol {x}} + \cos \phi \hat {\boldsymbol {y}} \\ \hat {\boldsymbol {z}} = \hat {\boldsymbol {z}} \end{array} \right\}\tag{1.75}
$$

无限小位移元为

$$
\mathrm{d} l _ {s} = \mathrm{d} s, \quad \mathrm{d} l _ {\phi} = s \mathrm{d} \phi , \quad \mathrm{d} l _ {z} = \mathrm{d} z\tag{1.76}
$$

所以

$$
\mathrm{d} \boldsymbol {l} = \mathrm{d} s \hat {\boldsymbol {s}} + s \mathrm{d} \phi \hat {\boldsymbol {\phi}} + \mathrm{d} z \hat {\boldsymbol {z}}\tag{1.77}
$$

体积元是

$$
\mathrm{d} \tau = s \mathrm{d} s \mathrm{d} \phi \mathrm{d} z\tag{1.78}
$$

s 变化范围是从 $0 \rightarrow \infty$ ， $\phi$ 从 $0 \rightarrow 2\pi$ ，z 从 $-\infty$ 到 $\infty$ 。

![](images/8650d58f6f6285afb3079edfc16db84facc95f3637def067c333f0bf40973ec9.jpg)  
图1.42

在柱坐标系下的矢量导数为：

梯度：

$$
\nabla T = \frac {\partial T}{\partial s} \hat {\boldsymbol {s}} + \frac {1}{s} \frac {\partial T}{\partial \phi} \hat {\boldsymbol {\phi}} + \frac {\partial T}{\partial z} \hat {\boldsymbol {z}}\tag{1.79}
$$

散度：

$$
\nabla \cdot \boldsymbol {v} = \frac {1}{s} \frac {\partial}{\partial s} (s v _ {s}) + \frac {1}{s} \frac {\partial v _ {\phi}}{\partial \phi} + \frac {\partial v _ {z}}{\partial z}\tag{1.80}
$$

旋度：

$$
\nabla \times \boldsymbol {v} = \left(\frac {1}{s} \frac {\partial v _ {z}}{\partial \phi} - \frac {\partial v _ {\phi}}{\partial z}\right) \hat {\boldsymbol {s}} + \left(\frac {\partial v _ {s}}{\partial z} - \frac {\partial v _ {z}}{\partial s}\right) \hat {\boldsymbol {\phi}} + \frac {1}{s} \left[ \frac {\partial}{\partial s} (s v _ {\phi}) - \frac {\partial v _ {s}}{\partial \phi} \right] \hat {\boldsymbol {z}}\tag{1.81}
$$

拉普拉斯算符：

$$
\nabla^ {2} T = \frac {1}{s} \frac {\partial}{\partial s} \left(s \frac {\partial T}{\partial s}\right) + \frac {1}{s ^ {2}} \frac {\partial^ {2} T}{\partial \phi^ {2}} + \frac {\partial^ {2} T}{\partial z ^ {2}}\tag{1.82}
$$

这些公式也列在前环衬内。

习题 1.42 用 $\hat{x}, \hat{y}, \hat{z}$ 表示出柱坐标系的单位矢量 $\hat{s}, \hat{\phi}, \hat{z}$ [即推导式（1.75）]。逆变换你求的式子，用 $\hat{s}, \hat{\phi}, \hat{z}$ 表示出 $\hat{x}, \hat{y}, \hat{z}$ 。

习题1.43

(a) 求函数

$$
\pmb {v} = s (2 + \sin^ {2} \phi) \hat {\pmb {s}} + s \sin \phi \cos \phi \hat {\phi} + 3 z \hat {\pmb {z}}
$$

的散度。

（b）利用体积为图1.43所示的 $1 / 4$ 圆柱体(半径2，高度5)，验证该函数的散度定理。

(c) 求 $\pmb{v}$ 的旋度。

![](images/6a9447531557aa4f5dfb9439a18a75dccd895319b2bb2efaa99fd32700bfae5f.jpg)  
图1.43

## 1.5 狄拉克 $\delta$ 函数

## 1.5.1 $\hat{r} / r^2$ 的散度

考虑矢量函数

$$
\pmb {v} = \frac {1}{r ^ {2}} \hat {\pmb {r}}\tag{1.83}
$$

在每一点上， $v$ 的方向都是指向径向的（图1.44）；如果说有一个函数应该有很大的正散度，那就是它。然而，当你实际计算它的散度时[利用式（1.71）]，你得到的值恰恰为零。

$$
\nabla \cdot \boldsymbol {v} = \frac {1}{r ^ {2}} \frac {\partial}{\partial r} \left(r ^ {2} \frac {1}{r ^ {2}}\right) = \frac {1}{r ^ {2}} \frac {\partial}{\partial r} (1) = 0\tag{1.84}
$$

（如果你做了习题1.16，你已经遇到了这个悖论。）当我们将散度定理应用于该函数时，情况变得复杂起来。假设我们在原点为中心、半径为 $R$ 的球体上积分（见习题1.39b），曲面积分为

$$
\begin{array}{r l} \oint \boldsymbol {v} \cdot \mathrm{d} \boldsymbol {a} & = \int \left(\frac {1}{R ^ {2}} \hat {\boldsymbol {r}}\right) \cdot (R ^ {2} \sin \theta \mathrm{d} \theta \mathrm{d} \phi \hat {\boldsymbol {r}}) \\ & = \left(\int_ {0} ^ {\pi} \sin \theta \mathrm{d} \theta\right) \left(\int_ {0} ^ {2 \pi} \mathrm{d} \phi\right) = 4 \pi \end{array}\tag{1.85}
$$

但是，如果我们真的认为式（1.84）是对的，体积分 $\int \nabla \cdot \mathbf{v}\mathrm{d}\tau$ 是零。这是否意味着散度定理是错误的？究竟是怎么回事？

![](images/9746702911f6a962936704e16e16d48faa99df871446b2de74437266c9b674d0.jpg)  
图1.44

问题的根源出在 $r = 0$ 点，这里 $\pmb{v}$ 是发散的[在方程（1.84）中，我们在无意中除以了零]。确实，除原点外，其他地方的 $\nabla \cdot \pmb{v} = 0$ ，但原点的情况较为复杂。请注意，表面积分[方程（1.85）]与 $R$ 无关；如果散度定理是正确的（事实确实如此），那么对于以原点为中心的任何球体，无论多么小，我们都应该得到 $\int \nabla \cdot \pmb{v}\mathrm{d}\tau = 4\pi$ 。显然，整个贡献都必须来自 $r = 0$ 点！因此， $\nabla \cdot \pmb{v}$ 具有奇异的性质，即除了一点外，其他任何地方处处为零，而且它的积分（在包含该点的任何体积上）为 $4\pi$ 。这是普通函数不具备的特性。[另一方面，我确实想到物理中却有这样的一个例子：点粒子的密度（单位体积的质量），除了粒子所处的位置一点外，其他位置处处为零，而它的积分是有限的，即粒子的质量。]我们无意中发现了一个被物理学家称为狄拉克 $\delta$ 函数（Dirac delta function）的数学命题。在理论物理学的许多分支中它经常出现。此外，眼下的具体问题（函数 $\hat{r} /r^2$ 的散度）不仅仅是晦涩难懂的异物——事实上，它是整个电动力学理论的核心。因此，在这里停下来仔细研究狄拉克 $\delta$ 函数是值得的。

## 1.5.2 一维狄拉克 $\delta$ 函数

一维狄拉克 $\delta$ 函数 $\delta(x)$ 可以描述为一个无限高、无限窄的“尖峰”，面积为 1（图 1.45）。也就是说，

$$
\delta (x) = \left\{ \begin{array}{l l} {0,} & {\text {如果} x \neq 0} \\ {\infty ,} & {\text {如果} x = 0} \end{array} \right.\tag{1.86}
$$

和 $^{12}$

$$
\int_ {- \infty} ^ {\infty} \delta (x) \mathrm{d} x = 1\tag{1.87}
$$

![](images/9ef89c10fd4d5490b116c0b911cc080a390f3a7cf5e609db207ced8525e16808.jpg)  
图1.45

原则上讲， $\delta(x)$ 根本不是函数，因为它的值在 $x = 0$ 时是不确定的。在数学文献中，它被称为广义函数（generalized function）或分布（distribution）。如果你愿意，它是一系列函数的极限，比如高度为 $n$ 、宽度为 $1/n$ 的矩形 $R_{n}(x)$ ，或者高为 $n$ 、底边为 $2/n$ 等腰三角形（图1.46）。

![](images/afb7f6da5b765194a238fa2017a9d55b954e9cd7b5ceeac9454dbb0f82e4a91e.jpg)  
a)

![](images/0eac0c810a73ffb2c4b033f61ee4970d39b2563c6fa773f129abc52f9aabd23f.jpg)  
图1.46  
b)

如果 $f(x)$ 是某个“普通”函数[也就是说，不是另外一个 $\delta$ 函数——事实上，为安全起见，假设 $f(x)$ 是连续的]；那么，除了在 $x = 0$ 外，乘积 $f(x)\delta (x)$ 在任何其他地方都是零。因此

$$
f (x) \delta (x) = f (0) \delta (x)\tag{1.88}
$$

[这是关于 $\delta$ 函数最重要的结论，所以务必请你理解它的含义：由于除在 $x = 0$ 外，乘积 $f(x)\delta (x)$ 处处为零，我们可以用它在原点处的值替换 $f(x)$ 。]特别地

$$
\int_ {- \infty} ^ {\infty} f (x) \delta (x) \mathrm{d} x = f (0) \int_ {- \infty} ^ {\infty} \delta (x) \mathrm{d} x = f (0)\tag{1.89}
$$

那么，在积分下， $\delta$ 函数在 $x = 0$ 时“挑选”出 $f(x)$ 的值。（由此及以下，积分不必从 $-\infty$ 积到 $\infty$ ，只要积分区域遍及 $\delta$ 函数上就足够了，从 $-\varepsilon$ 到 $+\varepsilon$ 也可以。）

当然，我们也可以将尖峰从 $x = 0$ 移动到其他点 $x = a$ （图1.47）：

$$
\delta (x - a) = \left\{ \begin{array}{l l} {0,} & {x \neq a} \\ {\infty ,} & {x = a} \end{array} \right. \text {和} \int_ {- \infty} ^ {\infty} \delta (x - a) \mathrm{d} x = 1\tag{1.90}
$$

方程（1.88）变为

$$
f (x) \delta (x - a) = f (a) \delta (x - a)\tag{1.91}
$$

方程（1.89）推广为

$$
\boxed {\int_ {- \infty} ^ {\infty} f (x) \delta (x - a) \mathrm{d} x = f (a)}\tag{1.92}
$$

![](images/f52bc599501b2955f9a2532d24b415f8efe4ff086b8c7ddf936c0b940b8e32b7.jpg)  
图1.47

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
例题1.15 证明 $\delta (kx) = \frac{1}{|k|}\delta (x)$ (1.94)其中 $k$ 为任意（非零）常数。[特别是 $\delta (-x) = \delta (x)$ 。] [解答] 对于任意检验函数 $f(x)$，考虑积分 $\int_{-\infty}^{\infty}f(x)\delta (kx)\mathrm{d}x$ 进行变量代换，我们令 $y\equiv kx$ ，这样有 $x = y / k$ ， $\mathrm{dx} = \mathrm{dy} / k$ 。若 $k$ 为正值，则积分仍然是从 $-\infty$ 到 $\infty$；但是，若 $k$ 是负值，则 $x = \infty$ 对应 $y = -\infty$ ，反之亦然；因此，积分上下限顺序颠倒，恢复到“正当”的积分上下限顺序，产生一个负号。因此 $\int_{-\infty}^{\infty}f(x)\delta (kx)\mathrm{d}x = \pm \int_{-\infty}^{\infty}f(y / k)\delta (y)\frac{\mathrm{d}y}{k} = \pm \frac{1}{k} f(0) = \frac{1}{|k|} f(0)$ （当 $k$ 为负，适用式中下面的符号，我们通过对 $k$ 加上绝对值符号来说明这一点。）那么，在积分号下，$\delta (kx)$ 与 $(1 / |k|)\delta (x)$ 的作用相同：$\int_{-\infty}^{\infty}f(x)\delta (kx)\mathrm{d}x = \int_{-\infty}^{\infty}f(x)\left[\frac{1}{|k|}\delta (x)\right]\mathrm{d}x$ 因此，根据方程（1.93），$\delta (kx)$ 与 $(1 / |k|)\delta (x)$ 相等。
</div>

例题1.14 计算积分

$$
\int_ {0} ^ {3} x ^ {3} \delta (x - 2) \mathrm{d} x
$$

[解答] $\delta$ 函数在 $x = 2$ 处把 $x^{3}$ 的值挑选出来，因此积分为 $2^{3} = 8$ 。然而，请注意，如果上限不是3而是1，答案将是零，因为“尖峰”处在积分区域以外。

虽然 $\delta$ 本身不像是一个合理合规的函数，但在 $\delta$ 上的积分是完全可以认可的。事实上，最好将 $\delta$ 函数视为总是用于积分符号下面的函数。特别是，对所有的（“普通”）函数 $f(x)$ 都有 $^{13}$ ，如果

$$
\int_ {- \infty} ^ {\infty} f (x) D _ {1} (x) \mathrm{d} x = \int_ {- \infty} ^ {\infty} f (x) D _ {2} (x) \mathrm{d} x\tag{1.93}
$$

我们说涉及 $\delta$ 函数两个表达式[比如说， $D_{1}(x),D_{2}(x)]$ 是相等的。

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
习题1.44 计算下列积分：  
(a) $\int_2^6 (3x^2 - 2x - 1)\delta (x - 3)\mathrm{d}x.$   
(b) $\int_0^5\cos x\delta (x - \pi)\mathrm{d}x.$   
(c) $\int_0^3 x^3\delta (x + 1)\mathrm{d}x.$   
(d) $\int_{-\infty}^{\infty}\ln (x + 3)\delta (x + 2)\mathrm{d}x.$
</div>

习题1.45 计算下列积分：

(a) $\int_{-2}^{2}(2x+3)\delta(3x)\mathrm{d}x.$

$$
\int_ {0} ^ {2} (x ^ {3} + 3 x + 2) \delta (1 - x) \mathrm{d} x. \tag {b}
$$

$$
\int_ {- 1} ^ {1} 9 x ^ {2} \delta (3 x + 1) \mathrm{d} x. \tag {c}
$$

(d) $\int_{-\infty}^{a}\delta (x - b)\mathrm{d}x.$

习题1.46

(a) 证明

$$
x \frac {\mathrm{d}}{\mathrm{d} x} (\delta (x)) = - \delta (x)
$$

[提示：利用分部积分。]

(b) 设 $\theta(x)$ 为阶梯函数（step function）

$$
\theta (x) \equiv \left\{ \begin{array}{l l} 1, & x > 0 \\ 0, & x \leqslant 0 \end{array} \right.\tag{1.95}
$$

证明 $\mathrm{d}\theta/\mathrm{d}x = \delta(x)$ 。

## 1.5.3 三维 $\delta$ 函数

很容易将 $\delta$ 函数推广到三维：

$$
\delta^ {3} (\boldsymbol {r}) = \delta (x) \delta (y) \delta (z)\tag{1.96}
$$

[同前面一样， $\hat{r} = x\hat{x} + y\hat{y} + z\hat{z}$ 是从原点到点 $(x, y, z)$ 的位置矢量。] 这个三维 $\delta$ 函数在点 $(0, 0, 0)$ 为无限大，其他地方处处为零。其体积分为 1：

$$
\int_ {\mathrm{整个空间}} \delta^ {3} (\pmb {r}) \mathrm{d} \tau = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} \delta (x) \delta (y) \delta (z) \mathrm{d} (x) \mathrm{d} (y) \mathrm{d} (z) = 1\tag{1.97}
$$

并且，推广方程（1.92）

$$
\int_ {\text {整个空间}} f (\pmb {r}) \delta^ {3} (\pmb {r} - \pmb {a}) \mathrm{d} \tau = f (\pmb {a})\tag{1.98}
$$

与一维情况一样，对 $\delta$ 函数的积分可以把函数 f 在尖峰位置处的函数值挑选出来。

我们现在可以解决第 1.5.1 节中引入的悖论。你会记得，我们发现 $\hat{r}/r^{2}$ 的散度在除原点外的任何地方处处为零，但它在包含原点的任何体上的积分都是一个常数（即 $4\pi$ ）。这些正是界定狄拉克 $\delta$ 函数的条件；显然

$$
\nabla \cdot \left(\frac {\hat {\boldsymbol {r}}}{r ^ {2}}\right) = 4 \pi \delta^ {3} (\boldsymbol {r})\tag{1.99}
$$

更普遍地，

$$
\boxed {\nabla \cdot \left(\frac {\hat {\mathbf {r}}}{r ^ {2}}\right) = 4 \pi \delta^ {3} (\mathbf {r})}\tag{1.100}
$$

同前一样，其中 $z \equiv r - r'$ 是分离矢量。注意这里的求导是关于 r 的，而 $r'$ 保持不变。顺便说一句，因为

$$
\nabla \left(\frac {1}{r}\right) = - \left(\frac {\hat {r}}{r ^ {2}}\right)\tag{1.101}
$$

（见习题1.13b）由此可见

$$
\nabla^ {2} \left(\frac {1}{\imath}\right) = - 4 \pi \delta^ {3} (\imath)\tag{1.102}
$$

例题1.16 计算积分

$$
J = \int_ {\mathcal {V}} (r ^ {2} + 2) \nabla \cdot \left(\frac {\hat {\boldsymbol {r}}}{r ^ {2}}\right) \mathrm{d} \tau
$$

其中 V 是以原点为中心、半径为 R 的球体。

解法1：使用方程（1.99）重写散度，使用方程（1.98）进行积分：

$$
J = \int_ {\mathcal {V}} (r ^ {2} + 2) 4 \pi \delta^ {3} (\boldsymbol {r}) \mathrm{d} \tau = 4 \pi (0 + 2) = 8 \pi
$$

这个只有一行的解答显示了 $\delta$ 函数强大的优越性，但我还是要给你们展示第二种解题方法，这种方法有点烦琐，但可以说明第1.3.6节中的分部积分的方法。

解法2：利用方程（1.59），把对 $\hat{r} / r^2$ 的求导转换为对 $(r^2 + 2)$ 的求导：

$$
J = - \int_ {\mathcal {V}} \frac {\hat {\boldsymbol {r}}}{r ^ {2}} \cdot \nabla (r ^ {2} + 2) \mathrm{d} \tau + \oint_ {\mathcal {S}} (r ^ {2} + 2) \frac {\hat {\boldsymbol {r}}}{r ^ {2}} \cdot \mathrm{d} \boldsymbol {a}
$$

梯度为

$$
\nabla (r ^ {2} + 2) = 2 r \hat {\boldsymbol {r}}
$$

所以体积分变为

$$
\int {\frac {2}{r}} \mathrm{d} \tau = \int {\frac {2}{r}} r ^ {2} \sin \theta \mathrm{d} r \mathrm{d} \theta \mathrm{d} \phi = 8 \pi \int_ {0} ^ {R} r \mathrm{d} r = 4 \pi R ^ {2}
$$

同时，在球的边界上 $(r = R)$

$$
\mathrm{d} \boldsymbol {a} = R ^ {2} \sin \theta \mathrm{d} \theta \mathrm{d} \phi \hat {\boldsymbol {r}}
$$

所以面积分为

$$
\int (R ^ {2} + 2) \sin \theta \mathrm{d} \theta \mathrm{d} \phi = 4 \pi (R ^ {2} + 2)
$$

综合在一起

$$
J = - 4 \pi R ^ {2} + 4 \pi (R ^ {2} + 2) = 8 \pi
$$

这与前面结果一致。

习题1.47

（a）写出处在 $r'$ 点电荷 q 的体电荷密度 $\rho(\boldsymbol{r})$ 的表示式，确保 $\rho(\boldsymbol{r})$ 的体积分为 q。

（b）由位于原点的点电荷 $-q$ 和在 $\pmb{a}$ 点的点电荷 $+q$ 组成的电偶极子的体电荷密度是多少？

(c) 以原点为中心的半径为 $R$ 的、总电荷为 $Q$ 的均匀、无限薄球壳的体电荷密度（在球坐标系中）是多少？[提示：对整个空间的积分必须等于 $Q$ 。]

习题1.48 计算下列积分：

(a) $\int_{\text{整个空间}} (r^2 + r \cdot a + a^2) \delta^3 (r - a) \, \mathrm{d}\tau,$ 其中 $a$ 是一常矢量， $a$ 是它的大小，积分遍布整个空间。

(b) $\int_{\mathcal{V}} |\pmb{r} - \pmb{b}|^2 \delta^3 (5\pmb {r}) \mathrm{d}\tau$ ，其中 $\mathcal{V}$ 是中心在原点、边长为 2 的立方体， $\pmb{b} = 4\hat{\pmb{y}} + 3\hat{\pmb{z}}$ 。

(c) $\int_{\mathcal{V}}\left[r^{4}+r^{2}(\boldsymbol{r}\cdot\boldsymbol{c})+c^{4}\right]\delta^{3}(\boldsymbol{r}-\boldsymbol{c})\mathrm{d}\tau$ ，其中 V 是球心在原点、半径为 6 的球体； $c=5\hat{x}+3\hat{y}+2\hat{z}$ ，c 是它的大小。

(d) $\int_{\mathcal{V}} \boldsymbol{r} \cdot (\boldsymbol{d} - \boldsymbol{r}) \delta^3 (\boldsymbol{e} - \boldsymbol{r}) \mathrm{d}\tau$ ，其中 $d = (1,2,3)$ ， $e = (3,2,1)$ ，且 $\mathcal{V}$ 是球心在点 $(2,2,2)$ 、半径为 1.5 的球体。

习题1.49 如例题1.16所示，用两种不同方法计算积分

$$
J = \int_ {\mathcal {V}} \mathrm{e} ^ {- r} \nabla \cdot \left(\frac {\hat {\boldsymbol {r}}}{r ^ {2}}\right) \mathrm{d} \tau
$$

(其中 V 是球心在原点、半径为 R 的球。)

## 1.6 矢量场理论

## 1.6.1 亥姆霍兹定理

自法拉第以来，电学和磁学定律一直用电场 E 和磁场 B 来表述。与许多物理定律一样，这些定律可以最简洁地表示成微分方程。由于 E 和 B 都是矢量，微分方程自然要涉及矢量导数：散度和旋度。事实上，麦克斯韦将整个理论简化为四个方程，分别指定了 E 和 B 散度和旋度。

麦克斯韦方程提出了一个重要的数学问题：矢量函数在多大程度上由其散度和旋度所决定？换句话说，如果我告诉你 F 的散度（代表 E 和 B，视情况而定）是一个给定的（标量）函数 D，

$$
\nabla \cdot \boldsymbol {F} = D
$$

和 $\pmb{F}$ 的旋度是一个给定的（矢量）函数 $C$ ，即

$$
\nabla \times \boldsymbol {F} = \boldsymbol {C}
$$

（为了保持一致， $C$ 必须是无散度的，即 $\nabla \cdot C = 0$ ，因为旋度的散度始终为零。）那么，你能确定函数 $\pmb{F}$ 吗？

其实，并不见得能完全确定。例如，正如你在习题1.20中发现的那样，许多函数的散度和旋度处处为零——当然， $F = 0$ 是一种平庸情况，但有诸如 $F = yz\hat{x} + zx\hat{y} + xy\hat{z}$ ， $F = \sin x\cosh y\hat{x} -\cos x\sinh y\hat{y}$ ，等等。要求解微分方程，还必须给定适当的边界条件。在电动力学中，我们通常要求场“在无限远处”（远离所有电荷）为零 $^{14}$ 。有了这些额外的条件，亥姆霍兹定理保证了场由它的散度和旋度唯一地确定。（亥姆霍兹定理在附录 B 中讨论。）

## 1.6.2 势函数

如果矢量场（F）的旋度处处为零，则 F 可以表示为标（量）势（V, scalar potential）的梯度：

$$
\nabla \times \boldsymbol {F} = \mathbf {0} \Leftrightarrow \boldsymbol {F} = - \nabla V\tag{1.103}
$$

（负号纯属惯例）这是下列定理的核心：

定理 1：无旋场 [Curl-less (或 “irrotational”)fields]。下列条件是等价的（即，当且仅当 F 满足其他所有条件时它也满足余下的一条。）:

(a) 对于任何一点， $\nabla \times F = 0$ 。

(b) 对于任何给定的端点， $\int_{a}^{b}F\cdot dl$ 与路径无关。

(c) 对任何闭合路径， $\oint F \cdot dl = 0$ 。

(d) F 是某标量函数的梯度， $F = -\nabla V$ 。

标量势不是唯一的——任意常数都可以随意地加在 V 上，因为这不会影响其梯度大小。

如果矢量场（F）的散度处处为零，则 F 可以表示为矢势（A, vector potential）的旋度：

$$
\nabla \cdot \boldsymbol {F} = 0 \Leftrightarrow \boldsymbol {F} = \nabla \times \boldsymbol {A}\tag{1.104}
$$

这是下列定理的主要结论：

定理2：无散场[Divergence-less(或“solenoidal”)fields]。下列条件是等价的：

(a) 对于场中任何一点， $\nabla\cdot F=0$ 。

(b) 对于任何给定边界， $\int F\cdot \mathrm{d}\pmb{a}$ 与所选表面无关。

（c）对于任何闭合曲面， $\oint F\cdot \mathrm{d}\pmb {a} = 0$

(d) F 是某个矢量函数的旋度， $F = \nabla \times A$ 。

矢量势不是唯一的——加上任何一个标量的梯度都不会影响其旋度，因为梯度的旋度始终为零。

现在，除了（a）、（b）或（c）暗含（d）的联系，你应该能够证明这些定理之间的所有关系了。这些非常微妙，后面我们将会用到。顺便提及，在任何情况下（无论其散度和旋度如何），矢量场 F 都可以写成一个标量的梯度加上一个矢量的旋度：

$$
\boldsymbol {F} = - \nabla V + \nabla \times \boldsymbol {A}\tag{1.105}
$$

习题1.50

(a) 假设 $F_{1}=x^{2}\hat{z}$ ， $F_{2}=x\hat{x}+y\hat{y}+z\hat{z}$ 。计算 $F_{1}$ 和 $F_{2}$ 的散度和旋度。哪个可以写成标量的梯度？找到满足该要求的一个标量势。哪个可以写成矢量的旋度？找到一个合适的矢量势。

(b) 证明 $F_{3} = yz\hat{x} + zx\hat{y} + xy\hat{z}$ 即可以写成一个标量的梯度，也可以写成一个矢量的旋度。给出此函数的标量和矢量势。

习题1.51 由定理1证明， $(\mathrm{d})\Rightarrow (\mathrm{a}),(\mathrm{a})\Rightarrow (\mathrm{c}),(\mathrm{c})\Rightarrow (\mathrm{b}),(\mathrm{b})\Rightarrow (\mathrm{c})$ 以及 $(\mathrm{c})\Rightarrow (\mathrm{a})$ 。

习题1.52 由定理2证明， $(\mathrm{d})\Rightarrow (\mathrm{a}),(\mathrm{a})\Rightarrow (\mathrm{c}),(\mathrm{c})\Rightarrow (\mathrm{b}),(\mathrm{b})\Rightarrow (\mathrm{c})$ 以及 $(\mathrm{c})\Rightarrow (\mathrm{a})$ 。

习题1.53

（a）在习题1.15中，哪个矢量可以表示为标量的梯度。给出一个满足条件的标量函数。

（b）在习题1.15中，哪个矢量可以表示为矢量的旋度。给出一个这样的矢量。

## 第1章补充习题

习题1.54 使用半径为 $R$ 的球体的一个1/8作为体积（图1.48），对于函数

$$
\boldsymbol {v} = r ^ {2} \cos \theta \hat {\boldsymbol {r}} + r ^ {2} \cos \phi \hat {\boldsymbol {\theta}} - r ^ {2} \cos \theta \sin \phi \hat {\boldsymbol {\phi}}
$$

验证散度定理。确保包含整个表面。[答案： $\pi R^{4}/4$ ]

![](images/a4d2981ee1c0cb9c5b7bb60d7cd20f18a2d5fa4edddceda87b7ae91607abcb0c.jpg)  
图1.48

习题1.55 使用函数 $v = ay\hat{x} + bx\hat{y}$ （ $a, b$ 为常数）和以 $xy$ 平面中的原点为中心、半径为 $R$ 的圆形路径来验证斯托克斯定理。[答案： $\pi R^2(b - a)]$

习题1.56 沿图1.49所示的三角路径计算函数

$$
\pmb {v} = 6 \hat {\pmb {x}} + y z ^ {2} \hat {\pmb {y}} + (3 y + z) \hat {\pmb {z}}
$$

的线积分。利用斯托克斯定理验证你的结果。[答案：8/3]

![](images/2bd48cdf45824b38fe7073bb0bfeb55d2b8281ebaedf49b0de724c63e2605866.jpg)  
图1.49

习题 1.57 沿图 1.50 所示路径周围（这些点用直角坐标系标记）计算函数

$$
\pmb {v} = r ^ {2} \cos \theta \hat {\pmb {r}} - r \cos \theta \sin \theta \hat {\pmb {\theta}} + 3 r \hat {\pmb {\phi}}
$$

的线积分。在柱坐标系或球坐标系中分别计算。利用斯托克斯定理验证你的结果。[答案： $3\pi /2]$

![](images/032f50656ae4df50b97b1c4fd4e333c24a97fcf637baaf070afbd1d18356b01c.jpg)  
图1.50

习题1.58 使用图1.51所示的三角形曲面，验证函数 $v = y\hat{z}$ 的斯托克斯定理。[答案： $a^2$ ]

习题1.59 使用图1.52所示的“冰淇淋锥”的体积（顶面是球形的，半径为 $R$ ，中心位于原点），验证函数

$$
\pmb {v} = r ^ {2} \sin \theta \hat {\pmb {r}} + 4 r ^ {2} \cos \theta \hat {\pmb {\theta}} + r ^ {2} \tan \theta \hat {\pmb {\phi}}
$$

的散度定理。[答案： $(\pi R^2 /12)(2\pi +3\sqrt{3})]$

![](images/031fd7d7a8e238bbb49b5d79689e30993376486a158fb410e1e448f8de6327de.jpg)  
图1.51

![](images/dfbdc9945129c2b47e45ead7c97f7d70b042eaf461401b615cbab3319d4bbf8f.jpg)  
图1.52

习题1.60 以下是对两个基本定理的巧妙验证：

(a) 将梯度定理的推理 2 与斯托克斯定理（这里用 $v = \nabla T$ ）结合，证明所得结果与你已经知道的二次导数一致。

（b）将斯托克斯定理的推理2与散度定理结合，证明所得结果是我们已知所熟知的。

\- 习题1.61 虽然梯度、散度和旋度定理是矢量积分的基本积分定理，但可以从中推导出许多推论。证明：

(a) $\int_{\mathcal{V}} (\nabla T) \mathrm{d}\tau = \oint_{S} T \mathrm{d}\boldsymbol{a}$ 。[提示：在散度定理中，设 $\boldsymbol{v} = cT$ ，其中 $c$ 为常数，利用乘积定则。]

(b) $\int_{\mathcal{V}} (\nabla \times \boldsymbol{v}) \mathrm{d}\tau = -\oint_{\mathcal{S}} \boldsymbol{v} \times \mathrm{d}\boldsymbol{a}$ 。[提示：在散度定理中，以 $\boldsymbol{v} \times \boldsymbol{c}$ 代替 $\boldsymbol{v}$ 。]

(c) $\int_{\mathcal{V}}\left[T\nabla^{2}U + (\nabla T)\cdot (\nabla U)\right]\mathrm{d}\tau = \oint_{\mathcal{S}}(T\nabla U)\cdot \mathrm{d}\boldsymbol {a}_{\circ}$ [提示：在散度定理中，设 $\pmb {v} = T\nabla U]$

(d) $\int_{\mathcal{V}} (T \nabla^2 U - U \nabla^2 T) \, \mathrm{d}\tau = \oint_S (T \nabla U - U \nabla T) \cdot \mathrm{d}a$ 。[评注：这有时称为格林第二恒等式（Green's second identity），它由（c）得出，即格林恒等式（Green's identity）。]

(e) $\int_{\mathcal{S}} (\nabla T) \times \mathrm{d}\boldsymbol{a} = -\oint_{\mathcal{P}} T \mathrm{d}\boldsymbol{l}$ 。[提示：在斯托克斯定理中，设 $\boldsymbol{v} = cT$ 。]

习题1.62 积分

$$
a \equiv \int_ {S} \mathrm{d} a\tag{1.106}
$$

有时称为表面 S 的矢量面积。如果 S 恰好是平坦的，显然 $|a|$ 就是普通的（标量）面积。

(a) 求出半径为 R 的半球形碗的矢量面积。

(b) 证明对任何闭合曲面都有 $a = 0$ 。[提示：利用习题1.61a。]

(c) 证明对具有相同边界的任何曲面的 a 都相同。

(d) 证明

$$
a = \frac {1}{2} \oint r \times \mathrm{d} l\tag{1.107}
$$

其中积分是沿着边界线。[提示：一种方法是在原点绘制一个环对向的圆锥体。将圆锥体表面分割为无限多的三角楔形，每个楔形的顶点在原点，对边是 $\mathrm{d}l$ ，并利用叉积的几何解释（图1.18）。]

(e) 证明，对任何常矢量都有

$$
\oint (\boldsymbol {c} \cdot \boldsymbol {r}) \mathrm{d} l = \boldsymbol {a} \times \boldsymbol {c}\tag{1.108}
$$

[提示：在习题 1.61e 中设 $T = c \cdot r$ 。]

·习题 1.63

(a) 求函数

$$
\boldsymbol {v} = \frac {\hat {\boldsymbol {r}}}{r}
$$

的散度。首先，如方程（1.84）那样直接计算。然后，如式（1.85）那样，利用散度定理验证你的结果。就像函数 $\hat{r} / r^2$ 一样，原点是否存在 $\delta$ 函数？ $r^n\hat{r}$ 散度的一般公式是什么？[答案： $\nabla \cdot (r^n\hat{r}) = (n + 2)r^{n - 1}$ ，除非 $n = -2$ ，在这种情况下，它是 $4\pi \delta^3 (r)$ ；对于 $n < -2$ ，在原点处散度定义不清。]

(b) 求 $r^n \hat{r}$ 的旋度。用习题 1.61b 验证你的结果。[答案： $\nabla \times (r^n \hat{r}) = 0$ ]

习题1.64 如果你不相信 $\nabla^2 (1 / \hat{r}) = -4\pi \delta^3 (\hat{r})$ [为简单起见，令方程（1.102）中为 $\hat{r}' = 0]$ ，尝试用 $\sqrt{r^2 + \varepsilon^2}$ 替换 $r$ ，然后考察当 $\varepsilon \to 0$ 的结果[15]。具体来说，让

$$
D (r, \varepsilon) \equiv - \frac {1}{4 \pi} \nabla^ {2} \frac {1}{\sqrt {r ^ {2} + \varepsilon^ {2}}}
$$

为证明在 $\varepsilon \to 0$ 时上式为 $\delta^3 (\hat{r})$

(a) 证明： $D(r,\varepsilon)=(3\varepsilon^{2}/4\pi)(r^{2}+\varepsilon^{2})^{-5/2}$ 。

(b) 验证：当 $\varepsilon \to 0$ 时， $D(0, \varepsilon) \to \infty$ 。

(c) 验证：对于所有 $r \neq 0$ ，当 $\varepsilon \to 0$ 时， $D(r, \varepsilon) \to 0$ 。

(d) 验证 $D(r, \varepsilon)$ 在整个空间上的积分是否为 1。

## 第2章 静电学

## 2.1 电场

## 2.1.1 引言

电动力学希望解决的基本问题是（图 2.1）：空间有一些电荷 $q_{1}, q_{2}, q_{3}, \cdots$ （source charges，称为源电荷），它们对另一个电荷 Q（test charges，称为检验电荷）施加的力是什么？给定源电荷的位置（作为时间的函数），要计算检验电荷的轨迹。一般来讲，源电荷和检验电荷都是运动的。

叠加原理（principle of superposition）有助于解决这个问题，该原理指出，任何两个电荷之间的相互作用都不受其他电荷存在的影响。这意味着，为了确定作用在 Q 上的力，我们可以首先计算仅由 $q_{1}$ 引起的力 $F_{1}$ （忽略所有其他的力），然后我们计算仅由 $q_{2}$ 引起的力 $F_{2}$ ；最后，我们求出所有这些单独力的矢量和： $F = F_{1} + F_{2} + F_{3} + \cdots$ 。因此，如果我们能够求出单个源电荷 q 作用在 Q 上的力，原则上我们就解决问题了（剩下的只是一遍又一遍地重复相同的计算，并将其加起来的问题） $^{1}$ 。

好吧，这看起来好像非常容易：为什么我不直接写出 q 对 Q 的作用力公式，然后计算它？我将在第 10 章这么做，不过现在看到它你会感到震惊，因为作用在 Q 上的力不仅与距 q 的距离 r 有关（图 2.2），而且还与它们的速度以及 q 的加速度有关。此外，现在重要的不是 q 的位置、速度和加速度；电磁“信息”以光速传播，所以与 Q 有关的是在信息离开时的某个较早时间 q 的位置、速度和加速度。

![](images/655d1b030a400f01fd0e7da428d7499b7abe816b177f25f3a8633d0095541ab7.jpg)  
图2.1

![](images/9fa3d0d1bf1d612acb80a1fa947a71b4fc4640e558069befe23c357cbabee111.jpg)  
图2.2

因此，尽管基本问题（q 作用在 Q 上的力是多少）简单明了，但要处理起来却没有那么容易；我们将分阶段进行。与此同时，我们发展的理论将允许解决更复杂的电磁问题，这些问题不会以这种简单的形式出现。最开始，我们将考虑静电学（electrostatics）的特殊情况，其中所有源电荷都是静止的（尽管检验电荷可能在运动）。

## 2.1.2 库仑定律

相距 $z$ 处静止的单个点电荷 $q$ 对检验电荷 $Q$ 的作用力是多少？答案由（基于实验）库仑定律（Coulomb's law）给出：

$$
\boxed {F = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q Q}{r ^ {2}} \hat {\mathbf {r}}}\tag{2.1}
$$

常数 $\varepsilon_{0}$ 称为真空介电常数（permittivity of free space）。在国际单位制中，力的单位为牛顿（N），距离单位为米（m），电荷单位为库仑（C），则

$$
\varepsilon_ {0} = 8. 8 5 \times 1 0 ^ {- 1 2} \frac {\mathrm{C} ^ {2}}{\mathrm{N} \cdot \mathrm{m} ^ {2}}
$$

换句话说，力与电荷的乘积成正比，与间距的平方成反比。与以前一样（第1.1.4节），z 是从 $r'$ （q 的位置）到 $r$ （Q 的位置）的位移矢量：

$$
r = r - r ^ {\prime}\tag{2.2}
$$

$\hat{z}$ 是 $z$ 的大小， $\hat{z}$ 是 $z$ 的方向。力的指向为由 $q$ 点到 $Q$ 点的连线；若 $q$ 和 $Q$ 符号相同，表现为排斥力；若 $q$ 和 $Q$ 符号相反，表现为吸引力。

库仑定理和叠加原理构成了静电学的物理思想基础——除了物质的一些特殊性质外，其余的事情都是对这些基本规律的数学阐述。

习题2.1

$$
= \frac {Q}{4 \pi \varepsilon_ {0}} \left(\frac {q _ {1}}{r _ {1} ^ {2}} \hat {\pmb {\nu}} _ {1} + \frac {q _ {2}}{r _ {2} ^ {2}} \hat {\pmb {\nu}} _ {2} + \frac {q _ {3}}{r _ {3} ^ {2}} \hat {\pmb {\nu}} _ {3} + \dots\right)
$$

或者

$$
\boxed {F = Q E}\tag{2.3}
$$

其中

$$
\boldsymbol {E} (\boldsymbol {r}) \equiv \frac {1}{4 \pi \varepsilon_ {0}} \sum_ {i = 1} ^ {n} \frac {q _ {i}}{r _ {i} ^ {2}} \hat {\boldsymbol {z}} _ {i}\tag{2.4}
$$

E 称为源电荷的电场（electric field）。请注意，它是位置（r）的函数，因为位移矢量 $\alpha_{i}$ 取决于场点（field point）P 的位置（图 2.3）。但是这里并不涉及检验电荷 Q。电场是一个逐点变化的矢量，由源电荷的空间位置分布所决定；物理上讲，如果你把一个检验电荷放在 P 点上， $E(r)$ 则是每单位电荷施加在检验电荷上的力。

![](images/3e93debf9314be509796610a2b19ae1e0db78acdb6e28998c3d4c9fec5496ba3.jpg)  
图2.3

电场究竟是什么？我特意从你可以称之为 E 的“极简”解释开始，并作为计算电场力的中间步骤。但我鼓励你把电场想象成一个“真实”的物理实体，充满电荷周围的空间。麦克斯韦本人起初认为电场和磁场是一种看不见的原生态果冻状“以太”中的应力和应变。狭义相对论迫使我们放弃以太的概念，以及麦克斯韦对电磁场的力学解释。（即使很麻烦，也有可能将经典电动力学表述为“超距作用”理论，并完全抛弃场的概念。）此时，我不能告诉你们电场到底是什么——仅能告诉你如何计算它，以及一旦你得到它，又能去做些什么。

验证：当 $z \gg d$ 时，它看起来就像一个 $2q$ 的电荷，所以电场应该减小到 $E = \frac{1}{4\pi\varepsilon_0} \frac{2q}{z^2} \hat{z}$ 。确实如此（只需令公式中 $d \to 0$ ）。

a)  
![](images/67bc3d5281ccc3bb7eacd928b335e74dd5bdc648b5f0aa5b8444bcde88562306.jpg)

![](images/e0458e017cd533cdf689eb587a6ff88ce1e9dfc9d0d8aec1f9443b43742e3e14.jpg)  
图2.4  
b)

习题2.2 求相距为 $d$ 的等量异号电荷（ $\pm q$ ）的中点上方距离 $z$ 处的电场（大小和方向）（除了 $x = d / 2$ 处的电荷为 $-q$ ，与例题2.1相同）。

## 2.1.4 连续电荷分布

我们对电场的定义 [式（2.4）] 假设场源是分立的点电荷 $q_{i}$ 的集合。相反，如果电荷在某个区域上是连续分布的，则求和变为积分（图 2.5a）：

$$
\boldsymbol {E} (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {1}{\nu^ {2}} \hat {\mathbf {z}} \mathrm{d} q\tag{2.5}
$$

如果电荷沿一条线上分布（图 2.5b），每单位长度上的电荷为 $\lambda$ ，则 $dq = \lambda dl'$ （ $dl'$ 为沿着这条线的线元）；如果电荷分布在表面上（图 2.5c），单位面积上的电荷量为 $\sigma$ ，则 $dq = \sigma da'$ （ $da'$ 为表面的面元）；如果电荷分布在体积中（图 2.5d），单位体积中的电荷为 $\rho$ ，则 $dq = \rho d\tau'$ （ $d\tau'$ 为体元）：

$$
\mathrm{d} q \rightarrow \lambda \mathrm{d} l ^ {\prime} \sim \sigma \mathrm{d} a ^ {\prime} \sim \rho \mathrm{d} \tau^ {\prime}
$$

因此，线电荷的电场为

$$
\boldsymbol {E} (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\lambda (\boldsymbol {r} ^ {\prime})}{r ^ {2}} \hat {\boldsymbol {z}} d l ^ {\prime}\tag{2.6}
$$

对面电荷

$$
\boldsymbol {E} (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\sigma (\boldsymbol {r} ^ {\prime})}{r ^ {2}} \hat {\boldsymbol {r}} \mathrm{d} a ^ {\prime}\tag{2.7}
$$

对体电荷

$$
\boxed {E (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\rho (\boldsymbol {r} ^ {\prime})}{r ^ {2}} \hat {\mathbf {z}} d \tau^ {\prime}}\tag{2.8}
$$

![](images/298a19ef7bd17b38d296bec05402feff288053166f3b4ffb76105ac58accf6da.jpg)

![](images/c920216bf4c44f17f293febdb0d8822f958081758b5f5f43545f4ecf47621135.jpg)  
a) 连续分布

![](images/c78bd6c4fb49a3df3074d373a72d590f4ba48a4a6c6be4efa6f42dd48e4b1bf1.jpg)  
b) 线电荷, $\lambda$

![](images/174681a54b2f754bbe23e0a0257818e2ecc559f69d4dc63da192be4a3eeb3a13.jpg)  
c) 面电荷, $\sigma$

![](images/865a8dfb557b9b803a0bc49f7028be5f70b4824913acffba44b810e9f5241cb3.jpg)  
d)体电荷, $\rho$  
图2.5

式（2.8）通常也被称为“库仑定律”，因为它与原始式（2.1）很接近，而且从某种意义上说，体电荷是最普遍和最实际的情况。请仔细留意这些公式中 $\pmb{z}$ 的含义。最初，在式（2.4）中， $\pmb{z}_i$ 表示从源电荷 $q_i$ 到场点 $\pmb{r}$ 的矢量。相应地，在式（2.5）～式（2.8）中， $\pmb{z}$ 表示从 $\mathrm{d}q$ （因此是从 $\mathrm{d}l', \mathrm{d}a', \mathrm{d}\tau'$ ）到场点 $\pmb{r}$ 的矢量²。

[解答] 最简单的方法是将直线切割成成对的线元，对称放置（在 $\pm x$ 处），引用例题2.1的结果（ $d / 2 \to x, q \to \lambda \mathrm{d}x$ ），并积分（ $x:0 \to L$ ）。但这里有一个更普遍的方法 $^3$ ：

$$
\boldsymbol {r} = z \hat {\boldsymbol {z}}, \quad \boldsymbol {r} ^ {\prime} = x \hat {\boldsymbol {x}}, \quad \mathrm{d} l ^ {\prime} = \mathrm{d} x
$$

$$
\hat {\mathbf {z}} = \mathbf {r} - \mathbf {r} ^ {\prime} = z \hat {\mathbf {z}} - x \hat {\mathbf {x}}, \quad \eta = \sqrt {z ^ {2} + x ^ {2}}, \quad \hat {\mathbf {z}} = \frac {\mathbf {z}}{\eta} = \frac {z \hat {\mathbf {z}} - x \hat {\mathbf {x}}}{\sqrt {z ^ {2} + x ^ {2}}}
$$

$$
= \frac {\lambda}{4 \pi \varepsilon_ {0}} \left[ z \hat {z} \int_ {- L} ^ {L} \frac {1}{(z ^ {2} + x ^ {2}) ^ {3 / 2}} \mathrm{d} x - \hat {x} \int_ {- L} ^ {L} \frac {x}{(z ^ {2} + x ^ {2}) ^ {3 / 2}} \mathrm{d} x \right]
$$

$$
\begin{array}{l} {= \frac {\lambda}{4 \pi \varepsilon_ {0}} \left[ z \hat {z} \left(\frac {x}{z ^ {2} \sqrt {z ^ {2} + x ^ {2}}}\right) \Big | _ {- L} ^ {L} - \hat {x} \left(- \frac {1}{\sqrt {z ^ {2} + x ^ {2}}}\right) \Big | _ {- L} ^ {L} \right]} \\ {= \frac {1}{4 \pi \varepsilon_ {0}} \frac {2 \lambda L}{z \sqrt {z ^ {2} + L ^ {2}}} \hat {z}} \end{array}
$$

对于远离直线的点 $(z\gg L)$

$$
\boldsymbol {E} \cong \frac {1}{4 \pi \varepsilon_ {0}} \frac {2 \lambda L}{z ^ {2}}
$$

这是合情合理的：从远处看，这条线看起来像一个点电荷 $q = 2\lambda L$ 。另一方面，在 $L \to \infty$ 的极限下，我们得到了无限直导线的电场：

$$
E = \frac {1}{4 \pi \varepsilon_ {0}} \frac {2 \lambda}{z}\tag{2.9}
$$

习题2.3 求长度为 $L$ 的直线段的一端上方距离为 $z$ 处的电场（图2.7）。该直线段带有均匀的线电荷密度 $\lambda$ 。验证你得到的公式是否与你对 $z \gg L$ 时的预期一致。

习题 2.4 正方形环（边长为 a）分布有均匀线电荷密度 $\lambda$ ，求其中心上方距离 z 处的电场（图 2.8）。[提示：利用例题 2.2 的结果。]

习题2.5 求半径为 $r$ 的圆环中心上方距离 $z$ 处的电场（图2.9），该圆环带有均匀的线电荷密度为 $\lambda$ 。

![](images/5d8dbc561b932a5a489d2b05a0c84b1ada68b9053f904b4ae83035962ddf4328.jpg)  
图2.7

![](images/d72eeb5df27d2ee1b995aa9f60b7c421c96bbd54188589fcad4061bbb68783a8.jpg)  
图2.8

![](images/c9bd33528e8a8ffb269e0ce02f67cb26f743ac3d05a666df2906551173c45e6e.jpg)  
图2.9

习题 2.6 半径为 R 的圆盘带有均匀的面电荷密度为 $\sigma$ ，求其中心上方距离为 z 处的电场（图 2.10）。在极限 $R \to \infty$ 的情况下，从你的公式中能给出什么结论？同样还要验证 $z \gg R$ 的情况。

!习题 2.7 半径为 R 的球壳带有均匀的面电荷密度 $\sigma$ ，求距球心距离为 z 处的电场（图 2.11）。考虑 z < R（球内）和 z > R（球外）两种情况。用球面上所带的总电荷 q 表示你的答案。[提示：使用余弦定理将 n 用 $R, \theta$ 表示。确保取正平方根：如果 R > z，则 $\sqrt{R^{2} + z^{2} - 2Rz} = R - z$ ；但如果 R < z，则为 $z - R_{0}$ 。]

![](images/0b28578ec42d2e2f541631231d12b9eff4c8853a7d2bcd012fc4a84bab992b76.jpg)  
图2.10

![](images/3a1a9f12d746f2eddc2a714bc9efe7afef1facca5497ceb6cc6bc62e317b1a74.jpg)  
图2.11

习题2.8 使用习题2.7的结果，求半径为 $R$ 、体电荷密度为 $\rho$ 的均匀带电球体内外的电场。用球体所带的总电荷 $q$ 表示你的答案。画出 $|\pmb{E}|$ 作为距球心距离函数的图形。

## 2.2 静电场的散度和旋度

## 2.2.1 场线、通量和高斯定理

原则上，我们已经解决了静电学的问题。式（2.8）告诉我们如何计算电荷分布的电场，式（2.3）告诉我们施加在该电场的电荷 Q 所受作用力是什么。遗憾的是，正如你在习题 2.7 中所发现得那样，计算 E 所涉及的积分是非常棘手的，即便对于非常简单的电荷分布也是如此。静电学的其余大部分内容都致力于汇集大量的工具和技巧，以避免这些烦琐的积分。这一切都将始于 E 的散度和旋度。我将在 2.2.2 节中直接从式（2.8）计算 E 的散度，但首先我想向你展示一种更定性、也许更具启发性、更直观的方法。

让我们从最简单的情况开始。一个位于原点的点电荷：

$$
\boldsymbol {E} (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r ^ {2}} \hat {\boldsymbol {r}}\tag{2.10}
$$

为了对这个电场有个“直感”，在图2.12a中我画出它的一些代表性的矢量。由于该场是按照 $1/r^{2}$ 衰减的，距离原点越远矢量就越短；矢量指向总是沿径向向外的。但还有一种更有效的方法来表示这个场，那就是把箭头连接起来，形成电场线（field lines，图2.12b）。你可能会认为，我这样做会丢掉了关于箭头的长度所包含的电场强度的信息。实际上，并非如此。场的大小可由场线的密度表示：在中心附近，场线靠得很近，场线的强度很强，而在更远的地方，场线相距相对较远，场线强度较弱。

![](images/0f8f84d5a806c5f37043c6def627ee019aeb474049d8a70576fffec42b398895.jpg)

![](images/5068193b2f2e1e9709dea62519bb6c613d8a3d15a6e6128d9664a9087363235b.jpg)  
图2.12

事实上，当我在二维表面上绘制电场线图时，场线图是误导人的，因为穿过半径为 r 的圆的场线密度是总数除以周长 $(n/2\pi r)$ ，类似于按照 1/r 减小，而并非 $1/r^{2}$ 。但是，如果你把模型想象成三维的（像一个球形针插，在所有的方向都有外指的针），在三维空间来画电场线时则场线密度就是总场线数除以球的面积 $(n/4\pi r^{2})$ ，这的确是按 $1/r^{2}$ 减小的。

这样的场线图也便于表示更复杂的场。当然，你想要画的线条数量取决于你有多懒（以及你的铅笔有多锋利），不过你应该包括足够数目的线条来准确地描述这个场的含义，而且你必须保持自洽：如果电荷 q 有 8 条，那么 2q 应该有 16 条。而且你必须把它们合理地隔开——它们从一个点电荷对称地向各个方向发出。电场线从正电荷出发，终止于负电荷；场线不能空中某处中断 $^{4}$ ，尽管它们可以延伸到无限远处。此外，电场线永远不会交叉——如果交叉意味着在交叉点处的电场有两个不同的方向！考虑到这一切，就可以很容易地画出任何的简单点电荷构型形成的场线：首先在每一个点电荷附近区域画出它的场线，然后连接这些场线或者把它们延伸到无限远处（图 2.13 和图 2.14）。

![](images/81a4989b5393edee097e8c7ced79e55c2c93b26b608a5348b4aeba4478cbf49f.jpg)  
两个异号电荷

图2.13  
![](images/32c9d6b4fdf8357d9b7194ec5164c91ee18603d877f1d9b7f56dd08c2079c1e5.jpg)  
图2.14

在这种模型中，通过表面 S 的 E 的电通量为

$$
\Phi_ {E} \equiv \int_ {\mathcal {S}} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {a}\tag{2.11}
$$

它是通过 S 的 “场线数目” 的量度。我之所以把它放在引号中是因为我们仅能画出一些代表性的场线——总的数目是无限多的。但对于给定的采样率，通量与绘制的场线数成正比，因为场强与场线密度成正比（单位面积的场线数量）；因此， $E \cdot da$ 与穿过无限小面元 da 的场线数也成正比。（如图 2.15 所示，点积给出 da 沿电场 E 方向的分量。当我们说场线密度是每单位面积的数量时，我们指的是它垂直于 E 的平面内的面积。）

![](images/cf4a3a426f051a37b04ee37e85499b125467ab062a2b9a3dfe6001ece51e86c9.jpg)  
图2.15

这表明，通过任何闭合曲面的通量是曲面内部所含总电荷的量度。对于源自正电荷的场线，要么穿出闭合曲面，要么终止于曲面内部的负电荷上（图2.16a）。另一方面，位于闭合曲面外的电荷对总的通量没有任何贡献，因为它的场线从闭合曲面一侧传入，而从另一侧穿出（图2.16b）。这就是高斯定理（Gauss's law）的本质。现在让我们把它定量化。

![](images/5dc3502194a2c193699d26cd6d2970be5c2c57a191f3988ad7f829111b36c826.jpg)

![](images/a98dd371e54b467908f357bf0b3e418309fb9fd3ca908a0ff10028fc6a138f8a.jpg)  
图2.16

对于位于原点的点电荷 q，通过半径为 r 的球面 E 的通量为

$$
\oint \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {a} = \int \frac {1}{4 \pi \varepsilon_ {0}} \left(\frac {q}{r ^ {2}} \hat {\boldsymbol {r}}\right) \cdot \left(r ^ {2} \sin \theta \mathrm{d} \theta \mathrm{d} \phi \hat {\boldsymbol {r}}\right) = \frac {1}{\varepsilon_ {0}} q\tag{2.12}
$$

请注意，上式中球的半径相互抵消，因为球表面积按 $r^2$ 增大，而电场强度按 $1/r^2$ 减小，所以两者乘积是不变的。就场线图而言，这更有道理；因为无论球体大小如何，从以原点为中心穿出的场线数量是相同的。事实上，它不一定是球体——任何封闭的表面，无论其形状如何，都会被相同数量的场线刺穿。显然，通过包围电荷的任何闭合表面的通量都是 $q/\varepsilon_0$ 。

现在假设不再是原点处的一个点电荷，而是一堆分散的电荷。根据叠加原理，总的电场强度是所有单个电荷的电场强度的（矢量）和：

$$
\boldsymbol {E} = \sum_ {i = 1} ^ {n} \boldsymbol {E} _ {i}
$$

通过包围他们的表面的通量为

$$
\oint \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {a} = \sum_ {i = 1} ^ {n} \left(\oint \boldsymbol {E} _ {i} \cdot \mathrm{d} \boldsymbol {a}\right) = \sum_ {i = 1} ^ {n} \left(\frac {1}{\varepsilon_ {0}} q _ {i}\right)
$$

对任何闭合表面，

$$
\boxed {\oint \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {a} = \frac {1}{\varepsilon_ {0}} Q _ {\text {enc}}}\tag{2.13}
$$

其中 $Q_{enc}$ 是闭合表面内的总电荷。这就是高斯定理的定量表述。虽然它不比库仑定律和叠加原理中包含更多的信息，但正如你将在第 2.2.3 节中看到的那样，它具有十分神奇的能力。请注意，这一切都取决于库仑定律的 $1/r^{2}$ 性质；否则，式（2.12）中 r 就不会被抵消，E 的总通量将不单单是取决于闭合面内包含的总电荷，也取决于所选择表面。其他的 $1/r^{2}$ 力（我特别想到的是牛顿的万有引力定律）也服从它们自己的“高斯定理”，我们在这里所讨论的应用对它们也直接适用。

目前，高斯定理是一个积分方程，但通过应用散度定理，我们可以很容易地将其转换为微分方程

$$
\oint_ {\mathcal {S}} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {a} = \int_ {\mathcal {V}} (\nabla \cdot \boldsymbol {E}) \mathrm{d} \tau
$$

用电荷密度 $\rho$ 表示 $Q_{enc}$ ，有

$$
Q _ {\mathrm{enc}} = \int_ {\mathcal {V}} \rho \mathrm{d} \tau
$$

所以，高斯定理变为

$$
\int_ {\mathcal {V}} (\nabla \cdot \boldsymbol {E}) \mathrm{d} \tau = \int_ {\mathcal {V}} \left(\frac {\rho}{\varepsilon_ {0}}\right) \mathrm{d} \tau
$$

由于这对任何体积上都成立，因此被积函数必须相等：

$$
\boxed {\nabla \cdot \boldsymbol {E} = \frac {1}{\varepsilon_ {0}} \rho}\tag{2.14}
$$

式（2.14）含有与式（2.13）同样多的信息；它是高斯定理的微分形式（Gauss's law in differential form）。微分形式更简洁，但积分形式的优点是它更自然地适合讨论点、线和面电荷分布情况。

习题 2.9 假定在球坐标系中，某个区域的电场为 $E = kr^{3}\hat{r}$ （k 为常数）。

(a) 求出电荷密度 $\rho_{0}$

(b) 求出以原点为中心、半径为 R 的球体中包含的总电荷。(用两种不同的方法。)

习题2.10 如图2.17所示，电荷 $q$ 位于立方体的后下角。通过阴影面 $\pmb{E}$ 的通量是多少？

![](images/f4fa3ac37d70c8750248b51f0949e5eb9afbda08a2165daffe0d4a480f0ca863.jpg)  
图2.17

## 2.2.2 $E$ 的散度

现在，让我们回过头来，直接由式（2.8）计算 E 的散度：

$$
\boldsymbol {E} \left(\boldsymbol {r}\right) = \frac {1}{4 \pi \varepsilon_ {0}} \int_ {\mathrm{整个空间}} \frac {\hat {\textbf {\mathrm{之}}}}{\nu^ {2}} \rho \left(\boldsymbol {r} ^ {\prime}\right) \mathrm{d} \tau^ {\prime}\tag{2.15}
$$

（起初，积分仅对有电荷占据的空间进行，但我可以将其扩展到整个空间，因为无论如何，外部区域的 $\rho = 0$ 。）注意到电场对 $r$ 的依赖是包含在 $z = r - r'$ 中的，我们有

$$
\nabla \cdot \boldsymbol {E} (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \int \nabla \cdot \left(\frac {\hat {\boldsymbol {r}}}{r ^ {2}}\right) \rho (\boldsymbol {r} ^ {\prime}) \mathrm{d} \tau^ {\prime}
$$

这正是我们在式（1.100）计算过的散度：

$$
\nabla \cdot \left(\frac {\hat {\mathbf {r}}}{\mathbf {r} ^ {2}}\right) = 4 \pi \delta^ {3} (\mathbf {r})
$$

因此

$$
\nabla \cdot \boldsymbol {E} = \frac {1}{4 \pi \varepsilon_ {0}} \int 4 \pi \delta^ {3} (\boldsymbol {r} - \boldsymbol {r} ^ {\prime}) \rho (\boldsymbol {r} ^ {\prime}) \mathrm{d} \tau^ {\prime} = \frac {1}{\varepsilon_ {0}} \rho (\boldsymbol {r})\tag{2.16}
$$

这正是高斯定理的微分形式 [式（2.14）]。为了恢复到积分形式 [式（2.13）]，我们颠倒前面的过程，对体积进行积分并利用散度定理：

$$
\int_ {\mathcal {V}} (\nabla \cdot \boldsymbol {E}) \mathrm{d} \tau = \oint_ {\mathcal {S}} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {a} = \frac {1}{\varepsilon_ {0}} \int_ {\mathcal {V}} \rho \mathrm{d} \tau = \frac {1}{\varepsilon_ {0}} Q _ {\text {enc}}
$$

## 2.2.3 高斯定理的应用

此时，我必须把理论探讨停下来，向你们展示一下高斯定理积分形式的特别有用之处。当对称性允许时，它提供了迄今为止最快、最简单的计算电场的方法。我将通过几个例子来说明这种方法。

$\pmb{E}$ 的大小在高斯面上是恒定的，因此它可以被移到积分号外：

\( ^{12} \) \( ^{1} \) \( ^{1} \) \( ^{1} \) \( ^{1} \) \( ^{1} \) \( ^{1} \) \( ^{1} \) \( ^{1} \) \( ^{1} \) \( ^{1} \) \( ^{1} \) \( ^{1} \) \( ^{1} \) \( ^{1} \) \( ^{1} = 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5

$\cdots\cdots=1$

$$
\int_ {\mathcal {S}} | \pmb {E} | \mathrm{d} a = | \pmb {E} | \int_ {\mathcal {S}} \mathrm{d} a = | \pmb {E} | 4 \pi r ^ {2}
$$

$$
| \pmb {E} | 4 \pi r ^ {2} = \frac {1}{\varepsilon_ {0}} q
$$

$$
\pmb {E} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r ^ {2}} \hat {\pmb {r}}
$$

请注意这一结果的一个显著特征：球体外的电场与把所有电荷都集中在中心时所产生的电场完全相同。

1. $\frac{1}{2}$ . $\frac{1}{2}$ . $\frac{1}{2}$ . $\frac{1}{2}$ . $\frac{1}{2}$ . $\frac{1}{2}$ . $\frac{1}{2}$ . $\frac{1}{2}$ . $\frac{1}{2}$ . $\cdots$ . $\frac{1}{2}$ . $\frac{1}{2}$ . $\frac{1}{2}$ . $\frac{1}{2}$ . $\frac{1}{2}$ . $\frac{1}{2}$ . $\frac{1}{2}$ . $\frac{1}{2}$ .

![](images/62a81e7a53395c2c731eca3ea2a627a73584406c0e44fecee79ac5bb68ed50fc.jpg)  
图2.18

$^{22}$ $^{23}$ $^{24}$ $^{25}$ $^{26}$ $^{27}$ $^{28}$ $^{29}$ $^{30}$ $^{31}$ $^{32}$ $^{33}$ $^{34}$ $^{35}$ $^{36}$ $^{37}$ $^{38}$ $^{39}$ $^{40}$ $^{41}$ $^{42}$ $^{43}$ $^{44}$ $^{45}$ $^{46}$ $^{47}$ $^{48}$ $^{49}$ $^{50}$ $^{51}$ $^{52}$ $^{53}$ $^{54}$ $^{55}$ $^{56}$ $^{57}$ $^{58}$ $^{59}$ $^{60}$ $^{61}$ $^{62}$ $^{63}$ $^{64}$ $^{65}$ $^{66}$ $^{67}$ $^{68}$ $^{69}$ $^{70}$ $^{71}$ $^{72}$ $^{73}$ $^{74}$ $^{75}$ $^{76}$ $^{77}$ $^{78}$ $^{79}$ $^{80}$ $^{81}$ $^{82}$ $^{83}$ $^{84}$ $^{85}$ $^{86}$ $^{87}$ $^{88}$ $^{89}$ $^{90}$ $^{91}$ $^{92}$ $^{93}$ $^{94}$ $^{95}$ $^{96}$ $^{97}$ $^{98}$ $^{99}$ $^{100}$

高斯定理总是成立的，但是并不总是有用的。如果 $\rho$ 不是均匀的（或者，至少不是球对称分布），或者我们选择了其他形状的高斯面；那么， $\pmb{E}$ 的通量仍然是 $q / \varepsilon_0$ ，但是 $\pmb{E}$ 方向不一定总是与 $\mathrm{d}\pmb{a}$ 的方向相同，它的大小在高斯面上也未必是恒定的；没有这一点，我们也就无法把 $|\pmb{E}|$ 移到积分号外。对称性对于高斯定理的应用至关重要。据我所知，只有三种对称性对高斯定理是有效的：

（1）球对称性：高斯面为同心球面。

(2) 柱对称性: 高斯面为共轴圆柱面 (图 2.19)。

（3）平面对称性：高斯面为横跨表面的“扁盒”状柱面（图2.20）。

尽管（2）和（3）在原则上要求无限长的圆柱体和延伸到无限长的平面，但我们常常可以对远离边缘的“长”圆柱体或者“大”的平面体系做近似求解。

![](images/705a726afa4662091fb6145b0b3d7ac223ade0cc06a252c47a6ae402559f1da2.jpg)  
图2.19

![](images/e1bc0b7301a5b69044b1dcec331b461a289efc46ead46290d0d4ebb9b89ddcc1.jpg)  
图2.20

[解答] 在圆柱体内画一个长度为 $l$ 、半径为 $s$ 的高斯圆柱体面。对该曲面，由高斯定理得

$\oint_{S} \boldsymbol{E} \cdot \mathrm{d}\boldsymbol{a} = \frac{1}{\varepsilon_0} Q_{\text{包含柱面内}}$

所包含的电荷为

$$
Q _ {\mathrm{enc}} = \int \rho \mathrm{d} \tau = \int (k s ^ {\prime}) (s ^ {\prime} \mathrm{d} s ^ {\prime} \mathrm{d} \phi \mathrm{d} z) = 2 \pi k l \int_ {0} ^ {s} s ^ {\prime 2} \mathrm{d} s ^ {\prime} = \frac {2}{3} \pi k l s ^ {3}
$$

[我使用了式（1.78）中适用于柱坐标的体积元，并从0到 $2\pi$ 对 $\mathrm{d}\phi$ 进行积分，从0到 $l$ 对 $\mathrm{dz}$ 进行积分；我在积分变量 $s$ 上加了一撇，以将其与高斯面的半径 $s$ 区分开来。]

![](images/6d9a16565b8e6cb60a8a82e678199a4ad837e4aa6ca77cf1354ad3b11a002e55.jpg)  
图2.21

现在，对称性要求 $\pmb{E}$ 必须沿径向指向外，因此对于高斯圆柱体侧面弧形部分，我们有

$$
\int \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {a} = \int | \boldsymbol {E} | \mathrm{d} a = | \boldsymbol {E} | \int \mathrm{d} a = | \boldsymbol {E} | 2 \pi s l
$$

而两端的表面贡献为零（这里 E 垂直于 da）。因此，

$$
| \pmb {E} | 2 \pi s l = \frac {1}{\varepsilon_ {0}} \frac {2}{3} \pi k l s ^ {3}
$$

最后有

$$
\boldsymbol {E} = \frac {1}{3 \varepsilon_ {0}} k s ^ {2} \hat {\boldsymbol {s}}
$$

例题 2.5 无限大平面带有均匀的电荷密度 $\sigma$ ，求它的电场强度。

[解答] 画出一个“高斯扁盒”，在平面上下延伸相等的距离（图2.22）。将高斯定理应用于此曲面：

$$
\oint \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {a} = \frac {1}{\varepsilon_ {0}} Q _ {\mathrm{enc}}
$$

在这种情况下， $Q_{enc} = \sigma A$ ，其中 A 是扁盒盖子的面积。根据对称性，E 指向远离平面的方向（向上指向上方的点，向下指向下方的点）。因此，顶面和底面给出

$$
\oint \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {a} = 2 A | \boldsymbol {E} |
$$

侧面的贡献为零，因此

$$
2 A | \pmb {E} | = \frac {1}{\varepsilon_ {0}} \sigma A
$$

$$
\boldsymbol {E} = \frac {\sigma}{2 \varepsilon_ {0}} \hat {\boldsymbol {n}}\tag{2.17}
$$

其中 $\hat{n}$ 是指向远离曲面的单位矢量。在习题2.6中，你曾用一个很麻烦的方法得到这一结果。

![](images/4e8b694e23ea970a1d59c0a98166be0ef590f6b413734ecbc5f05668954a1f8b.jpg)  
图2.22

首先，令人惊讶的是，无限大平面产生的电场强度与到平面的距离无关。库仑定律中的 $1 / r^2$ 规律还成立吗？这里关键在于，随着你越来越远离平面，越来越多的电荷进入你的“视野”（从你的眼睛延伸出来的锥形），这个弥补了距离的增加导致的电场强度的减弱。球体外的电场按照 $1 / r^2$ 减小；无限长直线的电场按照 $1 / r$ 减小；而无限大平面的电场不随距离发生变化（你无法逃离无限大平面）。

尽管直接利用高斯定理计算电场仅限于球形、圆柱形和平面对称的情况，但我们可以计算具有这些对称性物体组合形成的体系的电场，即便是它们作为一个整体不存在对称性。例如，借助叠加原理，我们可以求出两个平行的均匀带电圆柱体附近区域的电场，或者是在无限大平面附近存在一个球体所形成的电场。

例题2.6 两无限大平行平面分别带有大小相等但符号相反的均匀电荷密度 $\pm \sigma$ （图2.23）。求出在下列三个区域内的电场强度：（i）在两者的左侧，（ii）在两者的中间，（iii）在两者的右侧。[解答]左板形成的电场的电场强度大小为 $\sigma /2\varepsilon_0$ ，方向指向远离它的方向（图2.24），在区域（i）中指向左，在区域（ii）和（iii）中指向右。带负电荷的右板形成的电场的电场强度大小为 $\sigma /2\varepsilon_0$ ，该场指向板本身——在区域（i）和（ii）中指向右，在区域（iii）中指向左。这两个电场在区域（i）和（iii）中相互抵消；在区域（ii）中叠加。结论：在两平面之间的电场大小为 $\sigma /\varepsilon_0$ ，方向指向右侧；其他地方为零。

![](images/bc5213af9a06b2ee0173c03e9e2616350e72d7129caf1701e0184ddf3a1657a9.jpg)  
图2.23

![](images/3b6ffd62a50785c64da50e50b183b6c30852879df5ea8af403db345061bee8b0.jpg)  
图2.24  
习题2.11 使用高斯定理求出半径为 $R$ 的球壳内外的电场强度，球壳带有均匀的表面电荷密度 $\sigma$ 。

将你的答案与习题 2.7 进行比较。

习题2.12 利用高斯定理，求出均匀带电球体内的电场。将你的答案与习题2.8进行比较。

习题2.13 求出距无限长直导线的距离为 $s$ 处的电场，该直线带有均匀的线电荷密度 $\lambda$ 。并与式（2.9）做比较。

习题2.14 带电球体的电荷密度与离原点的距离成正比， $\rho = kr$ ， $k$ 是某个常数，求球体内部的电场。[提示：这个球体的电荷分布不是均匀的，你必须通过积分才能得到球体内的总电荷。]

习题2.15 厚球壳携带的电荷密度（图2.25）

$$
\rho = \frac {k}{r ^ {2}} \quad (a \leqslant r \leqslant b)
$$

求出下列三个区域中的电场：（i） $r < a$ ，（ii） $a < r < b$ ，（iii） $r > b$ 。对于 $b = 2a$ 的情况，画出 $|E|$ 作为 $r$ 的函数关系图。

习题2.16 长同轴电缆（图2.26）的内芯（半径为 $a$ ）载有均匀的体电荷密度 $\rho$ ，外圆柱形壳层（半径为 $b$ ）载有均匀的面电荷密度。面电荷为负值，其大小正好是使得整个电缆是电中性的。求出下列三个区域内的电场：（i）内芯里面（ $s < a$ ），（ii）内芯与外壳层之间（ $a < s < b$ ），（iii）电缆外部（ $s > b$ ）。画出 $|E|$ 随 $s$ 的函数变化图。

![](images/9f58d1cb833919b75808a3f0242c4f6426b1ad5f645c3e6fdcf37475da02da85.jpg)  
图2.25

![](images/c183dfd7e4bd3d551131891b3880dcda3fd269122ced9752b07753231bd03b2f.jpg)  
图2.26

习题 2.17 厚度为 2d 的无限大平板带有均匀的体电荷密度 $\rho$ （图 2.27）。取 y=0 为平板的中心，求出以 y 作为函数的电场，并画出 E 随 y 的变化关系图。当 E 指向 +y 方向时称其为正，当它指向 -y 方向称其为负。

\- 习题2.18半径均为 $R$ 两个带电球体分别带有均匀的电荷密度 $\rho$ 和 $-\rho$ ，将其部分交叠放置（图2.28）。令从带正电球的中心到带负电球的中心的距离矢量为 $d$ 。证明在交叠区的电场强度为一恒定值，并求出该值。[提示：利用习题2.12的结果。]

![](images/b1bac8efb97108d45e71a9a03e75978370c3a37adb142119612b8d81ffe34e22.jpg)  
图2.27

![](images/05bf6b55cd00c2e14df077b67236c338e60836ed8aba77dbaa90ae489f714952.jpg)  
图2.28

## 2.2.4 E 的旋度

首先，如同我在2.2.1节计算 $\pmb{E}$ 的散度那样，我将通过学习一个最简单的构型——一个位于原点的点电荷，来计算 $\pmb{E}$ 的旋度。在这种情况下，

$$
\pmb {E} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r ^ {2}} \hat {\pmb {r}}
$$

现在，观察图2.12应该使你相信这个电场的旋度必须为零，但我想我们还是应该设法给出一个比这更严谨的证明。如果我们计算这个场从某个点 $\pmb{a}$ 到另一个点 $\pmb{b}$ 的线积分（图2.29）：

$$
\int_ {a} ^ {b} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l}
$$

在球坐标系中， $\mathrm{d}\pmb {l} = \mathrm{d}r\hat{\pmb{r}} + r\mathrm{d}\theta \hat{\pmb{\theta}} + r\sin \theta \mathrm{d}\phi \hat{\phi}$ ，所以

$$
\boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r ^ {2}} \mathrm{d} r
$$

![](images/a4f77f94706413ededb386e4fa7c7a49b829584b638d9e0567c81a0a9a00acbb.jpg)  
图2.29

因此，

$$
\int_ {a} ^ {b} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = \frac {1}{4 \pi \varepsilon_ {0}} \int_ {a} ^ {b} \frac {q}{r ^ {2}} \mathrm{d} r = \frac {- 1}{4 \pi \varepsilon_ {0}} \left. \frac {q}{r} \right| _ {r _ {a}} ^ {r _ {b}} = \frac {1}{4 \pi \varepsilon_ {0}} \left(\frac {q}{r _ {a}} - \frac {q}{r _ {b}}\right)\tag{2.18}
$$

其中， $r_{a}$ 是从原点到 a 点的距离， $r_{b}$ 是从原点到 b 点的距离。沿一个闭合路径的积分显然为零（因为 $r_{a}=r_{b}$ ）：

$$
\boxed {\oint \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = 0}\tag{2.19}
$$

因此，应用斯托克斯定理，

$$
\boxed {\nabla \times \boldsymbol {E} = \mathbf {0}}\tag{2.20}
$$

现在，我所证明的电场方程（2.19）和（2.20）仅是限于位于原点处的单个点荷的，但这些结果并没有涉及任意的选择什么样的坐标系；无论电荷位于何处，他们都成立。此外，如果有很多电荷，叠加原理表明总的电场强度是它们各自电场的矢量和：

$$
\pmb {E} = \pmb {E} _ {1} + \pmb {E} _ {2} + \dots
$$

所以

$$
\nabla \times \pmb {E} = \nabla \times (\pmb {E} _ {1} + \pmb {E} _ {2} + \dots) = \nabla \times \pmb {E} _ {1} + \nabla \times \pmb {E} _ {2} + \dots = \mathbf {0}
$$

因此，式（2.19）和式（2.20）适用于任何静电荷分布的场。

习题2.19 根据式（2.8），利用第2.2.2节中的方法直接计算 $\nabla \times E$ 。如果你被卡住了，请参阅习题1.63。

## 2.3 电势

## 2.3.1 引言

电场 E 不是随便哪个普通的矢量函数，它是一种非常特殊的矢量函数：旋度为零的矢量函数。例如， $E = y\hat{x}$ 就不可能是静电场，任何一组电荷，无论其大小和位置如何，都无法产生这样的电场。我们将利用电场的这一特殊性质，把矢量问题（求 E）简化为更简单的标量问题。在 1.6.2 节中的第一个定理指出，任何旋度为零的矢量都等于某个标量的梯度。我现在要做的是，在静电学的背景下来证明这一结论。

因为 $\nabla \times \mathbf{E} = \mathbf{0}$ , $\mathbf{E}$ 对任何闭合环路的线积分为零（这是根据斯托克斯定理得出的）。由于 $\oint \mathbf{E} \cdot \mathrm{d}\mathbf{l} = 0$ ，从点 $a$ 到点 $b$ , $\mathbf{E}$ 的线积分对所有路径都是相等的 [否则，你可以沿路径（i）出去，然后沿着路径（ii）返回，如图2.30所示，得到 $\oint \mathbf{E} \cdot \mathrm{d}\mathbf{l} \neq 0$ 的矛盾结果]。因为电场的线积分与路径无关，我们可以定义一个函数 $^6$

$$
\boxed {V (\boldsymbol {r}) \equiv - \int_ {\mathcal {O}} ^ {\boldsymbol {r}} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l}}\tag{2.21}
$$

其中 O 是我们事先商定的一些标准参考点；这样 V 仅与点 $\hat{r}$ 坐标有关，它被称为电势 (electric potential)。

![](images/9b1005e2b594dbe9340fc94c31848e65710bd30374559cc0222c8875f1bb9bf8.jpg)  
图2.30

$$
V (\boldsymbol {r}) \equiv - \int_ {\mathcal {O}} ^ {\boldsymbol {r}} \boldsymbol {E} (\boldsymbol {r} ^ {\prime}) \cdot \mathrm{d} \boldsymbol {l} ^ {\prime}
$$

$a$ 和 $b$ 两点之间的电势差为

$$
\begin{array}{r l} V (\boldsymbol {b}) - V (\boldsymbol {a}) & = - \int_ {\mathcal {O}} ^ {\boldsymbol {b}} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} + \int_ {\mathcal {O}} ^ {\boldsymbol {a}} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} \\ & = - \int_ {\mathcal {O}} ^ {\boldsymbol {b}} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} - \int_ {\boldsymbol {a}} ^ {\mathcal {O}} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = - \int_ {\boldsymbol {a}} ^ {\boldsymbol {b}} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} \end{array}\tag{2.22}
$$

梯度的基本定理表明

$$
V (\boldsymbol {b}) - V (\boldsymbol {a}) = \int_ {\boldsymbol {a}} ^ {\boldsymbol {b}} (\nabla V) \cdot \mathrm{d} \boldsymbol {l}
$$

所以

$$
\int_ {a} ^ {b} (\nabla V) \cdot \mathrm{d} \boldsymbol {l} = - \int_ {a} ^ {b} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l}
$$

最后，由于这对任何点 $a$ 和 $b$ 都是成立的，因此被积函数必须相等：

$$
\boxed {E = - \nabla V}\tag{2.23}
$$

式（2.23）是式（2.21）的微分表述；它指出静电场是一标量势函数的梯度，这就是我们想要证明的。

请注意在这个论证中，路径无关（或者，等价为 $\nabla \times \pmb{E} = 0$ 的事实）所起到的微妙但至关重要的作用。如果 $\pmb{E}$ 的线积分与所走的路径有关，那么式（2.21）中 $V$ 的定义将是无稽之谈。既然改变路径就会改变 $V(\pmb{r})$ 的值，在这种情况下是无法定义势函数的。顺便说一句，不要让式（2.23）中的减号转移你的注意力；它从式（2.21）延续而来，在很大程度上这是一个约定。

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
习题2.20 下面的哪一个不可能是静电场？(a) $\pmb{E} = k[xy\hat{x} + 2yz\hat{y} + 3xz\hat{z} ]$ (b） $E = k[y^{2}\hat{x} +(2xy + z^{2})\hat{y} + 2yz\hat{z} ].$
</div>

这里 $k$ 是一具有适当单位的常数。使用原点作为参考点，求出可能的电场的势的大小。并通过计算 $\nabla V$ 来验证你的结果。[提示：你必须选择一个具体的路径来进行积分。选择什么路径是无关紧要的，因为结果是路径无关的；但除非你指定了一条具体的路径，否则根本无法进行积分。]

## 2.3.2 有关势的评注

（i）名称。“势”这个词用词不当，因为它不可避免地使你联想到势能。正如你将在第2.4节中看到的那样，这尤其严重的是因为“势”和“势能”之间存在有联系。我很抱歉无法避免使用这个词。我所能尽力而为的就是强调“势”和“势能”是完全不同的概念，它们应该有不同的术语。顺便说一句，电势相等的表面称为等势面（equipotential）。

（ii）势表示形式的优点。如果知道了 V，很容易求出 E —— 计算梯度： $E = -\nabla V$ 。当你停下来思考一下，这的确非同寻常，因为 E 是一个矢量（有三个分量），而 V 是一个标量（一个分量）。一个函数怎么可能包含三个独立函数的所具有信息呢？答案是 $\pmb{E}$ 的三个分量并不像看起来那么独立；事实上，它们通过从 $\nabla \times \pmb{E} = 0$ 开始的特定条件明确地相互关联着。以分量表述为

$$
\frac {\partial E _ {x}}{\partial y} = \frac {\partial E _ {y}}{\partial x}, \quad \frac {\partial E _ {z}}{\partial y} = \frac {\partial E _ {y}}{\partial z}, \quad \frac {\partial E _ {x}}{\partial z} = \frac {\partial E _ {z}}{\partial x}.
$$

这让我们回到了我在第 2.3.1 节开始时的评论：E 是一类非常特殊的矢量。势的表述充分展示了这个特殊性并将其优点发挥到极致，将矢量问题简化为标量问题，这样就不必对分量大惊小怪。

（iii）参考点 $\mathcal{O}$ 。由于参考点 $\mathcal{O}$ 的选择是任意的，因此势的定义在本质上就存在不确定性。改变参考点相当于在电势中增加一个常数 $K$ ：

$$
V ^ {\prime} (\boldsymbol {r}) \equiv - \int_ {\mathcal {O} ^ {\prime}} ^ {\boldsymbol {r}} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = - \int_ {\mathcal {O} ^ {\prime}} ^ {\mathcal {O}} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} - \int_ {\mathcal {O}} ^ {\boldsymbol {r}} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = K + V (\boldsymbol {r})
$$

其中 K 是 E 从原来的参考点 O 到新的参考点 $O'$ 的线积分。当然，因为 K 被抵消掉了，所以在 V 中加上一个常数不会影响两点之间的电势差：

$$
V ^ {\prime} (\boldsymbol {b}) - V ^ {\prime} (\boldsymbol {a}) = V (\boldsymbol {b}) - V (\boldsymbol {a})
$$

[实际上，从式（2.22）可以清楚地看出，电势差可以表示为 E 从点 a 到点 b 线积分，并不涉及 O 点，因此它与 O 无关。] 由于常数的导数始终为零，电势不确定性也不会影响 V 的梯度：

$$
\nabla V ^ {\prime} = \nabla V
$$

这就是为什么 V 在不同参考点下有不同的数值，却只对应着同一个电场强度 E。

势本身并不具有真正的物理意义，因为在任何给定的点上，我们都可以通过重新选择O点来随意调整其值。从这个意义上说，它很像海拔高度：如果我问你丹佛有多高，你可能会告诉我它的海拔高度，因为这是一个既实用又习惯的参考点。我们也同意去测量它高于华盛顿、格林尼治，或者其他任何地方的高度，这将从我们所得的以海平面为参考的读数中增加（或者更确切地说，减少）一个固定的值，但它对现实世界的任何东西都不会引起改变。唯一值得关注的量是两点之间的高度差，不管你的参考基准如何，差值都是一样的。

然而，话虽如此，类似于海平面的高度，人们常把距离电荷无穷远处的点选作为 $\mathcal{O}$ 点是一个很自然的约定。通常情况下，我们选择“在无限远处电势为零”。[由于 $V(\mathcal{O}) = 0$ ，选择一个参考点相当于选择这个地方的电势 $V$ 为零。]但是我必须提醒你，在一种特殊情况下这种约定是不成立的：也就是当电荷本身的分布扩展到无限远时。在这种情况下，所遇到的问题是电势会出现发散。例如，如在例题2.5中我们讨论的均匀带电平面的电场为 $(\sigma /2\varepsilon_0)\hat{n}$ ；如果我们天真地选择 $\mathcal{O} = \infty$ ，则平面上方高度为 $z$ 处的电势为

$$
V (z) = - \int_ {\infty} ^ {z} \frac {1}{2 \varepsilon_ {0}} \sigma \mathrm{d} z = - \frac {1}{2 \varepsilon_ {0}} \sigma (z - \infty)
$$

此时，解决的办法就是选择其他的参考点（在本例中，你可以选择平面上的一个点）。请注意，这样的难题仅会在课本的习题中出现；在“现实生活”中，不存在永远持续不断的电荷分布，我们总是可以选择无限远处作为参考点。

（iv）电势遵循叠加原理。原始的叠加原理适用于检验电荷 $Q$ 上所受的力。它指出 $Q$ 所受到的合力等于每个源点荷单独产生的力的矢量和：

$$
\boldsymbol {F} = \boldsymbol {F} _ {1} + \boldsymbol {F} _ {2} + \dots
$$

除以 $Q$ ，我们看到电场也遵循叠加原理：

$$
\pmb {E} = \pmb {E} _ {1} + \pmb {E} _ {2} + \dots
$$

从同一参考点到 $r$ 进行积分，可见，势也满足这样一个定则：

$$
V = V _ {1} + V _ {2} + \dots
$$

也就是说，任何给定点的电势等于所有源电荷单独产生的电势之和。只不过现在是普通的加法，而不是矢量和，这使得它使用起来更加方便。

（v）电势的单位。在我们的单位制中，力以牛顿（N）为单位，电荷以库仑（C）为单位，所以电场以牛顿每库仑（N/C）为单位。相应地，电势的单位是牛顿米每库仑（N·m/C），或者用焦耳每库仑（J/C）。1焦耳每库仑称为1伏特(V)。

图2.31

$$
\pmb {E} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r ^ {2}} \hat {\pmb {r}}
$$

$$
(r > R)
$$

$$
V (r) = - \int_ {\mathcal {O} ^ {\prime}} ^ {r} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = \frac {- 1}{4 \pi \varepsilon_ {0}} \int_ {\infty} ^ {r} \frac {q}{r ^ {\prime 2}} \mathrm{d} r ^ {\prime} = \frac {1}{4 \pi \varepsilon_ {0}} \left. \frac {q}{r ^ {\prime}} \right| _ {\infty} ^ {r} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r}
$$

$$
V (r) = \frac {- 1}{4 \pi \varepsilon_ {0}} \int_ {\infty} ^ {R} \frac {q}{r ^ {\prime 2}} \mathrm{d} r ^ {\prime} - \int_ {R} ^ {r} (0) \mathrm{d} r ^ {\prime} = \frac {1}{4 \pi \varepsilon_ {0}} \left. \frac {q}{r ^ {\prime}} \right| _ {\infty} ^ {R} + 0 = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{R}
$$

请注意，即使球壳内部的电场为零，但电势并不为零。 $V$ 在球壳内是一个常数，所以 $\nabla V = 0$ ——这是问题关键所在。在这类问题中，你必须始终从参考点开始；这里就是电势被确定的地方。人们很容易认为，仅仅根据球体内部电场就可以计算出那里的电势大小，但这往往是错误的：球体内的势对球外的电荷分布也非常敏感。如果我们在 $R' > R$ 处再放一个均匀带电球壳，即使是球 $R$ 内的电场仍然为零，但 $R$ 内的电势也会发生变化。只要它是球形或圆柱形对称的，高斯定理保证其外部某给定点的电荷（即在较大的 $r$ 处）对其内部的点不会产生净的电场；但对电势这样的结论不成立。

习题2.21 求半径为 $R$ 、所带总电荷为 $q$ 的均匀实心球体内外的电势，取无限远处电势为零。计算每个区间电势 $V$ 的梯度，并验证由它所得到的电场是否正确。画出 $V(r)$ 的草图。

习题2.22 求距离无限长直线为 $s$ 处的电势，已知无限长直线的线电荷密度为 $\lambda$ 。计算所得电势的梯度，并验证由此所得的电场是否正确。

习题2.23 对习题2.15中的电荷分布，取无限远处为参考点，求出中心处的势。

习题 2.24 对习题 2.16 中的电荷分布，求轴上一点和外圆柱上一点之间的电势差。请注意，如果使用式（2.22），则没有必要去指定一个特定的参考点。

## 2.3.3 泊松方程和拉普拉斯方程

我们在 2.3.1 节发现，电场可以写作标量势的梯度：

$$
\boldsymbol {E} = - \nabla V
$$

那么问题来了：就 $V$ 而言， $\pmb{E}$ 的散度和旋度是什么样子的，

$$
\nabla \cdot \pmb {E} = \frac {\rho}{\varepsilon_ {0}} \text {和} \nabla \times \pmb {E} = \mathbf {0}
$$

这很简单，既然 $\nabla \cdot \pmb{E} = \nabla \cdot (-\nabla V) = -\nabla^2 V$ ，所以，除了反复出现的负号外， $\pmb{E}$ 的散度可表示为 $V$ 的拉普拉斯算符。那么，高斯定理表述为

$$
\boxed {\nabla^ {2} V = \frac {\rho}{\varepsilon_ {0}}}\tag{2.24}
$$

这被称为泊松方程（Poisson's equation）。在没有电荷的区域内，即 $\rho = 0$ ，泊松方程简化为拉普拉斯方程（Laplace's equation）：

$$
\nabla^ {2} V = 0\tag{2.25}
$$

我们将在第 3 章中更全面地探讨这个方程。

高斯定理讨论到此为止。旋度定理如何呢？这就是说

$$
\nabla \times \boldsymbol {E} = \nabla \times (- \nabla V) = 0
$$

但这不是对 $V$ 的条件——梯度的旋度总是零。当然，我们是利用了旋度定理证明 $\pmb{E}$ 可以表示为标量的梯度，所以这并不奇怪： $\nabla \times \pmb{E} = 0$ 使得 $\pmb{E} = -\nabla V$ 有可能；反过来， $\pmb{E} = -\nabla V$ 保证了 $\nabla \times \pmb{E} = 0$ 。由于 $V$ 是标量，仅需一个方程（泊松方程）就可以确定 $V$ ，而对 $\pmb{E}$ 则需要两个，散度方程和旋度方程。

## 2.3.4 局域电荷分布的势

我根据 E 定义了 V[式（2.21）]。不过，通常情况下，我们需要求的物理量是 E（如果我们已知道 E，计算 V 就没有多大意义了）。具体想法是先得到 V，然后通过取梯度计算 E 可能会更容易。一般情况是我们知道电荷在哪里（即我们知道 $\rho$ ），我们想求出 V。现在，泊松方程将 V 和 $\rho$ 联系起来；遗憾的是，但这和实际情况完全弄反了：如果我们知道 V，可以求出 $\rho$ ，但我们知道是 $\rho$ ，想要求的是 V。那么，我们要做的是把泊松方程“倒过来”。这是这节要讲的内容，尽管我会采用一种迂回的方式来完成，一如既往地从位于原点的点电荷开始。

电场是 $\boldsymbol{E}=(1/4\pi\varepsilon_{0})(q/r^{2})\hat{\boldsymbol{r}}$ ，且 $dl=dr\hat{r}+rd\theta\hat{\theta}+r\sin\theta d\phi\hat{\phi}$ [式（1.68）]，因此

$$
\boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r ^ {2}} \mathrm{d} r
$$

取无限远处为参考点，位于原点的点电荷 q 的电势为

$$
V (r) = - \int_ {\mathcal {O}} ^ {r} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = \frac {- 1}{4 \pi \varepsilon_ {0}} \int_ {\infty} ^ {r} \frac {q}{r ^ {\prime 2}} \mathrm{d} r ^ {\prime} = \frac {1}{4 \pi \varepsilon_ {0}} \left. \frac {q}{r ^ {\prime}} \right| _ {\infty} ^ {r} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r}
$$

（你在这里看到了使用无限远作为参考点的优点：它消除了积分的下限。）注意 V 的符号：选择 V 的定义 [式（2.21）] 中约定的负号是为了保证正电荷的电势值为。正电荷区域是电势的 “山丘”，负电荷区域是电势的 “山谷”，电场由正到负指向 “下坡” 方向，记住这些是很有用的。

一般来说，点电荷 q 的电势为

$$
V (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{\nu}\tag{2.26}
$$

和以前一样， $\nu$ 是 q 到 r 的距离（图 2.32）。利用叠加原理，则点电荷集合的电势为

$$
V (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \sum_ {i = 1} ^ {n} \frac {q _ {i}}{r _ {i}}\tag{2.27}
$$

![](images/49dfda33edd36f3abcf3930daa74f573335b64f685e10bcd01c5a2640c4a7b52.jpg)  
图2.32

或者，对连续的电荷分布

$$
V (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {1}{2} \mathrm{d} q\tag{2.28}
$$

特别是，对体电荷分布有

$$
\boxed {V (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\rho (\boldsymbol {r} ^ {\prime})}{\imath} \mathrm{d} \tau^ {\prime}}\tag{2.29}
$$

这就是我们一直在寻找的方程，它告诉我们知道了 $\rho$ 时如何计算出 V，换句话说，这就是局域电荷分布泊松方程的“解” $^{7}$ 。将式（2.29）与相应的用 $\rho$ 表示的电场公式 [式（2.8）]

$$
\boldsymbol {E} (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\rho (\boldsymbol {r} ^ {\prime})}{r ^ {2}} \hat {\boldsymbol {r}} \mathrm{d} \tau^ {\prime}
$$

进行比较：需要留意的一点是，“讨厌”的单位矢量 $\hat{z}$ 没有了，所以你无须再为考虑分量而烦恼。线电荷和面电荷的电势分别是

$$
\frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\lambda \left(\boldsymbol {r} ^ {\prime}\right)}{n} \mathrm{d} l ^ {\prime} \text {和} \quad \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\sigma \left(\boldsymbol {r} ^ {\prime}\right)}{n} \mathrm{d} a ^ {\prime}\tag{2.30}
$$

我应该提醒你，本节中讨论的所有内容都是基于参考点位于无穷远假设的基础上的。这一点在式（2.29）中几乎不明显；但请记住，我们是从原点处点电荷势 $(1 / 4\pi \varepsilon_0)(q / r)$ 出发得该方程的，该方程仅在 $O = \infty$ 时成立。如果你试图将这些公式应用于电荷本身可以延伸到无限远处的人为的物理问题上，积分将会出现发散。

[解答] 这与我们在例题2.7中解决的问题相同，但现在我们使用式（2.30）来求解：

我们不妨把点 $P$ 设在 $z$ 轴上，用余弦定理表示 $\mathfrak{L}$

$$
r ^ {2} = R ^ {2} + z ^ {2} - 2 R z \cos \theta^ {\prime}
$$

球面上的面元为 $R^2\sin \theta '\mathrm{d}\theta '\mathrm{d}\phi '$ ，所以

$$
\begin{array}{r l} & {4 \pi \varepsilon_ {0} V (z) = \sigma \int \frac {R ^ {2} \sin \theta^ {\prime} \mathrm{d} \theta^ {\prime} \mathrm{d} \phi^ {\prime}}{\sqrt {R ^ {2} + z ^ {2} - 2 R z \cos \theta^ {\prime}}}} \\ & {\qquad = 2 \pi R ^ {2} \sigma \int_ {0} ^ {\pi} \frac {\sin \theta^ {\prime}}{\sqrt {R ^ {2} + z ^ {2} - 2 R z \cos \theta^ {\prime}}} \mathrm{d} \theta^ {\prime}} \\ & {\qquad = 2 \pi R ^ {2} \sigma \left. \left(\frac {1}{R z} \sqrt {R ^ {2} + z ^ {2} - 2 R z \cos \theta^ {\prime}}\right) \right| _ {0} ^ {\pi}} \\ & {\qquad = \frac {2 \pi R \sigma}{z} (\sqrt {R ^ {2} + z ^ {2} + 2 R z} - \sqrt {R ^ {2} + z ^ {2} - 2 R z})} \\ & {\qquad = \frac {2 \pi R \sigma}{z} [ \sqrt {(R + z) ^ {2}} - \sqrt {(R - z) ^ {2}} ]} \end{array}
$$

现在，我们必须非常小心地取正根。对球面外的点， $z > R$ ，所以 $\sqrt{(R - z)^2} = z - R$ ；对球面内的点， $\sqrt{(R - z)^2} = R - z$ 。因此

$V(z) = \frac{R\sigma}{2\varepsilon_0z} [(R + z) - (z - R)] = \frac{R^2\sigma}{\varepsilon_0z},$ 球外

$V(z) = \frac{R\sigma}{2\varepsilon_0z} [(R + z) - (R - z)] = \frac{R\sigma}{\varepsilon_0},$ 球内

如用 r 和球壳上的总电荷 $q = 4\pi R^{2}\sigma$ 表示，

$$
V (r) = \left\{ \begin{array}{l l} \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r} & (r \geqslant R) \\ \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{R} & (r \leqslant R) \end{array} \right.
$$

当然，在这种特殊情况下，使用式（2.21）会比使用式（2.30）更容易得到电势 $V$ ，因为利用高斯定理轻而易举地就求出了 $\pmb{E}$ 。但如果你将例题2.8和习题2.7比较，就能领悟到电势形式的优势。

习题2.25 利用式（2.27）和式（2.30），求图2.34中的电荷分布中心上方距离为 $z$ 处的电势。在每种情况下，计算 $E = -\nabla V$ ，并将你的结果分别与例题2.1、例题2.2和习题2.6做比较。假定在图2.34a中把右边的电荷换为 $-q$ ，则 $P$ 点的电势为多少？这暗示了它是什么样的电场？将你的结果与习题2.2做比较，并仔细解释任何差异。

![](images/a60c32dd6cb121ec4cfd9fbe20cc7a9b92352bce5edf7fc76e8fa5724919912e.jpg)  
a) 两个点电荷

![](images/b63ad3c06f0de344844239b4d9e5beb76e47dd114f8d435ff38963be54184d89.jpg)  
b) 均匀线电荷

![](images/38c44d83232a3981aa64381efea4f4bbd334e727f2c8020874125ddf9aeb421e.jpg)  
图2.34  
c)均匀面电荷

习题2.26 一圆锥形表面（一个空的冰淇淋蛋卷）带有均匀的表面电荷，电荷密度为 $\sigma$ ；圆锥体的高度是 $h$ ，顶部的半径也是 $h$ 。求点 $a$ （顶点）和点 $b$ （顶部中心）之间的电势差。

习题2.27 均匀带电实心圆柱体长度为 $L$ 、半径为 $R$ 、电荷密度为 $\rho$ ；求其轴上距中心为 $z$ 的点的电势。利用所得结果计算此点处的电场强度。（假设 $z > L / 2$ ）

习题2.28 利用式（2.29）计算半径为 $R$ 、总电荷为 $q$ 的均匀带电实心球体内的电势。将你的答案与习题2.21做比较。

习题2.29 应用拉普拉斯算符和式（1.102），验证式（2.29）满足泊松方程。

## 2.3.5 边界条件

典型的静电学问题中，我们往往是要求出给定源电荷分布 $\rho$ 所产生的电场强度 E。除非所讨论的问题具有对称性使得可以通过高斯定理求解，通常是先计算电势作为一个中间步骤会更利于求解。静电学的三个基本物理量是 $\rho$ 、E 和 V。在前面的讨论中，我们已经推导了与它们相关的所有六个公式。这些公式很简洁地总结在图 2.35 中。我们从两个实验观测开始：（1）叠加原理——一个对所有电磁力都成立的普遍定则，以及（2）库仑定律——静电学的基本规律。由此，其他的一切都随之而来。

![](images/dc73b067e009f554da624439f250a2767b70032854ad62c1e76f5e07a8099db4.jpg)  
图2.35

在学习例题 2.4 和 2.5，或者演算习题 2.7、2.11 和 2.16 时，你可能已经注意到当电场穿越一个面电荷为 $\sigma$ 的表面时，电场总是会出现不连续的变化。事实上，很容易就可以求出 E 在这样一个边界处的变化量。事实上，找到 E 在这样一个边界处的变化量是一件简单的事情。假定我们画出一个非常薄的高斯扁盒，上下两个方向刚好穿越出表面（图 2.36）。高斯定理指出

$$
\oint_ {S} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {a} = \frac {1}{\varepsilon_ {0}} Q _ {\mathrm{enc}} = \frac {1}{\varepsilon_ {0}} \sigma A ^ {\prime}
$$

式中，A 是扁盒盖子的面积。（如果表面上点与点之间 $\sigma$ 是变化的，或者表面是弯曲的，我们必须把 A 取得非常小。）此时，扁盒的侧面对电通量没有任何贡献，在扁盒厚度 $\varepsilon \rightarrow 0$ 的极限情况下，我们得到

$$
E _ {\mathrm{上方}} ^ {\perp} - E _ {\mathrm{下方}} ^ {\perp} = \frac {1}{\varepsilon_ {0}} \sigma\tag{2.31}
$$

式中， $E_{\perp}^{\perp}$ 表示垂直于正上方表面的 E 的分量， $E_{\perp}^{\perp}$ 的意义相同，只不过刚好指向表面下方。为了保持一致性，我们设“向上”都为两者的正方向。结论：E 的法线分量在任何边界上都有大小为 $\sigma/\varepsilon_{0}$ 的不连续。特别地，在没有表面电荷的情况下， $E^{\perp}$ 是连续的，例如在均匀带电的实心球体的表面。

![](images/274d60b8c068e7b25757d853d5eed18ab65bcf1c4c2ac42d3df50e3a183f31a5.jpg)  
图2.36

相比之下，E 的切线分量总是连续的。因为如果我们应用式（2.19），

$$
\oint \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = 0
$$

于图2.37所示的非常窄的长方形闭合路径，两端的路径对积分没有贡献（当 $\varepsilon \rightarrow 0$ 时），两边给出 $(E_{\text{上方}}^{\parallel}l - E_{\text{下方}}^{\parallel}l)$ ，所以

$$
E _ {\mathrm{上方}} ^ {\parallel} = E _ {\mathrm{下方}} ^ {\parallel}\tag{2.32}
$$

式中， $E^{\parallel}$ 表示 E 平行于表面的分量。E 的边界条件 [式（2.31）和式（2.32）] 可以合并为一个公式：

$$
\pmb {E} _ {\mathrm{上方}} - \pmb {E} _ {\mathrm{下方}} = \frac {\sigma}{\varepsilon_ {0}} \hat {\pmb {n}}\tag{2.33}
$$

式中， $\hat{n}$ 是垂直于表面的单位矢量，方向由“下”指向“上” $^{8}$ 。

![](images/06a0631b9cff84d023e643acfd650a28fb0f10da0886fffb5434a2676ddcd730.jpg)  
图2.37

同时，电势在任何边界上都是连续的（图 2.38），因为

$$
V _ {\text {上方}} - V _ {\text {下方}} = - \int_ {a} ^ {b} E \cdot \mathrm{d} l
$$

随着路径长度减少到零时，积分也减少到零：

$$
V _ {\text {上方}} = V _ {\text {下方}}\tag{2.34}
$$

然而， $V$ 的梯度延续了 $\pmb{E}$ 的不连续性；由于 $E = -\nabla V$ ，式（2.33）意味着

$$
\nabla V _ {\mathrm{上方}} - \nabla V _ {\mathrm{下方}} = - \frac {1}{\varepsilon_ {0}} \sigma \hat {\pmb {n}}\tag{2.35}
$$

或者更方便地

$$
\frac {\partial V _ {\mathrm{上方}}}{\partial n} - \frac {\partial V _ {\mathrm{下方}}}{\partial n} = - \frac {1}{\varepsilon_ {0}} \sigma\tag{2.36}
$$

其中

$$
\frac {\partial V}{\partial n} = \nabla V \cdot \hat {\pmb {n}}\tag{2.37}
$$

表示 V 的法向导数（normal derivative）（即在垂直于表面方向上的变化率）。

![](images/61c229aedbb2acf13db443f1f5393f5a80764911ac55fa3e595144b7c86f439a.jpg)  
图2.38

请注意，这些边界条件涉及表面正上方和正下方的电场和电势。例如，当我们从两侧接近表面时，式（2.36）导数是极限值。

习题2.30

(a) 验证例题 2.4、2.5 和习题 2.11 的结果与式（2.33）一致。

（b）利用高斯定理求出长空心圆柱管内外的电场，该圆柱管带有均匀的表面电荷密度 $\sigma$ 。验证所得结果是否与式（2.33）一致。

(c) 验证例题 2.8 的结果与边界条件式（2.34）和式（2.36）一致。

## 2.4 静电学中的功和能

## 2.4.1 移动电荷所需做的功

假定源电荷的位置分布是固定不变的，你想把一个检验电荷 $Q$ 从 $\pmb{a}$ 点移动到 $\pmb{b}$ 点（图2.39）。问题：你需要做多少功呢？在路径上的任何一点，作用在 $Q$ 上的电场力为 $\pmb {F} = QE$ ；你必须施加的力应是与这个力方向相反，即 $-QE$ 。（如果你被负号所困惑，设想你举起一块砖：重力向下施加力 $mg$ ，但你施加了一向上的力 $mg$ 。当然，你可以施加一个更大的力——这时砖将加速运动，你的部分气力将被“浪费”在产生砖的动能上。我们所感兴趣的是你必须施加的最小力来举起这块砖。）因此，你做的功是

$$
W = \int_ {a} ^ {b} \boldsymbol {F} \cdot \mathrm{d} \boldsymbol {l} = - Q \int_ {a} ^ {b} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = Q [ V (\boldsymbol {b}) - V (\boldsymbol {a}) ]
$$

请注意, 答案与你从 $a$ 点到 $b$ 点所选择的路径无关; 在力学中, 我们称静电力为 “保守力”。除以 $Q$ , 我们得到

$$
V (\boldsymbol {b}) - V (\boldsymbol {a}) = \frac {W}{Q}\tag{2.38}
$$

换句话说， $a$ 和 $b$ 点之间的电势差等于把单位电荷的粒子从 $a$ 点移动 $b$ 点所需做的功。特别是，如果你想把电荷 $Q$ 从无限远处移到 $r$ 处，你必须做的功是

$$
W = Q \left[ V (\boldsymbol {r}) - V (\infty) \right]
$$

若你取无穷远处为参考点，则

$$
W = Q V (\boldsymbol {r})\tag{2.39}
$$

从这个意义上讲，电势是单位电荷的势能（创建系统所需的功）（就像电场是单位电荷所受的力一样）。

![](images/0bf4fe2c4c5c98cb39afe36456e94d49b17e8e0aba319465f37e67c13224ede5.jpg)  
图2.39

## 2.4.2 点电荷分布的能量

若将一个点电荷集合体系聚集起来需要做多少功呢？想象一下，从无限远处一个接一个地把点电荷移到指定位置（图2.40）。引入第一个点电荷时无须做功，因为还没有可以克服的电场。当引入第二个电荷时，按照式（2.39），这需要做功 $q_{2}V_{1}(r_{2})$ ，其中 $V_{1}$ 是 $q_{1}$ 所产生的势， $r_{2}$ 是 $q_{2}$ 移动到的位置：

$$
W _ {2} = \frac {1}{4 \pi \varepsilon_ {0}} q _ {2} \left(\frac {q _ {1}}{n _ {1 2}}\right)
$$

![](images/45c82f0df8a4876ffac6e72fc87c5893e98de9d480c086209924f1b5724770fb.jpg)  
图2.40

$(r_{12} \text{ 是 } q_{1} \text{ 与 } q_{2} \text{ 移动后两者之间的距离。})$ 在引入每个电荷时，将其固定在一个不变的位置，这样在引入下一个电荷时它就不会移动。现在引入 $q_{3}$ ，所需做的功为 $q_{3} V_{1,2}(r_{3})$ ，其中 $V_{1,2}$ 是点电荷 $q_{1}$ 和 $q_{2}$ 所产生的电势，即 $(1/4\pi\varepsilon_{0})(q_{1}/r_{13} + q_{2}/r_{23})$ 。于是

$$
W _ {3} = \frac {1}{4 \pi \varepsilon_ {0}} q _ {3} \left(\frac {q _ {1}}{r _ {1 3}} + \frac {q _ {2}}{r _ {2 3}}\right)
$$

同样，引入第4个电荷额外所需做的功为

$$
W _ {4} = \frac {1}{4 \pi \varepsilon_ {0}} q _ {4} \left(\frac {q _ {1}}{r _ {1 4}} + \frac {q _ {2}}{r _ {2 4}} + \frac {q _ {3}}{r _ {3 4}}\right)
$$

构建这四个点电荷集合体系所需的总功为

$$
W = \frac {1}{4 \pi \varepsilon_ {0}} \left(\frac {q _ {1} q _ {2}}{r _ {1 2}} + \frac {q _ {1} q _ {3}}{r _ {1 3}} + \frac {q _ {1} q _ {4}}{r _ {1 4}} + \frac {q _ {2} q _ {3}}{r _ {2 3}} + \frac {q _ {2} q _ {4}}{r _ {2 4}} + \frac {q _ {3} q _ {4}}{r _ {3 4}}\right)
$$

你们可以看出其一般的规则：取每对电荷的乘积，除以它们之间的距离，然后求和：

$$
W = \frac {1}{4 \pi \varepsilon_ {0}} \sum_ {i = 1} ^ {n} \sum_ {j > i} ^ {n} \frac {q _ {i} q _ {j}}{n _ {i j}}\tag{2.40}
$$

j > i 的约定只是提醒你不要对一对电荷计算两次。实现这一点的一个更好方法是故意将每对电荷计算两次，然后除以 2:

$$
W = \frac {1}{8 \pi \varepsilon_ {0}} \sum_ {i = 1} ^ {n} \sum_ {j \neq i} ^ {n} \frac {q _ {i} q _ {j}}{n _ {i j}}\tag{2.41}
$$

（当然，我们需要避免 j = i 的情况。）请注意，在这个表达式中，由于每对电荷都出现在求和中，显然所得结果与你引入电荷的顺序无关。

最后，让我们提取出因子 $q_{i}$

$$
W = \frac {1}{2} \sum_ {i = 1} ^ {n} q _ {i} \left(\sum_ {j \neq i} ^ {n} \frac {1}{4 \pi \varepsilon_ {0}} \frac {q _ {j}}{r _ {i j}}\right)
$$

括号内的项是所有的其他点电荷在点 $r_i$ （ $q_i$ 所处位置）处产生的电势——电荷是指体系构建起来后所有的点电荷，而不是在构建过程中的某个阶段存在的电荷。因此，

$$
W = \frac {1}{2} \sum_ {i = 1} ^ {n} q _ {i} V (\boldsymbol {r} _ {i})\tag{2.42}
$$

这就是构建一个点电荷集合体系所需要做的功；这也是拆散这个点电荷集合体系你所能够获得的能量。与此同时，它代表了储存在这个体系中的能量（如果你愿意，可称之为“势”能，尽管出于显而易见的原因，我倾向于避免使用这个词）。

习题2.31

(a) 如图 2.41 所示，3 个电荷位于正方形（边长为 a）的三个顶角，把另外一个电荷 +q 从无限远处移到第 4 个顶角处需要做多少功？

(b) 构建这整个 4 点电荷集合体系需要做多少功?

![](images/9bbfa6a5fd2298efb3b7d7c9d7d5e2a6376bc99050cd503bd6609d694eb4b2d9.jpg)  
图2.41

习题2.32 两个带正电的点电荷 $q_{\mathrm{A}}$ 和 $q_{\mathrm{B}}$ （质量分别为 $m_{\mathrm{A}}$ 和 $m_{\mathrm{B}}$ ）处于静止状态，由一根长度为 $a$ 的轻线连接在一起。现把轻线剪断，粒子沿相反方向飞离。当它们相距甚远时，各自的速度是多少？

习题2.33 考虑一个沿 $x$ 轴由正负电荷（ $\pm q$ ）交替排列的点电荷链，每个点电荷与其最近邻点电荷相距为 $a$ 。求组成该体系中需要对每个粒子做的功。[部分答案：对于某个无量纲数 $\alpha, -\alpha q^2 / (4\pi\varepsilon_0 a)$ ，你的任务是确定 $\alpha$ 。它被称为马德隆常数（Madelung constant）。计算二维和三维点阵的马德隆常数要微妙得多，也更困难。]

## 2.4.3 连续电荷分布的能量

对于体电荷密度 $\rho$ ，式（2.42）变为

$$
W = \frac {1}{2} \int \rho V \mathrm{d} \tau\tag{2.43}
$$

（线电荷和面电荷的相应积分分别为 $\int \lambda V\mathrm{d}l$ 和 $\int \sigma V\mathrm{d}a_{\circ}$ ）有一个很漂亮的方法可以重写这个结果，其中 $\rho$ 和 $V$ 被消除，取而代之的是 $\pmb{E}$ 。首先，使用高斯定理将 $\rho$ 用 $\pmb{E}$ 来表示：

$$
\rho = \varepsilon_ {0} \nabla \cdot \pmb {E} \quad \text {所以} \quad W = \frac {\varepsilon_ {0}}{2} \int (\nabla \cdot \pmb {E}) V \mathrm{d} \tau
$$

现在利用分部积分将对 E 的求导转换为对 V 的求导：

$$
W = \frac {\varepsilon_ {0}}{2} \left[ - \int \boldsymbol {E} \cdot (\nabla V) \mathrm{d} \tau + \oint V \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {a} \right]
$$

然而 $\nabla V = -\pmb{E}$ ，所以

$$
W = \frac {\varepsilon_ {0}}{2} \left(\int_ {\mathcal {V}} E ^ {2} \mathrm{d} \tau + \oint_ {\mathcal {S}} V \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {a}\right)\tag{2.44}
$$

但我们对哪些体积进行积分？让我们回到开始出发的式（2.43）。从它的推导可以清楚地看出，我们应该在电荷所在的区域进行积分。但实际上，对任何更大的区域积分都是可以的，我们增加的“额外”区域对积分没有任何贡献，因为那里的 $\rho = 0$ 。考虑到这一点，我们回到式（2.44）。当我们把积分区域扩大到包含所有电荷区域以外时会发生什么？那么， $E^{2}$ 的积分只能增加（被积函数是正的）；显然，表面积分必须相应地减小，以保证总和保持不变。（事实上，在远离电荷的区域，E 按 $1/r^{2}$ 衰减，V 按 1/r 衰减，而面积按 $r^{2}$ 增加。所以粗略来讲，面积分按 1/r 减小。）请准确理解，无论你使用多大区域（只要包含所有的电荷）进行积分，式（2.44）给出正确的能量 W；但随积分区域的体积越来越大，体积分的贡献会增大，而面积分的贡献则会减小。特别是，为什么把积分区域扩大为整个空间呢？这样表面积分变为零，仅剩下

$$
\boxed {W = \frac {\varepsilon_ {0}}{2} \int_ {\text {整个空间}} E ^ {2} \mathrm{d} \tau}\tag{2.45}
$$

例题2.9 求总电荷量为 $q$ 、半径为 $R$ 的均匀带电球壳的能量。

解法 1：使用适用于表面电荷的式（2.43）:

$$
W = \frac {1}{2} \int \sigma V \mathrm{d} a
$$

此时，该球壳表面的电势是 $(1 / 4\pi \varepsilon_0)q / R$ （一个常数，见例题2.7），所以

$$
W = \frac {1}{8 \pi \varepsilon_ {0}} \frac {q}{R} \int \sigma \mathrm{d} a = \frac {1}{8 \pi \varepsilon_ {0}} \frac {q ^ {2}}{R}
$$

解法2：使用式（2.45）。在球内， $\pmb {E} = \mathbf{0}$ ；在球外

$$
\pmb {E} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r ^ {2}} \hat {\pmb {r}} \quad \mathrm{所以} \quad E ^ {2} = \frac {1}{(4 \pi \varepsilon_ {0}) ^ {2}} \frac {q ^ {2}}{r ^ {4}}
$$

$$
W _ {\mathrm{总}} = \frac {\varepsilon_ {0}}{2 (4 \pi \varepsilon_ {0}) ^ {2}} \int_ {\mathrm{球外空间}} \left(\frac {q ^ {2}}{r ^ {4}}\right) (r ^ {2} \sin \theta \mathrm{d} r \mathrm{d} \theta \mathrm{d} \phi)
$$

$$
= \frac {1}{3 2 \pi^ {2} \varepsilon_ {0}} q ^ {2} 4 \pi \int_ {R} ^ {\infty} \frac {1}{r ^ {2}} \mathrm{d} r = \frac {1}{8 \pi \varepsilon_ {0}} \frac {q ^ {2}}{R}
$$

习题2.34 用下列三种不同方法：求半径为 $R$ 、电荷为 $q$ 的均匀带电实心球体的能量。

(a) 利用式（2.43）和在习题 2.21 中求出的势。

(b) 利用式（2.45），别忘了对整个空间积分。

(c) 利用式（2.44），取一个半径为 $a$ 的球体。当 $a \to \infty$ 会发生什么。

习题2.35 这里是计算均匀带电实心球体能量的第四种方法：将其像雪球一样逐层构筑，每次从无穷远处移入无限小电荷 $\mathrm{d}q$ 并将其均匀地涂抹在表面上，从而使其半径增加。将半径增大 $\mathrm{d}r$ 需要多少功 $\mathrm{d}W$ ？对此进行积分，求构造出一个半径为 $R$ 、总电荷为 $q$ 的整个球体所需的功。

## 2.4.4 关于静电场能量的评注

（i）令人困惑的“矛盾”。式（2.45）清楚地表明静止电荷分布的能量总是正的。另一方面，式（2.42）[事实上式（2.45）是由此推导出的]可以是正或负的。例如，根据式（2.42），相距为 $\nu$ 的两个电量相等但符号相反电荷的能量为 $-(1 / 4\pi \varepsilon_0)(q^2 /\nu)$ 。问题出在哪里呢？哪个方程是正确的？

答案是两者都是正确的，但它们所讨论的问题略有不同。首先式（2.42）没有考虑放置点电荷所需要做的功；我们从点电荷开始，只是求出了将它们聚在一起所需的功。这是明智的选择，因为式（2.45）表明点电荷的能量实际上是无限大的：

$$
W = \frac {\varepsilon_ {0}}{2 (4 \pi \varepsilon_ {0}) ^ {2}} \int \left(\frac {q ^ {2}}{r ^ {4}}\right) (r ^ {2} \sin \theta \mathrm{d} r \mathrm{d} \theta \mathrm{d} \phi) = \frac {q ^ {2}}{8 \pi \varepsilon_ {0}} \int_ {0} ^ {\infty} \frac {1}{r ^ {2}} \mathrm{d} r = \infty
$$

在某种意义上，式（2.45）更加完善，因为它告诉你储存在点电荷体系中的总能量；但当你处理点电荷问题时，式（2.42）更合适；因为我们更希望（有充分理由！）忽略总能量中用于构筑点电荷体系本身所需的那部分能量。毕竟，实际中的点电荷（比如电子）是现成的；我们所做的只是移动它们。因为我们没有把它们靠在一起，也不把它们拆开，所以这个过程中涉及做多少功并不重要。（尽管如此，点电荷的无限能量仍然是电磁理论中反复出现的困境的来源，与经典电磁理论和量子电磁理论都相冲突，我们将在第11章中回到这个问题的讨论中。）

现在，你可能想知道这种“矛盾”是从哪里渗透到一个看似无懈可击的推导中的。“错误”出现在式（2.42）和式（2.43）之间：在前者中， $V(\boldsymbol{r}_{i})$ 表示除了电荷 $q_{i}$ 外其他所有电荷产生的电势，而在后者中， $V(\boldsymbol{r})$ 是全部电荷的电势。对于电荷的连续分布这里没有区别，因为 r 点的电荷量非常小，对电势的贡献为零。但对于点电荷，你最好使用式（2.42）。

（ii）能量储存在哪里？式（2.43）和式（2.45）提供了计算同一问题的两种不同方法。第一种是对电荷分布的积分；第二种是对电场的积分。这些积分可能涉及完全不同的区域。例如，在带电球壳的情况下（例题2.9），电荷被限制分布在表面上，而电场在表面外则无处不在。那么，能量存储在哪里？它是如式（2.45）所暗示的那样储存在电场中，还是如式（2.43）所暗示的一样存储在电荷中？在现阶段，这是一个无法回答的问题：我可以告诉你们总能量是多少，我也可以为你提供几种不同的计算方法，但担心能量储存在哪里有点不着边际。在辐射理论（第11章）的背景下，将能量视为储存在电场中是有用的（在广义相对论是必不可少的），能量密度为

$$
\frac {\varepsilon_ {0}}{2} E ^ {2} = \mathrm{每单位体积中的能量}\tag{2.46}
$$

但在静电学中，我们也可以说它储存在电荷中，能量密度为 $\frac{1}{2}\rho V$ 。这两种说法的差异纯粹是“记账法”的不同而已。

（iii）叠加原理。因为电场中的静电能是二次方的，所以它不遵循叠加原理。复合系统

的能量不是单独的各个部分的能量之和，也有“交叉项”存在：

$$
\begin{array}{r l} W _ {\mathrm{tot}} & = \frac {\varepsilon_ {0}}{2} \int E ^ {2} \mathrm{d} \tau = \frac {\varepsilon_ {0}}{2} \int (E _ {1} + E _ {2}) ^ {2} \mathrm{d} \tau \\ & = \frac {\varepsilon_ {0}}{2} \int (E _ {1} ^ {2} + E _ {2} ^ {2} + 2 E _ {1} \cdot E _ {2}) \mathrm{d} \tau \\ & = W _ {1} + W _ {2} + \varepsilon_ {0} \int E _ {1} \cdot E _ {2} \mathrm{d} \tau \end{array}\tag{2.47}
$$

例如，如果把每处的电荷加倍，总能就会翻两番。

习题2.36 考虑两个半径分别为 $a$ 和 $b$ 同心球壳。假设内壳带有电荷 $q$ ，外壳带有电荷 $-q$ （两者都均匀分布在球面上）。计算该体系的能量：（a）使用式（2.45），（b）利用式（2.47）和例题2.9的结果。

习题2.37 求相距为 $a$ 的两点电荷 $q_{1}$ 和 $q_{2}$ 的相互作用能[式（2.47）中的 $\varepsilon_0\int E_1\cdot E_2\mathrm{d}\tau$ 项]。[提示：将 $q_{1}$ 放在原点， $q_{2}$ 放在 $z$ 轴上；使用球坐标并首先对 $r$ 进行积分。]

## 2.5 导体

## 2.5.1 基本性质

在玻璃或橡胶等绝缘体（insulator）中，每个电子都被束缚在一个特定的原子上。相比之下，在金属导体（conductor）中，每个原子有一个或多个电子可以自由漫游。（在盐水等液体导体中，是离子在运动。）理想导体包含无限多的自由电荷。在现实生活中，不存在理想导体，但在大多数情况下认为金属是非常接近理想导体的。

根据这一定义，理想导体的基本静电特性如下：

（i）导体内部 E = 0。为什么？因为如果导体内部存在任何电场，那些自由电荷将会移动，也就不再是静电场了。这不是一个令人满意的解释；也许这只能证明，当导体存在时根本就没有静电场。我们最好研究一下当你把一个导体放入一个外场 $E_{0}$ 时会发生什么（图 2.42）。最初，电场会将正的自由电荷移向右边，将负的自由电荷移向左边。[实际上，是负电荷（电子）在移动，但当它们离开时，右侧就会留下一个净的正电荷（静止的原子核），所以说哪种电荷移动并不重要，其效果是一样的。] 当它们到达导体的边界时，电荷将会积累起来：右侧为正电荷，左侧为负电荷。这些感生电荷（induced charges）本身将会产生一个电场 $E_{1}$ ，如图所示。它的方向与 $E_{0}$ 相反。这是问题的要害，因为它意味着感生电荷的电场倾向于抵消原来的电场 $E_{0}$ 。电荷将持续移动直到完全抵消 $E_{0}$ ，其结果是导体内部的合电场为零 $^{9}$ 。整个电荷移动的过程几乎是瞬间完成的。

（ii）导体内部 $\rho = 0$ 。这是根据高斯定理得出的： $\nabla \cdot \mathbf{E} = \rho / \varepsilon_0$ 。如果 $\mathbf{E} = \mathbf{0}$ ，则 $\rho$ 也为零。当然导体内仍然有电荷，只是正电荷与负电荷一样多，所以导体内部的净电荷密度为零。

![](images/dccdf54479aa38ebb592145e455eb3dcf64c3583a455773c6c5f75bf2b2fc817.jpg)  
图2.42

（iii）净电荷都分布在表面上。这是唯一剩下的地方留给电荷待的位置。

（iv）导体是等势体。因为如果 a, b 是导体内给定的任意两点（或者是表面上的任意点）， $V(b) - V(a) = -\int_{a}^{b} E \cdot dl = 0$ ，因此 $V(a) = V(b)$ 。

（v）E 垂直于导体外表面。否则的话，如同（i）中的情况，电荷将会在表面周围运动，直到电场的切向分量为零（图 2.43）。（当然，在垂直于表面方向上由于电荷被限制在导体上，它不能流动。）

![](images/ec7cf857a3918544c6588cecb1c83efe934678b3d70a5f19a61bd8261c05780c.jpg)  
图2.43

我认为导体上的电荷流到表面是令人惊讶的。由于它们的相互排斥，它们尽可能地彼此远离，但将它们全部都转移到表面上似乎是对内部空间的浪费。当然，从尽可能彼此远离的角度来看，我们可以做得更好，把其中一些电荷分布在整个导体中。好吧，事实并非如此。无论导体的大小和形状如何，你最好把所有的电荷都放在表面上 $^{10}$ ，这才是正确的。

这个问题也可以用能量来表述。像其他任何无约束动力学系统一样，导体中的电荷也将寻求一个能使其势能最小的几何位置分布。性质（iii）断言当电荷分散在导体表面上时，导体（具有特定形状和总电荷）的静电能是最小的。例如，像我们在例题2.9所发现的那样，若电荷均匀分布在表面上，球体的静电能为 $(1 / 8\pi \varepsilon_0)(q^2 /R)$ ；但如果电荷是均匀分布在整个球体中，则它的能量更大，为 $(3/20\pi\varepsilon_{0})(q^{2}/R)$ （习题 2.34）。

## 2.5.2 感生电荷

如果你把电荷 +q 靠近一不带电的导体（图 2.44），两者会相互吸引。原因是 q 会将导体中的负电荷吸引到靠近自己的一侧，并将正电荷排斥到远离自己的一侧。（另一种思考方式是，导体内电荷以一种方式移动以消除导体内部点电荷 q 产生的电场，内部的电场必须为零。）由于负的感生电荷更靠近 q，因此存在净的吸引力。（在第 3 章中，我们将具体计算球形导体情况下该力大小。）

当我提到导体“内部”的场、电荷或电势时，我指的是导体的“肉”；如果导体中有一些空腔，并且在该空腔内放置了一些电荷，那么空腔中的电场将不会为零。但奇妙的是，空腔和其里面的电荷通过周围的导体与外界实现了静电屏蔽（图2.45）。没有外部电场能够穿透导体；它们在外表面被那里的感生电荷抵消。同样，对于所有导体外部的点，腔内电荷引起的电场被内表面上的感生电荷抵消。然而，导体外表面产生的补偿电荷有效地将 $q$ 的存在“传达”给了外界。腔壁上总的感生电荷与内部电荷大小相等且符号相反，这是因为如果我们用高斯面包围空腔，其高斯面上所有的点都在导体中（图2.45） $\oint E\cdot \mathrm{d}\pmb {a} = 0$ ，因此（根据高斯定律）高斯面包围的净电荷必须为零。因为 $Q_{\mathrm{enc}} = q + q_{\text{诱导}}$ ，所以 $q_{\text{诱导}} = -q$ 。因此，如果导体作为一个整体是电中性的，那么其外表面一定有 $+q$ 的电荷。

![](images/319466a1360cd6ea49f437455ca15fd8b054b19bddb653805bf93ece79ce0b22.jpg)  
图2.44

![](images/abb77643316440a440ffc987c74cea1e4d5108aa87ae78368d74763b8f8013da.jpg)  
图2.45

例题2.10 以原点为中心的不带电球形导体上雕刻出一个形状怪异的腔体（图2.46），空腔内某处有一个电荷 $q$ 。问题：球体外的电场是什么？

[解答] 乍一看，答案似乎取决于空腔的形状和腔内电荷的位置。但这是错误的：不管怎样，答案都是

$$
\pmb {E} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r ^ {2}} \hat {\pmb {r}}
$$

导体向我们掩盖了有关空腔性质的所有信息，仅透露了它所包含的总电荷。这怎么可能？电荷 +q 在腔壁上感应出相反的电荷 -q，该感生电荷的分布使得它在空腔外部任何一点产生的电场同 +q 所产生的电场相抵消。由于导体不带净电荷，这使得电荷 +q 在球体表面上均匀分布。（外表面电荷均匀分布是因为空腔内电荷 +q 的不对称的影响被内表面 -q 的不对称分布所抵消。）那么，对于球体外面的点，唯一剩下的就是均匀分布在外表面上 +q 所产生的电场。

![](images/976aaa218c70a3abc044fd78974750ca826bf110826656d9148c24aacb04236b.jpg)  
图2.46

你可能会想到, 这个论点在某个方面是可以质疑的: 实际上这里有三个场在起作用: $E_{q}$ 、 $E_{\text{内表面电荷}}$ 以及 $E_{\text{外表面电荷}}$ 。我们所知道的是在导体内部这三者之和为零, 但我声称前两个电场相互抵消, 而第三个单独为零。此外, 即使是前两个在导体内部各点相互抵消, 谁又能说它们在球外面的点也是相互抵消呢? 毕竟, 它们在空腔内的点是不能相消的。我现在无法给你一个完全令人满意的答案, 但至少有一点是正确的: 有一种方法可以将 $-q$ 分布在内表面上, 从而它可以抵消 $q$ 在外表面所有点处产生的电场。因为同样的空腔可能是由一个半径为 27 英里或光年的巨大球形导体雕刻而成的。在这种情况下, 导体外表面剩余电荷 $+q$ 太远, 无法产生一个显著的电场, 因此另外两个电场必须自己相互抵消。所以我们知道它们能做到这一点……但是我们确定它们会选择这样做吗? 也许对于很小的球体, 大自然更喜欢某些复杂的三个电场相消的方式。不, 正如我们将在第 3 章的唯一性定理中看到的, 静电学对其选择非常吝啬; 总是用一种选择方式——没有其他别的——令导体上的电荷分布使其内部电场为零。一旦确定一种可能的方法后, 原则上就没有其他替代方法。

如果被导电材料包围的腔体内本身没有电荷，那么腔体内的电场为零。对于任何电场线都必须开始于腔壁和终止于腔壁，起于正电荷止于负电荷（图2.47）。假设该电场线是闭合回路的一部分，其余下部分完全是在导体内部（这里 $E = 0$ ），积分 $\oint E \cdot dl$ 显然大于零，这就违反了式（2.19）。因此，在空洞内 $E = 0$ ，空腔表面实际上再也没有电荷存在。[这就是为什么在雷暴期间，你躲在金属轿车内相对安全的原因——如果遭雷击，你可能会被煮熟，但你不会触电。同样的原理也适用将敏感仪器设备放置在一个接地的法拉第笼（Faraday cage）内，以屏蔽外界杂散电场的干扰。在实践中，外壳甚至不必是实心导体——通常网状铁丝就足够了。]

![](images/5f06bf0418272415dc35b06cb07f534315f774fb295329390af38207aa18aa31.jpg)  
图2.47

习题2.38 半径为 $R$ 、带电荷量为 $q$ 的金属球被一厚的同心金属壳包围（金属壳内半径为 $a$ ，外半径为 $b$ ，如图2.48所示），球壳不带净电荷。

(a) 求 R, a, b 处的表面电荷密度 $\sigma$ 。

(b) 以无穷远为参考点，求中心处的电势。

（c）现在，球壳外表面接地线，接地将会流尽电荷并将其电势降至零（与无穷大时相同）。对于（a）和（b）中的答案有何变化？

习题2.39 在半径为 $R$ 的（中性）导体球体内挖两个两个半径分别为 $a$ 和 $b$ 的球形空腔（如图2.49所示），并分别在每个空腔的中心放置一个点电荷 $q_{a}$ 和 $q_{b}$ 。

(a) 求面电荷密度 $\sigma_{a}, \sigma_{b}$ 和 $\sigma_{R}$ 。

(b) 导体外面的电场是多少?

(c) 每个空腔内的电场是多少?

(d) $q_{a}$ 和 $q_{b}$ 受力各是多少？

(e) 如果将第 3 个电荷 $q_{c}$ 靠近导体，上面这些答案中哪一个会改变？

![](images/f582313f764a1faf7c9af4ca6fa81e5c324f07718a3b45bfc51722b011912867.jpg)  
图2.48

![](images/ae8e135494477a6184837ed59e69d0f889a4464f48c5a677c037c48cd56a01a4.jpg)  
图2.49

习题2.40

(a) 点电荷 q 位于不带电导体的空腔内（图 2.45）。q 受力一定为零吗？ $^{11}$

(b) 点电荷和周围不带电导体之间的力总是吸引力吗？ $^{12}$

## 2.5.3 表面电荷和导体受力

由于导体内部的电场为零，边界条件式（2.33）要求导体外部的电场为

$$
\pmb {E} = \frac {\sigma}{\varepsilon_ {0}} \hat {\pmb {n}}\tag{2.48}
$$

这与前面电场始终垂直于表面的结论相一致。从势的角度而言，式（2.36）给出

$$
\sigma = - \varepsilon_ {0} \frac {\partial V}{\partial n}\tag{2.49}
$$

如果你能确定 E 或 V，通过这些公式就能够计算导体上的表面电荷；我们将在下一章中经常用到它们。

在电场存在的情况下，表面电荷将受到力；单位面积的力 f 为 $\sigma E$ 。但是这里有一个问题，由于电场在表面电荷处是不连续的，那么我们应当使用哪个电场强度： $E_{上方}, E_{下方}$ ，或者两者之间的某个值？答案是，我们应该使用两者的平均值：

$$
\pmb {f} = \sigma \pmb {E} _ {\text {平均}} = \frac {1}{2} \sigma \left(\pmb {E} _ {\text {上方}} + \pmb {E} _ {\text {下方}}\right)\tag{2.50}
$$

为什么是平均值？理由很简单，尽管说起来很复杂。让我们把注意力集中在所讨论点周围的一小块面积上（图2.50）。（使其足够小，基本上是平的，其表面电荷密度基本上是恒定的。）总的电场由两部分组成——一部分是由这小块面积本身所带电荷的贡献，另一部分是来自其他方面的贡献（比如表面的其他区域，以及可能存在的外部源电荷等）：

$$
\pmb {E} = \pmb {E} _ {\text {小面}} + \pmb {E} _ {\text {其他}}
$$

![](images/3c1a151a4862927990fef36067a9ecf8726e6b48bc5aec5c7d1e98e54766ea86.jpg)  
图2.50

现在，这个小面积块自身不能对自己施加力，就像你站在一个篮子里，通过向上提提梁要把你自己举起一样。因此，作用在这小面积块上的力完全是由 $E_{\text{其他}}$ 引起的，并且没有不连续性（若我们移除这小块面积块，剩下的“孔”的电场是非常光滑的）。这种电场的不连续性完全是由小面积块上的电荷引起的，它在两侧都产生了一个指向远离表面的电场 $(\sigma / 2\varepsilon_0)$ 。所以，

$$
\begin{array}{r l} & {\pmb {E} _ {\text {上方}} = \pmb {E} _ {\text {其他}} + \frac {\sigma}{2 \varepsilon_ {0}} \hat {\pmb {n}}} \\ & {\pmb {E} _ {\text {下方}} = \pmb {E} _ {\text {其他}} - \frac {\sigma}{2 \varepsilon_ {0}} \hat {\pmb {n}}} \end{array}
$$

因此

$$
\pmb {E} _ {\mathrm{其他}} = \frac {1}{2} \left(\pmb {E} _ {\mathrm{上方}} + \pmb {E} _ {\mathrm{下方}}\right) = \pmb {E} _ {\mathrm{平均}}
$$

平均实际上只是一种消除小面积块本身对电场贡献的方法。

这个论断适用于任何情况的表面电荷分布；对于导体这种特殊情况下，导体内部电场为零，外部的电场为 $(\sigma/\varepsilon_{0})\hat{n}$ [式（2.48）]，因此平均值为 $(\sigma/2\varepsilon_{0})\hat{n}$ ，单位面积受力为

$$
\boldsymbol {f} = \frac {1}{2 \varepsilon_ {0}} \sigma^ {2} \hat {\boldsymbol {n}}\tag{2.51}
$$

这相当于作用在表面上一个向外静电压力（electrostatic pressure），无论 $\sigma$ 为正还是负，都倾向于把导体拉进电场。用表面外的电场表示该压力，

$$
P = \frac {\varepsilon_ {0}}{2} E ^ {2}\tag{2.52}
$$

习题2.41 两个大金属板（每个面积为 $A$ ）之间相距为 $d$ 。假设每个板都带电荷 $Q$ ，金属板上的静电压力是多少？

习题2.42 半径为 $R$ 的金属球带有总电荷 $Q$ 。北“半球”和南“半球”之间的斥力是多少？

## 2.5.4 电容

假定我们有两个导体，其中一个带电荷 +Q，另一个带电荷 -Q（图 2.51）。由于每个导体上的电势 V 都是常数，我们可以明确地给出它们之间的电势差：

$$
V = V _ {+} - V _ {-} = - \int_ {(-)} ^ {(+)} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l}
$$

我们不知道两个导体上的电荷是如何分布的，如果它们的形状很复杂，计算电场将是一个难以处理的事情，但我们确实知道：E 正比于 Q。因为 E 由库仑定律给出：

$$
\pmb {E} = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\rho}{r ^ {2}} \hat {\pmb {r}} \mathrm{d} \tau
$$

所以如果把 $\rho$ 加倍， $\pmb{E}$ 也加倍。[请稍等一下！我们怎么知道 $Q$ 加倍（- $Q$ 也同样）就会加倍 $\rho$ ？也许电荷会形成一个完全不同的分布状态，在某些地方 $\rho$ 将是原来的4倍，而另外一些地方仅有原来的一半，这样每个导体总电荷还是翻一倍。事实上，这种担忧是没有根据的——在任何地方， $Q$ 加倍都会使 $\rho$ 加倍；它不会带来电荷分布的变化。我们将在第三章对此给出证明；现在你只需相信我的论断就可以了。]

![](images/0bf482d50a93012c97e18832cc7c87180fdce616a5006c986df0813b9e25bded.jpg)

![](images/62134b886f6afe9dab9d0e874c6f562040ce48d9ba0a53f550982bf70e4867fb.jpg)  
图2.51

既然 E 正比于 Q，那么 V 也正比于 Q。比例常数称为该体系的电容（capacitance）：

$$
C \equiv \frac {Q}{V}\tag{2.53}
$$

电容是一个纯粹的几何量，由两个导体的尺寸、形状以及两者的间距决定。在国际单位制中，C 的单位是法拉（farads，F）；法拉为库仑每伏特。实际应用中，这个单位太大，很不方便使用；更实用的单位是微法（ $10^{-6}F$ ）和皮法（ $10^{-12}F$ ）。

请注意，根据其定义， $V$ 等于带正电导体的电势与带负电导体的电势之差；同样， $Q$ 是带正电的导体电荷值。因此，电容本质上是一个正值。[顺便说一句，你偶尔会听到有人谈论单个导体的电容。在这种情况下，带负电荷的“第二个导体”是包围这个导体的一个无限大半径的假想球壳。该无限大半径球壳对电场没有贡献，因此电容由式（2.53）给出，其中 $V$ 是以无限远处为参考点的电势。]

例题 2.11 求由相距为 d、面积为 A 的两个金属极板组成的平行板电容器（parallel-plate capacitor）的电容（图 2.52）。

图2.52

[解答] 如果极板的面积足够大，间距很小 $^{13}$ ，当我们把上极板带上电荷+Q，下极板带上电荷-Q时，电荷将均匀地分布在极板两个表面上。上极板表面电荷密度为 $\sigma = Q / A$ ，根据例题2.6的结果，电场强度为 $(1/\varepsilon_{0})Q / A$ 。所以，两板间的电势差是

$$
V = \frac {Q}{A \varepsilon_ {0}} d
$$

$$
C = \frac {A \varepsilon_ {0}}{d}\tag{2.54}
$$

例如，如果极板是边长为 $1\mathrm{cm}$ 的正方形，并且他们相距 $1\mathrm{mm}$ ，则电容为 $9 \times 10^{-13}\mathrm{F}$ 。

例题2.12 求内外半径分别为 $a$ 和 $b$ 的同心球形金属壳的电容。

[解答] 在内球壳放电荷 +Q，外球壳放电荷 -Q。两球壳之间的电场为

$$
E = \frac {1}{4 \pi \varepsilon_ {0}} \frac {Q}{r ^ {2}} \hat {r}
$$

所以，它们之间的电势差为

$$
V = - \int_ {b} ^ {a} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = - \frac {Q}{4 \pi \varepsilon_ {0}} \int_ {b} ^ {a} \frac {1}{r ^ {2}} \mathrm{d} r = \frac {Q}{4 \pi \varepsilon_ {0}} \left(\frac {1}{a} - \frac {1}{b}\right)
$$

正如之前所述， $V$ 与 $Q$ 成正比，电容为

$$
C = \frac {Q}{V} = 4 \pi \varepsilon_ {0} \frac {a b}{(b - a)}
$$

要给电容器 “充电”，你必须把正极板上的电子移动到负极板上。这样做需要克服电场的阻碍，因为电场将会使电子远离负极板并把它拉回到正极板上。那么，将电容充电至最终带电量为 Q 时需要做多少功？假设在该充电过程中的某个中间阶段，正极板上所带电荷为 q，此时的势差为 q/C。根据式（2.38），再移动电荷元 dq 到正极板上所需做的功为

$$
\mathrm{d} W = \left(\frac {q}{C}\right) \mathrm{d} q
$$

那么。从 $q = 0$ 到 $q = Q$ 所需的总功为

$$
W = \int_ {0} ^ {Q} \left(\frac {q}{C}\right) \mathrm{d} q = \frac {1}{2} \frac {Q ^ {2}}{C}
$$

或者，由于 $Q = CV$

$$
W = \frac {1}{2} C V ^ {2}\tag{2.55}
$$

其中 V 是电容器的电势差。

习题 2.43 求半径分别为 a 和 b 的两根同轴金属圆柱管的单位长度电容（图 2.53）。

![](images/8ef951a37f6333a1378d8706baff32cdb078ace8841d4a98c944461ffd4c441f.jpg)  
图2.53

习题 2.44 假设平板电容器的两极板由于相互吸引而以无穷小的距离 $\varepsilon$ 靠近。

（a）使用式（2.52）表示静电力做的功，已知电场 E 和板面积 A。

（b）使用式（2.46）表示在此过程中电场损失的能量。（这个问题应该很容易，但它包含了利用能量守恒对式（2.52）进行替代推导的雏形。）

## 第2章补充习题

习题2.45 求带有均匀面电荷密度 $\sigma$ 的正方形薄片（边长为 $a$ ）中心上方高度为 $z$ 处的电场。验证 $a \to \infty$ 和 $z \gg a$ 两种极限情况下的结果。 $\left[\text{答案: } (\sigma / 2\varepsilon_0) \left\{(4 / \pi) \arctan \sqrt{1 + (a^2 / 2z^2)} - 1\right\}\right]$

习题2.46 如果某个区域的电场（在球坐标系中）可由某个常数 $k$ 的表达式

$$
\boldsymbol {E} (\boldsymbol {r}) = \frac {k}{r} [ 3 \hat {\boldsymbol {r}} + 2 \sin \theta \cos \theta \sin \phi \hat {\pmb {\theta}} + \sin \theta \cos \phi \hat {\phi} ]
$$

给出，那么电荷密度是多少？[答案： $3k\varepsilon_0(1 + \cos 2\theta \sin \phi) / r^2]$

习题 2.47 求均匀带电固体球的南半球对北半球施加的净电力。用球的半径 R 和总电荷 Q 表示你的答案。[答案： $(1/4\pi\varepsilon_{0})(3Q^{2}/16R^{2})$ ]

习题2.48 半径为 $R$ 的倒置半球形碗分布有均匀的面电荷密度为 $\sigma$ 。求“北极”与中心之间的电势差。[答案： $(R\sigma / 2\varepsilon_0)(\sqrt{2} - 1)]$

习题2.49 半径为 $R$ 的球体分布有密度为 $\rho(r) = kr$ （其中 $k$ 是常数）的电荷。求该球体的能量。至少用两种不同的方法来验证你的答案。[答案： $\pi k^2 R^7 / 7\varepsilon_0]$

习题2.50 某种电荷分布产生的电势为

$$
V (\boldsymbol {r}) = A \frac {\mathrm{e} ^ {- \lambda r}}{r}
$$

其中 $A$ 与 $\lambda$ 为常数。求电场强度 $E(r)$ 、电荷密度 $\rho (r)$ ，以及总电荷 $Q$ 。[答案： $\rho = \varepsilon_0A(4\pi \delta^3 (r) - \lambda^2$ $\mathrm{e}^{-\lambda r} / r)]$

习题 2.51 求均匀带电圆盘（半径为 R，电荷密度为 $\sigma$ ）边缘的电势。[提示：首先证明 $V = k(\sigma R / \pi \varepsilon_{0})$ ，你可以把这里的无量纲数 k 用积分来表示。然后，通过分析来估算 k 值，或者有可能的话用计算机来计算它。]

!习题 2.52 两条平行于 x 轴的无限长导线分别具有均匀的线电荷密度 +λ 和 -λ（图 2.54）。

(a) 以坐标原点为参考点，求任意一点 $(x,y,z)$ 的电势。

（b）证明等势面是圆柱体，并确定对应于给定电势 $V_{0}$ 的圆柱体的轴线和半径。

!习题 2.53 在真空二极管中，电子在零电势下从热阴极（cathode）“蒸发”，并通过两极间的间隙加速到阳极（anode），阳极电势恒定为 $V_{0}$ 。在两极间移动的电子云（称为空间电荷，space charge）迅速积聚，使阴极表面的电场减小到零。从此，在两极板之间形成稳定的电流 I。假设极板相对于间距很大（ $A \gg d$ ，如图 2.55 所示），因此可以忽略边缘效应。那么 V, $\rho$ , v（电子速度）都仅是 x 的函数。

(a) 写出两板之间区域的泊松方程。

(b) 假设电子自阴极由静止开始运动，在电势为 $V(x)$ 的点 x 处电子速度是多少？

(c) 在稳态下， $I$ 与 $x$ 无关。那么， $\rho$ 和 $v$ 之间的关系是什么？

(d) 利用上述三个结果，通过消去 $\rho$ 和 v，得到 V 的微分方程。

(e) 求 $V$ 作为 $x, V_0, d$ 的函数的方程。画出 $V(x)$ 草图，并将其与没有空间电荷的电势情况进行比较。另外，求出 $\rho$ 和 $v$ 作为 $x$ 的函数。

## (f) 证明

$$
I = K V _ {0} ^ {3 / 2}\tag{2.56}
$$

并求出常数 $K$ 。[式（2.56）称为柴尔德-朗缪尔定律（Child-Langmuir Law）。只要空间电荷限制电流的情况下，它也适用于其他几何形状。请注意，空间电荷受限二极管是非线性的——它不遵守欧姆定律。]

![](images/deb7da770be107b2b855da66b84dc2928c3f2fbdd2e792475dccdb6125d6974c.jpg)  
图2.54

![](images/b3a28a5591bb7651a38bd7acc44a804e09ed09142ab538f88dbc18cb164f9f09.jpg)  
图2.55

!习题 2.54 想象一下，新的、非常精确的测量结果揭示了库仑定律的一个错误。发现两点电荷之间的实际相互作用力为

$$
\boldsymbol {F} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q _ {1} q _ {2}}{r ^ {2}} \left(1 + \frac {r}{\lambda}\right) \mathrm{e} ^ {- r / \lambda} \hat {\boldsymbol {z}}
$$

其中 $\lambda$ 是一个新的自然常数（显然，它具有长度量纲，并且是一个巨大的数字——比如说已知宇宙半径的一半——因此引起的修正很小，这就是为什么以前没有人注意到这种差异）。你的任务是依据这个新发现重新表述静电学。假定叠加原理仍然成立。

(a) 电荷分布为 $\rho$ 的电场是什么 [代替式（2.8）]?

(b) 这个电场允许标量势吗？简要解释一下你是如何得出结论的。（不需要正式的证明——仅需一个有说服力的论点。）

(c) 类似于式（2.26），求点电荷 $q$ 的电势。[如果你对（b）的答案是“否”，最好回过头来改正一下！]取 $\infty$ 作为参考点。

(d) 对位于原点的点电荷，证明

$$
\oint_ {\mathcal {S}} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {a} + \frac {1}{\lambda^ {2}} \int_ {\mathcal {V}} V \mathrm{d} \tau = \frac {1}{\varepsilon_ {0}} q
$$

其中 S 是以 q 为中心的任何球体的表面积，V 是体积。

(e) 证明：对任意的电荷分布。上面的结果推广为

$$
\oint_ {\mathcal {S}} \pmb {E} \cdot \mathrm{d} \pmb {a} + \frac {1}{\lambda^ {2}} \int_ {\mathcal {V}} V \mathrm{d} \tau = \frac {1}{\varepsilon_ {0}} Q _ {\mathrm{闭合面内}}
$$

（在新的“静电学”中，这是仅次于高斯定理的最好的东西。）

(f) 画出这个电磁世界的三角图（图2.35），填上所有适当的公式。[将泊松方程看成以 $V$ 表示 $\rho$ 的形式，将高斯定理（微分形式）看成以 $\pmb{E}$ 表示 $\rho$ 的形式。]

(g) 证明导体上的一部分电荷（均匀地！）分布在整个体积上，其余的分布在表面上。[提示：在导体内部，E仍然为零。]

习题2.55 假设电场 $\pmb {E}(x,y,z)$ 具有以下形式：

$$
E _ {x} = a x, \quad E _ {y} = 0, \quad E _ {z} = 0
$$

其中 $a$ 是常数。电荷密度是多少？当电荷密度均匀时，你如何解释电场指向一特定方向的事实？[这是一个比看起来更微妙的问题，值得仔细思考。]

习题2.56 所有的静电学都遵循库仑定律的 $1 / r^2$ 特性以及叠加原理。因此，可以为牛顿万有引力定律构建一个类似的理论。假设球体的密度是均匀的，质量为 $M$ 、半径为 $R$ 的球体的引力能是多少？使用你的结果估计太阳的引力能量（查找相关数据）。请注意，球体能量是负值——质量是相互吸引，而（类似）电荷是相互排斥的。当物质“落入”太阳时，它的能量被转化为其他形式的能（通常是热能），随后以辐射的形式释放出来。太阳的辐射功率是 $3.86 \times 10^{26} \mathrm{~W}$ ，如果所有辐射能都来自引力能，太阳能生存多久？[事实上，太阳的年龄要大得多，所以，很明显这不是它的能量来源[14]。]

!习题2.57 我们知道导体上的电荷会到达表面，但它在那里是如何分布的并不容易确定。一个可以明确计算表面电荷密度的著名例子是椭球体：

$$
\frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} + \frac {z ^ {2}}{c ^ {2}} = 1
$$

在这种情况下 $^{15}$

$$
\sigma = \frac {Q}{4 \pi a b c} \left(\frac {x ^ {2}}{a ^ {4}} + \frac {y ^ {2}}{b ^ {4}} + \frac {z ^ {2}}{c ^ {4}}\right) ^ {- 1 / 2}\tag{2.57}
$$

其中 $Q$ 为总电荷。选择适当的 $a, b, c$ 的值，求[由式（2.57）]：（a）半径为 $R$ 圆盘的净（两侧）表面电荷密度 $\sigma(r)$ ；（b） $xy$ 平面内横跨 $y$ 轴从 $x = -a$ 到 $x = a$ 的无限长导电“丝带”上的净表面电荷密度（设 $\Lambda$ 为“丝带”上单位长度的总电荷）；（c）求从 $x = -a$ 到 $x = a$ 的导电“针”上每单位长度的净电荷 $\lambda(x)$ 。在每种情况下，绘制结果草图。

## 习题2.58

（a）一等边三角形内接在半径为 $a$ 的圆上，每个顶点都放有点电荷 $q$ 。中心的电场（显然）为零，但（令人惊讶的是）三角形内还有其他三个点的电场也为零。他们分别在哪里？[答案： $r = 0.285a$ ，你可能需要用计算机计算才能得到它。]

（b）对于正 $n$ 边多边形，（除了中心）还有 $n$ 个点的电场为零 $^{16}$ 。对于 $n = 4$ 和 $n = 5$ 的情况，求出它们距中心的距离。当 $n = \infty$ 时，你认为会是什么样子的结果？

习题 2.59 证明或反驳（用反例）以下内容：

定理：假设有一带净电荷 $Q$ 的导体，将其放置在外电场 $\pmb{E}_{\mathrm{e}}$ 中时会受到力 $\pmb{F}$ ；若将外电场反转 $(E_{\mathrm{e}} \rightarrow -E_{\mathrm{e}})$ ，则受力也反转 $(F \rightarrow -F)$ 。

如果我们明确要求外场是均匀的，结果如何呢？

习题 2.60 点电荷 q 位于不带电的导体球壳的中心，球壳的内半径为 a，外半径为 b。问题：将电荷 q 移动到无穷远处（通过球壳上钻的小孔）需要多少功？[答案： $\left(q^{2}/8\pi\varepsilon_{0}\right)(1/a-1/b)$ 。]

习题 2.61 在半径为 R 的圆上或圆内放置 N 个相同的点电荷，体系的最小能量几何构型是什么 $^{17}$ ? 因为导体上的电荷会移至表面，你可能会认为 N 个点电荷会围绕圆周（均匀地）排列。证明（相反）对于 N = 12 的情况，在圆周上放置 11 个，在中心放置 1 个是最好的。对于 N = 11 情况又是如何（如果你把所有 11 个都放置在圆周上；或者你把 10 个放置在周长上，1 个放在中心位置，哪个能量会更低）？[提示：用数值表示结果——需要保留 4 位有效数字。将所有能量表示为 $q^{2}/4\pi\varepsilon_{0}R$ 的倍数。]

## 3.1 拉普拉斯方程

## 3.1.1 引言

静电学的主要任务是求出给定静态电荷分布的电场。原则上，这一目的可以通过诸如式(2.8)形式的库仑定律来实现：

$$
\pmb {E} \left(\pmb {r}\right) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\hat {\pmb {\nu}}}{\hat {\nu} ^ {2}} \rho \left(\pmb {r} ^ {\prime}\right) \mathrm{d} \tau^ {\prime}\tag{3.1}
$$

遗憾的是，除了一些最简单的电荷分布构型外，这种类型的积分都很难计算。偶尔我们可以通过利用对称性和高斯定理来解决这个问题，但通常最好的方案是首先计算电势 $V$ ，它由更易于处理的式(2.29)给出：

$$
V (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {1}{\eta} \rho (\boldsymbol {r} ^ {\prime}) \mathrm{d} \tau^ {\prime}\tag{3.2}
$$

尽管如此，即使是这样的一个积分也往往很难得到解析解。此外，在涉及导体的问题中，电荷密度 $\rho$ 本身可能无法事先知道：由于电荷可以自由运动，我们唯一直接控制的是每个导体的总电荷（或电势）。

在这种情况下，使用泊松方程 [式 (2.24)] 重新把这个问题表述成微分形式是富有成效的：

$$
\nabla^ {2} V = - \frac {1}{\varepsilon_ {0}} \rho\tag{3.3}
$$

该方程加上适当的边界条件等价于式(3.2)。事实上，通常我们仅对求 $\rho = 0$ 区域的电势感兴趣。（当然，如果处处 $\rho = 0$ ，则 $V = 0$ ，也就无话可言了——我并不是这个意思。在其他地方可能存在大量的电荷，但我们更关心的是这些没有电荷的区域。）在这种情况下，泊松方程简化为拉普拉斯方程：

$$
\nabla^ {2} V = 0\tag{3.4}
$$

或者，用直角坐标系写出

$$
\frac {\partial^ {2} V}{\partial x ^ {2}} + \frac {\partial^ {2} V}{\partial y ^ {2}} + \frac {\partial^ {2} V}{\partial z ^ {2}} = 0\tag{3.5}
$$

该方程对静电学是如此的基础，以至于人们几乎可以讲静电学就是研究拉普拉斯方程的。同时，它是一个十分普遍存在的方程，常出现在引力、磁学、热理论等不同的物理学分支中。在数学中，拉普拉斯方程在解析函数论中起着重要作用。为了了解拉普拉斯方程及其解（称为调和函数，harmonic functions），我们将从更易于描述的一维和二维情况入手，并阐明三维情况的所有基本性质。

## 3.1.2 一维拉普拉斯方程

假设 V 仅和变量有关。那么拉普拉斯方程变为

$$
\frac {\mathrm{d} ^ {2} V}{\mathrm{d} x ^ {2}} = 0
$$

它的通解是

$$
V (x) = m x + b\tag{3.6}
$$

是一条直线。由于是一个二阶（普通）微分方程，它包含满足二阶（常）微分方程的两个待定常数（m 和 b）。在某种特定情况下，他们由问题所给的边界条件决定。可以具体地说，在 x=1 处 V=4，以及在 x=5 处 V=0。在这种情况下，m=-1, b=5；因此 $V=-x+5$ （图 3.1）。

![](images/641ae88a8e655a00702aadf02d2235781ab2c5ff78465f65b6ba588604cdb3c2.jpg)  
图3.1

我想提醒你注意这一结果的两个特点：在一维情况下，它们可能看起来很普通和显而易见，我可以明确地写出通解；但在二维和三维情况下，同样的事情就变得非常有用，且绝非再显而易见。

1. 对于任意 $a, V(x)$ 是 $V(x + a)$ 和 $V(x - a)$ 的平均值：

$$
V (x) = \frac {1}{2} \left[ V (x + a) + V (x - a) \right]
$$

拉普拉斯方程是一种求平均值的操作或指令：它告诉你把 $x$ 左边和右边点的平均值赋予点 $x$ 。从这个意义上说，求解拉普拉斯方程和拟合正确的边界数值是非常无聊的事情。

2. 拉普拉斯方程不允许存在局域的极大值和极小值： $V$ 的极值必须出现在端点处。实际上，这是（1）的结果，因为如果存在一个局域极大值点， $V$ 在该点的值将比两边的都大，因此它不可能由两边的值平均得到。（通常，你所预期在极大值处的二阶导数为负，极小值处的二阶导数为正。相反，由于拉普拉斯方程要求二阶导数为零，因此拉普拉斯方程的解不应有极值似乎是合理的。然而，这并不是一个证明，因为有的函数在其极大值或极小值处的二阶导数为零。例如，函数 $x^{4}$ 在 $x = 0$ 具有极小值且此处二阶导数为零。）

## 3.1.3 二维拉普拉斯方程

如果 $V$ 依赖两个变量，拉普拉斯方程为

$$
\frac {\partial^ {2} V}{\partial x ^ {2}} + \frac {\partial^ {2} V}{\partial y ^ {2}} = 0
$$

这不再是一个常微分方程（即仅是一般导数方程）；这是一个偏微分方程。这样一来，你可能熟悉的一些简单规则就不适用了。例如，这个方程的通解包含不止两个待定常数——同样也不包含任何有限数目的常数——尽管它是一个二阶方程。事实上，我们无法写出“通解”[至少，不是像式(3.6)那样的封闭形式解]。然而，仍然可以推断出所有解的某些共同性质。

记住一个物理例子可能会有所帮助。想象将一张薄薄的橡胶膜（或肥皂膜）拉伸展开在某些支撑物上。为了明确起见，假设你拿一个纸板箱，沿四周剪出一条波浪线，然后把切下的顶部去掉（图3.2）。现在，在盒子上粘上一层绷紧的橡胶膜，使其看起来像鼓头（当然，除非你选择把边缘切掉，否则它不会是鼓头）。此刻如果你标定盒子的底部为 $(x, y)$ 坐标平面，那么点 $(x, y)$ 上方的橡胶膜的高度 $V(x, y)$ 将满足拉普拉斯方程1。（一维情况是在两点之间拉伸的橡皮筋。当然，这将形成一条直线。）

![](images/4dcbc04a1ba60584ca5e251681ede5d28ac6978ac1a5b2909cd7c4db9724111d.jpg)  
图3.2

二维情况下的调和函数具有的性质和前面所提到的一维情况相同：

$$
\frac {\partial}{\partial x} \left(g \frac {\partial V}{\partial x}\right) + \frac {\partial}{\partial y} \left(g \frac {\partial V}{\partial y}\right) = 0, \quad \text {其中} g = \left[ 1 + \left(\frac {\partial V}{\partial x}\right) ^ {2} + \left(\frac {\partial V}{\partial y}\right) ^ {2} \right] ^ {- 1 / 2}
$$

1. 点处 $V$ 的数值是该点周围各点的平均值。更精确地说，如果你围绕点 $(x, y)$ 画一个半径为 $R$ 的圆，圆周上的平均值等于圆心处的值：

$$
V (x, y) = \frac {1}{2 \pi R} \oint_ {\mathrm{圆周线}} V \mathrm{d} l
$$

[顺便说一句，这是计算机求解拉普拉斯方程所基于的弛豫方法（method of relaxation）：从边界处 $V$ 的某特定值开始，并对内部网格上的点的 $V$ 值进行合理猜测；第一步，将每个点最近邻点的平均值重新赋予该点。第二步，使用校正后的值，重复这个过程，依此类推。经过几次迭代，数值开始收敛下来，后续的迭代产生的变化可以忽略不计，这样就得到了给定边界值的拉普拉斯方程的数值解²。]

2. $V$ 没有局域极大值和极小值，所有极值都出现在边界处。[如前所述，这是由（1）导出的。]同样，拉普拉斯方程选择了与边界条件一致的最无特征的函数：无丘无谷，只有最平滑的面。例如，如果你把一个乒乓球放在图3.2所示的绷紧的橡胶膜上，它会滚到一边并脱落——它不会在某个地方找到一个“口袋”稳定在那里；因为拉普拉斯方程不允许表面上有这样的凹痕存在。从几何的角度来看，正如两点之间的直线距离最短一样，二维调和函数使跨越给定边界线的表面积最小化。

## 3.1.4 三维拉普拉斯方程

在三维空间中，我既不能为你提供一个确定的解（如一维情况那样），也无法提供一个具有启发的物理例子来引导你的想象（如二维情况那样）。然而，这两个性质仍然成立，这次我将给出一个简单的证明 $^{3}$ 。

1. r 点处的 V 值是以 r 为中心的半径为 R 的球面上所有的 V 的平均值：

$$
V (\pmb {r}) = \frac {1}{4 \pi R ^ {2}} \oint_ {\mathrm{球面}} V \mathrm{d} a
$$

2. 因此， $V$ 不能有局域的极大值或极小值； $V$ 的极值必须出现在边界处。（因为如果 $V$ 在某个 $\pmb{r}$ 处有一个局域极大值，那么根据最大值的性质，我可以以 $\pmb{r}$ 为圆心画一个球面，球面上所有的 $V$ 值，尤其是平均值，都小于 $\pmb{r}$ 处的值。）

证明：让我们从计算半径为 R 的球面上的平均电势开始，该电势是位于球面外的单个点电荷 q 产生的。我们也可以将球体位于原点处，并选择坐标系使 q 位于 z 轴上（图 3.3）。

表面上某点的电势为

$$
V = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r}
$$

其中

$$
r ^ {2} = z ^ {2} + R ^ {2} - 2 z R \cos \theta
$$

所以

$$
\begin{array}{r l} & {V _ {\text {平均}} = \frac {1}{4 \pi R ^ {2}} \frac {q}{4 \pi \varepsilon_ {0}} \int \left[ z ^ {2} + R ^ {2} - 2 z R \cos \theta \right] ^ {- 1 / 2} R ^ {2} \sin \theta \mathrm{d} \theta \mathrm{d} \phi} \\ & {\quad = \frac {q}{4 \pi \varepsilon_ {0}} \frac {1}{2 z R} \sqrt {z ^ {2} + R ^ {2} - 2 z R \cos \theta} \Big | _ {0} ^ {\pi}} \\ & {\quad = \frac {q}{4 \pi \varepsilon_ {0}} \frac {1}{2 z R} [ (z + R) - (z - R) ] = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{z}} \end{array}
$$

然而这正是点电荷位于球心处产生的电势！根据叠加原理，对球体外的任何点电荷集合都应是如此：它们在球面上的平均电势等于它们在球中心处产生的净电势。证毕。

![](images/62ad4ab7d46a173e5231476be8100b626932855a04a54ce6dab64cc1dc803e19.jpg)  
图3.3

习题 3.1 求半径为 R 的球内一点电荷在球面上产生的电势的平均值（如同前面一样计算，只不过现在 z < R）。(当然，在这种情况下，拉普拉斯方程在球内不成立。)证明，一般情况下有

$$
V _ {\mathrm{平均}} = V _ {\mathrm{球心}} + \frac {Q _ {\mathrm{enc}}}{4 \pi \varepsilon_ {0} R}
$$

其中 $V_{球心}$ 是所有球外部电荷在球心处所产生的电势， $Q_{enc}$ 是球面所包围的总电荷。

习题3.2 用一句话来证明恩肖定理（Earnshaw's Theorem）：一个带电粒子不能仅由静电力保持稳定的平衡。例如，考虑图3.4中固定电荷在立方体顶角的排列。因为来自每个顶角的斥力，看起来位于中心的正电荷会悬浮在半空中。这个“静电瓶”的漏洞在哪里？[为了将核聚变作为一种能实际利用的能源，有必要将等离子体（雾化带电粒子）加热到极高的温度——以至于任何普通坩埚与之接触就会被蒸发。恩肖定理指出，静电约束也不能解决问题。幸运的是，可以利用磁场来约束热等离子体。]

![](images/5483db69de750c711c2159f65f5f53b78abd74253e911d7d0b63b1c2eeb3bd23.jpg)  
图3.4

习题3.3 对 $V$ 仅与 $r$ 有关的情况，在球坐标系中求拉普拉斯方程的通解。假定 $V$ 仅依赖于 $s$ ，在柱坐标系中做同样求解。

习题3.4

（a）证明：电荷位于球体外部和位于球体中心在球表面产生的平均电场相同。

(b) 球体内部电荷所产生的电场平均值是多少?

## 3.1.5 边界条件和唯一性定理

拉普拉斯方程本身并不能确定 $V$ ；除此之外，还必须给定适当的边界条件。这就提出了一个棘手的问题：什么是适当的边界条件，它足以确定方程的解，但又不至于多到引起前后不一致？一维情况很容易，因为通解 $V = mx + b$ 包含两个待定常数，因此我们需要两个边界条件。例如，我们可以给定两个端点函数的值；或者我们可以在一个端点给定函数的值和其导数值；或者在一个端点给定函数值，在另一端点给定其导数值，以此类推。但仅给定一个端点的函数值，或者仅其导数值是不行的——所给条件是不充分的。仅指定两端的导数也是有问题的——这要么是多余的（如果两者相等），要么自相矛盾（如果两者不相等）。

在二维和三维的情况下，我们面对的是偏微分方程，并不十分清楚什么样的边界条件是令人满意的。例如，绷紧橡胶膜的形状是由它被拉伸的框架唯一确定的，还是像罐头盖一样，可以从一种稳定构型变为另一种？正如你的直觉所暗示的那样，答案为 V 是唯一地由其边界值所决定的（灌装瓶显然不遵从拉普拉斯方程）。然而，也可以使用其他边界条件（见习题 3.5）。证明一组适当的边界条件是否充分通常以唯一性定理（uniqueness theorem）的形式给出。静电学中有很多这样的定理，它们都有相同的基本形式——我将给你展示两个最有用的定理 $^{4}$ 。

第一唯一性定理（First uniqueness theorem）：在某个体积 V 内，拉普拉斯方程的解由电势 V 在该区域边界面 S 上的值所唯一确定。

证明：在图 3.5 中，我绘制了这样一个区域及其边界。（只要电势的值在它们的所有表面上都确定，在内部也可以有“孤岛”存在；此外，外边界可以是无限远处，那里的电势通常取为零。）假定存在两个拉普拉斯方程的解：

$$
\nabla^ {2} V _ {1} = 0, \quad \nabla^ {2} V _ {2} = 0
$$

两者都假定表面上存在确定的值。我要证明它们必须相等。技巧是考虑它们的差

$$
V _ {3} \equiv V _ {1} - V _ {2}
$$

它也满足拉普拉斯方程

$$
\nabla^ {2} V _ {3} = \nabla^ {2} V _ {1} - \nabla^ {2} V _ {2} = 0
$$

而且 $V_{3}$ 在所有边界上为零（因为 $V_{1}$ 和 $V_{2}$ 在边界上相同）。但拉普拉斯方程不允许存在局域的最大值和最小值——所有极值都出现在边界上。所以 $V_{3}$ 的最大值和最小值均为零。因此， $V_{3}$ 必须处处为零，这样有

$$
V _ {1} = V _ {2}
$$

证毕。

![](images/e42dba1926133376a5251883c4d78fc9c89be2d793f9ffde2928f06a55b60ba5.jpg)  
图3.5

例题 3.1 证明：在导体所包围空腔中，只要腔内没有电荷存在，则电势是个恒定值。

[解答] 空腔壁上的电势是个定值 $V_0$ [见 2.5.1 节（iv）], 因此, 空腔内的电势是一个满足拉普拉斯方程的函数, 并且在边界上具有定值 $V_0$ 。很容易给出空腔内的一个解是: 处处 $V = V_0$ 。唯一性定理保证了这是唯一的解。(由此, 空腔内的电场为零——基于截然不同的理由, 我们在 2.5.2 节曾得到同样的结果。)

唯一性定理赋予我们更多的想象：你用什么方法得到解都无关紧要；如果（a）它满足拉普拉斯方程，并且（b）它在边界上有正确的值，那么它就是对的。当我们学习镜像法时，你将会看到这一论点的威力所在。

顺便提一下，很容易改进第一唯一性定理：我曾假定在所研究的区域内没有电荷存在，所以电势满足拉普拉斯方程，但是我们也可以放入一些电荷（此时 V 满足泊松方程）。理由是一样的，只是这次

$$
\nabla^ {2} V _ {1} = - \frac {\rho}{\varepsilon_ {0}}, \nabla^ {2} V _ {2} = - \frac {\rho}{\varepsilon_ {0}}
$$

所以，

$$
\nabla^ {2} V _ {3} = \nabla^ {2} V _ {1} - \nabla^ {2} V _ {2} = - \frac {\rho}{\varepsilon_ {0}} + \frac {\rho}{\varepsilon_ {0}} = 0
$$

电势差（ $V_{3} \equiv V_{1} - V_{2}$ ）依然满足拉普拉斯方程，并且在所有边界上为零。所以 $V_{3} = 0$ ，因此有 $V_{1} = V_{2}$ 。

推论：如果（a）整个体积的电荷密度和（b）所有的边界上的 V 都已明确指定，则体积 V 内的电势是唯一确定的。

## 3.1.6 导体和第二唯一性定理

静电学问题设置边界条件的最简单方法是给出所关注区域周围所有表面上的电势 V 值。这种情况在实践中经常发生：在实验室里，我们将导体连接到电池上，使导体保持有一定的电势，或者将其接地（ground），这是实验工作者对 V = 0 的表述。但是，在其他的一些情况下，我们并不知道边界处的电势值，而只是知道各种各样的导体表面上的电荷。假定我把电荷 $Q_{a}$ 放在第一个导体上， $Q_{b}$ 放在第二个导体上，以此类推——我无法告诉你电荷是如何在每个导体表面分布的，因为一旦我把它放置在导体上，它就会以一种我无法控制的方式运动。除此之外，假定导体之间的区域存在给定的电荷密度 $\rho$ 。电场现在是唯一确定的吗？或者，电荷能以多种不同的方式排列在各自的导体上，每种方式都会形成不同的电场？

第二唯一性定理（Second uniqueness theorem）：设在由导体包围并且给定电荷密度 $\rho$ 分布的区域 V 中，若给定每个导体上的总电荷，则电场是唯一确定的（图 3.6）。（该区域作为一个整体可以由另一个导体界定，也可以是无界的。）

![](images/8deb357a88872266cbe06526eab1097d410240068065f1894aceb16f83541eeb.jpg)  
图3.6

证明：假定有两个电场满足所给问题的条件。在两个导体之间的空间中，两者都满足微分形式的高斯定理：

$$
\nabla \cdot \pmb {E} _ {1} = \frac {1}{\varepsilon_ {0}} \rho , \nabla \cdot \pmb {E} _ {2} = \frac {1}{\varepsilon_ {0}} \rho
$$

对于包围每个导体的高斯曲面，两者都满足积分形式的高斯定理：

$$
\oint_ {\text {第} i \text {个导体面}} \boldsymbol {E} _ {1} \cdot \mathrm{d} \boldsymbol {a} = \frac {1}{\varepsilon_ {0}} Q _ {i}, \quad \oint_ {\text {第} i \text {个导体面}} \boldsymbol {E} _ {2} \cdot \mathrm{d} \boldsymbol {a} = \frac {1}{\varepsilon_ {0}} Q _ {i}
$$

同样，对于外部边界（无论是在封闭导体内部还是在无穷远处），

$$
\oint_ {\text {外部边界}} \boldsymbol {E} _ {1} \cdot \mathrm{d} \boldsymbol {a} = \frac {1}{\varepsilon_ {0}} Q _ {\text {总}}, \quad \oint_ {\text {外部边界}} \boldsymbol {E} _ {2} \cdot \mathrm{d} \boldsymbol {a} = \frac {1}{\varepsilon_ {0}} Q _ {\text {总}}
$$

如前所述，我们考虑两个电场之差

$$
\pmb {E} _ {3} \equiv \pmb {E} _ {1} - \pmb {E} _ {2}
$$

在导体之间的区域中，同时也满足

$$
\nabla \cdot \boldsymbol {E} _ {3} = 0\tag{3.7}
$$

并且在每个边界表面上满足

$$
\oint \boldsymbol {E} _ {3} \cdot \mathrm{d} \boldsymbol {a} = 0\tag{3.8}
$$

现在，我们必须利用最后一条信息：虽然我们不知道电荷 $Q_{i}$ 在第 $i$ 个导体上是如何分布的，但我们却知道每个导体都是等势体，因此电势 $V_{3}$ 在每个导体表面都是一恒量（不一定是相同的常量）。（它不一定是零，因为 $V_{1}$ 和 $V_{2}$ 可能不相等——我们唯一确定的是，在任何导体上，两者都是常量。）接下来用一个技巧。利用（前环衬）乘积法则第（5）条，我们有

$$
\nabla \cdot (V _ {3} \pmb {E} _ {3}) = V _ {3} (\nabla \cdot \pmb {E} _ {3}) + \pmb {E} _ {3} \cdot (\nabla V _ {3}) = - (E _ {3}) ^ {2}
$$

这里我使用了式(3.7)和 $E_{3}=-\nabla V_{3}$ 。对整个体积进行积分，并将散度定理应用于左侧：

$$
\int_ {\mathcal {V}} \nabla \cdot (V _ {3} \pmb {E} _ {3}) \mathrm{d} \tau = \oint_ {\mathcal {S}} V _ {3} \pmb {E} _ {3} \cdot \mathrm{d} \pmb {a} = - \int_ {\mathcal {V}} (E _ {3}) ^ {2} \mathrm{d} \tau
$$

表面积分包含所讨论区域的所有边界面——导体面和外边界面。 $V_{3}$ 在每个表面上都是常量（若外边界面为无穷大，则 $V_{3}=0$ ），因此，按照式 (3.8)， $V_{3}$ 可以提到积分号外，而剩下的部分积分都为零。因此有

$$
\int_ {\mathcal {V}} (E _ {3}) ^ {2} \mathrm{d} \tau = 0
$$

但这个被积函数永远不会为负值；唯一的可能是当 $E_{3}$ 处处为零时积分为零。因此， $\pmb{E}_1 = \pmb{E}_2$ ，定理得到证明。

这个证明并不容易，并且存在一个真切的危险，即定理本身对你来说似乎比证明更加可信。如果你认为第二唯一性定理是“显而易见的”，考虑珀塞尔的这个例子：图3.7给出一个简单的静电构型，它包含有四个所带电荷量分别为 $\pm Q$ 的导体，其位置使带正电荷的导体紧靠着带负电的一个。这一切看起来都很稳定自然。现在，如图3.8所示，如果我们用细导线把它们成对连接起来将会发生什么？由于正电荷非常接近负电荷（这是它们最可能在的位置），你也许会猜想什么都不会发生——几何构型仍然稳定。

![](images/270b11be321c1cc3c89de37f75f502395fd7c0218a4ebfc8aecf676ec54926e1.jpg)  
图3.7

![](images/113dc1d6267533394f8b596ed9b5e61b8cb4337bd453f6a2ea266286a430fb08.jpg)  
图3.8

好的，这听起来很合理，但却是错误的。图 3.8 中所给的构型是不可能的。因为现在实际上有两个导体，每个导体上的总电荷为零。在这些导体上电荷分布为零的一种可能方式是在导体上任何地方都没有电荷积聚，因此电场处处为零（图 3.9）。根据第二唯一性定理，这一定是问题的解：电荷将沿细线流动，正负相互抵消。

![](images/be4c5e278454dc7d2a40f53618c6c61218c3073898323dc1e52f61511fab570c.jpg)  
图3.9

习题 3.5 证明：当电荷密度 $\rho$ 给定，并且在每个边界上 V 或其法向导数 $\partial V/\partial n$ 给定时，电场可以唯一确定。不要假设边界是导体，也不要假设 V 在任何表面上是恒量。

习题3.6 第二唯一性定理的一个更简洁的证明利用了格林恒等式（习题1.61c），其中 $T = U = V_{3}$ 给出详细证明。

## 3.2 镜像法

## 3.2.1 典型镜像问题

假设点电荷 q 位于无限大接地导体平面上方距离 d 处（图 3.10）。问题：导体平面上方区域的电势是多少？它不会再是 $(1/4\pi\varepsilon_{0})q/\nu$ ，因为 q 将在靠近它的平面上感应出一定量的负电荷；总的电势部分是由 q 直接产生的，部分是由感应电荷产生的。但是，当我们不知道感应出多少电荷或者电荷是如何分布时，我们怎么可能计算出电势呢？

![](images/f5a29ce3afd085e49c6e6022a17d78c48e99899231690c998ceeb7527437713f.jpg)  
图3.10

从数学的角度来看，我们的问题是在 $z > 0$ 的区域内求解泊松方程，其中在 $(0,0,d)$ 处有一点电荷，受边界条件的约束：

1. 当 z=0 时，V=0（因为导体平板接地）；

2. 当远离电荷时， $V \rightarrow 0$ （即 $x^{2} + y^{2} + z^{2} \gg d^{2}$ ）。

第一唯一性定理（实际上是它的推论）保证只有一个函数满足上述要求。如果我们能通过一些技巧或精心的猜测可以找到这样一个函数，那它一定是答案。

技巧：把实际问题放在一边，我们研究一个完全不同的情况。新的几何构型有两个点电荷，+q 在 $(0,0,d)$ 处，-q 在 $(0,0,-d)$ 处，没有导体平面存在（图 3.11）。对于这个构型，我可以很容易地写出它的电势：

$$
V (x, y, z) = \frac {1}{4 \pi \varepsilon_ {0}} \left[ \frac {q}{\sqrt {x ^ {2} + y ^ {2} + (z - d) ^ {2}}} - \frac {q}{\sqrt {x ^ {2} + y ^ {2} + (z + d) ^ {2}}} \right]\tag{3.9}
$$

（分母分别表示从点 $(x,y,z)$ 到 $+q$ 或 $-q$ 的距离。）由此可见

1. 当 $z = 0$ 时， $V = 0$ ;

2. 对于 $x^{2} + y^{2} + z^{2} \gg d^{2}$ 时， $V \to 0$

![](images/bdaa34d2f6b3a9b943934a5088173bdc7b6d93759f288a129c4161300447b95a.jpg)  
图3.11

并且在 $z > 0$ 区域中，仅有的电荷是位于 $(0,0,d)$ 处的点电荷 $+q$ 。但这些正是原始问题的条件！显然，在 $z \geqslant 0$ 的“上半”区域，第二种几何构型恰好与第一种几何构型所产生的电势完全相同。（在 $z < 0$ 的“下半”区域，是完全不同的，但我们不关心这个，仅上半部分是我们需要的。）结论：当 $z \geqslant 0$ 时，无限大接地导体板上方的点电荷产生的电势由式(3.9)给出。

请注意唯一性定理在这个论证中所起的关键作用：没有它，没有人会相信这个解，因为它是针对一个完全不同的电荷分布得到的。但唯一性定理证明了这一点：如果解在所考虑问题区域内满足泊松方程，并在边界处取正确的值，那么它一定是正确的解。

## 3.2.2 表面感应电荷

现在一旦我们知道了电势，计算导体上感应的表面电荷 $\sigma$ 就很直截了当了。根据式(2.49)，

$$
\sigma = - \varepsilon_ {0} \frac {\partial V}{\partial n}
$$

式中， $\partial V / \partial n$ 是 $V$ 在表面处的法向导数。在这种情况下，法向就是 $z$ 方向，所以

$$
\sigma = - \varepsilon_ {0} \left. \frac {\partial V}{\partial z} \right| _ {z = 0}
$$

由式 (3.9)

$$
\frac {\partial V}{\partial z} = \frac {1}{4 \pi \varepsilon_ {0}} \left\{\frac {- q (z - d)}{\left[ x ^ {2} + y ^ {2} + (z - d) ^ {2} \right] ^ {3 / 2}} + \frac {q (z + d)}{\left[ x ^ {2} + y ^ {2} + (z + d) ^ {2} \right] ^ {3 / 2}} \right\}
$$

所以 $^{5}$

$$
\sigma (x, y) = \frac {- q d}{2 \pi (x ^ {2} + y ^ {2} + d ^ {2}) ^ {3 / 2}}\tag{3.10}
$$

正如预期的那样，感应电荷是负的（假设 $q$ 是正的）， $\sigma$ 在 $x = y = 0$ 时最大。

既然说到这里，让我们计算总的感应电荷

$$
Q = \int \sigma \mathrm{d} a
$$

对平面上的这个积分可以在直角坐标系中完成，其中 $\mathrm{da} = \mathrm{d}x\mathrm{d}y$ ；不过用极坐标 $(r, \phi)$ 进行积分会更容易些，此时 $r^2 = x^2 + y^2$ 以及 $\mathrm{da} = r\mathrm{d}r\mathrm{d}\phi$ 。那么

$$
\sigma (r) = \frac {- q d}{2 \pi (r ^ {2} + d ^ {2}) ^ {3 / 2}}
$$

从而

$$
Q = \int_ {0} ^ {2 \pi} \int_ {0} ^ {\infty} \frac {- q d}{2 \pi (r ^ {2} + d ^ {2}) ^ {3 / 2}} r \mathrm{d} r \mathrm{d} \phi = \left. \frac {q d}{\sqrt {r ^ {2} + d ^ {2}}} \right| _ {0} ^ {\infty} = - q\tag{3.11}
$$

在平板面上感应的总电荷为 -q，（后见之明）你们可以说服自己它的确应该如此。

## 3.2.3 力和能

由于负的感应电荷，电荷 q 将被吸引向板面。让我们计算一下这个吸引力。由于 q 附近的电势与类似问题（即有 +q 和 -q，但是没有导体板的问题）中的电势相同，因此电场也是如此，所以力为

$$
\pmb {F} = - \frac {1}{4 \pi \varepsilon_ {0}} \frac {q ^ {2}}{(2 d) ^ {2}} \hat {\pmb {z}}\tag{3.12}
$$

小心：这很容易一时兴奋而忘乎所以，并假设这两个问题中的一切都是一样的。然而，能量并不一样。对没有导体板存在的两个点电荷问题，式(2.42)给出

$$
W = - \frac {1}{4 \pi \varepsilon_ {0}} \frac {q ^ {2}}{2 d}\tag{3.13}
$$

但对于单电荷和导体板问题，能量为该值的一半：

$$
W = - \frac {1}{4 \pi \varepsilon_ {0}} \frac {q ^ {2}}{4 d}\tag{3.14}
$$

为什么是一半？思考一下储存在电场中的能量 [式 (2.45)]:

$$
W = \frac {\varepsilon_ {0}}{2} \int E ^ {2} \mathrm{d} \tau
$$

在第一种情况下，上半区域 $(z>0)$ 和下半区域 $(z<0)$ 都有贡献——而且由对称性它们的贡献是相等的。但在第二种情况下，仅在上半区域存在非零的电场，因此能量是其一半 $^{6}$ 。

当然，也可以通过计算从无限远处引入 $q$ 所需的功来确定能量。所需的力是 $(1 / 4\pi \varepsilon_0)(q^2 /4z^2)\hat{z}$ [与式(3.12)所给的电场力反向]，所以

$$
W = \int_ {\infty} ^ {d} \boldsymbol {F} \cdot \mathrm{d} \boldsymbol {l} = \frac {1}{4 \pi \varepsilon_ {0}} \int_ {\infty} ^ {d} \frac {q ^ {2}}{4 z ^ {2}} \mathrm{d} z = \frac {1}{4 \pi \varepsilon_ {0}} \left. \left(- \frac {q ^ {2}}{4 z}\right) \right| _ {\infty} ^ {d} = - \frac {1}{4 \pi \varepsilon_ {0}} \frac {q ^ {2}}{4 d}.
$$

当我把 q 移向导体板时，我仅对 q 做功。感应电荷确实也在导体板上运动，但这并不消耗能量，因为整个导体的电势为零。相比之下，如果我同时引入两个点电荷（没有导体板），我对两个电荷都需要做功，因此总功（再次）加倍。

## 3.2.4 其他镜像问题

前面描述的方法并不仅限于单个点电荷；通过引入镜像，接地导体板附近任何静止电荷分布都可以用这种方法处理——因此称为镜像法（method of images）。（记住，镜像电荷具有相反的符号；这是保证 $xy$ 平面处于电势为零的原因。）也有一些奇特的问题也可以用类似的方法处理，下面是最吸引人的一个。

例题3.2 一点电荷 $q$ 位于距半径为 $R$ 的接地导体球中心 $a$ 处（图3.12）。求球外的电势。

![](images/22bba279fb0601d1998eaa5d51d9e56eb987e884e96dde8ba601e305fbf8dcdd.jpg)  
图3.12

[解答] 考察由点电荷和另外一个点电荷组成的完全不同的几何构型

$$
q ^ {\prime} = - \frac {R}{a} q\tag{3.15}
$$

将其放置在距球心右边的距离为（图3.13）

$$
b = \frac {R ^ {2}}{a}\tag{3.16}
$$

现在没有导体板——仅有两个电荷。这个几何构型的电势为

$$
V (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \left(\frac {q}{\nu} + \frac {q ^ {\prime}}{\nu^ {\prime}}\right)\tag{3.17}
$$

其中 $n, n'$ 分别为场点到 $q$ 和 $q'$ 的距离。现在，碰巧这个势在球面上所有的点都为零（见习题3.8），因此在球体外部区域满足我们的原始问题设定的边界条件 $^{7}$ 。

![](images/5a9141a7c7b2f98f3c4363bddb88c009b9bc5ac61e690d73c436f254b6c763bc.jpg)  
图3.13

结论：式(3.17)是接地导体球附近的点电荷的电势。（请注意：b小于R，所以镜像电荷 $q'$ 安全地位于球内——你不能将镜像电荷放在你要计算V的区域内；这将会改变 $\rho$ ，你会用错误的源电荷求解泊松方程。）特别是，点电荷和球体之间的吸引力为

$$
F = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q q ^ {\prime}}{(a - b) ^ {2}} = - \frac {1}{4 \pi \varepsilon_ {0}} \frac {q ^ {2} R a}{(a ^ {2} - R ^ {2}) ^ {2}}\tag{3.18}
$$

镜像法在使用时非常简单。但镜像法既是一门科学，也是一门艺术，因为你必须以某种方式想出正确的“辅助”构型，对于大多数形状来说，即使是可能的，它也是极其复杂的。

习题 3.7 求图 3.14 中作用在电荷 +q 上的力。(xy 平面接地。)

![](images/0b58b8cc2961a1c9fc1abde5cf53e5e42f05e5e29b41543f48fabbd1c61353de.jpg)  
图3.14

## 习题3.8

（a）利用余弦定理，证明式(3.17)可以写成如下形式：

$$
V (r, \theta) = \frac {1}{4 \pi \varepsilon_ {0}} \left[ \frac {q}{\sqrt {r ^ {2} + a ^ {2} - 2 r a \cos \theta}} - \frac {q}{\sqrt {R ^ {2} + (r a / R) ^ {2} - 2 r a \cos \theta}} \right]\tag{3.19}
$$

其中 $r$ 和 $\theta$ 是通常的球面极坐标， $z$ 沿穿过 $q$ 的线。在这种形式下，很明显球面上， $r = R$ 。

(b) 作为 $\theta$ 的函数，求出球体上感应的表面电荷。对其积分求出总感应电荷。（应该是多少？）

(c) 计算该几何构型的能量。

习题3.9 在例题3.2中，我们假设导体球是接地的 $(V = 0)$ 。但是，通过添加第二个镜像电荷，同样的模型可以处理球体具有任意电势 $V_{0}$ 的情况（当然是相对于无限远处）。你应该使用什么样的电荷，应该把它放在哪里？求点电荷 $q$ 和中性导体球之间的吸引力。

!习题 3.10 一无限长均匀带电的导线线密度为 $\lambda$ ，位于接地导体板上方的距离为 $d_{0}$ （假设带电导线平行于 x 轴并位于其上方，导体板为 xy 平面。）

(a) 求导体板平面上方区域的电势。(提示：参考习题 2.52)

(b) 求导体板上感应的电荷密度 $\sigma_{0}$

习题 3.11 如图 3.15 所示，两个半无限大接地导体板的夹角为直角，在它们之间的区域有一点电荷 q。给出镜像电荷的几何构型，计算在该区域内的电势。你应当选用什么样的电荷，应该把它们放在哪里？作用在 q 上的力是多少？把 q 从无限远处移至图示位置需要做多少功？假定两导体板的夹角度不是 $90^{\circ}$ ，你还能用镜像法求解该问题吗？如果不能，该方法适用于哪些特定角度？

![](images/d758eaaf232d869800e17ab5beb59604dc6e9de4cef635502bf334cd9925fda3.jpg)  
图3.15

!习题 3.12 两根长而直的铜管，每根半径为 R，相距为 2d。一个电势为 $V_{0}$ ，另一个为 $-V_{0}$ （图 3.16）。求各处的电势。[提示：利用习题 2.52 的结果。]

![](images/064b5b048bd4070727c3bca27ac61f850469861c8a9d2aec044d33939866f782.jpg)  
图3.16

## 3.3 分离变量法

在本节中，我们将直接使用分离变量法（separation of variables）全力求解拉普拉斯方程，这是物理学家最喜欢的求解偏微分方程的工具。该方法适用于在某些区域的边界上电势（V）或电荷密度（ $\sigma$ ）给定，要求求解内部电势大小的情况。基本方法很简单：我们寻求函数乘积形式的解，每个函数只与一个坐标有关。然而，具体代数细节可能有点繁杂，所以我将通过一系列的例子来阐述这种方法。我先从直角坐标系开始，然后再讨论球坐标系（我将在习题3.24中把柱坐标系的情况留给你自己处理。）

![](images/769f7039dee4fce810194fa73847a195a8b75446e64e94df0b3f52c475a96154.jpg)  
图3.17

## 3.3.1 直角坐标系

例题3.3 两个无限大接地金属平板平行于 $xz$ 平面放置，一个位于 $y = 0$ 处，另一个位于 $y = a$ （图3.17）处。在 $x = 0$ 处的两板左端，用一无限长绝缘条将两板封闭连接起来，并维持绝缘条上一给定电势 $V_{0}(y)$ 。求“狭槽”中的电势。

[解答] 该几何构型与 $z$ 无关，所以这实际上是一个二维问题。用数学术语来讲，我们必须求解拉普拉斯方程

$$
\frac {\partial^ {2} V}{\partial x ^ {2}} + \frac {\partial^ {2} V}{\partial y ^ {2}} = 0\tag{3.20}
$$

满足如下边界条件：

$$
\left. \begin{array}{l} {\mathrm{(i)} \text {当} y = 0 \text {时,} V = 0} \\ {\mathrm{(ii)} \text {当} y = a \text {时,} V = 0} \\ {\mathrm{(iii)} \text {当} x = 0 \text {时,} V = V _ {0} (y)} \\ {\mathrm{(iv)} \text {当} x \to \infty \text {时,} V \to 0} \end{array} \right\}\tag{3.21}
$$

（最后一个边界条件虽然在问题中没有明确给出，但从物理的角度来看是必要的：当你离 $x = 0$ 处的“热”带越来越远时，电势应该减小至零。）由于电势在所有边界上都是给定的，因此问题的解是唯一确定的。

第一步是找出具有乘积形式的解：

$$
V (x, y) = X (x) Y (y)\tag{3.22}
$$

从表面上看来，这是一个不合理的限制——拉普拉斯方程的绝大多数解都不具有这样的形式。例如， $V(x, y) = (5x + 6y)$ 满足式(3.20)，但你不能将其表示为一个 $x$ 的函数和一个 $y$ 的函数的乘积。显然，通过这种方法我们只能得到所有可能解中的一小部分，如果其中一个满足了我们问题的边界条件，那将是一个奇迹……但请稍候，因为我们得到的解的确非常特殊，事实证明，通过把这些特解黏合在一起，我们就可以得到通解。

不管怎样，将式(3.22)代入式(3.20)，我们得到

$$
Y \frac {\mathrm{d} ^ {2} X}{\mathrm{d} x ^ {2}} + X \frac {\mathrm{d} ^ {2} Y}{\mathrm{d} y ^ {2}} = 0
$$

下一步是“分离变量”（也就是说，将所有与 $x$ 有关的项合成一项，所有与 $y$ 有关的项合在另外一项）。通常，这可以通过除以 $V$ 来实现：

$$
\frac {1}{X} \frac {\mathrm{d} ^ {2} X}{\mathrm{d} x ^ {2}} + \frac {1}{Y} \frac {\mathrm{d} ^ {2} Y}{\mathrm{d} y ^ {2}}\tag{3.23}
$$

现在第一项只与 $x$ 有关，第二项仅与 $y$ 有关；换句话说，我们有如下形式的方程式

$$
f (x) + g (y) = 0\tag{3.24}
$$

该方程成立只有一种可能： $f$ 和 $g$ 都必须为常量。因为 $f(x)$ 随 $x$ 的变化而变化，那么如果我们保持 $y$ 不变并改变 $x$ ，则 $f(x) + g(x)$ 将发生改变，这违反了式 (3.24)，也就是两者之和始终为零。（这是一个简单但又难以解释的论点；不要在没有经过深思熟虑的情况下接受它，因为整个的方法都取决于它。）根据式 (3.23)，可以得出

$$
\frac {1}{X} \frac {\mathrm{d} ^ {2} X}{\mathrm{d} x ^ {2}} = C _ {1}, \quad \frac {1}{Y} \frac {\mathrm{d} ^ {2} Y}{\mathrm{d} y ^ {2}} = C _ {2}, \quad C _ {1} + C _ {2} = 0\tag{3.25}
$$

其中一个常数为正，另一个为负（或者两个都为零）。一般来说，我们必须对所有的可能性进行研究；不过，在具体问题中，我们让 $C_1$ 为正， $C_2$ 为负，其中的原因稍后说明。这样

$$
\frac {\mathrm{d} ^ {2} X}{\mathrm{d} x ^ {2}} = k ^ {2} X, \quad \frac {\mathrm{d} ^ {2} Y}{\mathrm{d} y ^ {2}} = - k ^ {2} Y\tag{3.26}
$$

请注意发生了什么：一个偏微分方程 [式 (3.20)] 转换成两个常微分方程 [式 (3.26)]。这样做的好处是显而易见的——常微分方程更容易求解。的确：

$$
X (x) = A \mathrm{e} ^ {k x} + B \mathrm{e} ^ {- k x}, Y (y) = C \sin k y + D \cos k y
$$

所以

$$
V (x, y) = (A \mathrm{e} ^ {k x} + B \mathrm{e} ^ {- k x}) (C \sin k y + D \cos k y)\tag{3.27}
$$

这就是拉普拉斯方程相应的分离变量解；仍需要加上边界条件，给出关于常数的值。从末尾开始，条件（iv）要求 A 等于零 $^{8}$ 。将 B 代入 C 和 D 中，我们只剩下

$$
V (x, y) = \mathrm{e} ^ {- k x} (C \sin k y + D \cos k y)
$$

现在条件（i）要求 $D = 0$ ，所以

$$
V (x, y) = C \mathrm{e} ^ {- k x} \sin k y\tag{3.28}
$$

同时条件（ii）给出 $\sin ka = 0$ ，由此可得

$$
k = \frac {n \pi}{a} (n = 1, 2, 3, \dots)\tag{3.29}
$$

（此时，你可以明白我为什么选择 $C_1$ 为正和 $C_2$ 为负：如果 $X$ 是正弦函数，我们无法使它在无限远处为零；如果 $Y$ 是指数函数，我们也无法使它在0和 $a$ 点处为零。顺便说一句， $n = 0$ 是无意义的，因为在这种情况下电势处处为零。我们也已经排除了 $n$ 为负的情况。）

这就是至此我们利用分离变量所能够做到的。除非对于某个整数 $n$ ， $V_0(y)$ 恰好具有 $\sin(n\pi y/a)$ 的形式，否则我们根本不可能在 $x = 0$ 处找到最终的边界条件。但现在关键的一步来了，它弥补了这种方法：分离变量法给我们提供了一个无限的解集（每个 $n$ 对应一个解），尽管它们本身都不满足最终的边界条件，但它们以某种方式的组合却是有可能的。拉普拉斯方程是线性方程，即如果 $V_1, V_2, V_3, \cdots$ 分别满足方程，则它们的任何线性组合 $V = \alpha_1 V_1 + \alpha_2 V_2 + \alpha_3 V_3 + \cdots$ 也满足该方程，其中 $\alpha_1, \alpha_2, \alpha_3, \cdots$ 为任意常数。因为

$$
\nabla^ {2} V = \alpha_ {1} \nabla^ {2} V _ {1} + \alpha_ {2} \nabla^ {2} V _ {2} + \dots = 0 \alpha_ {1} + 0 \alpha_ {2} + \dots = 0
$$

利用这个事实，我们可以把分离变量解（3.28）组合起来构造更一般的通解：

$$
V (x, y) = \sum_ {n = 1} ^ {\infty} C _ {n} \mathrm{e} ^ {- n \pi x / a} \sin (n \pi y / a)\tag{3.30}
$$

这仍然满足三个边界条件；问题是，我们能否满足（通过巧妙地选择组合系数 $C_n$ ）最后的边界条件 (iii)?

$$
V (0, y) = \sum_ {n = 1} ^ {\infty} C _ {n} \sin (n \pi y / a) = V _ {0} (y)\tag{3.31}
$$

好的，你可能已经认出这个求和——它是傅里叶正弦级数（Fourier sine series）。狄利克雷（Dirichlet）定理 $^{9}$ 保证了几乎任何函数 $V_{0}(y)$ ——甚至它可以有有限个不连续的数——都可以利用这个级数展开。

但是，由于系数隐藏在无穷求和当中，我们实际上又是如何确定它的呢？实现这一目标的方法太漂亮了，值得拥有一个名字——尽管欧拉似乎在早些时候使用了基本相同的想法，我还是称之为傅里叶技巧（Fourier's trick）。这个技巧是这样的：将式(3.31)乘以 $\sin (n' \pi y / a)$ （其中 $n'$ 是正整数），并从0到 $a$ 进行积分：

$$
\sum_ {n = 1} ^ {\infty} C _ {n} \int_ {0} ^ {a} \sin (n \pi y / a) \sin \left(n ^ {\prime} \pi y / a\right) \mathrm{d} y = \int_ {0} ^ {a} V _ {0} (y) \sin (n \pi y / a) \mathrm{d} y\tag{3.32}
$$

你可以自己求出左边的积分；答案是

$$
\int_ {0} ^ {a} \sin (n \pi y / a) \sin (n ^ {\prime} \pi y / a) \mathrm{d} y = \left\{ \begin{array}{l l} {{0}} & {{\text {如果} n ^ {\prime} \neq n}} \\ {{\frac {a}{2}}} & {{\text {如果} n ^ {\prime} = n}} \end{array} \right.\tag{3.33}
$$

因此，除 $n' = n$ 项以外，级数中其余项都为零，式 (3.32) 的左侧简化为 $(a/2)C_{n'}$ 。结论 $^{10}$ ：

$$
C _ {n} = \frac {2}{a} \int_ {0} ^ {a} V _ {0} (y) \sin (n \pi y / a) \mathrm{d} y\tag{3.34}
$$

这样就可以了：式(3.30)是所要求的解，系数由式(3.34)给出。作为一个具体的例子，假定在 $x = 0$ 处的条带是一块具有恒定电势的金属板（请记住，在 $y = 0$ 和 $y = a$ 处，它是与接地板绝缘的）。那么

$$
C _ {n} = \frac {2 V _ {0}}{a} \int_ {0} ^ {a} \sin (n \pi y / a) \mathrm{d} y = \frac {2 V _ {0}}{n \pi} (1 - \cos n \pi) = \left\{ \begin{array}{c l} {{0,}} & {{\text {如果} n \text {为偶数}}} \\ {{\frac {4 V _ {0}}{\pi n},}} & {{\text {如果} n \text {为奇数}}} \end{array} \right.\tag{3.35}
$$

$$
V (x, y) = \frac {4 V _ {0}}{\pi} \sum_ {n = 1, 3, 5, \dots} \frac {1}{n} \mathrm{e} ^ {- n \pi x / a} \sin (n \pi y / a)\tag{3.36}
$$

图 3.18 为该电势的曲线图；图 3.19 展示了傅里叶级数中前几项是如何叠加起来越来越接近常数 $V_{0}$ 的：（a）仅含 n=1 项，（b）n 取到前 5 项，（c）为前 10 项之和，（d）为前 100 项之和。

![](images/084f85fb9ec5a3411cb2091ff0ab3a4d6e4a15a015f7f54715ffa02de0618cd4.jpg)  
图3.18

![](images/ec1aa52caef0033f790cc6a929b84d8376a41f1b397ac542c6ece32646368d9b.jpg)  
图3.19

顺便说一句，式(3.36)中的无穷级数可以显式求和（如果你愿意，可以试试）；结果是

$$
V (x, y) = \frac {2 V _ {0}}{\pi} \arctan \left(\frac {\sin (\pi y / a)}{\sinh (\pi x / a)}\right)\tag{3.37}
$$

在这种形式中，很容易去验证拉普拉斯方程是否成立以及四个边界条件 [式 (3.21)] 是否得到满足。

分离变量解的成功取决于该方法的两个独特的性质 [式 (3.28) 和式 (3.29)]：完备性（completeness）和正交性（orthogonality）。如果任何其他函数都可以表示为一组函数 $f_{n}(y)$ 的线性组合，则称这组函数是完备的：

$$
f (y) = \sum_ {n = 1} ^ {\infty} C _ {n} f _ {n} (y)\tag{3.38}
$$

函数集 $\sin (n\pi y / a)$ 在区间 $0\leqslant y\leqslant a$ 上是完备的（complete）。正是这样一个事实，加之狄利克雷定理的保证下和适当选择系数，式(3.31）就可以满足。（对一组特定的函数完备性的证明是一项非常困难的工作，恐怕物理学家都是倾向于承认它是正确的，而把验证留给他人。）如果函数集的任意两个函数的乘积的积分为零，则函数集是正交的（orthogonal）：

$$
\int_ {0} ^ {a} f _ {n} (y) f _ {n} ^ {\prime} (y) \mathrm{d} y = 0 \quad \text {对} n ^ {\prime} \neq n\tag{3.39}
$$

正弦函数是正交的 [式 (3.33)]；这个性质是傅里叶技巧的基础，它使得我们能够消除无穷级数中除一项外的所有项，从而求得系数 $C_n$ 。（正交性的证明通常很简单，要么通过直接积分，要么通过分析函数所来自的微分方程。）

例题3.4如图3.20所示，两个无限长的接地金属板，分别在 $y = 0$ 和 $y = a$ 放置；在 $x = \pm b$ 的侧边由具有恒定电势为 $V_{0}$ 的两个金属条带连接起来构成一个矩形管道（在每个角都有一层薄薄的绝缘层防止金属板之间短路）。求矩形管道中的电势。

![](images/888b68617ca437c0fa0cc478dca4f9afbe7746c33d7cdf2e539d1f4884f23df4.jpg)  
图3.20

[解答] 再次，该几何构型与 $z$ 无关。我们的问题是求解下面边界条件下的拉普拉斯方程

$$
\frac {\partial^ {2} V}{\partial x ^ {2}} + \frac {\partial^ {2} V}{\partial y ^ {2}} = 0,
$$

(ii) 当 $y = a$ 时， $V = 0$

(iii) 当 $x = b$ 时， $V = V_0$

(3.40)

(iv) 当 $x = -b$ 时， $V = V_0$

直到式 (3.27)，所有做法同以前一样：

$$
V (x, y) = \left(A \mathrm{e} ^ {k x} + B \mathrm{e} ^ {- k x}\right) (C \sin k y + D \cos k y)
$$

然而，这一次我们不能再令 $A = 0$ ；问题所讨论的区域没有扩展到 $x = \infty$ ，因此 $\mathrm{e}^{kx}$ 是完全可取的。另一方面，所研究问题关于 $x$ 轴对称，所以 $V(-x,y) = V(x,y)$ ，因此有 $A = B$ 。利用

$$
\mathrm{e} ^ {k x} + \mathrm{e} ^ {- k x} = 2 \cosh k x
$$

并将 2A 代入 C 和 D，我们有

$$
V (x, y) = \cosh k x \left(C \sin k x + D \cos k x\right)
$$

同前面一样，边界条件（i）和（ii）要求 $D = 0$ 和 $k = n\pi /a$ ，所以

$$
V (x, y) = C \cosh (n \pi x / a) \sin (n \pi y / a)\tag{3.41}
$$

由于 $V(x,y)$ 是 $x$ 的偶函数，如果它满足条件（iii），它将自动满足条件（iv）。因此，仍然需要构建一般的线性组合

$$
V (x, y) = \sum_ {n = 1} ^ {\infty} C _ {n} \cosh (n \pi x / a) \sin (n \pi y / a)
$$

通过满足条件（iii）来确定系数 $C_n$

$$
V (b, y) = \sum_ {n = 1} ^ {\infty} C _ {n} \cosh (n \pi b / a) \sin (n \pi y / a) = V _ {0}
$$

这与我们之前在傅里叶分析中面临的问题相同；我引用式（3.35）的结果

$$
C _ {n} \cosh (n \pi b / a) = \left\{ \begin{array}{l l} 0, \\ \frac {4 V _ {0}}{n \pi}, \end{array} \right.
$$

如果 $n$ 为偶数

如果 $n$ 为奇数

结论：在这种情况下电势为

$$
V (x, y) = \frac {4 V _ {0}}{\pi} \sum_ {n = 1, 3, 5, \dots} \frac {1}{n} \frac {\cosh (n \pi x / a)}{\cosh (n \pi b / a)} \sin (n \pi y / a)\tag{3.42}
$$

该函数如图 3.21 所示。

![](images/c557a57f3f08a1f8648aad3ad541ecffdfa8e465d1ae19b88b84c0c3d207e703.jpg)

例题3.5 如图3.22所示，无限长矩形金属管（边长分别为 $a$ 和 $b$ ），在其 $x = 0$ 的一端保持给定的电势 $V_{0}(y,z)$ 。求管内的电势。[解答] 这是一个真正的三维问题

$$
\frac {\partial^ {2} V}{\partial x ^ {2}} + \frac {\partial^ {2} V}{\partial y ^ {2}} + \frac {\partial^ {2} V}{\partial z ^ {2}} = 0\tag{3.43}
$$

其边界条件为

$$
\left. \begin{array}{l l} \text {(i)} y = 0, & V = 0 \\ \text {(ii)} y = a, & V = 0 \\ \text {(iii)} z = 0, & V = 0 \\ \text {(iv)} z = b, & V = 0 \\ \text {(v)} x \to \infty , & V \to 0 \\ \text {(vi)} x = 0, & V = V _ {0} (y, z) \end{array} \right\}\tag{“”}
$$

(3.44)

![](images/6dd48ea9b5df8c167579899cff8be3ed5708be6b7ca6d4bbaea56f20a1e7bf9f.jpg)  
图3.22

与前面一样，我们寻找乘积形式的解

$$
V (x, y, z) = X (x) Y (y) Z (z)\tag{3.45}
$$

将该式代入式 (3.43) 并除以 $V$ ，我们有

$$
\frac {1}{X} \frac {\mathrm{d} ^ {2} X}{\mathrm{d} x ^ {2}} + \frac {1}{Y} \frac {\mathrm{d} ^ {2} Y}{\mathrm{d} y ^ {2}} + \frac {1}{Z} \frac {\mathrm{d} ^ {2} Z}{\mathrm{d} z ^ {2}} = 0
$$

由此可得

$$
\frac {1}{X} \frac {\mathrm{d} ^ {2} X}{\mathrm{d} x ^ {2}} = C _ {1}, \frac {1}{Y} \frac {\mathrm{d} ^ {2} Y}{\mathrm{d} y ^ {2}} = C _ {2}, \frac {1}{Z} \frac {\mathrm{d} ^ {2} Z}{\mathrm{d} z ^ {2}} = C _ {3}, \text {其中,} C _ {1} + C _ {2} + C _ {3} = 0
$$

我们之前的经验（例题3.3）表明： $C_1$ 必须为正， $C_2$ 和 $C_3$ 必须为负。令 $C_2 = -k^2$ ， $C_3 = -l^2$ ，因此有 $C_1 = k^2 + l^2$ ，所以

$$
\frac {\mathrm{d} ^ {2} X}{\mathrm{d} x ^ {2}} = \left(k ^ {2} + l ^ {2}\right) X, \quad \frac {\mathrm{d} ^ {2} Y}{\mathrm{d} y ^ {2}} = - k ^ {2} Y, \quad \frac {\mathrm{d} ^ {2} Z}{\mathrm{d} z ^ {2}} = - l ^ {2} Z\tag{3.46}
$$

分离变量再次将一个偏微分方程转化为常微分方程。解为

$$
\begin{array}{l} X (x) = A \mathrm{e} ^ {\sqrt {k ^ {2} + l ^ {2}} x} + B \mathrm{e} ^ {- \sqrt {k ^ {2} + l ^ {2}} x} \\ Y (y) = C \sin k y + D \cos k y \\ Z (z) = E \sin l z + F \cos l z \end{array}
$$

边界条件（v）意味着 $A = 0$ ，（i）给出 $D = 0$ ，（iii）得到 $F = 0$ ，而（ii）和（iv）要求 $k = n\pi /a$ 和 $l = m\pi /b$ ，这里 $n,m$ 为正整数。结合剩余的常数，我们得到

$$
V (x, y, z) = C \mathrm{e} ^ {- \pi \sqrt {(n / a) ^ {2} + (m / b) ^ {2}} x} \sin (n \pi y / a) \sin (m \pi z / b)\tag{3.47}
$$

该解满足除（vi）之外的所有边界条件。它包含两个待定整数 $m$ 和 $n$ ，最一般的线性组合是对双重求和：

• = , i    , i
,    =    ,    ,
=    i =    ,
,    , ,    ,

$$
V (x, y, z) = \sum_ {n = 1} ^ {\infty} \sum_ {m = 1} ^ {\infty} C _ {n, m} \mathrm{e} ^ {- \pi \sqrt {(n / a) ^ {2} + (m / b) ^ {2}} x} \sin (n \pi y / a) \sin (m \pi z / b)\tag{3.48}
$$

我们希望通过选择合适的系数 $C_{n,m}$ 来满足剩余的边界条件

$$
V (0, y, z) = \sum_ {n = 1} ^ {\infty} \sum_ {m = 1} ^ {\infty} C _ {n, m} \sin (n \pi y / a) \sin (m \pi z / b) = V _ {0} (y, z)\tag{3.49}
$$

为了确定这些系数，我们乘以 $\sin (n' \pi y / a) \sin (m' \pi z / b)$ ，其中 $n', m'$ 为任意正整数，然后进行积分：

$$
\begin{array}{l} \sum_ {n = 1} ^ {\infty} \sum_ {m = 1} ^ {\infty} C _ {n, m} \int_ {0} ^ {a} \sin (n \pi y / a) \sin (n ^ {\prime} \pi y / a) \mathrm{d} y \int_ {0} ^ {b} \sin (m \pi z / b) \sin (m ^ {\prime} \pi z / b) \mathrm{d} z \\ = \int_ {0} ^ {a} \int_ {0} ^ {b} V _ {0} (y, z) \sin (n ^ {\prime} \pi y / a) \sin (m ^ {\prime} \pi z / b) \mathrm{d} y \mathrm{d} z \end{array}
$$

引用式 (3.33) 的结果，左边等于 $(ab / 4)C_{n',m'}$ ，所以

$$
C _ {n, m} = \frac {4}{a b} \int_ {0} ^ {a} \int_ {0} ^ {b} V _ {0} (y, z) \sin (n \pi y / a) \sin (m \pi z / b) \mathrm{d} y \mathrm{d} z\tag{3.50}
$$

式 (3.48) 是我们问题的解，其系数由式 (3.50) 给出。

例如，如果管的端部是恒定电势 $V_{0}$ 的导体，

$$
C _ {n, m} = \frac {4 V _ {0}}{a b} \int_ {0} ^ {a} \sin (n \pi y / a) \mathrm{d} y \int_ {0} ^ {b} \sin (m \pi z / b) \mathrm{d} z
$$

i, n, i, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n,

$$
= \left\{ \begin{array}{l l} 0, & \text {如果} n \text {或} m \text {为偶数} \\ \frac {1 6 V _ {0}}{\pi^ {2} n m}, & \text {如果} n \text {和} m \text {为奇数} \end{array} \right.\tag{3.51}
$$

在这种情况下

$\begin{array}{ccccccccc}1 & = & \ddots & \ddots & 1 &  &  & \ddots \\ = & = & \ddots &  &  &  & \ddots & \ddots \\ = & = & \ddots & \ddots &  &  & \ddots & \ddots \\ = & = & \ddots & \ddots & 1 &  &  &  \\ = & = & \ddots & 1 & \frac{1}{2} & = &  &  \\ = & 1 &  &  &  &  &  &  \\ = & 1 &  &  &  &  &  &  \\ = & 1 &  &  &  &  &  &  \\ = & 1 &  &  &  &  &  &  \\ = & 1 &  &  &  &  &  &  \\ = & 1 &  &  &  &  &  &  \\ = & 1 &  &  & \end{array}$

$$
V (x, y, z) = \frac {1 6 V _ {0}}{\pi^ {2}} \sum_ {n, m = 1, 3, 5, \dots} ^ {\infty} \frac {1}{n m} \mathrm{e} ^ {- \pi \sqrt {(n / a) ^ {2} + (m / b) ^ {2} x}} \sin (n \pi y / a) \sin (m \pi z / b)\tag{3.52}
$$

请注意，后面的各项衰减很快；通过仅保留前几项就可以得到合理的近似。

习题3.13 在例题3.3所示的无限狭槽中，若 $x = 0$ 边界是由两个金属带组成：一个从 $y = 0$ 到 $y = a / 2$ ，并保持恒定电势 $V_{0}$ ；另一个从 $y = a / 2$ 到 $y = a$ ，并保持恒定电势 $-V_{0}$ 。求出该狭槽中的电势。

习题3.14 对于例题3.3中的无限狭槽，假设在 $x = 0$ 处的条带是一具有恒定电势 $V_{0}$ 的导体，求条带上的电荷密度 $\sigma(y)$ 。

习题3.15 一平行于 $z$ 轴放置（从 $-\infty$ 到 $\infty$ ）的矩形管有三个接地的金属面，分别在 $y = 0, y = a, x = 0$ 处。在 $x = b$ 处的第四个面上有恒定电势 $V_0(y)$ 。

(a) 求管内电势的通解公式。

(b) 对于 $V_{0}(y)=V_{0}$ （常数）的情况，求具体的电势值。

习题 3.16 边长为 a 立方体箱子由五块金属板组成，这些金属板焊接在一起并接地（图 3.23）。顶部由单独的金属板制成，与其他金属板绝缘，并保持恒定电势。求箱子内的电势。[中心点 $(a/2, a/2, a/2)$ 的电势应该是多少？通过数值求解来验证该值是否与你的公式相一致。] $^{11}$

![](images/23e1e8a7d7207417d986e503c01072d5c1242565816872382c59bf4af4b09176.jpg)  
图3.23

## 3.3.2 球坐标系

在迄今为止考虑的例子中，由于边界都是平面，所以直角坐标系显然非常适用。对于圆形物体，使用球坐标更合适。在球面系统中，拉普拉斯方程为

$$
\frac {1}{r ^ {2}} \frac {\partial}{\partial r} \left(r ^ {2} \frac {\partial V}{\partial r}\right) + \frac {1}{r ^ {2} \sin \theta} \frac {\partial}{\partial \theta} \left(\sin \theta \frac {\partial V}{\partial \theta}\right) + \frac {1}{r ^ {2} \sin^ {2} \theta} \frac {\partial^ {2} V}{\partial \phi^ {2}} = 0\tag{3.53}
$$

我假定所讨论的问题具有角对称性（azimuthal symmetry），所以 V 与 $\phi$ 无关 $^{12}$ ；在这种情况下，式 (3.53) 简化为

$$
\frac {\partial}{\partial r} \left(r ^ {2} \frac {\partial V}{\partial r}\right) + \frac {1}{\sin \theta} \frac {\partial}{\partial \theta} \left(\sin \theta \frac {\partial V}{\partial \theta}\right) = 0\tag{3.54}
$$

与以前一样，我们求具有乘积形式的解：

$$
V (r, \theta) = R (r) \Theta (\theta)\tag{3.55}
$$

将该式代入式 (3.54)，并除以 $V$ ：

$$
\frac {1}{R} \frac {\mathrm{d}}{\mathrm{d} r} \left(r ^ {2} \frac {\mathrm{d} R}{\mathrm{d} r}\right) + \frac {1}{\Theta \sin \theta} \frac {\mathrm{d}}{\mathrm{d} \theta} \left(\sin \theta \frac {\mathrm{d} \Theta}{\mathrm{d} \theta}\right) = 0\tag{3.56}
$$

由于第一项仅与 $r$ 有关，第二项仅与 $\theta$ 有关，因此每项都必须是常数：

$$
\frac {1}{R} \frac {\mathrm{d}}{\mathrm{d} r} \left(r ^ {2} \frac {\mathrm{d} R}{\mathrm{d} r}\right) = l (l + 1), \quad \frac {1}{\Theta \sin \theta} \frac {\mathrm{d}}{\mathrm{d} \theta} \left(\sin \theta \frac {\mathrm{d} \Theta}{\mathrm{d} \theta}\right) = - l (l + 1)\tag{3.57}
$$

这里 $l(l + 1)$ 只是表示分离常数的一种便利方式——你很快就会明白为什么这样做的方便之处。

与往常一样，分离变量将偏微分方程 [式 (3.54)] 转化为常微分方程 [式 (3.57)]。径向方程是

$$
\frac {\mathrm{d}}{\mathrm{d} r} \left(r ^ {2} \frac {\mathrm{d} R}{\mathrm{d} r}\right) = l (l + 1) R\tag{3.58}
$$

具有通解

$$
R (r) = A r ^ {l} + \frac {B}{r ^ {l + 1}}\tag{3.59}
$$

你可以很容易验证； $A$ 和 $B$ 是二阶微分方程解中预期的两个任意常数。但角方程

$$
\frac {\mathrm{d}}{\mathrm{d} \theta} \left(\sin \theta \frac {\mathrm{d} \Theta}{\mathrm{d} \theta}\right) = - l (l + 1) \sin \theta \Theta\tag{3.60}
$$

就没有那没简单了。其解是以变量 $\cos \theta$ 表示的勒让德多项式（Legendre polynomials）

$$
\Theta (\theta) = P _ {l} (\cos \theta)\tag{3.61}
$$

$P_{l}(x)$ 最方便地可由罗德里格斯公式（Rodrigues formula）来定义：

$$
P _ {l} (x) = \frac {1}{2 ^ {l} l !} \left(\frac {\mathrm{d}}{\mathrm{d} x}\right) ^ {l} \left(x ^ {2} - 1\right) ^ {l}\tag{3.62}
$$

表 3.1 列出了前几个勒让德多项式。

表 3.1 勒让德多项式

<table><tr><td rowspan="6"></td><td> $P_0(x) = 1$ </td></tr><tr><td> $P_1(x) = x$ </td></tr><tr><td> $P_2(x) = (3x^2 - 1)/2$ </td></tr><tr><td> $P_3(x) = (5x^3 - 3x)/2$ </td></tr><tr><td> $P_4(x) = (35x^4 - 30x^2 + 3)/8$ </td></tr><tr><td> $P_5(x) = (63x^5 - 70x^3 + 15x)/8$ </td></tr></table>

请注意，（顾名思义） $P_{l}(x)$ 是 $x$ 的一个 $l$ 阶多项式；如果 $l$ 是偶数，它仅含有偶次幂；如果 $l$ 是奇数，它仅含有奇次幂。 $(1 / 2^{l}l!)$ 前面系数的选取是为了

$$
P _ {l} (1) = 1\tag{3.63}
$$

罗德里格斯公式显然仅适用于 $l$ 为非负的整数值。此外，它仅为我们提供一个解。但方程(3.60)是二阶微分方程，对 $l$ 的每个值，它应当有两个独立的解。事实证明，这些“其他解”在 $\theta = 0$ 和/或者 $\theta = \pi$ 时会发散，因此从物理角度来看它们是不可取的 $^{13}$ 。例如， $l = 0$ 的第二个解是

$$
\Theta (\theta) = \ln \left(\tan {\frac {\theta}{2}}\right)\tag{3.64}
$$

你可以自己验证一下是否满足方程 (3.60)。

在方位角对称的情况下，符合最低物理要求的拉普拉斯方程分离变量通解为

$$
V (r, \theta) = \left(A r ^ {l} + \frac {B}{r ^ {l + 1}}\right) P _ {l} (\cos \theta)
$$

[式 (3.61) 中不需要引进一个总常数，因为目前它可以包含在 $A$ 和 $B$ 中。] 如前所述，分离变量法会得到一组无限的解集，每个解对应于一个 $l$ 值。通解是这些分离变量解的线性组合：

$$
\boxed {V (r, \theta) = \sum_ {l = 0} ^ {\infty} \left(A _ {l} r ^ {l} + \frac {B _ {l}}{r ^ {l + 1}}\right) P _ {l} (\cos \theta)}\tag{3.65}
$$

以下的例题说明了这个结果的重要性。

例题 3.6 半径为 R 的空心球面上具有给定的电势 $V_{0}(\theta)$ 。求球内的电势。

[解答] 在这种情况下，对所有的 $l$ 有 $B_{l} = 0$ ；否则的话电势在原点发散。因此

$$
V (r, \theta) = \sum_ {l = 0} ^ {\infty} A _ {l} r ^ {l} P _ {l} (\cos \theta)\tag{3.66}
$$

在 $r = R$ 时，它必须与给定的势 $V_{0}(\theta)$ 相匹配：

$$
V (R, \theta) = \sum_ {l = 0} ^ {\infty} A _ {l} R ^ {l} P _ {l} (\cos \theta) = V _ {0} (\theta)\tag{3.67}
$$

适当选择系数 $A_{l}$ ，这个方程是否满足？是的：勒让德多项式（如正弦函数）构成 $-1 \leqslant x \leqslant 1 (0 \leqslant \theta \leqslant \pi)$ 区间上的一组函数完备集。我们如何确定这些系数呢？同样，通过傅里叶技巧来实现，因为勒让德多项式（如正弦）是正交函数 $^{14}$ ：

$$
\begin{array}{r} {{ \int_ {- 1} ^ {1} P _ {l} (x) P _ {l ^ {\prime}} (x) \mathrm{d} x = \int_ {0} ^ {\pi} P _ {l} (\cos \theta) P _ {l ^ {\prime}} (\cos \theta) \sin \theta \mathrm{d} \theta}} \\ {{= \left\{ \begin{array}{l l} {{0,}} & {{\text {如果} l \neq l ^ {\prime}}} \\ {{\frac {2}{2 l + 1},}} & {{\text {如果} l = l ^ {\prime}}} \end{array} \right.}} \end{array}\tag{3.68}
$$

因此，将式(3.67)乘以 $P_{l'}(\cos \theta)$ 并积分，我们得到

• • • •
• • • •
• • • •
• • • •
• • • •
• • • •

$$
A _ {l ^ {\prime}} R ^ {l ^ {\prime}} \frac {2}{2 l ^ {\prime} + 1} = \int_ {0} ^ {\pi} V _ {0} (\theta) P _ {l ^ {\prime}} (\cos \theta) \sin \theta \mathrm{d} \theta
$$

或者

$$
A _ {l} = \frac {2 l + 1}{2 R ^ {l}} \int_ {0} ^ {\pi} V _ {0} (\theta) P _ {l} (\cos \theta) \sin \theta \mathrm{d} \theta\tag{3.69}
$$

式 (3.66) 是我们问题的解，系数由式 (3.69) 给出。

解析上对式 (3.69) 计算积分可能很困难，在实际中，“凭肉眼”求解方程 (3.67) 通常更容易些 $^{15}$ 。例如，假设球面上的电势已给定：

$$
V _ {0} (\theta) = k \sin^ {2} (\theta / 2)\tag{3.70}
$$

其中 $k$ 是一个常数。使用半角公式，将其重写为

$$
V _ {0} (\theta) = \frac {k}{2} (1 - \cos \theta) = \frac {k}{2} \left[ P _ {0} (\cos \theta) - P _ {1} (\cos \theta) \right]
$$

将其代入式 (3.67)，我们直接得到 $A_0 = k / 2, A_1 = -k / (2R)$ ，其余的 $A_l$ 为零。因此

$$
V (r, \theta) = \frac {k}{2} \left[ r ^ {0} P _ {0} (\cos \theta) - \frac {r ^ {1}}{R} P _ {1} (\cos \theta) = \frac {k}{2} \left(1 - \frac {r}{R} \cos \theta\right) \right]\tag{3.71}
$$

例题3.7 再次指定 $V_{0}(\theta)$ 为半径为 $R$ 的球面上的电势，这次是在假设那里没有电荷的情况下，求球面外的电势。

[解答] 对这种情况下， $A_{l}$ 必须为零（否则 V 在 $\infty$ 处不会为零），因此

$$
V (r, \theta) = \sum_ {l = 0} ^ {\infty} \frac {B _ {l}}{r ^ {l + 1}} P _ {l} (\cos \theta)\tag{3.72}
$$

在球体的表面，我们要求

$$
V (R, \theta) = \sum_ {l = 0} ^ {\infty} \frac {B _ {l}}{R ^ {l + 1}} P _ {l} (\cos \theta) = V _ {0} (\theta)
$$

将该式乘以 $P_{l'}(\cos \theta)\sin \theta$ 并积分，再次利用正交关系式(3.68)得

$$
\frac {B _ {l ^ {\prime}}}{R ^ {l ^ {\prime} + 1}} \frac {2}{2 l ^ {\prime} + 1} = \int_ {0} ^ {\pi} V _ {0} (\theta) P _ {l ^ {\prime}} (\cos \theta) \sin \theta \mathrm{d} \theta
$$

或者

$$
B _ {l} = \frac {2 l + 1}{2} R ^ {l + 1} \int_ {0} ^ {\pi} V _ {0} (\theta) P _ {l} (\cos \theta) \sin \theta \mathrm{d} \theta\tag{3.73}
$$

式 (3.72) 就是我们问题的解，其系数是由式 (3.73) 给出。

例题3.8如图3.24所示，半径为 $R$ 不带电金属球放置在匀强电场 $\pmb {E} = E_0\hat{z}$ 中。该电场将把正电荷推到球体的“北部”表面，并对称地将负电荷推到“南部”表面。反过来，这种感应电荷将扭曲球面附近的电场。求球外区域的电势。

[解答] 球体是一个等势体——我们不妨设为零。然后，由对称性得，整个 $xy$ 平面的电势为零。不过，对本题的情况，在 $z \to \infty$ 时 $V$ 并不为零。事实上，在远离球体的地方，电场是 $E_0\hat{z}$ ，因此

$$
V \rightarrow - E _ {0} z + C
$$

由于在赤道面上 $V = 0$ ，常数 $C$ 必须为零。因此，该问题的边界条件是

$$
\left. \begin{array}{l l} {\mathrm{(i)}    \text {当}   r = R   \text {时},} & {V = 0} \\ {\mathrm{(ii)}    \text {当}   r \gg R   \text {时},} & {V \to - E _ {0} r \cos \theta} \end{array} \right\}\tag{3.74}
$$

我们必须用式 $(3.65)$ 形式的函数来满足这些边界条件。

第一个边界条件给出

$$
A _ {l} R ^ {l} + \frac {B _ {l}}{R ^ {l + 1}} = 0
$$

或者

$$
B _ {l} = - A _ {l} R ^ {2 l + 1}\tag{3.75}
$$

所以

$$
V (r, \theta) = \sum_ {l = 0} ^ {\infty} A _ {l} \left(r ^ {l} - \frac {R ^ {2 l + 1}}{r ^ {l + 1}}\right) P _ {l} (\cos \theta)
$$

![](images/405eb72d018d9100b899310262e4f3c7ae4565c5563fe7c2ee9eb7d19b4ccd5b.jpg)  
图3.24

对于 $r \gg R$ ，括号中的第二项可以忽略不计，因此边界条件（ii）要求

$$
\sum_ {l = 0} ^ {\infty} A _ {l} r ^ {l} P _ {l} (\cos \theta) = - E _ {0} r \cos \theta
$$

显然，只有 $l = 1$ 项存在。事实上，由于 $P_{1}(\cos \theta) = \cos \theta$ ，我们立即可以得到 $A_{1} = -E_{0}$ ，其余的 $A_{l}$ 为零

结论：

$$
V (r, \theta) = - E _ {0} \left(r - \frac {R ^ {3}}{r ^ {2}}\right) \cos \theta\tag{3.76}
$$

第一项 $(-E_0r\cos \theta)$ 是由外场引起的：感应电荷的贡献是

$$
E _ {0} \frac {R ^ {3}}{r ^ {2}} \cos \theta
$$

如果你想知道感应电荷密度，可以用通常的方法计算：

$$
\sigma (\theta) = - \left. \varepsilon_ {0} \frac {\partial V}{\partial r} \right| _ {r = R} = \varepsilon_ {0} E _ {0} \left(1 + 2 \frac {R ^ {3}}{r ^ {3}}\right) \cos \theta \bigg | _ {r = R} = 3 \varepsilon_ {0} E _ {0} \cos \theta\tag{3.77}
$$

正如预期的那样，它在“北半球” $(0 < \theta < \pi / 2)$ 是正的，在“南半球” $(\pi / 2 < \theta < \pi)$ 是负的。

例题3.9 半径为 $R$ 的球壳表面上涂有给定的面电荷密度 $\sigma_0(\theta)$ 。求球壳内外的电势。[解答] 当然，你可以通过直接积分来求解：

$$
V = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\sigma_ {0}}{\nu} \mathrm{d} a
$$

但分离变量法通常更容易。对于内部区域有

$$
V (r, \theta) = \sum_ {l = 0} ^ {\infty} A _ {l} r ^ {l} P _ {l} (\cos \theta) \quad (r \leqslant R)\tag{3.78}
$$

(没有 $B_{l}$ 项——它们在原点处发散); 在外部区域

$$
V (r, \theta) = \sum_ {l = 0} ^ {\infty} \frac {B _ {l}}{r ^ {l + 1}} P _ {l} (\cos \theta) \quad (r \geqslant R)\tag{3.79}
$$

（没有 $A_{l}$ 项——它们在无穷远处不为零）。这两个函数必须通过表面本身的适当边界条件连接在一起。首先，电势在 $(r = R)$ 是连续的[式(2.34)]：

$$
\sum_ {l = 0} ^ {\infty} A _ {l} R ^ {l} P _ {l} (\cos \theta) = \sum_ {l = 0} ^ {\infty} \frac {B _ {l}}{R ^ {l + 1}} P _ {l} (\cos \theta)\tag{3.80}
$$

由此可见，两边同幂次的勒让德多项式的系数相等：

$$
B _ {l} = A _ {l} R ^ {2 l + 1}\tag{3.81}
$$

[要正式证明这一点，将式(3.80)的两边同乘以 $P_{\nu}(\cos \theta)\sin \theta$ ，从0到 $\pi$ 积分，并利用正交关系式(3.68)。]其次，在球面上 $V$ 的径向导数存在不连续[式(2.36)]：

$$
\left(\frac {\partial V _ {\mathrm{out}}}{\partial r} - \frac {\partial V _ {\mathrm{in}}}{\partial r}\right) \bigg | _ {r = R} = - \frac {1}{\varepsilon_ {0}} \sigma_ {0} (\theta)\tag{3.82}
$$

即

$$
- \sum_ {l = 0} ^ {\infty} (l + 1) \frac {B _ {l}}{R ^ {l + 2}} P _ {l} (\cos \theta) - \sum_ {l = 0} ^ {\infty} l A _ {l} R ^ {l - 1} P _ {l} (\cos \theta) = - \frac {1}{\varepsilon_ {0}} \sigma_ {0} (\theta)
$$

或者利用式 (3.81):

$$
\sum_ {l = 0} ^ {\infty} (2 l + 1) A _ {l} R ^ {l - 1} P _ {l} (\cos \theta) = \frac {1}{\varepsilon_ {0}} \sigma_ {0} (\theta)\tag{3.83}
$$

从这里开始，可以使用傅里叶技巧来确定系数：

$$
A _ {l} = \frac {1}{2 \varepsilon_ {0} R ^ {l - 1}} \int_ {0} ^ {\pi} \sigma_ {0} (\theta) P _ {l} (\cos \theta) \sin \theta \mathrm{d} \theta\tag{3.84}
$$

式 (3.78) 和式 (3.79) 组成我们问题的解，系数由式 (3.81) 和式 (3.84) 给出。例如，如果对于某个常数

$$
\sigma_ {0} (\theta) = k \cos \theta = k P _ {1} (\cos \theta)\tag{3.85}
$$

则除 $l = 1$ 外，其余所有 $A_{l}$ 均为零，

$$
A _ {1} = \frac {k}{2 \varepsilon_ {0}} \int_ {0} ^ {\pi} [ P _ {1} (\cos \theta) ] ^ {2} \sin \theta \mathrm{d} \theta = \frac {k}{3 \varepsilon_ {0}}
$$

因此，球体内部的电势为

$$
V (r, \theta) = \frac {k}{3 \varepsilon_ {0}} r \cos \theta \quad (r \leqslant R)\tag{3.86}
$$

而在球体之外的电势为

$$
V (r, \theta) = \frac {k R ^ {3}}{3 \varepsilon_ {0}} \frac {1}{r ^ {2}} \cos \theta \quad (r \geqslant R)\tag{3.87}
$$

特别是，如果 $\sigma_0(\theta)$ 是外场 $E_0\hat{z}$ 在金属球面上的感应电荷，则 $k = 3\varepsilon_0E_0$ [式(3.77)]，则内部的电势为 $E_0r\cos \theta = E_0z$ ，电场为 $-E_0\hat{z}$ ——这恰好抵消了外场，这是理所当然的。在球体外，感应电荷产生的电势为

$$
E _ {0} \frac {R ^ {3}}{r ^ {2}} \cos \theta
$$

这与我们在例题 3.8 中的结论一致。

习题3.17 从罗德里格斯公式[式(3.62)]推导出 $P_{3}(x)$ ，并验证 $P_{3}(\cos \theta)$ 是否满足 $l = 3$ 的角方程[式(3.60)]。通过直接积分验证 $P_{3}$ 与 $P_{1}$ 是否正交。

习题3.18

（a）假设球体表面上的电势为常数 $V_{0}$ 。利用例题3.6和3.7的结果求球体内外的电势。（当然，你们提前已经知道答案，这仅是为了验证方法的一致性。）

（b）利用例题3.9的结果，求均匀的带有电荷密度 $\sigma_0$ 的球壳内外的电势。

习题3.19 球体表面（半径为 $R$ ）的电势由下式给出：

$$
V _ {0} = k \cos 3 \theta
$$

其中 $k$ 是常数。求球体内外的电势以及球体上的表面电荷密度 $\sigma (\theta)$ 。（假设球体内外都没有电荷。）

习题3.20 假设球体表面上的电势 $V_{0}(\theta)$ 是给定的，且球体内外都没有电荷。证明球体上的电荷密度为

$$
\sigma (\theta) = \frac {\varepsilon_ {0}}{2 R} \sum_ {l = 0} ^ {\infty} (2 l + 1) ^ {2} C _ {l} P _ {l} (\cos \theta)\tag{3.88}
$$

其中

$$
C _ {l} = \int_ {0} ^ {\pi} V _ {0} (\theta) P _ {l} (\cos \theta) \sin \theta \mathrm{d} \theta\tag{3.89}
$$

习题 3.21 求放置在均匀电场中的带电金属球（电荷 Q，半径 R）外部的电势。解释清楚在哪里选取电势的零点。

习题3.22 在习题2.25中，你知道了均匀带电圆盘轴线上的电势：

$$
V (r, 0) = \frac {\sigma}{2 \varepsilon_ {0}} \left(\sqrt {r ^ {2} + R ^ {2}} - r\right)
$$

(a) 利用这个结果以及结合 $P_{l}(1) = 1$ 的事实，计算圆盘上离开轴点处的电势展开式[式(3.72)]中的前三项，假设 $r \gg R$ 。

(b) 使用式 (3.66)，通过同样的方法求 $r < R$ 的电势。[提示：你必须将内部区域分成两个半球，即圆盘的上方和下方。在两个半球中系数 $A_{l}$ 不能假设是相同的。]

习题3.23 半径为 $R$ 的球壳在“北”半球上带有均匀的表面电荷密度 $\sigma_0$ ，在“南”半球带有均匀的表面电荷密度 $-\sigma_0$ 。求球壳内外的电势，计算具体系数直到 $A_{6}$ 和 $B_{6}$ 。

\- 习题3.24 在柱坐标系中，通过分离变量法求解拉普拉斯方程，假设解与 $z$ 无关（圆柱对称性）。[确保你求出了径向方程的所有解。尤其是，你的结果中必须包含无限长线电荷分布的情况，（当然）对此情况我们已经知道了答案。]

习题3.25 半径为 $R$ 的无限长金属管与匀强电场 $\pmb{E}_0$ 垂直放置。求管外部的电势以及管上感应的表面电荷。[利用习题3.24中的结论。]

习题3.26 电荷密度

$$
\sigma (\phi) = a \sin 5 \phi
$$

(其中 $a$ 是常数) 涂在半径为 $R$ 的无限长圆柱体表面上 (图3.25)。求圆柱体内外的电势。[利用习题3.24中的结论。]

![](images/4ad5851bba2dc0253cea8d8cb14e8715539b72fc4277ccc8847e9c922e3687d1.jpg)  
图3.25

## 3.4 多极矩展开

## 3.4.1 远距离近似电势

当你距一个局域电荷分布很远时，它“看起来”就像一个点电荷，它的电势可以很好地近似为 $(1/4\pi\varepsilon_{0})Q/r$ ，其中Q是总电荷。我们经常用它来检验V的公式是否正确。但如果Q为零会是怎样呢？你可能会回答说，电势近似为零；当然，从某种意义上说，你是对的（即便Q不为零，在很远处的电势的确很小）。但我们希望探寻比这更多的信息。

例题3.10 物理上电偶极子（electric dipole）是由两个相距为 $d$ 、所带电量相等但符号相反的电荷组成的。求远离电偶极子的点的近似电势。

[解答] 设 $\lambda_{-}$ 为所求电势点到 -q 的距离， $\lambda_{+}$ 为点到 +q 的距离（图 3.26）。则有

$$
V (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \left(\frac {q}{\eta_ {+}} - \frac {q}{\eta_ {-}}\right)
$$

以及（由余弦定理）

$$
\mathcal {I} _ {\pm} ^ {2} = r ^ {2} + (d / 2) ^ {2} \mp r d \cos \theta = r ^ {2} \left(1 \mp \frac {d}{r} \cos \theta + \frac {d ^ {2}}{4 r ^ {2}}\right)
$$

我们对 $r \gg d$ 的区域感兴趣，所以忽略第三项，由二项式展开式得出

$$
\frac {1}{r _ {\pm}} \cong \frac {1}{r} \left(1 \mp \frac {d}{r} \cos \theta\right) ^ {- 1 / 2} \cong \frac {1}{r} \left(1 \pm \frac {d}{2 r} \cos \theta\right)
$$

所以

$$
\frac {1}{r _ {+}} - \frac {1}{r _ {-}} \cong \frac {d}{r ^ {2}} \cos \theta
$$

因此

$$
V (\boldsymbol {r}) \cong \frac {1}{4 \pi \varepsilon_ {0}} \frac {q d \cos \theta}{r ^ {2}}\tag{3.90}
$$

当 r 较大时，电偶极子的电势按照 $1/r^{2}$ 减小；正如我们预见的那样，它比点电荷的电势减小得更快。如果我们把一对相同的电偶极子反向放在一起构成一个四极子（quadrupole），则电势按 $1/r^{3}$ 减小；对背靠背的四极子（八极子，octopole）的电势按 $1/r^{4}$ 减小，等等。图 3.27 总结了这一层次结构；为完整起见，我也包括了单极子（monopole，点电荷），当然它的电势是按 1/r 减小的。

![](images/719b99b348b41f7a210667d5bbee8d056c4948cd0537874927fef99b7ba2b7ff.jpg)  
图3.27

例题3.10适用于一种非常特殊的电荷分布情况。借助 $1 / r$ 幂函数，我现在发展一种适用于任意局域电荷分布的电势的系统展开方法。图3.28定义了相关变量；在 $\pmb{r}$ 点处的电势为

$$
V (\pmb {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {1}{\eta} \rho (\pmb {r} ^ {\prime}) \mathrm{d} \tau^ {\prime}\tag{3.91}
$$

![](images/1161a3afe55d4eeae0bb304352cfab10ed49cfdebef558d95205068b30d9745b.jpg)  
图3.28

利用余弦定理

$$
\nu^ {2} = r ^ {2} + (r ^ {\prime}) ^ {2} - 2 r r ^ {\prime} \cos \alpha = r ^ {2} \left[ 1 + \left(\frac {r ^ {\prime}}{r}\right) ^ {2} - 2 \left(\frac {r ^ {\prime}}{r}\right) \cos \alpha \right]
$$

其中 $\alpha$ 是 $r$ 和 $r'$ 之间的夹角，因此

$$
r = r \sqrt {1 + \varepsilon}\tag{3.92}
$$

式中

$$
\varepsilon \equiv \left(\frac {r ^ {\prime}}{r}\right) \left(\frac {r ^ {\prime}}{r} - 2 \cos \alpha\right)
$$

对于电荷分布区域以外的点， $\varepsilon$ 的值远小于 1，利用二项式展开：

$$
\frac {1}{r} = \frac {1}{r} (1 + \varepsilon) ^ {- 1 / 2} = \frac {1}{r} \left(1 - \frac {1}{2} \varepsilon + \frac {3}{8} \varepsilon^ {2} - \frac {5}{1 6} \varepsilon^ {3} + \dots\right)\tag{3.93}
$$

或者用 $r, r'$ 和 $\alpha$ 表示：

$$
\begin{array}{r l} \frac {1}{2} & = \frac {1}{r} \left[ 1 - \frac {1}{2} \left(\frac {r ^ {\prime}}{r}\right) \left(\frac {r ^ {\prime}}{r} - 2 \cos \alpha\right) + \frac {3}{8} \left(\frac {r ^ {\prime}}{r}\right) ^ {2} \left(\frac {r ^ {\prime}}{r} - 2 \cos \alpha\right) ^ {2} - \right. \\ & \left. \frac {5}{1 6} \left(\frac {r ^ {\prime}}{r}\right) ^ {3} \left(\frac {r ^ {\prime}}{r} - 2 \cos \alpha\right) ^ {3} + \dots \right] \\ & = \frac {1}{r} \left[ 1 + \left(\frac {r ^ {\prime}}{r}\right) \cos \alpha + \left(\frac {r ^ {\prime}}{r}\right) ^ {2} \left(\frac {3 \cos^ {2} \alpha - 1}{2}\right) + \right. \\ & \left. \left(\frac {r ^ {\prime}}{r}\right) ^ {3} \left(\frac {5 \cos^ {3} \alpha - 3 \cos \alpha}{2}\right) + \dots \right] \end{array}
$$

在最后一步中，我按 $(r'/r)$ 的幂次进行集项：令人惊讶的是，它们的系数（括号中的项）是勒让德多项式！值得注意的结果是 $^{16}$

$$
\frac {1}{r} = \frac {1}{r} \sum_ {n = 0} ^ {\infty} \left(\frac {r ^ {\prime}}{r}\right) ^ {n} P _ {n} (\cos \alpha)\tag{3.94}
$$

将该式代回到式 (3.91) 中，并注意到就积分而言， $r$ 是个常数；我的结论是

$$
\boxed {V (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \sum_ {n = 0} ^ {\infty} \frac {1}{r ^ {(n + 1)}} \int \left(r ^ {\prime}\right) ^ {n} P _ {n} (\cos \alpha) \rho \left(\boldsymbol {r} ^ {\prime}\right) \mathrm{d} \tau^ {\prime}}\tag{3.95}
$$

或者，更明确地讲，

$$
\begin{array}{c} {{V (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \left[ \frac {1}{r} \int \rho (\boldsymbol {r} ^ {\prime}) \mathrm{d} \tau^ {\prime} + \frac {1}{r ^ {2}} \int r ^ {\prime} \cos \alpha \rho (\boldsymbol {r} ^ {\prime}) \mathrm{d} \tau^ {\prime} + \right.}} \\ {{\left. \frac {1}{r ^ {3}} \int (r ^ {\prime}) ^ {2} \left(\frac {3}{2} \cos^ {2} \alpha - \frac {1}{2}\right) \rho (\boldsymbol {r} ^ {\prime}) \mathrm{d} \tau^ {\prime} + \dots \right]}} \end{array}\tag{3.96}
$$

这就是期望的结果——V 按 1/r 幂次的多极展开。第一项 $(n=0)$ 是单极的贡献（按照 1/r 减小）；第二项 $(n=1)$ 是偶极贡献（按 $1/r^{2}$ 减小）；第三项是四极矩贡献；第四项是八极矩贡献，等等。请记住 $\alpha$ 是 r 和 $r'$ 之间的夹角，所以积分取决于到场点的方向。如果你对 $z'$ 轴上的电势感兴趣（或者换句话说，如果你调整坐标 $r'$ ，使 $z'$ 轴沿着 r），那么 $\alpha$ 就是通常的极角 $\theta'$ 。

就目前情况而言，式(3.95)是精确的，但它主要用于近似计算；展开式中最低阶的非零项给出了在大 $r$ 情况下近似势的值；如果需要更高的精度，后面的项告诉我们如何改进近似。

习题3.27 球心位于原点、半径为 $R$ 的球具有电荷密度

$$
\rho (r, \theta) = k \frac {R}{r ^ {2}} (R - 2 r) \sin \theta
$$

其中 k 是常数， $r, \theta$ 是通常的球坐标。求 z 轴上远离球体位点的近似电势。

习题 3.28 在 xy 平面内（半径 R，以原点为中心）的圆环带有均匀的线电荷密度 $\lambda$ 。在 $V(r, \theta)$ 的多极展开式中求出前三项。

## 3.4.2 单极项和偶极项

一般而言，多极展开中的主要贡献来自于单极项（在 $r$ 较大时）：

$$
V _ {\text {单极}} (\pmb {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \frac {Q}{r}\tag{3.97}
$$

式中， $Q=\int\rho\mathrm{d}\tau$ 是整个分布的总电荷。这正是在远离电荷情况下我们所期望的近似电势。对于位于原点处的点电荷， $V_{mon}$ 不仅仅是大r情况下的一级近似，它就是严格电势值；在这种情况下，所有高阶的多极展开项都为零。

如果总电荷为零，对电势的主要贡献是偶极项（当然，除非它也为零）：

$$
V _ {\text {偶极}} (\pmb {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \frac {1}{r ^ {2}} \int r ^ {\prime} \cos \alpha \rho (\pmb {r} ^ {\prime}) \mathrm{d} \tau^ {\prime}
$$

由于 $\alpha$ 是 r 与 $r'$ 之间的夹角（图 3.28），

$$
r ^ {\prime} \cos \alpha = \hat {r} \cdot r ^ {\prime}
$$

偶极势可以写得更为简洁：

$$
V _ {\mathrm{偶极}} (\pmb {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \frac {1}{r ^ {2}} \hat {\pmb {r}} \cdot \int \pmb {r} ^ {\prime} \rho (\pmb {r} ^ {\prime}) \mathrm{d} \tau^ {\prime}
$$

式中，积分部分（与 r 无关），称为电荷分布的偶极矩（dipole moment）。

$$
\boxed {p \equiv \int r ^ {\prime} \rho (r ^ {\prime}) \mathrm{d} \tau^ {\prime}}\tag{3.98}
$$

偶极子对电势的贡献可以简化为

$$
\boxed {V _ {\text {偶极}} (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \frac {\boldsymbol {p} \cdot \hat {\boldsymbol {r}}}{r ^ {2}}}\tag{3.99}
$$

偶极矩是由电荷分布的几何形状（尺寸、形状和密度）所决定的。对式(3.98)可按通常的方式转换成点电荷、线电荷和面电荷分布情况（见2.1.4节）。因此，点电荷集合的偶极矩为

$$
\boldsymbol {p} = \sum_ {i = 1} ^ {n} q _ {i} \boldsymbol {r} _ {i} ^ {\prime}\tag{3.100}
$$

对于客观存在的偶极子（大小相等、符号相反的电荷， $\pm q$ ）

$$
\boldsymbol {p} = q \boldsymbol {r} _ {+} ^ {\prime} - q \boldsymbol {r} _ {-} ^ {\prime} = q (\boldsymbol {r} _ {+} ^ {\prime} - \boldsymbol {r} _ {-} ^ {\prime}) = q \boldsymbol {d}\tag{3.101}
$$

其中 d 是从负电荷到正电荷的位置矢量（图 3.29）。

![](images/751cee649cbed57bf924aeb0293cfffa2371bafba9bc14040c398d6e08ed77e4.jpg)  
图3.29

这与我们在例题 3.10 中得到的结果一致吗？是一致的：如果你将式 (3.101) 代入式 (3.99)，则可以复原式 (3.90)。不过，请注意这仅是偶极子的近似势——显然还有更高的多极项的贡献。当然，随着你走得越来越远，由于高阶项随着 r 的增加而迅速衰减掉， $V_{偶极}$ 成为越来越好的近似。出于同样的原因，在 r 固定的情况下，随着间距 d 的减小，偶极近似也会得到改善。要构造一个电势完全由式 (3.99) 给出的“理想”偶极子 [perfect (point) dipole]，你必须让 d 接近零。遗憾的是，你也会失去偶极项，除非你能同时让 q 变为无穷大！在绝对的人为极限 $d \rightarrow 0, q \rightarrow \infty$ ，并且乘积 qd = p 保持不变的情况下，物理偶极子成为纯粹偶极子。当有人使用“偶极子”这个词时，你并不总是能分辨出他们指的是物理偶极子（电荷之间有一定的距离）还是理想的（点）偶极子。如果有疑问，假定 d 足够小（与 r 相比），这样你可以放心地应用式 (3.99)。

偶极矩是矢量，它们遵从相应的矢量加法：如果有两个偶极子，偶极矩分别为 $p_1$ 和 $p_2$ 则总偶极矩是 $p_1 + p_2$ 。例如，如图3.30所示的正方形四个角分别有四个电荷，其净的偶极矩为零。你可以通过将电荷结合成对（竖直方向上， $\downarrow + \uparrow = 0$ ，水平方向上， $\rightarrow + \leftarrow = 0$ ）或者利用式(3.100)将四个电荷的贡献单独加在一起的方式来明白这一点。正如我之前指出的那样，这是一个四极子，它的电势由多极矩展开中的四极矩项所决定。

![](images/d63224bb238bd1c7a19ecb2eda12482cbb8c8ad487dc756e68f3eac339b85ae7.jpg)  
图3.30

习题3.29 四个粒子（一个带电荷 $q$ ，一个带电荷为 $3q$ ，另两个带电荷为 $-2q$ ）放置在如图3.31所示的位置，每个粒子与原点距离都为 $a$ 。求在远离原点位置的某处电势的近似表达式。（用球坐标表示你的答案。）

![](images/3857a1eb8be4821e3e6f4a6b3acaf13b3cbe89caef758f7acbbeba97aa69e10e.jpg)  
图3.31

习题3.30 在例题3.9中，我们推导出了半径为 $R$ 、表面电荷密度为 $\sigma = k\cos \theta$ 的球壳的精确势。

(a) 计算该电荷分布的偶极矩。

(b) 求在远离球壳的点上的近似电势，并与精确解 [式 (3.87)] 做比较。关于更高的多极子，你能得出什么样的结论？

习题3.31 对例题3.10中的偶极子，将 $1 / \lambda_{\pm}$ 展开到 $(d / r)^{3}$ 阶，并利用它来确定势中的四极矩和八极矩项。

## 3.4.3 多极展开中的坐标原点

我之前提到过，位于原点处的点电荷构成一个“纯”单极子。如果它不在原点，就不再是纯的单极子。例如，图3.32中的电荷具有偶极矩 $p=qd\hat{y}$ ，其电势中有相应的偶极项。单极电势 $(1/4\pi\varepsilon_{0})q/r$ 对这个几何构型并不完全正确；确切的电势是 $(1/4\pi\varepsilon_{0})q/r$ 。请记住，多极展开是r（到原点的距离）的系列逆幂级数。当我们展开 $1/r$ 时，我们得到了所有的幂次项，而不仅仅是第一个幂级数。

![](images/c1350951174b5e8001e93394c35a943ff64cdf35719282fc00be6f29382bce36.jpg)  
图3.32

因此，移动原点（或者，移动电荷）可以完全改变多极展开。显然，由于总电荷与坐标系无关，单极矩 $Q$ 并不发生改变。（在图3.32中，当我们把 $q$ 从原点移开时，单极矩项不受影响——只是它现在不再是事情的全貌：偶极项——以及所有更高的极矩项——也都会出现了。）通常，当你移动原点时，偶极矩确实会发生变化，但有一个特例：如果总电荷为零，那么偶极矩与原点的选择无关。假设我们将原点移动了位移 $\pmb{a}$ （图3.33）。新的偶极矩为

$$
\bar {\boldsymbol {p}} = \int \bar {\boldsymbol {r}} ^ {\prime} \rho (\boldsymbol {r} ^ {\prime}) \mathrm{d} \tau^ {\prime} = \int (\boldsymbol {r} ^ {\prime} - \boldsymbol {a}) \rho (\boldsymbol {r} ^ {\prime}) \mathrm{d} \tau^ {\prime}
$$

$$
= \int \boldsymbol {r} ^ {\prime} \rho (\boldsymbol {r} ^ {\prime}) \mathrm{d} \tau^ {\prime} - \boldsymbol {a} \int \rho (\boldsymbol {r} ^ {\prime}) \mathrm{d} \tau^ {\prime} = \boldsymbol {p} - \boldsymbol {a} Q
$$

特别是，如果 $Q = 0$ ，则 $\bar{p} = p$ 。所以，如果有人问图3.34a中的偶极矩是多少，你可以确定地回答“ $qd$ ”，但如果问你图3.34b中的偶极矩是多少，合适的回答应为“你指的是原点选在哪里？”

![](images/a418eef20eacf4f0c20f1aba9f124f5d1f53a7d39a2b8d25d9a8fb96dc120102.jpg)  
图3.33

![](images/f265f9c4fe05c10f1fb63e4c64b770cbeb499ecb80db74f74206d69a051d551b.jpg)  
a)

![](images/d77ee18eac78ba0ee536e2a035f477d1f14d8b1f414526350bb2e6762e6ac2e0.jpg)  
b)  
图3.34

习题3.32 两个点电荷 $3q$ 和 $-q$ 相距为 $a$ ，对于图3.35中所示的每种排列；求（i）单极矩，（ii）偶极矩，（iii）大 $r$ 情况下的近似势（在球坐标系中）（包括单极和偶极的贡献）。

![](images/eb510a90913241467dfb19ca677733c3a65b4cfcd2bfbd47edb86884ae0e06a4.jpg)  
a)

![](images/81f0623402022531ca3ed98014f8ed0a61f8d1996a26b5b91d3667b1b4bebabe.jpg)  
b)  
图3.35

![](images/223ff2febeee9ee8428a81671dde0dfe3bc22f5697a9f2201f91185262723389.jpg)  
c)

## 3.4.4 偶极子的电场

到目前为止，我们只研究了电势。现在我想计算（理想）偶极子的电场。如果我们选择坐标系使得 p 位于原点并指向 z 轴方向（图 3.36），则在点 $(r, \theta)$ 处的电势为 [式 (3.99)]

$$
V _ {\text {偶极}} (r, \theta) = \frac {\hat {\pmb {r}} \cdot \pmb {p}}{4 \pi \varepsilon_ {0} r ^ {2}} = \frac {p \cos \theta}{4 \pi \varepsilon_ {0} r ^ {2}}\tag{3.102}
$$

为得到该电场的大小，我们取 V 的负梯度：

$$
E _ {r} = - \frac {\partial V}{\partial r} = \frac {2 p \cos \theta}{4 \pi \varepsilon_ {0} r ^ {3}}
$$

$$
E _ {\theta} = - \frac {1}{r} \frac {\partial V}{\partial \theta} = \frac {p \sin \theta}{4 \pi \varepsilon_ {0} r ^ {3}}
$$

$$
E _ {\phi} = - \frac {1}{r \sin \theta} \frac {\partial V}{\partial \phi} = 0
$$

所以

$$
\boxed {E _ {\text {偶极}} (r, \theta) = \frac {p}{4 \pi \varepsilon_ {0} r ^ {3}} (2 \cos \theta \hat {\boldsymbol {r}} + \sin \theta \hat {\boldsymbol {\theta}})}\tag{3.103}
$$

该表达式明确指定了所用的坐标系（球坐标系），并假设 p 具有特定的方向（沿 z 方向）。它也可以用不指定坐标系的形式重新表述出来——类似于式 (3.99) 中的电势，见习题 3.36。

![](images/d3d8faa728a40e7724bb58e289c187989372c20411678bf6ec56aca646e6dbd7.jpg)  
图3.36

请注意，偶极矩场随 $1 / r^3$ 衰减；当然，单极场 $(Q / 4\pi \varepsilon_0r^2)\hat{r}$ 按 $1 / r^2$ 衰减。四极矩的场按 $1 / r^4$ 衰减，八极矩场按 $1 / r^5$ 衰减，等等。（这仅仅反映了单极势按 $1 / r$ 下降，偶极势按 $1 / r^2$ 下降，四极矩势按 $1 / r^3$ ，等等——梯度引入了另外一个 $1 / r$ 因子。）

图 3.37a 给出了“纯”偶极子的电场线 [式 (3.103)]。为了进行比较，我还绘制了“实际的”偶极子的电场线，如图 3.37 所示。请注意，如果你遮住中心区域，这两个图会变得非常相似；然而，近距离观察它们是完全不同的。只有对于 $r \gg d$ 的点，式 (3.103) 才表示物理偶极子场的有效近似。正如我之前提到的那样，这种情况可以通过取较大 r 或者让两点电荷靠得非常近来实现 $^{17}$ 。

![](images/11a08964d0654a3cd00f10c4dc98e88beb43d4ca57c0d6a485ce87f591372e83.jpg)  
a) “纯”偶极子的场

![](images/84647d98feef9f2fbec32e92ff8117a887bade5b2975e2350095543ae160668c.jpg)  
b) “物理”偶极子的场  
图3.37

习题3.33 一个“纯”偶极子 $\pmb{p}$ 位于原点，指向 $z$ 方向。

(a) 作用在位于 $(a,0,0)$ （直角坐标系）的点电荷 $q$ 上的力是多少？

(b) 作用在位于 $(0,0,a)$ 的点电荷 $q$ 上的力是多少？

(c) 把点电荷 q 从点 $(a,0,0)$ 移至点 $(0,0,a)$ 所需要做的功为多少?

习题3.34 三个点电荷的位置如图3.38所示，每个点电荷距原点的距离为 $a$ 。求远离原点处的近似电场。将你的结果在球坐标中表示出来，并在多极展开中保留两个最低阶。

![](images/ccdedb1cdfc7edea24b3e118dff29378ac9c36f9fbabf4cb4f220815cf7ceec0.jpg)  
图3.38

习题3.35 半径为 $R$ 的实心球体以原点为中心。“北”半球具有均匀的电荷密度 $\rho_0$ ，“南”半球具有均匀的电荷密度 $-\rho_0$ 。求远离球体（ $r \gg R$ ）的点处的近似电场 $\pmb{E}(r, \theta)$ 。

习题3.36 证明（纯）偶极子的电场[式(3.103)]可以写成不含坐标系的形式

$$
\boxed {E _ {\text {偶极}} (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \frac {1}{r ^ {3}} [ 3 (\boldsymbol {p} \cdot \hat {\boldsymbol {r}}) \hat {\boldsymbol {r}} - \boldsymbol {p} ]}\tag{3.104}
$$

## 第3章补充习题

习题3.37 在第3.1.4节中，我已经证明：在没有电荷分布区域中的任何一点 $P$ 的静电势等于其在以 $P$ 为中心的任意球面（半径为 $R$ ）上的平均值。这里有一个不依赖库仑定律，只依赖拉普拉斯方程的另一个论点。我们不妨将原点设在 $P$ 点。设 $V_{\text{平均}}(R)$ 为平均值；首先证明

$$
\frac {\mathrm{d} V _ {\text {平均}}}{\mathrm{d} R} = \frac {1}{4 \pi R ^ {2}} \oint \nabla V \cdot \mathrm{d} a
$$

（请注意 da 中的 $R^{2}$ 抵消了前面的 $1/R^{2}$ ，因此 V 本身仅与 R 有关。）现在使用散度定理，并得出结论：如果 V 满足拉普拉斯方程，那么对于所有 R，有 $V_{\text{平均}}(R) = V_{\text{平均}}(0) = V_{\text{平均}}(P)^{18}$ 。

习题 3.38 这是式 (3.10) 的另一种推导（由距离平面上方为 d 的点电荷 q 在接地导电平面上感应的表面电荷密度）。这种方法 $^{19}$ （推广到许多其他问题）不依赖于镜像法。总的电场部分归因于 q，部分归因于表面感应电荷。以 q 和表面下方未知的 $\sigma(x, y)$ 表示出这些场的 z 分量。当然，因为这是在导体内部，总的电荷之和必须为零。由此来确定 $\sigma$ 。

习题3.39 两个无限长的平行接地导电平面相距为 $a$ 。点电荷 $q$ 位于两平面之间，距其中一个平面距离为 $x$ 。求 $q$ 的受力 $^{20}$ 。对于 $a \to \infty$ 和 $x = a / 2$ 的特殊情况，验证所得结果是否正确。

习题3.40 两长直线分别带有符号相反的均匀分布线电荷 $\pm \lambda$ ，放置在一长导电圆柱体的两侧（图3.39）。圆柱体（净电荷为零）的半径为 $R$ ，两长直线与圆柱体轴线的距离均为 $a$ 。求空间的电势。

$$
\left[ \mathrm{答案}: V (s, \phi) = \frac {\lambda}{4 \pi \varepsilon_ {0}} \ln \left\{\frac {(s ^ {2} + a ^ {2} + 2 s a \cos \phi) [ (s a / R) ^ {2} + R ^ {2} - 2 s a \cos \phi ]}{(s ^ {2} + a ^ {2} - 2 s a \cos \phi) [ (s a / R) ^ {2} + R ^ {2} + 2 s a \cos \phi ]} \right\} \right]
$$

![](images/145c26db8468205f485d37e58b1b9bc613e5c3695e22869fc3c646ccf042f235.jpg)  
图3.39

习题 3.41 巴克明斯特富勒烯是一种由 60 个碳原子组成的分子，其排列方式类似于足球上的缝合线。它可以近似看成半径 $R=3.5\AA$ 的导电球壳。按照习题 3.9，附近的电子会被吸引，因此离子 $C_{60}^{-}$ 的存在并不奇怪。（想象一下，平均而言电子会均匀地涂抹在表面上。）但第二个电子如何呢？很明显，在很远的地方，它会被离子排斥，但它在一定距离 r（距离中心）时，合力变为零，比这更近的地方则会被吸引。因此，一个有足够能量的电子进入如此近的距离应该和富勒烯结合在一起。

(a) 求 $r$ ，单位为 $\mathring{\mathrm{A}}$ 。[你必须采用数值求解。]

(b) 将一个电子（从无穷远）移至 r 点需要多少能量（以电子伏特为单位）?

[顺便说一句，已经观察到 $\mathrm{C}_{60}^{-}$ 离子。]21

习题 3.42 你可以使用叠加原理来组合变量分离获得的解。例如，在习题 3.16 中，如果五个面接地，第六个面处于恒定的电势 $V_{0}$ ，就可以求得立方体内的电势；若六个表面保持特定的恒定电压 $V_{1}, V_{2}, \cdots, V_{6}$ ，通过 6 次结果的叠加，你可以获得立方体内部的电势。按照这种方法，使用例题 3.4 和习题 3.15 的结果，求矩形管内的电势，矩形管两个相对侧面 $(x = \pm b)$ 的电势为 $V_{0}$ ，第三个面 $(y = a)$ 的电势为 $V_{1}$ ，最后一个面 $(y = 0)$ 接地。

习题3.43 半径为 $a$ 、电势为 $V_{0}$ 的导体球被半径为 $b (b > a)$ 的同心薄球壳包围，球壳上涂有表面电荷，其密度为

$$
\sigma (\theta) = k \cos \theta
$$

其中 k 是常数， $\theta$ 是通常的球坐标。

(a) 求 (i) $r \geqslant b$ 和 (ii) $a \leqslant r \leqslant b$ 区域内的电势。

(b) 求导体球上的感应表面电荷密度 $\sigma_{i}(\theta)$ 。

(c) 该体系的总电荷是多少？验证你的答案与较大 r 处 V 的变化行为一致。

$\left[\dot{\text{答案}}: V(r, \theta) = \left\{ \begin{array}{ll} aV_0 / r + (b^3 - a^3)k\cos \theta / 3r^2\varepsilon_0, & r\geqslant b\\ aV_0 / r + (r^3 - a^3)k\cos \theta / 3r^2\varepsilon_0, & a\leqslant r\leqslant b \end{array} \right.\right]$

习题3.44 电荷 $+Q$ 沿 $z$ 轴从 $z = -a$ 到 $z = +a$ 均匀分布。证明：对于 $r > a$ ，点 $\pmb{r}$ 处的电势由下式给出：

$$
V (r, \theta) = \frac {q}{4 \pi \varepsilon_ {0}} \frac {1}{r} \left[ 1 + \frac {1}{3} \left(\frac {a}{r}\right) ^ {2} P _ {2} (\cos \theta) + \frac {1}{5} \left(\frac {a}{r}\right) ^ {4} P _ {4} (\cos \theta) + \dots \right]
$$

习题3.45 半径为 $R$ 的长圆柱壳上半部分带有均匀的表面电荷密度 $\sigma_0$ ，下半部分带有相反的电荷密度 $-\sigma_0$ ，如图3.40所示。求圆柱壳内外的电势。

![](images/7e1ab67801eba15f08482a014809c958fa52d9835c0465beae7ccc712b1ceedb.jpg)  
图3.40

习题3.46 一根从 $z = -a$ 延伸到 $z = +a$ 的细绝缘杆，载有下面所示的线电荷。在下列每种情况下，求出多极展开势中的首项：（a） $\lambda = k\cos (\pi z / 2a)$ ，（b） $\lambda = k\sin (\pi z / a)$ ，（c） $\lambda = k\cos (\pi z / a)$ ，其中 $k$ 为常数。

习题3.47 证明：半径为 $R$ 的球由球内所有电荷所产生的平均电场为

$$
E _ {\mathrm{平均}} = - \frac {1}{4 \pi \varepsilon_ {0}} \frac {P}{R ^ {3}}\tag{3.105}
$$

其中 p 是总偶极矩。有几种方法可以证明这个简单有趣的结果。这里是其中一种 $^{22}$ ：

（a）证明球体内单个电荷 $q$ 在点 $\pmb{r}$ 处所产生的平均电场与球体内均匀电荷分布 $\rho = -q / \left(\frac{4}{3}\pi R^3\right)$ 在 $\pmb{r}$ 处产生的电场相同，即

$$
\frac {1}{4 \pi \varepsilon_ {0}} \frac {1}{\left(\frac {4}{3} \pi R ^ {3}\right)} \int \frac {q}{r ^ {2}} \hat {\mathbf {z}} \mathrm{d} \tau^ {\prime}
$$

其中 $\hat{z}$ 是从 r 到 $d\tau'$ 的单位矢量。

(b) 后者可由高斯定理（见习题2.12）得出。用 $q$ 的偶极矩表示你的结果。

(c) 使用叠加原理推广到任意电荷分布。

(d) 当你这样做的时候，证明由外部所有电荷在球体内产生的平均电场与它们在球心处所产生的电场相同。

习题3.48

(a) 利用式 (3.103)，计算以原点为中心的半径为 $R$ 的球体上偶极子的平均电场。首先进行角积分。[请注意：在积分之前，你必须用 $\hat{x}, \hat{y}, \hat{z}$ 来表示出 $\hat{r}$ 和 $\hat{\theta}$ （见本书后环衬）。如果你不明白为什么，请重新阅读第1.4.1节的讨论。]将你的答案与一般定理[式(3.105)]相比较。这里的差异与偶极子的电场在 $r = 0$ 时发散的事实有关。角积分为零，但径向积分为无穷大，所以我们确实不知道该怎么理解这个答案。为了解决这个难题，假设式(3.103)适用于半径为 $\varepsilon$ 的小球的外部——则它对 $E_{\text{平均}}$ 的贡献明显为零，整个结果完全来自 $\varepsilon$ -球内的场。

(b) 为了使一般定理 [式 (3.105)] 成立, $\varepsilon$ -球内部的电场必须是多少? [提示: 由于 $\varepsilon$ 是任意小, 我们讨论的是在 $r = 0$ 时无穷大的某个量, 它在无穷小体积上的积分是有限的。][答案: $-(p/3\varepsilon_0)\delta^3(r)]$

很显然，偶极子的实际电场是

$$
E _ {\mathrm{dip}} (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \frac {1}{r ^ {3}} \left[ 3 (\boldsymbol {p} \cdot \hat {\boldsymbol {r}}) \hat {\boldsymbol {r}} - \boldsymbol {p} \right] - \frac {1}{3 \varepsilon_ {0}} p \delta^ {3} (\boldsymbol {r})\tag{3.106}
$$

你也许会想知道我们在计算第 3.4.4 节中的电场时是如何丢掉 $\delta$ 函数项的 $^{23}$ 。回答是，除 r=0 之外，导致式 (3.103) 的微分是完全有效的，但我们应当知道（根据在第 1.5.1 节中的经验）r=0 点微分是有问题的 $^{24}$ 。

习题3.49 在例题3.9中，我们得到了表面电荷为 $\sigma (\theta) = k\cos \theta$ 的球壳的电势。在习题3.30中，你会发现外面的电场是纯偶极子场；内部是均匀的[式(3.86)]。证明在 $R\to 0$ 极限情况下，再现了式(3.106)中的 $\delta$ 函数项。

习题3.50

(a) 假定电荷分布 $\rho_{1}(\pmb{r})$ 形成电势 $V_{1}(\pmb{r})$ ，而其他电荷分布 $\rho_{2}(\pmb{r})$ 形成电势 $V_{2}(\pmb{r})$ 。[对于我所关注的：这两种情况也许不存在任何共同点——也许1号是一个均匀带电球体，2号是一个平行板电容器。请注意 $\rho_{1}$ 和 $\rho_{2}$ 不同时存在；我们讨论的是两个不同的问题，一个是只存在 $\rho_{1}$ 的问题，另外一个是只有 $\rho_{2}$ 的问题。]证明格林互易定理（Green reciprocity theorem） $^{25}$ ：

$$
\int_ {\mathrm{整个空间}} \rho_ {1} V _ {2} \mathrm{d} \tau = \int_ {\mathrm{整个空间}} \rho_ {2} V _ {1} \mathrm{d} \tau
$$

[提示：计算 $\int E_1\cdot E_2\mathrm{d}\tau$ 有两种方法，首先写出 $E_{1} = -\nabla V_{1}$ ，并利用分部积分将求导转变为对 $E_{2}$ 求导，然后再写出 $E_{2} = -\nabla V_{2}$ ，并将求导转变为对 $E_{1}$ 求导。]

(b) 假设现在你有两个分开的导体（图3.41）。如果你使导体 $a$ 带电量 $Q$ （使导体 $b$ 不带电），使得导体 $b$ 的电势为 $V_{ab}$ 。另一方面，如果你让导体 $b$ 带同样的电荷 $Q$ （导体 $a$ 不带电），使得导体 $a$ 的电势为 $V_{ba}$ 。利用格林互易定理证明 $V_{ab} = V_{ba}$ （这是一个令人吃惊的结果，因为我们对导体的形状和位置没有做任何假设）。

![](images/560c6fcda3795cf6b16d7ad18932d650d119a93af864948054b200213f393789.jpg)  
图3.41

习题 3.51 利用格林互易定理（习题 3.50）求解下面两个问题。[提示：对于分布 1，使用实际的情况；对于分布 2，移去电荷 q，设导体的电势为 $V_{0}$ 。]

(a) 平行板电容器的两板都接地，点电荷 $q$ 放置在他们之间，距极板1的距离为 $x$ 。两板间的间距为 $d$ 。求每个极板上的感应电荷。[答案： $Q_{1} = q(x / d - 1)$ ; $Q_{2} = -qx / d$ ]

（b）两个同心的导体球壳（半径分别为 $a$ 和 $b$ ）接地，点电荷 $q$ 放置在他们之间半径为 $r$ 处（ $a < r < b$ ），求每个球体上的感应电荷。

习题3.52

(a) 证明：在多极展开中的四极矩项可以写为

$$
V _ {\mathrm{quan}} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {1}{2 r ^ {3}} \sum_ {i, j = 1} ^ {3} \hat {r} _ {i} \hat {r} _ {j} Q _ {i j}
$$

式中 [如式 (1.31) 所示]

$$
Q _ {i j} \equiv \int \left[ 3 r _ {i} ^ {\prime} r _ {j} ^ {\prime} - (r ^ {\prime}) ^ {2} \delta_ {i j} \right] \rho (\boldsymbol {r} ^ {\prime}) \mathrm{d} \tau^ {\prime}
$$

这里

$$
\delta_ {i j} = \left\{ \begin{array}{l l} {{1,}} & {{\text {如果} i = j}} \\ {{0,}} & {{\text {如果} i \neq j}} \end{array} \right.
$$

为克罗内克 $\delta$ 函数， $Q_{ij}$ 是电荷分布的四极矩。请注意阶次：

$$
V _ {\text {单极}} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {Q}{r}; V _ {\text {偶极}} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {\sum \hat {r} _ {i} p _ {i}}{r ^ {2}}; V _ {\text {四极}} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {\sum \hat {r} _ {i} \hat {r} _ {j} Q _ {i j}}{r ^ {3}}; \dots
$$

单极矩（Q）是标量，偶极矩（p）是矢量，四极矩（ $Q_{ij}$ ）是二阶张量，依此类推。

(b) 对于图 3.30 所示的构型中，求 $Q_{ij}$ 的所有九个分量（假设正方形的边长为 a，位于以原点为中心的 xy 平面内）。

（c）证明如果单极矩和偶极矩都为零，则四极矩与原点位置无关。（该结论对其他阶次极矩都成立——最低非零多极矩总是与原点位置无关。）

(d) 你如何定义八极矩？用八极矩表示多极展开中的八极项。

习题3.53 在例题3.8中，我们确定了位于均匀外电场 $E_0$ 中的导体球（半径 $R$ ）外部的电场。现在使用镜像法求解该问题，并验证你的答案是否与式(3.76)一致。[提示：利用例题3.2结果，但放入另外一个电荷与 $q$ 完全相反的 $-q$ 。设 $a \to \infty$ ，并使 $(1/4\pi\varepsilon_0)(2q/a^2) = -E_0$ 为常数。]

!习题 3.54 对例题 3.4 中的无限长矩形管，假设底面 $(y=0)$ 和两侧 $(x=\pm b)$ 上的电势为零，但顶部表面 $(y=a)$ 的电势为非零常数 $V_{0}$ 。求管内的电势。[注：这是将习题 3.15（b）旋转的情况；但按照在例题 3.4 中的方式，对 y 用正弦函数，对 x 用双曲函数。必须包含 k=0 的情况并不多见。] $^{26}$

[答案： $V_{0}\left(\frac{y}{a} +\frac{2}{\pi}\sum_{n = 1}^{\infty}\frac{(-1)^{n}}{n}\frac{\cosh(n\pi x / a)}{\cosh(n\pi b / a)}\sin (n\pi y / a)\right)$ 。或者，对 $x$ 使用正弦函数，对 $y$ 使用的双曲线函数， $-\frac{2V_0}{b}\sum_{n = 1}^{\infty}\frac{(-1)^n\sinh(\alpha_ny)}{\alpha_n\sinh(\alpha_na)}\cos (\alpha_nx)$ ，这里 $\alpha_{n}\equiv (2n - 1)\pi /2b]$

!习题3.55

（a）横截面为正四边形（边长为 $a$ ）的长金属管，管的三个侧面接地，而第四个侧面（与其他三面绝缘）维持有恒定的电势 $V_{0}$ 。求和 $V_{0}$ 面正对的表面上单位长度的净电荷。[提示：利用习题3.15和3.54的结果。]

（b）将横截面半径为 $R$ 的长金属管沿纵向分成四个相等的部分，其中三个接地，第四个维持恒定的电势 $V_{0}$ 。求和 $V_{0}$ 相对的部分上面单位长度的净电荷。[(a)和(b)的答案： $\lambda = -(\varepsilon_0V_0 / \pi)\ln 2]$

习题 3.56 如图 3.36 所示，理想的电偶极子位于原点，指向 z 轴方向。电荷从 xy 平面上的某一点由静止开始释放。证明：它以半圆弧形来回摆动，就好像它是一个挂在原点的钟摆 $^{28}$ 。

习题 3.57 静止的电偶极子 $p = p \hat{z}$ 位于原点。质量为 m 的正点电荷 q 在偶极子电场中以恒定速度做半径为 s 的圆周运动。描述轨道平面的特征。求电荷的速度、角动量和总能量 $^{29}$ 。

[答案： $L = \sqrt{qpm / 3\sqrt{3}\pi\varepsilon_0} ]$

习题3.58 求半径为 $R$ 的球体表面上的电荷密度 $\sigma(\theta)$ ，使得对于球体外部的点，该密度与 $z$ 轴上 $a < R$ 点处的电荷 $q$ 产生相同的电场。[答案： $\frac{q}{4\pi R}(R^2 - a^2)(R^2 + a^2 - 2Ra\cos\theta)^{-3/2}]$

## 第 4 章 介质中的电场

## 4.1 极化

## 4.1.1 电介质

在本章中，我们将学习物质中的电场。当然，物质有很多种——固体、液体、气体、金属、木材和玻璃——这些物质对静电场的响应并不都是一样的。然而，日常大多数物质（至少在很好的近似下）属于两大类中之一：导体（conductors）和绝缘体（insulators）（或电介质，dielectrics）。我们已经讲到过导体，它们是可以“无限”地提供在其内部可自由移动电荷的物体。实际上，这通常意味着许多电子（在典型的金属中，每个原子提供一个或者两个电子）并不与任何特定的原子核相结合，而是在导体中随意漫游。相比之下，在电介质中，所有的电荷都附着在特定的原子或分子上——它们被严格地束缚着，所有的电子只能在原子或分子内移动一点点。这种微观位移并不像在导体中电荷的大规模重排那样剧烈，但是它们的累积效应可以解释电介质材料的行为特征。实际上，有两种主要机制使得电场可以改变电介质中原子或分子中的电荷分布：伸展和旋转。在接下来的两节中，我将讨论这些过程。

## 4.1.2 诱导偶极子

当中性原子处于电场中时会发生什么？你的第一想法可能是：“绝对没什么会发生——因为原子不带电，电场对它没有影响。”但这是不正确的。虽然原子作为一个整体是电中性的，但有一个带正电的核心（原子核）和一个带负电的电子云围绕着它。在原子内这两个带电的区域是受外电场影响的：原子核被推向电场的方向，电子则被推向相反的方向。原则上，如果电场足够大，它可以将原子完全拉开，使其“电离”（物体随后变成导体）。然而，在不那么极端的电场中，很快就会建立平衡，因为如果电子云分布的中心和原子核的中心不重合，这些正负电荷就会相互吸引，从而将原子结合在一起。两个相反的力——E使电子和原子核拉开，它们之间的相互吸引将它们拉回到一起——达到一个平衡，平衡时正电荷略微向一个方向移动，负电荷略微向另一个方向偏移，导致原子极化（polarized）。原子现在有了一个微小的偶极矩 p，它与电场的方向相同。一般来讲，这个诱导的偶极矩与电场近似成正比（只要电场不是太强）：

$$
\boldsymbol {p} = \alpha \boldsymbol {E}\tag{4.1}
$$

比例常数 $\alpha$ 称为原子极化率（atomic polarizability）。它的值取决于所讨论原子的具体结构。表4.1列出了一些实验确定的原子极化率。

表 4.1 原子极化率 ( $\alpha/4\pi\varepsilon_{0}$ ，单位 $10^{-30}m^{3}$ )  
来源：《物理化学手册》（第91版）（Boca Raton: CRC Press, 2010）

<table><tr><td>H</td><td>He</td><td>Li</td><td>Be</td><td>C</td><td>Ne</td><td>Na</td><td>Ar</td><td>K</td><td>Cs</td></tr><tr><td>0.667</td><td>0.205</td><td>24.3</td><td>5.60</td><td>1.67</td><td>0.396</td><td>24.1</td><td>1.64</td><td>43.4</td><td>59.4</td></tr></table>

例题4.1 原子的原始模型是由一个点核（ $+q$ ）和一个半径为 $a$ 的均匀带电球形电子云（ $-q$ ）组成的（图4.1）。计算这种原子的原子极化率。

![](images/b9ba1ecbf217a86a0ba72baf4515a31ad0aa22e29614ab3eb6626c2150ed35e4.jpg)  
图4.1

[解答] 如图 4.2 所示，在存在外场 E 的情况下，原子核将略微向右移动，电子云将向左移动。（因为实际位移非常小，正如如你在下面的习题 4.1 中看到的那样，可以合理地假设电子云保持其球形不变。）假设当原子核从球中心移动距离 d 时达到平衡。此时，将原子核向右推的外场与将其向右拉的内部电场完全平衡： $E = E_{e}$ ，其中 $E_{e}$ 为电子云产生的电场。那么，距离均匀带电球体中心 d 处的电场为

$$
E _ {\mathrm{e}} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q d}{a ^ {3}}
$$

(习题 2.12)。在平衡位置时，有

The image contains no legible text. The characters 'A', 'B', and 'C' are part of a large, fragmented character that is visually indistinct. According to Rule 4 (Edge Noise Strategy), since the ground truth is not clearly visible, the OCR should not output any character. Therefore, the corrected OCR text is:

[No text detected]

$$
E = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q d}{a ^ {3}} \quad \text {或} \quad p = q d = (4 \pi \varepsilon_ {0} a ^ {3}) E
$$

$$
\alpha = 4 \pi \varepsilon_ {0} a ^ {3} = 3 \varepsilon_ {0} v
$$

其中 v 是原子的体积。虽然这个原子模型非常粗糙，但结果 [式 (4.2)] 并不是太糟糕——对于许多简单的原子来说，它的精确度可达到万分之一。

图4.2

对于分子来说，情况并不是那么简单了，因为它们常常在某些方向上比在其他方向上更容易极化。例如，当沿分子轴施加电场时，对二氧化碳（图4.3）的极化率为 $4.5\times10^{-40}C^{2}\cdot m/N$ ，但对于垂直于该方向的外加电场，极化率仅为 $2\times10^{-40}C^{2}\cdot m/N$ 。当外加电场与分子轴成一定角度时，必须将其分解为平行和垂直分量，并将每个分量乘以相应的极化率：

$$
\boldsymbol {p} = \alpha_ {\perp} \boldsymbol {E} _ {\perp} + \alpha_ {\parallel} \boldsymbol {E} _ {\parallel}
$$

在这种情况下，诱导的偶极矩甚至可能与电场 E 的方向不同。就分子而言， $CO_{2}$ 分子相对比较简单，因为其中的原子至少排列成一条直线；对于完全不对称的分子，式 (4.1) 中的关系将被更普遍的线性关系所取代：

$$
\left. \begin{array}{l} p _ {x} = \alpha_ {x x} E _ {x} + \alpha_ {x y} E _ {y} + \alpha_ {x z} E _ {z} \\ p _ {y} = \alpha_ {y x} E _ {x} + \alpha_ {y y} E _ {y} + \alpha_ {y z} E _ {z} \\ p _ {z} = \alpha_ {z x} E _ {x} + \alpha_ {z y} E _ {y} + \alpha_ {z z} E _ {z} \end{array} \right\}\tag{4.3}
$$

![](images/227550c9d8ed5c21a549711fb69a151aa784057e623906618fa4a4bdcfbe6c47.jpg)  
图4.3

这九个常数 $\alpha_{ij}$ 的集合组成了分子的极化张量（polarizability tensor）。它们的实际值取决于你所选取坐标轴的方向，尽管通常总是可以选取“主”轴，使得非对角项 $(\alpha_{xy}, \alpha_{zx}$ 等）为零，只留下三个非零的极化率： $\alpha_{xx}, \alpha_{yy}, \alpha_{zz}$ 。

习题4.1 一个氢原子（玻尔半径为 $0.5\AA$ ）位于相距 $1\mathrm{mm}$ 的两个金属板中间，两金属板连接在 $500\mathrm{V}$ 电池的正负极上。粗略的估计分离距离 $d$ 大致等于原子半径的几分之一？估计用该装置电离氢原子所需的电压为多少。[使用表4.1中的 $\alpha$ 值。我们谈论的位移是十分微小的，即使是在原子尺寸上也是如此。]

习题4.2 根据量子力学，基态氢原子的电子云有电荷密度：

$$
\rho (r) = \frac {q}{\pi a ^ {3}} \mathrm{e} ^ {- 2 r / a}
$$

其中 q 是电子的电荷，a 为玻尔半径。求这种原子的原子极化率。[提示：首先计算电子云的电场 $E_{e}(r)$ ; 然后，假设 $r \ll a$ ，将指数展开 $^{1}$ 。]

习题 4.3 根据式 (4.1)，原子的诱导偶极矩与外场成正比。这是一条“经验法则”，并非一条基本定律，理论上很容易编造例外情况。例如，假设在半径 R 以内电子云的电荷密度正比于该点至中心的距离。在这种情况下，p 与 E 的几次幂成正比？给出使式 (4.1) 在弱场极限下成立 $\rho(r)$ 所满足的条件。

习题4.4 点电荷 $q$ 与极化率为 $\alpha$ 的中性原子相距较大的距离 $r$ 。求它们之间的吸引力。

## 4.1.3 极性分子的排列

第 4.1.2 节中讨论的中性原子开始时并没有偶极矩——p 是由外加电场诱导的。一些分子具有固有偶极矩。例如，在水分子中，电子倾向于聚集在氧原子周围（图 4.4），由于分子中原子中心连线呈 $105^{\circ}$ 角，这使得负电荷位于顶角处，而正电荷在相反的一侧。（水的偶极矩异常大： $6.1 \times 10^{-30} C \cdot m$ ；事实上，这就是水为什么可以作为有效溶剂的原因。）当这些分子（称为极性分子，polar molecules）被置于电场中时，将会发生什么？

![](images/b5e3cfe0ca11dc783e087b2790880be9fb5cf7cb91106896eec54a59f25a6e4e.jpg)  
图4.4

如果场是均强电场，则作用在正电荷端的力 $F_{+} = qE$ 恰好和作用在负电荷端的力 $F_{-} = -qE$ 相互抵消（图 4.5）。但是，将有一个力矩：

$$
\begin{array}{r l} \boldsymbol {N} & = (\boldsymbol {r} _ {+} \times \boldsymbol {F} _ {+}) + (\boldsymbol {r} _ {-} \times \boldsymbol {F} _ {-}) \\ & = [ (\boldsymbol {d} / 2) \times (q \boldsymbol {E}) ] + [ (- \mathbf {d} / 2) \times (- q \boldsymbol {E}) ] = q \boldsymbol {d} \times \boldsymbol {E} \end{array}
$$

因此，均匀外场中的偶极子 $p = qd$ 会受到一个力矩

$$
\boxed {N = \boldsymbol {p} \times \boldsymbol {E}}\tag{4.4}
$$

请注意，N 的方向倾向于使 p 与 E 平行；自由转动的偶极分子会四处摆动，直到它指向施加外电场的方向。

![](images/3e11d4012abb45630881399f163bf5ae4c67b198172bf4f9916c1cbec25d4389.jpg)  
图4.5

如果电场是非均匀的，使得 $F_{+}$ 与 $F_{-}$ 不能完全相抵，除了力矩外，还会有合力作用在偶极子上。当然，E 必须变化十分显著，这才能使分子的空间发生显著变化；在讨论电介质行为时这通常不是一个需要考虑的主要因素。然而，非均匀电场中偶极子所受力的公式颇具研究价值：

$$
\boldsymbol {F} = \boldsymbol {F} _ {+} + \boldsymbol {F} _ {-} = q (\boldsymbol {E} _ {+} - \boldsymbol {E} _ {-}) = q (\Delta \boldsymbol {E})
$$

其中 $\Delta E$ 代表正极端电场和负极端电场之间的差。假设偶极子非常短，我们可以使用式(1.35)来近似 $E_{x}$ 的微小变化：

$$
\Delta E _ {x} \equiv (\nabla E _ {x}) \cdot d
$$

$E_{y}, E_{z}$ 也有相应的公式。更简洁地有

$$
\Delta E = (d \cdot \nabla) E
$$

因此 $^{2}$

$$
\boxed {\boldsymbol {F} = (\boldsymbol {p} \cdot \nabla) \boldsymbol {E}}\tag{4.5}
$$

对于长度无穷小的“理想”偶极子，即使在非均匀电场中，式(4.4)也给出了偶极子中心的力矩；而关于任意的其他点，力矩为 $N=(p\times E)+(r\times F)$ 。

习题 4.5 在图 4.6 中， $p_{1}$ 和 $p_{2}$ 是相距为 r 的理想偶极子。 $p_{2}$ 作用在 $p_{1}$ 上的力矩为多少？ $p_{1}$ 作用在 $p_{2}$ 上的力矩为多少？[在每种情况下，所求的力矩都应是关于偶极子绕其自身中心的力矩。如果所得到的答案不相等或相反，这会让你感到困扰，请参阅习题 4.29。]

![](images/8b139da7bdfe597f48fafd930cc4b768d831e03fc4e06d0213b3b41ffb897d15.jpg)  
图4.6

习题 4.6 理想偶极子 p 位于无限接地导体平面上方距离 z 处（图 4.7）。偶极子与垂直于平面的方向成夹角 $\theta$ 。求作用在 p 上的力矩。如果偶极子可以自由旋转，那么它将静止在什么方向上？

![](images/bc0288aae1cf0f745c243c10283c522f0fd9c776c99ed8001f2275c24f937376.jpg)  
图4.7

习题4.7 证明在电场中理想偶极子 $\pmb{p}$ 的能量由下式给出：

$$
\boxed {U = - \boldsymbol {p} \cdot \boldsymbol {E}}\tag{4.6}
$$

习题4.8 证明相距位移为 $\pmb{r}$ 的两个理想偶极子的相互作用能为

$$
U = \frac {1}{4 \pi \varepsilon_ {0}} \frac {1}{r ^ {3}} [ \pmb {p} _ {1} \cdot \pmb {p} _ {2} - 3 (\pmb {p} _ {1} \cdot \hat {\pmb {r}}) (\pmb {p} _ {2} \cdot \hat {\pmb {r}}) ]\tag{4.7}
$$

[提示：利用习题4.7和式(3.104)]

习题 4.9 偶极子 p 距点电荷 q 的距离为 r，且 p 与从 q 到 p 的矢量 r 的夹角为 $\theta$ 。

(a) 作用在 $\pmb{p}$ 上的力是多少？

(b) 作用在 $q$ 上的力是多少？

## 4.1.4 极化

在前两节中，我们考虑了外场对单个原子或分子的影响。我们现在能够回答（定性地）最初的问题：当一块电介质材料放入电场中时会发生什么？如果物质是由中性原子（或非极性分子）组成的，则电场将在每个原子或非极性分子中都会诱导出一个微小的偶极矩，其方向指向与电场相同的方向 $^{3}$ 。如果材料是由极性分子组成的，每一个固有偶极矩都会受到一个力矩作用，使它倾向于沿着电场方向排列。（随机的热运动与这一过程竞争，因此极化分子的完全一致的排列是不可能的，特别是在较高温的情况下，一旦移去外场，极化排列将立即消失。）

请注意，这两种机制产生了相同的基本结论：许多小偶极子沿着电场方向——材料出现极化（polarized）。衡量这种效果的一个方便的方法是

$$
P \equiv \text { 单位体积偶极矩 }
$$

这称作极化。从现在开始，我们将不再过多关注极化是怎样形成的。事实上，我所描述的这两种机制并不像我说的区别有那么明显。即使在极性分子中，也会因位移而产生一些极化（尽管通常旋转分子比拉伸它要容易得多，因此第二种机制占主导地位）。在某些材料中甚至有可能“冻结住”极化，这样它在外电场撤除后仍然存在极化。现在，让我们先暂且忘记产生极化的原因，来研究极化材料自身产生的电场。然后，在第4.3节中，我们将它们结合起来：它诱导极化的原电场，加上由P产生新电场。

## 4.2 极化物体的场

## 4.2.1 束缚电荷

假设我们有一块极化材料——一个包含许多排列整齐的微观偶极子的物体。单位体积的偶极矩由 P 给出。问题：这个物体产生的电场是多少（不是可能引起极化的电场，而是极化本身产生的场）？好的，我们已经知道单个偶极子的电场是多少，那么为什么不将物体分割为许多无限小的偶极子并通过积分得到整个电场呢？通常情况下，利用电势来求解电场会更容易一些。对于单个的偶极子 p，我们有 [式 (3.99)]

$$
V (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \frac {\boldsymbol {p} \cdot \hat {\boldsymbol {r}}}{r ^ {2}}\tag{4.8}
$$

其中 $\pmb{z}$ 是从偶极子到我们所要计算电势的点的矢量（图4.8）。在此情况下，每个小体积元 $\mathrm{d}\tau^{\prime}$ 都有偶极矩 $p = P\mathrm{d}\tau^{\prime}$ ，因此总的电势为

$$
V (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \int_ {\mathcal {V}} \frac {\boldsymbol {P} (\boldsymbol {r} ^ {\prime}) \cdot \hat {\boldsymbol {r}}}{r ^ {2}} \mathrm{d} \tau^ {\prime}\tag{4.9}
$$

原则上就是这样。但一个小小的技巧将这个积分变成了一个更具启发性的形式。注意到

$$
\nabla^ {\prime} \left(\frac {1}{r}\right) = \frac {\hat {r}}{r ^ {2}}
$$

其中（与习题1.13不同）微分是相对于源坐标 $(r^{\prime})$ 的，我们有

$$
V = \frac {1}{4 \pi \varepsilon_ {0}} \int_ {\mathcal {V}} \boldsymbol {P} \cdot \nabla^ {\prime} \left(\frac {1}{\nu}\right) \mathrm{d} \tau^ {\prime}
$$

使用矢量积规则 5，并利用分部积分，给出

$$
V = \frac {1}{4 \pi \varepsilon_ {0}} \left[ \int_ {\mathcal {V}} \nabla^ {\prime} \cdot \left(\frac {\boldsymbol {P}}{\imath}\right) \mathrm{d} \tau^ {\prime} - \int_ {\mathcal {V}} \frac {1}{\imath} (\nabla^ {\prime} \cdot \boldsymbol {P}) \mathrm{d} \tau^ {\prime} \right]
$$

或者，援引散度定理，

$$
V = \frac {1}{4 \pi \varepsilon_ {0}} \oint_ {\mathcal {S}} \frac {1}{2} \boldsymbol {P} \cdot \mathrm{d} \boldsymbol {a} ^ {\prime} - \frac {1}{4 \pi \varepsilon_ {0}} \int_ {\mathcal {V}} \frac {1}{2} (\nabla^ {\prime} \cdot \boldsymbol {P}) \mathrm{d} \tau^ {\prime}\tag{4.10}
$$

第一项看起来像是表面电荷的电势

$$
\boxed {\sigma_ {\mathrm{b}} \equiv \boldsymbol {P} \cdot \hat {\boldsymbol {n}}}\tag{4.11}
$$

(其中 $\hat{n}$ 为法向单位矢量)，而第二项看起来像是体电荷的电势

$$
\boxed {\rho_ {\mathrm{b}} \equiv - \nabla \cdot P}\tag{4.12}
$$

根据这些定义，式 (4.10) 变为

$$
V (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \oint_ {\mathcal {S}} \frac {\sigma_ {\mathrm{b}}}{\imath} \mathrm{d} a ^ {\prime} + \frac {1}{4 \pi \varepsilon_ {0}} \int_ {\mathcal {V}} \frac {\rho_ {\mathrm{b}}}{\imath} \mathrm{d} \tau^ {\prime}\tag{4.13}
$$

![](images/3c3b817f6316576c10da6c1fbb8a7e6806acadb20cc61ccdc7c8550508d8b58e.jpg)  
图4.8

这意味着极化物体的电势（以及电场）与体电荷密度 $\rho_{b} \equiv -\nabla \cdot P$ 加上表面电荷 $\sigma_{b} = P \cdot \hat{n}$ 所产生的电势相同。与其像式 (4.9) 中那样对所有无穷小偶极子的贡献进行积分，我们可以先求出这些束缚电荷（bound charges），然后计算它们产生的电场，就像我们计算任何其他体积或表面电荷的电场一样（例如，利用高斯定理）。

例题 4.2 求半径为 R 的均匀极化球体所产生的电场。

[解答] 我们可以选择坐标 $z$ 轴与极化方向重合（图4.9）。因为是均匀的，体束缚电荷密度 $\rho_{\mathrm{b}}$ 为零，但

$$
\sigma_ {\mathrm{b}} = P \cdot \hat {n} = P \cos \theta
$$

其中 $\theta$ 为通常的球坐标。那么，我们想要求的是涂在球体表面上电荷密度 $P\cos \theta$ 所产生的电场。但我们在例题3.9中已经计算过这种构型的电势：

$$
V (r, \theta) = \left\{ \begin{array}{l l} \frac {P}{3 \varepsilon_ {0}} r \cos \theta , & r \leqslant R \\ \frac {P}{3 \varepsilon_ {0}} \frac {R ^ {3}}{r ^ {2}} \cos \theta , & r \geqslant R \end{array} \right.
$$

![](images/41e1f71de289e899851ceebe794c00e1a5183b9869362e0836d5eb6da24b9f0f.jpg)  
图4.9

由于 $r\cos \theta = z$ ，所以球体内部的电场是均匀的：

$$
\pmb {E} = - \nabla V = - \frac {P}{3 \varepsilon_ {0}} \hat {\pmb {z}} = - \frac {1}{3 \varepsilon_ {0}} \pmb {P}, r <   R\tag{4.14}
$$

这一值得注意的结果在下文中非常有用。在球体之外，其电势与原点处的理想偶极子的电势相同，

$$
V = \frac {1}{4 \pi \varepsilon_ {0}} \frac {\pmb {p} \cdot \hat {\pmb {r}}}{r ^ {2}}, r \leqslant R\tag{4.15}
$$

毫不奇怪，其偶极矩等于球体的总偶极矩：

$$
\boldsymbol {p} = \frac {4}{3} \pi R ^ {3} \boldsymbol {P}\tag{4.16}
$$

图 4.10 给出了均匀极化球体的电场。

![](images/642bc71445d541c0ade3b2f2bf655b5e3fef928a07f13166376908d9599bce25.jpg)

•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•

## 习题4.10 半径为 $R$ 的球体具有极化矢量

$$
P (r) = k r
$$

其中 $k$ 是常数， $\pmb{r}$ 为原点位于球心的矢量。

(a) 计算束缚电荷 $\sigma_{b}$ 和 $\rho_{b}$ 。

(b) 求球体内部和外部的电场。

习题 4.11 半径为 a、长度为 L 的短圆柱体具有平行于其轴线的“冻结”均匀极化强度 P。求束缚电荷，并对下列情况绘出电场的草图，(i) $L \gg a$ ，(ii) $L \ll a$ ，(iii) $L \approx a$ 。[这被称为条形永电体（bar electret）；它类比于条形磁铁。在实际中，只有非常特殊的材料才能保持永久的电极化，钛酸钡盐是最为“熟知”的例子。这就是为什么你不能在玩具店里买到永电体。]

习题 4.12 直接利用式 (4.9) 计算均匀极化球体的电势（例题 4.2）。

## 4.2.2 束缚电荷的物理诠释

在上一节中，我们发现物体的极化电场与由“束缚电荷”特定分布 $\sigma_{b}$ 和 $\rho_{b}$ 所产生的电场相同。但这一结论是在对式 (4.9) 中的积分进行抽象运算的过程中得出的，让我们对这些束缚电荷的物理意义一无所知。的确，一些作者给你们的印象是束缚电荷在某种意义上是“虚构的”——仅仅是用来帮助计算电场的纸面上的东西而已。事实远非如此： $\rho_{b}$ 和 $\sigma_{b}$ 代表了完全真实的电荷累积。在本节中，我将解释极化是如何导致这些电荷分布的。

基本思想很简单：假设我们有一长串如图 4.11 所示的偶极子阵列，沿着这条线，一个偶极子的头部与它的相邻偶极子的尾部相抵消，但在线的两端剩余了两个电荷：正电荷在右端，负电荷在左端。就像是我们在一端剥离了一个电子，并将其沿线一直带到另一端。尽管事实上并没有一个电子完成了这个旅程——许多微小的位移加起来就是一个大的位移。我们将末端的净电荷称为束缚电荷，来提醒我们它是不能移动的；在电介质中，每个电子都附着于一个特定的原子或分子上。除此之外，束缚电荷与其他任何类型的电荷并没有什么不同。

![](images/d5292195721c028e1b7398b56e941b797378610f81032b8c9f66e12a820c2782.jpg)  
图4.11

为了计算一个给定极化强度产生的束缚电荷的大小，考查一平行于 P 的电介质“管”。图 4.12 所示的一小体积块的偶极矩为 $P(Ad)$ ，其中 A 为管的横截面积，d 是小体积块的长度。对于末端的电荷 (q)，偶极矩也可以写为 qd。因此堆积在管右端的束缚电荷是

$$
q = P A
$$

如果末端被垂直切割，那么表面电荷密度为

$$
\sigma_ {\mathrm{b}} = \frac {q}{A} = P
$$

![](images/461e707e3039853dbea5035cf413e48791f87cd2988d20914244beadf3025af4.jpg)  
图4.12

对于斜切（图4.13），电荷依然相同，但 $A = A_{\text{末}}\cos \theta$ ，所以

$$
\sigma_ {\mathrm{b}} = \frac {q}{A _ {\text {末}}} = P \cos \theta = P \cdot \hat {n}
$$

因此，极化的效果就是在物体表面涂上束缚电荷 $\sigma_{b}=P\cdot\hat{n}$ 。这正是我们在 4.2.1 节中通过更严谨的方法得到的结论。但现在我们知道束缚电荷是从哪里来的了。

![](images/f27dca93f62e4b49905cc6e94234485c212bf3083d9b7254c40a0a77aef84a95.jpg)  
图4.13

如果极化不均匀，会在物体内部和表面上同时积累有束缚电荷。从图4.14可以看出，发散的 $P$ 会导致负电荷的堆积。事实上，给定体积中的净束缚电荷 $\int \rho_{\mathrm{b}}\mathrm{d}\tau$ 与被排挤出表面的电荷相等且符号相反。后者（根据我们之前所用的相同的推理）是每单位面积 $P\cdot \hat{n}$ 所以

$$
\int_ {\mathcal {V}} \rho_ {\mathrm{b}} \mathrm{d} \tau = - \oint_ {\mathcal {S}} \boldsymbol {P} \cdot \mathrm{d} a = - \int_ {\mathcal {V}} (\boldsymbol {\nabla} \cdot \boldsymbol {P}) \mathrm{d} \tau
$$

由于对于任何的体积都适用，我们得到

$$
\rho_ {\mathrm{b}} = - \nabla \cdot P
$$

再次得出第 4.2.1 节中更严格的结论。

![](images/4eec20f395d2756af13843c38e62a2d218518554db4c3053526ece3c83f1b535.jpg)  
图4.14

例题 4.3 还有另一种分析均匀极化球体的方法（例题 4.2），且能很好地说明束缚电荷的概念。我们实际上有两个带电球体：一个带正电荷，一个带负电荷。在没有极化的情况下，两者是完全重叠并且其电荷完全抵消。但是当物体均匀极化时，所有的正电荷稍微向上（z 方向）移动，而所有的负电荷稍微向下移动（图 4.15）。这两个球体不再完全重叠：在顶部有一个剩余正电荷的“帽子”，而在底部有一个负电荷的“帽子”。这个“剩余”电荷恰恰就是表面束缚电荷 $\sigma_{b}$ 。

![](images/6de5a56749bd5b9de9c2eb8103febbed5e5f13df7763478d926e69e589c131dd.jpg)  
图4.15

在习题2.18中，你们计算了两个均匀带电球体重叠区域的电场；答案是

$$
\pmb {E} = - \frac {1}{4 \pi \varepsilon_ {0}} \frac {q \pmb {d}}{R ^ {3}}
$$

其中 $q$ 是带正电荷球体的总电荷， $d$ 是从负电荷中心到正电荷中心的位置矢量， $R$ 是球的半径。我们可以用球体的极化来表示这一点， $p = q d = \left(\frac{4}{3} \pi R^3\right) P$

$$
\boldsymbol {E} = - \frac {1}{3 \varepsilon_ {0}} \boldsymbol {P}
$$

同时，对于球体外部的点，就好像每个带电球体的所有电荷都集中在各自的中心。那么，我们得到一个偶极子，其电势为

$$
V = \frac {1}{4 \pi \varepsilon_ {0}} \frac {\pmb {p} \cdot \hat {\pmb {r}}}{r ^ {2}}
$$

（请记住： $d$ 非常之小，仅是原子半径的一小部分；图4.15被严重夸大了。）当然，这些结果和例题4.2的答案是一致的。

习题4.13 半径为 $a$ 的长的圆柱体，垂直于其轴线方向具有均匀极化强度 $P$ 。求圆柱体内的电场。证明圆柱体外的电场可以用如下形式表示：

$$
\boldsymbol {E} (\boldsymbol {r}) = \frac {a ^ {2}}{2 \varepsilon_ {0} s ^ {2}} \left[ 2 \left(\boldsymbol {P} \cdot \hat {\boldsymbol {s}}\right) \hat {\boldsymbol {s}} - \boldsymbol {P} \right]
$$

[注意：我是说“均匀”，而不是“放射状”！]

习题 4.14 当极化中性电介质时，电荷会移动一点点，但是总电荷保持为零。这一事实应反映在束缚电荷 $\sigma_{b}$ 和 $\rho_{b}$ 上。利用式 (4.11) 和式 (4.12) 证明总束缚电荷为零。

## 4.2.3 电介质内部的场 $^{4}$

此前我并没有深究“纯”偶极子和“物理”偶极子之间的区别。在发展束缚电荷理论时，我假设我们研究的是纯偶极子——事实上，我是从纯偶极子的电势，即式(4.8)开始的。然而，实际的极化电介质是由物理偶极子构成的，尽管它们非常微小。更重要的是，我假设将分立的分子偶极子可以用一个连续的密度函数 $P$ 来表示。如何证明此种方法的合理性？在电介质之外，它是没有任何问题的：此时我们距离分子较远（ $\nu$ 比正负电荷之间的间距大很多倍），所以偶极子势起主导作用，源“颗粒性”的细节被距离所掩盖。然而，在电介质内部，我们几乎不能再假定距所有偶极子都很远；所以，我在第4.2.1节中所使用的推导过程面临着严峻的挑战。

事实上，当你停下来想一想，物体内部的电场在微观层面上一定极其复杂。如果你恰好靠近一个电子的话，那么它的电场是巨大的，而当变化一个很小距离时，它可能会变得很小，也可能指向完全不同的方向。此外，瞬间之后，随着原子的移动，电场将会完全改变。这个真正的微观（microscopic）电场是完全不可能计算出来的，即使如果可以的话，也不会有多大意义。正如我们基于宏观角度考虑可以把水视为一种连续的流体，忽略其分子结构一样，我们也可以忽略物体内部电场中的微观隆起和褶皱，而只专注于宏观（macroscopic）电场。这被定义为包含成千个原子的足够大区域的平均场（这样就可以消除我们不感兴趣的微观波动），但这个区域也要足够小，以保证我们没有剔除电场中任何有意义的宏观变化。（实际上，这就意味着我们必须在比物体本身尺度小很多的区域内进行平均。）人们通常所说的物体内部的电场就是这样的宏观电场 $^{5}$ 。

剩下的事情是证明当我们使用第 4.2.1 节的方法时，所得到的电场实际上就是宏观电场。这个论点很微妙，所以我们先放一下。假设我想计算电介质内部某些点 r 处的宏观电场（图 4.16）。我知道我必须在适当体积内对真实的（微观）电场求平均，所以让我画一个半径为 r 的球，比如说，半径为分子尺寸大小的 1000 倍。那么，r 处的宏观电场包含两部分：球体上所有外部电荷的平均电场，再加上球体所有内部电荷的平均电场：

$$
\pmb {E} = \pmb {E} _ {\text {外}} + \pmb {E} _ {\text {内}}
$$

![](images/e3ef81265d711095add4325b584200e69205a1f8a0f3cacdcaf37a5ab6fc9a05.jpg)  
图4.16

你在习题3.47d中已经证明了球体上由外部电荷产生的平均电场和它们在中心所产生的电场相等，所以 $\pmb{E}_{\text{外}}$ 就是球体外部的偶极子在 $\pmb{r}$ 处产生的电场。这些偶极子足够远，我

们可以放心地使用式 (4.9):

$$
V _ {\text {外}} = \frac {1}{4 \pi \varepsilon_ {0}} \int_ {\text {外部}} \frac {P (r ^ {\prime}) \cdot \hat {\mathbf {z}}}{r ^ {2}} \mathrm{d} \tau^ {\prime}\tag{4.17}
$$

球体内的偶极子太近，无法以这种方式处理。但很幸运，我们只需要它们的平均场，而不管球体内电荷分布的细节。根据式(3.105)，这个场为

$$
E _ {\text {内}} = - \frac {1}{4 \pi \varepsilon_ {0}} \frac {p}{R ^ {3}}
$$

唯一相关的量是总偶极矩 $p=\left(\frac{4}{3}\pi R^{3}\right)P$ :

$$
E _ {\text {内}} = - \frac {1}{3 \varepsilon_ {0}} P\tag{4.18}
$$

现在，假设球体足够小以至于在其体积上不会发生显著变化，因此式（4.17）中积分省略的项对应于均匀极化球体中心的电场，即： $-(1/3\varepsilon_{0})P$ [式（4.14)]。但这正是 $E_{内}$ [式（4.18）] 所给的！所以宏观电场由以下电势给出：

$$
V (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\boldsymbol {P} (\boldsymbol {r} ^ {\prime}) \cdot \hat {\boldsymbol {r}}}{\nu^ {2}} \mathrm{d} \tau^ {\prime}\tag{4.19}
$$

其中积分遍布电介质的整个体积。当然，这就是我们在第 4.2.1 节中使用过的；在没有理解的情况下，我们正确地计算了电介质内点的平均宏观场。

你可能需要重新阅读最后几段才能理解这个论点。请注意，这一切都反复围绕着一个奇怪的事实展开，即任何球体上的平均场（由内部电荷引起）总是和具有相同总电偶极矩的均匀极化球体中心的电场相同。这也就是说，无论实际的微观电荷结构如何复杂，如果我们只想知道它的宏观（平均）场，都可以用理想偶极子的平滑分布来代替它。顺便说一句，虽然这个论点表面上依赖于我选择球形来求平均，但宏观电场与平均区域的几何形状无关，这反映在式(4.19)中的最终结果上。也许，我们可用立方体、椭圆球或者其他任意形状来重复以上的论证——这样计算也许会更困难，但是结论是一样的。

## 4.3 电位移

## 4.3.1 有电介质时的高斯定理

在第 4.2 节中，我们发现极化的影响是产生（束缚）电荷的积累，即电介质内部 $\rho_{b} = -\nabla \cdot P$ 和在表面上 $\sigma_{b} = P \cdot \hat{n}$ 。介质的极化引起的电场就是这个束缚电荷的电场。现在我们准备把它放在一起：束缚电荷引起的场加上其他一切因素引起的电场（由于没有更好的术语，我们称之为自由电荷，free charge, $\rho_{f}$ ）。自由电荷可能由导体中的电子或者嵌入电介质材料中的离子或者其他任何电荷组成；换句话说，任何不是由极化产生的电荷。在电介质内，总电荷密度可以写为

$$
\rho = \rho_ {\mathrm{b}} + \rho_ {\mathrm{f}}\tag{4.20}
$$

高斯定律如下：

$$
\varepsilon_ {0} \nabla \cdot \boldsymbol {E} = \rho = \rho_ {\mathrm{b}} + \rho_ {\mathrm{f}} = - \nabla \cdot \boldsymbol {P} + \rho_ {\mathrm{f}}
$$

其中 E 现在是总电场，而不仅仅是由极化产生的部分电场。

将这两个散度项结合起来很方便：

$$
\nabla \cdot (\varepsilon_ {0} \boldsymbol {E} + \boldsymbol {P}) = \rho_ {\mathrm{f}}
$$

将括号中的表达式用字母 D 表示：

$$
\boxed {\boldsymbol {D} \equiv \varepsilon_ {0} \boldsymbol {E} + \boldsymbol {P}}\tag{4.21}
$$

这称为电位移（electric displacement）。用 D 可以把高斯定理写为

$$
\boxed {\nabla \cdot D = \rho_ {\mathrm{f}}}\tag{4.22}
$$

或者，用积分的形式，

$$
\oint \pmb {D} \cdot \mathrm{d} \pmb {a} = Q _ {\mathrm{f} \text {包含}}\tag{4.23}
$$

其中 $Q_{f包含}$ 表示包含在体积内的总的自由电荷。在电介质存在的情况下，这种形式的高斯定理是特别有用的，因为它只涉及自由电荷，并且自由电荷是我们可以控制的。束缚电荷随之而来：根据第 4.1 节中讨论的机制，当我们把自由电荷放在某处时，会自动地产生极化，这种极化将产生束缚电荷。因此，在实际的问题中，我们知道 $\rho_{f}$ ，但（最初）不知道 $\rho_{b}$ ；式 (4.23) 刚好就可以帮助我们使用这些信息进行计算。特别是，体系只要存在必要的对称性，我们就可以立即运用标准的高斯定理计算出 D。

![](images/f9e5d2f929bffd234de23c54bcbff110d87a81064d528311168b59c5afefaf99.jpg)  
图4.17

你可能已经发现我在推导式 (4.22) 时没有考虑表面束缚电荷 $\sigma_{\mathrm{b}}$ ，在某种意义上说也确实是这样。我们不能把高斯定理精确地应用到电介质的表面，因为此处的 $\rho_{\mathrm{b}}$ 趋于无穷大 $^6$ ，导致 $E$ 的散度也如此。但在其他的任何地方都是合理的；事实上，如果我们把电介质的边缘想象成具有有限厚度，在该厚度内极化逐渐减小到零（无论如何，这可能是一个比突然截止更现实的模型），那么就不存在所谓的表面束缚电荷；在这个“皮肤薄层”内 $\rho_{\mathrm{b}}$ 变化迅速但光滑，在任何地方应用高斯定理都是正确的。无论何种情况，式 (4.23) 的积分形式就没有这种“缺陷”。

习题4.15 厚球壳（内径为 $a$ ，外径为 $b$ ）由具有“冻结”极化的电介质材料制成，

$$
\boldsymbol {P} (\boldsymbol {r}) = \frac {k}{r} \hat {\boldsymbol {r}}
$$

其中 k 是常量，r 是距中心的距离（图 4.18）。（此问题中没有自由电荷）用两种不同的方法求三个区域的电场：

(a) 求所有的束缚电荷，并使用高斯定理 [式 (2.13)] 计算它产生的电场。

(b) 使用式 (4.23) 求出 $D$ ，然后从式 (4.21) 中求出 $E$ 。（请注意，第二种方法更快捷，而且避免了直接利用任何形式的束缚电荷。）

![](images/1107ac33f0684f4a1e286c099c26b59ca4a40d95d794e36aa2236de1a0f15e4a.jpg)  
图4.18

习题 4.16 假设一大块电介质内部的电场为 $E_{0}$ ，则电位移为 $D_{0} \equiv \varepsilon_{0} E_{0} + P$ 。

(a) 现在从材料中挖出一个小球形空腔（图 4.19a），由 $E_{0}$ 和 P 求空腔中心的电场。并由 $D_{0}$ 和 P 求空腔中心的位移。假设极化是“冻结的”，因此在空腔开挖时不会改变。

(b) 对平行于 P 的长针形空腔进行同样的计算（图 4.19b）。

(c) 对垂直于 P 的薄圆形空腔进行同样的计算（图 4.19c）。

假设上述空腔足够小，且基本均匀。[提示：挖一个空腔与叠加一个形状相同但极化相反的物体的效果是一样的。]

![](images/ddd5df7b934a8062ca5220da36c2fe6cfe819b3d96da8d962fccc14a4161f57a.jpg)  
图4.19

## 4.3.2 误导性的类比

式(4.22)看起来就像高斯定理，仅仅是自由电荷密度 $\rho_{\mathrm{f}}$ 替代了总电荷密度 $\rho$ 且 $D$ 取代了 $\varepsilon_0E$ 。出于这个原因，你或许会推断出 $D$ “宛如” $E$ （除了因子 $\varepsilon_0$ ），只是它的源电荷是 $\rho_{\mathrm{f}}$ 而不是 $\rho$ ：“为了解决电介质的问题，你可以完全不考虑束缚电荷——计算电场时和通常的做法一样，仅仅是在做答案时用 $D$ 替换掉 $E$ ”。这种论证很有诱惑力，但结论是错误的；特别是， $D$ 没有“库仑定律”：

$$
D (\boldsymbol {r}) \neq \frac {1}{4 \pi} \int \frac {\hat {\mathbf {r}}}{\nu^ {2}} \rho_ {\mathrm{f}} (\boldsymbol {r} ^ {\prime}) \mathrm{d} \tau^ {\prime}
$$

E 和 D 之间的对比关系比这更微妙。

仅由散度是不足以确定矢量场的；你还需要知道它的旋度。在静电场的情况下，人们往往会忘记这一点，因为 E 的旋度总是零。但 D 的旋度并不总是为零。

$$
\nabla \times \boldsymbol {D} = \varepsilon_ {0} (\nabla \times \boldsymbol {E}) + (\nabla \times \boldsymbol {P}) = \nabla \times \boldsymbol {P}\tag{4.25}
$$

一般来说，没有理由假设 P 的旋度为零。有时候它确实为零，比如在例题 4.4 和习题 4.15 中那样，但是更常见的情况并非如此。习题 4.11 的条形永电体就是一个很好的例子：在这里任何地方都没有自由电荷，所以如果你真的相信 D 的唯一来源是 $\rho_{f}$ ，你将被迫得出结论，任何地方的 D = 0，所以在电介质内部有 $E = (-1/\varepsilon_{0})P$ 且外部有 E = 0，这显然是错误的。（在这个问题中，我把那里的 $\nabla \times P \neq 0$ 的问题留给你自己。）此外，因为 $\nabla \times D \neq 0$ ，D 不能表示成标量的梯度——D 没有“电势”。

建议：当你要求计算电位移时，首先要寻找体系对称性。如果问题中出现球体、圆柱体或者平面对称性，那么你可以利用高斯定理，从式(4.23)直接求得 $D$ 。（显然在这种情况下， $\nabla \times P$ 自动满足为零，但由于仅由对称性就可以求出结果，你不必担心它的旋度。）如果体系不具备必需的对称性，你将不得不考虑其他的方法，特别是，你决不能假设 $D$ 完全是由自由电荷决定的。

## 4.3.3 边界条件

在第 2.3.5 节中的静电场边界条件可根据 D 重新确定。式 (4.23) 告诉我们垂直于界面的分量不连续：

$$
D _ {\text {上}} ^ {\perp} - D _ {\text {下}} ^ {\perp} = \sigma_ {\mathrm{f}}\tag{4.26}
$$

而式 (4.25) 给出了平行分量的不连续:

$$
D _ {\text {上}} ^ {\parallel} - D _ {\text {下}} ^ {\parallel} = P _ {\text {上}} ^ {\parallel} - P _ {\text {下}} ^ {\parallel}\tag{4.27}
$$

在电介质存在的情况下，和电场 E 的相应的边界条件相比 [式 (2.31) 和式 (2.23)]，这些方程显得更有用：

$$
E _ {\mathrm{上}} ^ {\perp} - E _ {\mathrm{下}} ^ {\perp} = \frac {1}{\varepsilon_ {0}} \sigma\tag{4.28}
$$

和

$$
\pmb {E} _ {\text {上}} ^ {\parallel} - \pmb {E} _ {\text {下}} ^ {\parallel} = 0\tag{4.29}
$$

例如，你可以尝试将它们应用于习题 4.16 和习题 4.17。

习题 4.17 对于习题 4.11 中的条形永电体，仔细绘制三张草图：一个关于 P，一个关于 E，另一个关于 D。假设 L 约为 2a。[提示：E 线止于电荷；D 线止于自由电荷。]

## 4.4 线性电介质

## 4.4.1 电极化率、介电常数和相对介电常数

在第 4.2 节和第 4.3 节中，我们并没有关注 P 的起因；我们仅仅讨论了极化的影响。然而，从第 4.1 节的定性讨论中，我们知道电介质的极化通常是由电场引起的，电场使原子或分子中的偶极子沿直线排列起来。事实上，只要不是特别强，很多物质的极化强度与电场是成正比的：

$$
\pmb {P} = \varepsilon_ {0} \chi_ {\mathrm{e}} \pmb {E}\tag{4.30}
$$

比例常数 $\chi_{e}$ 称为介质的电极化率（electric susceptibility）(提取 $\varepsilon_{0}$ 因子使 $\chi_{e}$ 无量纲)。 $\chi_{e}$ 的值与所研究材料的微观结构有关（也与温度等外部条件有关）。我将把满足式 (4.30) 的材料称为线性电介质（linear dielectrics） $^{7}$ 。

请注意，式(4.30)中的 E 是总电场；一部分可能是由自由电荷引起的，一部分是由极化本身引起的。例如，如果我们将一块电介质放入外场 $E_{0}$ 中，就无法直接通过式(4.30)计算 P；这个外电场将使材料极化，并且这种极化将产生自己的电场，然后会对总电场有贡献，而且它反过来又会改变材料的极化，如此反复……打破这种无休止的重复并不是那么容易的。稍后你将看到一些例子。最简单的方法是从电位移开始，在这些情况下至少D可以直接从自由电荷分布导出。

在线性介质中，我们有

$$
\pmb {D} = \varepsilon_ {0} \pmb {E} + \pmb {P} = \varepsilon_ {0} \pmb {E} + \varepsilon_ {0} \chi_ {\mathrm{e}} \pmb {E} = \varepsilon_ {0} (1 + \chi_ {\mathrm{e}}) \pmb {E}\tag{4.31}
$$

因此 D 也与 E 成正比:

$$
\boldsymbol {D} = \varepsilon \boldsymbol {E}\tag{4.32}
$$

其中

$$
\varepsilon \equiv \varepsilon_ {0} (1 + \chi_ {\mathrm{e}})\tag{4.33}
$$

这个新常数 $\varepsilon$ 称为材料的介电常数（permittivity）。[在真空中，没有物质可以极化，极化率为零，介电常数为 $\varepsilon_0$ ，这就是为什么 $\varepsilon_0$ 被称为真空介电常数（permittivity of free space）。我不喜欢这个词，因为它表明真空只是一种特殊的线性电介质，其中介电常数恰好为 $8.85 \times 10^{-12} \mathrm{C}^2 / \mathrm{N} \cdot \mathrm{m}^2$ 。] 如果你去掉一个系数 $\varepsilon_0$ ，剩下的无量纲量

$$
\varepsilon_ {\mathrm{r}} \equiv 1 + \chi_ {\mathrm{e}} = \frac {\varepsilon}{\varepsilon_ {0}}\tag{4.34}
$$

称为材料的相对介电常数（relative permittivity）或介电常数。表4.2列出了一些常见物质的介电常数。（请注意，对于一般材料，所有的 $\varepsilon_{\mathrm{r}}$ 都大于1。）当然，介电常数和相对介电常数并没有较极化率提供更多的任何信息，式(4.32)中也没有任何实质的新内容；线性电介质的所有物理本质都包含在式(4.30)中8。

表 4.2 介电常数（除非有特殊说明，均为在 1atm 和 20°C 条件下的数值）  
来源：《物理化学手册》（第91版）(Boca Raton: CRC Press, 2010)

<table><tr><td>材料</td><td>相对介电常数</td><td>材料</td><td>相对介电常数</td></tr><tr><td>真空</td><td>1</td><td>苯</td><td>2.28</td></tr><tr><td>氦</td><td>1.000065</td><td>金刚石</td><td>5.7~5.9</td></tr><tr><td>氖</td><td>1.00013</td><td>盐</td><td>5.9</td></tr><tr><td>氢( $H_2$ )</td><td>1.000254</td><td>硅</td><td>11.7</td></tr><tr><td>氩</td><td>1.000517</td><td>甲醇</td><td>33.0</td></tr><tr><td>空气(干燥)</td><td>1.000536</td><td>水</td><td>80.1</td></tr><tr><td>氮( $N_2$ )</td><td>1.000548</td><td>冰(-30°C)</td><td>104</td></tr><tr><td>水蒸气(100°C)</td><td>1.00589</td><td> $KTaNbO_3$ (0°C)</td><td>34,000</td></tr></table>

例题4.5 半径为 $a$ 的金属球带电量为 $Q$ （图4.20）。它被介电常数为 $\varepsilon$ 的线性电介质包裹，外半径为 $b$ 。求中心的电势（相对于无穷远处）。

![](images/952de4eaa9f665f647fee14572af59c58693cb429926ca777afbb36f4660c120.jpg)  
图4.20

[解答] 为了计算 $V$ ，我们需要知道 $\pmb{E}$ ；为了求出 $\pmb{E}$ ，我们可以首先尝试确定束缚电荷；我们能够从 $\pmb{P}$ 中得到束缚电荷，但除非能够知道 $\pmb{E}$ ，否则我们是无法计算 $\pmb{P}$ 的 [式 (4.30)]。我们似乎陷入了困境。我们所知道的是自由电荷 $Q$ ，幸运地，它的排列呈球对称分布的，所以让我们从式 (4.23) 计算 $\pmb{D}$ 开始：

$D = \frac{Q}{4\pi r^2}\hat{r},$ 对 $r > a$ 的所有点

（当然，在金属球内部有 $E = P = D = 0$ 。）一旦知道了 $D$ ，就可以轻而易举得到 $E$ ，利用式(4.32):

$$
\boldsymbol {E} = \left\{ \begin{array}{l l} \frac {Q}{4 \pi \varepsilon r ^ {2}} \hat {\boldsymbol {r}}, & a <   r <   b \\ \frac {Q}{4 \pi \varepsilon_ {0} r ^ {2}} \hat {\boldsymbol {r}}, & r > b \end{array} \right.
$$

因此，中心的电势为

$$
\begin{array}{r l} & {V = - \int_ {\infty} ^ {0} \pmb {E} \cdot \mathrm{d} \pmb {l} = - \int_ {\infty} ^ {b} \frac {Q}{4 \pi \varepsilon_ {0} r ^ {2}} \mathrm{d} r - \int_ {b} ^ {a} \frac {Q}{4 \pi \varepsilon r ^ {2}} \mathrm{d} r - \int_ {a} ^ {0} (0) \mathrm{d} r} \\ & {\qquad = \frac {Q}{4 \pi} \left(\frac {1}{\varepsilon_ {0} b} + \frac {1}{\varepsilon a} - \frac {1}{\varepsilon b}\right)} \end{array}
$$

事实证明，我们没有必要明确计算极化强度或者束缚电荷，尽管这很容易做到：

$$
\pmb {P} = \varepsilon_ {0} \chi_ {\mathrm{e}} \pmb {E} = \frac {\varepsilon_ {0} \chi_ {\mathrm{e}} Q}{4 \pi \varepsilon r ^ {2}} \hat {\pmb {r}}
$$

在电介质中，因此

$$
\rho_ {\mathrm{b}} = - \nabla \cdot P = 0
$$

这里

1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

$$
\sigma_ {\mathrm{b}} = P \cdot \hat {n} = \left\{ \begin{array}{l l} {{\frac {\varepsilon_ {0} \chi_ {\mathrm{e}} Q}{4 \pi \varepsilon b ^ {2}},}} & {{\text {外表面}}} \\ {{\frac {- \varepsilon_ {0} \chi_ {\mathrm{e}} Q}{4 \pi \varepsilon a ^ {2}},}} & {{\text {内表面}}} \end{array} \right.
$$

请注意，a 处的表面束缚电荷为负（ $\hat{n}$ 相对于电介质指向外面，b 处为 $+\hat{r}$ ，a 处为 $-\hat{r}$ ）。这是很正常的，因为金属球上的电荷会吸引所有电介质中的异号电荷。正是这个负电荷层将电介质内的电场从 $1/4\pi\varepsilon_0(Q/r^2)\hat{r}$ 减少到 $1/4\pi\varepsilon(Q/r^2)\hat{r}$ 。从这个方面来讲，电介质很像一个非完美的导体：在导体壳中的表面感应电荷将完全抵消 $a < r < b$ 范围内 $Q$ 的电场；然而电介质虽尽其所能，依然只能抵消一部分。

你或许会认为线性电介质避开了 E 和 D 之间类比时出现的问题。既然现在 P 和 D 都与 E 成正比，那么它们的旋度为什么不能像 E 一样也为零？遗憾的是事实并非如此，尽管在跨越两种材料之间的边界的闭合路径上的线积分 E 一定是零，P 在同一环路上的积分不一定为零，原因在于界面两侧的比例系数 $\varepsilon_{0}\chi_{e}$ 是不同的。例如，在极化电介质和真空之间的界面处（图 4.21），P 在一侧为零，但在另一侧不为零。沿此环路有 $\oint P \cdot dl \neq 0$ ，因此，根据斯托克斯定理，P 的旋度不可能在环路上任何地方都为零（事实上，它在边界处是无穷大） $^{9}$ 。

![](images/784b8a662edf86112db5915becc12645e13929b4ff1aea7fc0fa6c92884d02c9.jpg)  
图4.21

当然，如果空间完全充满了均匀的线性电介质 $^{10}$ ，在这种相当特殊的情况下，则就不存在这个问题：

$$
\nabla \cdot \pmb {D} = \rho_ {\mathrm{f}} \quad \text {且} \quad \nabla \times \pmb {D} = \mathbf {0}
$$

所以，如同电介质不存在一样， $D$ 可以通过自由电荷求出：

$$
D = \varepsilon_ {0} E _ {\mathrm{真空}}
$$

其中 $E_{真空}$ 是在真空情况下，由同样的自由电荷分布产生的电场。根据式 (4.32) 和式 (4.34) 有

$$
\pmb {E} = \frac {1}{\varepsilon} \pmb {D} = \frac {1}{\varepsilon_ {\mathrm{r}}} \pmb {E} _ {\mathrm{真空}}\tag{4.35}
$$

结论：当所有空间都充满均匀线性电介质时，各处的电场将会减小为原来的 $1/\varepsilon_{r}$ 倍。（事实上，电介质不必充满所有空间：因为在电场为零的地方，任何情况下都不会出现极化，电介质的存在与否几乎无关紧要。）

例如，若将自由电荷 $q$ 嵌入一大块电介质中，它产生的电场为

$$
\pmb {E} = \frac {1}{4 \pi \varepsilon} \frac {q}{r ^ {2}} \hat {\pmb {r}}\tag{4.36}
$$

（这里分母是 $\varepsilon$ ，而不是 $\varepsilon_{0}$ 。）并且作用在附近电荷上的力相应地减小。但这并不是说库仑定律有什么问题；相反，自由电荷则被介质中有相反符号的束缚电荷包围起来，即介质的极化部分地“屏蔽”了该电荷（图 4.22） $^{11}$ 。

![](images/d155177684f2a4675e4f0f78bbf6bddb806666c4fed063cd93ee389f332f3e5a.jpg)  
图4.22

例题4.6 平行板电容器（图4.23）充满有相对介电常数为 $\varepsilon_{\mathrm{r}}$ 的绝缘材料。这对其电容有什么影响？

[解答] 由于电场被限制在两金属板之间，电介质将使电场 E 减少至原来的 $1/\varepsilon_{r}$ ，同时使电势差 V 减少至原来的 $1/\varepsilon_{r}$ 。因此，电容 C = Q/V 将会增大 $\varepsilon_{r}$ 倍：

……

$\begin{array}{ccccccccc}\mathrm{hs} &  & 1 &  & \bullet & = & 1 & \bullet & = & = \\  &  & 1 & \infty & \bullet & = & 1 & \bullet & = & \bullet \\ \vdots & = & \vdots & \ddots & \bullet & = & 1 & \bullet & \ddots & \bullet \\ \vdots & & \vdots & \ddots & 1 &  &  & \bullet & \bullet \\ \vdots & &  &  &  &  &  &  & \bullet \\ \end{array}$

$$
C = \varepsilon_ {\mathrm{r}} C _ {\mathrm{真空}}\tag{4.37}
$$

事实上，这是增大电容量的常见方法。

![](images/66f7747739d52e391095bc22808d366768f74e8fa92b312eaa3483ab987f9806.jpg)

晶体在某些方向上通常比在其他方向上更容易极化 $^{12}$ ，在这种情况下，式(4.30)要被更普遍的线性关系所取代：

$$
\left. \begin{array}{l} P _ {x} = \varepsilon_ {0} (\chi_ {\mathrm{e} _ {x x}} E _ {x} + \chi_ {\mathrm{e} _ {x y}} E _ {y} + \chi_ {\mathrm{e} _ {x z}} E _ {z}) \\ P _ {y} = \varepsilon_ {0} (\chi_ {\mathrm{e} _ {y x}} E _ {x} + \chi_ {\mathrm{e} _ {y y}} E _ {y} + \chi_ {\mathrm{e} _ {y z}} E _ {z}) \\ P _ {z} = \varepsilon_ {0} (\chi_ {\mathrm{e} _ {z x}} E _ {x} + \chi_ {\mathrm{e} _ {z y}} E _ {y} + \chi_ {\mathrm{e} _ {z z}} E _ {z}) \end{array} \right\}\tag{4.38}
$$

正如对于非对称分子，式 (4.1) 被式 (4.3) 所取代一样。九个系数 $\chi_{e_{xx}}, \chi_{e_{xy}}, \cdots$ 构成了极化率张量（susceptibility tensor）。

习题4.18 平行板电容器极板之间填充了两块线性电介质材料（图4.24）。每块的厚度为 $a$ ，所以电容器两板之间的距离为 2a。板 1 和板 2 的介电常数分别为 2 和 1.5。顶板和底板上的自由电荷密度分别为 $\sigma$ 和 $-\sigma$ 。

![](images/d2aadf1fef94b14e589ab2258b43ebd4cf3e97c59e887a67824c91d17f465471.jpg)  
图4.25

(a) 求板 1 和板 2 中的电位移 D。

(b) 求板 1 和板 2 中的电场 E。

(c) 求板 1 和板 2 中的极化强度 P。

(d) 求两平板之间的电势差。

(e) 求所有束缚电荷的位置和大小。

(f) 现在你已经知道了所有的电荷（自由电荷和束缚电荷），请重新计算每块电介质中的电场，并验证（b）中的答案。

![](images/1a81a88b7be2ce99fcbafd47ee5cea624b6a4977d7becde588b3054b1adccfd4.jpg)  
图4.24

习题 4.19 假设你有足够的介电常数为 $\varepsilon_{r}$ 的线性电介质材料，用它来填充电容器两个极板之间空间的一半，如图 4.25 所示。当按照图 4.25a 所示结构填充材料时，电容增加了多少？对于图 4.25b 所示的填充，结果又如何？对于给定的电容器两板之间电势 V，求每个区间内的 E、D、P 的大小，并在这两种情况下求出所有表面的自由电荷和束缚电荷。

习题4.20 一线性介电材料球中嵌入均匀的自由电荷密度 $\rho$ 。若球的半径为 $R$ ，介电常数为 $\varepsilon_{\mathrm{r}}$ ，求球体中心的电势（相对于无穷远处）。

习题 4.21 一种同轴电缆由半径为 a 的铜线和内径为 c 的同心铜管组成（图 4.26）。两者之间的空间部分填充有介电常数为 $\varepsilon_{r}$ 的材料（从 b 到 c），求该电缆每单位长度上的电容。

![](images/a2dd0c1d081f6934495cf1f1006893f0f5ca2562240836573cdb4f727dab9502.jpg)  
图4.26

## 4.4.2 线性电介质的边界值问题

在均匀各向同性的线性电介质中，束缚电荷密度 $\rho_{\mathrm{b}}$ 正比于自由电荷密度 $\rho_{\mathrm{f}}^{13}$

$$
\rho_ {\mathrm{b}} = - \nabla \cdot \boldsymbol {P} = - \nabla \cdot \left(\varepsilon_ {0} \frac {\chi_ {\mathrm{e}}}{\varepsilon} \boldsymbol {D}\right) = - \left(\frac {\chi_ {\mathrm{e}}}{1 + \chi_ {\mathrm{e}}}\right) \rho_ {\mathrm{f}}\tag{4.39}
$$

特别是，除非自由电荷是真的嵌入电介质材料中，否则 $\rho = 0$ ，任何净电荷都必须存在于电介质的表面。因此，在这种电介质中，电势遵循拉普拉斯方程，第三章中描述的所有的机制都同样适用。不过根据电荷密度与自由电荷的关系，我们可以把边值关系[式(4.26)]简写成只依赖于自由电荷的函数：然而，仅以自由电荷的形式重写边界条件是很方便的。由式(4.26)，

$$
\varepsilon_ {\mathrm{上}} E _ {\mathrm{上}} ^ {\perp} - \varepsilon_ {\mathrm{下}} E _ {\mathrm{下}} ^ {\perp} = \sigma_ {\mathrm{f}}\tag{4.40}
$$

或者（用电势表示）：

$$
\varepsilon_ {\mathrm{上}} \frac {\partial V _ {\mathrm{上}}}{\partial n} - \varepsilon_ {\mathrm{下}} \frac {\partial V _ {\mathrm{下}}}{\partial n} = - \sigma_ {\mathrm{f}}\tag{4.41}
$$

当然，电势本身是连续的 [式 (2.34)]:

$$
V _ {\text {上}} = V _ {\text {下}}\tag{4.42}
$$

例题 4.7 将一均匀的线性介质球置于匀强电场 $E_{0}$ 中（图 4.27）。求球内电场强度。

![](images/6dc752b506e08eada4e8cedae718fde0fc9470767aee9d3a8464494b199d6b04.jpg)  
图4.27

$^{13}$ 这不适用于表面电荷 $\sigma_{b}$ ，因为 $\chi_{e}$ 与边界处的位置显然无关。

[解答] 这使人回想起例题3.8，其中把一不带电的导体球置于均匀的外场中，这种情况下，在导体球内部感应电荷形成的电场与外电场 $E_0$ 完全抵消。在电介质中，来自束缚电荷形成的电场只是部分抵消。

我们的问题是在满足下面边界条件情况下求解拉普拉斯方程，即当 $r \leqslant R$ 时， $V_{\text{内}}(r, \theta)$ ；和当 $r \geqslant R$ 时， $V_{\text{外}}(r, \theta)$ ，

(i)

$$
V _ {\text {内}} = V _ {\text {外}}, \qquad r = R\tag{ii}
$$

$$
\varepsilon \frac {\partial V _ {\text {内}}}{\partial r} = \varepsilon_ {0} \frac {\partial V _ {\text {外}}}{\partial r}, \quad r = R\tag{4.43}
$$

(iii)

其中第二个条件是由式（4.41）给出的，因为在电介质表面不存在自由电荷。在介质球内，式（3.65）表示为

$$
V _ {\text {内}} (r, \theta) = \sum_ {l = 0} ^ {\infty} A _ {l} r ^ {l} P _ {l} (\cos \theta)\tag{4.44}
$$

在介质球外，根据边界条件（iii）我们有

• = 1 • = 1 = = = 1
= 1 • = = = = 1
• = 1 • = 1 • = 1
• = 1 • = 1

$$
V _ {\text {外}} (r, \theta) = - E _ {0} r \cos \theta + \sum_ {l = 0} ^ {\infty} \frac {B _ {l}}{r ^ {l + 1}} P _ {l} (\cos \theta)\tag{4.45}
$$

边界条件（i）要求

$$
\sum_ {l = 0} ^ {\infty} A _ {l} R ^ {l} P _ {l} (\cos \theta) = - E _ {0} R \cos \theta + \sum_ {l = 0} ^ {\infty} \frac {B _ {l}}{R ^ {l + 1}} P _ {l} (\cos \theta)
$$

$$
1 4
$$

$$
\left. \begin{array}{l} {A _ {l} R ^ {l} =  \frac {B _ {l}}{R ^ {l + 1}}, \quad \text {对}   l \neq 1} \\ {A _ {1} R = - E _ {0} R +  \frac {B _ {1}}{R ^ {2}}} \end{array} \right\}\tag{4.46}
$$

同时，边界条件（ii）给出

$$
\varepsilon_ {\mathrm{r}} \sum_ {l = 0} ^ {\infty} A _ {l} R ^ {l - 1} P _ {l} (\cos \theta) = - E _ {0} \cos \theta + \sum_ {l = 0} ^ {\infty} \frac {(l + 1) B _ {l}}{R ^ {l + 2}} P _ {l} (\cos \theta)
$$

所以

$$
\left. \begin{array}{l} {{\varepsilon_ {r} l A _ {l} R ^ {l - 1} = - \frac {(l + 1) B _ {l}}{R ^ {l + 2}}, \quad \text {对}   l \neq 1}} \\ {{\varepsilon_ {r} A _ {1} = - E _ {0} - \frac {2 B _ {1}}{R ^ {3}}}} \end{array} \right\}\tag{4.47}
$$

由此可见

$$
\left. \begin{array}{l l} {{A _ {l} = B _ {l} = 0,}} & {{\mathrm{对} l \neq 1}} \\ {{A _ {1} = - \frac {3}{\varepsilon_ {\mathrm{r}} + 2} E _ {0},}} & {{B _ {1} = \frac {\varepsilon_ {\mathrm{r}} - 1}{\varepsilon_ {\mathrm{r}} + 2} R ^ {3} E _ {0}}} \end{array} \right\}\tag{4.48}
$$

明显地

$$
V _ {\text {内}} (r, \theta) = - \frac {3 E _ {0}}{\varepsilon_ {\mathrm{r}} + 2} r \cos \theta = - \frac {3 E _ {0}}{\varepsilon_ {\mathrm{r}} + 2} z
$$

因此，球内的电场（令人吃惊的）是均匀的：

$$
\pmb {E} = \frac {3}{\varepsilon_ {\mathrm{r}} + 2} \pmb {E} _ {0}\tag{4.49}
$$

例题4.8 假设图4.28中 $z = 0$ 平面以下的整个区域填充有极化率为 $\chi_{\mathrm{e}}$ 的均匀线性介电材料。计算在位于原点上方距离为 $d$ 处的点电荷 $q$ 所受的力。

![](images/7e90744db651d2c837f80a3b612cb1fb308a8fdad66ea7cce0882f604ada0a22.jpg)  
图4.28

[解答] $xy$ 平面上的表面束缚电荷与 $q$ 的符号相反，所以 $q$ 受到引力作用。[根据式 (4.39)，不存在体束缚电荷。] 我们首先利用式 (4.11) 和式 $(4.30)^{15}$ 计算出表面电荷密度 $\sigma_{\mathrm{b}}$ ：

$$
\sigma_ {\mathrm{b}} = P \cdot \widehat {n} = P _ {z} = \varepsilon_ {0} \chi_ {\mathrm{e}} E _ {z}
$$

其中， $E_{z}$ 是电介质内部总电场的 $z$ 方向分量。该电场一部分由电荷 $q$ 产生，另一部分由束缚电荷本身产生。根据库仑定律，前者的贡献是

$$
- \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{(r ^ {2} + d ^ {2})} \cos \theta = - \frac {1}{4 \pi \varepsilon_ {0}} \frac {q d}{(r ^ {2} + d ^ {2}) ^ {3 / 2}}
$$

其中 $r = \sqrt{x^2 + y^2}$ 是距原点的距离。与此同时，束缚电荷电场的 $z$ 分量是 $-\sigma_{\mathrm{b}} / 2\varepsilon_0$ [参见式(2.33)后的脚注]。所以

$$
\sigma_ {\mathrm{b}} = \varepsilon_ {0} \chi_ {\mathrm{e}} \left[ - \frac {1}{4 \pi \varepsilon_ {0}} \frac {q d}{(r ^ {2} + d ^ {2}) ^ {3 / 2}} - \frac {\sigma_ {\mathrm{b}}}{2 \varepsilon_ {0}} \right]
$$

我们可以求解 $\sigma_{\mathrm{b}}$

$$
\sigma_ {\mathrm{b}} = - \frac {1}{2 \pi} \left(\frac {\chi_ {\mathrm{e}}}{\chi_ {\mathrm{e}} + 2}\right) \frac {q d}{(r ^ {2} + d ^ {2}) ^ {3 / 2}}\tag{4.50}
$$

除了系数 $\chi_{\mathrm{e}} / (\chi_{\mathrm{e}} + 2)$ 之外，该式与相似情况下的无穷大导体平面上的感应电荷完全相同[式(3.10)]16。显然，总束缚电荷是

$$
q _ {\mathrm{b}} = - \left(\frac {\chi_ {\mathrm{e}}}{\chi_ {\mathrm{e}} + 2}\right) q\tag{4.51}
$$

当然，我们可以通过直接积分得到 $\sigma_{b}$ 的电场

$$
\boldsymbol {E} = \frac {1}{4 \pi \varepsilon_ {0}} \int \left(\frac {\hat {\mathbf {r}}}{\mathbf {r} ^ {2}}\right) \sigma_ {\mathrm{b}} \mathrm{d} a
$$

但是，与导体平面的情况一样，可通过更简洁的镜像法来求解。的确，若在 $(0,0, - d)$ 处用一个的镜像点电荷 $(q_{\mathrm{b}})$ 替代电介质 $(q_{\mathrm{b}})$ 的话，在 $z > 0$ 的区域，我们得到

$$
V = \frac {1}{4 \pi \varepsilon_ {0}} \left[ \frac {q}{\sqrt {x ^ {2} + y ^ {2} + (z - d) ^ {2}}} + \frac {q _ {\mathrm{b}}}{\sqrt {x ^ {2} + y ^ {2} + (z + d) ^ {2}}} \right]\tag{4.52}
$$

同时， $(0,0,d)$ 处的电荷 $(q + q_{\mathrm{b}})$ 在 $z < 0$ 区域产生电势为

$$
V = \frac {1}{4 \pi \varepsilon_ {0}} \left[ \frac {q + q _ {\mathrm{b}}}{\sqrt {x ^ {2} + y ^ {2} + (z + d) ^ {2}}} \right]\tag{4.53}
$$

综上所述，式(4.52)和式(4.53)构成点电荷位于 $(0,0,d)$ 处的泊松方程。它满足在无穷远处为零、在边界 $z = 0$ 处连续，以及电势的法向导数表现出与 $z = 0$ 处表面电荷 $\sigma_{\mathrm{b}}$ 相应的不连续性：

$$
- \varepsilon_ {0} \left(\frac {\partial V}{\partial z} \bigg | _ {z = 0 ^ {+}} - \frac {\partial V}{\partial z} \bigg | _ {z = 0 ^ {-}}\right) = - \frac {1}{2 \pi} \left(\frac {\chi_ {\mathrm{e}}}{\chi_ {\mathrm{e}} + 2}\right) \frac {q d}{(x ^ {2} + y ^ {2} + d ^ {2}) ^ {3 / 2}}
$$

因此，该电势就是我们问题的正确结果。特别地， $q$ 所受的力是

$$
\boldsymbol {F} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q q _ {\mathrm{b}}}{(2 d) ^ {2}} \hat {\boldsymbol {z}} = - \frac {1}{4 \pi \varepsilon_ {0}} \left(\frac {\chi_ {\mathrm{e}}}{\chi_ {\mathrm{e}} + 2}\right) \frac {q ^ {2}}{4 d ^ {2}} \hat {\boldsymbol {z}}\tag{4.54}
$$

就像所有的镜像解法一样，我并不认为这里为式(4.52)和式(4.53)提供了一个令人信服的理由。这个方程的合理性在于它有效：它求解了泊松方程，并且满足边界条件。尽管如此，得到镜像解并不完全是一个猜测的问题。至少有两条“游戏规则”：（1）你绝不能把镜像电荷放置在要计算电势的区域里[式(4.52)描述 $z > 0$ 区域的电势，但镜像电荷应放置在 $z = -d$ 处；当我们转向求 $z < 0$ 区域的电势时[式(4.53)]，镜像电荷 $(q + q_{\mathrm{b}})$ 放置在 $z = d$ 处。](2)每个区域镜像电荷的总和必须正确。[这也是我如何知道用 $q_{\mathrm{b}}$ 代替 $z < 0$ 区域里的电荷，用 $(q + q_{\mathrm{b}})$ 代替 $z > 0$ 区域里的电荷。]

习题4.22 将一很长的线性电介质材料圆柱体置于匀强电场 $E_0$ 中，求圆柱体内的电场。（圆柱体半径为 $a$ ，极化率为 $\chi_{\mathrm{e}}$ ，轴线与 $E_0$ 垂直。）

习题 4.23 通过以下逐次逼近法，求位于匀强电场 $E_{0}$ 中的线性介质球内的电场（例题 4.7）：首先，假设介质球内部的电场仅为 $E_{0}$ ，利用式 (4.30) 得到极化强度 $P_{0}$ 。该极化产生一个自己的电场 $E_{1}$ （例题 4.2），这反过来又将极化改变了 $P_{1}$ ，进而又将电场改变了 $E_{2}$ ，以此类推。最终得到的电场是 $E_{0} + E_{1} + E_{2} + \cdots$ 。将级数求和，并将你的结果与式 (4.49) 进行比较。

习题4.24 半径为 $a$ 的不带电导体球在半径为 $b$ 的范围内覆有一层很厚的绝缘球壳（介电常数为 $\varepsilon_{\mathrm{r}}$ ）。现将该球体置于均匀的电场 $E_0$ 中。求绝缘球壳中的电场。

习题 4.25 假设在例题 4.8 中 xy 平面上方的区域也填充有线性电介质，但极化率 $\chi_{e}^{\prime}$ 不同。求空间所有地方的电势。

## 4.4.3 介电系统的能量

给电容充电需要做功 [式 (2.55)]:

$$
W = \frac {1}{2} C V ^ {2}
$$

如果电容器填充有线性电介质，正如例题4.6所给出的那样，则其电容大小为真空值的介电常数倍：

$$
C = \varepsilon_ {\mathrm{r}} C _ {\mathrm{真空}}
$$

显然，给充满介质的电容器充电所需要做的功也增加相同的倍数。原因很明显：极板上为了达到给定的电势，你必须注入更多的（自由）电荷，因为电场被束缚电荷抵消掉一部分。在第2章中，我已经推导出任何静电系统中储能的一般公式[式(2.45)]：

$$
W = \frac {\varepsilon_ {0}}{2} \int E ^ {2} \mathrm{d} \tau\tag{4.55}
$$

对于电容器充满线性电介质的情况下，应该将其改为

$$
W = \frac {\varepsilon_ {0}}{2} \int \varepsilon_ {\mathrm{r}} E ^ {2} \mathrm{d} \tau = \frac {1}{2} \int \boldsymbol {D} \cdot \boldsymbol {E} \mathrm{d} \tau
$$

为了证明这一点，假设电介质材料的位置是固定的，我们一次引入一点点自由电荷。当电荷 $\rho_{f}$ 增加了 $\Delta\rho_{f}$ 时，极化将发生变化，束缚电荷分布也将随之改变。但我们只对自由电荷增量所需要做的功感兴趣：

$$
\Delta W = \int (\Delta \rho_ {\mathrm{f}}) V \mathrm{d} \tau\tag{4.56}
$$

因为 $\nabla \cdot D = \rho_{\mathrm{f}}, \Delta \rho_{\mathrm{f}} = \nabla \cdot (\Delta D)$ ，其中 $\Delta D$ 是 $D$ 改变量，所以

$$
\Delta W = \int [ \nabla \cdot (\Delta D) ] V \mathrm{d} \tau
$$

这样一来，

$$
\nabla \cdot [ (\Delta D) V ] = [ \nabla \cdot (\Delta D) ] V + \Delta D \cdot (\nabla V)
$$

因此（分部积分）

$$
\Delta W = \int \nabla \cdot [ (\Delta D) V ] \mathrm{d} \tau + \int (\Delta D) \cdot E \mathrm{d} \tau
$$

散度定理将第一项转化为曲面积分，如果我们在整个空间上进行积分，则该积分为零。因此，所做的功为

$$
\Delta W = \int (\Delta D) \cdot E \mathrm{d} \tau\tag{4.57}
$$

至此，上式适用于任何材料。现在，如果电介质是线性电介质，有 $D = \varepsilon E$ ，对于无穷小的改变量：

$$
\frac {1}{2} \Delta (\boldsymbol {D} \cdot \boldsymbol {E}) = \frac {1}{2} \Delta (\varepsilon E ^ {2}) = \varepsilon (\Delta \boldsymbol {E}) \cdot \boldsymbol {E} = (\Delta \boldsymbol {D}) \cdot \boldsymbol {E}
$$

所以

$$
\Delta W = \Delta \left(\frac {1}{2} \int \pmb {D} \cdot \pmb {E} \mathrm{d} \tau\right)
$$

如预期一样 $^{17}$ ，当电容器极板上的自由电荷从零开始增加到最终值，做的总功是

$$
W = \frac {1}{2} \int \boldsymbol {D} \cdot \boldsymbol {E} \mathrm{d} \tau\tag{4.58}
$$

我们在第 2 章中推导的普适公式在电介质存在情况下不再适用，而它需要用式 (4.58) 替代，这或许让你感到困惑。问题的关键不是说这两个方程中某一个是错的，而是说它们针对的是不同的问题。这种区别是微妙的，所以让我们回到问题的开头：我们所说的“系统的能量”指的是什么？答：它是构建系统所需的功。非常正确，但当涉及电介质时，我们有两种截然不同的方式来理解这个过程：

1. 我们用镊子一个接一个地把全部电荷（自由电荷和束缚电荷）带进电介质，然后把每一个都粘在适当的最终位置。如果这就是你所讲的“构建系统”的话，那么式(4.55)就是系统存储能量的公式。但请注意，这个能量并不包括延伸和扭转电介质分子所做的功。（如果我们把正电荷和负电荷想象成由微小的弹簧连接在一起，它不包括与每个分子极化相关的弹性动能 $\frac{1}{2} kx^2$ 。） $^{18}$

2. 在电介质没有发生极化的情况下，我们一个接一个地引入自由电荷，使电介质能够随所引入的电荷而做出响应。如果这就是“构建系统”的意思（通常是这样的过程，因为只有自由电荷才是我们实际能差来遣去的东西），那么式(4.58)就是你所想要的公式。在这种情形下，“弹簧”存储的能量被包括在内，尽管是间接的。因为对自由电子所施加的力取决于束缚电荷的位置。当你移动自由电子时，你会自动拉伸那些“弹簧”。

例题4.9 半径为 $R$ 的球体填充有介电常数为 $\varepsilon_{\mathrm{r}}$ 的介电材料和均匀嵌入的自由电荷密度 $\rho_{\mathrm{f}}$ 。该体系的能量是多少？

[解答] 根据高斯定理 [用式 (4.23) 的形式], 电位移为

$$
D (r) = \left\{ \begin{array}{l l} \frac {\rho_ {\mathrm{f}}}{3} r & (r <   R) \\ \frac {\rho_ {\mathrm{f}}}{3} \frac {R ^ {3}}{r ^ {2}} \hat {r} & (r > R) \end{array} \right.
$$

所以电场是

$$
\boldsymbol {E} (\boldsymbol {r}) = \left\{ \begin{array}{l l} \frac {\rho_ {\mathrm{f}}}{3 \varepsilon_ {0} \varepsilon_ {\mathrm{r}}} \boldsymbol {r} & (r <   R) \\ \frac {\rho_ {\mathrm{f}}}{3 \varepsilon_ {0}} \frac {R ^ {3}}{r ^ {2}} \hat {\boldsymbol {r}} & (r > R) \end{array} \right.
$$

纯静电能为 [式 (4.55)]

$$
\begin{array}{r l} & W _ {1} = \frac {\varepsilon_ {0}}{2} \left[ \left(\frac {\rho_ {\mathrm{f}}}{3 \varepsilon_ {0} \varepsilon_ {\mathrm{r}}}\right) ^ {2} \int_ {0} ^ {R} r ^ {2} 4 \pi r ^ {2} \mathrm{d} r + \left(\frac {\rho_ {\mathrm{f}}}{3 \varepsilon_ {0}}\right) ^ {2} R ^ {6} \int_ {R} ^ {\infty} \frac {1}{r ^ {4}} 4 \pi r ^ {2} \mathrm{d} r \right] \\ & \quad = \frac {2 \pi}{9 \varepsilon_ {0}} \rho_ {\mathrm{f}} ^ {2} R ^ {5} \left(\frac {1}{5 \varepsilon_ {\mathrm{r}} ^ {2}} + 1\right) \end{array}
$$

但总能 [式 (4.58)] 为

$$
\begin{array}{r l} & W _ {2} = \frac {1}{2} \left[ \left(\frac {\rho_ {\mathrm{f}}}{3}\right) \left(\frac {\rho_ {\mathrm{f}}}{3 \varepsilon_ {0} \varepsilon_ {\mathrm{r}}}\right) \int_ {0} ^ {R} r ^ {2} 4 \pi r ^ {2} \mathrm{d} r + \left(\frac {\rho_ {\mathrm{f}} R ^ {3}}{3}\right) \left(\frac {\rho_ {\mathrm{f}} R ^ {3}}{3 \varepsilon_ {0}}\right) \int_ {R} ^ {\infty} \frac {1}{r ^ {4}} 4 \pi r ^ {2} \mathrm{d} r \right] \\ & \qquad = \frac {2 \pi}{9 \varepsilon_ {0}} \rho_ {\mathrm{f}} ^ {2} R ^ {5} \left(\frac {1}{5 \varepsilon_ {\mathrm{r}}} + 1\right) \end{array}
$$

请注意， $W_{1}<W_{2}$ ——这是因为 $W_{1}$ 不包括拉伸分子所涉及的能量。

让我们验证一下 $W_{2}$ 就是在构建系统时对自由电荷做的功。我们从（不带电、没有极化的）电介质球体开始，引入无穷小的自由电荷（dq）来逐层填充球体。当填充半径为 r 时，空间的电场为

$$
\boldsymbol {E} (\boldsymbol {r}) = \left\{ \begin{array}{l l} \frac {\rho_ {\mathrm{f}}}{3 \varepsilon_ {0} \varepsilon_ {\mathrm{r}}} \boldsymbol {r} & (r <   r ^ {\prime}) \\ \frac {\rho_ {\mathrm{f}}}{3 \varepsilon_ {0} \varepsilon_ {\mathrm{r}}} \frac {r ^ {\prime 3}}{r ^ {2}} \hat {\boldsymbol {r}} & (r ^ {\prime} <   r <   R) \\ \frac {\rho_ {\mathrm{f}}}{3 \varepsilon_ {0}} \frac {r ^ {\prime 3}}{r ^ {2}} \hat {\boldsymbol {r}} & (r > R) \end{array} \right.
$$

将下一个 $\mathrm{d}q$ 从无穷远移至 $r'$ 处所需做的功是

$$
\mathrm{d} W = - \mathrm{d} q \left[ \int_ {\infty} ^ {R} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} + \int_ {R} ^ {r ^ {\prime}} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} \right]
$$

$$
- \mathrm{dq} \left[ \frac {\rho_ {\mathrm{f}} r ^ {\prime 3}}{3 \varepsilon_ {0}} \int_ {\infty} ^ {R} \frac {1}{r ^ {2}} \mathrm{dr} + \frac {\rho_ {\mathrm{f}} r ^ {\prime 3}}{3 \varepsilon_ {0} \varepsilon_ {\mathrm{r}}} \int_ {R} ^ {r ^ {\prime}} \frac {1}{r ^ {2}} \mathrm{dr} \right]
$$

$$
= \frac {\rho_ {\mathrm{f}} r ^ {\prime 3}}{3 \varepsilon_ {0}} \left[ \frac {1}{R} + \frac {1}{\varepsilon_ {\mathrm{r}}} \left(\frac {1}{r ^ {\prime}} - \frac {1}{R}\right) \right] \mathrm{d} q
$$

这增加了半径 $(r')$ ：

$$
\mathrm{d} q = \rho_ {\mathrm{f}} 4 \pi r ^ {\prime 2} \mathrm{d} r ^ {\prime}
$$

因此，从 $r' = 0$ 到 $r' = R$ 所做的总功为

$$
\begin{array}{r} W = \frac {4 \pi \rho_ {\mathrm{f}} ^ {2}}{3 \varepsilon_ {0}} \left[ \frac {1}{R} \left(1 - \frac {1}{\varepsilon_ {\mathrm{r}}}\right) \int_ {0} ^ {R} r ^ {\prime 5} \mathrm{d} r ^ {\prime} + \frac {1}{\varepsilon_ {\mathrm{r}}} \int_ {0} ^ {R} r ^ {\prime 4} \mathrm{d} r ^ {\prime} \right] \\ = \frac {2 \pi}{9 \varepsilon_ {0}} \rho_ {\mathrm{f}} ^ {2} R ^ {5} \left(\frac {1}{5 \varepsilon_ {\mathrm{r}}} + 1\right) = W _ {2} \end{array}
$$

显然，“储存在弹簧中”的能量是

$$
W _ {\mathrm{弹簧}} = W _ {2} - W _ {1} = \frac {2 \pi}{4 5 \varepsilon_ {0} \varepsilon_ {\mathrm{r}} ^ {2}} \rho_ {\mathrm{f}} ^ {2} R ^ {5} (\varepsilon_ {\mathrm{r}} - 1)
$$

我将在一个等效的模型中来证实这一点。将电介质想象成微小的原始偶极子的集合，每个原始偶极子由 $+q$ 和 $-q$ 两个电荷连接到劲度系数为 $k$ 和平衡时长度为零的弹簧上组成，因此在没有任何场的情况下，两正负端重合。每个偶极子的一端被固定在适当的位置（就像固体中的原子核），但另一端可以自由移动以响应任何外加的电场。设 $\mathrm{d}\tau$ 为每个原始偶极子的体积（偶极子本身可能只占据这个空间的很少一部分）。

加上电场后，自由端的电场力和弹性力平衡 $^{19}$ ，电荷分开距离为 d，即 qE = kd。在本例子中，

$$
\boldsymbol {E} (r) = \frac {\rho_ {\mathrm{f}}}{3 \varepsilon_ {0} \varepsilon_ {r}} \boldsymbol {r}
$$

由此得到的偶极矩为 p = qd，极化矢量为 $P = p / d\tau$ ，因此

$$
k = \frac {\rho_ {\mathrm{f}}}{3 \varepsilon_ {0} \varepsilon_ {\mathrm{r}} d ^ {2}} P r \mathrm{d} \tau
$$

这个特殊的弹簧的能量是

$$
\mathrm{d} W _ {\text { 弹簧 }} = \frac {1}{2} k d ^ {2} = \frac {\rho_ {\mathrm{f}}}{6 \varepsilon_ {0} \varepsilon_ {\mathrm{r}}} P r \mathrm{d} \tau
$$

因此，总能为

$$
W _ {\mathrm{弹簧}} = \frac {\rho_ {\mathrm{f}}}{6 \varepsilon_ {0} \varepsilon_ {\mathrm{r}}} \int P r \mathrm{d} \tau
$$

这样一来，

$$
\boldsymbol {P} = \varepsilon_ {0} \chi_ {\mathrm{e}} \boldsymbol {E} = \varepsilon_ {0} \chi_ {\mathrm{e}} \frac {\rho_ {\mathrm{f}}}{3 \varepsilon_ {0} \varepsilon_ {\mathrm{r}}} \boldsymbol {r} = \frac {(\varepsilon_ {\mathrm{r}} - 1) \rho_ {\mathrm{f}}}{3 \varepsilon_ {\mathrm{r}}} \boldsymbol {r}
$$

所以

$$
W _ {\mathrm{弹簧}} = \frac {\rho_ {\mathrm{f}}}{6 \varepsilon_ {0} \varepsilon_ {\mathrm{r}}} \frac {(\varepsilon_ {\mathrm{r}} - 1) \rho_ {\mathrm{f}}}{3 \varepsilon_ {\mathrm{r}}} 4 \pi \int r ^ {4} \mathrm{d} r = \frac {2 \pi}{4 5 \varepsilon_ {0} \varepsilon_ {\mathrm{r}} ^ {2}} \rho_ {\mathrm{f}} ^ {2} R ^ {5} (\varepsilon_ {\mathrm{r}} - 1)
$$

而且结果符合得很好。

有时有人声称，即使是对于非线性电介质，式(4.58)也表示其能量，但这是错误的：在式(4.57)之后的推导必须做出线性电介质的假设。事实上，对于耗散系统来说，“存储能量”的整个概念失去了意义，因为所做的功不仅与最终的形状有关，还和它是如何到达那里的有关。例如，如果允许分子弹簧有一定的摩擦，通过在电荷聚集的过程中让弹簧伸长和收缩多次才达到最终状态，这样 $W_{弹簧}$ 就可以是任意大。特别是，若将式(4.58)应用于极化冻结的永电体时，你将会得到完全没有意义的结果（见习题4.27）。

习题4.26 半径为 $a$ 的导体球带电荷为 $Q$ （图4.29）。它被极化率为 $\chi_{\mathrm{e}}$ 的线性电介质材料包围，直至半径 $b$ 。求该形状的能量[式(4.58)]。

![](images/18dc950226bdfc2fabc696f0bceef00629ef9ed12ae014c903d839a03300cc76.jpg)  
图4.29

习题 4.27 利用式 (4.55) 和式 (4.58)，计算半径为 R、具有冻结均匀极化 P 的球体的 W（例题 4.2）。讨论两者的不同。哪个（如果有的话）是系统的“真实”能量？

## 4.4.4 电介质上的力

正如导体在电场中被吸引一样 [式 (2.51)]，电介质也是如此——原因基本相同：束缚电荷倾向于在与其相反符号的自由电荷附近聚集。但计算电介质所受的力非常困难。例如，考虑一块线性电介质平板的情况，其部分插入平行板电容器的两板之间，如图 4.30 所示。我们总是假设平行板电容板内部的电场是均匀的，外部为零。如果这个假设是正确的，那么电介质上将完全不受合力作用，因为电场在所有地方都垂直于极板。然而，实际上在极板边缘周围存在一个“边缘场”（fringing field），在多数情况下，这个边缘场可以忽略；但在这种情况下，对整个效应起决定性作用的正是这个边缘场（事实上，电场不可能在电容边缘处突然为零，因为如果确实如此，图 4.31 中所示的闭合环路中对 E 线积分将不为零）。正是因为这种不均匀的边缘电场将电介质拉向电容器内部。

![](images/a38041a8e66c2cb064b33b00cf637f4f0d3a7df21d2832810cf8faf1cf034a7f.jpg)  
图4.30

![](images/203a9b9bce4fbb8fae4e5903f7d6662cd7aa80c71d572109e675867aa7afe99c.jpg)  
图4.31

众所周知，边缘电场很难计算；幸运的是，我们可以通过以下巧妙的方法完全避免这种计算 $^{20}$ 。设 W 为系统的能量——当然，它与电介质板和电容器极板的重叠程度有关。如果我将电介质拉出一无穷小的距离 dx，能量的变化等于所做的功：

$$
\mathrm{d} W = F _ {\mathrm{me}} \mathrm{d} x\tag{4.59}
$$

其中 $F_{me}$ 是我必须施加的力，以抵消作用在电介质板所受的电场力： $F_{me} = -F$ 。因此，电介质板所受的电场力为

$$
F = - \frac {\mathrm{d} W}{\mathrm{d} x}\tag{4.60}
$$

现在，电容器中储存的总能量是

$$
W = \frac {1}{2} C V ^ {2}\tag{4.61}
$$

本问题中的电容是

$$
C = \frac {\varepsilon_ {0} w}{d} \left(\varepsilon_ {\mathrm{r}} l - \chi_ {\mathrm{e}} x\right)\tag{4.62}
$$

其中 l 是电容器极板的长度（图 4.30）。在电介质板移动过程中，假设电容极板上的总电量保持不变 $(Q = CV)$ 。按照 Q 来计算有

$$
W = \frac {1}{2} \frac {Q ^ {2}}{C}\tag{4.63}
$$

$$
F = - \frac {\mathrm{d} W}{\mathrm{d} x} = \frac {1}{2} \frac {Q ^ {2}}{C ^ {2}} \frac {\mathrm{d} C}{\mathrm{d} x} = \frac {1}{2} V ^ {2} \frac {\mathrm{d} C}{\mathrm{d} x}\tag{4.64}
$$

然而

$$
\frac {\mathrm{d} C}{\mathrm{d} x} = - \frac {\varepsilon_ {0} \chi_ {\mathrm{e}} w}{d}
$$

因此

$$
F = - \frac {\varepsilon_ {0} \chi_ {\mathrm{e}} w}{2 d} V ^ {2}\tag{4.65}
$$

(负号表示力沿 x 轴的负方向，电介质被拉入电容器里。)

在计算力时，使用式(4.61)（ $V$ 为常数）而不是式(4.63)（ $Q$ 为常数）是一个常见的错误。这样得到

$$
F = - \frac {1}{2} V ^ {2} \frac {\mathrm{d} C}{\mathrm{d} x}
$$

这里错了一个负号。当然，通过将电容器接到电池上，可以使它保持一个恒定的电势。但在这种情况下，电池也会随着电介质板的移动而做功。我们现在得到的不再是式(4.59)，而是

$$
\mathrm{d} W = F _ {\mathrm{me}} + V \mathrm{d} Q\tag{4.66}
$$

其中 VdQ 是电池做的功。由此可见

$$
F = - \frac {\mathrm{d} W}{\mathrm{d} x} + V \frac {\mathrm{d} Q}{\mathrm{d} x} = - \frac {1}{2} V ^ {2} \frac {\mathrm{d} C}{\mathrm{d} x} + V ^ {2} \frac {\mathrm{d} C}{\mathrm{d} x} = \frac {1}{2} V ^ {2} \frac {\mathrm{d} C}{\mathrm{d} x}\tag{4.67}
$$

与之前 [式 (4.64)] 相同，符号正确。

请理解：电介质上的力与是否保持 Q 或 V 为常数无关——它完全是由自由电荷和束缚电荷的分布决定的。如果假设 Q 恒定，计算力会变得更简单些，因为这样你不必考虑电池所做的功；但如果你坚持保持 V 为常数，无论哪种方式都可以正确地计算出来。

请注意，我们可以在完全不了解边缘电场的情况下，计算出由它最终决定的力来！当然，它内置于静电学的整个结构 $\nabla \times E = 0$ 中，因此边缘场必须存在。我们在这里并不是真的一无所获，只是巧妙地利用了理论的内在自洽性。随着介质板的移动，边缘场本身存储的能量（本推导中未考虑）保持不变；真正发生变化的是电容内部的能量，那里的电场是均匀的。

习题4.28 两个长同轴圆柱形金属管（内径为 $a$ ，外径为 $b$ ）垂直放置在一个油性介质罐（极化率为 $\chi_{\mathrm{e}}$ ，质量密度为 $\rho$ ）中。内管保持恒定电势 $V$ ，外管接地（图4.32）。求在两管之间油所能上升的高度 $(h)$ ?

![](images/6c20de59537986ede976ef07c11a7fdad5c807d9401be11f5fc2133ad4815492.jpg)  
图4.32

## 第4章补充习题

## 习题4.29

(a) 对于习题 4.5 中的构型，计算 $p_{1}$ 对 $p_{2}$ 的作用力和 $p_{2}$ 对 $p_{1}$ 的作用力。答案是否符合牛顿第三定律？

(b) 求 $p_2$ 上相对于 $p_1$ 的中心的总力矩。并将其与 $p_1$ 上关于同一点的总力矩进行比较。[提示：将（a）的答案与习题4.5的结果结合起来。]

习题 4.30 如图 4.33 所示，一个指向 y 轴方向的电偶极子 p 置于两个大导体板的中间。两个导体板各自与 x 轴形成一个小的夹角 $\theta$ ，且两板的电势保持为 $\pm V$ 。那么，p 上的合力方向是什么？（这里无须具体计算，但请定性解释你的答案。）

![](images/4d13045acb8bae55f78a8d64053596507bf7f1b71df8ceddbce78ebd36a1dd06.jpg)  
图4.33

习题4.31 点电荷 $Q$ 被“固定”在桌子上。距它半径为 $R$ 的周围有一无摩擦的圆形轨道，偶极子 $\pmb{p}$ 约束在轨道上运动，方向始终与圆相切。使用式(4.5)证明偶极子所受的电场力为

$$
\pmb {F} = \frac {Q}{4 \pi \varepsilon_ {0}} \frac {\pmb {p}}{R ^ {3}}
$$

请注意，该力始终保持“向前”的方向（你可以通过绘制一张显示有偶极子两端受力的草图来确认这一点）。为什么这不是永动机 $^{21}$ ?

!习题 4.32 恩绍定理（Earnshaw's theorem，习题 3.2）指出你无法在静电场中捕获住带电粒子。问题：你能在静电场中捕获中性（但可极化）原子吗 $^{22}$ ?

(a) 证明原子受力为 $F = \frac{1}{2}\alpha \nabla (E^2)$ 。

(b) 因此，问题就变成： $E^{2}$ 是否可能（在自由电荷区域）存在一个局域极大值？在这种情况下，原子所受的力将会把原子推至其平衡位置。证明：答案是不存在的。[提示：利用习题3.4(a)] $^{23}$

习题4.33 边长为 $a$ 的立方体电介质中心位于原点，具有“冻结”极化强度 $P = kr$ ，其中 $k$ 为常数。求出所有的束缚电荷，并验证它们的总和是否为零。

习题4.34 平行板电容器极板之间填充有介电材料，其介电常数从下底板（ $x = 0$ ）的1线性变化到上极板（ $x = d$ ）的2。电容器接在电压为 $V$ 的电池上。求所有束缚电荷，并验证其总和是否为零。

习题 4.35 点电荷 q 嵌入线性介电球体中心（极化率为 $\chi_{e}$ ，半径为 R）。求电场强度、极化和束缚电荷密度 $\rho_{b}, \sigma_{b}$ 。球表面上的总束缚电荷为多少？补偿负束缚电荷位于何处？

习题4.36 在一个线性电介质和另一个线性介质之间的界面处，电场线会发生弯折（图4.34）。假设在边界处没有自由电荷，证明

$$
\tan \theta_ {2} / \tan \theta_ {1} = \varepsilon_ {2} / \varepsilon_ {1}\tag{4.68}
$$

[评注：式 (4.68) 让人想起光学中的斯涅尔（Snell）定律。电介质材料的凸“透镜”会使电场“聚焦”或“散焦”吗？]

!习题 4.37 点电偶极子 p 嵌入线性介电材料球体的中心（半径为 R，极化率为 $\chi_{e}$ ）。求球体内外的电势。

$$
\left[ \mathrm{答案}: \quad {\frac {p \cos \theta}{4 \pi \varepsilon_ {0} r ^ {2}}} \left(1 + 2 {\frac {r ^ {3}}{R ^ {3}}} {\frac {(\varepsilon_ {\mathrm{r}} - 1)}{(\varepsilon_ {\mathrm{r}} + 2)}}\right), \quad r \leqslant R; \quad {\frac {p \cos \theta}{4 \pi \varepsilon_ {0} r ^ {2}}} \left({\frac {3}{\varepsilon_ {\mathrm{r}} + 2}}\right), \quad r \geqslant R \right]
$$

![](images/5fd29f56a05a9a1f3fd305d83fde0f19b2592b3291f0bdbba13539591c22fc1c.jpg)  
图4.34

习题 4.38 证明下面唯一性定理：体积 V 内部包含给定的自由电荷分布和各种线性介电材料，每种材料的极化率都是给定的。若 V 边界 S 上的电势给定（在无穷远处满足 V = 0），则整个 V 中的电势是唯一确定的。[提示：在整个体积 V 上对 $\nabla \cdot (V_{3}D_{3})$ 进行积分。]

习题4.39 电势为 $V_{0}$ 的导体球的 $V$ 一半嵌入极化率为 $\chi_{\mathrm{e}}$ 的电介质中，电介质充满 $z < 0$ 区域（图4.35）。断言：每处的电势都与没有电介质存在时的电势相同。按照下面的步骤验证该断言：

(a) 根据 $V_{0}, r$ 和 $R$ 写出拟求的电势 $V(r)$ 的公式。并用它来确定球体上的电场强度、极化强度、束缚电荷以及球体表面的自由电荷分布。

(b) 证明由此产生的电荷分布确实会产生电势 $V(r)$ 。

(c) 利用习题 4.38 中的唯一性定理来完成论证。

(d) 你能用相同的电势对图4.36中所示的形状进行求解吗？如果不能，请解释原因。

![](images/8160f2b384c16c7abdbd5fdb76e08e0a1ac02357e77aa84b16fbeab48165ee70.jpg)  
图4.35

![](images/a7ce4407e9a7c99c604b57a8f97d8b5e25007aa7e8ede4c3b6d4c87a52b5c436.jpg)  
a)  
图4.36

![](images/47364a24d0e219f66b1f0931e86a706ab439fa719f92c5e1372b93a94421648b.jpg)  
b)

习题 4.40 根据式 (4.5)，作用在单个电偶极子上的力为 $(\boldsymbol{p} \cdot \nabla) \boldsymbol{E}$ ，因此电介质物体上的合力为

$$
\pmb {F} = \int (\pmb {p} \cdot \nabla) \pmb {E} _ {\mathrm{ext}} \mathrm{d} \tau\tag{4.69}
$$

[这里 $E_{ext}$ 是除电介质以外的所有物体产生的电场。或许你可能会认为使用总电场也无关紧要，毕竟电介质不能对本身施加力的作用。然而，由于电介质的电场在任何有表面束缚电荷存在的地方都是不连续的，其导数将引入了伪 $\delta$ 函数，因此最安全的方法是使用 $E_{ext}$ 。] 利用式 (4.69) 求作用半径为 R 的小球上的力，该小球由极化率为 $\chi_{e}$ 的线性介电材料组成。小球距带均匀线电荷密度为 $\lambda$ 的细线的距离为 s。

!习题 4.41 在线性电介质中，极化与电场成正比： $P=\varepsilon_{0}\chi_{e}E$ 。如果材料由原子（或者非极性分子）组成，则每个原子的诱导偶极矩和电场成正比， $p=\alpha E$ 。问题：原子极化率 $\alpha$ 和 $\chi_{e}$ 的关系是什么？

由于 $P$ （单位体积内的偶极矩）是 $\pmb{p}$ （每个原子的偶极矩）乘以 $N$ 倍（单位体积内的原子数目）， $P = N\pmb{p} = N\alpha E$ ，你可能会认为

$$
\chi_ {\mathrm{e}} = \frac {N \alpha}{\varepsilon_ {0}}\tag{4.70}
$$

事实上，如果密度很低，该公式和实际结果相差不是很大；但仔细研究会发现一个微妙的问题，因为式(4.30)中的 E 是介质中总的宏观电场，而式(4.1)中的场是除了原子本身以外所有因素引起的场（孤立原子的极化率是在给定外场下定义的），称这个场为 $E_{其他}$ 。设想每个原子所占据的空间为半径为 R 的球，证明

$$
\pmb {E} = \left(1 - \frac {N \alpha}{3 \varepsilon_ {0}}\right) \pmb {E} _ {\text {其他}}\tag{4.71}
$$

由此得出结论

$$
\chi_ {\mathrm{e}} = \frac {N \alpha / \varepsilon_ {0}}{1 - N \alpha / 3 \varepsilon_ {0}}
$$

或者

$$
\alpha = \frac {3 \varepsilon_ {0}}{N} \left(\frac {\varepsilon_ {\mathrm{r}} - 1}{\varepsilon_ {\mathrm{r}} + 2}\right)\tag{4.72}
$$

式（4.72）被称为克劳修斯-莫索提（Clausius-Mossotti）公式，或者在应用光学中被称为洛伦兹-洛伦茨（Lorentz-Lorenz）方程。

习题 4.42 验证表 4.1 中所列气体的克劳修斯-莫索提关系 [式 (4.72)]，介电常数如表 4.2 所示。[这里密度非常小，以至于式 (4.70) 和式 (4.72) 无法区分。关于确定克劳修斯-莫索提校正项的实验数据请参见珀塞尔著的《电磁学》第 1 版，习题 9.28。] $^{24}$

!习题 4.43 克劳修斯-莫索提方程（习题 4.41）告诉你如何根据原子极化率 $\alpha$ 计算非极性物质的极化率 $\chi_{e}$ 。郎之万方程（Langevin equation）告诉你如何根据永久分子偶极矩 p 计算极性物质的极化率。具体是这样的：

(a) 外场 E 中偶极子的能量 $u = -p \cdot E = -pE \cos \theta$ [式 (4.6)]; 若将 z 轴定义为沿电场 E 的方向， $\theta$ 就是通常的极角。根据指向，范围从 -pE 到 +pE。统计力学告诉我们当材料处于温度为 T 的平衡状态时，分子具有给定能量 u 的概率与玻尔兹曼因子

$$
\exp (- u / k T)
$$

成正比，因此，偶极子的平均能量为

$$
\langle u \rangle = \frac {\int u \mathrm{e} ^ {- (u / k T)} \mathrm{d} \Omega}{\int \mathrm{e} ^ {- (u / k T)} \mathrm{d} \Omega}
$$

其中， $d\Omega = \sin\theta d\theta d\varphi$ ，积分遍及所有方向（ $\theta: 0 \to \pi; \varphi: 0 \to 2\pi$ ）。由此证明每单位体积内包含有 N 个极化分子的极化强度为

$$
P = N p [ \coth (p E / k T) - (k T / p E) ]\tag{4.73}
$$

这就是郎之万方程。画出 $pE / kT$ 与 $P / Np$ 的函数关系图。

(b) 请注意，在强场/低温情况下，几乎所有的分子都是线状排列，材料是非线性的。然而，一般情况下 $T - kT$ 远大于 $pE$ 。证明：在这种情况下，材料是线性的，并根据 $N, p, T$ ，和 $k$ （玻尔兹曼常数）计算其极化率。计算 $20^{\circ}\mathrm{C}$ 下水的极化率，并和表4.2中的实验值进行比较（水的偶极矩为 $6.1 \times 10^{-30}\mathrm{C} \cdot \mathrm{m}$ )。这样的结果相差是非常大的，因为我们再次忽略了 $\pmb{E}$ 和 $\pmb{E}_{\text{其他}}$ 之间的区别。在低密度气体它们符合得非常好，因为 $\pmb{E}$ 和 $\pmb{E}_{\text{其他}}$ 的区别可以忽略。在 $100^{\circ}\mathrm{C}$ 和 $1\mathrm{atm}$ 压强下测试一下水蒸气的结果。

## 5.1 洛伦兹力定律

## 5.1.1 磁场

请记住经典电动力学的基本问题：我们有一组电荷 $q_{1}, q_{2}, q_{3}, \cdots$ （“源”电荷），我们想计算这些电荷对其他电荷 Q（“检验”电荷）的作用力（图 5.1）。根据叠加原理，只需求出单个源电荷的作用力就足够了，那么总和就是所有单个力的矢量和。到现在为止，我们只关注最简单的情况——静电学，即源电荷处于静止状态（尽管检验电荷不必如此）。现在是该考虑运动中的电荷之间的作用力的时候了。

![](images/d1839f2df9754ee7b750ab2237845f47736f6d3cb157e6c3b7b0dcc721811cd4.jpg)  
图5.1

为了让你对将要讲的内容有所了解，想象一下我演示如下实验：天花板上下垂两根导线，相距几厘米；我打开电源，使电流向上流过一根导线，再向下流经另一根导线，这时两导线跳动远离——它们显然会相互排斥（图5.2a）。我们如何解释这一点？你也许会认为电池（或者其他驱动电流的设备）确实在给导线充电，而这种力的起因就是类似电荷之间的排斥作用。但这是不正确的。我可以在这些导线附近放置一个检验电荷，它不会受到任何力的作用 $^{1}$ ，因为这些导线实际上是电中性的。（的确，电子沿导线运动——这就是电流——但在导线上任何给定的一段长度中，静止的正电荷与运动的负电荷都一样多。）此外，我还可以改变演示的线路接法，使两根导线中的电流都向上流动（图5.2b），这时就会发现它们相互吸引！
![](images/0d0cffd537db48b5a78fa5649197fbf0ef924c1ad110db6a6ec810d93c690a48.jpg)  
a) 相反电流相互排斥

![](images/4593bae3f1a3bab793468996546742270fc7a9443edbe0a3c3944a5a74ed5ac1.jpg)  
b) 同向电流相互吸引  
图5.2

本质上，无论是平行电流的相互吸引还是反平行电流的相互排斥都不是静电力作用。这是我们第一次遇到磁力。静止电荷在其周围的空间只产生电场 E，而运动电荷还会产生磁场 B。确切地讲，实际中磁场更容易被探测到——你只需要一个孩子玩的指南针。眼下这些指南针的工作原理无关话题；只需要知道指南针针尖指向的是所处局域磁场的方向就足够了。通常，它指向地球北方，以相应地球的磁场。但在实验室里，一般的磁场可能会比这强数百倍，指南针会指向任何的实验室磁场的方向。

现在，如果你把一个小指南针放在载流导线附近，你很快会发现一件很奇特的现象：磁场方向既不指向导线，也不远离电线，而是环绕着导线。事实上，如果你用右手握住导线，拇指指向电流的方向，其余四指环绕的方向就是磁场的方向（图5.3）；这样的磁场是如何对附近的平行电流产生吸引力的呢？在第二根导线上，磁场指向方向指向纸面内（图5.4）电流的方向向上，产生的力的方向向左！要解释这些方向，需要一条奇怪的定律。

![](images/adb7d13510f85daf765cbd7f5b3f2a00bc9df8de14d2ed707d7a1b3080c3e70e.jpg)  
图5.3

![](images/b812d655b72ff32aee60dbb74b24b17bdbe15588ab2739bc29c72069cd10d4cb.jpg)  
图5.4

## 5.1.2 磁力

事实上，这种方向的组合正好适用于叉积。在磁场 B 中以速度 v 运动的电荷 Q 所受力为 $^{2}$

$$
\boxed {F _ {\text {磁力}} = Q (\pmb {v} \times \pmb {B})}\tag{5.1}
$$

这被称作洛伦兹力定律（Lorentz force law） $^{3}$ 。在电场和磁场都存在的情况下，Q所受的总力为

$$
\boldsymbol {F} = Q [ \boldsymbol {E} + (\boldsymbol {v} \times \boldsymbol {B}) ]\tag{5.2}
$$

当然，我并不敢自诩我推导出了式(5.1)；它是该理论的一个基本公理，其正确性可以在第5.1.1节中描述的实验中找到。

从现在开始，我们的主要工作就是计算磁场 B（以及电场 E，当源电荷运动时，运动规律会更加复杂）。但在开始之前，很值得仔细研究一下洛伦兹力定律；这是一个奇特的定律，并会导致一些异乎寻常的粒子轨迹。

例题5.1 回旋运动（Cyclotron motion）。圆周运动是带电粒子在磁场中的典型运动，磁场力提供向心加速度。在图5.5中，均匀磁场方向指向纸面向里；如果电荷量为 $Q$ 的粒子以速度 $v$ 绕半径为 $R$ 的圆轨道做逆时针运动；磁场力方向指向圆心，其大小恒定为 $QvB$ ——正好维持粒子做匀速圆周运动：

$$
Q v B = m \frac {v ^ {2}}{R} \quad \text {或} \quad p = Q B R\tag{5.3}
$$

![](images/29dcc59676e26e5fda3f3c83761c5d71f65b23efc34babff8e60216839aef1d2.jpg)  
图5.5

其中 $m$ 是粒子的质量， $p = mv$ 是它的动量。式 (5.3) 称为回旋加速器公式（cyclotron formula），因为它描述了回旋加速器中粒子的运动。回旋加速器是第一个近代粒子加速器。它还提供了一种测量粒子动量的简单实验方法：将粒子穿过已知磁场区域，并测量其轨道半径。这实际上是确定基本粒子动量的标准方法。

我假设带电粒子在垂直于磁场 B 的平面内运动，如果初始速度有平行于磁场 B 的分量 $v_{\parallel}$ ，则在该方向的运动不受磁场的影响，粒子的运动轨迹将是一个螺旋线（图 5.6）。半径仍然由式 (5.3) 给出，但其所讨论的速度应是垂直于磁场 B 的分量 $v_{\perp}$ 。

![](images/bac1f1ac23827a86762064f08319344015d9fca6a8a1d8b2ca8866af510457d3.jpg)  
图5.6

例题5.2 圆滚线运动（Cycloid Motion）。若我们引入与磁场方向垂直的匀强电场，则粒子的运动轨迹更奇特。例如，假设 $\pmb{B}$ 指向 $x$ 轴方向， $\pmb{E}$ 指向 $z$ 轴方向，如图5.7所示。从原点开始释放正电荷，它的运动轨迹是什么？

![](images/7c6aa4b32d7ab969482f2102e412739f74cfaa07a56626397058225af2692fb0.jpg)  
图5.7

[解答] 首先，让我们定性地考虑一下本问题。粒子开始时处于静止，因此所受磁场力为零，在 $z$ 轴方向上粒子在电场作用下加速运动。根据式(5.1)，粒子一旦具有速度，就会受到磁场力作用，并使电荷弯曲向右运动。速度越快，磁场力 $F_{\mathrm{mag}}$ 越大；最终，粒子的运动轨迹向 $y$ 轴方向弯曲。此时，电荷运动方向变为与电场力方向相反，粒子开始减速且磁场力也将减小，电场力再次变得起主导作用，使粒子在如图5.7所示的 $a$ 点静止。此后整个运动重复开始，粒子运动到 $b$ 点，如此反复。

现在让我们定量计算本题。在 $x$ 方向上没有受力的情况下，粒子在任意时刻 $t$ 位置可由矢量 $(0, y(t), z(t))$ 描述；因此，速度为

$$
\boldsymbol {v} = (0, \dot {y}, \dot {z})
$$

其中点表示对时间的导数。所以

$$
\boldsymbol {v} \times \boldsymbol {B} = \left| \begin{array}{c c c} \hat {\boldsymbol {x}} & \hat {\boldsymbol {y}} & \hat {\boldsymbol {z}} \\ 0 & \dot {y} & \dot {z} \\ B & 0 & 0 \end{array} \right| = B \dot {z} \hat {\boldsymbol {y}} - B \dot {y} \hat {\boldsymbol {z}}
$$

应用牛顿第二定律

$$
\pmb {F} = Q (\pmb {E} + \pmb {v} \times \pmb {B}) = Q (E \hat {z} + B \dot {z} \hat {y} - B \dot {y} \hat {z}) = m \pmb {a} = m (\ddot {y} \hat {y} + \ddot {z} \hat {z})
$$

或者，将 $\hat{y}$ 和 $\hat{z}$ 的分量分别处理，

$$
Q B \dot {z} = m \ddot {y}, \quad Q E - Q B \dot {y} = m \ddot {z}
$$

方便起见，令

$$
\omega = \frac {Q B}{m}\tag{5.4}
$$

[这称为回旋频率（cyclotron frequency），在没有电场的情况下，粒子将在该点旋转。]则运动方程的形式如下：

$$
\ddot {y} = \omega \dot {z}, \quad \ddot {z} = \omega \left(\frac {E}{B} - \dot {y}\right)\tag{5.5}
$$

其通解为 $^{4}$

$$
\left. \begin{array}{l} y (t) = C _ {1} \cos \omega t + C _ {2} \sin \omega t + (E / B) t + C _ {3} \\ z (t) = C _ {2} \cos \omega t - C _ {1} \sin \omega t + C _ {4} \end{array} \right\}\tag{5.6}
$$

由于粒子在原点 $(y(0) = z(0) = 0)$ 从静止 $(\dot{y}(0) = \dot{z}(0) = 0)$ 开始运动；这四个初始条件决定常数 $C_1, C_2, C_3, C_4$ ：

$$
y (t) = \frac {E}{\omega B} (\omega t - \sin \omega t), z (t) = \frac {E}{\omega B} (1 - \cos \omega t)\tag{5.7}
$$

这种形式的答案意义不明显，若我们令

$$
R \equiv \frac {E}{\omega B}\tag{5.8}
$$

再由三角函数等式 $\sin^2\omega t + \cos^2\omega t = 1$ 消去正弦和余弦函数，我们得到

$$
(y - R \omega t) ^ {2} + (z - R) ^ {2} = R ^ {2}\tag{5.9}
$$

这是半径为 $R$ 的圆的方程，圆心在 $(0, R\omega t, R)$ 并以恒定速度沿 $y$ 轴方向运动：

$$
v = \omega R = \frac {E}{B}\tag{5.10}
$$

粒子的运动就像是沿 $y$ 轴滚动的轮子边缘上的一个点，以这种方式运动形成的曲线称为摆线（cycloid）。请注意：整体运动并非如你所想的那样沿着 $\pmb{E}$ 的方向，而是垂直于 $\pmb{E}$ 的方向。

洛伦兹力定律式 (5.1) 的一个含义值得特别关注：

## 磁力不做功

例如，如果 $Q$ 运动了一段位移 $\mathrm{d}l = v\mathrm{d}t$ ，它所做的功为

$$
\mathrm{d} W _ {\mathrm{mag}} = \boldsymbol {F} _ {\mathrm{mag}} \cdot \mathrm{d} \boldsymbol {l} = Q (\boldsymbol {v} \times \boldsymbol {B}) \cdot \boldsymbol {v} \mathrm{d} t = 0\tag{5.11}
$$

$(\boldsymbol{v} \times \boldsymbol{B})$ 的方向与 v 垂直，因此 $(\boldsymbol{v} \times \boldsymbol{B}) \cdot \boldsymbol{v} = 0$ 。磁场力可以改变粒子的运动方向，但不能使其加速或减速。磁力不做功的事实是洛伦兹力定律的最基本、最直接的结论，但在许多情况下，它看起来显然是错误的结论，以至于人们对此犹豫不决。例如，当磁性起重机吊起一辆报废汽车时，显然某种力在做功，如果否定磁力做功似乎是荒谬的。好吧，不管荒谬与否，我们必须否认这一点，在这种情况下，弄清楚谁在做功是一件非常微妙的事情。我们将在下一节中看到一个有趣的例子，但完整的描述将不得不等待到第8章。

习题 5.1 如图 5.8 所示，带电粒子 q 入射到匀强磁场 B 中（方向指向面内），磁场使粒子偏离原来的入射路径至上方距离为 d 处。粒子带正电荷还是负电荷？根据 a, d, B 和 q，求出粒子的动量。

![](images/5e94bbf2ae2c3e9ee8d6111558774cd6a324c1c58eec67a32bbcfc214e5b803d.jpg)  
图5.8

习题5.2 如果粒子以下面的速度从原点出发，则在例题5.2中求出粒子的轨迹并画出草图。

(a) $\boldsymbol{v}(0)=(E/B)\hat{\boldsymbol{y}}$ ,

(b) $\boldsymbol{v}(0)=(E/2B)\hat{\boldsymbol{y}}$ ,

(c) $\boldsymbol{v}(0)=(E/B)(\hat{\boldsymbol{y}}+\hat{\boldsymbol{z}})$ 。

习题 5.3 1897 年，汤姆孙（J. J. Thomson）通过测量“阴极射线”的比荷“发现”了电子，（实际上是带电为 q、质量为 m 的电子束），如下所示：

(a) 首先，他让粒子束穿过均匀交叉的电场 E 和磁场 B（它们相互垂直，且都垂直于电子束）。调整电场直到粒子束无偏转，那么粒子的速度为多少？（用 E 和 B 来表示）

（b）然后，他撤去电场，测量仅在磁场作用下粒子束运动的轨道半径 $R$ 。利用参数 $E, B$ 和 $R$ 表示粒子的比荷 $(q / m)$ 。

## 5.1.3 电流

导线中的电流是单位时间内通过给定点的电荷。根据定义，向左运动的负电荷与向右运动的正电荷数量相同。这通常反映了这样一个物理事实，即几乎所有涉及运动电荷的物理现象都依赖于电荷和速度的乘积——如果你同时改变 $q$ 和 $\pmb{v}$ 的符号，会得到相同样的结果，因此电流中的电荷是正是负并不重要。[洛伦兹力定律就是一个这样的例子，而霍尔效应（习题5.41）则是一个典型的例外。]在实际中，通常是带负电的电子在与电流相反的方向上运动。为了避免由此带来的小麻烦，我通常假设是正电荷在运动，事实上现在这种假设在本杰明·富兰克林建立不适合的约定后已经延续了一个世纪 $^{5}$ 。电流用库仑每秒或者安培（A）来量度：

$$
1 \mathrm{A} = 1 \mathrm{C} / \mathrm{s}\tag{5.12}
$$

线电荷 $\lambda$ 以速度 $v$ 在导线中运动形成电流为

$$
I = \lambda v\tag{5.13}
$$

因为一段长度为 $v\Delta t$ 、所带电荷 $\lambda v\Delta t$ 的线段在时间间隔 $\Delta t$ 内通过导线中点 $P$ 。电流实际上是一个矢量：

$$
I = \lambda v\tag{5.14}
$$

因为电流流动的路径是由金属丝的形状决定的，所以通常不会特意显示电流 I 矢量特性。但是，当涉及表面电流和体电流时 $^{6}$ ，我们就不能如此随意，为了术语的一致性，最好在开始就承认电流的矢量性。当然，零线包含的固定正电荷和移动负电荷一样多。前者对电流没有贡献——式(5.13)中的电荷密度 $\lambda$ 仅对运动电荷而言。在两种电荷都参与运动的特殊情况下， $I = \lambda_{+}v_{+} + \lambda_{-}v_{-}$ 。

![](images/35a81da64ccf3ef722eb80624ff5d1526eaa550ff99a9ccc1b0e070546516014.jpg)  
图5.9

载流导线上的磁力为

$$
F _ {\mathrm{mag}} = \int (\boldsymbol {v} \times \boldsymbol {B}) \mathrm{d} q = \int (\boldsymbol {v} \times \boldsymbol {B}) \lambda \mathrm{d} l = \int (\boldsymbol {I} \times \boldsymbol {B}) \mathrm{d} l\tag{5.15}
$$

由于 I 和 dl 都指向同一方向，我们也可以这样写：

$$
\boxed {F _ {\mathrm{mag}} = \int I (\mathrm{d} l \times B)}\tag{5.16}
$$

通常情况下，电流 I 沿导线是一常量（大小），I 可以提到积分号外面：

$$
\boldsymbol {F} _ {\mathrm{mag}} = I \int (\mathrm{d} \boldsymbol {l} \times \boldsymbol {B})\tag{5.17}
$$

例题5.3 如图5.10所示，一个矩形下端挂有质量为 $m$ 的物体线圈，上端处在匀强磁场 $\pmb{B}$ 中。磁场 $\pmb{B}$ 的方向指向图示阴影区域的面内。线圈中通入多大的电流 $I$ ，向上的磁力会与向下的引力完全达到平衡？

[解答] 首先，电流必须沿顺时针方向，以便磁场中水平部分受磁场力方向 $(I\times B)$ 向上。磁场力大小为

$$
F _ {\mathrm{mag}} = I B a
$$

其中 $a$ 为线圈的宽度。（作用在两竖直边的磁场力抵消。）为使磁力 $F_{\mathrm{mag}}$ 和重力 $mg$ 平衡，必须有

$$
I = \frac {m g}{B a}\tag{5.18}
$$

这样重物就悬挂在半空中了。

![](images/9f4f7e5781712d7d0fcdabb3b276590ae8be203f612b08d32ed1db08273d3d02.jpg)  
图5.10

如果我们现在增大电流会发生什么？此时，向上的磁场力会超过向下的重力，线框会带着重物向上运动。某个事物做功了，看起来磁场力做功似乎是很合理的。的确，我们可以写出

$$
W _ {\mathrm{mag}} = F _ {\mathrm{mag}} h = I B a h\tag{5.19}
$$

其中 $h$ 是线圈升高的距离。但我们知道磁场力是永远不会做功的。这是怎么回事呢？

当线圈开始上升时，导线中的电荷不再是水平运动，除了与电流有关的水平分量 $w(I=\lambda w)$ 外，现在它的速度还有一个向上的分量 u，即线框的速度（图 5.11）。始终垂直于速度的磁场力不再指向正上方，而是向后倾斜。磁场力垂直于电荷的合位移（沿 v 的方向），因此它不对电荷 q 做功。它的确有一个垂直分量 qwB；所有电荷 $\lambda a$ 作用在上边框上的垂直力是

$$
F _ {\text { v   e   r   t }} = \lambda a w B = I B a\tag{5.20}
$$

（如前）；但现在它还有一个水平分量 $quB$ ，它与电流的方向相反。因此要维持电流的流动必须克服使电荷向后的磁场力。

![](images/3b6ab9021abc47cc20323f3057155214abc3030520dd4b4af4d8e203081293e6.jpg)  
图5.11

线框上部水平方向的合力为

$$
F _ {\mathrm{horiz}} = \lambda a u B\tag{5.21}
$$

在 dt 时间内，电荷移动的（水平）距离为 wdt，因此外界（可能是电池或发电机）所做的功是

$$
W _ {\mathrm{电池}} = \lambda a B \int u w \mathrm{d} t = I B a h
$$

这正是我们天真地在方程（5.19）中归因于磁场力的原因。在这个过程中做功了吗？当然是的！那么是谁在做功呢？电池！那么磁场力的角色是什么呢？好吧，它使电池提供的水平力转向为线框和重物的竖直运动 $^{7}$ 。

考虑一个力学类比也许会有所帮助。想象一下，你正用拖把水平推一个行李箱，把它滑上一个无摩擦的斜坡（图5.12）。支持力 $(N)$ 不做功，因为它垂直于斜面。但它确实有一个竖直分量（事实上，这是提起行李箱的原因）和一个（向后的）水平分量（你必须通过拖把来克服）。是什么在这里做功？很明显，是你自己，但你的力（纯粹是水平推力）并不是举起行李箱的力（至少不是直接的）。这里支持力扮演着同例题5.3中磁场力同样的（关键）角色：尽管它本身不做功，它将主动作用（你或者电池）的作用效果从水平方向转到了垂直方向。

![](images/8356705faf6a6e1d7f276c8b48f410ebabda4c534549b4dc0b19d898d997b6f6.jpg)  
图5.12

当电荷流过表面时，我们用表面电流密度（surface current density）K 来描述它，定义如下：考虑一个宽度为 $dl_{\perp}$ 、与电流平行的无穷小“带”(图 5.13)，如果该带中的电流为 dI，则表面电流密度为

$$
\boldsymbol {K} = \frac {\mathrm{d} \boldsymbol {I}}{\mathrm{d} l _ {\perp}}\tag{5.22}
$$

换句话说，K 就是每单位宽度上流过的电流。特别是，如果表面电流密度为 $\sigma$ ，速度为 v，则

$$
\boldsymbol {K} = \sigma \boldsymbol {v}\tag{5.23}
$$

一般来说，K 在表面上逐点变化，以反映 $\sigma$ 和 v 的变化。表面电流所受的磁场力是

$$
\boldsymbol {F} _ {\mathrm{mag}} = \int (\boldsymbol {v} \times \boldsymbol {B}) \sigma \mathrm{d} a = \int (\boldsymbol {K} \times \boldsymbol {B}) \mathrm{d} a\tag{5.24}
$$

警告：正如 $E$ 在有表面电荷时是不连续的一样， $B$ 在有表面电流时也是不连续的。在式(5.24)中，你要十分小心地使用平均场，就像我们在第2.5.3节所做的那样。

![](images/0cab16ab280efe56cf642ee55d8b766aab394fd90e9e370a6ee039f5c5201884.jpg)  
图5.13

当电荷的流分布在三维空间时，我们用体电流密度 J 来描述它，定义如下：考虑一横截面为 $da_{\perp}$ 且电流方向平行的无限小细管（图 5.14）。若管中电流为 dI，则体电流密度为

$$
J = \frac {\mathrm{d} I}{\mathrm{d} a _ {\perp}}\tag{5.25}
$$

换句话说， $J$ 就是单位面积上流过的电流。如果体电荷密度为 $\rho$ ，速度为 $\pmb{v}$ ，则

$$
J = \rho v\tag{5.26}
$$

因此，作用在体电流上的磁场力为

$$
\pmb {F} _ {\mathrm{mag}} = \int (\pmb {v} \times \pmb {B}) \rho \mathrm{d} \tau = \int (\pmb {J} \times \pmb {B}) \mathrm{d} \tau\tag{5.27}
$$

![](images/b8d56e46912f3fb07b89df8a9ffe38c058ac3c31a3866289bb986d9768eb5e79.jpg)  
图5.14

例题5.4（a）电流 $I$ 均匀分布在半径为 $a$ 的圆形横截面导线上（图5.15）。求体电流密度 $J_{\circ}$ （b）假设导线中的电流密度与离圆轴的距离成正比：

$$
J = k s
$$

(k 为常数)，求导线中的总电流 I。

![](images/22260d7387bcd276f26dda898e6eb3e93e46b5d6066bdd21dcd3a81282bce9f1.jpg)  
图5.15

[解答]（a）（垂直于电流方向的）面积为 $\pi a^2$ ，因此

$$
J = \frac {I}{\pi a ^ {2}}
$$

因为电流密度是均匀的，所以求解很简单。

（b）因为 $J$ 随 $s$ 而变化，我们必须对式(5.25)进行积分。如图5.16所示，阴影部分的电流是 $J\mathrm{da}_{\perp}$ ，而 $\mathrm{da}_{\perp} = s\mathrm{d}s\mathrm{d}\varphi$ ，因此

$$
I = \int (k s) (s \mathrm{d} s \mathrm{d} \phi) = 2 \pi k \int_ {0} ^ {a} s ^ {2} \mathrm{d} s = \frac {2 \pi k a ^ {3}}{3}
$$

图5.16

根据式 (5.25)，通过表面 $S$ 的总电流可以写成

$$
I = \int_ {\mathcal {S}} J \mathrm{d} a _ {\perp} = \int_ {\mathcal {S}} \boldsymbol {J} \cdot \mathrm{d} \boldsymbol {a}\tag{5.28}
$$

（点积恰好得到 $\mathrm{da}$ 的适当分量），特别是，单位时间内流出体积 $\mathcal{V}$ 的总电荷为

$$
\oint_ {\mathcal {S}} \boldsymbol {J} \cdot \mathrm{d} \boldsymbol {a} = \int_ {\mathcal {V}} (\nabla \cdot \boldsymbol {J}) \mathrm{d} \tau
$$

因为电荷是守恒的，所以有多少电荷从表面流出，内部电荷就有相应的减少：

$$
\int_ {\mathcal {V}} (\nabla \cdot \boldsymbol {J}) \mathrm{d} \tau = - \frac {\mathrm{d}}{\mathrm{d} t} \int_ {\mathcal {V}} \rho \mathrm{d} \tau = - \int_ {\mathcal {V}} \left(\frac {\partial \rho}{\partial t}\right) \mathrm{d} \tau
$$

（负号表示电荷向外流出对应减少 V 内剩余的电荷。）由于它对任意体积都成立，所以

$$
\boxed {\nabla \cdot \boldsymbol {J} = - \frac {\partial \rho}{\partial t}}\tag{5.29}
$$

这就是局域电荷守恒的精确数学表达式，它被称为连续性方程（continuity equation）。

为了将来参考方便，让我们总结一下约定的“词汇”，方便用于把方程写作点、线、面和体电流的形式。

$$
\sum_ {i = 1} ^ {n} \left(\right) q _ {i} \pmb {v} _ {i} \sim \int_ {\mathrm{线}} \left(\right) \pmb {I} \mathrm{d} l \sim \int_ {\mathrm{面}} \left(\right) \pmb {K} \mathrm{d} a \sim \int_ {\mathrm{体}} \left(\right) \pmb {J} \mathrm{d} \tau\tag{5.30}
$$

这种对应关系类似于各种电荷分布 $q \sim \lambda dl \sim \sigma da \sim \rho d\tau$ ，这相应地从最初的洛伦兹力定律得到了式 (5.15)、式 (5.24) 和式 (5.27)。

## 习题5.4 假设在某区域磁场具有形式

$$
B = k z \hat {x}
$$

(k 为常数)。边长为 a 的圆环位于 yz 平面内、中心处在原点。当你沿 x 轴向下看时，圆环内沿逆时针流有电流 I。求作用在圆环上的力。

习题5.5 电流 $I$ 沿半径为 $a$ 的导线流动。

（a）如果电流均匀分布在导线表面上，则表面电流密度 $K$ 为多少？

(b) 如果电流密度分布与到中心轴的距离成反比，则 $J$ 是多少？

习题5.6

(a) 留声机唱片表面具有均匀的静止电荷密度 $\sigma$ 。若它以角速度 $\omega$ 旋转，则距离中心 $r$ 处的表面电流密度 $K$ 为多少？

（b）一半径为 R、总电荷为 Q 的均匀带电实心球，中心处在原点位置，并以恒定角速度 $\omega$ 绕 z 轴旋转。求球内任意一点 $(r, \theta, \varphi)$ 处的电流密度 J。

习题5.7 对限制在体积 $\nu$ 内的电荷和电流分布，证明

$$
\int_ {\mathcal {V}} J \mathrm{d} \tau = \mathrm{d} p / \mathrm{d} t\tag{5.31}
$$

其中 p 是总电偶极矩。[提示：计算 $\int_{\mathcal{V}} \nabla \cdot (x J) \, \mathrm{d}\tau$ 。]

## 5.2 毕奥-萨伐尔定律

## 5.2.1 稳恒电流

固定电荷可以产生不随时间变化的稳恒电场；因此命名为静电场（electrostatics） $^{8}$ 。稳恒电流产生不随时间变化的恒定磁场；稳恒电流理论称为静磁学（magnetostatics）。

$$
\begin{array}{r l} & \text {固定电荷} \Rightarrow \text {静电场：静电学} \\ & \text {稳恒电流} \Rightarrow \text {静磁场：静磁学} \end{array}
$$

我所说的稳流是指永远持续的流动，没有电流的改变，也没有电荷在任何地方的积累。（有些人称之为“静电流”，在我看来这是一个术语上的矛盾。）从形式上讲，静电磁学是任何地方任何时间保持

$$
\frac {\partial \rho}{\partial t} = 0, \quad \frac {\partial J}{\partial t} = 0\tag{5.32}
$$

的规则。当然，在实际情况中并没有真正稳定的电流，就像没有真正静止的电荷一样。从这个意义上讲，静电学和静磁学所描述的仅是存在于书本中的人为世界。但是，只要实际的涨落十分缓慢或是渐进的，它们就代表合适的近似值。事实上，对大多数的目的而言，静磁学可以很好地适用于每秒交替120次的家庭电流！

注意到运动的点电荷不可能形成稳恒电流。如果它某一瞬间在这里，下一瞬间就会到别处。这在你看来可能是一个小问题，但对我而言却是一个头痛的问题。在静电学中，我从静止点电荷这种简单情况开始，展开每个主题的学习。然后，我又通过利用叠加原理将其推广到任意电荷分布的情况。在静磁学中，这种方法对我们来说并不适用，因为运动的点电荷不可能形成一个静磁场。所以从一开始我们就不得不去处理扩展的电流分布情况，因此，论证过程必然会更加复杂和烦琐。

当导线中通入稳恒电流时，在导线中各处电流的大小 I 必须始终是一样的；否则，电荷会在导线某处积累，那它将不再是稳恒电流。一般而言，由于在静磁学中 $\partial\rho/\partial t=0$ ，因此，连续性方程 (5.29) 变为

$$
\nabla \cdot \boldsymbol {J} = 0\tag{5.33}
$$

## 5.2.2 稳恒电流的磁场

稳恒线电流产生的磁场由毕奥-萨伐尔定律给出：

$$
\boxed {B (\boldsymbol {r}) = \frac {\mu_ {0}}{4 \pi} \int \frac {\boldsymbol {I} \times \hat {\boldsymbol {r}}}{r ^ {2}} \mathrm{d} l ^ {\prime} = \frac {\mu_ {0}}{4 \pi} I \int \frac {\mathrm{d} l ^ {\prime} \times \hat {\boldsymbol {r}}}{r ^ {2}}}\tag{5.34}
$$

积分沿着电流流动方向的路径进行； $dl'$ 是沿导线的长度微元，如同前面一样，z 是从源点指向点 r 的矢量（图 5.17）。常数 $\mu_{0}$ 称为真空磁导率（permeability of free space） $^{9}$ 。

$$
\mu_ {0} = 4 \pi \times 1 0 ^ {- 7} \mathrm{N/A} ^ {2}\tag{5.35}
$$

B 的单位是牛顿每安培米（根据洛伦兹力定律要求）或特拉斯（teslas，T） $^{10}$ ：

$$
1 \mathrm{T} = 1 \mathrm{N} / (\mathrm{A} \cdot \mathrm{m})\tag{5.36}
$$

作为静磁学的基础，毕奥-萨伐尔定律所起的作用类似于库仑定律在静电学中所起的作用。事实上，对这两个定律都有相同的 $1 / \nu^2$ 依赖关系。

![](images/e5491d5b977843c49ed1551371d548e5e92204e865de9f0fa4fb39a97f949967.jpg)  
图5.17

例题5.5 如图5.18所示，求距离通有稳恒电流 $I$ 的长直导线 $s$ 处的磁场。

[解答] 在图中， $(\mathrm{d}l^{\prime}\times \hat{\mathbf{z}})$ 指向纸面外，其大小为

$$
\mathrm{d} l ^ {\prime} \sin \alpha = \mathrm{d} l ^ {\prime} \cos \theta
$$

由于 $l' = s\tan \theta$ ，所以

$$
\mathrm{d} l ^ {\prime} = \frac {s}{\cos^ {2} \theta} \mathrm{d} \theta
$$

由于 $s = 2\cos \theta$ ，所以

$$
\frac {1}{r ^ {2}} = \frac {\cos^ {2} \theta}{s ^ {2}}
$$

因此，

$$
\begin{array}{r l} B & = \frac {\mu_ {0} I}{4 \pi} \int_ {\theta_ {1}} ^ {\theta_ {2}} \left(\frac {\cos^ {2} \theta}{s ^ {2}}\right) \left(\frac {s}{\cos^ {2} \theta}\right) \cos \theta \mathrm{d} \theta \\ & = \frac {\mu_ {0} I}{4 \pi s} \int_ {\theta_ {1}} ^ {\theta_ {2}} \cos \theta \mathrm{d} \theta = \frac {\mu_ {0} I}{4 \pi s} (\sin \theta_ {2} - \sin \theta_ {1}) \end{array}\tag{5.37}
$$

![](images/6a1e0ea25413e5f6bdebbec19abfd968a2302f2a28e242458a44fdae98be1599.jpg)  
图5.18

由初始角度 $\theta_{1}$ 和最终的角度 $\theta_{2}$ , 式 (5.37) 给出了任何一段直线在某点处产生的磁场（图 5.19）。当然, 有限的一段导线本身并不能维持稳恒电流（当电荷达到终点时, 它将会流向哪里呢?），但它可以是某个闭合电路的一部分。式 (5.37) 只代表导线段对整个磁场的贡献。在无限长直导线情况下, $\theta_{1} = -\pi / 2$ , $\theta_{2} = \pi / 2$ , 因此得到

$$
B = \frac {\mu_ {0} I}{2 \pi s}\tag{5.38}
$$

请注意，如同无限长线电荷所产生的电场一样，周围某点的磁场与距无限长导线的距离成反比？在导线下方的区域，B 的方向指向纸面内；通常，根据右手规则，磁场方向是“绕”着导线“转”（图5.3）。

$$
\boldsymbol {B} = \frac {\mu_ {0} I}{2 \pi s} \hat {\phi}\tag{5.39}
$$

![](images/c8ce8f6a2080f21768a2c84c460c7bef0bb5a105bc6d22e8cf8d33cdb820764e.jpg)  
直导线段  
图5.19

作为一个应用，让我们求出相距为 $d$ 的长直且平行的导线之间的吸引力，这两根导线分别通有电流 $I_{1}$ 和 $I_{2}$ （图5.20）。导线（1）在导线（2）处产生的磁场为

$$
B = \frac {\mu_ {0} I _ {1}}{2 \pi d}
$$

它的方向指向纸内。洛伦兹力定律 [以适合线电流的形式，式 (5.17)] 给出导线（2）受到的力是指向导线（1）的，其大小为

$$
F = I _ {2} \left(\frac {\mu_ {0} I _ {1}}{2 \pi d}\right) \int \mathrm{d} l
$$

毫不奇怪，合力是无穷大的。但单位长度的力是

$$
f = \frac {\mu_ {0}}{2 \pi} \frac {I _ {1} I _ {2}}{d}\tag{5.40}
$$

如果电流方向是反向的（一个向上，一个向下），则它们之间是排斥力——再次与第 5.1.1 节中定性观察相一致。

![](images/eaa43eb5c255b283d8dd136b10557734e3a3e2779b88e6129232440b7c3c55dc.jpg)  
图5.20

例题5.6 如图5.21所示，求半径为 $R$ 的圆环中心上方距离为 $z$ 处的磁场强度，该圆环通有稳恒电流 $I$ 。

![](images/657cc7ac6a288b7a4f1a557c6bdad542de7fbf59c4f7317b555a36be43cb5cf5.jpg)  
图5.21

[解答] 电流元 $dl'$ 产生的磁场 $\mathrm{dB}$ 方向如图5.21所示，当对 $\mathrm{dl'}$ 沿圆环进行积分时， $\mathrm{dB}$ 扫过一个圆锥面，水平分量相互抵消为零，竖直分量之和为

$$
B (z) = \frac {\mu_ {0}}{4 \pi} I \int \frac {\mathrm{d} l ^ {\prime}}{r ^ {2}} \cos \theta
$$

（请注意，本题中 $\mathrm{d}l'$ 和 $\hat{\pmb{\imath}}$ 是相互垂直的； $\cos \theta$ 因子投影出竖直分量。）由于 $\cos \theta$ 和 $x^2$ 均为常数， $\int \mathrm{d}l'$ 就是简单的周长 $2\pi R$ ，所以

$$
B (z) = \frac {\mu_ {0} I}{4 \pi} \left(\frac {\cos \theta}{\hbar^ {2}}\right) 2 \pi R = \frac {\mu_ {0} I}{2} \frac {R ^ {2}}{(R ^ {2} + z ^ {2}) ^ {3 / 2}}\tag{5.41}
$$

对于面电流和体电流，毕奥-萨伐尔定律分别为

$$
\pmb {B} \left(\pmb {r}\right) = \frac {\mu_ {0}}{4 \pi} \int \frac {\pmb {K} \left(\pmb {r} ^ {\prime}\right) \times \hat {\pmb {\lambda}}}{\mathfrak {r} ^ {2}} \mathrm{d} a ^ {\prime} \quad \text {和} \quad \pmb {B} \left(\pmb {r}\right) = \frac {\mu_ {0}}{4 \pi} \int \frac {\pmb {J} \left(\pmb {r} ^ {\prime}\right) \times \hat {\pmb {\lambda}} ^ {\prime}}{\mathfrak {r} ^ {2}} \mathrm{d} \tau^ {\prime}\tag{5.42}
$$

利用式 $(5.30)$ 的“约定”，你可能想写出运动点电荷的相应公式：

$$
B (\boldsymbol {r}) = \frac {\mu_ {0}}{4 \pi} \frac {q \boldsymbol {v} \times \hat {\boldsymbol {r}}}{r ^ {2}}\tag{5.43}
$$

但这完全是错误的 $^{11}$ ，正如我之前提到的，点电荷并不能形成稳恒电流，而毕奥-萨伐尔定律仅适用于稳恒电流，并不能正确确定其磁场。

如同电场中的叠加原理一样，叠加原理对磁场也同样适用：如果你有一组源电流，则总磁场就是各个源电流分别产生的磁场的矢量和。

## 习题5.8

（a）如图5.22所示，一正方形环通有稳恒电流 $I$ 。设其中心到边的距离为 $R$ ，求正方形环中心的磁场。

![](images/6e432d0e1835549ebefdc5fda39992c76ec05c17aba5354a32d2e75726362507.jpg)  
图5.22

（b）求通有稳恒电流 I 的正 n 边形中心的磁场，同样设 R 是从其中心到任意一边的距离。

(c) 验证你的结果是否在极限 $n \to \infty$ 时简化为圆环中心的磁场。

习题 5.9 对于图 5.23 所示的每种稳恒电流分布，求 P 点处的磁场。

![](images/91bb70fc199a5d90d1158df12b69a712ece192be8e30272ae4b4d5998a3c49fe.jpg)  
a)

![](images/63956879aa16235a35959713832033687387b7ab1a6c16a4addbfd4f43d0217c.jpg)  
b)  
图5.23

习题5.10

（a）如图 5.24a 所示，正方形环放在一无限长直导线附近，环和导线均通有恒定电流 I。求环所受到的力。

(b) 求图 5.24b 中三角环所受到的力。

![](images/11d62a047a24480358377fb318a9bc8f5c91adb829d708a46460e62379766375.jpg)  
a)

![](images/8514d965f77f22eb34f3b832e9814743c74a185034e7ad1f969db332b819824c.jpg)  
b)  
图5.24

习题 5.11 求紧密缠绕的（螺旋线圈）螺旋管中心轴线上 P 点处的磁场。该螺线管每单位长度上缠绕有 n 匝线圈，线圈缠绕在半径为 a 的圆柱形管上，并通有稳恒电流 I（图 5.25）。用 $\theta_{1}$ 和 $\theta_{2}$ 来表示你的结果（这样最简单）。考虑到每匝线圈基本上都是圆形的，可以利用例题 5.6 的结果。无限长螺旋线管轴线上的磁场是多少？（双向无限）

![](images/76da457a2ca99c6a944fb2f21ca24afc4055c16c2a1cce4f50a75be37b4a1240.jpg)  
图5.25

习题 5.12 利用例题 5.6 的结果计算半径为 R、总电荷为 Q、以恒定角速度 $\omega$ 旋转的均匀带电球壳中心的磁场。

习题5.13 假设你有两根无限长直导线，线电荷密度均为 $\lambda$ ，相距为 $d$ ，两导线均以恒定速度 $v$ 运动（图5.26）。为了使磁场之间的吸引力和电荷间的排斥力相互平衡， $v$ 必须为多大？算出具体的数字。这样的速度合理吗[12]？

![](images/14daf2d0c20ddb1295a01e3e0349847fa6b819eeb408d130b7ecb77d7f732204.jpg)  
图5.26

## 5.3 直线电流 $B$ 的散度和旋度

## 5.3.1 直线电流

图 5.27 所示为无限长直导线的磁场（电流方向沿纸面向外），很明显可以看出这个场的旋度不为零（这是你在静电场中永远不会看到过的）。让我们来计算一下。

![](images/c493776e43868e15bfceeb319181e4c009d3b10979f4d4d1b55d6d1e7eafa8e6.jpg)  
图5.27

根据式 (5.38)，沿以导线为中心、半径为 $s$ 的圆形路径 $\pmb{B}$ 的积分是

$$
\oint \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {l} = \oint \frac {\mu_ {0} I}{2 \pi s} \mathrm{d} l = \frac {\mu_ {0} I}{2 \pi s} \oint \mathrm{d} l = \mu_ {0} I
$$

请注意, 这个结果与 $s$ 无关; 这是因为 $\pmb{B}$ 随着圆周长增加而以相同的比率减小。实际上, 积分路径不一定非得是一个圆; 任意一个环绕电流的闭合路径都会给出同样的结果。如果我们使用柱坐标 $(s, \varphi, z)$ , 电流沿 $z$ 轴方向流动, 则 $\pmb{B} = (\mu_0 I / 2\pi s) \hat{\phi}$ , 且 $\mathrm{d}\pmb{l} = \mathrm{d}s \hat{s} + s \mathrm{d}\phi \hat{\phi} + \mathrm{d}z \hat{z}$ , 所以

$$
\oint \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {l} = \frac {\mu_ {0} I}{2 \pi} \oint \frac {1}{s} s \mathrm{d} \phi = \frac {\mu_ {0} I}{2 \pi} \int_ {0} ^ {2 \pi} \mathrm{d} \phi = \mu_ {0} I
$$

以上假设环路恰好环绕导线一周；如果它环绕了两周，则 $\phi$ 角度将从0到 $4\pi$ ；如果它根本不环绕导线，如图5.28所示，先从 $\phi_{1}$ 到 $\phi_{2}$ ，然后再从 $\phi_{2}$ 到 $\phi_{1}$ ，则 $\int \mathrm{d}\varphi = 0$ 。

![](images/4b3b33d6d77ee201d9ea532574a4329341a59c6d427302d453cc20a4611428a2.jpg)  
图5.28

现在假设我们有许多直导线，穿过积分回路的每根导线都贡献 $\mu_{0}I$ ，位于回路外面的导线的贡献为零（图 5.29）。则线积分为

$$
\oint \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {l} = \mu_ {0} I _ {\mathrm{enc}}\tag{5.44}
$$

![](images/6c64a77faae564f8a864dddda62edb021a3eb60985ab838610542a22a4b32cd5.jpg)  
图5.29

其中 $I_{enc}$ 代表闭合回路内所包含的总电流。如果电荷流用体电流密度 J 来表示，则包含的电流为

$$
I _ {\mathrm{enc}} = \int J \cdot \mathrm{d} a\tag{5.45}
$$

其中积分覆盖由闭合环路所围成的任何曲面。将斯托克斯定理应用于式(5.42)，则有

$$
\int (\nabla \times \boldsymbol {B}) \cdot \mathrm{d} \boldsymbol {a} = \mu_ {0} \int \boldsymbol {J} \cdot \mathrm{d} \boldsymbol {a}
$$

因此，

$$
\nabla \times \boldsymbol {B} = \mu_ {0} \boldsymbol {J}\tag{5.46}
$$

实际上，我们已经轻而易举地得到了 B 旋度的一般表示式。但这里存在的一个严重问题是我们的推导过程基于无限长直导线及它们的组合为前提。大多数导线形状不可能是无限长直导线的组合，因此我们没有依据假设式 (5.44) 也适用于它们。因此，下一节将从毕奥-萨伐尔定律出发，对 B 的散度和旋度给出一个严格推导。

## 5.3.2 $B$ 的散度和旋度

在一般情况下，体电流的毕奥-萨伐尔定律给出

$$
\boldsymbol {B} (\boldsymbol {r}) = \frac {\mu_ {0}}{4 \pi} \int \frac {\boldsymbol {J} (\boldsymbol {r} ^ {\prime}) \times \hat {\boldsymbol {r}}}{r ^ {2}} \mathrm{d} \tau^ {\prime}\tag{5.47}
$$

该公式通过对电流分布 $J(x', y', z')$ 的积分，给出了点 $r = (x, y, z)$ 处的磁场（图 5.30）。现在我们最好明确一下每个物理量：

$$
\pmb {B} \text {是} (x, y, z) \text {的函数}
$$

$J$ 是 $(x', y', z')$ 的函数

$$
\begin{array}{r l} \boldsymbol {z} & = (x - x ^ {\prime}) \hat {\boldsymbol {x}} + (y - y ^ {\prime}) \hat {\boldsymbol {y}} + (z - z ^ {\prime}) \hat {\boldsymbol {z}} \\ & \mathrm{d} \tau^ {\prime} = \mathrm{d} x ^ {\prime} \mathrm{d} y ^ {\prime} \mathrm{d} z ^ {\prime} \end{array}
$$

积分是对带撇的坐标系进行的；而散度和旋度是对不带撇的坐标进行的。

![](images/9c60784f4c923289b5d7dd0b4c19c43108bfb9d1d9edfc97964dea203e2bd6cd.jpg)  
图5.30

对式 (5.47) 求散度，我们得到

$$
\nabla \cdot \boldsymbol {B} = \frac {\mu_ {0}}{4 \pi} \int \nabla \cdot \left(\boldsymbol {J} \times \frac {\hat {\boldsymbol {r}}}{r ^ {2}}\right) \mathrm{d} \tau^ {\prime}\tag{5.48}
$$

利用矢量积规则（6）

$$
\nabla \cdot \left(\boldsymbol {J} \times \frac {\hat {\boldsymbol {r}}}{r ^ {2}}\right) = \frac {\hat {\boldsymbol {r}}}{r ^ {2}} \cdot (\nabla \times \boldsymbol {J}) - \boldsymbol {J} \cdot \left(\nabla \times \frac {\hat {\boldsymbol {r}}}{r ^ {2}}\right)\tag{5.49}
$$

因为 J 与不带撇的坐标 $(x,y,z)$ 无关，所以 $\nabla \times J = 0$ 。且 $\nabla \times (\hat{\mathbf{z}} / r^{2}) = 0$ （见习题 1.63），所以

$$
\boxed {\nabla \cdot \boldsymbol {B} = 0}\tag{5.50}
$$

显然，磁场的散度为零。

对式 (5.47) 求旋度，我们得到

$$
\nabla \times \boldsymbol {B} = \frac {\mu_ {0}}{4 \pi} \int \nabla \times \left(\boldsymbol {J} \times \frac {\hat {\boldsymbol {r}}}{r ^ {2}}\right) \mathrm{d} \tau^ {\prime}\tag{5.51}
$$

同样，我们的方法是使用适当的矢量积规则把被积函数展开——在本例中是积规则（8）：

$$
\nabla \times \left(\boldsymbol {J} \times \frac {\hat {\boldsymbol {r}}}{r ^ {2}}\right) = \boldsymbol {J} \left(\nabla \cdot \frac {\hat {\boldsymbol {r}}}{r ^ {2}}\right) - (\boldsymbol {J} \cdot \nabla) \frac {\hat {\boldsymbol {r}}}{r ^ {2}}\tag{5.52}
$$

[由于 $J$ 与 $(x,y,z)$ 无关，我已经把含有 $J$ 散度的项去掉了。]正如我们将在下一段中看到的那样，第二项的积分为零。第一项涉及我们在第1章中要努力计算的散度[式(1.100)]：

$$
\nabla \cdot \left(\frac {\hat {\mathbf {r}}}{\mathbf {r} ^ {2}}\right) = 4 \pi \delta^ {3} (\mathbf {r})\tag{5.53}
$$

这样

$$
\nabla \times \boldsymbol {B} = \frac {\mu_ {0}}{4 \pi} \int \boldsymbol {J} (\boldsymbol {r} ^ {\prime}) 4 \pi \delta^ {3} (\boldsymbol {r} - \boldsymbol {r} ^ {\prime}) \mathrm{d} \tau^ {\prime} = \mu_ {0} \boldsymbol {J} (\boldsymbol {r})
$$

这证实了式 $(5.46)$ 并不限于直线电流，而是在静磁学中普遍成立。

然而，为了完成整个推导过程，我们必须验证式(5.52)中的第二项积分是否为零。因为散度仅作用在 $\hat{\mathbf{z}} / \mathbf{v}^2$ 上，我们通过加上一个负号将 $\nabla$ 转换为 $\nabla'^{13}$

$$
- (\boldsymbol {J} \cdot \nabla) \left(\frac {\hat {\boldsymbol {r}}}{r ^ {2}}\right) = (\boldsymbol {J} \cdot \nabla^ {\prime}) \frac {\hat {\boldsymbol {r}}}{r ^ {2}}\tag{5.54}
$$

特别是坐标 $x$ 分量

$$
\left(\boldsymbol {J} \cdot \nabla^ {\prime}\right) \left(\frac {x - x ^ {\prime}}{r ^ {3}}\right) = \nabla^ {\prime} \cdot \left[ \frac {(x - x ^ {\prime})}{r ^ {3}} \boldsymbol {J} \right] - \left(\frac {x - x ^ {\prime}}{r ^ {3}}\right) (\nabla^ {\prime} \cdot \boldsymbol {J})
$$

（利用了积规则第5条）。由于对稳恒电流， $J$ 的散度为零[式(5.33)]，因此

$$
\left[ - \left(\boldsymbol {J} \cdot \nabla\right) \frac {\hat {\mathbf {r}}}{r ^ {2}} \right] _ {x} = \nabla^ {\prime} \cdot \left[ \frac {(x - x ^ {\prime})}{r ^ {3}} \boldsymbol {J} \right]
$$

所以，对积分 [式 (5.51)] 的贡献可以写为

$$
\int_ {\mathcal {V}} \nabla^ {\prime} \cdot \left[ \frac {(x - x ^ {\prime})}{r ^ {3}} J \right] \mathrm{d} \tau^ {\prime} = \oint_ {\mathcal {S}} \frac {(x - x ^ {\prime})}{r ^ {3}} J \cdot \mathrm{d} a ^ {\prime}\tag{5.55}
$$

（分部积分是允许从 $\nabla$ 转换到 $\nabla'$ 的原因。）但是，我们应对哪个区域进行积分呢？它是毕奥-萨伐尔定律中出现的空间区域——它足够大，以包括所有的电流。如果你愿意，它还可以是更大的空间区域；只不过在外面的区域 $J = 0$ ，因此它对积分没有任何贡献。关键点是：边界上的电流为零（所有电流一定都处在内部），因此对表面的积分[式(5.55)]为零 $^{14}$ 。

## 5.3.3 安培定律

$\pmb{B}$ 的旋度方程为

$$
\boxed {\nabla \times \boldsymbol {B} = \mu_ {0} \boldsymbol {J}}\tag{5.56}
$$

称为（微分形式）安培定律（Ampère's law）。它可以通过应用一个基本定理转换成积分形式——在现在这种情况下就是斯托克斯定理：

$$
\int (\nabla \times \boldsymbol {B}) \cdot \mathrm{d} \boldsymbol {a} = \oint \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {l} = \mu_ {0} \int \boldsymbol {J} \cdot \mathrm{d} \boldsymbol {a}
$$

这里 $\int J\cdot \mathrm{d}\pmb{a}$ 是所有流过曲面的电流（图5.31），我们称作 $I_{\mathrm{enc}}$ [安培环路（Amperian loop）所包围的电流]。因此

$$
\boxed {\oint \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {l} = \mu_ {0} I _ {\mathrm{enc}}}\tag{5.57}
$$

这就是安培定律的积分形式；它将式(5.42)推广到任何的稳恒电流情况。请注意，式(5.57)继承了斯托克斯定理中的正负号的不确定性（见1.3.5节）：积分路径应该是沿哪个环路？通过表面的哪个方向对应于“正”电流方向？其答案还是右手定则：如果你右手四指环绕的方向为积分回路的方向，则大拇指的方向就是正电流的方向。

![](images/50de49cd49ed2c0ae287c6f2ce5319884cecad684c0e3cec510d0fa378d4ba5c.jpg)  
图5.31

正如毕奥-萨伐尔定律在静磁学中起的作用如同库仑定律在静电学中的作用一样，所以安培定律也起着如同高斯定理一样的作用：

$$
\left\{\begin{array}{l l}{{\mathrm{静电学}: \mathrm{库仑} \rightarrow \mathrm{高斯}}}\\{{\mathrm{静磁学}: \mathrm{毕奥-萨伐尔} \rightarrow \mathrm{安培}}}\end{array}\right.
$$

特别是，对于具有适当的对称性的电流，积分形式的安培定律提供了一种非常简洁有效的计算磁场的方法。

例题5.7如图5.32所示，求距通有稳恒电流 $I$ 的长直导线距离为 $s$ 的点处的磁场。（与在例题5.5中利用毕奥-萨伐尔定律求解过的问题相同。）

![](images/87d3c74bc5c33a61b7e2e4a47951613712b67c16258e67755784b7246e4690fc.jpg)  
图5.32

[解答] 我们知道 B 的方向是 “环绕形的”，如右手定则所示围绕金属导线旋转，根据对称性磁场 B 的大小在以导线为中心、半径为 s 的安培环路上为恒定值。因此安培定律给出

$$
\oint \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {l} = B \oint \mathrm{d} l = B 2 \pi s = \mu_ {0} I _ {\mathrm{enc}} = \mu_ {0} I
$$

$$
B = \frac {\mu_ {0} I}{2 \pi s}
$$

这与我们之前得到的答案相同 [式 (5.38)]，但这次要容易得多。

例题5.8 如图5.33所示，求在无穷大 $xy$ 平面上流有均匀表面电流 $K = k\hat{x}$ 产生的磁场。

![](images/8432d1a7e930c4ecee09b9135c4e3b6e82571e813ae698e9bf03cfc9605375eb.jpg)  
图5.33

[解答] 首先，B 的方向指向哪里？它能有 x 方向的分量吗？没有，只要看一下毕奥-萨伐尔定律 [式 (5.39)]，我们就知道 B 是垂直于 K 的。那么 B 有 z 分量吗？同样是没有。你可以通过来自 +y 一边的细丝对 z 方向的贡献与来自相应的 -y 一边的细丝对 z 方向的贡献相互抵消来证明。但有一个更好的论证方法：假设磁场方向远离平面，通过反转电流的方向，我们可以使它指向平面（在毕奥-萨伐尔定律中，通过改变电流的方向可以改变磁场方向）。但 B 的 z 分量不可能与 xy 平面上的电流方向有关。（仔细考虑它！）因此，B 只能有一个 y 分量，用右手定则检验一下你很快就能确定磁场方向是在平面上方指向左侧，而在平面下方指向右侧。

基于这一点考虑，我们可以画一个矩形安培环路，如图5.33所示。它平行于 $yz$ 平面，上下两边距 $xy$ 平面的距离相同。应用安培定律，

$$
\oint \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {l} = 2 B l = \mu_ {0} I _ {\mathrm{enc}} = \mu_ {0} K l
$$

(一个 Bl 来自上部，一个 Bl 来自下部)，因此 $B = (\mu_{0}/2)K$ ，或者，更确切地

$$
B = \left\{ \begin{array}{l l} + (\mu_ {0} / 2) K \hat {\mathbf {y}}, & z <   0 \\ - (\mu_ {0} / 2) K \hat {\mathbf {y}}, & z > 0 \end{array} \right.\tag{5.58}
$$

请注意，磁场大小与到平面的距离无关，这与均匀表面电荷的电场式一样（例题2.5）。

例题5.9如图5.34所示，长螺线管由半径为 $R$ 的圆柱体每单位长度上紧密缠绕 $n$ 匝线圈组成，线圈通有恒定电流 $I$ 。求长螺线管的磁场。[密绕是指我们可以把每匝都看作圆线圈。如果你对此感到不解（毕竟，无论线圈绕得多么密，沿螺线管轴线方向都有净电流 $I$ ），请把它想象成一张通有均匀表面电流 $K = nI$ 的铝箔包裹在柱体表面（图5.35）。或者做一个双向的环绕，当线圈绕到一端后——然后保持绕向不变——再原路绕回，从而这样就消除了净纵向电流。但是，事实上这些没有必要这样严格，因为（相对来说）螺线管内部的磁场是非常大的，纵向电流的磁场至多是一个微小的修正。]

![](images/e11ac488dbffbb48f0e426f34734740fa667e634824ee187446f01d0ba770025.jpg)  
图5.34

![](images/a2546bb8ee233a6d4bb08fded3cb850da5c7aa7cf92ac621ea82ace0662b91b9.jpg)  
图5.35

[解答] 首先，B 的方向是什么？它能有径向分量吗？没有，因为若假设 $B_{s}$ 是正向的；如果我们使电流的方向反向，则 $B_{s}$ 会变成负向的。但在物理上切换电流 I 的方向等同于将螺线管的上下端颠倒，这当然不会改变径向电场方向。那么有“环绕”的分量吗？没有，因为与螺线管同心的安培环路上 $B_{\phi}$ 是常量（图 5.36），得

$$
\oint \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {l} = B _ {\varphi} (2 \pi s) = \mu_ {0} I _ {\mathrm{enc}} = 0
$$

因为闭合环路内没有电流。

![](images/3c7800a0db93f2f5944c565ae6a266e91ed6b03ab16b528f954b01011837b32a.jpg)  
图5.36

因此，无限长密绕的螺线管内的磁场平行于轴线。根据右手定则，我们预期在螺线管内部它的方向向上，在外部它的方向向下。此外，在很远处它将趋于零。考虑到这一点，让我们将安培定律应用于图5.37中的两个矩形环，回路1完全位于螺线管外面，其侧面距离轴线的距离分别为 $a$ 和 $b$

$$
\oint \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {l} = [ B (a) - B (b) ] L = \mu_ {0} I _ {\mathrm{enc}} = 0
$$

所以

$$
B (a) = B (b)
$$

显然，外部的磁场与距轴线的距离无关。但我们确切知道当距离 $s$ 很大时磁场应为零。因此，在外部它必须处处都为零。（当然，这个令人惊讶的结论也可以从毕奥-萨伐尔定律中得出，但计算要困难得多。见习题5.46。）

![](images/fcfa6443daa72bb6e945169f1f08ed839724b93c80eb00d4db55b2f686e2038b.jpg)  
图5.37

对一半在螺线管内一半在其外部的回路2，安培定律给出

$$
\oint \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {l} = B L = \mu_ {0} I _ {\mathrm{enc}} = \mu_ {0} n I L
$$

其中 B 为螺线管内的磁场。(由于外面磁场 B = 0，回路的右边没有贡献)。结论是：

$$
B = \left\{ \begin{array}{l l} {{\mu_ {0} n I \hat {z},}} & {{\text {螺线管内部}}} \\ {{0,}} & {{\text {螺线管外部}}} \end{array} \right.\tag{5.59}
$$

请注意，螺线管内的磁场是均匀的，它与距轴线的距离无关；从这个意义上说，螺线管对静磁学的作用就像平行板电容器对静电学的作用一样：一种产生均匀磁场的简单装置。

与高斯定理一样，（对于稳恒电流）安培定律也总是正确的，但它并不总是有用的。只有当研究的问题的对称性使你能够将 B 移到积分 $\oint B \cdot dl$ 的外面时，你才能根据安培定律来计算磁场。如果能够用安培定律，这将是迄今为止最快的方法；如果不能应用安培定律，你将不得不求助于毕奥-萨伐尔定律。可应用安培定律的电流形状有

1. 无限长直电流（范例：例题5.7）

2. 无限大平面（范例：例题5.8）

3. 无限长螺线管（范例：例题 5.9）

4. 环形线圈（范例：例题5.10）

最后的形状是安培定律应用中最奇妙和优美的一个。与习题 5.8 和习题 5.9 一样，难点在于确定磁场的方向（我们现在一劳永逸地对这四种几何形状中的每个确定其磁场的方向）；而实际应用安培定律的内容仅占一行。

例题5.10 如图5.38所示，环形线圈由一个圆环或者“甜甜圈”组成，其周围包裹着一根长线。绕线均匀且足够紧密，因此每圈都可以被视为一个平面闭环。线圈横截面的形状无关紧要。为了简单起见，我在图5.38中将其当作矩形，但只要环截面形状保持不变，它也可以是圆形，或其他没有对称性的奇特形状，如图5.39所示。在这种情况下，我们可以得出结论：环形线圈的磁场在线圈内外的所有点都是圆周形的。

![](images/250c1f61b645e32cda8e24258649d4027902299b2c64c7707a38b602507023c8.jpg)  
图5.38

![](images/169adb9645fc1ee6656b97a99b7e893521bda70b97a71ce25db150db2d829e9a.jpg)  
图5.39

证明：根据毕奥-萨伐尔定律， $r'$ 处的电流元在r处产生的磁场是

$$
\mathrm{d} B = \frac {\mu_ {0}}{4 \pi} \frac {I \times \hat {\mathbf {z}}}{r ^ {3}} \mathrm{d} l ^ {\prime}
$$

我们也可以把 $r$ 取在 $xz$ 平面内（图5.39），所以它的直角坐标分量为 $(x,0,z)$ ，电流元的坐标为

$$
\boldsymbol {r} ^ {\prime} = \left(s ^ {\prime} \cos \phi^ {\prime}, s ^ {\prime} \sin \phi^ {\prime}, z ^ {\prime}\right)
$$

再者

$$
\pmb {n} = \left(x - s ^ {\prime} \cos \varphi^ {\prime}, - s ^ {\prime} \sin \varphi^ {\prime}, z - z ^ {\prime}\right)
$$

由于电流没有 $\phi$ 分量，所以 $I = I_{s}\hat{s} + I_{z}\hat{z}$ ，或者（在直角坐标系中）

$$
I = \left(I _ {s} \cos \phi^ {\prime}, I _ {s} \sin \phi^ {\prime}, I _ {z}\right).
$$

因此

$$
\begin{array}{r l} & {\pmb {I} \times \pmb {\mathscr {r}} = \left[ \begin{array}{c c c} \hat {\pmb {x}} & \hat {\pmb {y}} & \hat {\pmb {z}} \\ I _ {s} \cos \phi^ {\prime} & I _ {s} \sin \phi^ {\prime} & I _ {z} \\ (x - s ^ {\prime} \cos \phi^ {\prime}) & (- s ^ {\prime} \sin \phi^ {\prime}) & (z - z ^ {\prime}) \end{array} \right]} \\ & {\quad = [ \sin \phi^ {\prime} (I _ {s} (z - z ^ {\prime}) + s ^ {\prime} I _ {z}) ] \hat {\pmb {x}}} \\ & {\quad \quad + [ I _ {z} (x - s ^ {\prime} \cos \phi^ {\prime}) - I _ {s} \cos \phi^ {\prime} (z - z ^ {\prime}) ] \hat {\pmb {y}} + [ - I _ {s} x \sin \phi^ {\prime} ] \hat {\pmb {z}}} \end{array}
$$

但在位置 $r''$ 处有一个对称的电流元（图5.39），具有相同的 $s'$ 、相同的 $\mathfrak{z}$ 、相同的 $\mathrm{dl}'$ 、相同的 $I_{s}$ 和相同的 $I_{z}$ ，但 $\phi'$ 为负。因为 $\sin \varphi'$ 改变了符号，所以 $r'$ 和 $r''$ 两点处电流元在 $\hat{x}$ 和 $\hat{z}$ 方向对磁场的贡献相互抵消，仅有 $\hat{y}$ 分量。因此，在 $r$ 处的磁场沿 $\hat{y}$ 方向，通常情况下磁场沿 $\hat{\phi}$ 方向。

既然我们知道磁场是圆周的，那么确定它的大小就十分容易。只需将安培定律应用于绕中心轴的半径为 $s$ 的圆上：

$$
B 2 \pi s = \mu_ {0} I _ {\mathrm{enc}}
$$

因此

$$
B (r) = \left\{ \begin{array}{l l} { \frac {\mu_ {0} N I}{2 \pi s} \hat {\phi},} & {\text {圆环内部的点}} \\ {0,} & {\text {圆环外部的点}} \end{array} \right.\tag{5.60}
$$

其中 $N$ 是总匝数。

习题5.14 如图5.40所示，半径为 $a$ 的长圆柱形导线流有恒定电流 $I$ 。求下面情况下导线内外的磁场。

(a) 电流均匀地分布在电线的外表面上。

(b) 电流密度 J 的分布与离轴的距离 s 成正比。

![](images/174e991a2e2e37c8a70eb7cf019a9de79ae398b7ba26859096987345ee21fd9b.jpg)  
图5.40

习题5.15 如图5.41所示，从 $z = -a$ 延伸到 $z = a$ （在 $x$ 和 $y$ 方向上为无穷大）厚板分布有均匀的体电流密度 $J = J\hat{x}$ 。求作为函数 $z$ 的板内、板外磁场大小。

![](images/3b75aeaa8e11dac25b3df4568f7c7bd1e82ce4ebdc86d063fae3c959c11b22ae.jpg)  
图5.41

习题 5.16 如图 5.42 所示，两个长同轴螺线管都通有恒定电流 I，但电流方向相反。内螺线管（半径为 a）单位长度上有 $n_{1}$ 匝线圈，外螺线管（半径为 b）单位长度上有 $n_{2}$ 匝线圈，求出下列三个区域中的磁场：（1）内螺线管的里面；（2）两螺线管之间；（3）两个螺线管的外面。

![](images/a94830fc3ebd19067320b683d6e5aa108638aac4a575ab1806ec075bb1fb3737.jpg)  
图5.42

习题 5.17 如图 5.43 所示，一个上下极板分别具有均匀表面电荷 $\pm\sigma$ 的大型平行板电容器以恒定速率 v 运动。

(a) 求极板之间以及上方和下方的磁场。

(b) 求上极板单位面积所受的磁场力及其方向。

(c) 磁场力和电场力平衡时，电容器运动速率 v 应为大 $^{15}$ ?

![](images/19bcaf447c2fe2a27097004a1b87c4cd4949be330ced6e5e6a1e223044d4d7e8.jpg)  
图5.43

!习题 5.18 证明：对于无限长螺线管，无论其横截面积形状如何，只要它沿螺线管的长度是不变的，则螺线管的磁场平行于轴线。螺线管内外的磁场是多少？证明当环形螺线管的半径很大时，以至于它其中的一段就可以认为基本是直的，环形螺线管内的场 [式 (5.60)] 还原为直螺线管的磁场。

习题5.19 在计算安培环路所包含的电流时，通常必须计算以下形式的积分：

$$
I _ {\mathrm{enc}} = \int_ {S} \boldsymbol {J} \cdot \mathrm{d} \boldsymbol {a}
$$

问题是，有无穷多个曲面共用相同的边界线，我们应该选用哪一个？

## 5.3.4 静磁学与静电学的比较

静电场的散度和旋度是

$$
\left\{ \begin{array}{l l} {\nabla \cdot \pmb {E} = \frac {1}{\varepsilon_ {0}} \rho} & {(\text {高斯定理})} \\ {\nabla \times \pmb {E} = \pmb {0}} & {(\text {没有名字})} \end{array} \right.
$$

这些是静电场麦克斯韦方程组（Maxwell's equations）。如果给定源电荷密度 $\rho$ ，麦克斯韦方程组与远离所有电荷处 $E \to 0$ 边界条件 $^{16}$ 结合在一起确定了电场；本质上，它们与库仑定律加上叠加原理所包含的信息基本一样。静磁学的散度和旋度为

$$
\left\{ \begin{array}{l l} {{\nabla \cdot B = 0}} & {{(\mathrm{没有名字})}} \\ {{\nabla \times B = \mu_ {0} J}} & {{(\mathrm{安培定理})}} \end{array} \right.
$$

这些是静磁场麦克斯韦方程组。同样，麦克斯韦方程与远离所有电流处 $B \rightarrow 0$ 的边界条件结合一起确定了磁场：它们等价于毕奥-萨伐尔定律（加叠加原理）。麦克斯韦方程组和

## 洛伦兹力定律

$$
\boldsymbol {F} = Q (\boldsymbol {E} + \boldsymbol {v} \times \boldsymbol {B})
$$

构成了静电学和静磁学最优美的表述。

电场背离正电荷；磁场环绕着电流（图5.44）。电场线源于正电荷，终止于负电荷；磁场线无头无尾——散度需要不为零。它们通常形成闭环或延伸到无穷远 $^{17}$ 。换句话说，B没有像电场E那样的点电荷源；不存在类似电荷的磁荷。这就是 $\nabla\cdot B=0$ 的物理含义。库仑和其他一些人相信磁场来源于磁荷（magnetic charges）（magnetic monopoles，我们现在称之为磁单极子），在一些老版书中，你依然可以找到关于磁场的库仑定律，描述它们之间的吸引力和排斥力。安培首先推测所有的磁效应都可归因于运动着的电荷（电流）。就目前所知，安培是正确的；然而磁单极子在自然界中是否存在仍然是一个悬而未决的实验课题（它们显然非常罕见，或许有人会发现一个 $^{18}$ ）；事实上，最近的一些基本粒子理论需要它们的存在。然而，就我们的目的而言，B是无散度的，并且磁单极子也不存在。磁场需要一个运动的电荷来产生，而“感知”它则需要另外一个运动电荷。

![](images/56f8f2c75f13066cf6897ddaf709c95ddce4a0c131a85ba3a95eeed20d257b32.jpg)  
a) 点电荷的电场

![](images/a2367a9de5e3e33857985402d6ea496b67095981017d605df2b51675e95aa2d4.jpg)  
b) 长导线的磁场  
图5.44

通常来讲，电场力要比磁场力大得多。这不是该理论本身固有的属性；这与基本常数 $\varepsilon_0$ 和 $\mu_0$ 的大小有关。一般来讲，只有当源电荷和测试电荷都以接近光速的速度运动时，磁力的强度才可能接近电场力（习题5.13和习题5.17阐明了这一规律）。那么，我们又是如何观察到磁效应的呢？答案是，无论是磁场的产生（毕奥-萨伐尔定律），还是探测磁场（洛伦兹力定律）都与电流戚戚相关，对于电荷很小的运动速度，我们可以通过向导线中注入大量电荷来弥补。通常，这种电荷会同时产生很大的电场力从而淹没磁场力。但是，我们如果能够在电线中嵌入等量、符号相反的静止电荷从而使导线保持电中性，电场就会相互抵消，仅剩下磁场。这听起来很复杂，但这正是普通载流导线中所发生的事情。

## 习题5.20

（a）设每个原子贡献一个自由电子，求一块铜中运动电荷的密度 $\rho$ （查阅必要的物理常数）。

(b) 计算直径为 $1\mathrm{mm}$ 、电流1A的铜导线中的平均电子速度。[注意：这简直是蜗牛的速度。那么，你怎么能进行长途电话交谈呢？]

(c) 相距为 $1\mathrm{cm}$ 的两根导线之间的吸引力是多少？

(d) 如果你能用某种方法移走导线中静止的正电荷，那么电场排斥力将是多少？它比磁场力大多少倍？

习题5.21 安培定律是否满足旋度的散度等于零的普适规则[式(1.46)]？证明：一般来说，安培定律对非静磁学并不成立。其他三个麦克斯韦方程中是否存在这样的“缺陷”？

习题5.22 假设确实存在磁单极子。你将如何修正麦克斯韦方程和洛伦兹力定律去和它们取得一致？列举你认为可行的几个方案，并给出建议如何通过实验来判定哪一个是正确的。

## 5.4 磁矢势

## 5.4.1 矢势

正如 $\nabla \times \pmb{E} = \mathbf{0}$ 允许我们在静电学中引入标势（V）一样，

$$
\boldsymbol {E} = - \nabla V
$$

那么，在静磁学中， $\nabla\cdot B=0$ 引入矢势 A:

$$
\boxed {B = \nabla \times A}\tag{5.61}
$$

前者是由定理1（1.6.2节）所赋予，后者是由定理2（定理2的证明在习题5.31中介绍）所赋予。矢势的这种表述自动满足 $\nabla \cdot B = 0$ （因为旋度的散度总是0）；依然存在安培定律

$$
\nabla \times \boldsymbol {B} = \nabla \times (\nabla \times \boldsymbol {A}) = \nabla (\nabla \cdot \boldsymbol {A}) - \nabla^ {2} \boldsymbol {A} = \mu_ {0} \boldsymbol {J}\tag{5.62}
$$

现在，电势有一个固有的歧义；你可以在不改变物理量 E 的情况下，将任何梯度为零的函数（也就是说，任何常数）加到 V 上。同样，你也可以将任何旋度为零的函数（即任何标量的梯度）加到 A 上，而对 B 没有任何影响。我们可以利用这种选择的自由性来使 A 的散度为零：

$$
\boxed {\nabla \cdot A = 0}\tag{5.63}
$$

为了证明这总是可能的，假设我们初始势 $A_0$ 的散度不为零。如果我们加上 $\lambda$ 的梯度 $(A = A_0 + \nabla \lambda)$ ，新的散度就是

$$
\nabla \cdot \boldsymbol {A} = \nabla \cdot \boldsymbol {A} _ {0} + \nabla^ {2} \lambda
$$

我们可以容纳式(5.63)，那么，如果可以找到满足以下条件的函数 $\lambda$

$$
\nabla^ {2} \lambda = - \nabla \cdot \mathbf {A} _ {0}
$$

新的矢势就满足式 (5.63)。这在数学上等同于泊松方程 [式 (2.24)]

$$
\nabla^ {2} V = - \frac {\rho}{\varepsilon_ {0}}
$$

用 $\nabla \cdot A_{0}$ 替代 $\rho/\varepsilon_{0}$ 作为 “源”。现在我们已经知道如何求解泊松方程——这是静电学的全部内容（“给定电荷分布，求电势”）。特别是，如果 $\rho$ 在无穷远处为零，则解为式 (2.29):

$$
V = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\rho}{\imath} \mathrm{d} \tau^ {\prime}
$$

基于同样的原因，如果 $\nabla \cdot A_0$ 在无限远处为零，则

$$
\lambda = \frac {1}{4 \pi} \int \frac {\nabla \cdot A _ {0}}{r} \mathrm{d} \tau^ {\prime}
$$

如果 $\nabla \cdot A_0$ 在无限远处不为零，我们必须使用其他方法找出合适的 $\lambda$ ，就如同我们在电荷分布扩展到无限远时通过其他方法得到电势一样。但要点依然存在：总是有可能使矢势的散度为零。换言之：当用定义 $B = \nabla \times A$ 确定了 $A$ 的旋度时，但它并没有给定 $A$ 的散度——我们可自由地选择，零通常是最简单的选择。

在 $\mathbf{A}$ 的这种条件下，安培定律[式(5.62)]变为

$$
\boxed {\nabla^ {2} \boldsymbol {A} = - \mu_ {0} \boldsymbol {J}}\tag{5.64}
$$

这也不过是泊松方程——或者更确切地说，这是三个泊松方程，每个直角坐标分量对应一个 $^{19}$ 。假设在无穷远处 J 为零，我们可以读取解：

$$
\boxed {A (\boldsymbol {r}) = \frac {\mu_ {0}}{4 \pi} \int \frac {\boldsymbol {J} \left(\boldsymbol {r} ^ {\prime}\right)}{\imath} \mathrm{d} \tau^ {\prime}}\tag{5.65}
$$

对于线电流和面电流

$$
\boldsymbol {A} = \frac {\mu_ {0}}{4 \pi} \int \frac {\boldsymbol {I}}{r} \mathrm{d} l ^ {\prime} = \frac {\mu_ {0} I}{4 \pi} \int \frac {1}{r} \mathrm{d} l ^ {\prime}; \quad \boldsymbol {A} = \frac {\mu_ {0}}{4 \pi} \int \frac {\boldsymbol {K}}{r} \mathrm{d} a ^ {\prime}\tag{5.66}
$$

(如果电流在无限远处不为零, 我们不得不利用其他的方法得到 A; 其中一些将在例题 5.12 和本节末尾的习题中进行探讨。)

必须说 A 并不像 V 那样有用。首先，它仍然是一个矢量，尽管式 (5.65) 和式 (5.64) 比毕奥-萨伐尔定律更容易计算，你仍然需要去处理分量。如果我们处理的是标量势，那就太方便了：

$$
\pmb {B} = - \nabla U\tag{5.67}
$$

但是，由于梯度的旋度是总是零，这和安培定律是不相容的。[如果你严格限在一个单连通的无电流区域，静磁标量势（magnetostatic scalar potential）是可以使用的，但作为一种理论工具，我们的兴趣有限，请参阅习题5.29。]此外，由于磁场力不做功，不能对 $\pmb{A}$ 简单地赋予每单位电荷的势能这样的物理解释。（在某些情况下，它可以被解释为每单位荷的动量20。）尽管如此，正如我们在第10章中看到的那样，矢势具有实质性的理论重要性。

例题5.11 如图5.45所示，半径为 $R$ 的球壳的表面分布有均匀电荷密度 $\sigma$ ，球壳以角速度 $\omega$ 旋转。求它在 $r$ 点产生的矢势。

![](images/a3b66ee42840ec84dee5c0d68443188b36a292d77b42c67c67387b437b567993.jpg)  
图5.45

[解答] 选取沿 $\omega$ 旋转的轴为极轴看起来很自然，但事实上，如果我们让 $r$ 位于 $z$ 轴上积分会更容易，这样 $\omega$ 与 $z$ 轴的夹角为 $\psi$ 。如图5.46所示，我们也可以确定 $x$ 轴的方向，使 $\omega$ 位于 $xz$ 平面内。根据式(5.66)，

$$
\boldsymbol {A} (\boldsymbol {r}) = \frac {\mu_ {0}}{4 \pi} \int \frac {\boldsymbol {K} (\boldsymbol {r} ^ {\prime})}{n} \mathrm{d} a ^ {\prime}
$$

![](images/ded33cec9e9a390c8169c0b9be028aa8029f75a5afaea5a02088f2fb4ad408b2.jpg)  
图5.46

其中 $K = \sigma v$ ， $\nu = \sqrt{R^2 + r^2 - 2Rr\cos\theta'}$ ， $\mathrm{da}^{\prime} = R^{2}\sin \theta^{\prime}\mathrm{d}\theta^{\prime}\mathrm{d}\phi^{\prime}$ 。在一个旋转刚体上 $r'$ 处的速度由 $\omega \times r'$ 给出；在这种情况下，

请注意，除了第一项以外，这些项中的每一项都涉及 $\sin \phi'$ 或 $\cos \phi'$ ，由于

$$
\int_ {0} ^ {2 \pi} \sin \phi^ {\prime} \mathrm{d} \phi^ {\prime} = \int_ {0} ^ {2 \pi} \cos \phi^ {\prime} \mathrm{d} \phi^ {\prime} = 0
$$

这些项对积分没有贡献。剩余的为

$$
A (r) = - \frac {\mu_ {0} R ^ {3} \sigma \omega \sin \psi}{2} \left(\int_ {0} ^ {\pi} \frac {\cos \theta^ {\prime} \sin \theta^ {\prime}}{\sqrt {R ^ {2} + r ^ {2} - 2 R r \cos \theta^ {\prime}}} \mathrm{d} \theta^ {\prime}\right) \hat {y}
$$

令 $u \equiv \cos \theta'$ ，积分变为

$$
\begin{array}{r} \int_ {- 1} ^ {+ 1} \frac {u}{\sqrt {R ^ {2} + r ^ {2} - 2 R r u}} \mathrm{d} u = - \frac {R ^ {2} + r ^ {2} + R r u}{3 R ^ {2} r ^ {2}} \left. \sqrt {R ^ {2} + r ^ {2} - 2 R r u} \right| _ {- 1} ^ {+ 1} \\ = - \frac {1}{3 R ^ {2} r ^ {2}} \left[ (R ^ {2} + r ^ {2} + R r) | R - r | - (R ^ {2} + r ^ {2} - R r) (R + r) \right] \end{array}
$$

如果 $r$ 位于球内，则 $R > r$ ，上面的表达式还原为 $(2r / 3R^2)$ ；如果 $r$ 位于球外，则 $R < r$ ，表达式变为 $(2R / 3r^2)$ 。注意到 $(\omega \times r) = -\omega r \sin \psi \hat{y}$ ，我们最后得到

$$
\begin{array}{r} {{A (r) = \left\{ \begin{array}{l l} {{\frac {\mu_ {0} R \sigma}{3} (\pmb {\omega} \times \pmb {r}),}} & {{\mathrm{球内的点}}} \\ {{\frac {\mu_ {0} R ^ {4} \dot {\sigma}}{3 r ^ {3}} (\pmb {\omega} \times \pmb {r}),}} & {{\mathrm{球外的点}}} \end{array} \right.}} \end{array}\tag{5.68}
$$

计算出积分式后，我再回到图5.45中的“自然”坐标系，其中 $\omega$ 转动轴与 $z$ 轴重合，点 $\pmb{r}$ 位于 $(r,\theta ,\varphi)$

$$
\boldsymbol {A} (r, \theta , \varphi) = \left\{ \begin{array}{l l} \frac {\mu_ {0} R \omega \sigma}{3} r \sin \theta \hat {\phi}, & r \leqslant R \\ \frac {\mu_ {0} R ^ {4} \omega \sigma}{3} \frac {\sin \theta}{r ^ {2}} \hat {\phi}, & r \geqslant R \end{array} \right.\tag{5.69}
$$

奇怪的是，这个球壳内的磁场是均匀的：

$$
\boldsymbol {B} = \nabla \times \boldsymbol {A} = \frac {2 \mu_ {0} R \omega \sigma}{3} \left(\cos \theta \hat {\boldsymbol {r}} - \sin \theta \hat {\boldsymbol {\theta}}\right) = \frac {2}{3} \mu_ {0} \sigma R \omega \hat {\boldsymbol {z}} = \frac {2}{3} \mu_ {0} \sigma R \omega\tag{5.70}
$$

例题5.12 求每单位长度有 $n$ 匝、半径为 $R$ 且通有电流 $I$ 的无限长螺线管内外的矢势。

[解答] 由于电流本身延伸到无限远处，这次我们不能利用式(5.66)。但这里有一个更漂亮的方法来求解。注意到

$$
\oint \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {l} = \int (\nabla \times \boldsymbol {A}) \cdot \mathrm{d} \boldsymbol {a} = \int \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {a} = \Phi\tag{5.71}
$$

其中 $\Phi$ 是通过所讨论环路的通量。这使我们想起安培定律的积分形式 [式 (5.57)],

$$
\oint \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {l} = \mu_ {0} I _ {\text { enc }}
$$

事实上，如果做替换， $B \rightarrow A, \mu_{0} I_{enc} \rightarrow \Phi$ ，它们是同一个方程。如果对称性允许，我们可以像在第5.3.3节中从 $I_{enc}$ 中得到 B 一样，从 $\Phi$ 中确定 A。目前的问题（螺线管内有均匀的纵向磁场 $\mu_{0} n I$ ，外部无磁场）类似于具有均匀分布电流的粗导线的安培定律情况。矢势是“环形”的（类似导线周围的磁场）；在螺线管内半径为 s 处，利用圆形的“安培环路”，我们有

$$
\oint \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {l} = A (2 \pi s) = \int \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {a} = \mu_ {0} n I (\pi s ^ {2})
$$

所以

$$
\boldsymbol {A} = \frac {\mu_ {0} n I}{2} s \hat {\phi}, \quad s <   R\tag{5.72}
$$

对于螺线管外的安培环路，通量为

$$
\int B \cdot \mathrm{d} a = \mu_ {0} n I (\pi s ^ {2})
$$

因为该场只延伸到 $R$ 处，所以

$$
\boldsymbol {A} = \frac {\mu_ {0} n I}{2} \frac {R ^ {2}}{s} \hat {\phi}, \quad s \geqslant R\tag{5.73}
$$

如果你对此答案有任何疑问，请验证， $\nabla \times \mathbf{A} = \mathbf{B}$ ？ $\nabla \cdot \mathbf{A} = 0$ ？如果成立，我们就是正确的。

通常，A 的方向类似电流的方向。例如，在例题 5.11 和 5.12 中，两者的方向都是方位角。的确，如果所有的电流都流向一个方向，那么式 (5.65) 表明 A 也必将指向这个方向。因此，有限长直导线段的矢势方向与电流方向一致（习题 5.23）。当然，如果电流延伸到无穷远处，首先就不能使用式 (5.65)（见习题 5.26 和 5.27）。此外，你总是可以对 A 添加一个任意常矢量——这类似于改变 V 的参考点，它不影响 A 的散度和旋度 [在式 (5.65) 中，我们选择了常数，使 A 在无限远处变为零]。原则上，你甚至可以选用一个散度不为零的矢势，在这种情况下，事情就应另当别论。尽管有这些警告，但基本要点不变：通常 A 的方向将与电流的方向匹配起来。

习题5.23 求载流为 $I$ 的有限长直线段的磁矢势。[取直导线段沿 $z$ 轴方向，从 $z_{1}$ 到 $z_{2}$ ，利用式(5.66)]验证你的答案是否与式(5.37)一致。

习题5.24 在柱坐标系中, 什么样的电流密度会产生矢势 $A = k\hat{\phi}$ (其中 $k$ 为常数)?

习题5.25 如果 $\pmb{B}$ 是均匀的，则证明 $A(r) = -\frac{1}{2} (r \times B)$ 成立。也就是说，验证 $\nabla \cdot A = 0, \nabla \times A = B$ 。该结果是唯一的吗，是否还有其他函数具有相同的散度和旋度？

习题5.26

(a) 通过你能想到的任何方法（除了查找），求距离载流为 $I$ 的无限长直导线 $\mathbf{s}$ 处的矢势，验证 $\nabla \cdot \mathbf{A} = 0$ 和 $\nabla \times \mathbf{A} = \mathbf{B}$ 。

(b) 若导线的半径为 R 且电流分布均匀，求导线内的磁矢势。

习题 5.27 求例题 5.8 中平面电流上下表面的矢势。

习题5.28

(a) 通过应用散度公式，验证式 (5.65) 与式 (5.63) 一致。

(b) 通过应用旋度公式，验证式 (5.65) 与式 (5.47) 一致。

(c) 应用拉普拉斯公式，验证式 (5.65) 和式 (5.64) 一致。

习题5.29 假设你想定义载流导线附近的磁标势U[式(5.67)]。首先，你必须远离导线本身（这里有 $\nabla \times B\neq 0$ ）；但这还不够。通过将安培定律应用于从某 $a$ 点开始环绕导线到 $\pmb{b}$ 点（图5.47），证明磁标势不能是单值的[即 $U(a)\neq U(b)$ ，即使它们代表相同的物理意义上的点]。作为一个例子，求无限长直导线的磁标势。（为了避免多值势的情况，你必须将自己限制在每条导线的一侧或另一侧的单连通区域，而没有环绕导线的闭合环路。）

![](images/c313f61b082256fb9a23ee3169bec7ff501f6ea2c8845d6591e39ae4460d2a71.jpg)  
图5.47

习题5.30 利用习题5.11的结果，求以恒定角速度 $\omega$ 旋转的固体球体内的磁场，该球体半径为 $R$ 具有均匀的电荷密度 $\rho$ 。

习题5.31

（a）完成第1.6.2节中定理2的证明。即证明任何散度为零的矢量场 $\pmb{F}$ 都可以表示成矢势 $\pmb{A}$ 的旋度。你所需要做的就是求出 $A_{x}, A_{y}, A_{z}$ 并满足：（i） $\partial A_{z} / \partial x - \partial A_{y} / \partial z = F_{x}$ ；（ii） $\partial A_{x} / \partial z - \partial A_{z} / \partial x = F_{y}$ ；（iii） $\partial A_{y} / \partial x - \partial A_{x} / \partial y = F_{z}$ 。以下是一种方法：选择 $A_{x} = 0$ ，求解（ii）和（iii）得到 $A_{y}$ 和 $A_{z}$ 。请注意，“积分常数”本身就是 $y$ 和 $z$ 的函数——它们仅相对于 $x$ 而言是常数。现在将这些表达式代入（i）中，并利用 $\nabla \cdot \pmb{F} = 0$ 的事实，可以得到

$$
A _ {y} = \int_ {0} ^ {x} F _ {z} (x ^ {\prime}, y, z) \mathrm{d} x ^ {\prime}; \quad A _ {z} = \int_ {0} ^ {y} F _ {x} (0, y ^ {\prime}, z) \mathrm{d} y ^ {\prime} - \int_ {0} ^ {x} F _ {y} (x ^ {\prime}, y, z) \mathrm{d} x ^ {\prime}
$$

(b) 通过直接求导，验证你在（a）部分中得到的 A 满足 $\nabla \times A = F$ 。A 的散度为零吗？[这是一个非常不对称的结构，如果真是这样的话，这将是很令人吃惊的——尽管我们知道存在一个旋度为 F 并且散度为零的矢量。]

(c) 作为一个例子，设 $F = y\hat{x} + z\hat{y} + x\hat{z}$ 。计算 $\mathbf{A}$ ，并证明 $\nabla \times \mathbf{A} = \mathbf{F}$ （进一步的讨论参阅习题5.53）。

## 5.4.2 边界条件

在第 2 章中，我绘制了一个三角图来总结静电学的三个基本量之间的关系：电荷密度 $\rho$ 、电场 E 和电势 V。对静磁学也可以绘制一个类似的三角图（图 5.48），能将电流密度 J、磁场 B 和矢势 A 联系起来。在图中缺失了一个“关系的关联”：B 表示出 A 的方程。你可能不需要这个公式，但如果你感兴趣，请参阅见习题 5.52 和 5.53。

![](images/cb056d400a3f168e4a5d880064df741907da9c07f9c06cd8272121c4748cd1e8.jpg)  
图5.48

正如电场在表面电荷存在处不连续一样，磁场在有表面电流处也是不连续的。只是现在是磁场的切线分量发生了变化。因为如果我们以积分形式将式(5.50)

$$
\oint \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {a} = 0
$$

应用到一个横跨表面扁盒子（图5.49），我们得到

$$
B _ {\mathrm{上方}} ^ {\perp} = B _ {\mathrm{下方}} ^ {\perp}\tag{5.74}
$$

对于切线分量，垂直于电流方向的安培环路（图 5.50）有

$$
\oint \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {l} = \big (B _ {\text {上方}} ^ {\parallel} - B _ {\text {下方}} ^ {\parallel} \big) l = \mu_ {0} I _ {\mathrm{enc}} = \mu_ {0} K l
$$

或者

$$
B _ {\mathrm{上方}} ^ {\parallel} - B _ {\mathrm{下方}} ^ {\parallel} = \mu_ {0} K\tag{5.75}
$$

因此 B 平行于表面且垂直于电流的分量是不连续的，变化量为 $\mu_{0}K$ 。对平行于电流方向的安培环路，平行于电流的分量是连续的。这些结果可以用一个公式来概括：

$$
\pmb {B} _ {\text {上方}} - \pmb {B} _ {\text {下方}} = \mu_ {0} (\pmb {K} \times \hat {\pmb {n}})\tag{5.76}
$$

其中 $\hat{n}$ 是垂直于表面指向 “上方” 的单位矢量。

![](images/2f5c47307a90f060a65eae786fb1aec87f6a4a9cdf643b5ed7889814f3e3b175.jpg)  
图5.49

![](images/f08a807f00ae9218b4ac974c2f7e013cb67a82ed3bf394ec4ef665f28288c597.jpg)  
图5.50

与静电学中的标势一样，磁矢势在任何边界上都是连续的：

$$
A _ {\text {上方}} = A _ {\text {下方}}\tag{5.77}
$$

因为 $\nabla \cdot \mathbf{A} = 0$ 保证了法向分量是连续的 $^{21}$ ，而 $\nabla \times \mathbf{A} = \mathbf{B}$ ，以

$$
\oint \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {l} = \int \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {a} = \varPhi
$$

的形式保证了切向分量的连续（通过厚度趋于零的安培环路中的通量为零）。但是 A 的散度继承了 B 的不连续性：

$$
\frac {\partial \pmb {A} _ {\mathrm{上方}}}{\partial n} - \frac {\partial \pmb {A} _ {\mathrm{下方}}}{\partial n} = - \mu_ {0} \pmb {K}\tag{5.78}
$$

习题5.32

(a) 用例题 5.9 中的分布情况验证式 (5.76)。

(b) 用例题 5.11 中的分布情况验证式 (5.77) 和式 (5.78)。

习题5.33 利用式(5.63)、式(5.76)和式(5.77)证明式(5.78)。[建议：我在曲面上建立了直角坐标系， $z$ 垂直于曲面， $x$ 平行于电流。]

## 5.4.3 矢势的多极展开

如果你想要得到一个局域电流分布在远处的矢势的有效近似公式，多极展开是很适合的。请记住：多极展开的思想就是将势写成 $1 / r$ 的幂级数形式，其中 $r$ 是到所讨论点的距离（图5.51）；如果 $r$ 足够大，级数中起主要贡献的是最低阶的非零项，而高阶项可以忽略。正如我们在第3.4.1节中所得到的那样[式(3.94)]，

$$
{\frac {1}{r}} = {\frac {1}{\sqrt {r ^ {2} + (r ^ {\prime}) ^ {2} - 2 r r ^ {\prime} \cos \alpha}}} = {\frac {1}{r}} \sum_ {n = 0} ^ {\infty} \left({\frac {r ^ {\prime}}{r}}\right) ^ {n} P _ {n} (\cos \alpha)\tag{5.79}
$$

其中 $\alpha$ 是 $r$ 和 $r'$ 之间的夹角。因此，电流环路的矢势可以写为

$$
\boldsymbol {A} (\boldsymbol {r}) = \frac {\mu_ {0} I}{4 \pi} \oint \frac {1}{r} \mathrm{d} \boldsymbol {l} ^ {\prime} = \frac {\mu_ {0} I}{4 \pi} \sum_ {n = 0} ^ {\infty} \frac {1}{r ^ {n + 1}} \oint \left(r ^ {\prime}\right) ^ {n} P _ {n} (\cos \alpha) \mathrm{d} \boldsymbol {l} ^ {\prime}\tag{5.80}
$$

或者更明确地为

$$
\boldsymbol {A} (\boldsymbol {r}) = \frac {\mu_ {0} I}{4 \pi} \left[ \frac {1}{r} \oint \mathrm{d} \boldsymbol {l ^ {\prime}} + \frac {1}{r ^ {2}} \oint r ^ {\prime} \cos \alpha \mathrm{d} \boldsymbol {l ^ {\prime}} + \frac {1}{r ^ {3}} \oint (r ^ {\prime}) ^ {2} \left(\frac {3}{2} \cos^ {2} \alpha - \frac {1}{2}\right) \mathrm{d} \boldsymbol {l ^ {\prime}} + \dots \right]\tag{5.81}
$$

与 V 的多极展开一样，我们称第一项（1/r 项）为单极项（monopole），第二项（ $1/r^{2}$ 项）为偶极项（dipole），第三项为四极项（quadrupole），依此类推。

![](images/89a1083ef45f510c52543d6fc952fcfa1c61a9c26756859a51398017aa1f430f.jpg)  
图5.51

现在，因为积分是沿闭合环路一周总的位移矢量，磁单极子始终为零：

$$
\oint \mathrm{d} l ^ {\prime} = 0\tag{5.82}
$$

这反映了自然界中不存在磁单极子的事实（麦克斯韦方程 $\nabla \cdot B = 0$ 中包含的一个假设，整个矢势理论都是基于该假设）。

在单极项没有贡献的情况下, 起主要作用是偶极项 (除非在极少数情况下, 它也为零):

$$
\boldsymbol {A} _ {\mathrm{dip}} (\boldsymbol {r}) = \frac {\mu_ {0} I}{4 \pi r ^ {2}} \oint r ^ {\prime} \cos \alpha \mathrm{d} l ^ {\prime} = \frac {\mu_ {0} I}{4 \pi r ^ {2}} \oint (\hat {\boldsymbol {r}} \cdot \boldsymbol {r} ^ {\prime}) \mathrm{d} l ^ {\prime}\tag{5.83}
$$

如果利用式 (1.108)，并令 $c = r$ ：我们可以把该积分写得更加简明，

$$
\oint \left(\hat {\boldsymbol {r}} \cdot \boldsymbol {r} ^ {\prime}\right) \mathrm{d} \boldsymbol {l} ^ {\prime} = - \hat {\boldsymbol {r}} \times \int \mathrm{d} \boldsymbol {a} ^ {\prime}\tag{5.84}
$$

则有

$$
\boxed {A _ {\mathrm{dip}} (\boldsymbol {r}) = \frac {\mu_ {0}}{4 \pi} \frac {\boldsymbol {m} \times \hat {\boldsymbol {r}}}{r ^ {2}}}\tag{5.85}
$$

其中 m 是磁偶极矩（magnetic dipole moment）:

$$
\boxed {m \equiv I \int \mathrm{d} a = I a}\tag{5.86}
$$

这里 a 是闭合环路的 “面积矢量”（见习题 1.62）；如果闭合环路是平的，a 就是环路所围的普通面积，其方向由右手规则确定（手指指向电流方向）。

例题5.13 求图5.52所示的“书挡形状”环路的磁偶极矩。图中所有边长都为 $w$ ，并通有电流 $I$ 。

![](images/95637e7557377a32938594989b288c79fa256685472fd3fc7500f400cd8a66a2.jpg)  
图5.52

[解答] 这个闭合环路可以看作两个平面上的正方形环的叠加（图 5.53），当把它们两个边放在一起时，“额外”边（AB）会相互抵消，因为通过的电流方向相反。总磁偶极矩为

$$
\boldsymbol {m} = I w ^ {2} \hat {\boldsymbol {y}} + I w ^ {2} \hat {\boldsymbol {z}}
$$

它的大小为 $\sqrt{2} Iw^2$ ，方向指向 $z = y$ 的 $45^{\circ}$ 角线。

![](images/e88358210aa35d60d576a996169dbc3e9b48476034bb1ab547bf33baa96852df.jpg)  
图5.53

从式 (5.86) 中可以清楚地看出磁偶极矩的大小与原点的选择无关。你们可能还记得，只有当总电荷为零时，电偶极矩的大小才与原点的选择无关 (第 3.4.3 节)。由于磁单极矩始终为零，因此磁偶极矩与原点的选择无关也就不足为奇了。

尽管在多极展开中偶极项起主导作用（除非 m=0），因此它提供了对真实势的一个很好的近似，但通常它不是严格的势；还有四极项、八极项和更高项的贡献。你可能会问，能否设计出一个电流分布，使它产生的势为“纯”偶极项——使式(5.85)成为精确的？好吧，也许可以，也许不可以：和电场的情况做类比，这是可以做到的，但模型有点难做。首先，你必须在原点取一个无穷小的环，但是，为了得到一定的偶极矩，你还不得不将电流调至无穷大，以使乘积 m=Ia 保持不变。在实际中，只要距离 r 远远超出闭合环路的大小，偶极势就是一个合理的近似。

如果我们令 m 位于原点，方向沿 z 轴方向（图 5.54），偶极矩的磁场就很容易计算。根据式 (5.85)，点 $(r, \theta, \varphi)$ 处的矢势为

$$
A _ {\mathrm{dip}} (\boldsymbol {r}) = \frac {\mu_ {0}}{4 \pi} \frac {m \sin \theta}{r ^ {2}} \hat {\phi}\tag{5.87}
$$

因此

$$
\pmb {B} _ {\mathrm{dip}} (\pmb {r}) = \nabla \times \pmb {A} = \frac {\mu_ {0} m}{4 \pi r ^ {3}} (2 \cos \theta \hat {\pmb {r}} + \sin \theta \hat {\pmb {\theta}})\tag{5.88}
$$

令人惊讶的是，这在结构上同电偶极子的场相同[式(3.103)]！（然而，仔细观察一下，物理上的磁偶极子的场——一个小电流环，与物理上的电偶极子的场——相距很近的正负电荷，看起来是场截然不同的。将图5.55与图3.37进行比较。）

![](images/5e208379c49dc32a43b8ad20c1a1212a0654d00bb45a667e4269893928a215ee.jpg)  
图5.54

![](images/358c94d443ffc59a6bd8f066e0fe9616af76d918eb4dd44ff192f6cbce6a5652.jpg)  
a) “纯”偶极子的场  
图5.55

![](images/d2be0ea4cd4151bb8fefdb23734ce90b5bc831144e5832fcb0ec398f5c891421.jpg)  
b) “物理” 偶极子的场

·习题 5.34 证明偶极子的磁场可以写成与自由坐标形式：

$$
\boxed {B _ {\mathrm{dip}} (\boldsymbol {r}) = \frac {\mu_ {0}}{4 \pi} \frac {1}{r ^ {3}} [ 3 (\boldsymbol {m} \cdot \hat {\boldsymbol {r}}) \hat {\boldsymbol {r}} - \boldsymbol {m} ]}\tag{5.89}
$$

习题5.35 半径为 $R$ 的圆形电线环位于 $xy$ 平面内（以原点为中心），沿正 $z$ 轴方向看，通有逆时针流动的电流 $I$ 。

(a) 它的磁偶极矩是多少?

(b) 远离原点位置处的磁场（近似）为多少？

(c) 证明，对于 $z$ 轴上的点，当 $z \gg R$ 时，你的答案与精确场一致（例题5.6）。

习题5.36 求边长为 $w$ 的方形环中心上方距离为 $z$ 处的磁场，环中通有电流 $I$ 。证明：当 $z \gg w$ 时，用偶极矩近似，它约化为具有适当偶极矩的偶极子场。

习题5.37

（a）半径为 $R$ 的留声机唱片，带有均匀的面电荷 $\sigma$ ，以恒定角速度 $\omega$ 旋转，求它的磁偶极矩。

（b）对例题5.11中的旋转球壳的磁偶极矩，证明对于点 $r > R$ ，它的矢势是理想偶极子的矢势。

习题5.38 我计算出了直线电流矢势的多极展开式，因为这是最常见的类型，在某些方面也是最容易处理的。对于体电流 $J$ ：

(a) 类似于式 (5.80)，写出多极展开式。

(b) 写出单极势，并证明它等于零。

(c) 利用式 (1.107) 和式 (5.86)，证明磁偶极矩可以写成

$$
\boldsymbol {m} = \frac {1}{2} \int (\boldsymbol {r} \times \boldsymbol {J}) \mathrm{d} \tau\tag{5.90}
$$

## 第5章补充习题

习题 5.39 分析质量为 m、带电荷量为 q 的粒子在通有稳定电流 I 的长直线磁场中的运动。

(a) 它的动能守恒吗?

(b) 电流 $I$ 沿 $z$ 轴，在柱坐标系中求作用在粒子上的力。

(c) 求出运动方程。

(d) 假设 $\dot{z}$ 是常数。描述运动情况。

习题 5.40 你可能已经想到，既然平行电流相互吸引，单根导线中的电流应该沿着中心轴线收缩成一条细小的电流束。然而在实际中，电流通常均匀地分布于导线中，你们怎么解释这件事？如果正电荷（密度 $\rho_{+}$ ）被“钉住”，负电荷（密度 $\rho_{-}$ ）以速度 v 运动（这些都与距离轴线的远近无关），则证明 $\rho_{-} = -\rho_{+}\gamma^{2}$ ，其中 $\gamma = 1/\sqrt{1 - (v/c)^{2}}$ ， $c^{2} = 1/\mu_{0}\varepsilon_{0}$ 。如果整条导线是电中性的，那么补偿电荷处在什么地方 $^{22}$ ？[请注意，对于通常的速度大小（见习题 5.19），两种电荷密度基本上不受电流的影响（因为 $\gamma \approx 1$ ）。然而，在等离子体中，正电荷也可自由运动，这种所谓的收缩效应是非常显著的。]

习题5.41 如图5.56所示，匀强磁场 $B$ 的方向指向纸面向外，矩形条状导电材料中通有向右流动的电流 $I$ 。

(a) 如果运动电荷是正的, 磁场将使它们向哪个方向偏转? 这种偏转将导致电荷在上下表面的积累, 进而反过来将产生电场力来抵消磁场力, 当两者完全抵消时, 将处于平衡状态。(这个现象称作霍尔效应, Hall effect。)

(b) 根据 B, v（电荷速度）以及导体相关尺寸 $^{23}$ ，求导体上下表面的电势差（霍尔电压，Hall voltage）。

（c）如果运动电荷为负，那么你的分析会有什么变化？[霍尔效应是检测材料中移动电荷载流子符号的典型方法。]

![](images/e567291367481e9f02aecb4fc93024d22bcffa317b622de8cf6e3fbd02edd01c.jpg)  
图5.56

习题 5.42 形状不规则的平面导线环的一部分位于均匀磁场 B 中（在图 5.57 中，磁场占据阴影区域，方向垂直于导线所在平面），导线通有电流 I。证明作用在导线上的总磁力为 F = IBw，其中 w 为弦宽。将此结果推广到磁场区域本身具有不规则形状的情况。力的方向朝哪里？

![](images/a984b411d1625b092ce4920775da03b88c2f918c8e55b8d4ba4b6e387459bd32.jpg)  
图5.57

习题5.43 一个垂直于纸面的圆形对称磁场（ $B$ 仅与到中心轴的距离有关）处在图5.58中阴影区域。如果总磁通量（ $\int B \cdot \mathrm{d}a$ ）为零，则证明从中心出发的带电粒子将沿径向从磁场边缘射出（前提是它能够逃逸）。反过来，沿相反的轨迹，一个从磁场外部进入中心的粒子将击中圆心（如果它有足够高的能量），尽管粒子可能走过一条弯曲的路径才能到达哪里。[提示：利用洛伦兹力定律计算粒子获得的总角动量。]

![](images/a4d7bb9a9bee084af01ba58e26f8145c8e8dffadeeebffcb24f816d94a2f53b0.jpg)  
图5.58

习题5.44 计算旋转带电球壳南北半球之间的磁吸引力（例题5.11）。[答案： $(\pi /4)\mu_0\sigma^2\omega^2 R^4 ]$

1 习题 5.45 考虑质量为 m、带电荷量为 $q_{e}$ 的粒子在（假想的）静止于原点处的磁单极 $q_{m}$ 所产生的磁场中运动：

$$
B = \frac {\mu_ {0}}{4 \pi} \frac {q _ {\mathrm{m}}}{r ^ {2}} \hat {r}
$$

(a) 求 $q_{e}$ 的加速度，并用 $qq_{m}, m, r$ （该粒子的位置）和 v （它的速度）表示。

(b) 证明速度 $v = |\pmb{v}|$ 是一个运动常量。

(c) 证明矢量

$$
Q \equiv m (\boldsymbol {r} \times \boldsymbol {v}) - \frac {\mu_ {0} q _ {\mathrm{e}} q _ {\mathrm{m}}}{4 \pi} \hat {\boldsymbol {r}}
$$

是一运动恒量。[提示：将它对时间进行求导，利用（a）中得到的运动方程证明导数为零。]

(d) 选择球坐标 $(r, \theta, \varphi)$ ，极轴（ $z$ ）沿 $Q$ 方向。

（i）计算 $Q \cdot \hat{\phi}$ ，证明 $\theta$ 是一运动恒量（所以 $q_{e}$ 在一个锥形表面运动——庞加莱在 1896 年首次发现这个问题 $^{24}$ ）；

(ii) 计算 $Q \cdot \hat{r}$ , 并证明 $Q$ 的大小为

$$
Q = \frac {\mu_ {0}}{4 \pi} \left| \frac {q _ {\mathrm{e}} q _ {\mathrm{m}}}{\cos \theta} \right|
$$

(iii) 计算 $Q \cdot \hat{\theta}$ ，证明

$$
\frac {\mathrm{d} \varphi}{\mathrm{d} t} = \frac {k}{r ^ {2}}
$$

并确定常数 $k$ 。

(e) 在球坐标中表示出 $v^2$ ，给出下列形式的轨迹方程：

$$
\frac {\mathrm{d} r}{\mathrm{d} \varphi} = f (r)
$$

[即确定函数 $f(r)]$ 。

(f) 求解 $r(\varphi)$ 的方程。

!习题 5.46 利用毕奥-萨伐尔定律 [最方便的形式是适用于表面电流的式 (5.42)]，求半径为 R、每单位长度有 n 匝的无限长螺线管内外的场，螺线管通有稳恒电流 I。

习题5.47 圆形电流环轴线上的磁场[式(5.41)]远非均匀（随着 $z$ 的增加，磁场急剧下降）。使用相距为 $d$ 的两个这样的圆环可以产生非常接近均匀的磁场（图5.59）。

![](images/bde6b8bb3732880f0a592e3466150b16d47e7c5d4e80cc7a9bd11e6ebe247057.jpg)  
图5.59

(a) 求作为 $z$ 函数的磁场 $\pmb{B}$ ，并证明在它们之间的中点处 $(z = 0)$ ， $\partial B / \partial z$ 为零。

(b) 如果你把 $d$ 选取得适当，在中点处 $B$ 的二阶导数也为零。这种装置就是亥姆霍兹线圈（Helmholtz coil），这是在实验室中产生相对均匀的磁场的一种方便方法。确定 $d$ 使中点处 $\partial^2 B / \partial z^2 = 0$ ，并求中心处的磁场（答案： $8\mu_0 I / 5\sqrt{5} R$ ）。

习题 5.48 利用式 (5.41) 求习题 5.37（a）中旋转圆盘中心轴上的磁场。证明如果 $z \gg R$ ，则偶极子场 [式 (5.88)] 和你在习题 5.37 中得到的偶极矩是一个很好的近似值。

习题 5.49 假设你想求不在圆环中心正上方的一点 r 处的磁场（例题 5.6）（图 5.60）。你可以选择坐标轴使 r 位于 yz 平面内的 $(0, y, z)$ 处。源点是 $(R \cos \phi', R \sin \phi', 0)$ ， $\phi'$ 从 0 变化到 $2\pi$ 。给出可以用来计算 $B_x, B_y, B_z$ 的积分式 $^{25}$ 并计算出 $B_x$ 。

![](images/b9190a0c12b55b70fcb654241480d2ef73752b91fda5b0d02179b774cb0910db.jpg)  
图5.60

习题 5.50 静磁学将 “源电流”（产生磁场的电流）和 “受体电流”（受到力的电流）处理得是如此非对称，以至于两个电流环路之间的磁力与牛顿第三定律不一致。从毕奥-萨伐尔定律 [式 (5.34)] 和洛伦兹力定律 [式 (5.16)] 出发，证明回路 1 作用在回路 2 上的磁力（图 5.61）可以写成

$$
\pmb {F} _ {2} = - \frac {\mu_ {0}}{4 \pi} I _ {1} I _ {2} \oint \oint \frac {\hat {\pmb {r}}}{r ^ {2}} \mathrm{d} l _ {1} \mathrm{d} l _ {2}\tag{5.91}
$$

在这种表达式中可以清晰看出 $F_{2} = -F_{1}$ ，因为当 1 和 2 的角色互换时， $\hat{z}$ 会改变方向。（你似乎得到一个“额外”的项，请注意 $dl_{2} \cdot \hat{z} = dl_{0}$ 。）

![](images/fdc82ebfcb36d8ad2c6b814f78fa990a8bda8cd8e7e6d6b888464892cd670a1a.jpg)  
图5.61

习题5.51 考虑一通有稳恒电流 $I$ 的平面导线环；我们要计算该平面上某点的磁场。不妨我们把该点作为原点（它可以在环内部或者环外）。在极坐标系中，导线的形状由特定的函数 $r(\theta)$ 给出（图5.62）。

(a) 证明磁场大小是 $^{26}$

$$
B = \frac {\mu_ {0} I}{4 \pi} \oint \frac {\mathrm{d} \theta}{r}\tag{5.92}
$$

[提示：从毕奥-萨伐尔定律出发；请注意 $\hat{\pmb{z}} = -\pmb{r}$ ，且 $\mathrm{d}\pmb{l} \times \pmb{r}$ 垂直于平面；证明 $|\mathrm{d}\pmb{l} \times \pmb{r}| = \mathrm{d}\pmb{l}\sin \phi = r\mathrm{d}\theta$ 。]

(b) 通过计算圆环中心的磁场来检验这个公式。

(c) “连锁螺旋”的定义如下：

$$
r (\theta) = \frac {a}{\sqrt {\theta}}, \quad 0 <   \theta \leqslant 2 \pi
$$

![](images/eda055b4b9e154954a612a97578a2381b09b66ef8a311c5f65b591d110501e69.jpg)  
图5.62

(对于某个常数 a)。绘图并沿 x 轴用一段直线完成闭环。原点处的磁场是多少？

(d) 对于以原点为焦点的圆锥曲线，

$$
r (\theta) = \frac {p}{1 + e \cos \theta}
$$

其中 $p$ 是半通径（ $y$ 是截距）， $e$ 是偏心率（ $e = 0$ 为圆， $0 < e < 1$ 为椭圆， $e = 1$ 为抛物线）。证明：无论偏心率是多少，场的大小为 $^{27}$

$$
B = \frac {\mu_ {0} I}{2 p}
$$

习题5.52

(a) 弥补图 5.48 中“缺失联系”的一种方法是利用 A 的定义方程式（即 $\nabla \cdot A = 0, \nabla \times A = B$ ）与 B 的麦克斯韦方程 $(\nabla \cdot B = 0, \nabla \times B = \mu_{0} J)$ 之间的类比。显然，A 与 B 和 B 与 $\mu_{0} J$ 具有完全相同的依赖方式（即毕奥-萨伐尔定律）。基于这一观察结果，写出用 B 来表示 A 的公式。

(b) (a) 中所得结果的电场类比是:

$$
V (\boldsymbol {r}) = - \frac {1}{4 \pi} \int \frac {\boldsymbol {E} (\boldsymbol {r} ^ {\prime}) \cdot \hat {\boldsymbol {r}}}{\nu^ {2}} \mathrm{d} \tau^ {\prime}
$$

通过适当的类比将其推导出来。

！习题5.53 填补图5.48中“缺失联系”的另一种去方法是找出一个与式(2.21)相应的静磁学相似式，最明显的候选是

$$
\boldsymbol {A} (\boldsymbol {r}) = \int_ {\mathcal {O}} ^ {r} (\boldsymbol {B} \times \mathrm{d} \boldsymbol {l})
$$

(a) 对于均匀磁场 $B$ 这种最简单的情况来验证这个公式（以原点作为参考点 $O$ ）。该结果是否与习题5.25一致？你可以通过在公式前引入因子1/2来解决这个问题，但这个方程的缺陷会更加明显。

(b) 通过对图5.63所示的矩形环路计算 $\oint (B\times \mathrm{d}l)$ ，证明 $\int (B\times \mathrm{d}l)$ 与路径有关。就我所知28，沿着这些路经，最好的办法就是求解下面一对方程：

(i) $V(\pmb {r}) = -\pmb {r}\cdot \int_{0}^{1}\pmb {E}(\lambda \pmb {r})\mathrm{d}\lambda$

(ii) $\boldsymbol{A}(\boldsymbol{r}) = -\boldsymbol{r} \times \int_{0}^{1} \lambda \boldsymbol{B}(\lambda \boldsymbol{r}) \, \mathrm{d}\lambda$

[式（i）相当于在式(2.21)中的积分选择了径向路径，式（ii）构造了习题5.31中更加“对称”的解。)

(c) 利用式（ii）求均匀磁场 B 的矢势。

(d) 利用式（ii）求载有稳恒电流为 $I$ 的无限长直导线的矢势。式（ii）是否自动满足 $\nabla \cdot \dot{\pmb{A}} = 0?$ [答案： $(\mu_0 I / 2\pi s)(z\hat{s} - s\hat{z})]$

![](images/41456754f2223a11a5793d7f7fbd9f4999eee3b098988c1200e6ede04f12d779.jpg)  
图5.63

习题5.54

(a) 构造“纯”磁偶极子 m 的标势 $U(r)$ 。

(b) 构造旋转球壳的标势（例题 5.11）。[提示：通过比较式 (5.69) 和式 (5.87) 可以看出，对于 $r > R$ 的情况，它是个“纯”的磁偶极子的场。]

(c) 尝试着对实心旋转球体内部做同样问题的探讨。[提示：如果你已经解答了习题5.30，你就已经知道了场；令其等于 $-\nabla U$ ，并求解 $U$ ，有什么问题吗？]

习题5.55 正如 $\nabla \cdot B = 0$ 可使我们将 $B$ 表示为矢势的旋度 $(B = \nabla \times A)$ 一样，因此 $\nabla \cdot A = 0$ 可使我们将 $A$ 本身表示为“更高”势的旋度： $A = \nabla \times W$ （该层次结构可以无限拓展）。

(a) 求 W 的通式（作为对 B 的积分），且当在无穷远处 $B \rightarrow 0$ 时它也成立。

(b) 求匀强磁场 B 情况下的 W。[提示：参阅习题 5.25。]

(c) 求无限长直螺线管内外的 W。[提示：参阅习题 5.12。]

习题5.56 证明下面的唯一性定理：如果电流密度 $J$ 在整个体积 $V$ 上是给定的，并且电势 $\mathbf{A}$ 或磁场 $B$ 在 $\mathcal{V}$ 的边界表面 $S$ 上也是给定的话，则在整个体积 $\mathcal{V}$ 中磁场本身被唯一地确定。[提示：首先，利用散度定理证明

$$
\int \left\{\left(\nabla \times \boldsymbol {U}\right) \cdot (\nabla \times \boldsymbol {V}) - \boldsymbol {U} \cdot [ \nabla \times (\nabla \times \boldsymbol {V}) ] \right\} \mathrm{d} \tau = \oint [ \boldsymbol {U} \times (\nabla \times \boldsymbol {V}) ] \cdot \mathrm{d} \boldsymbol {a}
$$

对任意的矢量函数 U 和 V 成立]

习题5.57 磁偶极子 $m = -m_0\hat{z}$ 位于原点，处于均匀磁场 $B = B_0\hat{z}$ 中。证明：存在一个以原点为中心且没有磁场线穿过的球面。求该球面的半径，并绘出球内和球外的磁场线。

习题 5.58 如图 5.64 所示，一带电荷 Q 和质量 M 的薄均匀圆环绕其轴线旋转。

(a) 求磁偶极矩与其角动量的比值，这被称为旋磁比（gyromagnetic ratio）（或者磁力比，magnetomechanical ratio）。

（b）均匀旋转球体的旋磁比是多少？[这不需要新的计算；仅需将球体分解为无限多的小环，并应用（a）中的结果。]

(c) 根据量子力学，电子的自旋角动量为 $\frac{1}{2}\hbar$ ，其中 $\hbar$ 为普朗克常量。那么，电子的磁偶极矩是多少？以 $\mathrm{A} \cdot \mathrm{m}^2$ 为单位。[这个半经典值比实际值几乎小了 2 倍；狄拉克的相对论电子理论正确地得到了因子 2，费曼、施温格和朝永振一郎后来计算出更进一步的修正。确定电子的磁偶极矩仍然是量子电动力学中的最新成就，并且可能是所有的物理学领域中理论和实验之间最令人惊奇的一致的结果。顺便说一句，物理量 $(e\hbar / 2m)$ 被称为玻尔磁子（Bohr magneton），其中 $e$ 为电子的电荷， $m$ 是它的质量。]

![](images/cdbb3f00bb23150cb9980abe5bf142b338057e5fa5ec6fe1b21c8aea60237fbf.jpg)  
图5.64

## 习题5.59

(a) 证明：由于球体内的稳定电流，半径为 $R$ 的球体上的平均磁场是

$$
B _ {\mathrm{ave}} = \frac {\mu_ {0}}{4 \pi} \frac {2 m}{R ^ {3}}\tag{5.93}
$$

其中 $m$ 为球体的总磁偶极矩。与静电学的结果式 (3.105) 做对比。[这很难，所以我给你开个头：

$$
B _ {\mathrm{ave}} = \frac {1}{\frac {4}{3} \pi R ^ {3}} \int B \mathrm{d} \tau
$$

用 $\nabla \times A$ 来表示 $B$ 并应用习题1.61(b)。现在代入式(5.65)，先进行表面积分，证明：

$$
\int \frac {1}{2} \mathrm{d} a = \frac {4}{3} \pi r ^ {\prime}
$$

(见图 5.65)，如果你喜欢，可以利用式 (5.90)。]

（b）证明由球外恒定电流产生的平均磁场与它们在中心产生的磁场相同。

![](images/7067d8d4b43156c93b7d97571d10c3fbeb9566dce400ba08a1a6d52e33f038d5.jpg)  
图5.65

习题 5.60 半径为 R 的均匀带电实心球携带有总电荷量 Q，并以角速度 $\omega$ 绕 z 轴旋转。

(a) 球的磁偶极矩是多少?

(b) 求球体内部的平均磁场（参见习题 5.59）。

(c) 对 $r \gg R$ 的情况，求点 $(r, \theta)$ 处的近似矢势。

(d) 求球体外点 $(r, \theta)$ 处的精确矢势，并验证它与（c）中的结果一致。[提示：参考例题5.11。]

(e) 求球内点 $(r, \theta)$ 处的磁场（习题5.30），并验证它与（b）中的结果一致。

习题 5.61 利用式 (5.88)，计算偶极子在以原点为中心、半径为 R 的球上的平均磁场。先做角积分。将你的答案与习题 5.59 中的一般定理进行比较，解释差异，并指出如何修正式 (5.89) 以解决在 r = 0 处的歧义。（如果你被卡住了，请参考习题 3.48。）

显然，磁偶极子的真实磁场为 $^{29}$

$$
B _ {\mathrm{dip}} (\boldsymbol {r}) = \frac {\mu_ {0}}{4 \pi} \frac {1}{r ^ {3}} \left[ 3 \left(\boldsymbol {m} \cdot \hat {\boldsymbol {r}}\right) \cdot \hat {\boldsymbol {r}} - \boldsymbol {m} \right] + \frac {2 \mu_ {0}}{3} \boldsymbol {m} \delta^ {3} (\boldsymbol {r})\tag{5.94}
$$

与静电学中类似式 (3.106) 做。

习题5.62如图5.66所示，半径为 $R$ 、长度为 $L$ 的细玻璃棒分布有均匀的表面电荷 $\sigma$ ，并以角速度 $\omega$ 绕其轴线旋转。在 $xy$ 平面内，求距离轴线为 $s\gg R$ 处的磁场。[提示：将其视作一系列偶极子。][答案： $\mu_0\omega \sigma LR^3 /4[s^2 +(L / 2)^2 ]^{3 / 2}]$

![](images/1aaa6eec2769ff71d4b238b1c5e8d57ba54d359000c8185e47f65b3e8cd1cb1d.jpg)  
图5.66

## 第6章 介质中的磁场

## 6.1 磁化

## 6.1.1 抗磁体、顺磁体和铁磁体

如果你问普通人什么是“磁性”，你可能会被告知冰箱贴、指南针和地球北极等——这些与运动电荷或者载流导线都没有任何明显的联系。然而，所有磁现象都是由运动中的电荷所引起的。事实上，如果你能够在原子尺度上观察一块磁性材料，你会发现其中存在微小的电流：围绕原子核旋转的电子和电子的自旋。从宏观角度来看，这些电流环非常小，我们可以将其视为磁偶极子。通常，由于原子的随机取向，它们会相互抵消。但是，当施加外磁场后，这些磁偶极子会出现有序的排列，介质会变为磁极化或磁化（magnetized）。

与电极化不同（电极化方向总是与外场 E 方向相同），磁极化中有些物质的磁化方向与外场 B 的方向平行（顺磁体，paramagnets），有些物质则与外场 B 的方向相反（抗磁体，diamagnets）。个别物质（称为铁磁体，ferromagnets；如铁，与最常见的例子不同）即使在外磁场撤去之后仍然保持其磁化状态——对于这些物质来说，磁化不是由当前的外加磁场决定的，而是由物体的整个磁化“历史”决定的。由铁制成的永磁体是铁磁性最熟悉的例子；但从理论角度来看，它们是最复杂的。我先从顺磁体和抗磁体的定性模型开始，将把铁磁体的讨论留在本章的最后。

## 6.1.2 磁偶极矩上的力和力矩

像电偶极子在电场中受到力矩作用一样，磁偶极子在磁场中也受到力矩作用。让我们来计算匀强磁场中矩形电流环上受到的力矩。（如图6.1所示，由于任何电流环都可以看成由无穷多个小的矩形组成，其所有“内部”边的电流相互抵消；因此，这里的讨论并不失一般性；但如果你更喜欢从随意画的一个任意形状开始，请参阅习题6.2。）将矩形的中心置于原点，并将其从 $z$ 轴向 $y$ 轴倾斜角度 $\theta$ （图6.2）。令 $B$ 沿着 $z$ 轴方向。倾斜边上受到的两个力相互抵消（它们倾向于拉伸矩形环，但不会使其旋转）。施加在水平边上的两个力大小相等且方向反向（因此矩形环上的合力为零），但它们确实会产生一个力矩：

$$
\mathbf {N} = a F \sin \theta \hat {\mathbf {x}}
$$

![](images/c445d703b8addc2a372fe36faa95cfe9477f6787bf9c5927ef03204336af9185.jpg)  
图6.1

![](images/7a44812eb38769692babcd818fd0e3d1b20ed4f7b7d1db362c06d7474d9549cc.jpg)

![](images/d66d6f51ab0601bd6131a093ca2b0b4e54f3a006134107b8846a833b9957df88.jpg)  
b)  
图6.2

每个边上力的大小是

$$
F = I b B
$$

因此

$$
\mathbf {N} = I a b B \sin \theta \hat {\mathbf {x}} = m B \sin \theta \hat {\mathbf {x}}
$$

或者

$$
\boxed {N = m \times B}\tag{6.1}
$$

其中 $m = Iab$ 是环路的磁偶极矩。式 (6.1) 给出了在匀强磁场情况下任意局域电流分布所受的力矩大小；在非匀强磁场中，该式是一无限小理想磁偶极子的力矩的严格表达式（围绕磁偶极子中心）。

请注意，式(6.1)在形式上同电学中的 $N = p \times E$ [式(4.4)]类似。特别是，力矩依然是使偶极子沿平行于磁场的方向排列。正是这种力矩导致了顺磁性（paramagnetism）。由于每个电子都构成一个磁偶极子（如果你愿意的话，可以把它想象为一个微小的旋转带电球体），所以你可能会认为顺磁性是一种普遍现象。实际上，量子力学（特别是泡利不相容原理）往往是要求给定原子中的电子以相反的自旋成对锁定在一起 $^{1}$ ，这样就大大地降低了总体上的力矩。因此，顺磁效应通常发生在具有奇数个电子的原子或者分子中，其中“多余”的未配对电子会受到磁力矩的影响。即使是这样，由于随机的热碰撞往往会导致无序作用，磁偶极子的完全定向排列远未实现。

在匀强磁场中，闭合环路受到的合力为零：

$$
\boldsymbol {F} = I \oint (\mathrm{d} \boldsymbol {l} \times \boldsymbol {B}) = I \left(\oint \mathrm{d} \boldsymbol {l}\right) \times \boldsymbol {B} = \mathbf {0}
$$

常数 B 移至积分符号外面，并且环绕闭合环路的总位移 $\oint dl$ 为零。在非匀强磁场中，情况并非如此。例如，假设半径为 R、通有电流大小为 I 的圆环形导线悬挂在一短螺线管“边缘”区域的上方（图 6.3）。这里磁场 B 存在一个径向分量，所以圆环受到一个向下的合力（图 6.4）：

$$
F = 2 \pi I R B \cos \theta\tag{6.2}
$$

对于处在磁场 B 中磁偶极矩为 m 的无穷小环，受力为

$$
\boxed {\boldsymbol {F} = \nabla (\boldsymbol {m} \cdot \boldsymbol {B})}\tag{6.3}
$$

(参阅习题 6.4)。如果我们将后者写成 $F = \nabla(\boldsymbol{p} \cdot \boldsymbol{E})$ ，那么磁学公式再次与其电学的“孪生”公式一模一样。[参阅式 (4.5) 的脚注。]

![](images/299d74809e2cebc168738643e3f88dc0e12f3ffd2dd75a083a7007d7d9e6e7ac.jpg)  
图6.3

![](images/698c6cc64c43ff663414429f12de141c4e4546ca84f40a88aa2097b16fbc4eca.jpg)  
图6.4

如果一开始你就有一种似曾相识的感觉，也许会更加敬佩那些早期物理学家们；他们认为，如同电偶极子一样（图6.5a），磁偶极子是由相隔很小的正负磁“电荷”（他们称之为北极和南极）组成。他们写出了这些磁单极子之间吸引和排斥作用的“库仑定律”，并且发展了与静电学完全类似的整个静磁学。从多个角度来看，这是一个不错的模型——它正确地给出了磁偶极子产生的磁场（至少远离原点时），作用在磁偶极子上的力矩（至少是在偶极子静止时）和作用在偶极子上的外力（至少在没有外电流的情况下）。但这是不正确的，因为并不存在单一的磁北极或者磁南极。如果你把一块条形磁铁摔成两半，你并不会在一只手中拿到北极，而另一只手中拿到南极；你得到的是两个完整的磁铁。磁现象不是归因于磁单极子，而是源于运动的电荷；磁偶极子是微小的环电流（如图6.5c）；至于 $m$ 的公式与 $\pmb{p}$ 的相应公式的任何相似之处，这都是一件非同寻常的事情。有些时候，按照磁偶极子的“吉尔波特（Gilbert）模型”（分离的磁单极子）要比按照物理上正确的“安培模型”（环形电流）来思考更为简单明了。事实上，这种图像有时候确会提供一个快速而巧妙的解决方法来处理烦琐的问题（你只需简单复制静电学的相应结论，将 $p$ 变为 $m$ ，将 $1 / \varepsilon_0$ 变为 $\mu_0$ ，将 $E$ 变为 $B$ ）。但当磁偶极子近距离的特征起作用时，这两种模型就会给出截然不同的答案。换句话说，我的建议是你可以使用吉尔波特模型来对问题获得一个直观的“感觉”，但永远不要依赖它来获得定量结果。

![](images/04794897651dfeee2d17c35abc4a7884f9455351928ce65f28cf9a7c9d83870f.jpg)  
图6.5

习题6.1 如图6.6所示，计算圆形环路施加在正方形环路上的力矩（假设 $r$ 远大于 $a$ 或 $b$ ）。如果正方形环路可以自由转动，平衡时它的方向指向何处？

![](images/ec592575e501ecdc1c946ffc08c9971fb68e9ca90e972c6666616cfab4651032.jpg)  
图6.6

习题 6.2 从式 (5.16) 形式的洛伦兹力定律出发，证明在匀强磁场 B 中任何稳恒电流分布的环路上（不仅仅是方形环路）所受力矩为 $m \times B$ 。

习题6.3 如图6.7所示，求相距为 $r$ 的两个磁偶极子 $m_{1}$ 和 $m_{2}$ 之间的吸引力：（a）利用式(6.2)，（b）利用式(6.3)。

![](images/7668bcd280a8126253fe7cd3fd654fd2f83870ffb367ec48e09dc1ea6a97f682.jpg)  
图6.7

习题6.4 推导式(6.3)。[这里给出一种方法：假设磁偶极子是一个边长为 $\varepsilon$ 的无穷小正方形（如果不是，将其切成正方形，并且将以下论证应用于每个正方形）。选择如图6.8所示的坐标轴，并且沿其四条边计算 $F = I\int (\mathrm{d}\pmb {l}\times \pmb{B})$ 。将等式右侧中的 $\pmb{B}$ 展开为泰勒级数，例如，

$$
\boldsymbol {B} = \boldsymbol {B} (0, \varepsilon , z) \cong \boldsymbol {B} (0, 0, z) + \varepsilon \left. \frac {\partial \boldsymbol {B}}{\partial y} \right| _ {(0, 0, z)}
$$

更为复杂的方法，参阅习题6.22。]

![](images/1bc46bc90c5303b99ac21cfdcd60486155429e87837f709d4c49f9854e3893fa.jpg)  
图6.8

习题6.5 均匀电流 $J = J_0\hat{z}$ 流过横跨 $yz$ 平面的平板，从 $x = -a$ 到 $x = a$ 。磁偶极子 $m = m_0\hat{x}$ 位于原点。

(a) 利用式 (6.3) 求偶极子的受力。

（b）对沿 $y$ 轴方向的偶极子 $\pmb {m} = m_0\hat{\pmb{y}}$ ，做同样的运算。

(c) 在静电学情况下，表达式 $F = \nabla(p \cdot E)$ 与 $F = (p \cdot \nabla)E$ 是等价的（证明它）；但静磁学中的类比表达式的情况并非如此（解释原因）。例如，计算（a），（b）两种情况下的 $(m \cdot \nabla)B$ 值。

## 6.1.3 磁场对原子轨道的影响

电子不仅有自旋；它们也围绕原子核旋转——为简单起见，假设它的轨道是一半径为 $R$ 的圆（图6.9）。尽管从原则上讲，这种轨道运动并不能形成稳恒电流，但实际上它的运动周期 $T = 2\pi R / v$ 非常短，除非你眨眼极快，否则它看起来就像稳恒电流：

$$
I = - \frac {e}{T} = - \frac {e v}{2 \pi R}
$$

（负号表示电子是负电荷）因此，轨道磁偶极矩 $(I\pi R^{2})$ 为

$$
\boldsymbol {m} = - \frac {1}{2} e v R \hat {\boldsymbol {z}}\tag{6.4}
$$

与任何其他磁偶极子一样，当原子处于磁场中时，这个偶极子会受到力矩 $m \times B$ 的影响。但是，倾斜整个轨道要比倾斜自旋困难得多，因此轨道对顺磁性的贡献很小。然而，磁场对轨道运动却有更显著的影响：电子的加速或减速，具体由 B 的方向而定。因为在通常情况下，向心加速度 $v^{2}/R$ 是由电场力提供的 $^{2}$ ，

$$
\frac {1}{4 \pi \varepsilon_ {0}} \frac {e ^ {2}}{R ^ {2}} = m _ {\mathrm{e}} \frac {v ^ {2}}{R}\tag{6.5}
$$

在磁场存在的情况下，多出一个额外的力 $-e(\boldsymbol{v} \times \boldsymbol{B})$ 。为了便于论证，假设 B 垂直于轨道平面，如图 6.10 所示，则

$$
\frac {1}{4 \pi \varepsilon_ {0}} \frac {e ^ {2}}{R ^ {2}} + e \bar {v} B = m _ {\mathrm{e}} \frac {\bar {v} ^ {2}}{R}\tag{6.6}
$$

在这样的情况下，新的速度 $\bar{v}$ 大于 v:

$$
e \bar {v} B = \frac {m _ {\mathrm{e}}}{R} (\bar {v} ^ {2} - v ^ {2}) = \frac {m _ {\mathrm{e}}}{R} (\bar {v} + v) (\bar {v} - v)
$$

或者，假定速度变化 $\Delta v = \bar{v} - v$ 很小，

$$
\Delta v = \frac {e R B}{2 m _ {\mathrm{e}}}\tag{6.7}
$$

当加上磁场 B 时，则电子就会加速 $^{3}$ 。

![](images/995359ed8d74ebe0df29dc50693fb1e9bb0f02efc13e0f008dc7cd38eb1d90da.jpg)  
图6.9

![](images/4b5403aa4d2b5c762ed8d42b0a941e49e7504f021c3e2439c67896679ebc7bd3.jpg)  
图6.10

轨道速度的变化意味着磁偶极矩的变化 [式 (6.4)]:

$$
\Delta \pmb {m} = - \frac {1}{2} e (\Delta v) R \hat {\pmb {z}} = - \frac {e ^ {2} R ^ {2}}{4 m _ {\mathrm{e}}} \pmb {B}\tag{6.8}
$$

请注意， $m$ 的变化与 $B$ 的方向相反。（以另外一种方式旋转的电子会有一个向上的偶极矩，但是沿这种轨道运动的电子会被磁场减速，所以变化仍然与 $B$ 方向相反。）通常，电子轨道是随机取向的，则轨道偶极矩相互抵消掉。但在磁场存在的情况下，每个原子都会获得一点“额外”的磁偶极矩，这些增量都与磁场反平行。这就是抗磁性（diamagnetism）的机制。这是一种普遍现象，它影响着所有原子。不过，通常抗磁性要比顺磁性弱得多，所以抗磁性通常只能在没有顺磁性的情况下，在具有偶数个电子的原子中观察到。

在推导式(6.8)时，我假设轨道一直保持圆形，并保持其原始半径 $R$ 不变。在现阶段，我无法对此提供理由。如果当加上磁场时原子是静止的，那么我的假设就可以被证明——然而，在这种情况下这不是静磁学，所以具体的细节不得不等到第7章时才能给出（参阅习题7.52）。如果原子被移至磁场中，情况会变得更加复杂。但没有关系——我只是想给你关于一个抗磁性的定性描述。如果你愿意的话，假设在轨道半径变化的情况下速度保持不变——公式(6.8)将被修改（多出一个因子2），但定性结论不受影响。事实是这个经典模型从根本上是有缺陷的（抗磁性其实是一种量子现象），所以没有必要去细化更多的细节。在反磁性材料中，真正重要的是感应偶极矩指向与磁场方向相反这一经验事实。

## 6.1.4 磁化强度

在磁场存在的情况下，物质会被磁化；也就是说，通过显微镜观察，你会发现它包含许多微小的偶极子，这些偶极子沿某个方向呈网状排列。我们已经讨论了解释这种磁化的两种机制：（1）顺磁性（与未配对电子自旋相关的偶极子受到一个迫使它们沿外磁场平行的方向排列的力矩）和（2）抗磁性（电子的轨道运动速度发生变化，从而改变了轨道偶极矩，使其方向与外磁场方向相反）。无论是什么原因，我们都用矢量来描述磁化状态

$$
M \equiv \text { 单位体积内的磁偶极矩 }\tag{6.9}
$$

M 称为磁化强度（magnetization）；它与静电学中的电极化强度 P 起着类似的作用。在下一节中，我们将不再考虑磁化是如何形成的——它可以是顺磁性、抗磁性，甚至是铁磁性——我们将把 M 取作一个已知量，来计算这种磁化本身所产生的磁场。

顺便说一句，你可能会惊讶地发现，除了著名的铁磁三元素（铁、镍和钴）之外，其他物质都会受到磁场的影响。当然，你不可能用磁铁吸起一块木头或者铝块。原因是它们的抗磁性和顺磁性都非常弱：需要一个精细的实验和一个强大磁铁才能探测到它们。如图6.3所示，如果你将一块顺磁材料悬挂在螺线管上方，感应磁化强度将向上，因此材料会受到向下的力。相比之下，抗磁材料的磁化强度方向是向下的，受力是向上的。一般来讲，当样品放置在非匀强磁场区域时，顺磁体会被吸引到磁场中，而抗磁体会被排斥出去。但实际的力却非常小——在典型的实验配置中，类似铁样品所受到力将是其大小的 $10^{4}$ 或者 $10^{5}$ 倍之多。这就是我们在第5章中计算一根铜线内部磁场时不考虑磁化影响的原因5。

习题 6.6 在以下材料中，你认为哪些是顺磁性的，哪些是抗磁性的：铝，铜，氯化铜（ $CuCl_{2}$ ），碳，铅，氮气（ $N_{2}$ ），食盐（NaCl），钠，硫，水？（实际上，铜具有微弱的抗磁性；否则，它们都是你所期望的。）

## 6.2 磁化介质的场

## 6.2.1 束缚电流

假设我们有一块磁化材料，其单位体积的磁偶极矩 $M$ 已知。该材料产生的磁场是多少？单个磁偶极子 $\pmb{m}$ 的矢势由式(5.85)给出：

$$
A (r) = \frac {\mu_ {0}}{4 \pi} \frac {m \times \hat {z}}{r ^ {2}}\tag{6.10}
$$

在磁介质中，每个体积元 $\mathrm{d}\tau^{\prime}$ 具有的磁偶极矩是 $M\mathrm{d}\tau^{\prime}$ ，因此总矢势为（图6.11）

$$
A (\boldsymbol {r}) = \frac {\mu_ {0}}{4 \pi} \int \frac {M (\boldsymbol {r} ^ {\prime}) \times \hat {\boldsymbol {r}}}{\nu^ {2}} \mathrm{d} \tau^ {\prime}\tag{6.11}
$$

![](images/5f21bfdbfd2fd59bd7363d8d4cb671a0c924c5bec4408e3a96f4437bdf115045.jpg)  
图6.11

原则上就是这样。但是，与静电学中的情形一样（第4.2.1节），通过利用恒等式可以将这个积分转化为更具启发性的形式：

$$
\nabla^ {\prime} \frac {1}{r} = \frac {\hat {r}}{r ^ {2}}
$$

有了上式，

$$
\boldsymbol {A} (\boldsymbol {r}) = \frac {\mu_ {0}}{4 \pi} \int \left[ \boldsymbol {M} \left(\boldsymbol {r} ^ {\prime}\right) \times \left(\nabla^ {\prime} \frac {1}{2}\right) \right] \mathrm{d} \tau^ {\prime}
$$

利用矢量积法则 7，并对上式进行分部积分有

$$
\boldsymbol {A} (\boldsymbol {r}) = \frac {\mu_ {0}}{4 \pi} \left\{\int \frac {1}{2} [ \nabla^ {\prime} \times \boldsymbol {M} (\boldsymbol {r} ^ {\prime}) ] \mathrm{d} \tau^ {\prime} - \int \nabla^ {\prime} \times \left[ \frac {\boldsymbol {M} (\boldsymbol {r} ^ {\prime})}{2} \right] \mathrm{d} \tau^ {\prime} \right\}
$$

习题1.61（b）要求我们将后者表示为曲面积分

$$
\boldsymbol {A} (\boldsymbol {r}) = \frac {\mu_ {0}}{4 \pi} \int \frac {1}{2} [ \nabla^ {\prime} \times \boldsymbol {M} (\boldsymbol {r} ^ {\prime}) ] \mathrm{d} \tau^ {\prime} + \frac {\mu_ {0}}{4 \pi} \oint \frac {1}{2} [ \boldsymbol {M} (\boldsymbol {r} ^ {\prime}) \times \mathrm{d} \boldsymbol {a} ^ {\prime} ]\tag{6.12}
$$

第一项看起来就像是体电流的矢势，

$$
\boxed {J _ {\mathrm{b}} = \nabla \times M}\tag{6.13}
$$

而第二项看起来像是面电流的矢势，

$$
\boxed {K _ {\mathrm{b}} = M \times \hat {n}}\tag{6.14}
$$

其中 $\hat{n}$ 是法向单位矢量。根据这些定义，

$$
\boldsymbol {A} (\boldsymbol {r}) = \frac {\mu_ {0}}{4 \pi} \int_ {\mathcal {V}} \frac {\boldsymbol {J} _ {\mathrm{b}} \left(\boldsymbol {r} ^ {\prime}\right)}{\nu} \mathrm{d} \tau^ {\prime} + \frac {\mu_ {0}}{4 \pi} \oint_ {\mathcal {S}} \frac {\boldsymbol {K} _ {\mathrm{b}} \left(\boldsymbol {r} ^ {\prime}\right)}{\nu} \mathrm{d} a ^ {\prime}\tag{6.15}
$$

这意味着磁化物体的矢势（以及磁场）与整个物体中的体电流 $J_{b} = \nabla \times M$ 和边界上的表面电流 $K_{\mathrm{b}} = M \times \hat{n}$ 共同产生的矢势是相同的。我们不使用式(6.11)来求所有无穷小偶极子的贡献，而是首先确定束缚电流（bound currents），然后求出它们产生的磁场，就像我们计算任意的体电流和面电流产生的磁场一样。注意与电学情况中的惊人一致：极化物体的电场与体束缚电荷 $\rho_{\mathrm{b}} = -\nabla \cdot P$ 加上表面束缚电荷 $\sigma_{\mathrm{b}} = P \cdot \hat{n}$ 产生的相同。

## 例题6.1 求出均匀磁化球体的磁场。

## [解答] 选择 $z$ 轴沿 $M$ 的方向（图6.12），我们有

$$
J _ {\mathrm{b}} = \nabla \times M = 0, \quad K _ {\mathrm{b}} = M \times \hat {n} = M \sin \theta \hat {\phi}
$$

![](images/884c271d6cec7943ff878a10cc920d112f2f9beb6586bc460790cf10b498ea42.jpg)  
图6.12

现在，具有均匀表面电荷 $\sigma$ 的旋转球壳对当于表面电流密度

$$
\pmb {K} = \sigma \pmb {v} = \sigma \omega R \sin \theta \hat {\phi}
$$

因此，只要 $\sigma \omega R \to M$ ，我们可以得出均匀磁化球体的磁场与旋转带电球壳产生的磁场相同。回到例题5.11，可推断出球内的磁场为

$$
\boldsymbol {B} = \frac {2}{3} \mu_ {0} \boldsymbol {M}\tag{6.16}
$$

而球外的磁场与理想偶极子的磁场相同，

$$
\boldsymbol {m} = \frac {4}{3} \pi R ^ {3} \boldsymbol {M}
$$

请注意，球内的磁场是均匀的，就像均匀极化球体内的电场一样[式(4.14)]，尽管这两种情况的具体表达式出奇的不一样 $\left(\frac{2}{3}\right)$ 代替了 $-\frac{1}{3}\bigg)^6$ 。外部磁场也是类似的：在这两种情况下都是纯偶极子场。

习题6.7 无限长圆柱体具有平行于其轴线的均匀的磁化强度 $M$ 。求由 $M$ 而引起圆柱体内外的磁场。

习题6.8 半径为 $R$ 的长圆柱体具有磁化强度 $M = ks^2\hat{\phi}$ ，其中 $k$ 为常数， $s$ 为距圆柱体轴线的距离，而 $\hat{\phi}$ 为常用方位角单位矢量（图6.13）。求由 $M$ 而产生的圆柱体内外点的磁场。

习题 6.9 半径为 a、长度为 L 的短圆柱体带有行于轴线的“冻结”均匀磁化强度 M。求它的束缚电流，并绘制该圆柱的磁场。（绘制三个草图：一种情况是 $L \gg a$ ，一种情况是 $L \ll a$ ，一种情况是 $L \approx a$ 。）将此条状磁铁（bar magnet）情况与习题 4.11 中的条形永电体进行比较。

习题 6.10 如图 6.14 所示，对长为 L、横截面为边长为的 a 正方形铁棒施加均匀的纵向磁化强度 M，然后将其弯成一个具有狭窄缺口的圆（缺口宽度为 w）。令 $w \ll a \ll L$ ，求缺口中心的磁场。[提示：将其视为一个完整的圆环加上一个反向电流的方形环的叠加。]

![](images/edf8fce5d86e699cb1dbe08166b3eb259134742aab3f61dc6a31a255b87218a5.jpg)  
图6.13

![](images/a700f2e9f225c3f1a91045ef74cc5a3eed677eb6c07886d0611d4129b6ea2712.jpg)  
图6.14

## 6.2.2 束缚电流的物理诠释

在上一节中，我们发现磁化物体的磁场与由特定分布的“束缚电流” $J_{b}$ 和 $K_{b}$ 所产生的磁场相同。我想告诉你这些束缚电流在物理上是如何产生的。这是个启发性的论证——严格的推导前面已经给出。图6.15描绘了一块均匀磁化的薄板，偶极子由微小的电流环表示。请注意，所有的“内部”电流都会相互抵消：每次有一个向右边流动的电流，就有与其相邻的一个向左边流动的电流。但是，在薄板的边缘处并没有相邻的环电流来将其抵消。因此，整体上等价于一个围绕边界流动的电流带I（图6.16）。

![](images/ee27ede51249a516401628c1a176d23ee27979bcc14ee777f063334be7afe3e7.jpg)  
图6.15

![](images/2a619819eaba3c80f56bc85bf3aa943546ce929b32850f76cbf57233fdbb6470.jpg)  
图6.16

这个与 M 有关的电流是多少？假定每个微小的环的面积为 a，厚度为 t（图 6.17）。其磁偶极矩用磁化强度 M 表示为 m = Mat。若以环电流 I 表示，则为 m = Ia。因此 I = Mt，所以表面电流为 $K_{b} = I/t = M$ 。使用指向外面的单位矢量 $\hat{n}$ （图 6.16）， $K_{b}$ 的方向可以很方便地由矢积得到：

$$
\boldsymbol {K} _ {\mathrm{b}} = \boldsymbol {M} \times \hat {\boldsymbol {n}}
$$

(该表达式还说明了在薄板的上表面和下表面没有电流的分布这一事实；这里 M 与 $\hat{n}$ 平行，因此矢积为零。)

![](images/bc65b6fdefd61a4e7d22dce180a47a30b738f920a1e5ed82ded5458e0d77bb9c.jpg)  
图6.17

这个束缚表面电流正是我们在第 6.2.1 节中得到的。在这种电流中没有一个电荷可以完成整个旅程——与此相反，每个电荷只在单个原子内的一个微小环路中移动，从这个意义上讲，这是一种特殊的电流。然而，总的效果是磁化介质表面流动的宏观电流。我们称之为“束缚”电流，这样称呼是提醒我们每个电荷都附着在一个特定的原子上，但它又是一个名副其实的真正电流，能够像其他的任何电流一样产生磁场。

当磁化不均匀时，内部电流不再相互抵消。图 6.18a 显示了磁化介质中两个相邻的磁化材料块，右侧的箭线较长，表明该点磁化强度大。在它们相连的表面上沿 x 方向有一净电流，它由下式给出：

$$
I _ {x} = \left[ M _ {z} (y + \mathrm{d} y) - M _ {z} (y) \right] \mathrm{d} z = \frac {\partial M _ {z}}{\partial y} \mathrm{d} y \mathrm{d} z
$$

![](images/6884f89b6f15a2ce2d38307879266f630c6a1b4830d2846da49ae8c56b204c5d.jpg)  
图6.18

因此，相应的体电流密度是

$$
(J _ {\mathrm{b}}) _ {x} = \frac {\partial M _ {z}}{\partial y}
$$

出于同样的考虑， $y$ 方向的非均匀磁化也会贡献一个量 $-\partial M_y / \partial z$ （图6.18b），所以

$$
(J _ {\mathrm{b}}) _ {x} = \frac {\partial M _ {z}}{\partial y} - \frac {\partial M _ {y}}{\partial z}
$$

一般来说

$$
J _ {\mathrm{b}} = \nabla \times M
$$

再次与第 6.2.1 节的结果一致。

顺便说一句，与任何其他稳恒电流一样， $J_{b}$ 应该遵守守恒定律式 (5.31):

$$
\nabla \cdot J _ {\mathrm{b}} = 0
$$

确实如此吗？当然，因为旋度的散度总是零。

## 6.2.3 介质内的磁场

与电场一样，介质内部的实际微观磁场在点与点之间、瞬间与瞬间之间存在剧烈的波动。当我们谈论介质内的“磁场”时指的是宏观场：即在足够大的区域内包含许多原子的平均值。（磁化强度 M 也在相同的意义上被“平滑”了。）当将第 6.2.1 节的方法应用于磁化介质内部的某点时，就会得到这个宏观场，正如你在下面的问题中证明的那样。

习题6.11 在第6.2.1节中，我们是从理想偶极子的矢势开始的[式(6.10)]，而事实上我们处理的是物理偶极子。利用第4.2.3节中的方法证明，我们仍然得到了正确的宏观场。

## 6.3 辅助场 $H$

## 6.3.1 磁介质中的安培定律

在第 6.2 节中，我们发现磁化的效果就是在介质内产生束缚电流 $J_{b} = \nabla \times M$ ，以及在表面上产生束缚电流 $K_{b} = M \times \hat{n}$ 。介质磁化产生的磁场就是这些束缚电流产生的磁场。我们现在可以将所有因素结合起来：束缚电流产生的磁场，加上其他一切所产生的磁场——我把称之为自由电流（free current）。自由电流可以流经嵌入磁化物体内部的导线，或者如果磁化物体是导体，则流经材料本身。在任何情况下，总电流都可以写为

$$
J = J _ {\mathrm{b}} + J _ {\mathrm{f}}\tag{6.17}
$$

式 (6.17) 中并没有新的内容；将电流分为这两部分只不过为了方便，因为它们是通过完全不同的方式得到的：自由电流之所以存在，是因为有人将导线连接到电池上——它涉及实际的电荷输运；束缚电流是因为磁化作用而存在的——它是由许多排列整齐的原子偶极子共同作用的结果。

根据式 $(6.13)$ 和式 $(6.17)$ ，安培定律可以写成

$$
\frac {1}{\mu_ {0}} (\nabla \times \boldsymbol {B}) = \boldsymbol {J} = \boldsymbol {J} _ {\mathrm{f}} + \boldsymbol {J} _ {\mathrm{b}} = \boldsymbol {J} _ {\mathrm{f}} + (\nabla \times \boldsymbol {M})
$$

或者，将式中两个旋度合并：

$$
\nabla \times \left(\frac {\boldsymbol {B}}{\mu_ {0}} - \boldsymbol {M}\right) = \boldsymbol {J} _ {\mathrm{f}}
$$

括号中的量用字母 H 表示：

$$
\boxed {H \equiv \frac {B}{\mu_ {0}} - M}\tag{6.18}
$$

于是，利用 $\pmb{H}$ 将安培定律表示为

$$
\boxed {\nabla \times \boldsymbol {H} = J _ {\mathrm{f}}}\tag{6.19}
$$

或者，表示成积分形式，

$$
\oint \boldsymbol {H} \cdot \mathrm{d} \boldsymbol {l} = \boldsymbol {I} _ {\text { fenc }}.\tag{6.20}
$$

其中 $I_{fenc}$ 是流经安培闭合环路中总的自由电流。

H 在静磁学中扮演着与静电学中 D 类似的角色：正如 D 允许我们将高斯定理写为只与自由电荷相关一样，H 使得我们可以将安培定理表述为仅与自由电流有关——自由电流是我们可以直接控制的。和束缚电荷一样，束缚电流伴随材料的磁化，材料磁化产生束缚电流；与自由电流不同，我们不能随意地打开或关闭束缚电流。在应用式 (6.20) 时，我们仅需考虑自由电流，这是我们施加上的，是已知的。特别是，当对称性允许时，我们可以直接从式 (6.20) 利用安培定律计算出 H。（例如，当注意到 H = 0 时，习题 6.7 和 6.8 可以只用一行就能得到解答。）

例题6.2 半径为 $R$ 的长铜棒中均匀分布有自由电流 $I$ （图6.19）。求棒内外的 $H$ 。

[解答] 铜具有微弱抗磁性，所以偶极子会沿磁场相反的方向排列。这导致束缚电流在导体内与 $I$ 反平行，并沿表面与 $I$ 平行（图6.20）。这些束缚流到底有多大，我们现在还不能确定——但为了计算 $H$ ，只要意识到所有电流都是纵向的就足够了，这样 $B, M$ 和 $H$ 都是环绕的。将式(6.20)应用于半径 $s < R$ 的安培环路，

$$
H \left(2 \pi s\right) = I _ {\mathrm{f} _ {\mathrm{enc}}} = I \frac {\pi s ^ {2}}{\pi R ^ {2}}
$$

所以导线内

$$
H = \frac {I}{2 \pi R ^ {2}} s \hat {\phi} (s \leqslant R)\tag{6.21}
$$

在导线外

$$
H = \frac {I}{2 \pi s} \hat {\phi} (s \geqslant R)\tag{6.22}
$$

在后者区域（真空中） $M = 0$ ，所以

$$
\boldsymbol {B} = \mu_ {0} \boldsymbol {H} = \frac {\mu_ {0} I}{2 \pi s} \hat {\phi} (s \geqslant R)
$$

这与一未磁化的导线是相同的（例题5.7）。目前还不能确定导线内的磁场 $B$ ，因为我们无法知道 $M$ （尽管在实际情况中铜的磁化强度非常小，以至于在大多数情况下我们可以完全忽略它）。

事实证明，H 是一个比 D 更有用的物理量。在实验室里，你会经常听到人们谈论 H（甚至比 B 更频繁），但你很少听到任何人谈起 D（只有 E）。原因是这样的：为了制造电磁铁，你需要让一定的（自由）电流流过线圈。电流正是你在表盘上看到的东西，它决定了 H 的大小（或者无论如何，决定了 H 的线积分）；B 则与你所使用的具体材料有关，如果是铁的话它甚至与磁化的历史有关。另一方面，如果你想要建立一个电场，你不需要把已知的自由电荷涂抹在平行板电容器的极板上，相反，你会把它们连接到一个已知电压的电池上。这是你在表盘上看到的电势差，它决定了 E（或者更确切地说，是 E 的线积分）；D 与你所使用的电介质的具体材料有关。如果电荷很容易测量，而电势很难测量，那么你就会发现实验物理学家们谈论的就是 D 而不是 E。因此，与 D 相比，对 H 的相对熟悉度是源于纯粹的实践上的考虑；照理说他们是对等的。

很多作者将 H，而不是 B，称作“磁场”。然后他们不得不再为 B 发明一个新词：“流密度”，或者磁“感应强度”（这是一个悖理的选择，因为这个词在电动力学中至少还有另外两个含义）。无论如何，B 无疑是一个基本量，所以我将继续称之为“磁场”，就像人们口语中称呼那样。H 没有一个合理的名字：称作“H”就可以了 $^{7}$ 。

习题6.12 半径为 $R$ 的无限长圆柱具有平行其轴线的“冻结”磁化强度，

$$
M = k s \hat {z}
$$

其中 $k$ 为常数而 $s$ 为到轴线的距离；空间不存在自由电流。通过两种不同的方法求圆柱体内外的磁场：

（b）使用安培定律 [利用式 (6.20) 的形式] 求 $H$ ，然后利用式 (6.18) 求 $B$ 。（请注意，第二个方法要快捷得多，并且避免了对于束缚电流的直接引用。）

习题6.13 假设大块磁性材料内部的场为 $B_{0}$ ，因此 $H_0 = (1 / \mu_0)B_0 - M$ ，其中 $M$ 是“冻结”磁化强度。

（a）现从材料中挖出一小球形腔（图6.21）。根据 $B_{0}$ 和 $M$ ，求空腔中心的磁场。根据 $H_0$ 和 $M$ 求空腔中心的 $\pmb{H}$ 。

(b) 对平行于 $M$ 的长针形腔做同样的计算。

(c) 对垂直于 M 的薄晶圆形空腔做同样的计算。

假设上述空腔都足够小，因此 $M, B_0$ 和 $H_0$ 基本恒定。与习题4.16做比较。[提示：挖出的空腔等同于叠加一形状相同但磁化强度方向相反的物体。]

![](images/f1243f924298f9348cb633ada5cc7328dfb797a683d529cdae4736f198eef9b0.jpg)  
图6.21

## 6.3.2 误导性的类比

除了总电流被自由电流替代，B 由 $\mu_{0}H_{0}$ 替代外，式 (6.19) 看起来很像原始的安培定律 [式 (5.56)]。然而，正如 D 的情况一样，我必须提醒你不要被这种相似性所迷惑。这并不是说 $\mu_{0}H$ “就像 B 一样，只是它的源是 $J_{f}$ 而不是 J”。因为旋度本身并不能决定一个矢量场——你还必须知道散度。而 $\nabla \cdot B = 0$ ，H 的散度一般不为零。事实上，根据式 (6.18) 有

$$
\nabla \cdot \boldsymbol {H} = - \nabla \cdot \boldsymbol {M}\tag{6.23}
$$

只有当 M 的散度为零时，B 和 H 之间才可以进行类比。

如果你认为我有点迂腐，考虑一下条形磁铁的例子——一个具有永均匀久磁化强度 M 且方向平行于其轴线的短铁柱（参阅习题 6.9 和 6.14）。在这种情况下，空间处处没有自由电流，将式 (6.20) 应用到这里可能会导致你认为 H = 0，因此磁铁内部 $B = \mu_{0} M$ ，而外部 B = 0，这是无稽之谈。确实 H 的旋度处处为零，但是散度不为零。（你能看出哪里的 $\nabla \cdot M = 0$ 吗？）建议：当你涉及在磁性材料的问题中求 B 或 H 时，首先要找出对称性。如果讨论的问题中具有圆柱、平面、螺线管，或者环状对称性，那么你就可以利用安培定律直接从式 (6.20) 中求出 H。（显然，在这些情况下， $\nabla \cdot M$ 自动为零，因为仅自由电流就确定了结果。）如果问题不具备一定的对称性，你就不得不考虑另一种方法，特别是你不能仅仅因为看到自由电流的情况下就假设 H 为零。

## 6.3.3 边界条件

第 5.4.2 节中的静磁学边界条件可以用 H 和自由电流重新表示。根据式 (6.23)，可以得出

$$
H _ {\text {上}} ^ {\perp} - H _ {\text {下}} ^ {\perp} = - (M _ {\text {上}} ^ {\perp} - M _ {\text {下}} ^ {\perp})\tag{6.24}
$$

而式 (6.19) 表明

$$
H _ {\mathrm{上}} ^ {\parallel} - H _ {\mathrm{下}} ^ {\parallel} = K _ {\mathrm{f}} \times \hat {n}\tag{6.25}
$$

当介质存在时，上述公式较用 B 来表示的相应边界条件 [式 (5.72) 和式 (5.73)] 更为有用：

$$
B _ {\text {上}} ^ {\perp} - B _ {\text {下}} ^ {\perp} = 0\tag{6.26}
$$

和

$$
\pmb {B} _ {\text {上}} ^ {\parallel} - \pmb {B} _ {\text {下}} ^ {\parallel} = \mu_ {0} (\pmb {K} \times \hat {\pmb {n}})\tag{6.27}
$$

你可以用例题 6.2 或者习题 6.14 来检验它们。

习题6.14 对于习题6.9中的条形磁铁，假设 $L$ 大约为 $2a$ ，仔细绘制 $M, B$ 和 $H$ 的草图。并与习题4.17做比较。

习题6.15 如果处处 $J_{\mathrm{f}} = 0$ ，则 $\pmb{H}$ 的旋度为零[式(6.19)]，我们可以将 $\pmb{H}$ 表示为标量势 $W$ 的梯度：

$$
\pmb {H} = - \nabla W
$$

根据式 (6.23) 有

$$
\nabla^ {2} W = \nabla \cdot M
$$

因此，W 满足以 $\nabla \cdot M$ 为 “源” 的泊松方程。这样拓展了第 3 章的所有内容。例如，通过分离变量法求均匀磁化球（例题 6.1）内磁场。[提示：除表面 $(r = R)$ 外，处处 $\nabla \cdot M = 0$ ；因此 W 在 r < R 和 r > R 的区域都满足拉普拉斯方程；使用式 (3.65)，并从式 (6.24) 中得出 W 的适当边界条件。]

## 6.4 线性和非线性介质

## 6.4.1 磁化率与磁导率

在顺磁性和抗磁性材料中，磁化是由磁场来维持的；当 B 撤掉后，M 也会消失。事实上，在磁场不是太强的情况下，大多数材料的磁化强度都与磁场强度成正比。为了与电学情况 [式 (4.30)] 在符号上保持一致，我应该把这种比例关系表示为

$$
M = \frac {1}{\mu_ {0}} \chi_ {\mathrm{m}} B \quad (\text {不正确!})\tag{6.28}
$$

但习惯上要求用 H 而不是 B 来表示：

$$
\boxed {M = \chi_ {\mathrm{m}} H}\tag{6.29}
$$

比例常数 $\chi_{\mathrm{m}}$ 被称为磁化率（magnetic susceptibility）；它是一个随介质而异的无量纲的量——顺磁质为正，抗磁质为负。通常数值大约为 $10^{-5}$ （参阅表6.1）。

表 6.1 磁化率值（除非特别注明，数值均为在 1 个大气压下，温度为 $20^{\circ}C$ 时得到）  
来源：《物理化学手册》（第91版）（Boca Raton: CRC Press, 2010），以及其他参考资料。

<table><tr><td>材料</td><td>磁化率</td><td>材料</td><td>磁化率</td></tr><tr><td>抗磁性:</td><td></td><td>顺磁性:</td><td></td></tr><tr><td>铋</td><td> $-1.7 \times 10^{-4}$ </td><td>氧( $O_2$ )</td><td> $1.7 \times 10^{-6}$ </td></tr><tr><td>金</td><td> $-3.4 \times 10^{-5}$ </td><td>钠</td><td> $8.5 \times 10^{-6}$ </td></tr><tr><td>银</td><td> $-2.4 \times 10^{-5}$ </td><td>铝</td><td> $2.2 \times 10^{-5}$ </td></tr><tr><td>铜</td><td> $-9.7 \times 10^{-6}$ </td><td>钨</td><td> $7.0 \times 10^{-5}$ </td></tr><tr><td>水</td><td> $-9.0 \times 10^{-6}$ </td><td>铂</td><td> $2.7 \times 10^{-4}$ </td></tr><tr><td>二氧化碳</td><td> $-1.1 \times 10^{-8}$ </td><td>液氧( $-200^{\circ}C$ )</td><td> $3.9 \times 10^{-3}$ </td></tr><tr><td>氢( $H_2$ )</td><td> $-2.1 \times 10^{-9}$ </td><td>钆</td><td> $4.8 \times 10^{-1}$ </td></tr></table>

遵从式(6.29)的材料称为线性介质（linear media）。根据式(6.18)，对线性介质有

$$
\pmb {B} = \mu_ {0} (\pmb {H} + \pmb {M}) = \mu_ {0} (1 + \chi_ {\mathrm{m}}) \pmb {H}\tag{6.30}
$$

这样 B 也与 H 成正比 $^{8}$ :

$$
\boldsymbol {B} = \mu \boldsymbol {H}\tag{6.31}
$$

其中

$$
\mu \equiv \mu_ {0} (1 + \chi_ {\mathrm{m}})\tag{6.32}
$$

$\mu$ 称为材料的磁导率（permeability） $^{9}$ 。在真空中，没有物质可以被磁化，磁化率 $\chi_{\mathrm{m}}$ 为零，磁导率为 $\mu_{0}$ 。这就是为什么 $\mu_{0}$ 被称为真空磁导率（permeability of free space）。

如果介质是顺磁性的，则磁场略有增强；如果它是抗磁性的，则磁场会有所减弱。

$$
K _ {\mathrm{b}} = M \times \hat {n} = \chi_ {\mathrm{m}} (H \times \hat {n}) = \chi_ {\mathrm{m}} n I \hat {\phi}
$$

这反映了前者 $(\chi_{\mathrm{m}} < 0)$ 表面束缚电流的方向与 $I$ 的方向是相同，而后者 $(\chi_{\mathrm{m}} > 0)$ 则相反的事实。

![](images/07e4819def32e46bcefd840cb89dd92004a8cb1dad0bdad8eed0fc6863606026.jpg)

你可能会认为线性介质避免了 B 和 H 之间类比中所出现的缺陷：既然 M 和 H 都与 B 成正比例，就像 B 的散度一样，那么它们的散度一定总是零？遗憾的是，事实并非如此 $^{10}$ ；事实上在两种不同磁化率材料的界面处，M 的散度可以是无穷大。例如，在线性顺磁材料圆柱体的末端，M 在一侧为零，但在另一侧不为零。对于图 6.23 中所示的“高斯扁盒”， $\oint M \cdot da \neq 0$ ，因此，根据散度定理， $\nabla \cdot M$ 不可能在其内部处处为零。

![](images/8eab298760e30185ed8d1e8d65d6535071c69ca308b44dd2baa39fbab5a933c9.jpg)  
图6.23

顺便说一句，各向同性线性材料中的体束缚电流密度与自由电流密度成正比：

$$
\boldsymbol {J} _ {\mathrm{b}} = \nabla \times \boldsymbol {M} = \nabla \times (\chi_ {\mathrm{m}} \boldsymbol {H}) = \chi_ {\mathrm{m}} \boldsymbol {J} _ {\mathrm{f}}\tag{6.33}
$$

特别是，除非自由电流真正流经材料，否则所有束缚电流都将在表面上。

习题6.16 同轴电缆由两根很长的圆柱形管组成，被磁化率为 $\chi_{\mathrm{m}}$ 的线性绝缘介质隔开。电流 $I$ 沿内导体向一侧流动，并沿外导体流回；在每种情况下，电流都均匀分布在表面上（图6.24）。求管间区域的磁场。作为验证，计算磁化强度和束缚电流，并确认它们（当然，包括自由电流）产生了正确的磁场。

![](images/f2e93bc7854121b4699817611e84cbb40329b79d7803df7fca710f3644f9cf6b.jpg)  
图6.24

习题 6.17 电流 I 流经一半径为 a 的长直导线。若导线是由磁化率为 $\chi_{m}$ 的线性材料制成的（比如说铜，或者铝），并且电流均匀分布，则距轴线距离为 s 处的磁场是多少？求所有的束缚电流。流经导线的净束缚电流是多少？

！习题6.18 将线性磁材料球体置于均匀的磁场 $B_{0}$ 中，求球内的磁场。[提示：参阅习题6.15或习题4.23。]

习题6.19 根据第6.1.3节中提出的简单模型，估计铜等抗磁性金属的磁化率。将你的答案与表6.1中的经验值进行比较，并对其差异进行讨论。

## 6.4.2 铁磁性

在线性介质中，原子偶极子的排列是由外加的磁场来维持的。铁磁体——明显是非线性的 $^{11}$ ——不需要外磁场来维持磁化；偶极子的排列是已被“冻结的”。与顺磁性一样，铁磁性与未配对电子自旋相关的磁偶极子有关。与顺磁性相比，铁磁性新的特征表现在相邻偶极子之间的相互作用：在铁磁体中，每个偶极子“喜欢”指向与其相邻偶极子一样的方向。这种特点的根本原因是量子力学，我在这里不尝试解释它；只要知道这种关联性非常强，以至于这些未配对的电子自旋几乎是100%的定向排列就足够了。如果你能以某种方法放大一块磁铁，并且能将单独的偶极子“看见”成为微小箭头，它看起来就会像图6.25，所有的箭头都指向相同的方向。

![](images/bde744e0ae51925ad32f6305d0846ee16bcd874c266258f6e0f7eb7ef8483334.jpg)  
图6.25

但是，如果这是真的，每个扳手和钉子为什么不是一个强大的磁铁？答案是这种同向排列仅在一个被称为畴（domains）的相对小的区域内发生。每个畴包含数十亿个偶极子，所有偶极子都是定向排列的（事实上这些畴通过合适的蚀刻工艺处理后在显微镜下是可以看见的——见图6.26），但是，这些畴本身是随机指向的。家用扳手包含大量的畴，但它们的磁场相互抵消，所以扳手作为整体是没有磁化的。（实际上，畴的取向并不是完全随机的；在给定的晶粒中，沿着晶轴方向的排列会更多些。但是，指向一个方向的畴与指向另一个方向的畴一样多，所以晶体仍然不会有大规模的磁化。此外，晶粒本身在大块金属内部也是随机指向的。）

![](images/dcf87ea0219527ca6f64caa3dc231b15602a282de13ea2e16d40065aebae440a.jpg)  
铁磁畴（照片承蒙R.W.德布洛斯提供）  
图6.26

那么，你如何构建一块就像在玩具店卖的那样的永磁体（permanent magnet）？如果你将一块铁放入一个强磁场中，力矩 $N = m \times B$ 驱使这些偶极子沿平行于磁场的方向排列。由于偶极子喜欢与它们的邻居保持平行，大多数偶极子将会抵抗这种力矩。然而，在两个畴之间的边界处，存在着相互竞争的邻居，该力矩对已与磁场高度平行畴有利；该畴会使边界上其他畴的偶极子转向成按照自己排列的方向。因此，磁场最终的效果是使畴边界发生移动。平行于磁场的畴生长变大，而其他的畴相对收缩。如果磁场足够强，则会变成单一畴，而此时铁块被称为是“饱和的”（saturated）。

事实证明，这个过程（响应外场而改变畴边界）并不完全可逆：当外场撤去后，虽然有一部分畴会变回随机取向的畴，但远非全部——仍然有大部分畴处于原来磁场的方向。你现在就有一块永磁体了。

在实际过程中,实现这一点的一个简单的办法是将待磁化物体上缠绕上线圈（图 6.27）。在线圈上通电流 I；这提供了外磁场（指向图中的左侧）。随着电流的增大，磁场增强，畴边界移动，磁化强度变大。最终，达到了饱和点，所有的偶极子都沿一个方向排列；进一步增大电流对 M 不会再产生任何影响（图 6.28，b 点）。

现在假设你减小电流。与原路返回到 M=0 不同，而是仅有部分畴恢复到原来随机取向畴。M 减小，但即使是切断仍有一些剩余磁化（c 点）。扳手现在是一个永磁体了。如果你想要消除剩磁，将不得不在线圈中通入一个反向电流（负的 I）。现在外磁场方向向右，当你增强 I（负的）时，M 降低到零（d 点）。如果你把 I 升得更高，很快就会再另一个方向上达到饱和——所有的偶极子指向右边（e）。在这个阶段，关闭电流将使扳手向右永久磁化（f 点）。为了完成全部过程，再次打开正方向的 I：M 回到零点（g），并最终返回到正向饱和点（b）。

![](images/96783c0322c253f07a754b638d49e439a75995df37be78bc9e57e52deb0b0aad.jpg)  
图6.27

![](images/3db472157269c2054d1022e6486d9448b9599c85a1591a9680d86c7f263efdb6.jpg)  
图6.28

我们上述所描绘的路径被称为磁滞回线（hysteresis loop）。请注意，扳手的磁化不仅与施加的磁场（依赖 $I$ ）有关，而且还与它之前的磁“历史”有关 $^{12}$ 。例如，在我们的实验中的三个不同时刻电流都为零（ $a, c$ 和 $f$ ），但每个时刻的磁化强度都不相同。实际上，通常将磁滞回线绘制为 $B$ 关于 $H$ 的曲线，而不是 $M$ 关于 $I$ 的曲线。[如果我们的线圈近似为一个长螺线管，每单位长度有 $n$ 匝，那么 $H = nI$ ，因此 $H$ 和 $I$ 成正比例。同时， $B = \mu_0(H + M)$ ，但在实际情况中， $M$ 与 $H$ 相比是很大的，因此从我们的意图和目的来看， $B$ 是与 $M$ 成正比的。]

为了使单位一致（特斯拉），我将 $(\mu_{0}H)$ 作为横轴（图6.29）；但是，请注意竖直标度是水平标度的 $10^{4}$ 倍。粗略地讲， $\mu_{0}H$ 是线圈不存在任何铁磁质的情况下产生的磁场；B是我们实际得到的磁场，与 $\mu_{0}H$ 相比，B则巨大无比。当周围存在铁磁性材料时，一个小的电流就可以产生很强的磁场。这就是为什么人们制造强磁铁时都要把线圈缠绕在铁心上。这样一来，不需要大的外磁场就可以移动畴边界，只要你加上外磁场，铁中的所有偶极子都做定向排列。

关于铁磁性的最后一点讨论：请记住，铁磁体的一切特性都源于给定畴内的偶极子的彼此平行排列。铁磁体中存在随机热运动与彼此平行排列的竞争，但只要温度不是太高，这些偶极子就不会偏离其定向排列。不过，在很高的温度情况下这种定向排列确实会给破坏掉，这并不奇怪。令人惊奇的是，这种情形发生在一个精确的温度下（对铁来说，770℃）。低于该温度（Curie point，称作居里点），铁就是铁磁性的；高于该温度，它就是顺磁性的。居里点很像沸点或者凝固点，因为从铁磁性到顺磁性之间不是逐渐变化，就像水和冰之间的转变一样。在严格定义的温度下发生的物质性质的这些突变在统计力学中被称为相变（phase transitions）。

![](images/f1a84fb66e368d2f46781a2dda0a55c37c6d6c935734babc723d1c5d5f539d31.jpg)  
图6.29

习题6.20 你如何给一块永磁铁进行退磁（例如，我们一直在讨论的扳手，处在磁滞回线的 $c$ 点）？即你如何将其恢复到 $I = 0$ 时 $M = 0$ 的原始状态？

## 习题6.21

(a) 证明磁场 B 中磁偶极子的能量是

$$
\boxed {U = - \boldsymbol {m} \cdot \boldsymbol {B}}\tag{6.34}
$$

[假设偶极矩的大小是不变的，而你所要做的就是将其移动到位并将其旋转到它的最终指向。维持电流流动所需要的能量是另一个问题，我们将在第7章中遇到。]与式(4.6)做比较。

（b）证明分开位移为 r 的两个磁偶极子的相互作用能量由下式给出：

$$
U = \frac {\mu_ {0}}{4 \pi} \frac {1}{r ^ {3}} [ m _ {1} \cdot m _ {2} - 3 (m _ {1} \cdot \hat {r}) (m _ {2} \cdot \hat {r}) ]\tag{6.35}
$$

将其与式 $(4.7)$ 做比较。

（c）根据图6.30中的角度 $\theta_{1}$ 和 $\theta_{2}$ 来表示（b）中的答案，并使用该结果给出两个偶极子在其之间距离保持不变且可以自由转动的情况下所处的稳定几何状态。

(d) 假设你有很多指南针，将它们沿直线等间距固定排列。它们将指向哪里（假设地球磁场可以忽略不计）？[矩形阵列的指南针会自发对齐，这有时候被用来做大规模“铁磁”现象的演示。然而，这有点欺骗的嫌疑，因为这里面的机制完全是经典的，而且比导致铁磁性的量子力学交换力要弱得多 $^{13}$ 。]

![](images/af9e234b86c8a2a691a1fca8f0e3ee68d1f034d1fcfe209507eb7368a69cdbe8.jpg)  
图6.30

## 第6章补充习题

！习题6.22 在习题6.4中，你通过“蛮力”计算了偶极子上的力。这里有一个更简洁的方法。首先将 $B(r)$ 写成关于线圈中心的泰勒展开式：

$$
\boldsymbol {B} (\boldsymbol {r}) \cong \boldsymbol {B} (\boldsymbol {r} _ {0}) + [ (\boldsymbol {r} - \boldsymbol {r} _ {0}) \cdot \nabla_ {0} ] \boldsymbol {B} (\boldsymbol {r} _ {0})
$$

其中 $r_0$ 是偶极子的位置， $\nabla_0$ 表示相对于 $r_0$ 的微分。将其代入洛伦兹力定律[式(5.16)]，得到

$$
\boldsymbol {F} = I \oint \mathrm{d} \boldsymbol {l} \times [ (\boldsymbol {r} \cdot \nabla_ {0}) \boldsymbol {B} (\boldsymbol {r} _ {0}) ]
$$

或者，将直角坐标从 1 编号到 3:

$$
F _ {i} = I \sum_ {j, k, l = 1} ^ {3} \varepsilon_ {i j k} \left\{\oint r _ {l} \mathrm{d} l _ {j} \right\} [ \nabla_ {0 l} B _ {k} (\boldsymbol {r} _ {0}) ]
$$

其中 $\varepsilon_{ijk}$ 是莱维-西维特（Levi-Civita symbol）符号（取 $+1$ ，如果 $ijk = 123,231,$ 或312；取-1，如果 $ijk = 132,213,$ 或321；取0，其他情况）；利用这个符号，矢量叉积可以写成 $(\pmb {A}\times \pmb {B})_i = \sum_{j,k = 1}^{3}\varepsilon_{ijk}A_jB_k$ 利用式(1.108）计算积分。注意

$$
\sum_ {j = 1} ^ {3} \varepsilon_ {i j k} \varepsilon_ {l j m} = \delta_ {i l} \delta_ {k m} - \delta_ {i m} \delta_ {k l}
$$

其中 $\delta_{ij}$ 是克罗内克 $\delta$ 符号（习题3.52）。

习题6.23如图6.31所示，一个常见玩具由甜甜圈形状的永磁体（磁化平行于轴线）组成，它们在竖直杆上无摩擦地滑动。将磁体视为质量为 $m_{d}$ 、偶极矩为 $\pmb{m}$ 的偶极子。

（a）如果你把两个背对背的磁体放在杆上，上面的一个会“浮起”——向上的磁力与向下的重力相平衡。磁体浮起的高度是多少 $(z)$ ？

（b）如果你在上面添加第3个磁体（与底部的那个方向相同），两个磁体的高度比是多少？（求出具体数字，精确到三位有效数字。）[答案：（a） $\left[3\mu_0m^2 /2\pi m_dg\right]^{1 / 4}$ ；（b）0.8501]

习题6.24 想象两个带电的磁偶极子（电荷 $q$ ，偶极矩 $m$ ）约束在 $z$ 轴上运动（与习题6.23（a）相同，但不受重力）。两者在电学上相互排斥，但在磁性上（如果两个 $m$ 都指向 $z$ 方向）相互吸引。

(a) 求平衡时分离的距离。

(b) 在这个方向上，两个电子的平衡间距是多少。[答案： $4.72 \times 10^{-13} \, m$ ]

(c) 那么，是否存在两个电子的稳定束缚态？

![](images/e847cfd9f315470a87448856b1461ba4587230ffad9da88d59e9b1dd753b8294.jpg)

![](images/e8569c1a95aa05df9e0abf6b1b076f5bfd9c68ea7632c743aac2304c8d8f9645.jpg)  
图6.31

习题6.25 请注意下述公式的相似之处：

$$
\left\{ \begin{array}{l l} {{\nabla \cdot \pmb {D} = 0,}} & {{\nabla \times \pmb {E} = \mathbf {0}, \quad \varepsilon_ {0} \pmb {E} = \pmb {D} - \pmb {P} \qquad (\mathrm{无自由电荷})}} \\ {{\nabla \cdot \pmb {B} = 0,}} & {{\nabla \times \pmb {H} = \mathbf {0}, \quad \mu_ {0} \pmb {H} = \pmb {B} - \mu_ {0} \pmb {M} \quad (\mathrm{无自由电流})}} \end{array} \right.
$$

因此，改写 $D \to B, E \to H, P \to \mu_0 M, \varepsilon_0 \to \mu_0$ 将静电学问题转化为类似的静磁学问题。结合你对静电学知识的了解，利用这些类比重新导出

(a) 均匀磁化球体内的磁场 [式 (6.16)];

（b）在均匀磁场中线性磁性材料球体内的磁场（习题6.18）；

(c) 球体内的稳定电流在球体上产生的平均磁场 [式 (5.93)]。

习题6.26 比较式(2.15)、式(4.9)和式(6.11)。请注意，如果 $\rho, P$ 和 $M$ 都是均匀的，则所有三个都涉及相同的积分：

$$
\int \frac {\hat {n}}{r ^ {2}} \mathrm{d} \tau^ {\prime}
$$

因此，如果你碰巧知道均匀带电物体产生的电场，就可以立即写出相同形状的均匀极化物体的标量势和均匀磁化物体的矢量势。使用此观察结果求均匀极化球体内外的 V（例题 4.2）和均匀磁化球体内外的 A（例题 6.1）。

习题6.27 在两个线性磁材料之间的界面处，磁场线弯折（图6.32）。证明 $\tan \theta_{2} / \tan \theta_{1} = \mu_{2} / \mu_{1}$ 假设边界处没有自由电流。与式(4.68)做比较。

![](images/91819f47755f9e821a97f87f7cb2cd57ddad78df85eb62e844d74d8bcb99c54e.jpg)  
图6.32

！习题6.28 磁偶极子 $m$ 嵌入线性磁性材料（磁导率为 $\mu$ ）球体（半径 $R$ ）的中心。证明球体内的

磁场 $(0 < r \leqslant R)$ 为

$$
\frac {\mu}{4 \pi} \left\{\frac {1}{r ^ {3}} [ 3 (\pmb {m} \cdot \hat {\pmb {r}}) \hat {\pmb {r}} - \pmb {m} ] + \frac {2 (\mu_ {0} - \mu) \pmb {m}}{(2 \mu_ {0} + \mu) R ^ {3}} \right\}
$$

## 球体外的磁场是多少？

习题 6.29 你被邀请评审一份基金申请，该项目旨在确定铁的磁化是由“安培”偶极子（电流环）还是由“吉尔波特”偶极子（分离的磁单极子）引起的。实验将涉及一个铁圆柱体（半径为 R，长度 L = 10R）沿其轴线方向均匀磁化。如果偶极子是安培型，则磁化相当于表面束缚电流 $K_{b} = M\hat{\phi}$ ；如果它们是吉尔波特型，则磁化相当于两端的表面磁单极子密度 $\sigma_{b} = \pm M$ 。遗憾的是，这两种情况在外部产生的磁场相同。然而，产生内部磁场却完全不同——在第一种情况下，B 与 M 的方向大体上相同，而在第二种情况下则与 M 大致相反。申请人建议在圆柱体上挖出一个小空腔并且通过测量放置在里面的微型指南针所受到的力矩来求出内部的磁场。

假设公认的技术困难可以克服，并且这个问题本身值得研究，你会建议资助这个实验吗？如果资助，你会建议什么样形状的空腔？如果不资助，这个申请存在什么问题？[提示：请参阅习题4.11、习题4.16、习题6.9和习题6.13。]

## 7.1 欧姆定律 电动势

## 7.1.1 欧姆定律

为了使电流流动，你必须推进其中的电荷。作为对给定驱动力的响应，这些电荷运动的快慢取决于材料的性质。对于大多数物质来说，电流密度 J 与每单位电荷受到的力 f 成正比：

$$
J = \sigma f\tag{7.1}
$$

比例因子 $\sigma$ （不要与面电荷密度相混淆）是一个因材料而异的经验常数；它被称为材料的电导率（conductivity）。事实上，相关手册上通常列出 $\sigma$ 的倒数，称为电阻率（resistivity）： $\rho = 1 / \sigma$ （不要与电荷密度相混淆——我很抱歉，但是我们快用光了希腊字母，而这是标准记号）。一些典型值在表7.1中给出。注意，即使绝缘体也会轻微地导电，尽管金属的电导率是大天文数字量级；事实上，对于大多数用途，金属可以被认为是理想导体（perfect conductors），其 $\sigma = \infty$ ；而对于绝缘体，我们可以假设 $\sigma = 0$ 。

原则上，驱动电荷产生电流的力可以是任何力——化学的、引力的，或者套上微型马具受过训练的蚂蚁。不过，对于我们的目的来说，通常是电磁力来承担这份工作。在这种情形下式(7.1)变为

$$
\boldsymbol {J} = \sigma (\boldsymbol {E} + \boldsymbol {v} \times \boldsymbol {B})\tag{7.2}
$$

通常，电荷的速度非常小，以至于第二项可以被忽略：

$$
\boxed {J = \sigma E}\tag{7.3}
$$

(然而,例如,在等离子体中,f 中磁的贡献可能会是显著的。)式 (7.3)称为 欧姆定律（Ohm's law），尽管事实上它背后的物理是包含在式 (7.1)中的，而式 (7.3)只是它的一个特例。

我知道：你们现在感到困惑，因为我说过一个导体内部 E = 0（第 2.5.1 小节）。但是那是对静止电荷来说的 $(J = 0)$ 。此外，对于理想导体来说，甚至当电流流动时也有 $E = J / \sigma = 0$ 。在实际中，金属是非常好的导体以至于在导体内部驱动电流所需要的电场是微不足道的。这样，（例如）我们通常将电路中连接的导线看成等势体。与此相反，电阻元件（resistors）是由导电性差的材料制成的。

表 7.1 材料电阻率（都是在 1atm 和 20°C 条件下的值，单位取 Ω·m）  
来源：《物理化学手册》（第91版）（Boca Raton: CRC Press, 2010）和其他文献。

<table><tr><td>材料</td><td>电阻率</td><td>材料</td><td>电阻率</td></tr><tr><td>导体:</td><td></td><td>半导体:</td><td></td></tr><tr><td>银</td><td> $1.59 \times 10^{-8}$ </td><td>海水</td><td>0.2</td></tr><tr><td>铜</td><td> $1.68 \times 10^{-8}$ </td><td>锗</td><td>0.46</td></tr><tr><td>金</td><td> $2.21 \times 10^{-8}$ </td><td>钻石</td><td>2.7</td></tr><tr><td>铝</td><td> $2.65 \times 10^{-8}$ </td><td>硅</td><td>2500</td></tr><tr><td>铁</td><td> $9.61 \times 10^{-8}$ </td><td>绝缘体:</td><td></td></tr><tr><td>水银</td><td> $9.61 \times 10^{-7}$ </td><td>纯水</td><td> $8.3 \times 10^{3}$ </td></tr><tr><td>镍铬合金</td><td> $1.08 \times 10^{-6}$ </td><td>玻璃</td><td> $10^{9} - 10^{14}$ </td></tr><tr><td>锰</td><td> $1.44 \times 10^{-6}$ </td><td>橡胶</td><td> $10^{13} - 10^{15}$ </td></tr><tr><td>石墨</td><td> $1.6 \times 10^{-5}$ </td><td>特氟隆</td><td> $10^{22} - 10^{24}$ </td></tr></table>

例题7.1 一个横截面积为 $A$ 、长度为 $L$ 的圆柱状电阻器是由电导率为 $\sigma$ 的材料制成的。（如图7.1所示，横截面并不需要是圆形的，但是我特假定横截面的形状是保持不变的。）保持两端的电势都是常数，而两端之间的电势差是 $V$ ，流过的电流为多大？

![](images/9e176d0aaeb42aa2d887878cdac20f69121420aa2ee8b370ef989e1cfab1be6e.jpg)

[解答] 可以证明，导线内部的电场是均匀的（我稍后会证明这一点）。从式(7.3)可以得出电流密度也是均匀的，所以

$$
I = J A = \sigma E A = \frac {\sigma A}{L} V
$$

例题7.2 两个同心金属长圆柱面（半径 $a$ 和 $b$ ）被电导率为 $\sigma$ 的材料分开，如图7.2所示。如果保持这两个圆柱面之间的电势差为 $V$ ，在长度 $L$ 内，从一个圆柱面流向另一个圆柱面的电流为多大？

![](images/3ca0a45e1db66a0ab46fc6a7c330d42752b2c3485edab2c111a363ecb08eab68.jpg)

图 1-2. 求 $L$ 的长度为 ${L}_{\text{总}}$ 。

图7.2[解答] 两个同心长圆柱面之间的场为 $E = \frac{\lambda}{2\pi\varepsilon_0s}\hat{s}$ 其中 $\lambda$ 是内部圆柱面上单位长度的电荷。从而在长度 $L$ 内电流为

$$
I = \int \boldsymbol {J} \cdot \mathrm{d} \boldsymbol {a} = \sigma \int \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {a} = \frac {\sigma}{\varepsilon_ {0}} \lambda L
$$

（这个积分是关于包围内部圆柱面的任意面的。）同时，圆柱面之间的电势差为

$$
V = - \int_ {b} ^ {a} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = \frac {\lambda}{2 \pi \varepsilon_ {0}} \ln \left(\frac {b}{a}\right)
$$

所以

$$
I = \frac {2 \pi \sigma L}{\ln (b / a)} V
$$

正如这些例子所表明的，从一个电极流向另一个电极的总电流与两者间的电势差成正比：

$$
\boxed {V = I R}\tag{7.4}
$$

当然，这是欧姆定律更加令人熟悉的版本。比例常数 $R$ 被称为电阻（resistance）；它是电极之间介质的分布形状和电导率的函数。[在例题7.1中， $R = (L / \sigma A)$ ；在例题7.2中， $R = \ln (b / a) / 2\pi \sigma L$ 。]电阻的单位是欧姆（ohms， $\Omega$ ）：一欧姆等于一伏特除以一安培。注意 $V$ 和 $I$ 之间的正比关系是式(7.3)的直接结果：如果想要 $V$ 翻倍，你只要将每处的电荷加倍——但这使 $E$ 加倍，对欧姆性材料也就使 $J$ 加倍，也就使 $I$ 加倍。

对于稳恒电流和均匀电导率来说，

$$
\nabla \cdot \pmb {E} = \frac {1}{\sigma} \nabla \cdot \pmb {J} = 0\tag{7.5}
$$

[这也就是式(5.33)]，因此电荷密度为零；任何未抵消的电荷都存在于表面上。（我们很久以前就利用 $E = 0$ 的事实对静止电荷情形证明了这个结论；显然，当允许电荷运动时这个结论也是正确的。）特别是，由此可得，在一个载有稳恒电流的各向同性欧姆材料中，拉普拉斯方程仍然成立，所以第3章中所有的工具和技巧都可以用来计算电势。

如果撤去导电材料，只剩下两边各一块的金属板（图 7.3），与上面相比，问题就要难得多了。显然对圆柱体情形，电荷以在内部产生均匀场的方式在导线表面上自行排布 $^{1}$ 。

![](images/f077d1294419f39d7cafea0ecb32a1bc1e52a9051779429941764054e0dc1b9e.jpg)  
图7.3

我想在物理学中不会有比欧姆定律更广为人知的公式了，但是从高斯定理或者安培定理的意义上来说，它确实并不是一个精确的定律；确切地说，它是一条可以很好地适用于很多情况的“经验定律”。你并不会因为找到了反例而获得诺贝尔奖。事实上，当你停下来去琢磨它，你可能有些惊讶，欧姆定律怎么总是成立？毕竟，一个给定的场 E 产生一个力 qE（对一个电荷 q），则根据牛顿第二定律，这个电荷会加速运动。但是如果这个电荷在加速，为什么电流不随时间增大，你维持电场的时间越长电流就增长得越大？与此相反，欧姆定律暗示，一个恒定场会产生一个恒定电流，这也就暗示了一个不变的速度。这不是违背了牛顿定律吗？

不是的，因为我们忘记了当电子通过导线时的频繁碰撞了。这有点像这样：假设你正开车途径一条每个路口都有停车标志的街道，所以，尽管你在两个路口之间均匀加速，但是你被迫在每个街区都重新开始加速。于是，你的平均速度就是一个常数，尽管事实上你一直在加速（除了周期性的突然停车）。如果一个街区的长度是 $\lambda$ ，而你的加速度为 a，行驶过一个街区需要的时间就是

$$
t = \sqrt {\frac {2 \lambda}{a}}
$$

因此平均速度为

$$
v _ {\mathrm{ave}} = \frac {1}{2} a t = \sqrt {\frac {\lambda a}{2}}
$$

但是等一下！这同样不能说明问题！上式说明速度与加速度的平方根成比例，因此电流应该与电场的平方根成比例！这个故事另有转折：事实是，电荷由于它们的热运动已经在以相当快的速度运动。但是热运动速度的方向是随机的，所以平均值为零。我们关心的是净定向漂移速度（drift velocity），它非常之小（习题5.20）。所以碰撞之间的时间实际上要比我们认为的短得多；如果我们为了论证而假设所有电荷在其相邻两次碰撞间隔运动相同的距离 $\lambda$ ，则

$$
t = \frac {\lambda}{v _ {\mathrm{热}}}
$$

因此

$$
v _ {\mathrm{ave}} = \frac {1}{2} a t = \frac {a \lambda}{2 v _ {\mathrm{热}}}
$$

如果每单位体积内有 $n$ 个分子，每个分子中有 $f$ 个自由电子，每个电子电量为 $q$ ，质量为 $m$ ，则电流密度为

$$
\pmb {J} = n f q \pmb {v} _ {\mathrm{ave}} = \frac {n f q \lambda}{2 v _ {\text {热}}} \frac {\pmb {F}}{m} = \left(\frac {n f \lambda q ^ {2}}{2 m v _ {\text {热}}}\right) \pmb {E}\tag{7.6}
$$

我并不断言括号中的量是电导率的精确表示式 $^{2}$ ，但是它确实给出了基本的要素，而且它正确地预言出电导率与漂移电荷的密度成正比，并且（通常情况下）随着温度升高而降低。

作为所有这些碰撞的结果，电场力所做的功被转化成电阻器的热。因为每单位电荷所做的功是 V，而每单位时间流过的电荷是 I，散发的功率为

$$
\boxed {P = V I = I ^ {2} R}\tag{7.7}
$$

这就是焦耳热定律（Joule heating law）。当 $I$ 以安培为单位而 $R$ 以欧姆为单位时，得出的 $P$ 以瓦特为单位（焦耳每秒）。

习题7.1 两个半径分别为 $a$ 和 $b$ 的同心金属球壳，被电导率为 $\sigma$ 的弱导电材料分开，如图7.4a所示。

(a) 如果它们之间保持电势差 $V$ ，从一个球壳流向另一个的电流多大？

(b) 球壳之间的电阻多大?

(c) 注意如果 $b \gg a$ ，外层球壳的半径 (b) 是不相关的。你怎么解释这个事实？利用这个观察结果解决下述问题。设有半径为 $a$ 的两个金属球，被浸没在足够深的海水中并且离得相当远，如图 7.4b 所示，如果两金属球之间的电势差为 $V$ ，求从一个球流向另一个的电流。（这个装置可以用来测量海水的电导率。）

![](images/5891648c09fc4e47a889527b32b8502aa3aeaea66325288191d5c8a06ff61413.jpg)  
a)

![](images/1035b538c44f19929e921d176bfd87b1c16b67c09594ac558882588a9bb404b1.jpg)  
b)  
图7.4

习题 7.2 一个电容器 C 被充电到电势为 $V_{0}$ ；在 t=0 时刻这个电容器与一个电阻 R 连接，并且开始放电，如图 7.5a 所示。

（a）求出电容器极板上的电荷作为时间的函数 $Q(t)$ 。流经电阻器的电流 $I(t)$ 是多少？

（b）电容器中最初存储的能量为多少 [式 (2.55)]？通过积分式 (7.7)，证实电阻释放的热量与电容器损失的能量相等。

现在设想给电容器充电，将电容器（和电阻器）在 t = 0 时刻连接到一个固定电压为 $V_{0}$ 的电池上，如图 7.5b 所示。

(c) 再求出充电时的 $Q(t)$ 和 $I(t)$ 。

(d) 求电池的总能量输出 $\left(\int V_{0}I\mathrm{d}t\right)$ 。确定给电阻器的热量。最终储存在电容中的能量有多大？电池所做的功中有多大部分作为电容器中的能量出现？[注意答案与 R 无关！]

![](images/cd9ab405c27e747f6c9841f8b682fe860f8838186b1d728097caab5463444e62.jpg)

![](images/c976b66f1927c21dd2f2bb4412d24628e8ee7d0e8d6e83e63e5c845dfd9e81dc.jpg)  
图7.5

习题7.3

（a）两块金属物体嵌在导电率为 $\sigma$ 的弱导电材料中，如图 7.6 所示。证明它们之间的电阻与这种布置的电容有关：

$$
R = \frac {\varepsilon_ {0}}{\sigma C}
$$

（b）假设你在1与2之间接上一个电池，并且将它们充电至电势差为 $V_{0}$ 。若之后你断开电池，电荷会逐渐泄漏。证明 $V(t) = V_0\mathrm{e}^{-t / \tau}$ ，并且求出用 $\varepsilon_0$ 和 $\sigma$ 表示的时间常数 $\tau$ 。

![](images/60824a2ce3ab5a8ad3d037a36c85da32f2414f9709bb0ea6a0d5acf9807911ae.jpg)  
图7.6

习题7.4 假设在例题7.2中分隔圆柱的材料的电导率不是均匀的；具体来说， $\sigma(s) = k / s$ ，其中 $k$ 为某个常数。求出两个圆柱之间的电阻。[提示：因为 $\sigma$ 是位置的函数，式(7.5)不再成立，在这个电阻介质中电荷密度不为零，而 $E$ 不会按 $1 / s$ 变化。但是我们确实知道对稳恒电流，流经每个柱面的 $I$ 是相同的。由此着手。]

## 7.1.2 电动势

如果你考虑一个典型的电路（图 7.7）——比如说，一个电池与一个灯泡相连——有一个令人困惑的问题来了：实际中，电流在整个回路中一直都是相同的；情况为什么会是这样？这时唯一明显的驱动力是在电池内部啊。立刻地，你可能会预料在电池内应该产生一个较大的电流而灯中一点电流也没有。那么是谁在其余电路中起着驱动力，而且恰巧这个驱动力在每一段导线中产生完全相同的电流？进一步讲，考虑到在通常导线中电荷以（简直）蜗牛般的速度移动（见习题5.20），为什么电流到达灯泡不需用半个小时呢？所有的电荷是如何知道要同时开始运动的呢？

答案：如果电流在整个电路中不是相同的（例如，开关闭合后的最初一瞬间），那么在某些地方电荷会累积起来，并且——这里是要点——这些累积电荷的电场沿使得电流均匀化的方向。例如，假设流进图7.8中的弯折处的电流比流出的大。那么电荷就在“膝盖”累积起来，这样就产生一个方向背离累积电荷的电场 $^{3}$ 。这个场与流进电流的方向相反（减速电荷）但是增强流出的电流（加速电荷）直到这两个电流相等，此时，电荷不会进一步积累，从而建立起了平衡。这是一个巧妙的系统，可以自动自纠维持电流均匀，而且这个过程进行得非常之快，实际中，你可以放心地假定整个电路中的电流是相同的，甚至在以无线电频率振荡的系统中也可如此。

![](images/fcaec262158218fbbacb5d2bb2500e664a932fc4d4ae5741c8da0842a2c0ab81.jpg)  
图7.7

![](images/ca929962bfab73e2dd3940a5cf1edfaa904c95bae0969c0ac88c23bbe921f350.jpg)  
图7.8

所有这些结果说明在驱动电流遍及电路的过程中其实涉及两个力：源 $f_{s}$ ，其通常是被限制在回路的一部分中（比如说，一节电池）；静电力，它促使电流均匀并且将电源的影响传播到电路的远端：

$$
f = f _ {s} + E\tag{7.8}
$$

产生 $f_{s}$ 的物理原因可以是多种多样的：在电池中是化学力；在压电晶体中机械压力转化为电脉冲；在热电偶中，由温度梯度产生；在光伏电池中是由光照产生的；而在范·德·格若夫（Van de Graff）起电机中，电子被装载在传送带上然后被移除。不论是什么机制，它总的效果是由遍及电路的对 f 的线积分决定的：

$$
\boxed {\mathcal {E} \equiv \oint f \cdot \mathrm{d} l = \oint f _ {s} \cdot \mathrm{d} l}\tag{7.9}
$$

（因为对于静电场 $\oint E\cdot \mathrm{d}l = 0$ ，你使用 $f$ 还是 $f_{s}$ 都没有关系。） $\mathcal{E}$ 被称作电路的电动势（electromotive force），或者emf。这是一个糟糕的术语，因为它根本就不是一个力——它是每单位电荷受到力的积分。有些人更喜欢electromotance（译者注：中文还是翻译为电动势）这个词，但是emf已经如此深入人心以至于我认为我们最好不要改变它。

在一个理想的电动势源中（例如，一节无电阻的电池 $^{4}$ ），电荷受到的合力为零 $[\sigma = \infty$ 代入式 (7.1) 中]，所以 $E = -f_{s}$ 。因此，(a 和 b) 两电极间电势差为

$$
V = - \int_ {a} ^ {b} \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = \int_ {a} ^ {b} \boldsymbol {f} _ {s} \cdot \mathrm{d} \boldsymbol {l} = \oint \boldsymbol {f} _ {s} \cdot \mathrm{d} \boldsymbol {l} = \mathcal {E}\tag{7.10}
$$

（我们可以将积分扩展到整个回路，因为电源之外 $f_{s}=0$ ）。这样，电池的作用就是建立并维持与电动势相等的电势差（例如，一节 6V 电池，保持正极比负极高 6V）。由此产生的静电场驱动电流遍及剩下的电路（但是，注意，在电池内部 $f_{s}$ 驱使电流以相反于 E 的方向流动） $^{5}$ 。

由于是 $f_{s}$ 的线积分，所以 E 可以被解释为电源对每单位电荷所做的功——的确，在某些书中电动势就是用这种方式定义的。但是，正如你将会在下一节中所看到的，这种解释之中有一些微妙的问题，所以我更喜欢用式 (7.9)。

习题7.5 一节电动势为 $\mathcal{E}$ 、内阻为 $r$ 的电池接入一个可变的“负载”电阻 $R$ 。如果想要将尽可能大的功率输送到负载上，你应该选择多大的电阻 $R?$ （当然，你无法改变 $\mathcal{E}$ 和 $r$ 。）

习题7.6 如图7.9所示，一个高度为 $h$ 的矩形导线框的一端放入一个平行板电容器的极板之间，线框平面法向与电场 $\pmb{E}$ 平行。另一端则放在电场基本为零的相当远的外面。这个回路中电动势多大？如果总电阻为 $R$ ，电流为多大？并解释。[警告：这是个有陷阱的问题，所以要小心：如果你创造出了一台永动机，肯定有什么地方是错误的。]

![](images/c5af406b44653f9cc601c64f83e1c067d9db8384834249bd35862ec75c78aa7b.jpg)  
图7.9

## 7.1.3 动生电动势

在上一节中我曾经列出了电动势的若干可能来源，电池是其中最熟悉的。但是我没有提到所有这些中最为常见的一种：发电机（generator）。发电机利用了动生电动势（motional emfs），这种电动势是当你将一根导线移过磁场时产生的。图7.10展示了一台发电机的原理模型。在阴影区有垂直纸面向里的匀强磁场 $B$ ，而电阻器 $R$ 代表任何我们试图驱使电流通过的物体（可能是一个灯泡或一台烤面包机）。如果整个回路以速度 $\pmb{v}$ 被拉向右边，在ab段中的电荷会受到一个磁场力，其垂直分量 $qvB$ 驱动电流以顺时针方向流过回路。电动势为

$$
\mathcal {E} = \oint f _ {\text {磁}} \cdot \mathrm{d} l = v B h\tag{7.11}
$$

其中 $h$ 是线框的宽度。（水平段 $bc$ 和 $ad$ 无贡献，因为这里的力是与导线垂直的。）

注意到你用来计算 $\mathcal{E}$ 的积分[式(7.9)或式(7.11)]是在某个瞬间进行的——拍一张线框的“快照”，如果你喜欢，从这个快照得到结果。这样，对于图7.10中的 $ab$ 段， $\mathrm{d}l$ 是垂直向上的，尽管线框是在向右移动。你不能对此质疑——电动势就是这样定义的——但是搞清楚这一点很重要。

![](images/18645e96fdf961417414ad822dfab735343d516af31bf086818335ed4cc59d0f.jpg)  
图7.10

特别是，尽管磁力是建立电动势的原因，但是它确实没有做任何功——磁力永不做功。那么，是谁提供了加热电阻器的能量呢？答案：拉动线圈的那个人！随着电流流动，ab段的自由电荷除了它们源自线框运动的水平速度v外，还有一个垂直速度（叫它u）。相应地，磁力有一个向左的分量quB。为了抵消这个力，拉动导线的那个人必须对每单位电荷施加向右的力（图7.11）

$$
f _ {\mathrm{拉}} = u B
$$

这个力由导线的结构传递到电荷上。

![](images/1ff9fbe7c97d4adb3a4f04913b998a281f226bc72447cb95c84f6fcb5d3b523b.jpg)  
图7.11

同时，粒子实际上是沿着合速度 w 的方向运动，而它运动的距离是 $(h/\cos\theta)$ 。因此，每单位电荷做的功是

$$
\int \pmb {f} _ {\text {拉}} \cdot \mathrm{d} \pmb {l} = (u B) \left(\frac {h}{\cos \theta}\right) \sin \theta = v B h = \mathcal {E}
$$

（ $\sin \theta$ 来自点积。）于是，正如上面证明的，每单位电荷所做的功与电动势完全相等，尽管积分是沿一条完全不同的路径得出的（图7.12），而且所涉及的是完全不同的力。为了计算电动势你应该在某个时刻沿着回路进行积分，但是为了计算所做的功，你应该跟随一个电荷沿回路的运动； $f_{\mathrm{pull}}$ 对电动势无贡献，因为它与导线垂直，然而 $f_{\mathrm{mag}}$ 对做功也没有

贡献，因为它与电荷的运动垂直 $^{6}$ 。

![](images/d7a8187922bca1dd8823e162536866769c38af875ae98d92514e74e5e8991040.jpg)  
a) 计算 $\varepsilon$ 的积分(在某时刻沿电线)

![](images/235be3e3750410050c67bb3956204d48b7c5e8ba92050cf09e0e998b3d92a313.jpg)  
b) 计算功的积分路径(随电荷沿回路)  
图7.12

有一个特别好的方法来表述运动闭合回路中产生的电动势。令 $\Phi$ 为 $B$ 通过回路的磁通量：

$$
\Phi \equiv \int \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {a}\tag{7.12}
$$

对于图 7.10 中的矩形回路，

$$
\Phi = B h x
$$

当线框向右运动时，通量减少：

$$
\frac {\mathrm{d} \Phi}{\mathrm{d} t} = B h \frac {\mathrm{d} x}{\mathrm{d} t} = - B h v
$$

（这里的负号计入了 $\frac{\mathrm{d}x}{\mathrm{d}t}$ 为负的事实。）而这正是电动势数值[式(7.11)]；显然回路中产生的电动势是通过回路磁通量变化率的负值：

$$
\boxed {\mathcal {E} = - \frac {\mathrm{d} \varPhi}{\mathrm{d} t}}\tag{7.13}
$$

这就是动生电动势的磁通量定则（flux rule）。

除了令人喜欢的简洁性，磁通量定则还有适用于在非匀强磁场中向任意方向移动的非矩形线框的优点；事实上，线框甚至不需要保持固定的形状。

[证明]：图7.13显示了一个在 $t$ 以及一段很短时间 $\mathrm{dt}$ 之后两个时刻的线框。假定我们使用面积 $S$ 计算了 $t$ 时刻的磁通量，而对于 $t + \mathrm{dt}$ 时刻的磁通量，使用包括 $S$ 加上连接线框新老位置的“带子”的面积。于是，磁通量的变化为

$$
\mathrm{d} \varPhi = \varPhi (t + \mathrm{d} t) - \varPhi (t) = \varPhi_ {\text {带子}} = \int_ {\text {带子}} \pmb {B} \cdot \mathrm{d} \pmb {a}
$$

让我们来考虑线框上的一点 P：在 dt 的时间内它移动到了 $P'$ 点。令 v 为导线的速度，而 u 为电荷在导线中运动的速度； $w = v + u$ 为 P 点电荷的合速度。带子上的无限小面元可以写为

$$
\mathrm{d} \boldsymbol {a} = (\boldsymbol {v} \times \mathrm{d} \boldsymbol {l}) \mathrm{d} t
$$

(见图 7.13 中的小图。) 因此

$$
\frac {\mathrm{d} \Phi}{\mathrm{d} t} = \oint \boldsymbol {B} \cdot (\boldsymbol {v} \times \mathrm{d} \boldsymbol {l})
$$

因为 $\boldsymbol{w} = (\boldsymbol{v} + \boldsymbol{u})$ 且 u 平行于 dl，我们也可以将其写作

$$
\frac {\mathrm{d} \varPhi}{\mathrm{d} t} = \oint \boldsymbol {B} \cdot (\boldsymbol {w} \times \mathrm{d} \boldsymbol {l})
$$

现在，标量三重积可以重写为

$$
\boldsymbol {B} \cdot (\boldsymbol {w} \times \mathrm{d} \boldsymbol {l}) = - (\boldsymbol {w} \times \boldsymbol {B}) \cdot \mathrm{d} \boldsymbol {l}
$$

所以

$$
\frac {\mathrm{d} \Phi}{\mathrm{d} t} = - \oint (\boldsymbol {w} \times \boldsymbol {B}) \cdot \mathrm{d} \boldsymbol {l}
$$

但是 $(\pmb{w} \times \pmb{B})$ 是每单位电荷受到的磁场力 $f_{\text{磁}}$ ，所以

$$
\frac {\mathrm{d} \varPhi}{\mathrm{d} t} = - \oint f _ {\text {磁}} \cdot \mathrm{d} l
$$

而这个关于 $f_{\text{磁}}$ 的积分就是电动势

$$
\mathcal {E} = - \frac {\mathrm{d} \varPhi}{\mathrm{d} t}
$$

证毕。

![](images/12101fc5f0b0b18af50e855b17d07b81467b2657a2059c058d337ff4cbd0b629.jpg)

放大的da

图7.13

在电动势的定义 [式 (7.9)] 中存在符号的模糊性：你应该沿着闭合回路的哪个方向来进行积分？在磁通量的定义 [式 (7.12)] 中也有类似的模糊性：什么是 da 的正方向？在应用磁通量定则时，符号的一致性（和往常一样）是由右手定则决定的：如果你的四指方向表示闭合回路的正方向，那么大拇指就表示 da 的方向。如果计算出的电动势是负的，它表示电流沿着闭合回路的负方向流动。

磁通量定则是计算动生电动势的一个有效的捷径。它并未包含任何新的物理——仅仅是洛伦兹力定律。但如果你不小心，可能会导致错误或歧义。磁通量规则假设你有一个单匝环——它可以（连续地）移动、旋转、拉伸或扭曲，但要知道开关、滑动触点或延伸导体允许各种电流路径。一个标准的“磁通量定则佯谬”涉及图7.14的电路。当开关切换（从a到b）时，通过电路的磁通量加倍，但没有动生电动势（没有导体在磁场中移动），而安培计（A）也没有显示有电流通过。

![](images/5c9433fef00ff6386041ba287fa437daa9575e91c529d883a0bb16b1a54a5dbb.jpg)  
图7.14

例题7.4 一个半径为 $a$ 的金属碟以角速度 $\omega$ 绕垂直于圆心的轴在一个方向向上的均匀场 $B$ 中转动。一个电阻的一端连接到轴上，另一端通过滑动接头连接到金属碟的外边缘构成一个回路（图7.15）。求电阻中的电流。

![](images/af067ed7acf65c4fac87263fce57a326075080fdc58f353b6c157411d5cbe8fe.jpg)  
图7.15

[解答] 碟子上距离轴为 s 处的速度为 $v = \omega s$ ，所以每单位电荷受的力为 $f_{磁} = v \times B = \omega s B \hat{s}$ 。因此电动势为

$$
\mathcal {E} = \int_ {0} ^ {a} f _ {\mathrm{磁}} \mathrm{d} s = \omega B \int_ {0} ^ {a} s \mathrm{d} s = \frac {\omega B a ^ {2}}{2}
$$

而电流为

$$
I = \frac {\mathcal {E}}{R} = \frac {\omega B a ^ {2}}{2 R}
$$

例题 7.4（法拉第盘或者法拉第发电机）涉及不能（至少，不能直接）从磁通量定则计算动生电动势。磁通量定则假定了电流是沿着一个定义明确的路径流动的，然而在本题中电流是分布在整个碟子上的，甚至“通过电路的磁通量”意味着什么都不是很清楚。

更加棘手的是涡旋电流的情形。取一大块铝（比如说），并且在一个非匀强磁场附近摇晃它。在材料中会产生电流，而你会感觉到一种“黏滞曳力”——就好像你在拉着这块物质穿过糖浆一样（这就是在动生电动势的讨论中我称作 $f_{拉}$ 的力）。涡流是出了名的难以计算 $^{7}$ ，但是演示起来却很简单且令人印象深刻。你可能已经见过这个典型的实验，一个竖直悬挂的铝盘摆穿过一个磁铁的两极（图 7.16a）。当其进入磁场区域时，铝盘突然开始持续减速。为了确认这是涡流引起的，重复以上演示，但这次使用一个上面切有许多狭缝的圆盘，从而防止大尺度的涡流（图 7.16b）。这次圆盘自由摆动，未受磁场阻碍。

![](images/c8e17288e941cd3d5da8edb0feca572d16aa1a6f3c5959cc7d4f4b66fca5d2d3.jpg)  
a)

图7.16  
![](images/3ee387cb97a39a56e8e45657d7b4209b9601af39e7aefd9ebb21eda818e9777e.jpg)  
b)

习题7.7 一根质量为 $m$ 的金属棒在两个相距 $l$ 的平行导电导轨上无摩擦地滑动（图7.17）。一个电阻 $R$ 连接在两个导轨之间，而一个方向指向纸面内的均匀磁场 $\pmb{B}$ 充满了整个区域。

（a）如果该棒以速率 $v$ 向右运动，电阻中的电流有多大？它向哪个方向流动？

(b) 棒上受到的磁力多大？朝哪个方向？

(c) 如果棒在 $t = 0$ 时刻开始以速率 $v_{0}$ 运动，随后自行滑动，在稍后时刻 $t$ 它的速度是多大？

（d）这根棒的初始动能，毫无疑问，是 $\frac{1}{2} mv_0^2$ 。验证传递到电阻上的能量恰好为 $\frac{1}{2} mv_0^2$ 。

![](images/171d55ff419676b117e2f841cd6811253a46417a99cd0d23ba96325af61a0222.jpg)  
图7.17

习题7.8 一个正方形导线框（边长为 $a$ ）平放在桌子上，它的一边距一条通有电流 $I$ 的长直导线的距离为 $s$ ，如图7.18所示。

(a) 求出穿过线框的 B 的通量;

（b）如果现在有人以速率 $v$ 将线框平直拉离导线，产生的电动势多大？电流朝哪个方向（顺时针或逆时针）流动？

(c) 如果线框是以速率 $v$ 被拉向右边，而不是远离呢？

![](images/4f1bd1cba50a1946a246761de785ef14fa0ebca5a89cd92debd8456f393ea034.jpg)  
图7.18

习题7.9 对一个给定边界线可有无穷多个不同的面与之相匹配，但是，在定义通过一个闭合回路的磁通量 $\varPhi = \int B\cdot \mathrm{d}a$ 时，我从来没有指定应该使用哪一个具体的面。对这个明显的疏忽加以解释。

习题 7.10 在方向向右的匀强磁场 B 中，一个正方形线框（边长为 a）绕垂直轴以角速度 $\omega$ 旋转（图 7.19）。求出这个交流电（alternating current）发电机的 $\mathcal{E}(t)$ 。

习题 7.11 一个由厚铝板剪得的正方形线框的上半部被放置在一个匀强磁场 B 中，在重力作用下下落（图 7.20）。（在这个示意图中，阴影区表示磁场；B 方向指向纸面。）如果磁场为 1.0T（一个相当标准的实验室中的场），求出线框离开磁场区域时的最终速度（以 m/s 为单位）。求出作为时间函数的线框速度。需要多久（以秒为单位）来达到，比如说，90% 的最终速度？如果你在这个回路中剪出一个微小的缝隙，从而破坏了电路，会发生什么？[注：线框的尺寸被消去了；以题中所给单位求出具体数值。]

![](images/0588da14f22d7405b51af7a61c63f8a12f480404106e902763f9f8bb96c36680.jpg)  
图7.19

![](images/3481644246776d8729e46688ad9ce142ea6ca037f67de16651ef869632892dfe.jpg)  
图7.20

## 7.2 电磁感应

## 7.2.1 法拉第定律

迈克尔·法拉第在 1831 年报告了一系列的实验，包括如下描述的三个实验（与真实的历史有一些出入）：

[实验 1]：他向右拉动一个导线框穿过磁场（图 7.21a）。在回路中有电流流动。

[实验 2]：他把磁铁向左移动，保持线圈静止（图 7.21b）。回路中仍有电流出现。

[实验 3]：线框与磁铁均保持静止（图 7.21c），但他改变了磁场的强度（他使用了一块电磁铁，改变线圈中的电流）。再一次，回路中出现了电流。

当然，第一个实验是动生电动势的直接例子，可以很方便地用磁通量定则表示出来：

$$
\mathcal {E} = - \frac {\mathrm{d} \varPhi}{\mathrm{d} t}
$$

我想实验 2 与实验 1 产生完全相同的电动势不会使你感到惊讶——真正重要的是磁铁与回路之间的相对运动。的确，根据狭义相对论，这必须如此。但是法拉第对相对论一无所知，而在经典电动力学中，这一简单的互易性是一种引人注目的巧合。因为如果是回路在运动，是磁力建立了电动势，但是如果回路是静止的，这个力就不可能是磁力了——静止的电荷不受磁力作用。在这个情况下，是什么力在起作用呢？是什么场在对静止电荷施加力呢？当然，电场可以，但是在这个情形下，似乎并不存在任何电场。

![](images/25c5fbc56f0cf1fd33c5fc47c0f18803324724dbbf11ce6fced96eee4fec11bb.jpg)  
图7.21

法拉第产生了一个奇妙的灵感：

一个变化的磁场可以感应出电场。

正是这个“感应” $^{8}$ 出的电场产生了实验2中的电动势 $^{9}$ 。的确，如果电动势同样等于磁通量的变化率的话（正如法拉第从经验中发现的那样），

$$
\mathcal {E} = \oint \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = - \frac {\mathrm{d} \Phi}{\mathrm{d} t}\tag{7.14}
$$

则 $\pmb{E}$ 就与 $\pmb{B}$ 的变化通过等式

$$
\oint \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = - \int \frac {\partial \boldsymbol {B}}{\partial t} \cdot \mathrm{d} \boldsymbol {a}\tag{7.15}
$$

联系了起来。这就是积分形式的法拉第定律（Faraday's law）。我们可以利用斯托克斯定理将其转化为微分形式：

$$
\boxed {\nabla \times \boldsymbol {E} = - \frac {\partial \boldsymbol {B}}{\partial t}}\tag{7.16}
$$

注意在静态的情况下（B 为常数），法拉第定律退化为老定则 $\oint E \cdot dl = 0$ （或者，用微分形式， $\nabla \times E = 0$ ），当然，也必须如此。

在实验 3 中磁场是完全不同的原因引起的变化，但是根据法拉第定律同样会感生出一个电场，从而产生电动势 $-\mathrm{d}\Phi/\mathrm{d}t$ 。的确，我们可以将这三种情况（以及对于它们任意组合的情形）全部概括为一种普适通量定则（universal flux rule）：

不论何时（并且不论什么原因），当通过一个回路的磁通量改变时，都会在回路中出现电动势

$$
\mathcal {E} = - \frac {\mathrm{d} \varPhi}{\mathrm{d} t}\tag{7.17}
$$

很多人将这个称为“法拉第定律”。可能我有点过于挑剔了，但是我觉得这很令人困惑。在式(7.17)中，实际上有两种完全不同的机制，而把这两者都认为是“法拉第定律”有点像说因为同卵双胞胎看起来很像所以我们应该把他们叫作相同的名字。在法拉第的第一个实验中，是洛伦兹力在起作用；电动势是磁力产生的。但是在另外两个实验中是电场（由变化的磁场感应出来的）起的作用。从这点看来，这三个过程都遵守同一个电动势的公式相当令人吃惊。事实上，正是这个“巧合”引导爱因斯坦建立了狭义相对论——他得到了关于经典电动力学中的这个奇妙巧合的更深一层的理解。但是这是属于第12章的故事。同时，我将会为由于磁场改变而感生出的电场保留“法拉第定律”这个术语，但是我不会将实验1视作法拉第定律的一个例子。

例题7.5 一个长为 $L$ 、半径为 $a$ 的长圆柱磁铁带有平行于其轴的均匀磁化强度 $M$ 。该圆柱以恒定速率 $v$ 穿过直径稍大的圆形导线环（图7.22）。将环中感生出来的电动势作为时间的函数画出。

![](images/48f9c4eed97a4f8470f8c3b8036f47614b76b2a9bad51525f87f46b50938f3fe.jpg)  
图7.22

[解答] 圆柱的磁场与长螺线管的一样，其面电流密度为 $K_{\mathrm{b}} = M\hat{\phi}$ 。所以除了在靠近两端处磁场开始分散，圆柱内部的磁场为 $B = \mu_0M$ 。当磁铁远离时，通过环的通量为零；当前端通过环时，磁通量逐渐增加到最大值 $\mu_0M\pi a^2$ ；而当末端通过后，磁通量减小到零（图7.23a）。电动势是 $\Phi$ 对时间的（负的）导数，所以它包括两个峰值，如图7.23b所示。

![](images/7a71bc19b0467244f546d2f9758080f484ab77f96a33bd88c6bb49c415767892.jpg)  
图7.23

追踪法拉第定律中的符号可能真的麻烦。例如，在例题7.5中我们想要知道感生电流沿着环的哪个方向流动。原则上，可以利用右手定则来确定（在图7.22中，我们将向左的 $\Phi$ 称为正的，所以环中电流的正方向当从左边看时是逆时针方向；因为图7.23b中的第一个峰值是负的，第一个电流脉冲以顺时针方向流动，而第二个则为逆时针）。但是有一个方便的定则，叫作楞次定律），它的唯一目的是帮助你正确地得到电流方向10：

自然反抗磁通量的改变。

感生电流将以这样的方向流动，由它产生的磁通量将倾向于抵消原磁通量的变化。（正如在例题7.5中，磁铁的前端进入环中时，磁通量增加，所以环中电流必须产生一个向右的场——因此电流沿顺时针方向流动。）注意，自然状态反抗的是磁通量的变化，而不是磁通量本身（当磁铁的末端离开环，磁通量减少，所以感生电流以逆时针方向流动，试图恢复磁通量）。法拉第感应是一种“惯性”现象：一个导电回路“喜欢”使通过它的通量保持恒定；如果你试图改变通过回路的磁通量，回路作为响应，会产生出一个电流，这个电流的方向是沿着能抵消你的努力的方向。（但不会完全抵消；感生电流产生的磁通量通常只是原通量的很小一个因子。楞次定律告诉你的只是电流的方向。）

例题7.6 “跳环”演示。如果你在一个铁柱上绕一个螺线管线圈（铁在这里是用来加强磁场的），在其顶部放置一个金属环，然后通上电，这个环会在空中跳好几英尺高（图7.24）。为什么？

![](images/c92f3fb1a0619a5dad09354e091d961853b9b1b4e063e8811f68a5d67d3d75f5.jpg)  
图7.24

[解答] 在你接通电流之前，通过环的磁通量为零。接通之后出现了磁通量（在图中向上），而环中产生的电动势导致一个电流（在环中），根据楞次定律，它产生的场的方向倾向于抵消这个新的通量。这意味着环中的电流与螺线管中的电流方向相反。相反的电流相互排斥，所以环飞起来了 $^{11}$ 。

习题 7.12 一个半径为 a 的长螺线管，由一个交变电流驱动，所以内部的场是正弦函数： $B(t) = B_{0} \cos(\omega t) \hat{z}$ 。一个半径为 a/2、电阻为 R 的环形导线线圈，被放置于螺线管内部，并与之同轴。求出回路中作为时间函数的感应电流。

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
例题7.7 一个方向竖直向上的匀强磁场 $B(t)$，位于图7.25的圆形阴影区域中。如果 $B$ 是随时间变化的，感应电场为多大？[解答] $\pmb{E}$ 的方向环绕圆周的切线方向，正如一个带有均匀电流密度的长直导线内部的磁场一样。取一个半径为 $s$ 的安培回路，并应用法拉第定律：$\oint \pmb{E} \cdot \mathrm{d}\pmb{l} = E(2\pi s) = -\frac{\mathrm{d}\Phi}{\mathrm{d}t} = -\frac{\mathrm{d}}{\mathrm{d}t} (\pi s^2 B(t)) = -\pi s^2 \frac{\mathrm{d}B}{\mathrm{d}t}$ 因此 $\pmb{E} = -\frac{s}{2} \frac{\mathrm{d}B}{\mathrm{d}t} \hat{\phi}$
</div>

习题7.13 一个边长为 $a$ 的正方形导线线框，置于 $xy$ 平面的第一象限，并且其中一角在原点处。在这个区域中有一个随时间变化的非匀强磁场 $B(y,t) = ky^3 t^2\hat{z}$ （其中 $\hat{z}$ 为一个常数）。求出回路中的感应电动势。

习题 7.14 作为一个课堂演示，一个短圆柱棒状磁铁从一个大约两米长、半径稍大的垂直铝管中落下。磁铁用了若干秒才到达底部，然而另一个完全一样但未磁化的铁块只用了不到一秒就到达了底部。解释为什么磁铁下落要慢得多 $^{12}$ 。

## 7.2.2 感生电场

法拉第定律将静电场规律 $\nabla \times \mathbf{E} = \mathbf{0}$ 推广到时间相关的情形。 $\pmb{E}$ 的散度仍由高斯定理 $\left(\nabla \cdot \mathbf{E} = \frac{1}{\varepsilon_0}\rho\right)$ 给出。而如果 $\pmb{E}$ 纯粹是法拉第场（完全源于变化磁场， $\rho = 0$ ），则

$$
\nabla \cdot \boldsymbol {E} = 0, \quad \nabla \times \boldsymbol {E} = - \frac {\partial \boldsymbol {B}}{\partial t}
$$

这在数学上与静磁学相同：

$$
\nabla \cdot \boldsymbol {B} = 0, \quad \nabla \times \boldsymbol {B} = \mu_ {0} \boldsymbol {J}
$$

结论: 法拉第感应电场由 $-\frac{\partial B}{\partial t}$ 决定, 正如静磁场由 $\mu_{0}J$ 决定一样。与毕奥-萨伐尔定律 $^{13}$ 类似的公式为

$$
\boldsymbol {E} = - \frac {1}{4 \pi} \int \frac {\left(\partial \boldsymbol {B} / \partial t\right) \times \hat {\boldsymbol {r}}}{r ^ {2}} \mathrm{d} \tau = - \frac {1}{4 \pi} \frac {\partial}{\partial t} \int \frac {\boldsymbol {B} \times \hat {\boldsymbol {r}}}{r ^ {2}} \mathrm{d} \tau\tag{7.18}
$$

进而如果对称性允许，我们可以利用所有与积分形式安培定理有关的技巧 $\left(\oint B\cdot \mathrm{d}l = \mu_0I_{\mathrm{enc}}\right)$ ，只是现在是积分形式的法拉第定律：

$$
\oint \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = - \frac {\mathrm{d} \varPhi}{\mathrm{d} t}\tag{7.19}
$$

通过安培回路的（磁）通量变化率现在扮演了之前 $\mu_0 I_{\mathrm{enc}}$ 的角色。

如果 B 增大，E 从上方看就是沿着顺时针方向的。

![](images/fdd6a5f9d4940594030ee9fd2ab7ff70d7e23fb0b31cd984e59b2633ef4c3ed3.jpg)  
图7.25

例题7.8 线电荷密度为 $\lambda$ 的线电荷被粘在半径为 $b$ 的轮缘上，该轮随后被水平悬挂，如图7.26所示，所以它可以自由转动（那些辐条是用一些不导电物质制作的——可能是木头）。从圆心到半径距离为 $a$ 的区域中，存在一个方向向上的匀强磁场 $B_{0}$ 。现在有人撤去磁场，会发生什么？

![](images/0d78c39407e66388333d1a6bb8c227f3099a19387b6b80c7a28c1deae250ae7b.jpg)  
图7.26

[解答] 变化的磁场会感应出一个电场，方向环绕着轮轴。这个电场施加给轮缘上的电荷一个力，随后轮子开始旋转。根据楞次定律，轮子转动的方向（电流的方向）是其场倾向于恢复朝上的磁通量的方向。因而，从上方看是逆时针方向。法拉第定律用于半径为 $b$ 的环给出

$$
\oint \pmb {E} \cdot \mathrm{d} \pmb {l} = E (2 \pi b) = - {\frac {\mathrm{d} \varPhi}{\mathrm{d} t}} = - \pi a ^ {2} {\frac {\mathrm{d} B}{\mathrm{d} t}}, \quad \text {或者} \quad \pmb {E} = - {\frac {a ^ {2}}{2 b}} {\frac {\mathrm{d} B}{\mathrm{d} t}} {\hat {\phi}}
$$

dl 上的力矩为 $(r \times dF)$ ，或 $b\lambda Edle_{z}$ 。因此，作用在轮子上的总力矩为

$$
N = b \lambda \left(- \frac {a ^ {2}}{2 b} \frac {\mathrm{d} B}{\mathrm{d} t}\right) \oint \mathrm{d} l = - b \lambda \pi a ^ {2} \frac {\mathrm{d} B}{\mathrm{d} t}
$$

而轮子获得的总角动量为

$$
\int N \mathrm{d} t = - \lambda \pi a ^ {2} b \int_ {B _ {0}} ^ {0} \mathrm{d} B = \lambda \pi a ^ {2} b B _ {0}
$$

你撤除磁场的快慢没有关系；轮子的最终角速度都相同。（如果你发现自己在奇怪这个角动量是从哪里来的话，你比我讲的故事超前了！等下一章吧。）

关于这个例子的最后一件事：是电场使轮子旋转起来。为了使你确信这一点，我故意将情况安排成这样，电荷所在之处（轮缘上）的磁场为零。实验者可能告诉你她从未加入任何电场——她做的所有事只是关掉了磁场。但是当她做这件事的时候，一个电场就自动出现了，而正是电场转动了轮子。

现在，我必须提醒你们一个有损法拉第定律众多应用名声的小骗局：电磁感应，当然，只在磁场变化时才能出现，而我们仍在用静磁学的工具（安培定理，毕奥-萨伐尔定律以及其他）来计算这些磁场。原则上讲，任何用这种方式得出的结果都只是近似正确的。但是在实际中，误差通常都是微不足道的，除非场变动得极快，或者是你对离源非常远的场点感兴趣。甚至在一根导线被一把剪子突然剪断的情形（习题7.18），也可以认为是足够静态而应用安培定理求解。这种情况，其中静磁学定律可以被用来计算法拉第定律右边项中的磁场，被称作似稳的。一般来说，只有我们谈到电磁波和辐射时，才需要认真考虑静磁学定律的失效问题。

例题7.9 一根无限长直导线载有缓慢变化的电流 $I(t)$ 。作为距导线距离 $s$ 的函数，求出感应电场 $^{14}$ 。

[解答] 在似稳近似中，磁场为 $(\mu_0 I / 2\pi s)$ ，方向是环绕导线的。正如一个螺线管的 $B$ 场一样，这里 $E$ 的方向与导线轴平行。对于图7.27中的矩形“安培回路”，法拉第定律给出：

$$
\begin{array}{r l} \oint \boldsymbol {E} \cdot \mathrm{d} \boldsymbol {l} = E (s _ {0}) l - E (s) l = & - \frac {\mathrm{d}}{\mathrm{d} t} \int \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {a} \\ = & - \frac {\mu_ {0} l}{2 \pi} \frac {\mathrm{d} I}{\mathrm{d} t} \int_ {s _ {0}} ^ {s} \frac {1}{s ^ {\prime}} \mathrm{d} s ^ {\prime} = - \frac {\mu_ {0} l}{2 \pi} \frac {\mathrm{d} I}{\mathrm{d} t} (\ln s - \ln s _ {0}) \end{array}
$$

这样有

$$
\boldsymbol {E} (s) = \left[ \frac {\mu_ {0}}{2 \pi} \frac {\mathrm{d} I}{\mathrm{d} t} \ln s + K \right] \hat {\boldsymbol {z}}\tag{7.20}
$$

其中 $K$ 是一个常数（这就是说，它与 $s$ 无关——可能仍然是 $t$ 的函数）。 $K$ 的实际值依赖于函数 $I(t)$ 的全部历史——我们会在第10章看到一些例子。

![](images/e3341b0a8ccb997e84fd2c2350b6e7985187197b078919627b70813e732b6ceb.jpg)  
图7.27

式 (7.20) 有一个奇怪的结论，当 $s$ 趋近于无限大时 $E$ 趋向无限大。这不可能是真的……哪里出错了？答案：我们已经越过了似稳近似的极限。正如我们将在第9章中看到的，电磁“信息”以光速传播，而在很远处某时刻的 $\pmb{B}$ 不依赖于此时的电流，而是依赖于某个更早时刻的电流（事实上，

是全部早先时间范围的电流，因为导线上的不同点离场点有不同的距离。）如果 $\tau$ 是 $I$ 发生可观变化所需要的时间，那么似稳近似仅对

(7.21)

时成立，因此式 $(7.20)$ 在极大的s处不适用。

习题7.15 一个半径为 $a$ 、每单位长度匝数为 $n$ 的长螺线管通有一个沿 $\hat{\phi}$ 方向且随时间变化的电流 $I(t)$ 。在似稳近似下，求出距轴 $s$ 处（螺线管内部和外部）的电场（大小和方向）。

习题7.16 一个交变电流 $I = I_0\cos (\omega t)$ 流经一个长直导线，然后沿着一个半径为 $a$ 的同轴导电管流回。

(a) 感应电场指向哪个方向（径向，切向还是纵向）?

(b) 假定当 $s \to \infty$ 时场趋近于零，求 $\pmb{E}(s, t)^{15}$ 。

习题7.17 一个半径为 $a$ 、单位长度带有 $n$ 匝的长螺线管如图7.28所示，被一个电阻为 $R$ 的导线环绕。

(a) 如果螺线管中的电流以一个固定速率变大 $(\mathrm{d}I / \mathrm{d}t = k)$ ，在线框中流动多大的电流？它从哪个方向（左或右）通过电阻？

(b) 如果螺线管中的电流 $I$ 是固定的，但是将螺线圈从线框中抽出（沿左边到达远离线框的地方），通过电阻的总电量是多少？

![](images/abcfc0f06f8ad39f5107967d89476528d2c9a9fb6af44cdde49db8fd2c3d0f64.jpg)  
图7.28

习题7.18 一个边长为 $a$ 、电阻为 $R$ 的正方形线框，位于距离一条通有电流 $I$ 的无限长直导线 $s$ 处（图7.29）。现在有人剪断了导线，所以 $I$ 下降到零。在这个正方形线框中感应电流会朝着哪个方向流动，在这个电流流动过程中通过线框内一给定点的总电量是多少？如果你不喜欢这个剪刀模型，则如下逐渐降低电流：

$$
I (t) = \left\{ \begin{array}{l l} (1 - \alpha t) I, & 0 \leqslant t \leqslant 1 / \alpha \\ 0, & t > 1 / \alpha \end{array} \right.
$$

习题7.19 一个内径为 $a$ 、外径为 $a + w$ 、高为 $h$ 的环形螺线管其横截面为矩形。它共有 $N$ 匝密绕线圈，而电流以固定速率 $(\mathrm{d}I / \mathrm{d}t = k)$ 增长。如果 $w$ 与 $h$ 都远小于 $a$ ，求出距离环形中心上方 $z$ 点的电场。[提示：利用法拉第场与静磁场之间的相似性，并参考例题5.6。]

习题7.20 图7.21b中哪个地方 $\partial B / \partial t$ 不为零？利用法拉第定律和安培定律的相似性（定性）画出电场。

![](images/cea3f3fdc97c3850f2742393b673bfcf5f15aa7b55de53c5fad1b7cb2409c432.jpg)  
图7.29

习题7.21 假设整个空间分布有 $z$ 方向的均匀磁场 $(B = B_0\hat{z})$ 。一个正电荷粒子静止于原点。现在有人关闭磁场，从而感应出电场。该粒子将往哪个方向移动[16]？

## 7.2.3 电感

假设你有两个静止的导线回路（图7.30）。如果你在回路1中通上一个稳定电流 $I_{1}$ 它产生一个磁场 $B_{1}$ 。磁场线的一部分经过回路2；令 $\Phi_2$ 为 $B_{1}$ 通过2的磁通量。实际计算 $B_{1}$ 是比较困难的，但是观察一下毕奥-萨伐尔定律，

$$
\boldsymbol {B} _ {1} = \frac {\mu_ {0}}{4 \pi} I _ {1} \oint \frac {\mathrm{d} \boldsymbol {l} _ {1} \times \hat {\boldsymbol {r}}}{r ^ {2}}
$$

揭示出关于这个场的一个重要事实：它与电流 $I_{1}$ 成正比。因此，通过回路2的磁通量也是如此：

$$
\varPhi_ {2} = \int B _ {1} \cdot \mathrm{d} a _ {2}
$$

这样有

$$
\varPhi_ {2} = M _ {2 1} I _ {1}\tag{7.22}
$$

其中 $M_{21}$ 为比例系数；它被称为两个回路的互感系数（mutual inductance）。

![](images/d07108ae7aebb4025200d3c0836b111216c1e1549d1204c7a4d21a0d02dcae5a.jpg)  
图7.30

对于互感系数，有一个简洁的公式，你可以通过将磁通量用矢势表出然后运用斯托克斯定理得到它：

$$
\Phi_ {2} = \int B _ {1} \cdot \mathrm{d} a _ {2} = \int (\nabla \times A _ {1}) \cdot \mathrm{d} a _ {2} = \oint A _ {1} \cdot \mathrm{d} l _ {2}
$$

现在，根据式(5.66)，

$$
A _ {1} = \frac {\mu_ {0} I _ {1}}{4 \pi} \oint \frac {\mathrm{d} l _ {1}}{r}
$$

因此

$$
\varPhi_ {2} = \frac {\mu_ {0} I _ {1}}{4 \pi} \oint \left(\oint \frac {\mathrm{d} l _ {1}}{r}\right) \cdot \mathrm{d} l _ {2}
$$

显然

$$
M _ {2 1} = \frac {\mu_ {0}}{4 \pi} \oint \oint \frac {\mathrm{d} l _ {1} \cdot \mathrm{d} l _ {2}}{r}\tag{7.23}
$$

这就是纽曼公式（Neumann formula）；它涉及一个二重线积分——一个积分沿着回路1，另一个沿着回路2（图7.31）。它对于实际计算来说并不是非常有用，但是它确实展示出关于互感系数的两个重要的事情：

![](images/58f43b0beff58fc43b7c630094409abac5264fe50ea21e3e145a25cb45b2d387.jpg)  
图7.31

1. $M_{12}$ 完全是一个几何量，仅与两个回路的大小、形状以及相对位置有关。

2. 如果我们交换回路1与2的角色，式(7.23)中的积分不变；因此得出

$$
M _ {2 1} = M _ {1 2}\tag{7.24}
$$

这是一个令人吃惊的结论：不论线圈们的形状及位置，我们在1中接通一个电流 $I$ 时通过2的磁通量与当我们在2中接通相同的电流 $I$ 时通过1的磁通量相同。我们也可以去掉下标，将它们都称作 $M$ 。

例题7.10 如图7.32所示，一个短螺线管（长度为 $l$ ，半径为 $a$ ，每单位长度上有 $n_1$ 匝）位于一个非常长的螺线管的轴上（半径为 $b$ ，每单位长度上有 $n_2$ 匝）。在短螺线管中通有电流 $I$ 。通过长螺线管的磁通量多大？

[解答] 因为内部的螺线管很短，它有一个非常复杂的场；另外，它通过外部螺线管每一匝的磁通量都不相同。用这种方法计算总磁通量会是一件痛苦的任务。但是，如果我们利用互感系数的相同性，这个问题就变得非常简单了。只用从相反的情形考虑：在外部螺线管中接通电流 $I$ ，然后计算通过内部螺线管的磁通量。长螺线管内部的磁场是常数：

$$
B = \mu_ {0} n _ {2} I
$$

$= \frac{1}{n}$ $\sum_{i=1}^{n-1} \sum_{j=1}^{n-1} \sum_{k=1}^{n-1} \sum_{l=1}^{n-1} \sum_{m=1}^{n-1} \sum_{n=1}^{n-1} \sum_{p=1}^{n-1} \sum_{q=1}^{n-1} \sum_{r=1}^{n-1} \sum_{s=1}^{n-1} \sum_{t=1}^{n-1} \sum_{u=1}^{n-1} \sum_{v=1}^{n-1} \sum_{w=1}^{n-1}$

[式(5.59)], 所以通过短螺线管每一个单圈的磁通量为

$$
B \pi a ^ {2} = \mu_ {0} n _ {2} I \pi a ^ {2}
$$

， ， ， ， ， ， ， ， ， 。

![](images/07aac1a938c364b0e0d78da8f3a52562b2ba0e8b056e1bef2ea44ba3a2fb0a10.jpg)  
图7.32

总共有 $n_1l$ 匝，所以通过内部螺线管的总磁通量为

$$
\varPhi = \mu_ {0} \pi a ^ {2} n _ {1} n _ {2} l I
$$

这也就是在短螺线圈中通有电流 $I$ 时通过长螺线圈的磁通量，也就是我们最开始想要得到的结果。顺便提及，在这个情况下，互感系数是

$$
M = \mu_ {0} \pi a ^ {2} n _ {1} n _ {2} l
$$

现在假设你改变回路 1 中的电流。通过回路 2 的磁通量也会相应改变，而法拉第定律表明这个改变的磁通量会在回路 2 中感应出一个电动势：

$$
\mathcal {E} _ {2} = - \frac {\mathrm{d} \varPhi_ {2}}{\mathrm{d} t} = - M \frac {\mathrm{d} I _ {1}}{\mathrm{d} t}\tag{7.25}
$$

[在引用式 (7.22) 时——该式基于毕奥-萨伐尔定律——我暗中假定电流变化得足够慢，以使系统可被认为似稳的。] 这是一件多么惊人的事情：每当你改变回路 1 中的电流，就会有一个感应电流在回路 2 中流动——尽管并不存在任何导线连接它们！

让我们继续考虑，一个变化的电流不仅会在任何附近的回路中感应出电动势，而且会在源回路自身中感应出一个电动势（图 7.33）。再一次，磁场（而且因此磁通量也是）是与电流成正比的：

$$
\Phi = L I\tag{7.26}
$$

其中的比例系数 L 被称为回路的自感系数（self inductance，或者简称为电感）。和 M 一样，它取决于回路的几何性质（大小和形状）。如果电流改变，线圈中感应的电动势就是

$$
\mathcal {E} = - L \frac {\mathrm{d} I}{\mathrm{d} t}\tag{7.27}
$$

电感的度量单位是亨利（H）；一亨利是一伏特秒每安培。

![](images/0e35c6ba074eea99239be4c085f9324ce3141c4519c34149ea5ad57ebd818dcf.jpg)  
图7.33

例题7.11 求出横截面为矩形的环形螺线管的自感系数（内径为 $a$ ，外径为 $b$ ，高为 $h$ ），该螺线管总共有 $N$ 匝线圈。

[解答] 环内部的磁场是 [式 (5.60)]

$$
B = \frac {\mu_ {0} N I}{2 \pi s}
$$

通过一个单匝（图7.34）线圈的磁通量为

$$
\int \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {a} = \frac {\mu_ {0} N I}{2 \pi} h \int_ {a} ^ {b} \frac {1}{s} \mathrm{d} s = \frac {\mu_ {0} N I h}{2 \pi} \ln \left(\frac {b}{a}\right)
$$

总磁通量为这个的 $N$ 倍，所以自感系数[式(7.26)]为

$$
L = \frac {\mu_ {0} N ^ {2} h}{2 \pi} \ln \left(\frac {b}{a}\right)\tag{7.28}
$$

![](images/b73e244e3384ea40b752a087f1841524a8510bdc8ba8b5e94baec60f10694736.jpg)  
图7.34

电感（和电容一样）本质上是一个正值量。楞次定律，由式(7.27)中的负号所要求，使得电动势的方向是朝着反抗电流的任何变化。由于这个原因，它被称为反电动势。不论你何时试图改变导线中的电流，你必须克服这个反电动势。这样，电感在电路中扮演的角色与力学系统中的质量有些相似：L越大，改变电流就越困难，正如质量越大，改变一个物体的速度就越困难一样。

例题7.12 假设当有人突然剪断导线时在回路中有电流 $I$ 流动。电流“瞬间”降到零。这就产生了一个极大的反电动势，因为尽管 $I$ 可能很小，但是 $\mathrm{d}I / \mathrm{d}t$ 很大。这就是为什么你拔出电烙铁或者烤面包机的插头时会经常冒出火花——电磁感应拼命地想要维持电流，甚至不得不跳过电路中的间隙。

当你将电烙铁或者烤面包机的插头插入的时候就没有如此戏剧性的事情发生了。在现在情况下，电感会反抗电流的突然增加，从而产生一个平滑连续的电流增长。例如，假设一节电池（提供一个恒定电动势 $\mathcal{E}_0$ ）被连入一个电阻为 $R$ 、电感为 $L$ 的电路（图7.35）。流过的电流是什么？

[解答] 这个电路中的总电动势是来自电池的 $E_{0}$ 加上来自电感的 $-L(\mathrm{d}I/\mathrm{d}t)$ 。于是，欧姆定律表明 $^{17}$

$$
\mathcal {E} _ {0} - L \frac {\mathrm{d} I}{\mathrm{d} t} = I R
$$

这是 $I$ 作为关于时间函数的一个一阶微分方程。正如你们自己可以轻松导出的，方程的通解为

$$
I (t) = \frac {\mathcal {E} _ {0}}{R} + k \mathrm{e} ^ {- (R / L) t}
$$

其中 $k$ 为由初始条件决定的一个常数。特别的，如果你在 $t = 0$ 时刻闭合开关，所以 $I(0) = 0$ ，那么 $k$ 的值应为 $k = -\mathcal{E}_0 / R$ ，则

$$
I (t) = \frac {\mathcal {E} _ {0}}{R} \left[ 1 - \mathrm{e} ^ {- (R / L) t} \right]\tag{7.29}
$$

在图 7.36 中画出了这个函数。如果电路没有电感，电流会直接跳跃到 $E_{0}/R$ 。在实际中，每个电路都有一定的自感，而电流会渐近逼近 $E_{0}/R$ 。量 $\tau \equiv L/R$ 被称为时间常数；它告诉你电流要花多长时间才能达到其最终值的相当一部分（大约 2/3）。

![](images/7ce553518b0bf8f85bf90ce2d8ce514cc417188d8b53e3546ffbc916e54f7bbf.jpg)  
图7.35

![](images/40816323a05e8031a77e75123cfb7f45fadd51d119e424ff8fd58d0bb516eda3.jpg)  
图7.36

习题7.22 如图7.37所示，一个小导线框（半径为 $a$ ）位于一个大导线框（半径为 $b$ ）的中心上方距离 $z$ 处。两个线框平面平行，且垂直于它们的共同轴线。

(a) 假设在大线框中流有电流 $I$ ，求出通过小线框的磁通量。（小线框是如此之小，以至于你可以认为大线框的磁场基本上是均匀的。）

（b）假设在小线框中通有电流 I，求出通过大线框的磁通量。（小线框很小，你可以将其视为磁偶极子。）

(c) 求出互感系数，并且确认 $M_{12} = M_{21}$ 。

![](images/de370be8ec6e80bcdd08f1744905175e59f57c072344fc7c56164b2b5ad161d9.jpg)  
图7.37

习题7.23 一个边长为 $a$ 的正方形导线框，位于两个相距 $3a$ 的长直导线的正中间，并且它们位于同一平面。（实际上，这两根长导线可以是一个很大的矩形回路的长边，但是两个短边距离如此之远，以至于可以忽略它们。）在这个正方形线框中的一个顺时针流动的电流 $I$ 正在逐渐增大： $\mathrm{d}I / \mathrm{d}t = k$ （一个常数）。求出大回路中的感应电动势。感应电流会朝哪个方向流动？

习题7.24 求出一个半径为 $R$ 、每单位长度带有 $n$ 匝线圈的长直螺线管每单位长度的自感系数。

习题7.25 尝试计算图7.38所示的“发夹形”回路的自感系数。（忽略两端的贡献；磁通量中的绝大部分来自图中的长直部分。）你将碰见一个在很多自感计算中会出现的典型困难。为了得到确切的答案，假定导线有一个极小的半径 $\varepsilon$ ，并且忽略通过导线自身的磁通量。

习题 7.26 一个交变电流 $I(t) = I_{0} \cos(\omega t)$ （振幅 0.50 A，频率 60 Hz）流过一个直导线，该导线沿着一个横截面为矩形的环形螺线管线圈（内径 1.0 cm，外径 2.0 cm，高 1.0 cm，1000 匝）的轴放置。这个环形螺旋管线圈连接有一个 500 Ω 的电阻。

(a) 在似稳近似下，环形螺旋管线圈中会感应出多大的电动势？求出电阻中的电流 $I_{R}(t)$ 。

(b) 计算环形螺线管线圈中由于电流 $I_{R}(t)$ 产生的反电动势。这个反电动势与（a）中的“直接”电动势的振幅比多大？

习题7.27 一个电容 $C$ 被充电到电压为 $V$ ，并且连接到一个电感器 $L$ ，如图7.39所示。在 $t = 0$ 时刻合上开关S。求出电路中作为时间函数的电流。如果将一个电阻 $R$ 与 $C$ 和 $L$ 串联起来，你的答案会如何变化？

![](images/1a31c69f224d918b9d52ea31b71312aad9463bce5c31d985e1140bec884dccf6.jpg)  
图7.38

![](images/61f68e1f97d2b4b7b96b1f10fce1eeeb5c6795e8149004c1afb23de49f5a6a61.jpg)  
图7.39

## 7.2.4 磁场的能量

在一个电路中建立流动的电流需要消耗一定量的能量。我并不是在讨论传递给电阻然后转化为热的能量——只要与电路有关，这就是不可避免的损耗；而它可大可小，取决于你让电流流动多长时间。确切地说，我关心的是你克服反电动势从而使电流流动所必须做的功。这是一个固定量，并且它是可逆的：当你关闭电流时就回收了它。同时它代表了潜藏在电路中能量；正如我们马上就会看到的，它可以被认为是存储在磁场中的能量。

一单位电荷沿着电路运行一周克服反电动势所做的功是 $-\varepsilon$ （这里的负号标明了这是由你克服这个电动势所做的功，而不是电动势所做的功）。每单位时间内流过导线的电荷量是 I。所以每单位时间所做的总功是

$$
\frac {\mathrm{d} W}{\mathrm{d} t} = - \mathcal {E} I = L I \frac {\mathrm{d} I}{\mathrm{d} t}
$$

如果我们从零开始建立电流并将其增大到最终值 I，所做的功（将刚才的方程对时间进行积分）为

$$
\boxed {W = \frac {1}{2} L I ^ {2}}\tag{7.30}
$$

它不取决于我们加大电流用了多长时间，只与回路的几何形状（以 L 的形式）以及最终电流 I 有关。

有一个更漂亮的方式来写出 W，它具有很容易推广到面电流与体电流的优点。回忆通过回路的磁通量 $\Phi$ 与 LI 相等 [式 (7.26)]。另一方面，

$$
\Phi = \int_ {S} \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {a} = \int_ {S} (\nabla \times \boldsymbol {A}) \cdot \mathrm{d} \boldsymbol {a} = \oint_ {P} \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {l}
$$

其中 $P$ 为回路的周长而 $S$ 是以 $P$ 为边界的任意面。这样，

$$
L I = \oint_ {P} \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {l}
$$

因此

$$
W = \frac {1}{2} I \oint \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {l} = \frac {1}{2} \oint (\boldsymbol {A} \cdot \boldsymbol {I}) \mathrm{d} l\tag{7.31}
$$

这个形式到体电流的推广是显而易见的：

$$
W = \frac {1}{2} \int_ {\mathcal {V}} (\boldsymbol {A} \cdot \boldsymbol {J}) \mathrm{d} \tau\tag{7.32}
$$

但是，我们还可以做得更好，将 W 完全用磁场表示：安培定理， $\nabla \times B = \mu_{0} J$ ，使我们可以消去 J：

$$
W = \frac {1}{2 \mu_ {0}} \int \pmb {A} \cdot (\nabla \times \pmb {B}) \mathrm{d} \tau\tag{7.33}
$$

分部积分使可以将对 B 的求导转变为对 A 的求导；特别有，矢量积法则 6 给出

$$
\nabla \cdot (\boldsymbol {A} \times \boldsymbol {B}) = \boldsymbol {B} \cdot (\nabla \times \boldsymbol {A}) - \boldsymbol {A} \cdot (\nabla \times \boldsymbol {B})
$$

所以

$$
\boldsymbol {A} \cdot (\nabla \times \boldsymbol {B}) = \boldsymbol {B} \cdot \boldsymbol {B} - \nabla \cdot (\boldsymbol {A} \times \boldsymbol {B})
$$

因此

$$
\begin{array}{r l} W & = \frac {1}{2 \mu_ {0}} \left[ \int B ^ {2} \mathrm{d} \tau - \int \nabla \cdot (\boldsymbol {A} \times \boldsymbol {B}) \mathrm{d} \tau \right] \\ & = \frac {1}{2 \mu_ {0}} \left[ \int_ {\mathcal {V}} B ^ {2} \mathrm{d} \tau - \oint_ {\mathcal {S}} (\boldsymbol {A} \times \boldsymbol {B}) \cdot \mathrm{d} \boldsymbol {a} \right] \end{array}\tag{7.34}
$$

其中 S 为包围体积 V 的面。

现在，式(7.32)中的积分是对电流占据的整个体积进行的。但是比这个体积大的任何区域也是可以的，因为这个体积之外的区域内 $J$ 为零。在式(7.34)中，我们选取的区域越大，体积分的贡献就越大，而因此面积分的贡献就越小（这是合理的：当面离电流越远时， $A$ 和 $B$ 都会减小）。特别地，如果我们同意在全空间上进行积分，则面积分趋近于零，于是我们就剩下了

$$
\boxed {W = \frac {1}{2 \mu_ {0}} \int_ {\mathrm{全空间}} B ^ {2} \mathrm{d} \tau}\tag{7.35}
$$

从这个结果看, 我们说能量以每单位体积 $\left(B^{2}/2\mu_{0}\right)$ 的量被“存储在磁场中”。这是思考它的一个很好方法, 尽管考虑到式 (7.32) 有些人可能更倾向于说能量是以每单位体积 $\frac{1}{2}(\boldsymbol{A} \cdot \boldsymbol{J})$ 的量存储在电流分布中的。两者之间的差别只是写法的差别; 最重要的量是总能量 $W$ , 而我们将不用担心能量 “位于” 哪里 (可能的任何地方)。

你也许奇怪为什么建立磁场需要能量——毕竟，磁场自身并不做任何功。要点在于在原先并没有磁场的地方建立一个磁场需要磁场的变化，而一个变化的 B 场，根据法拉第定律，会感应出一个电场。后者当然会做功。在开始时不存在 E，而在最后也没有 E；但是在两者之间，当 B 正在建立时，存在 E，而正是为了克服它才需要做功。（你可以明白为什么在回到第五章时我不能计算存储在静磁场中的能量。）正是基于此点，磁场能公式与静电能公式形式上高度相似 $^{18}$ ：

$$
W _ {\mathrm{elec}} = \frac {1}{2} \int (V \rho) \mathrm{d} \tau = \frac {\varepsilon_ {0}}{2} \int E ^ {2} \mathrm{d} \tau\tag{2.43及2.45}
$$

$$
W _ {\mathrm{mag}} = \frac {1}{2} \int (\boldsymbol {A} \cdot \boldsymbol {J}) \mathrm{d} \tau = \frac {1}{2 \mu_ {0}} \int B ^ {2} \mathrm{d} \tau\tag{7.32及7.35}
$$

例题7.13 如图7.40所示，一个长同轴电缆带有电流 $I$ （电流沿着半径为 $a$ 的内圆柱的表面流出，然后沿着半径为 $b$ 的外柱面流回）。求出存储在一段长为 $l$ 的电缆内的能量。

![](images/f2f2732e0cc13b449eb80dd82ce889840c50f5aeb6ff5b8489ee4bd0b50d0db2.jpg)  
图7.40

[解答] 根据安培定理，两个柱面之间的场为

$$
B = \frac {\mu_ {0} I}{2 \pi s} \hat {\phi}
$$

其他地方磁场为零。这样，每单位体积的能量为

$$
\frac {1}{2 \mu_ {0}} \left(\frac {\mu_ {0} I}{2 \pi s}\right) ^ {2} = \frac {\mu_ {0} I ^ {2}}{8 \pi^ {2} s ^ {2}}
$$

因此，在一个长度为 $l$ 、半径为 $s$ 、厚度为 $\mathrm{ds}$ 的柱形壳内的能量为

$$
\frac {\mu_ {0} I ^ {2}}{8 \pi^ {2} s ^ {2}} 2 \pi l s \mathrm{d} s = \frac {\mu_ {0} I ^ {2} l}{4 \pi} \frac {\mathrm{d} s}{s}
$$

从 $a$ 到 $b$ 积分，我们有

$$
W = \frac {\mu_ {0} I ^ {2} l}{4 \pi} \ln \frac {b}{a}
$$

顺便提及，这给出了一种计算同轴电缆自感系数非常简单的方法。根据式(7.30)，能量也可以被写为 $\frac{1}{2} LI^2$ 。比较这两个表达式 $^{19}$ ，

$$
L = \frac {\mu_ {0} l}{2 \pi} \ln \frac {b}{a}
$$

当电流不是沿单一路径，而是分散在一些面上或者体积上时这种计算自感系数方法特别有用。在这种情况下，电流的不同部分可能围有不同的磁通量，而从式(7.26)直接得到自感系数可能会非常棘手；最好由式(7.30)定义L。

习题7.28 求出储存在一个长螺线管（半径 $R$ ，电流 $I$ ，每单位长度 $n$ 匝）中长度为 $l$ 的一段中的能量：

(a) 利用式 (7.30)（你已经在习题 7.24 中求出了 $L$ ）。

(b) 利用式 (7.31)（你在例题 5.12 中已经求出了 A）。

(c) 利用式 (7.35)。

(d) 利用式 (7.34)（选取从半径 $a < R$ 直到 $b > R$ 的圆柱管作为你的积分体积）。

习题 7.29 利用式 (7.35)，计算例题 7.11 中环形螺线管中储存的能量。利用该结果来检验式 (7.28)。

习题7.30 一个长电缆通有沿同一方向且在其（圆形）横截面上均匀分布的电流。电流沿着表面流回（有一层非常薄的绝缘套分开这两个电流）。求出每单位长度的自感系数。

习题7.31 假设图7.41中的电路已经连通了很长一段时间，这时，在时刻 $t = 0$ ，突然把开关S从 $A$ 推到 $B$ ，断开电池。

(a) 在随后任意 $t$ 时刻的电流多大？

(b) 传给电阻的总能量多大?

(c) 证明这个能量与最初存储在电感器中的能量相等。

习题7.32 两个小线框，各有面积 $a_1$ 和 $a_2$ ，两者位移为 $\pmb{\lambda}$ （图7.42）。

(a) 求出它们的互感系数。[提示：将它们当作磁偶极子处理，然后利用式 (5.88)。] 你的式子与式 (7.24) 一致吗？

(b) 假设一个电流 $I_{1}$ 在回路 1 中流动，而我们打算在回路 2 中建立一个电流 $I_{2}$ 。为了保持回路 1 中流动的电流 $I_{1}$ ，必须要克服互感电动势做多少功？依据这个结果，对式 (6.35) 做出评价。

![](images/a9c340ee536258b0cd5f3640ae916d9b66bd46eba90dd4759da811b326d19dea.jpg)  
图7.41

![](images/ecd6a17bb8dc29735d99fa5879bd930ffcca84311ad38188df689280fb2c4c15.jpg)  
图7.42

习题7.33 一个半径为 $R$ 的无限长圆柱带有面密度为 $\sigma$ 的电荷。我们设法将其设置为以最终角速度 $\omega_{\mathrm{f}}$ 绕其轴线旋转，每单位长度需要做多少功？用两种方法做，并比较你的结果：

(a) 寻找圆柱内外（在似稳近似下）磁场和感应电场，用 $\omega, \dot{\omega}$ 和 $s$ （到圆柱轴线的距离）表示。计算需要施加的力矩，由此计算每单位长度需要做的功 $(W = \int N\mathrm{d}\phi)$ ;

(b) 利用式 (7.35) 确定储存在最终磁场中的能量。

## 7.3 麦克斯韦方程组

## 7.3.1 麦克斯韦之前的电动力学

迄今为止，我们已经遇到了下列定律，它们给出了电场和磁场的散度与旋度 $^{20}$ ：

(i) $\nabla \cdot \pmb{E} = \frac{\rho}{\varepsilon_0}$ （高斯定理）

(ii) $\nabla \cdot B = 0$ （没有名字）

(iii) $\nabla \times \pmb{E} = -\frac{\partial\pmb{B}}{\partial t}$ （法拉第定律）

$$
(\mathrm{iv}) \nabla \times \pmb {B} = \mu_ {0} \pmb {J} (\text {安培定律})
$$

这些等式代表着 19 世纪中叶，当麦克斯韦开始他的工作时电磁理论的状况。在那个时代它们并没有被写成如此简洁的形式，但是它们的物理内容是熟悉的。现在，在这些公式中出现了一处致命的矛盾。它与旋度的散度总为零这一早已熟知的法则有关。如果你对第（iii）式计算散度，一切正常：

$$
\nabla \cdot (\nabla \times \boldsymbol {E}) = \nabla \cdot \left(- \frac {\partial \boldsymbol {B}}{\partial t}\right) = - \frac {\partial}{\partial t} (\nabla \cdot \boldsymbol {B})
$$

等式的左边为零，因为旋度的散度为零；由于式（ii），右边也为零。但是当你对式（iv）做同样的事情时，你就会碰到麻烦：

$$
\nabla \cdot (\nabla \times \boldsymbol {B}) = \mu_ {0} (\nabla \cdot \boldsymbol {J})\tag{7.36}
$$

上式左边必须为零，但是一般来说右边不是。对于稳恒电流，J 的散度为零，但是显然，当你超出静磁学的范围，安培定律不可能是正确的。

还有另外一种方式可以看出安培定律对于非稳恒电流注定是失效的。假设我们正在为一个电容器充电（图 7.43）。积分形式的安培定律为

$$
\oint \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {l} = \mu_ {0} I _ {\mathrm{enc}}
$$

我想要将其应用在图中所示的安塔回路上。我如何确定 $I_{\mathrm{enc}}$ ？好吧，让它是流过回路的总电流，或者说，更加精确些，通过以回路为边界的面上的电流。在这个情形下，最简单的面是位于回路所在的平面上——导线穿过这个面，所以 $I_{\mathrm{enc}} = I$ 。这很好——但是如果我取而代之画一个如图7.43所示的气球形的面又会怎样呢？没有电流流经这个面，所以我得出结论 $I_{\mathrm{enc}} = 0!$ 我们在静磁学中从来没有这个问题，因为只有当电荷在某处聚集时（在这个例子中，是在电容器极板上）这个矛盾才会出现。但是对于非稳恒电流来说（比如现在的情况）“一个环围住的电流”是一个不明确的概念，因为它完全取决于你使用哪个面。（如果这对于你来说看起来有点学究气了——“显而易见，应该使用平面”——请记住安培回路可以是一些甚至并不处于同一平面的扭曲形状。）

![](images/9c67ac7252ee114302381ba181c6ad3f18e8cdcb17c91475c387dbd0fb880c96.jpg)  
图7.43

当然，我们并没有权利预期安培定律对于静磁学之外的情况保持成立；毕竟，我们是从毕奥-萨伐尔定律得到它的。但是，在麦克斯韦的时代，没有任何实验上的原因来怀疑安培定律的广泛有效性。这里的缺陷完全是理论上的，而麦克斯韦通过纯粹的理论论证修正了它。

## 7.3.2 麦克斯韦如何修正安培定律

问题在于式 (7.36) 的右边，其应该为零，但是却不是。利用连续性方程 (5.29) 及高斯定理，这个令人不愉快的项可以改写为

$$
\nabla \cdot \boldsymbol {J} = - \frac {\partial \rho}{\partial t} = - \frac {\partial}{\partial t} (\varepsilon_ {0} \nabla \cdot \boldsymbol {E}) = - \nabla \cdot \left(\varepsilon_ {0} \frac {\partial \boldsymbol {E}}{\partial t}\right)
$$

如果我们在安培定律中，把 $\varepsilon_0(\partial E / \partial t)$ 与 $J$ 结合在一起，这样就会正好消除掉多余的散度：

$$
\boxed {\nabla \times \boldsymbol {B} = \mu_ {0} \boldsymbol {J} + \mu_ {0} \varepsilon_ {0} \frac {\partial \boldsymbol {E}}{\partial t}}\tag{7.37}
$$

（麦克斯韦本人对于在安培定律中想要增加这个量有着其他理由。对于他来说，连续性方程的拯救是一个令人高兴的红利，而不是最初的动机。但是现在我们把上面的论证当作一个比麦克斯韦的更令人信服的论证，麦克斯韦的论证建立在现在不足以取信的以太模型上 $^{21}$ 。）

仅就静磁学而言, 这样的一个修正什么都没有改变: 当 E 不变时, 我们仍然有 $\nabla \times B = \mu_{0} J$ 。事实上, 在通常的电磁学实验中, 麦克斯韦的这一项需要与 J 争抢风头, 是很难探测到的——这也就是为什么法拉第和其他人在实验室中都从未发现过它。但是, 正如我们将在第 9 章看到的, 它却在电磁波的传播中扮演着举足轻重的角色。

撇开对安培定律缺陷的弥补，麦克斯韦增添的项有着某种美感：正如一个变化的磁场会感应出一个电场（法拉第定律）那样，于是 $^{22}$ ，

## 一个变化的电场感应出一个磁场

当然，理论上的方便和美学上的一致性都仅是暗示性的——毕竟，也可能存在其他某种方式来修改安培定律。麦克斯韦理论的实际确认到1888年随着赫兹关于电磁波的实验才来到。麦克斯韦将他的额外项称为位移电流（displacement current）：

$$
J _ {\mathrm{d}} \equiv \varepsilon_ {0} \frac {\partial E}{\partial t}\tag{7.38}
$$

[这是一个容易令人误解的名字，因为， $\varepsilon_0(\partial E / \partial t)$ 除了在安培定律中加到 $J$ 上，与电流没有任何关系。]现在让我们来看一看，位移电流是如何解决充电电容器（图7.43）的佯谬的。如果电容器极板距离非常近（我并没有将它们画成那样，但是如果你假设如此，计算会简单得多），那么两极板之间的电场为

$$
E = \frac {1}{\varepsilon_ {0}} \sigma = \frac {1}{\varepsilon_ {0}} \frac {Q}{A}
$$

其中 Q 为极板上的电荷而 A 为它的面积。这样，在两个极板之间

$$
\frac {\partial E}{\partial t} = \frac {1}{\varepsilon_ {0} A} \frac {\mathrm{d} Q}{\mathrm{d} t} = \frac {1}{\varepsilon_ {0} A} I
$$

现在，积分形式的式 (7.37) 表示如下：

$$
\oint \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {l} = \mu_ {0} I _ {\mathrm{enc}} + \mu_ {0} \varepsilon_ {0} \int \left(\frac {\partial \boldsymbol {E}}{\partial t}\right) \cdot \mathrm{d} \boldsymbol {a}\tag{7.39}
$$

如果我们选取平坦表面，那么 E=0 而 $I_{enc}=I$ 。另一方面，如果我们选用气球状的表面，那么 $I_{enc}=0$ ，但是 $\int(\partial E/\partial t)\cdot\mathrm{d}a=I/\varepsilon_{0}$ 。所以对于这两个面，我们得到相同的答案，尽管在第一个情形下它来自传导电流而在第二个情形来自位移电流。

例题7.14 设有两个同心金属球壳（图7.44）。内壳（半径为 $a$ ）带电 $Q(t)$ ，外壳（半径为 $b$ ）带电 $-Q(t)$ 。内外壳之间充满电导率为 $\sigma$ 的导电介质，于是有径向电流：

$$
\boldsymbol {J} = \sigma \boldsymbol {E} = \sigma \frac {1}{4 \pi \varepsilon_ {0}} \frac {Q}{r ^ {2}} \hat {\boldsymbol {r}}, \quad I = - \dot {Q} = \int \boldsymbol {J} \cdot \mathrm{d} \boldsymbol {a} = \frac {\sigma Q}{\varepsilon_ {0}}
$$

这种位形是球对称的，因此磁场必须为零（它唯一可能的指向沿径向，并且 $\nabla \cdot B = 0 \Rightarrow \oint B \cdot \mathrm{d}a = B(4\pi r^2) = 0$ ，于是 $B = 0$ ）。什么？我一直认为电流产生磁场！这不正是毕奥-萨伐尔和安培教导我们的吗？怎么会出现一个 $J$ （电流分布）没有磁场的情况呢？

![](images/b7013690cc2ce45d1d90032c9215713373184d154bcaf5633f520b6c1cc01097.jpg)

[解答] 这不是静态位形： $Q$ 、 $\pmb{E}$ 和 $J$ 都是时间的函数，毕奥-萨伐尔定律和安培定理不适用。位移电流

$$
J _ {\mathrm{d}} = \varepsilon_ {0} \frac {\partial E}{\partial t} = \frac {1}{4 \pi} \frac {\dot {Q}}{r ^ {2}} \hat {r} = - \sigma \frac {Q}{4 \pi \varepsilon_ {0} r ^ {2}} \hat {r}
$$

完全抵消了传导电流[在式(7.37)中]，从而磁场（由 $\nabla \cdot B = 0, \nabla \times B = 0$ 确定）确实是零。

习题7.34 一个半径为 $a$ 的粗导线，其横截面上均匀分布有恒定电流 $I$ 。导线中有一个宽度 $w \ll a$ 的窄间隙，从而形成了一个如图7.45所示的平行板电容器。求出间隙中距离轴 $s < a$ 处的磁场。

![](images/3088ab10353c49adf780b8b1fbf8fbf6b530ec5d456884782ff87152fc42b930.jpg)  
图7.45

习题7.35 先前的问题是一个充电电容器的仿真模型，以避免与电流在极板平面扩散上有关的复杂性。对一个更现实的模型，假设细导线连接到两个极板的中心（图7.46a）。同样，电流 $I$ 是恒定的，电容器的半径为 $a$ ，而极板之间的间距 $w \ll a$ 。假定电流的流动可保证极板上在任何给定时刻有均匀的面电荷，且在 $t = 0$ 时刻电流为零。

![](images/0897327b16ead4f9c851810cbb73ecec08d786017be79672bfc006088797857b.jpg)  
a)

![](images/ef6adeb1d4d0858c67bf30f2083f5f61886c5a844de17dfabbc934836882a55c.jpg)  
图7.46

(a) 求出极板之间作为 $t$ 的函数的电场。

(b) 求出通过位于两极板正中间的平面上半径为 $s$ 的圆的位移电流。将这个圆当作你的“安培闭合回路”，并取回路所围的平面，求出距离轴 $s$ 处的磁场。

(c) 重复（b）的计算，但是这次使用图 7.46b 所示的圆柱面，该面向左延伸穿过极板到电容器之外，右端不闭合。注意通过这个面的位移电流为零，对 $I_{enc}$ 存在有两个贡献 $^{23}$ 。

习题7.36 参见习题7.16，对那个问题正确答案是

$$
\pmb {E} (s, t) = \frac {\mu_ {0} I _ {0} \omega}{2 \pi} \sin (\omega t) \ln \frac {a}{s} \hat {\pmb {z}}.
$$

(a) 求出位移电流密度 $J_{d}$ 。

(b) 将其积分从而得到总位移电流

$$
I _ {\mathrm{d}} = \int J _ {\mathrm{d}} \cdot \mathrm{d} a
$$

(c) 比较 $I_{\mathrm{d}}$ 和 $I_{\circ}$ 。（它们的比率多大？）假设外圆柱面的直径为 $2.0\mathrm{mm}$ ，为了使 $I_{\mathrm{d}}$ 为 $I$ 的 $1\%$ ，频率应该为多高？[这个习题是用来说明为什么法拉第从未发现位移电流，并且为什么通常忽略它们没有问题，除非电流频率极高。]

## 7.3.3 麦克斯韦方程组

在上一节中我们对麦克斯韦方程组进行了最后的修订 $^{4}$ ：

$$
\begin{array}{l l} \text {(i)} \nabla \cdot \boldsymbol {E} = \frac {\rho}{\varepsilon_ {0}} & (\text {高斯定理}) \\ \text {(ii)} \nabla \cdot \boldsymbol {B} = 0 & (\text {没有名字}) \\ \text {(iii)} \nabla \times \boldsymbol {E} = - \frac {\partial \boldsymbol {B}}{\partial t} & (\text {法拉第定律}) \\ \text {(iv)} \nabla \times \boldsymbol {B} = \mu_ {0} \boldsymbol {J} + \varepsilon_ {0} \mu_ {0} \frac {\partial \boldsymbol {E}}{\partial t} & (\text {带有麦克斯韦修正的安培定律}) \end{array}\tag{7.40}
$$

连同力定律，

$$
\boldsymbol {F} = q (\boldsymbol {E} + \boldsymbol {v} \times \boldsymbol {B})\tag{7.41}
$$

它们总结了经典电动力学的全部理论内容 $^{25}$ （除了介质的一些特别性质，我们已经在第4章和第6章遇到）。甚至电荷守恒定律的数学表述连续性方程

$$
\nabla \cdot \boldsymbol {J} = - \frac {\partial \rho}{\partial t}\tag{7.42}
$$

都可以通过对第（iv）式计算散度从麦克斯韦方程组得到。

我已经写出了传统写法的麦克斯韦方程组，这种写法特别强调 E 及 B 的散度与旋度。以这种形式，它们使电场既可以由电荷（ $\rho$ ）也可以由变化的磁场（ $\partial B/\partial t$ ）产生，而磁场既可以由电流（J）也可以由变化电场（ $\partial E/\partial t$ ）产生的观念更加明显。事实上，这也许有一点令人误解，因为归根结底， $\partial B/\partial t$ 与 $\partial E/\partial t$ 本身也是由电荷和电流产生的。我认为

将方程组写作

$$
\left. \begin{array}{l l} \text {(i)} \nabla \cdot \boldsymbol {E} = \frac {\rho}{\varepsilon_ {0}} & \quad \text {(iii)} \nabla \times \boldsymbol {E} + \frac {\partial \boldsymbol {B}}{\partial t} = 0 \\ \text {(ii)} \nabla \cdot \dot {\boldsymbol {B}} = 0 & \quad \text {(iv)} \nabla \times \boldsymbol {B} - \varepsilon_ {0} \mu_ {0} \frac {\partial \boldsymbol {E}}{\partial t} = \mu_ {0} \boldsymbol {J} \end{array} \right\}\tag{7.43}
$$

从逻辑上来说更为可取，其中场（E 和 B）在左边而源（ $\rho$ 和 J）在右边。这种写法强调所有的电磁场最终都可以归因于电荷与电流。麦克斯韦方程组告诉我们电荷如何产生场；而另一方面，力定律告诉我们场如何影响电荷。

## 习题7.37 假设

$$
\pmb {E} (\pmb {r}, t) = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r ^ {2}} \theta (v t - r) \hat {\pmb {r}}; \quad \pmb {B} (\pmb {r}, t) = \mathbf {0}
$$

( $\theta$ 函数是在习题 1.46b 中定义的。) 证明这些场满足所有的麦克斯韦方程，并且确定 $\rho$ 和 J。描述产生这些场的物理情境。

## 7.3.4 磁荷

麦克斯韦方程组存在一种令人喜欢的对称性；在 $\rho$ 和 $J$ 为零的自由空间中，这种对称性尤其显著：

$$
\left. \begin{array}{l} {\mathrm{(i)} \nabla \cdot \pmb {E} = 0} \\ {\mathrm{(ii)} \nabla \cdot \pmb {B} = 0} \end{array} \right. \qquad \left. \begin{array}{l} {\mathrm{(iii)} \nabla \times \pmb {E} = - \frac {\partial \pmb {B}}{\partial t}} \\ {\mathrm{(iv)} \nabla \times \pmb {B} = \varepsilon_ {0} \mu_ {0} \frac {\partial \pmb {E}}{\partial t}} \end{array} \right\}
$$

如果你将 E 替换为 B，而将 B 换为 $-\varepsilon_{0}\mu_{0}E$ ，第一对方程就会转变为第二对方程，反之亦然。不过，E 与 B 之间的这种对称性 $^{26}$ 却被高斯定理中的电荷项以及安培定律中的电流项所破坏。你不由自主地会对为什么相应量在 $\nabla \cdot B = 0$ 和 $\nabla \times E = -\partial B/\partial t$ 中是“缺失的”而感到奇怪。如果我们有

$$
\left. \begin{array}{l l} {\mathrm{(i)} \nabla \cdot \boldsymbol {E} = \frac {\rho_ {\mathrm{e}}}{\varepsilon_ {0}}} & {\mathrm{(iii)} \nabla \times \boldsymbol {E} = - \mu_ {0} \boldsymbol {J} _ {\mathrm{m}} - \frac {\partial \boldsymbol {B}}{\partial t}} \\ {\mathrm{(ii)} \nabla \cdot \boldsymbol {B} = \mu_ {0} \rho_ {\mathrm{m}}} & {\mathrm{(iv)} \nabla \times \boldsymbol {B} = \mu_ {0} \boldsymbol {J} _ {\mathrm{e}} + \varepsilon_ {0} \mu_ {0} \frac {\partial \boldsymbol {E}}{\partial t}} \end{array} \right\}\tag{7.44}
$$

又会怎样？此时 $\rho_{m}$ 代表磁“荷”的密度，而 $\rho_{e}$ 是电荷的密度； $J_{m}$ 将会是磁荷流，而 $J_{e}$ 是电荷流。这两种荷都应该是守恒的：

$$
\nabla \cdot \boldsymbol {J} _ {\mathrm{m}} = - \frac {\partial \rho_ {\mathrm{m}}}{\partial t}, \quad \text {以及} \quad \nabla \cdot \boldsymbol {J} _ {\mathrm{e}} = - \frac {\partial \rho_ {\mathrm{e}}}{\partial t}\tag{7.45}
$$

前一个式子来自对（iii）计算散度，后一个来自对（iv）取散度。

从某种意义上说，麦克斯韦方程组希望磁荷存在——它将会很完美地融合进来。但是，尽管经过了努力寻找，没有一个人曾经发现过任何磁荷 $^{27}$ 。就我们目前所知而言， $\rho_{m}$ 处处为零，而 $J_{m}$ 也是如此；B与E并非处于同等地位：对于E存在静止源（电荷）但是B不存在。（这反映在磁多极矩展开中没有单极项，而磁偶极子由电流环而不是由分开的北极和南极构成这些事实上。）显然，上帝并没有创造磁荷。（顺便提及，在量子电动力学中，磁荷不存在远非仅仅是美学上的遗憾：狄拉克证明，磁荷的存在将会解释为什么电荷是量子化的。见习题8.19。）

习题7.38 假设磁荷（ $q_{\mathrm{m}}$ ）的“库仑定律”写作

$$
\pmb {F} = \frac {\mu_ {0}}{4 \pi} \frac {q _ {\mathrm{m} _ {1}} q _ {\mathrm{m} _ {2}}}{r ^ {2}} \hat {\pmb {r}}\tag{7.46}
$$

给出一个单极子 $q_{m}$ 以速度 v 通过电场 E 和磁场 B 时的力定律 $^{28}$ 。

习题7.39 设想一个磁单极子 $q_{\mathrm{m}}$ 通过一个自感系数为 $L$ 的无电阻回路。在回路中会感应出多大的电流29？

## 7.3.5 介质中的麦克斯韦方程组

式 (7.40) 形式的麦克斯韦方程组其本身是完备且正确的。但是，当你处理那些经过电极化或者磁极化的材料时，存在一个更方便的形式来表述它们。对于内部极化的介质来说，会有“束缚”电荷和电流的积聚，对于这种积聚你不能施加直接控制。把麦克斯韦方程组改写为与那些我们直接控制的源（“自由”电荷与电流）有明确关系的形式将会很惬意。

在静场情形下，我们已经学过电极化强度 $P$ 产生束缚电荷密度[式(4.12)]

$$
\rho_ {\mathrm{b}} = - \nabla \cdot P\tag{7.47}
$$

同样的，磁极化强度（或者“磁化强度”）导致束缚电流[式(6.13)]

$$
\boldsymbol {J} _ {\mathrm{b}} = \nabla \times \boldsymbol {M}\tag{7.48}
$$

在非静态情形中，只有一个新特性需要考虑：电极化强度的任何变化都涉及（束缚）电荷的流动（称其为 $J_{\mathrm{p}}$ ），该电流必须包括在总电流中。假定我们考察一小块极化材料（图7.47）。极化导致在其中一端上的电荷密度 $\sigma_{\mathrm{b}} = P$ ，而在另一端为 $-\sigma_{\mathrm{b}}[$ 式(4.11)]。如果现在 $P$ 变大了一点，两端上的电荷也相应增多，从而带来了净电流

$$
\mathrm{d} I = \frac {\partial \sigma_ {\mathrm{b}}}{\partial t} \mathrm{d} a _ {\perp} = \frac {\partial P}{\partial t} \mathrm{d} a _ {\perp}
$$

因此该电流密度为

$$
J _ {\mathrm{p}} = \frac {\partial P}{\partial t}\tag{7.49}
$$

![](images/40c596178cc20f4bf65f669f43121886293cedafcc3ba00c342c4af7bb7f6a5a.jpg)  
图7.47

这个极化电流（polarization current）与束缚电流 $J_{b}$ 没有任何关系。后者与材料的磁化有关，并且涉及电子的自旋与轨道运动；与此相反， $J_{p}$ 是当电极化强度改变时电荷直线运动的结果。如果 P 指向右边并且正在变大，那么每个正电荷都向右移动一点而负电荷向左；其累积效应就是极化电流 $J_{p}$ 。我们应该检查式 (7.49) 与连续性方程是否保持一致：

$$
\nabla \cdot \boldsymbol {J} _ {\mathrm{p}} = \nabla \cdot \frac {\partial \boldsymbol {P}}{\partial t} = \frac {\partial}{\partial t} (\nabla \cdot \boldsymbol {P}) = - \frac {\partial \rho_ {\mathrm{b}}}{\partial t}
$$

是的：连续性方程是满足的；事实上， $J_{p}$ 对于保障束缚电荷的守恒是重要的。（顺便提及，一个变化的磁化强度并不会导致任何与此类似的电荷或者电流积累。当然，束缚电流 $J_{b} = \nabla \times M$ 会应 M 的改变而变化，但是仅此而已。）

考虑到所有这些，总的电荷密度可以被分为两个部分：

$$
\rho = \rho_ {\mathrm{f}} + \rho_ {\mathrm{b}} = \rho_ {\mathrm{f}} - \nabla \cdot P\tag{7.50}
$$

而电流密度分为三个部分：

$$
\boldsymbol {J} = \boldsymbol {J} _ {\mathrm{f}} + \boldsymbol {J} _ {\mathrm{b}} + \boldsymbol {J} _ {\mathrm{p}} = \boldsymbol {J} _ {\mathrm{f}} + \nabla \times \boldsymbol {M} + \frac {\partial \boldsymbol {P}}{\partial t}\tag{7.51}
$$

高斯定理现在可以写为

$$
\nabla \cdot \boldsymbol {E} = \frac {1}{\varepsilon_ {0}} \left(\rho_ {\mathrm{f}} - \nabla \cdot \boldsymbol {P}\right)
$$

或者

$$
\nabla \cdot \boldsymbol {D} = \rho_ {\mathrm{f}}\tag{7.52}
$$

其中，和静态情形中的一样， $D$ 由下式给出：

$$
\pmb {D} \equiv \varepsilon_ {0} \pmb {E} + \pmb {P}\tag{7.53}
$$

同时，安培定律（带有麦克斯韦项的）变为

$$
\nabla \times \boldsymbol {B} = \mu_ {0} \left(\boldsymbol {J} _ {\mathrm{f}} + \nabla \times \boldsymbol {M} + \frac {\partial \boldsymbol {P}}{\partial t}\right) + \mu_ {0} \varepsilon_ {0} \frac {\partial \boldsymbol {E}}{\partial t}
$$

或者

$$
\nabla \times \boldsymbol {H} = \boldsymbol {J} _ {\mathrm{f}} + \frac {\partial \boldsymbol {D}}{\partial t}\tag{7.54}
$$

其中，和以前一样，

$$
\pmb {H} \equiv \frac {1}{\mu_ {0}} \pmb {B} - \pmb {M}\tag{7.55}
$$

法拉第定律和 $\nabla \cdot B = 0$ 未被我们将电荷和电流分为自由及束缚部分所影响，因为它们不涉及 $\rho$ 或者 J。

于是，以自由电荷和自由电流表示的麦克斯韦方程组为

$$
\boxed { \begin{array}{l l} (\mathrm{i}) \nabla \cdot \boldsymbol {D} = \rho_ {\mathrm{f}} & (\mathrm{iii}) \nabla \times \boldsymbol {E} = - \frac {\partial \boldsymbol {B}}{\partial t} \\ (\mathrm{ii}) \nabla \cdot \boldsymbol {B} = 0 & (\mathrm{iv}) \nabla \times \boldsymbol {H} = \boldsymbol {J} _ {\mathrm{f}} + \frac {\partial \boldsymbol {D}}{\partial t} \end{array} }\tag{7.56}
$$

有些人将这些式子当作“真正的”麦克斯韦方程组，但是请明白它们绝不比式(7.40)更加“普适”；它们只不过说明将电荷和电流分为自由和非自由部分很方便。而且它们有混合记号的缺点，因为它们包括 $E$ 和 $D$ 两者，也包括 $B$ 和 $H$ 两者。因此，它们必须由合适的本构关系（constitutive relations）所补充，给出由 $E$ 和 $B$ 表示的 $D$ 和 $H$ 。这些关系依赖于材料的本质；对于线性介质

$$
P = \varepsilon_ {0} \chi_ {\mathrm{e}} E, \quad \text {而} M = \chi_ {\mathrm{m}} H\tag{7.57}
$$

所以

$$
\pmb {D} = \varepsilon \pmb {E}, \quad \text {而} \quad \pmb {H} = {\frac {1}{\mu}} \pmb {B}\tag{7.58}
$$

其中 $\varepsilon \equiv \varepsilon_{0}(1 + \chi_{\mathrm{e}})$ 而 $\mu \equiv \mu_{0}(1 + \chi_{\mathrm{m}})$ 。顺便提及，你会想起来 D 被称为电“位移”矢量：这就是为什么安培/麦克斯韦方程（iv）中的第二项被称为位移电流（displacement current）。在此背景下，

$$
\boldsymbol {J} _ {\mathrm{d}} \equiv \frac {\partial \boldsymbol {D}}{\partial t}\tag{7.59}
$$

习题7.40 海水在 $\nu = 4.0 \times 10^{8}\mathrm{Hz}$ 的频率下的介电常数为 $\varepsilon = 81\varepsilon_0$ ，磁导率为 $\mu = \mu_0$ ，电阻率为 $\rho = 0.23\Omega \cdot \mathrm{m}$ 。传导电流与位移电流之间的比率为多大？[提示：考虑一个浸泡在海水中由电压 $V_{0} \cos(2\pi\nu t)$ 驱动的平行板电容器。]

## 7.3.6 边界条件

一般来讲, 在两种不同介质之间的边界处, 或者在带有电荷密度 $\sigma$ 或电流密度 $K$ 的界面处, $E, B, D$ 和 $H$ 是不连续的。这种不连续性的具体形式可以从麦克斯韦方程组 (7.56) 的积分形式推导出来:

(i) $\oint_{\mathcal{S}} \boldsymbol{D} \cdot \mathrm{d}\boldsymbol{a} = Q_{\mathrm{fenc}}$ (ii) $\oint_{\mathcal{S}} \boldsymbol{B} \cdot \mathrm{d}\boldsymbol{a} = 0$ 在任意闭合面 $\mathcal{S}$ 上

(iii) $\oint_{\mathcal{P}}\pmb {E}\cdot \mathrm{d}\pmb {l} = -\frac{\mathrm{d}}{\mathrm{d}t}\int_{\mathcal{S}}\pmb {B}\cdot \mathrm{d}\pmb {a}$ (iv） $\oint_{\mathcal{P}}\pmb {H}\cdot \mathrm{d}\pmb {l} = I_{\mathrm{fenc}} + \frac{\mathrm{d}}{\mathrm{d}t}\int_{\mathcal{S}}\pmb {D}\cdot \mathrm{d}\pmb {a}$ 对于以闭合回路 $\mathcal{P}$ 为边界的任意曲面 $S$

将式（i）应用到一个微小扁高斯盒上，这个小盒在界面的两侧都只是略微延伸到材料中，我们得到（图7.48）：

$$
\boldsymbol {D} _ {1} \cdot \boldsymbol {a} - \boldsymbol {D} _ {2} \cdot \boldsymbol {a} = \sigma_ {\mathrm{f}} a
$$

（a 的正方向是从 2 指向 1 的。当盒的厚度趋近于零时，侧边无贡献，也没有任何体电荷密度。）这样，D 的垂直于界面的分量是不连续的：

$$
\boxed {D _ {1} ^ {\perp} - D _ {2} ^ {\perp} = \sigma_ {\mathrm{f}}}\tag{7.60}
$$

同样的论证，应用到方程（ii）上，有

$$
\boxed {B _ {1} ^ {\perp} - B _ {2} ^ {\perp} = 0}\tag{7.61}
$$

![](images/b7b7b3593aa8481cc95ba481d7ff49d00cebc5b5505868d78b9f5dcff31f819a.jpg)  
图7.48

至于式（iii），应用一个横跨界面的非常细的安培回路可得

$$
\boldsymbol {E} _ {1} \cdot \boldsymbol {l} - \boldsymbol {E} _ {2} \cdot \boldsymbol {l} = - \frac {\mathrm{d}}{\mathrm{d} t} \int_ {\mathcal {S}} \boldsymbol {B} \cdot \mathrm{d} \boldsymbol {a}
$$

但是当回路的宽度趋近于零时，磁通量为零。（以相同的理由，我已经去掉了回路两端对于 $\oint E\cdot \mathrm{d}l$ 的贡献。）因此，

$$
\boxed {E _ {1} ^ {\parallel} - E _ {2} ^ {\parallel} = 0}\tag{7.62}
$$

也就是说， $E$ 平行于界面的分量在界面处是连续的。同样的理由，（iv）意味着

$$
\boldsymbol {H} _ {1} \cdot \boldsymbol {l} - \boldsymbol {H} _ {2} \cdot \boldsymbol {l} = I _ {\mathrm{f} _ {\mathrm{enc}}}
$$

其中 $I_{\mathrm{fenc}}$ 是通过安培回路的自由电流。体电流密度没有贡献（在无限小宽度的极限下），但是面电流可有。事实上，如果 $\hat{\pmb{n}}$ 为垂直于界面的单位向量（从2指向1），那么 $(\hat{\pmb{n}} \times \pmb{l})$ 是安培回路的法线方向（图7.49），于是

$$
I _ {\mathrm{f} _ {\mathrm{enc}}} = K _ {\mathrm{f}} \cdot (\hat {n} \times l) = (K _ {\mathrm{f}} \times \hat {n}) \cdot l
$$

因此

$$
\boxed {\boldsymbol {H} _ {1} ^ {\parallel} - \boldsymbol {H} _ {2} ^ {\parallel} = \boldsymbol {K} _ {\mathrm{f}} \times \hat {\boldsymbol {n}}}\tag{7.63}
$$

所以 $\pmb{H}$ 的平行分量是不连续的，之差为一个与自由面电流密度成比例的量。

![](images/c8643225860ab22af3d27594f23a45d850694a6dddfc70a4467e094bc3830740.jpg)  
图7.49

式 (7.60)～式 (7.63) 是电动力学的普适边界条件。在线性介质的情形下，它们可以表示为仅与 E 和 B 有关：

$$
\varepsilon_ {1} E _ {1} ^ {\perp} - \varepsilon_ {2} E _ {2} ^ {\perp} = \sigma_ {\mathrm{f}}
$$

$$
\boldsymbol {E} _ {1} ^ {\parallel} - \boldsymbol {E} _ {2} ^ {\parallel} = \mathbf {0}
$$

$$
B _ {1} ^ {\perp} - B _ {2} ^ {\perp} = 0
$$

$$
\frac {1}{\mu_ {1}} B _ {1} ^ {\parallel} - \frac {1}{\mu_ {2}} B _ {2} ^ {\parallel} = K _ {\mathrm{f}} \times \hat {\boldsymbol {n}}\tag{7.64}
$$

特别有，如果在界面上没有自由电荷或自由电流，那么
(i) $\varepsilon_{1}E_{1}^{\perp}-\varepsilon_{2}E_{2}^{\perp}=0$ (iii) $E_{1}^{\parallel}-E_{2}^{\parallel}=0$ (ii) $B_{1}^{\perp}-B_{2}^{\perp}=0$ (iv) $\frac{1}{\mu_{1}}B_{1}^{\parallel}-\frac{1}{\mu_{2}}B_{2}^{\parallel}=0$

(7.65)

正如我们将会在第 9 章看到的，这些方程是反射和折射理论的基础。

## 第 7 章补充习题

!习题7.41 两个半径都为 $a$ 的长直铜管之间保持距离 $2d$ （图7.50）。其中一个电势为 $V_{0}$ ，另一个电势为 $-V_{0}$ 。铜管周围的空间充满了均匀电导率为 $\sigma$ 的弱导电材料。求出从一个铜管流向另一个铜管的每单位长度上的电流。[提示：参考习题3.12。]

![](images/cbc5480570da070a55f933c7a6abe11512dc2610a66ac614d1252f0ea4d9f9e2.jpg)  
图7.50

!习题 7.42 一个可以实际计算出电流的静电场 E 的罕见情形如下所述 $^{30}$ ：设想一个无限长圆柱形薄板，其电阻率均匀且半径为 a。如图 7.51 所示，一个位于 $\phi = \pm\pi$ 处的狭缝（与电池相对应）被保持在电势 $\pm V_{0}/2$ ，在圆柱表面上流有稳恒电流。于是，根据欧姆定律，

$$
V (a, \phi) = \frac {V _ {0} \phi}{2 \pi} \quad (- \pi <   \dot {\phi} <   + \pi)
$$

（a）利用柱坐标下的分离变量法，求出圆柱内部和圆柱外部的 $V(s,\phi)$ 。[答案： $(V_0 / \pi)\arctan [(s\sin \phi) /$

$$
(a + s \cos \phi) ], s <   a; (V _ {0} / \pi) \arctan [ (a \sin \phi) / (s + a \cos \phi) ], s > a ]
$$

(b) 求出圆柱面上的面电荷密度。[答案： $(\varepsilon_{0}V_{0}/\pi a)\tan(\phi/2)$ ]

![](images/8be715d01004fd57aa2272b4b9e2b2bb8d68f04f70549d0a93394e699d14e040.jpg)  
图7.51

习题7.43 一个带有稳恒电流 $I$ 的长直导线外部的磁场为

$$
\boldsymbol {B} = \frac {\mu_ {0}}{2 \pi} \frac {I}{s} \hat {\phi}
$$

导线内部的电场是匀强的：

$$
\pmb {E} = \frac {I \rho}{\pi a ^ {2}} \hat {\pmb {z}}
$$

其中 $\rho$ 为电阻率而 $a$ 为导线半径（见例题7.1及7.3）。问题：导线外部的电场是什么样的 $^{31}$ ？答案取决于你如何使电路闭合。假设电流沿着一个半径为 $a$ 的导电理想的接地同轴圆柱面流回（图7.52）。在 $a < s < b$ 的区域中，电势 $V(s,z)$ 满足拉普拉斯方程，并有边界条件

$$
\text {(i)} V (a, z) = - \frac {I \rho z}{\pi a ^ {2}}; \quad \text {(ii)} V (b, z) = 0
$$

这并不足以得到答案——我们还需要明确两端处的边界条件（尽管对于一根长导线这关系不大）。在文献中通常无视这里的含糊不清，简单地断言（直截了当地） $V(s,z)$ 与z成比例： $V(s,z)=zf(s)$ 。根据这一假设：

(a) 求出 $f(s)$ 。

(b) 求出 $E(s,z)$ 。

(c) 计算导线表面上的面电荷密度 $\sigma(z)$ 。

[答案： $V = (-Iz\rho/\pi a^{2})[\ln(s/b)/\ln(a/b)]$ ，这是一个很奇特的结果，因为 $E_{s}$ 和 $\sigma(z)$ 并非如同在真正的无限长直导线的情形中我们理所当然期望的那样与 z 无关。]

![](images/29812a4ef7a0c422aac541d563ca43c9686f9e191b7767ce6fe7da4f037397eb.jpg)  
图7.52

习题7.44 在理想导体（perfect conductor）中，电导率无穷大，所以 $E = 0$ [式(7.3)]，任何净电荷都位于导体表面上（正如同在静电学情形中，位于非理想导体的表面那样）。

(a) 证明理想导体内部磁场是恒定的 $(\partial B / \partial t = 0)$ 。

(b) 证明通过理想导电回路的磁通量是常数。

超导体（superconductor）是一种理想导体，但具有内部的（常数）B事实上为零的特殊性质。[这里的“磁通排斥”被称为迈斯纳效应（Meissner effect） $^{32}$ 。]

(c) 证明超导体中的电流被限制在表面上。

(d) 超导性在高于某个确定的临界温度 $(T_{\mathrm{c}})$ 时消失，这个温度对于不同的材料是不同的。假设你有一个温度高于其临界温度的球（半径 $a$ ），你再将它保持其在一个均匀磁场 $B_0\hat{z}$ 中并逐渐将其冷却到低于 $T_{\mathrm{c}}$ 的温度。作为极角 $\theta$ 的函数，求出感应面电流密度 $\pmb{K}$ 。

习题 7.45 一个超导性（习题 7.44）为人所熟知的演示是，在一块超导材料上方悬浮着一块磁铁。这个现象可以利用镜像法分析 $^{33}$ 。将磁铁视为一个理想偶极子 m，该偶极子在原点上方 z 处（并且限制其方向沿 z 方向），然后认为超导体占据了 xy 平面以下的整个半空间。由于迈斯纳效应，对于 $z \leqslant 0$ 处，而且因为 B 是无散度的，法线方向（z）分量是连续的，所以在界面的稍上方 $B_{z} = 0$ 。此边界条件可由镜像配置得到满足，即在 -z 处放置一个相同的偶极子作为超导体的替身；这两个不同的安排在 z > 0 区域产生相同的磁场。

(a) 镜像偶极子应该指向哪个方向 $(+z$ 还是 $-z)$ ?

（b）求出由于超导体上的感应电流而产生的施加在磁铁上的力（这也就是说，由镜像偶极子产生的力）。将其设定为与 $Mg$ 相等（其中 $M$ 是磁铁的质量），从而得到磁铁将会“悬浮”的高度。[提示：参考习题6.3。]

(c) 超导体表面（ $xy$ 平面）上的感应电流可以由关于 $\pmb{B}$ 切向分量的边界条件 [式 (5.76)] 得到： $\pmb{B} = \mu_0(\pmb{K} \times \hat{\pmb{z}})$ 。利用你通过镜像法得到的场，证明

$$
K = - \frac {3 m r h}{2 \pi \left(r ^ {2} + h ^ {2}\right) ^ {5 / 2}} \hat {\phi}
$$

其中 r 为距原点的距离。

!习题 7.46 如果一个悬浮在无限大超导平面上的磁偶极子（习题 7.45）可以自由旋转，它将会朝哪个方向转动，它将会在平面上悬浮得有多高？

习题7.47 在一个匀强磁场 $B = B_{0}\hat{z}$ 中，一个半径为 $a$ 的理想导电球壳绕着 $z$ 轴以角速度 $\omega$ 旋转。计算其“北极”与赤道之间产生的电动势。[答案： $\frac{1}{2} B_0\omega a^2$ ]

!习题 7.48 参考习题 7.11（并利用习题 5.42 的结果）：下落的圆环（半径为 a，质量为 m，电阻为 R）以其（变化的）最终速度穿过磁场 B 的底部需要多长时间？

习题7.49

（a）参考习题5.52a以及式7.18，对法拉第感应电场证明

$$
\boldsymbol {E} = - \frac {\partial \boldsymbol {A}}{\partial t}\tag{7.66}
$$

并通过对两边求散度和旋度检查上式。

（b）一个半径为 $a$ 的球壳带有均匀面电荷密度 $\sigma$ 。它绕着一个固定轴以缓慢随时间变化的角速度 $\omega$ 转动。求出球内部及外部的电场。[提示：这里有两部分的贡献：由于电荷而产生的库仑场，以及由于变化的 $B$ 而产生的法拉第场。参考例题5.11。]

习题7.50 经历回旋运动的电子可以通过增大磁场进行加速；伴随产生的电场会产生一个切向加速度。这就是电子感应加速器（betatron）的原理。有人想要在这个过程中保持轨道半径恒定。证明这可以通过设计这样一个磁场实现：其轨道区域上的平均磁场为圆周上磁场的两倍（图7.53）。假定电子在零场中从静止开始运动，并且此装置关于轨道的中心是对称的。（同样假定电子的速度始终远远低于光速，所以非相对论力学是适用的。）[提示：把式(5.3)对时间求导，并利用 $F = ma = qE$ 。]

习题7.51 一根无限长导线通有在 $z$ 方向恒定电流 $I$ ，以恒定速度 $\pmb{v}$ 沿 $y$ 方向移动。在似稳近似下，求当导线与 $z$ 轴重合的瞬时（图7.54）空间的电场。[答案： $-(\mu_0 I v / 2\pi s) \sin \phi \hat{z}$ ]

![](images/a231c7f46171310d819fd116c033c32dbb12e429d5b91afe0156a6a88fba03fd.jpg)  
图7.53

![](images/e072239fc03c5f7a2600962cac516b50e8d123e85c2a1039fd7de53cb1c1f548.jpg)  
图7.54

习题 7.52 一个原子中的电子（电荷为 q）在半径为 r 的轨道上围绕核（电荷量为 Q）运动；当然向心加速度是由不同符号电荷之间的吸引力提供的。现在垂直于轨道平面缓慢施加一个小磁场 dB。证明由感应电场提供的动能增加量 dT，正好可以维持电子在相同半径 r 上的圆周运动。（这就是为什么在我关于抗磁性的讨论中，我假设半径是固定的。参见 6.1.3 节以及那里引用的参考文献。）

习题7.53 一个长螺线管中的电流随时间线性增加，所以磁通量与 $t$ 成比例： $\Phi = \alpha t$ 。如图7.55所示，两个电压表，连同电阻（ $R_1$ 和 $R_2$ ），接在沿螺线管直径方向相对的两点（ $A$ 和 $B$ ）。这两个电压表上的读数分别为多少？假设这两个电压表是流过的电流可以忽略的理想电压表（它们有巨大的内阻），而电压表记录两个接头之间通过表的 $-\int_{a}^{b} E \cdot \mathrm{d}l$ 。[答案： $V_1 = \alpha R_1 / (R_1 + R_2)$ ； $V_2 = -\alpha R_2 / (R_1 + R_2)$ 。注意 $V_1 \neq V_2$ ，尽管它们连接到相同的点上！[34]

习题 7.54 圆形线圈（半径为 r，电阻为 R）内为一个均匀磁场区域，磁场 B 垂直于线圈平面。磁场（占据如图 7.56 所示的灰色区域）随时间线性增加 $(B = \alpha t)$ 。理想电压表（有无穷大内阻）接到 P 和 Q 两点。

(a) 线圈中电流是多少?

(b) 电压表的读数是多少? [答案: $\alpha r^2 / 2$ ]

![](images/7f4fa255ebb69435c79091d68726713880327dbd64d35908022f2957fe379fee.jpg)  
图7.55

![](images/b6b1b846c75524a7887b2cd17fd2f07c28ff32555461fe4094626cf19c19bc97.jpg)  
图7.56

习题 7.55 在动生电动势的讨论中（第 7.1.3节），我假定导线线圈（图 7.10）有电阻 R；于是产生的电流为 I = vBh/R。但是如果导线是由理想导体制作的，所以 R 为零，那将会怎样？在该情况下电流只被与线圈的自感系数 L 有关的反电动势（通常该电动势与 IR 相比是可以忽略的）所限制。证明在这个体系中线圈（质量为 m）做简谐运动，并且求出其频率 $^{35}$ 。[答案： $\omega = Bh/\sqrt{mL}$ ]

习题7.56

(a) 使用纽曼公式 [式 (7.23)] 计算图 7.37 中位形的互感系数，假设 $a$ 非常小 $(a \ll b, a \ll z)$ 。将你的答案与习题 7.22 比较。

(b) 对于一般情形（未假设 $a$ 很小）证明

$$
M = \frac {\mu_ {0} \pi \beta}{2} \sqrt {a b \beta} \left(1 + \frac {1 5}{8} \beta^ {2} + \dots\right)
$$

其中

$$
\beta \equiv \frac {a b}{z ^ {2} + a ^ {2} + b ^ {2}}
$$

习题7.57 两个线圈以使它们的每一匝通过的磁通量相等的方式沿着一圆柱形缠绕。（在实际中，这是通过在圆柱中穿过一个铁芯实现的；这个方法有集中磁通量的效果。）主线圈有 $N_{1}$ 匝，而副线圈有 $N_{2}$ 匝（图7.57）。如果主线圈中的电流 $I$ 正在改变，证明副线圈中的电动势由下式给出：

$$
\frac {\mathcal {E} _ {2}}{\mathcal {E} _ {1}} = \frac {N _ {2}}{N _ {1}}\tag{7.67}
$$

其中 $E_{1}$ 是主线圈的（反）电动势。[这就是变压器的原型——一种升高或者降低交变电流源电动势的设备。通过选择合适的匝数，可以在副线圈上得到任何想要的电动势。如果你认为这违背了能量守恒定律，研究习题 7.58。]

![](images/97b9bb4520dbff1d61ff664f970b23372874f0a4bdd9ac30c8b70344e3611733.jpg)  
图7.57

习题7.58 一个变压器（习题7.57）有振幅为 $V_{1}$ 的输入交流电压，并且输出振幅为 $V_{2}$ 的输出电压，该大小由匝数比决定 $(V_{2} / V_{1} = N_{2} / N_{1})$ 。如果 $N_{2} > N_{1}$ ，则输出电压比输入电压更大。为什么这没有违背能量守恒定律？答案：功率是电压与电流的乘积；显然，如果电压上升，电流必须下降。此问题的目的是来清楚地看看在简化过的模型中这是如何发生的。

(a) 在理想变压器中，主线圈与副线圈的每一匝都通过相同的磁通量。证明在这个情形下 $M^2 = L_1L_2$ ，其中 $M$ 为两个线圈之间的互感系数，而 $L_1$ 、 $L_2$ 为它们的自感系数。

(b) 假设主线圈由交流电压 $V_{\mathrm{in}} = V_{1}\cos (\omega t)$ 驱动，而副线圈连接到一个电阻 $R$ 。证明这两个电流满足关系

$$
L _ {1} \frac {\mathrm{d} I _ {1}}{\mathrm{d} t} + M \frac {\mathrm{d} I _ {2}}{\mathrm{d} t} = V _ {1} \cos (\omega t); L _ {2} \frac {\mathrm{d} I _ {2}}{\mathrm{d} t} + M \frac {\mathrm{d} I _ {1}}{\mathrm{d} t} = - I _ {2} R
$$

(c) 利用（a）中的结果，解出关于 $I_{1}$ 和 $I_{2}$ 的这两个方程。（假设 $I_{1}$ 没有直流成分。）

(d) 证明输出电压 $(V_{\mathrm{out}} = I_2R)$ 除以输入电压（ $V_{\mathrm{in}}$ ）等于匝数比： $V_{\mathrm{out}} / V_{\mathrm{in}} = N_2 / N_1$ 。

(e) 计算输入功率 $(P_{\mathrm{in}} = V_{\mathrm{in}}I_1)$ 与输出功率 $(P_{\mathrm{out}} = V_{\mathrm{out}}I_2)$ ，并证明它们关于一个完整周期的平均值相等。

习题7.59 一根无限长直导线沿 $z$ 方向延伸，其中所通过的电流 $I(z)$ 是 $z$ 的（但不是 $t$ 的）函数，电荷线密度 $\lambda(t)$ 是 $t$ 的（但不是 $z$ 的）函数。

(a) 通过检查在微小时间 $\mathrm{d}t$ 内流入微段 $\mathrm{d}z$ 的电荷，证明 $\mathrm{d}\lambda / \mathrm{d}t = -\mathrm{d}I / \mathrm{d}z$ 。如果我们设定 $\lambda(0) = 0$ 和 $I(0) = 0$ ，证明 $\lambda(t) = kt, I(z) = -kz$ ，其中 $k$ 是一个常量。

（b）假设有一段时间里过程是似稳的，因而场由式(2.9)与式(5.38)给出。通过验证这些满足麦克斯韦方程组的全部4个方程，证明实际上是场的精确解。（首先，对于 $s > 0$ 的区域，验证其微分形式，然后对于跨越轴的适当的高斯圆柱面/安培回路，验证其积分形式。）

习题 7.60 假设 $J(r)$ 不随时间变化但 $\rho(r,t)$ 不是——可能存在的情况，例如，在电容器的充电过程中。

(a) 证明在任何点的电荷密度都是时间的线性函数:

$$
\rho (\pmb {r}, t) = \rho (\pmb {r}, 0) + \dot {\rho} (\pmb {r}, 0) t
$$

其中 $\dot{\rho} (\pmb {r},0)$ 为在 $t = 0$ 时刻 $\rho$ 对于时间的导数。[提示：利用连续性方程]

这并不是一个静电学或静磁学系统 $^{36}$ ；然而——相当令人吃惊——库仑定律 [以式 (2.8) 的形式] 和毕奥-萨伐尔定律 [式 (5.42)] 成立，你可以通过证明它们满足麦克斯韦方程组来确认这一点。特别地：

(b) 证明

$$
B (r) = \frac {\mu_ {0}}{4 \pi} \int \frac {J \left(r ^ {\prime}\right) \times \hat {\mathbf {z}}}{\eta^ {2}} \mathrm{d} \tau^ {\prime}
$$

遵守带有麦克斯韦位移电流项的安培定律（或按脚注24，称安培-麦克斯韦定律——译者注）。

习题 7.61 一根通以电流 I 的无限长直导线的磁场可以通过下列方法从安培-麦克斯韦定律的位移电流项得到：设想由一个带有长为 $\varepsilon$ 的微小缺口的均匀线电荷 $\lambda$ 沿着 z 轴以速率 v 运动构成的电流（所以 $I = \lambda v$ ），该缺口在 t = 0 时刻到达原点。在下一个时刻（直到 $t = \varepsilon / v$ ），没有真实的电流通过一个 xy 平面上的环形安培环路，但是由于缺口中“缺失的”的电荷，存在位移电流。

(a) 对于 $xy$ 平面上距离原点 $s$ 处的点，利用库仑定律计算由于一段从 $z_{1} = vt - \varepsilon$ 到 $z_{2} = vt$ 的带有均匀电荷密度 $-\lambda$ 的一段导线产生电场的 $z$ 分量。

(b) 求出这个电场通过 $xy$ 平面上一个半径为 $a$ 的圆环的通量。

(c) 求出通过这个圆环的位移电流。证明在缺口宽度趋近于零的极限下， $I_{d}$ 等于 $I^{37}$ 。

习题7.62 某输电线路由两条宽度为 $w$ 、相距很小的距离 $h(\ll w)$ 的薄金属“带”构成。电流沿着其中一条流出，然后沿着另一条流回。电流在带的表面上是均匀分布的。

(a) 求出每单位长度的电容 C。

(b) 求出每单位长度的电感 $\mathcal{L}$ 。

(c) 乘积 $\mathcal{LC}$ 在数值上有多大？[当然， $\mathcal{L}$ 和 $\mathcal{C}$ 对于不同种类的传输线是不同的，但是它们的乘积是一个普适常数——例如，检验例题7.13中的电缆——只要两个导体之间的空间是真空的。在传输线的理论中，这个乘积与沿着导线传播的脉冲的速度有关： $v = 1 / \sqrt{\mathcal{LC}}$ 。]

(d) 如果这两条导线相互之间用介电常数为 $\varepsilon$ 、磁导率为 $\mu$ 的不导电材料绝缘，此时乘积 $\mathcal{L}\mathcal{C}$ 为多大？传播速度多大？[提示：见例题4.6；当一个电容器浸入磁导率为 $\mu$ 的线性材料中时， $\mathcal{L}$ 按照什么因子改变？]

习题7.63 证明阿尔芬定理（Alfven's theorem）：在理想导电流体中（例如，自由电子气），通过任意随流体流动的闭合回路的磁通量在所有时刻保持恒定。（磁场线，实际上，被“冻结”在流体中。）

(a) 利用式 (7.2) 形式的欧姆定律，以及法拉第定律，证明如果 $\sigma = \infty$ 但是 $J$ 有限，则

$$
\frac {\partial \boldsymbol {B}}{\partial t} = \nabla \times (\boldsymbol {v} \times \boldsymbol {B})
$$

(b) 令 S 为 t 时刻以回路（P）为边界的面，而 $S'$ 为以在 $t + dt$ 时刻的新位置（ $P'$ ）的回路为边界的面（图 7.58）。通量的变化为

$$
\mathrm{d} \Phi = \int_ {\mathcal {S} ^ {\prime}} \boldsymbol {B} (t + \mathrm{d} t) \cdot \mathrm{d} \boldsymbol {a} - \int_ {\mathcal {S}} \boldsymbol {B} (t) \cdot \mathrm{d} \boldsymbol {a}
$$

利用 $\nabla \cdot B = 0$ 证明

$$
\int_ {\mathcal {S} ^ {\prime}} \boldsymbol {B} (t + \mathrm{d} t) \cdot \mathrm{d} \boldsymbol {a} + \int_ {\mathcal {R}} \boldsymbol {B} (t + \mathrm{d} t) \cdot \mathrm{d} \boldsymbol {a} = \int_ {\mathcal {S}} \boldsymbol {B} (t + \mathrm{d} t) \cdot \mathrm{d} \boldsymbol {a}
$$

（其中 R 为连接 P 和 $P'$ 的 “带”。）因此（对于无限小的 dt）

$$
\mathrm{d} \varPhi = \mathrm{d} t \int_ {\mathcal {S}} \frac {\partial \boldsymbol {B}}{\partial t} \cdot \mathrm{d} \boldsymbol {a} - \int_ {\mathcal {R}} \boldsymbol {B} (t + \mathrm{d} t) \cdot \mathrm{d} \boldsymbol {a}
$$

利用第7.1.3节中的方法将第二个积分改写为

$$
\mathrm{d} t \oint_ {\mathcal {P}} (\boldsymbol {B} \times \boldsymbol {v}) \cdot \mathrm{d} \boldsymbol {l}
$$

并且利用斯托克斯定律，可以得到结论

$$
\frac {\mathrm{d} \Phi}{\mathrm{d} t} = \int_ {S} \left(\frac {\partial B}{\partial t} - \nabla \times (\boldsymbol {v} \times \boldsymbol {B})\right) \cdot \mathrm{d} \boldsymbol {a}
$$

连同（a）中的结果，这样就证明了阿尔芬定理。

![](images/6b792f2c56b3bd282e46d0b5e84864e8b2663df382903110698b280a9156a284.jpg)  
图7.58

习题7.64

(a) 证明带有磁荷项的麦克斯韦方程组 [式 (7.44)] 在对偶变换（duality transformation）下保持不变:

$$
\left. \begin{array}{l} \pmb {E} ^ {\prime} = \pmb {E} \cos \alpha + c \pmb {B} \sin \alpha \\ c \pmb {B} ^ {\prime} = c \pmb {B} \cos \alpha - \pmb {E} \sin \alpha \\ c q _ {\mathrm{e}} ^ {\prime} = c q _ {\mathrm{e}} \cos \alpha + q _ {\mathrm{m}} \sin \alpha \\ q _ {\mathrm{m}} ^ {\prime} = q _ {\mathrm{m}} \cos \alpha - c q _ {\mathrm{e}} \sin \alpha \end{array} \right\}\tag{7.68}
$$

其中 $c \equiv 1 / \sqrt{\varepsilon_0 \mu_0}$ ，而 $\alpha$ 是在“ $E / B$ -空间”中的一个任意转动角。荷和流密度按照与 $q_{\mathrm{e}}$ 和 $q_{\mathrm{m}}$ 相同的方式变换。[特别地，这意味着如果你知道某个电荷分布产生的场，就可以直接（利用 $\alpha = 90^{\circ}$ ）写下相应分布的磁荷产生的场。]

(b) 证明力定律（习题7.38）

$$
\boldsymbol {F} = q _ {\mathrm{e}} (\boldsymbol {E} + \boldsymbol {v} \times \boldsymbol {B}) + q _ {\mathrm{m}} \left(\boldsymbol {B} - \frac {1}{c ^ {2}} \boldsymbol {v} \times \boldsymbol {E}\right)\tag{7.69}
$$

同样在对偶变换下保持不变。

## 期间暂停

所有的牌都已在桌子上了，在一定程度上这意味着我已完成我的工作。在前7章，我们一块一块地把电动力学组装起来，而现在，以麦克斯韦方程组为它的最终形式，理论已经完备。没有更多的规律需要进一步学习，也没有进一步的推广需要考虑，并且（也许还有一个例外）没有潜在的不一致需要修补。如果你仅想修一学期的课程，也许现在是合理的终点。

但是从另一个意义上我们刚好到达一个起点。我们至少掌握了相当的知识，我们知道了游戏的规则——现在是玩它们的时候了。这是一个有趣的部分，在其中我们将享受电动力学强大的威力及丰富的内容。对一学年的课程，我们有充分的时间学习剩余的内容，也许可将等离子物理作为一个单元补充，或者交流电路理论，或者少许广义相对论的内容。但是如果你仅有时间学习一个课题，我建议第9章——电磁波（也许你想浏览第8章作为预备）。这是光学的继续，历史上这是麦克斯韦理论的最重要应用。

## 第 8 章 守恒律

## 8.1 电荷和能量

## 8.1.1 连续性方程

在这一章中我们将要学习电动力学中的能量、动量和角动量守恒。但是作为开始，我想先回顾一下电荷守恒，因为它是一切守恒定律的范例。精确来讲，电荷守恒告诉了我们什么？宇宙中的电荷总量是一个常数？当然——这是全局（global）的电荷守恒。但是局域（local）电荷守恒是一个更强表述：如果某一给定体积内的总电荷量有所改变，就必须有等量的电荷流入或流出包围这个体积的表面。就像老虎不能凭空跑到笼子外面，如果它从里面逃到外面，那么围栏上必然有一个洞。

形式上，一个体积 $\nu$ 内的电荷量为

$$
Q (t) = \int_ {\mathcal {V}} \rho (\boldsymbol {r}, t) \mathrm{d} \tau\tag{8.1}
$$

并且，通过边界 $\mathcal{S}$ 向外流出的电流为 $\oint_{\mathcal{S}} J \cdot \mathrm{d}a$ ，所以局域电荷守恒可表述为

$$
\frac {\mathrm{d} Q}{\mathrm{d} t} = - \oint_ {S} \boldsymbol {J} \cdot \mathrm{d} \boldsymbol {a}\tag{8.2}
$$

将方程(8.1)代入等式左边，并且在等式右边应用散度定理，我们得到

$$
\int_ {\mathcal {V}} \frac {\partial \rho}{\partial t} \mathrm{d} \tau = - \int_ {\mathcal {V}} \nabla \cdot \boldsymbol {J} \mathrm{d} \tau\tag{8.3}
$$

上式对任意体积 $\nu$ 都成立，所以有

$$
\boxed {\frac {\partial \rho}{\partial t} = - \nabla \cdot \boldsymbol {J}}\tag{8.4}
$$

这就是连续性方程——局域电荷守恒的严格数学表述。它可以从麦克斯韦方程组推导出来——电荷守恒不是一个独立的假设，而是已被纳入电动力学的规律中。它充当了源（ $\rho$ 与 $J$ ）的约束。它们不能只是任何函数——它们必须遵守电荷守恒 $^{1}$ 。

我们这一章的目的是对能量守恒和动量守恒构建相应的方程。在这个过程中（或许这更为重要），我们会学到如何去表达能量密度和动量密度（与 $\rho$ 类似），以及能量“流”和动量“流”（与 J 类似）。

## 8.1.2 坡印亭定理

在第2章中，我们发现将一个静态电荷分布聚集到一起需要的功（克服相同电荷间的库仑斥力）为[式(2.45)]

$$
W _ {\mathrm{e}} = \frac {\varepsilon_ {0}}{2} \int E ^ {2} \mathrm{d} \tau
$$

其中 E 为产生的电场。类似地，使电荷流动产生电流所需要的功（克服反电动势）为 [式 (7.35)]

$$
W _ {\mathrm{m}} = \frac {1}{2 \mu_ {0}} \int B ^ {2} \mathrm{d} \tau
$$

其中 B 为产生的磁场。这表明在单位体积中电磁场所储存的总能量为

$$
\boxed {u = \frac {1}{2} \left(\varepsilon_ {0} E ^ {2} + \frac {1}{\mu_ {0}} B ^ {2}\right)}\tag{8.5}
$$

本节我将确认式 $(8.5)$ ，并发展电动力学的能量守恒定律。

假设我们有某种电荷和电流分布，在时刻 $t$ ，它们产生电场 $\pmb{E}$ 和磁场 $\pmb{B}$ 。经过瞬时 $\mathrm{dt}$ ，电荷移动了一小段距离。问：在时间间隔 $\mathrm{dt}$ 中，作用在这些电荷上的电磁力做了多少功？根据洛伦兹力定律，电磁场对电荷 $q$ 所做的功为

$$
\boldsymbol {F} \cdot \mathrm{d} \boldsymbol {l} = q (\boldsymbol {E} + \boldsymbol {v} \times \boldsymbol {B}) \cdot \boldsymbol {v} \mathrm{d} t = q \boldsymbol {E} \cdot \boldsymbol {v} \mathrm{d} t
$$

采用电荷密度与电流密度， $q \rightarrow \rho d\tau$ ， $\rho v \rightarrow J$ ， $^{2}$ 因此电磁场对体积 V 内所有电荷做功的总功率为

$$
\frac {\mathrm{d} W}{\mathrm{d} t} = \int_ {\mathcal {V}} (\boldsymbol {E} \cdot \boldsymbol {J}) \mathrm{d} \tau\tag{8.6}
$$

显然， $E \cdot J$ 是单位时间内对单位体积内的电荷所做的功——也就是说，对单位体积传递的功率。我们可以仅用场量把它表示出来，用安培-麦克斯韦定律消去 J：

$$
\boldsymbol {E} \cdot \boldsymbol {J} = \frac {1}{\mu_ {0}} \boldsymbol {E} \cdot (\nabla \times \boldsymbol {B}) - \varepsilon_ {0} \boldsymbol {E} \cdot \frac {\partial \boldsymbol {E}}{\partial t}
$$

根据矢量积法则6

$$
\nabla \cdot (\boldsymbol {E} \times \boldsymbol {B}) = \boldsymbol {B} \cdot (\nabla \times \boldsymbol {E}) - \boldsymbol {E} \cdot (\nabla \times \boldsymbol {B})
$$

应用法拉第定律（ $\nabla \times \pmb {E} = -\partial \pmb {B} / \partial t$ ），随即得到

$$
\pmb {E} \cdot (\nabla \times \pmb {B}) = - \pmb {B} \cdot \frac {\partial \pmb {B}}{\partial t} - \nabla \cdot (\pmb {E} \times \pmb {B})
$$

又因为

$$
\pmb {B} \cdot {\frac {\partial \pmb {B}}{\partial t}} = {\frac {1}{2}} {\frac {\partial}{\partial t}} \left(B ^ {2}\right), \quad \text {以及} \quad \pmb {E} \cdot {\frac {\partial \pmb {E}}{\partial t}} = {\frac {1}{2}} {\frac {\partial}{\partial t}} \left(E ^ {2}\right)\tag{8.7}
$$

所以

$$
\pmb {E} \cdot \pmb {J} = - \frac {1}{2} \frac {\partial}{\partial t} \left(\varepsilon_ {0} E ^ {2} + \frac {1}{\mu_ {0}} B ^ {2}\right) - \frac {1}{\mu_ {0}} \nabla \cdot (\pmb {E} \times \pmb {B})\tag{8.8}
$$

将上式代入式 (8.6) 并对右边第二项应用散度定理，我们有

$$
\frac {\mathrm{d} W}{\mathrm{d} t} = - \frac {\mathrm{d}}{\mathrm{d} t} \int_ {\mathcal {V}} \frac {1}{2} \left(\varepsilon_ {0} E ^ {2} + \frac {1}{\mu_ {0}} B ^ {2}\right) \mathrm{d} \tau - \frac {1}{\mu_ {0}} \oint_ {\mathcal {S}} (\boldsymbol {E} \times \boldsymbol {B}) \cdot \mathrm{d} \boldsymbol {a}\tag{8.9}
$$

其中 $S$ 为体积 $\nu$ 的边界。这就是坡印亭定理（Poynting's theorem）；它是电动力学中的功能原理。右边第一项积分是储藏在电磁场中的总能量[式(8.5)]。第二项明显代表能量从体积 $\nu$ 中通过表面向外传输的速率。于是，坡印亭定理指出：电磁场对体积 $\nu$ 内所有电荷做的总功等于电磁场能量的减少减去从边界流出的能量。

电磁场在单位时间内通过单位表面积向外传递的能量称为坡印亭矢量（Poynting's vector）：

$$
\boxed {S \equiv \frac {1}{\mu_ {0}} (E \times B)}\tag{8.10}
$$

特别地， $S \cdot da$ 是单位时间内通过无限小面元 $da$ 的能量——能流（这样 $S$ 就是能流密度） $^{3}$ 。在第 9 章和第 11 章我们将会见到坡印亭矢量的多种应用，但是现在，我的主要兴趣是用它把坡印亭定理表述得更为紧凑：

$$
\frac {\mathrm{d} W}{\mathrm{d} t} = - \frac {\mathrm{d}}{\mathrm{d} t} \int_ {\mathcal {V}} u \mathrm{d} \tau - \oint_ {\mathcal {S}} \boldsymbol {S} \cdot \mathrm{d} \boldsymbol {a}\tag{8.11}
$$

如果对体积 $\mathcal{V}$ 中的电荷并没有做功会如何？——例如，我们在一个虚空的空间，其中并没有电荷会如何？在那种情形下， $\mathrm{d}W / \mathrm{d}t = 0$ ，于是

$$
\int {\frac {\partial u}{\partial t}} \mathrm{d} \tau = - \oint {\bf S} \cdot \mathrm{d} {\bf a} = - \int (\nabla \cdot {\bf S}) \mathrm{d} \tau
$$

于是

$$
\frac {\partial \boldsymbol {u}}{\partial t} = - \nabla \cdot \boldsymbol {S}\tag{8.12}
$$

这是能量的“连续性方程”——u（能量密度）扮演了 $\rho$ （电荷密度）的角色，而 S（能流密度）扮演了 J（电流密度）的角色。此式表达了电磁能量的局域守恒。

然而，一般来说，电磁能本身并不守恒（电荷的能量也不守恒）。场对电荷起作用，电荷产生场——能量在它们之间来回交换。在总能量记账时，物质和场的贡献你都必须包含。

例题8.1 当电流流过导线时，就会做功，以焦耳热的形式释放出来[方程(7.7)]。尽管有更简便的方法，我们可以利用坡印亭矢量来计算单位时间内传递给导线的能量。假设场是均匀的，则平行于导线的电场强度为

其中 $V$ 为导线两端的电势差， $L$ 为导线的长度（图8.1）。磁场环绕着导线，在导线表面（半径为 $a$ ）磁场大小为

$$
B = \frac {\mu_ {0} I}{2 \pi a}
$$

相应地，坡印亭矢量的大小为

$$
S = \frac {1}{\mu_ {0}} \frac {V}{L} \frac {\mu_ {0} I}{2 \pi a} = \frac {V I}{2 \pi a L}
$$

并且（根据右手定则）它沿径向指向导线内部，单位时间内通过表面传入导线内的能量为

$$
\boldsymbol {S} \cdot \mathrm{d} \boldsymbol {a} = S (2 \pi a L) = V I
$$

这正是我们在第 7.1.1 节 $^{4}$ 中用更直接的方法得到的结果。

![](images/2b449e8bd959bd4e113e4b85ec12fed23e3d5591dc32100b10bcc1eafb643c34.jpg)  
图8.1

习题8.1 计算例题7.13和习题7.62中沿着电缆传输的功率（单位时间内传输的能量），假设内外两个导线间的电势差为 $V$ ，电流为 $I$ （从一个流入，另一个流出）。

## 习题 8.2 考虑习题 7.34 中的充电电容器。

(a) 求间隙中的电场与磁场作为到轴线的距离 $s$ 与时间 $t$ 的函数。（假设在 $t = 0$ 时刻，电容器的电量为零。）

(b) 求间隙中的能量密度 u 和坡印亭矢量 S，特别要注意 S 的方向。并且验证是否满足式 (8.12)。

(c) 计算间隙中的总能量作为时间 $t$ 的函数。通过计算坡印亭矢量对一个合适的表面积分求出电磁场向间隙中传输的总功率，检验它与间隙中能量的增加率相等 [式 (8.9)——不过现在 $W = 0$ ，因为间隙中没有电荷]。[如果担心边缘场的影响，可以选取半径 $b < a$ 的体积使其完全处在间隙内部。]

## 8.2 动量

## 8.2.1 电动力学中的牛顿第三定律

设想一个点电荷 q 沿 x 轴以恒定速率 v 运动。因为运动，它所产生的电场并不由库仑定律给出；正如我们将在第 10 章见到的那样，E 的方向仍然沿电荷的瞬时位置的径向方向（图 8.2a）。更重要的是，一个运动的电荷并不产生稳定的电流，所以它的磁场并不由毕奥-萨伐尔定律给出。然而，仍旧环绕着 x 轴，如右手定则表述的那样（图 8.2b）；同样，在第 10 章将给出证明。

![](images/8d322bb332988b551826a6a4d7ec12b59700dbe0c90311ae657178685489f640.jpg)

![](images/b83301cfa4cc94f43e10464452984a45f14ce8bc5e3177ec7ed0fb1ae3c9a111.jpg)  
图8.2  
b)

现在，假设这个电荷遇见了另外一个具有相等电量、以同样速率 $v$ 沿 $y$ 轴运动的电荷。显然，电荷之间的电磁力会使它们偏离坐标轴。不过，让我们假设这两个电荷被固定在导轨上，或者由于别的什么原因，使它们只能沿固定方向以恒定速度运动（图8.3）。它们之间的电场力等值反向，但是磁场力呢？因为电荷 $q_{1}$ 产生的磁场指向纸内（在 $q_{2}$ 位置处），所以 $q_{2}$ 所受的磁场力指向右。同时， $q_{2}$ 产生的磁场指向纸外（在 $q_{1}$ 的位置上），因此 $q_{1}$ 所受磁场力向上。 $q_{1}$ 和 $q_{2}$ 所受电磁力大小相等，但并不指向相反方向，违背了牛顿第三定律。在静电学和静磁学中第三定律成立，但是在电动力学中它不成立。

![](images/ea977888fb78cc63bda0a1c88210a2ce3622edc76057cf362b68c211095228a7.jpg)  
图8.3

这真是一件好奇的有趣事情，但是在实际中，我们如何能经常使用牛顿第三定律呢？

答案：总是如此！动量守恒的证明是基于内力的相互抵消，内力遵循牛顿第三定律。当你篡改牛顿第三定律时，就把动量守恒放到了一个危险地位，而物理学中几乎没有比这更神圣的原则。

如果我们意识到电磁场本身携带动量，电动力学中的动量守恒定律被拯救了。考虑到我们已经将电磁场赋予了能量，这并不令人吃惊。粒子损失的动量被电磁场获得，只有把电磁场的动量加入粒子的机械动量中后，动量守恒才能恢复。

## 8.2.2 麦克斯韦应力张量

让我们来计算一体积 $\nu$ 内的电荷所受的电磁力

$$
\boldsymbol {F} = \int_ {\mathcal {V}} (\boldsymbol {E} + \boldsymbol {v} \times \boldsymbol {B}) \rho \mathrm{d} \tau = \int_ {\mathcal {V}} (\rho \boldsymbol {E} + \boldsymbol {J} \times \boldsymbol {B}) \mathrm{d} \tau\tag{8.13}
$$

单位体积所受的力为

$$
\boldsymbol {f} = \rho \boldsymbol {E} + \boldsymbol {J} \times \boldsymbol {B}\tag{8.14}
$$

与以前一样，我建议用场量把它表示出来，用麦克斯韦方程组中的（i）和（iv）消去 $\rho$ 和 $J$ 得

$$
\boldsymbol {f} = \varepsilon_ {0} (\nabla \cdot \boldsymbol {E}) \boldsymbol {E} + \left(\frac {1}{\mu_ {0}} \nabla \times \boldsymbol {B} - \varepsilon_ {0} \frac {\partial \boldsymbol {E}}{\partial t}\right) \times \boldsymbol {B}
$$

现在

$$
\frac {\partial}{\partial t} (\boldsymbol {E} \times \boldsymbol {B}) = \left(\frac {\partial \boldsymbol {E}}{\partial t} \times \boldsymbol {B}\right) + \left(\boldsymbol {E} \times \frac {\partial \boldsymbol {B}}{\partial t}\right)
$$

另由法拉第定律，有

$$
\frac {\partial \pmb {B}}{\partial t} = - \nabla \times \pmb {E}
$$

所以

$$
\frac {\partial \pmb {E}}{\partial t} \times \pmb {B} = \frac {\partial}{\partial t} + \pmb {E} \times (\nabla \times \pmb {E})
$$

这样有

$$
\pmb {f} = \varepsilon_ {0} [ (\nabla \cdot \pmb {E}) \pmb {E} - \pmb {E} \times (\nabla \times \pmb {E}) ] - \frac {1}{\mu_ {0}} [ \pmb {B} \times (\nabla \times \pmb {B}) ] - \varepsilon_ {0} \frac {\partial}{\partial t} (\pmb {E} \times \pmb {B})\tag{8.15}
$$

为了让方程看起来更对称一点，让我们加入一项 $(\nabla \cdot B)B$ ；因为 $\nabla \cdot B = 0$ ，这样做没有任何影响。同时，根据矢量积规则4，

$$
\nabla \left(E ^ {2}\right) = 2 (\boldsymbol {E} \cdot \nabla) \boldsymbol {E} + 2 \boldsymbol {E} \times (\nabla \times \boldsymbol {E})
$$

所以

$$
\pmb {E} \times (\nabla \times \pmb {E}) = \frac {1}{2} \nabla (E ^ {2}) - (\pmb {E} \cdot \nabla) \pmb {E}
$$

对 $\pmb{B}$ 也是如此，这样我们就有

$$
\begin{array}{r l} \boldsymbol {f} = & \varepsilon_ {0} [ (\nabla \cdot \boldsymbol {E}) \boldsymbol {E} + (\boldsymbol {E} \cdot \nabla) \boldsymbol {E} ] + \frac {1}{\mu_ {0}} [ (\nabla \cdot \boldsymbol {B}) \boldsymbol {B} + (\boldsymbol {B} \cdot \nabla) \boldsymbol {B} ] \\ & - \frac {1}{2} \nabla \left(\varepsilon_ {0} E ^ {2} + \frac {1}{\mu_ {0}} B ^ {2}\right) - \varepsilon_ {0} \frac {\partial}{\partial t} (\boldsymbol {E} \times \boldsymbol {B}) \end{array}\tag{8.16}
$$

太难看了！但是当我们引入麦克斯韦应力张量（Maxwell stress tensor）

$$
T _ {i j} \equiv \varepsilon_ {0} \left(E _ {i} E _ {j} - \frac {1}{2} \delta_ {i j} E ^ {2}\right) + \frac {1}{\mu_ {0}} \left(B _ {i} B _ {j} - \frac {1}{2} \delta_ {i j} B ^ {2}\right)\tag{8.17}
$$

方程可被简化。其中下标 $i$ 和 $j$ 表示坐标 $x, y$ 和 $z$ ，所以应力张量共有9个分量（ $T_{xx}, T_{yy}, T_{xz}, T_{yx}$ 等）。克罗内克符号（Kronecker delta） $\delta_{ij}$ ，当下标 $ij$ 相同为 $1(\delta_{xx} = \delta_{yy} = \delta_{zz} = 1)$ ，其余情况为 $0(\delta_{xy} = \delta_{xz} = \delta_{yz} = 0)$ 。这样有

$$
\begin{array}{l} {T _ {x x} = \frac {1}{2} \varepsilon_ {0} \left(E _ {x} ^ {2} - E _ {y} ^ {2} - E _ {z} ^ {2}\right) + \frac {1}{2 \mu_ {0}} \left(B _ {x} ^ {2} - B _ {y} ^ {2} - B _ {z} ^ {2}\right)} \\ {T _ {x y} = \varepsilon_ {0} \left(E _ {x} E _ {y}\right) + \frac {1}{\mu_ {0}} \left(B _ {x} B _ {y}\right)} \end{array}
$$

依此类推。

因为它有两个指标，而矢量只有一个，所以有时被写成一个带双箭号的符号： $\vec{T}$ 。我们可以用两种方式构造 $\vec{T}$ 与一个矢量 $a$ 的点积——从左边乘和从右边乘：

$$
(\boldsymbol {a} \cdot \stackrel {\leftrightarrow} {T}) _ {j} = \sum_ {i = x, y, z} a _ {i} T _ {i j}, \quad (\stackrel {\leftrightarrow} {T} \cdot \boldsymbol {a}) _ {j} = \sum_ {i = x, y, z} T _ {j i} a _ {i}\tag{8.18}
$$

所得结果只有一个指标，是一个矢量。特别有， $\vec{T}$ 的散度的第 $j$ 个分量是

$$
\begin{array}{r l} (\nabla \cdot \vec {T}) _ {j} = & \varepsilon_ {0} \left[ (\nabla \cdot \pmb {E}) E _ {j} + (\pmb {E} \cdot \nabla) E _ {j} - \frac {1}{2} \nabla_ {j} E ^ {2} \right] + \\ & \frac {1}{\mu_ {0}} \left[ (\nabla \cdot \pmb {B}) B _ {j} + (\pmb {B} \cdot \nabla) B _ {j} - \frac {1}{2} \nabla_ {j} B ^ {2} \right] \end{array}
$$

这样，单位体积所受的力[式(8.16)]可以写成更简洁的形式

$$
\boldsymbol {f} = \nabla \cdot \stackrel {\leftrightarrow} {T} - \varepsilon_ {0} \mu_ {0} \frac {\partial \boldsymbol {S}}{\partial t}\tag{8.19}
$$

其中，S 是坡印亭矢量 [式 (8.10)]。

显然，体积 $\mathcal{V}$ 内所有电荷所受的合力[式(8.13)]为

$$
\pmb {F} = \oint_ {\mathcal {S}} \stackrel {\leftrightarrow} {T} \cdot \mathrm{d} \pmb {a} - \varepsilon_ {0} \mu_ {0} \frac {\mathrm{d}}{\mathrm{d} t} \int_ {\mathcal {V}} \pmb {S} \mathrm{d} \tau\tag{8.20}
$$

（我已利用散度定理把第一项的体积分转换成面积分。）在静态情况，第二项就可以去掉，此时电荷分布所受的电磁力可以只用边界上电磁场的应力张量来表示：

$$
\pmb {F} = \oint_ {\mathcal {S}} \stackrel {\leftrightarrow} {T} \cdot \mathrm{d} \pmb {a} (\text {静态})\tag{8.21}
$$

物理上， $\vec{T}$ 是电磁场作用在表面上单位面积上的力（或应力，stress）。更精确地说， $T_{ij}$ 是作用在 $j$ 方向面元上沿 $i$ 方向（单位面积上）的力——“对角”元 $(T_{xx}, T_{yy}, T_{zz})$ 代表压力，“非对角”元 $(T_{xy}, T_{xz}$ 等）代表剪切力。

例题8.2 求一个均匀带电球下半球作用于上半球的力，球的半径为 $R$ ，带有电荷 $Q$ 。[和习题2.47相同，不过这一次，我们要用麦克斯韦应力张量和式(8.21)求解。]

[解答] 上半球的边界面由两部分组成——半径为 $R$ 的半球面和在 $\theta = \pi / 2$ 处的一个圆面（图8.4）。对于半球面

$$
\mathrm{d} \boldsymbol {a} = R ^ {2} \sin \theta \mathrm{d} \theta \mathrm{d} \phi \hat {\boldsymbol {r}}
$$

![](images/34e5f1e58479da5f04f50711003f9c82820820704386dc160d866bec88d8fafa.jpg)  
图8.4

$$
\boldsymbol {E} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {Q}{R ^ {2}} \hat {\boldsymbol {r}}
$$

$$
T _ {z x} = \varepsilon_ {0} E _ {z} E _ {x} = \varepsilon_ {0} \left(\frac {Q}{4 \pi \varepsilon_ {0} R ^ {2}}\right) ^ {2} \sin \theta \cos \theta \cos \phi
$$

$$
T _ {z y} = \varepsilon_ {0} E _ {z} E _ {y} = \varepsilon_ {0} \left(\frac {Q}{4 \pi \varepsilon_ {0} R ^ {2}}\right) ^ {2} \sin \theta \cos \theta \sin \phi
$$

$$
T _ {z z} = \frac {\varepsilon_ {0}}{2} \left(E _ {z} ^ {2} - E _ {x} ^ {2} - E _ {y} ^ {2}\right) = \frac {\varepsilon_ {0}}{2} \left(\frac {Q}{4 \pi \varepsilon_ {0} R ^ {2}}\right) ^ {2} \left(\cos^ {2} \theta - \sin^ {2} \theta\right)\tag{8.22}
$$

合力显然沿 $z$ 方向。所以，只需要计算

$$
(\stackrel {\leftrightarrow} {T} \cdot \mathrm{d} \pmb {a}) _ {z} = T _ {z x} \mathrm{d} a _ {x} + T _ {z y} \mathrm{d} a _ {y} + T _ {z z} \mathrm{d} a _ {z} = \frac {\varepsilon_ {0}}{2} \left(\frac {Q}{4 \pi \varepsilon_ {0} R}\right) ^ {2} \sin \theta \cos \theta \mathrm{d} \theta \mathrm{d} \phi
$$

$$
F _ {\mathrm{半球面}} = \frac {\varepsilon_ {0}}{2} \left(\frac {Q}{4 \pi \varepsilon_ {0} R}\right) ^ {2} 2 \pi \int_ {0} ^ {\pi / 2} \sin \theta \cos \theta \mathrm{d} \theta = \frac {1}{4 \pi \varepsilon_ {0}} \frac {Q ^ {2}}{8 R ^ {2}}\tag{8.23}
$$

对于赤道处的圆面

$$
\mathrm{d} a = - r \mathrm{d} r \mathrm{d} \phi \hat {z}\tag{8.24}
$$

并且（因为我们是在球体内部）

$$
\pmb {E} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {Q}{R ^ {3}} \pmb {r} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {Q}{R ^ {3}} r (\cos \phi \hat {\pmb {x}} + \sin \phi \hat {\pmb {y}})
$$

这样有

$$
T _ {z z} = \frac {\varepsilon_ {0}}{2} \left(E _ {z} ^ {2} - E _ {x} ^ {2} - E _ {y} ^ {2}\right) = - \frac {\varepsilon_ {0}}{2} \left(\frac {Q}{4 \pi \varepsilon_ {0} R ^ {3}}\right) ^ {2} r ^ {2}
$$

因此

$$
(\stackrel {\leftrightarrow} {T} \cdot \mathrm{d} \boldsymbol {a}) _ {z} = \frac {\varepsilon_ {0}}{2} \left(\frac {Q}{4 \pi \varepsilon_ {0} R ^ {3}}\right) ^ {2} r ^ {3} \mathrm{d} r \mathrm{d} \phi
$$

这样，作用于圆面上的力为

$$
F _ {\text {圆面}} = \frac {\varepsilon_ {0}}{2} \left(\frac {Q}{4 \pi \varepsilon_ {0} R ^ {3}}\right) ^ {2} 2 \pi \int_ {0} ^ {R} r ^ {3} \mathrm{d} r = \frac {1}{4 \pi \varepsilon_ {0}} \frac {Q ^ {2}}{1 6 R ^ {2}}\tag{8.25}
$$

结合式 (8.23) 和式 (8.25)，得到作用在北半球上的力为

$$
F = \frac {1}{4 \pi \varepsilon_ {0}} \frac {3 Q ^ {2}}{1 6 R ^ {2}}\tag{8.26}
$$

顺便提及，在应用式(8.21)时，任何体积只要它包含问题中的所有电荷（并且没有别的电荷），计算结果都相同。例如，在本题中我们可以对整个上半空间 $z > 0$ 做计算，这时边界变为整个 $xy$ 平面（加上一个半径为无穷的半球，但是那里的 $E = 0$ ，因此无须考虑）。代替原来的半球，我们现在要计算的是 $xy$ 平面中 $r > R$ 的部分。在这些地方

$$
T _ {z z} = - \frac {\varepsilon_ {0}}{2} \left(\frac {Q}{4 \pi \varepsilon_ {0}}\right) ^ {2} \frac {1}{r ^ {4}}
$$

[式(8.22)，此时 $\theta = \pi /2$ ，并且将 $R$ 代换为 $r$ 。]da由式(8.24)给出，所以

$$
(\overleftrightarrow {T} \cdot \mathrm{d} \pmb {a}) _ {z} = \frac {\varepsilon_ {0}}{2} \left(\frac {Q}{4 \pi \varepsilon_ {0}}\right) ^ {2} \frac {1}{r ^ {3}} \mathrm{d} r \mathrm{d} \phi
$$

圆面中 $r > R$ 部分所做的贡献为

$$
\frac {\varepsilon_ {0}}{2} \left(\frac {Q}{4 \pi \varepsilon_ {0}}\right) ^ {2} 2 \pi \int_ {R} ^ {\infty} \frac {1}{r ^ {3}} \mathrm{d} r = \frac {1}{4 \pi \varepsilon_ {0}} \frac {Q ^ {2}}{8 R ^ {2}}
$$

这和原来的半球面所得结果 [式 (8.23)] 一样。

我希望你们不要陷入例题 8.2 的细节。如果是这样的话，花点时间去体会一下要领。我们打算计算作用在一个固体上的力，取代一个预期的体积分，式(8.21)允许我们由一个面积分来实现目的；应力张量以某种方式感觉出体积内部的情况。

电荷面密度为 $\sigma$ 。[这和习题5.44相同，但是这一次用麦克斯韦应力张量和式(8.21)求解。]

## 习题8.4

（a）考虑相距为 $2a$ 、带有等量电量 $q$ 的两个点电荷。在到两电荷距离相等的平面上对麦克斯韦应力张量积分求一个电荷对另一个的作用力。

（b）若两电荷带等量相反电荷，重复（a）中求解。

## 8.2.3 动量守恒

根据牛顿第二定律，作用在物体上的力等于物体动量的变化率：

$$
\boldsymbol {F} = \frac {\mathrm{d} \boldsymbol {p} _ {\mathrm{mech}}}{\mathrm{d} t}
$$

因此，式(8.20)可以写成如下形式 $^{5}$ ：

$$
\frac {\mathrm{d} \boldsymbol {p} _ {\text { mech }}}{\mathrm{d} t} = - \varepsilon_ {0} \mu_ {0} \frac {\mathrm{d}}{\mathrm{d} t} \int_ {\mathcal {V}} \boldsymbol {S} \mathrm{d} \tau + \oint_ {\mathcal {S}} \vec {\boldsymbol {T}} \cdot \mathrm{d} \boldsymbol {a}\tag{8.27}
$$

其中， $p_{mech}$ 代表体积 V 内所有粒子的总（机械）动量，上式在结构上和坡印亭定理相似，也具有一个类似的解释：第一项积分代表储存在电磁场中的动量：

$$
\boldsymbol {p} = \mu_ {0} \varepsilon_ {0} \int_ {\mathcal {V}} \boldsymbol {S} \mathrm{d} \tau\tag{8.28}
$$

而第二个积分代表单位时间内通过表面流入的动量。方程(8.27)是电动力学中动量守恒的表达式：如果机械动量增加，要么是场的动量减少，要么是场通过表面携带动量进入体积。显然动量密度为

$$
\boxed {\boldsymbol {g} = \mu_ {0} \varepsilon_ {0} \boldsymbol {S} = \varepsilon_ {0} (\boldsymbol {E} \times \boldsymbol {B})}\tag{8.29}
$$

而场传输的动量流为 $-\vec{T}$ （具体说， $-\vec{T} \cdot \mathrm{d}\pmb{a}$ 是单位时间通过 $\mathrm{d}\pmb{a}$ 的动量）。

如果体积 $\nu$ 中的动量不改变（例如，我们在谈论一个虚空的空间区域），于是

$$
\int \frac {\partial \pmb {g}}{\partial t} \mathrm{d} \tau = \oint \vec {\boldsymbol {T}} \cdot \mathrm{d} \pmb {a} = \int \nabla \cdot \vec {\boldsymbol {T}} \mathrm{d} \tau
$$

从而

$$
\frac {\partial \boldsymbol {g}}{\partial t} = \nabla \cdot \vec {T}\tag{8.30}
$$

这是电磁动量的“连续性方程”——g（动量密度）扮演了 $\rho$ （电荷密度）的角色，而 $-\vec{T}$ （动量流密度）扮演了 J（电流密度）的角色。此式表达了电磁动量的局域守恒。然而，一般来说（当周围有电荷存在时），电磁场动量本身以及机械动量本身并不守恒——电荷和场交换动量，只有总动量守恒。

请注意，坡印亭矢量扮演两个十分不同的角色：S 自身是单位时间内电磁场通过单位面积传输的能量，同时 $\mu_{0}\varepsilon_{0}S$ 是电磁场单位体积具有的动量 $^{6}$ 。类似地， $\vec{T}$ 也扮演两个角色： $\vec{T}$ 自身是作用在表面上的电磁应力（单位面积上的力），同时， $-\vec{T}$ 描述场传输的动量（动量流密度）。

例题8.3 长为 $l$ 的长同轴电缆由内导线（半径为 $a$ ）和外导线（半径为 $b$ ）组成。如图8.5所示，在导线一端接有电池，另一端接有电阻。内导线带有均匀分布的电荷，每单位长度上电荷为 $\lambda$ 并且载有稳定向右的电流 $I$ ；外导线具有相反的电荷和电流。问：电磁场具有的动量为多少？

![](images/030e612e269315d11eebd2864586055a383c55b2c705a84a3849475d083f0ac8.jpg)  
图8.5

[解答] 同轴电缆内的电场和磁场分别为

$$
\pmb {E} = \frac {1}{2 \pi \varepsilon_ {0}} \frac {\lambda}{s} \hat {s}, \quad \pmb {B} = \frac {\mu_ {0}}{2 \pi} \frac {I}{s} \hat {\phi}
$$

因此，相应坡印亭矢量为

$$
S = \frac {\lambda I}{4 \pi^ {2} \varepsilon_ {0} s ^ {2}} \hat {z}
$$

于是能量沿导线传递，从电池传向电阻。事实上，传输功率为

$$
P = \int S \cdot \mathrm{d} a = \frac {\lambda I}{4 \pi^ {2} \varepsilon_ {0}} \int_ {a} ^ {b} \frac {1}{s ^ {2}} 2 \pi s \mathrm{d} s = \frac {\lambda I}{2 \pi \varepsilon_ {0}} \ln (b / a) = I V
$$

它也应该如此。

电磁场的动量为

$$
p = \mu_ {0} \varepsilon_ {0} \int S \mathrm{d} \tau = \frac {\mu_ {0} \lambda I}{4 \pi^ {2}} \hat {z} \int_ {a} ^ {b} \frac {1}{s ^ {2}} l 2 \pi s \mathrm{d} s = \frac {\mu_ {0} \lambda I l}{2 \pi} \ln (b / a) \hat {z} = \frac {I V l}{c ^ {2}} \hat {z}
$$

这是一个极为令人惊讶的结果。导线并没有运动，电场 E 和磁场 B 也是静态的，然而我们被告知系统具有动量！直觉告诉我们，这并不是全部。这一佯谬的解决要等到第 12 章（例题 12.12）。

假设现在我们增大电阻，这样电流就会减小。变化的磁场会诱导一个电场（式7.20）：

$$
\boldsymbol {E} = \left[ \frac {\mu_ {0}}{2 \pi} \frac {\mathrm{d} I}{\mathrm{d} t} \ln s + K \right] \hat {\boldsymbol {z}}
$$

这个电场会对内外导线上的电荷 $\pm \lambda$ 施加一个作用力：

$$
\boldsymbol {F} = \lambda l \left[ \frac {\mu_ {0}}{2 \pi} \frac {\mathrm{d} I}{\mathrm{d} t} \ln a + K \right] \hat {\boldsymbol {z}} - \lambda l \left[ \frac {\mu_ {0}}{2 \pi} \frac {\mathrm{d} I}{\mathrm{d} t} \ln b + K \right] \hat {\boldsymbol {z}} = - \frac {\mu_ {0} \lambda l}{2 \pi} \frac {\mathrm{d} I}{\mathrm{d} t} \ln (b / a) \hat {\boldsymbol {z}}
$$

当电流减小到零时，电磁场传给导线的总动量为

$$
p _ {\mathrm{mech}} = \int F \mathrm{d} t = \frac {\mu_ {0} \lambda I l}{2 \pi} \ln (b / a) \hat {z}
$$

这正是之前储存在电磁场中的动量。

习题8.5 设想两个平行的无限大薄片带有均匀的面电荷 $+\sigma$ （在 $z = d$ 处）和 $-\sigma$ （在 $z = 0$ 处）。它们以恒定速率 $v$ 沿 $y$ 方向上移动（如同习题5.17）。

(a) 在面积为 $A$ 的区域中电磁动量是多少？

（b）现在假设上面薄片缓慢向下移动（速率 u），直到到达下面薄片，因此场消失。通过计算全部电荷（ $q = \sigma A$ ）所受的合力，表明传送到薄片上的冲量等于最初存储在场中的动量。[提示：当上面薄片经过时，磁场降至零，感应出电场，该电场向下面薄片传送冲量。]

习题8.6 如图8.6所示，一个带电平行板电容器（板间有均匀电场 $E = E\hat{z}$ ）放置在均匀磁场 $B = B\hat{x}$ 中。

(a) 求两板之间的电磁动量。

(b) 用一个具有电阻的导线连接两平板，沿着轴方向，电容开始缓慢放电。导线中的电流会受到磁场力；求放电过程中系统受到的总冲量。 $^{7}$

![](images/d7364f4cbf94e0bc248403fa526c26d830248f815e95d514bf72d97a7c32c91a.jpg)  
图8.6

习题8.7 考虑一个无限大平板电容器，下板面（在 $z = -d / 2$ 处）具有面电荷密度为 $-\sigma$ ，上板面（在 $z = +d / 2$ 处）具有面电荷密度为 $+\sigma$ 。

（a）确定两板之间的电磁场应力张量的九个分量。将你的结果表示成如下 $3 \times 3$ 矩阵的形式：

$$
\left( \begin{array}{c c c} T _ {x x} & T _ {x y} & T _ {x z} \\ T _ {y x} & T _ {y y} & T _ {y z} \\ T _ {z x} & T _ {z y} & T _ {z z} \end{array} \right)
$$

(b) 利用式 (8.21) 求作用在上板面单位面积上的力。同式 (2.51) 比较。

(c) 单位时间内穿过 $xy$ 平面（或者是两板之间的任意一个平行于板面的平面）单位面积的动量是多少？

(d) 当然必须有机械力维持极板的分离——或许电容器充满了具一定压强的绝缘材料。假设我们突然移开这些绝缘物；(c) 的动量通量现在被极板吸收，而极板开始运动。求单位时间内给予上板面的动量（也就是说，作用在上板面上的力），同（b）的结果做比较。[注意：这并非一个其他的力，而仅是用不同的方法计算相同的力——在（b）中我们用力学定律求解，（d）中用动量守恒求解。]

## 8.2.4 角动量

到现在为止电磁场具有了自己的性质（一开始它们只是作为电荷间相互作用的中介）。它们具有能量密度 [式 (8.5)]:

$$
u = \frac {1}{2} \left(\varepsilon_ {0} E ^ {2} + \frac {1}{\mu_ {0}} B ^ {2}\right)\tag{8.31}
$$

也具有动量密度 [式 (8.29)]:

$$
\boldsymbol {g} = \varepsilon_ {0} (\boldsymbol {E} \times \boldsymbol {B})\tag{8.32}
$$

同样，角动量密度为

$$
\ell = \boldsymbol {r} \times \boldsymbol {g} = \varepsilon_ {0} [ \boldsymbol {r} \times (\boldsymbol {E} \times \boldsymbol {B}) ]\tag{8.33}
$$

即使是理想的静场也可以具有动量和角动量，只要 $E \times B$ 不为零，并且只有当这些场的作用考虑在内时守恒律才能得以保持。

例题8.4 设想有一个半径为 $R$ 的长螺线管线圈，单位长度绕有 $n$ 匝，载有电流 $I$ 。有两个长为 $l$ 的圆筒（不导电）与螺线管同轴，螺线管内的圆筒半径为 $a$ ，表面均匀带有电荷 $Q$ ；螺线管外的圆筒半径为 $b$ ，均匀带有电荷 $-Q$ （如图8.7所示，设 $l \gg b$ ）。当螺线管中电流逐渐减小时，圆筒开始旋转，就像我们在例题7.8中见到的一样。问：这些角动量来自哪里？

![](images/a72d59c9065377a107c5279d27f129395f8c7e55b4ab42bb106d3becbbf34881.jpg)  
图8.7

$^{8}$ 这是 “Feynman 盘佯谬” 的一个变形（R.P.Feyman,R.B.Leighton 和 M.Sand, The Feyman Lectures, vol2.pp.17-5 (Reading, Mass: Addison-Wesley, 1964)，由 F. L. Boos (Am. J. Phys.52, 756 (1984)) 提出。R. H. Romer 早先提出过一个相似的例子（Am.J.Phys.34, 772 (1966)）。进一步的文献，参阅 T.-C. E. Ma, Am. J. Phys.54, 949 (1986)。

[解答] 这些角动量起初储存在电磁场里。在电流变为零之前，在两管层之间存在电场

$$
\pmb {E} = \frac {Q}{2 \pi \varepsilon_ {0} l} \frac {1}{s} \hat {\pmb {s}} (a <   s <   b)
$$

在螺线管内存在磁场

$$
\boldsymbol {B} = \mu_ {0} n I \hat {\boldsymbol {z}} (s <   R)
$$

因此，在 $a < s < R$ 区域中动量密度[式(8.29)]为

$$
g = - \frac {\mu_ {0} n I Q}{2 \pi l s} \hat {\phi}
$$

角动量密度的 $z$ 分量为

$$
(\boldsymbol {r} \times \boldsymbol {g}) _ {z} = - \frac {\mu_ {0} n I Q}{2 \pi l}
$$

如结果所示，这是一个常量。用它乘以体积 $\pi (R^2 -a^2)l,$ 我们得到电磁场所存储的总角动量

$$
\boldsymbol {L} = - \frac {1}{2} \mu_ {0} n I Q \left(R ^ {2} - a ^ {2}\right) \hat {\boldsymbol {z}}\tag{8.34}
$$

当减小电流时（原文此处为“关闭”，按后面的解答，改为“减小”。——译者注），根据法拉第定律，变化的磁场产生一个环绕的电场：

$$
\boldsymbol {E} = \left\{ \begin{array}{l l} - \frac {1}{2} \mu_ {0} n \frac {\mathrm{d} I}{\mathrm{d} t} \frac {R ^ {2}}{s} \hat {\phi} & (s > R) \\ - \frac {1}{2} \mu_ {0} n \frac {\mathrm{d} I}{\mathrm{d} t} s \hat {\phi} & (s <   R) \end{array} \right.
$$

因而，作用在外面圆筒的力矩为

$$
\boldsymbol {N} _ {b} = \boldsymbol {r} \times (- Q \boldsymbol {E}) = \frac {1}{2} \mu_ {0} n Q R ^ {2} \frac {\mathrm{d} I}{\mathrm{d} t} \hat {z}
$$

它使外面圆筒产生角动量

$$
L _ {b} = \frac {1}{2} \mu_ {0} n Q R ^ {2} \hat {z} \int_ {I} ^ {0} \frac {\mathrm{d} I}{\mathrm{d} t} \mathrm{d} t = - \frac {1}{2} \mu_ {0} n I Q R ^ {2} \hat {z}
$$

类似地，作用在内部圆筒上的力矩为

$$
N _ {a} = - \frac {1}{2} \mu_ {0} n Q a ^ {2} \frac {\mathrm{d} I}{\mathrm{d} t} \hat {z}
$$

增加的角动量为

$$
L _ {a} = \frac {1}{2} \mu_ {0} n I Q a ^ {2} \hat {z}
$$

所以 $L_{\mathrm{em}} = L_a + L_b$ 总是成立：电磁场失去的角动量刚好等于内外圆筒获得的角动量，（电磁场加上物质的）总角动量守恒。

习题8.8 在例题8.4中假设我们用减小电场来代替减小磁场（即减小电流 $I$ ），在两圆筒之间接一个弱导电 $^{10}$ 的径向辐条电阻（我们在螺线管中开一个狭缝，以保证两壳层可以自由旋转）。由作用在辐条中电流上的磁场力，求整个放电过程中传递给圆筒的总角动量（注意：内外壳层现在被连接在一起，一起旋转）。同之前存储在电磁场中的总角动量[式(8.34)]做比较。（注意：在两个例子中，角动量从电磁场传递给圆筒的物理机理完全不同，在例题8.4中起作用的是法拉第定律，在本题中是洛伦兹力定律。)

习题 8.9 两个同心球面上分别有均匀分布的电荷 +Q（半径 a）和 -Q（半径 b > a），并处在 $B = B_{0}\hat{z}$ 的均匀磁场中。

(a) 求出场的角动量（相对于球心）。

（b）现在将磁场逐渐撤除，求每个球面上的转矩以及系统的角动量。

!习题8.10 $^{11}$ 设想一个半径为 $R$ 的均匀磁化铁球，带有电荷 $Q$ 和均匀磁化强度 $M = M\hat{z}$ 。铁球开始时处于静止。

(a) 计算存储在电磁场中的角动量。

（b）假设该球被逐渐（均匀）去磁（或许加热到居里温度以上）。用法拉第定律确定感应电场，求出这个电场作用在球体上的扭矩，求出在整个去磁过程中传递给球体的总角动量。

(c) 如果我们在球体北极连接一个接地导线使球体放电来代替去磁。假设球面上电流的流动使电荷密度保持均匀。用洛伦兹力定律确定作用在球上的力矩，并且计算整个放电过程中传递给球的总角动量。（球面处的磁场并不连续……这有影响吗？）[答案： $\frac{2}{9}\mu_{0}MQR^{2}$ ]

## 8.3 磁场力不做功 $^{12}$

这里可能是重新审视磁力不起作用这一旧佯谬的好地方 [式 (5.11)]。那用磁力起重机吊起一辆报废汽车的残骸如何？有人在对汽车做功，如果不是磁场，那是谁？这辆车是铁磁性的；在磁场存在的情况下，它包含许多微观磁偶极子（实际上是带自旋的电子），它们都排成一行。由此产生的磁化相当于围绕表面流动的束缚电流，因此让我们将汽车建模为一个圆形电流环——事实上，让它成为一个以角速度 $\omega$ 旋转的线电荷 $\lambda$ 的绝缘环（图8.8）。

![](images/7bc81d5dcb485b1bd6231e603327d8911fe77fb6b5ad87df5008063e09953ec8.jpg)  
图8.8

电流环所受的向上磁力为 [式 (6.2)]

$$
F = 2 \pi I a B _ {s}\tag{8.35}
$$

其中 $B_{s}$ 是磁场的径向分量 $^{13}$ ，而 $I = \lambda \omega a$ 。如果环上升了一段距离 dz（而磁体本身保持原位），则对其所做的功为

$$
\mathrm{d} W = 2 \pi a ^ {2} \lambda \omega B _ {s} \mathrm{d} z\tag{8.36}
$$

这增加了电流环的势能。谁做的功？粗看下来，似乎是磁场承担，但我们已经了解到（例题5.3）事实并非如此——随着环的上升，磁力垂直于环中电荷的合速度，因此它对它们没有做功。

然而，与此同时，在环中感应出动生电动势，这与电荷的流动相反，从而降低了其角速度：

$$
\mathcal {E} = - \frac {\mathrm{d} \varPhi}{\mathrm{d} t}
$$

这里 $\mathrm{d}\varPhi$ 是环在 $t$ 时刻通过“带”在 $t + \mathrm{d}t$ 时刻加入的通量（图8.9）：

$$
\mathrm{d} \varPhi = B _ {s} 2 \pi a \mathrm{d} z
$$

![](images/43bb8736c8fa8498d331afe7ac21fcb81d1b3c2622c36ece1f56e451fd89c87c.jpg)  
图8.9

现在

$$
\mathcal {E} = \oint \boldsymbol {f} \cdot \mathrm{d} \boldsymbol {l} = f (2 \pi a)
$$

其中 f 是单位电荷的受力。于是

$$
f = - B _ {s} \frac {\mathrm{d} z}{\mathrm{d} t}\tag{8.37}
$$

微段 $\mathrm{d}l$ 上受力为 $f\lambda \mathrm{d}l$ ，于是环受到的力矩为

$$
N = a \left(- B _ {s} \frac {\mathrm{d} z}{\mathrm{d} t}\right) \lambda (2 \pi a)
$$

对环所做的功（减缓了转动）为 $N\,d\phi = N\omega dt$ ，或者

$$
\mathrm{d} W = - 2 \pi a ^ {2} \lambda \omega B _ {s} \mathrm{d} z\tag{8.38}
$$

环的转动变慢，它失去的转动动能 [式 (8.38)] 正好等于其获得的势能 [式 (8.36)]。磁场全部所做的是把一种形式的能量转化为另一种。如果你允许一些草率的语言，则可以说磁场力竖直分量 [式 (8.35)] 所做的功与水平分量 [式 (8.37)] 所做的功大小相等，符号相反 $^{14}$ 。

磁铁呢？在这个过程中，它是完全被动的吗？假设我们把它建模为一个大圆环（半径为 $b$ ），放在桌子上，通有电流 $I_b$ ；“报废汽车”是一个相对较小的电流回路（半径为 $a$ ），位于正下方的地板上，通有电流 $I_a$ （图8.10）。这一次，为了换一下做法，让我们假设两个电流都是恒定的（我们将在每个电流环中包含一个稳压电源 $^{15}$ ）。平行电流相互吸引，我们建议将小环从地板上抬起，仔细跟踪所做的功和谁做功。

![](images/cc7b39551d03030a96d796548062450987e3441331314ed055db04262085a68a.jpg)  
图8.10

让我们开始调节电流，以让小环在桌子下方一段距离 h 处 “浮动”，而磁力正好与小环的重量 $(m_{a}g)$ 平衡。我让你计算磁力（习题 8.11）：

$$
F _ {\mathrm{mag}} = \frac {3 \pi}{2} \mu_ {0} I _ {a} I _ {b} \frac {a ^ {2} b ^ {2} h}{(b ^ {2} + h ^ {2}) ^ {5 / 2}} = m _ {a} g\tag{8.39}
$$

现在环上升一个无穷小的距离 $\mathrm{dz}$ ；对它所做的功等于它获得的势能增加量

$$
\mathrm{d} W _ {g} = m _ {a} g \mathrm{d} z = \frac {3 \pi}{2} \mu_ {0} I _ {a} I _ {b} \frac {a ^ {2} b ^ {2} h}{(b ^ {2} + h ^ {2}) ^ {5 / 2}} \mathrm{d} z\tag{8.40}
$$

谁做的功？是磁场吗？不是！而是由维持线圈 a 中电流的电源（例题 5.3）做的功。环 a 上升，其中动生电动势也就产生。通过环 a 的磁通量为

$$
\Phi_ {a} = M I _ {b}
$$

其中 $M$ 为两个环之间的互感系数（习题7.22）：

$$
M = \frac {\pi \mu_ {0}}{2} \frac {a ^ {2} b ^ {2}}{(b ^ {2} + h ^ {2}) ^ {3 / 2}}
$$

线圈 $a$ 中动生电动势

$$
\begin{array}{r l} \mathcal {E} _ {a} & = - \frac {\mathrm{d} \varPhi_ {a}}{\mathrm{d} t} = - I _ {b} \frac {\mathrm{d} M}{\mathrm{d} t} = - I _ {b} \frac {\mathrm{d} M}{\mathrm{d} h} \frac {\mathrm{d} h}{\mathrm{d} t} \\ & = - I _ {b} \left(- \frac {3}{2}\right) \frac {\pi \mu_ {0}}{2} \frac {a ^ {2} b ^ {2}}{(b ^ {2} + h ^ {2}) ^ {5 / 2}} 2 h \frac {(- \mathrm{d} z)}{\mathrm{d} t} \end{array}
$$

电源（抵抗这一动生电动势）所做的功为

$$
\mathrm{d} W _ {a} = - \mathcal {E} _ {a} I _ {a} \mathrm{d} t = \frac {3 \pi}{2} \mu_ {0} I _ {a} I _ {b} \frac {a ^ {2} b ^ {2} h}{(b ^ {2} + h ^ {2}) ^ {5 / 2}} \mathrm{d} z\tag{8.41}
$$

——与提升线圈所做的功 [式 (8.40)] 相等。

同时，由于下面线圈中磁通量的变化导致上面线圈有法拉第感应电动势

$$
\Phi_ {b} = M I _ {a} \Rightarrow \mathcal {E} _ {b} = - I _ {a} \frac {\mathrm{d} M}{\mathrm{d} t}
$$

而电源对上面线圈所做的功（以维持上面线圈中电流 $I_{b}$ ）是

$$
\mathrm{d} W _ {b} = - \mathcal {E} _ {b} I _ {b} \mathrm{d} t = \frac {3 \pi}{2} \mu_ {0} I _ {a} I _ {b} \frac {a ^ {2} b ^ {2} h}{(b ^ {2} + h ^ {2}) ^ {5 / 2}} \mathrm{d} z\tag{8.42}
$$

与 $dW_{a}$ 完全相同。这令人尴尬——电源所做的功是提升报废汽车所需能量的两倍！“浪费”的能量到哪里去了？答：它增加了储存在场中的能量。两个载流回路系统中的能量为（见习题 8.12）

$$
U = \frac {1}{2} L _ {a} I _ {a} ^ {2} + \frac {1}{2} L _ {b} I _ {b} ^ {2} + M I _ {a} I _ {b}\tag{8.43}
$$

所以

$$
\mathrm{d} U = I _ {a} I _ {b} \frac {\mathrm{d} M}{\mathrm{d} t} \mathrm{d} t = \mathrm{d} W _ {b}
$$

值得注意的是，所有四种能量增量都是相同的。我们可以这样分摊，回路 a 中的电源为提升下面线圈提供了所需的能量，而回路 b 中的电源则为磁场提供了额外的能量。如果我们感兴趣的只是提升下面线圈所做的功，可以完全忽略上面线圈（以及场中的能量）。

在这两种模型中，磁铁本身都是静止的。这就像通过在回形针上放一块磁铁来提起回形针。但在磁力起重机的情况下，汽车与磁铁保持接触，磁铁连接在一根吊起整个部件的电缆上。作为一个模型，我们可以把上面线圈粘在一个大盒子里，把下面线圈粘在小盒子里，然后加大电流，这样吸引力就比 $m_{a}g$ 大得多；两个盒子扣在一起，我们在上面的盒子上系上一根绳子，然后向上拉（图8.11）。

![](images/59881701fc752dcae7f409b7b6eb8a3de35027bed7effebf5b23ae584a34029d.jpg)  
图8.11

同样的旧机制（例题5.3）占主导：下面线圈上升，磁力向后倾斜；它的垂直分量提升线圈，但它的水平分量与电流相反，因此没有做净功。而这一次，动生电动势被法拉第电动势完全抵消，努力保持电流——通过下环的通量没有变化。（如果你愿意的话，通量增加是因为线圈向上移动，进入一个磁场更高的区域，但通量减少是因为上面线圈的磁场——在空间的任何给定点——随着线圈的向上移动而减小。）不需要电源来维持电流（就这一点而言，上面线圈也不需要电源，因为磁场中的能量不会改变）。是谁举起了汽车？显然是拉绳子的人。磁场的作用只是通过磁力的垂直分量将这种能量传递给汽车。但磁场本身（一如既往）不做功。

磁场不做功的事实直接来源于洛伦兹力定律，所以如果你发现一个例外，你还必须解释为什么该定律不正确。例如，如果磁单极子存在，具有电荷 $q_{\mathrm{e}}$ 和磁荷 $q_{\mathrm{m}}$ 的粒子受力变为[式(7.38)]

$$
\boldsymbol {F} = q _ {\mathrm{e}} (\boldsymbol {E} + \boldsymbol {v} \times \boldsymbol {B}) + q _ {\mathrm{m}} (\boldsymbol {B} - \varepsilon_ {0} \mu_ {0} \boldsymbol {v} \times \boldsymbol {E})\tag{8.44}
$$

在这种情况，磁场可以做功……但是只能对磁荷做功。所以除非你的汽车是磁单极子做的（我不这样认为），这不能解决问题。

一种不那么激进的可能性是，除了电荷外，还存在永久点磁偶极子（电子？），其偶极矩 m 与任何电流无关，而只是简单的存在。洛伦兹力定律获得了一个额外项

$$
\boldsymbol {F} = q (\boldsymbol {E} + \boldsymbol {v} \times \boldsymbol {B}) + \nabla (\boldsymbol {m} \cdot \boldsymbol {B})
$$

磁场可以对这些“内禀”偶极子（它们没有动生或法拉第电动势，因为它们没有磁通量）做功。我不知道是否可以用这种方式构建一个一致的理论，但无论如何，它都不是经典电动力学，经典电动力学是基于安培的假设，即所有磁现象都是由于运动中的电荷引起的，点磁偶极子必须被解释为微小电流回路的极限。

习题8.11 推导式(8.39)[提示：把下面小环视为磁偶极子。]

习题8.12 推导式(8.43)[提示：采用第7.2.4小节的方法，使得两环中的电流从零到终值。]

## 第8章补充习题

习题8.13 $^{16}$ 有一个非常长的半径为 $a$ 的螺线管线圈，单位长度绕有 $n$ 匝，载有电流 $I_s$ 。另一半径 $b \gg a$ 的圆线框与之同轴，线框电阻为 $R$ 。当螺线管中电流减小时，线框中产生感应电流 $I_r$ 。

(a) 计算感应电流 $I_{r}$ ，用 $dI_{s}/dt$ 表示。

(b) 向线框传输的功率 $(I_r^2 R)$ 必然来自螺线管。由计算螺线管外紧邻处的坡印亭矢量证实这一点（电场由螺线管内变化的磁场产生，磁场由线框中的感应电流产生）。对螺线管整个表面做积分验证它与总功率相等。

习题8.14 半径为 $a$ 的无限长圆柱形管沿其轴线以恒定速度 $v$ 运动。它每单位长度的净电荷 $\lambda$ 均匀分布在其表面上。它受半径 $b$ 处另一个圆筒包围，圆筒以相同的速度移动，但携带相反的电荷（ $-\lambda$ ）。求：

(a) 沿轴线方向 $^{17}$ 每单位长度储存的场的能量。

(b) 沿轴线方向每单位长度储存的场的动量。

(c) 每单位时间内通过垂直于圆筒轴线传输的能量。

习题8.15 点电荷 $q$ 位于矩形横截面、内径为 $a$ 、外径为 $a + w$ 和高度为 $h$ 的环形线圈的中心，该线圈密绕 $N$ 匝，通过电流为 $I$ 。

(a) 假设 $w$ 和 $h$ 都远小于 $a$ （以使你可以忽略在线圈横截面上的差异），求这一系统的电磁动量 $\pmb{p}$ 。

（b）现在，足够迅速撤除环形线圈中的电流，以至于当磁场降至零时，该点电荷不会明显移动。证明施加到 $q$ 的冲量等于电磁场中最初存储的动量。[提示：你可能想参考习题7.19。]

习题8.16 $^{18}$ 半径为 $a$ 的球体带有均匀极化矢量 $\pmb{P}$ 和磁化强度 $\pmb{M}$ （并不一定在相同方向）。求这一系统的电磁动量。[答案： $(4 / 9)\pi \mu_0R^3 (M\times P)]$

习题8.17 $^{19}$ 设想电子是一个均匀带电的球壳，总电量为 $e$ ，球壳半径为 $R$ ，自旋角速度为 $\omega$ 。

(a) 计算储存在电磁场中的总能量。

(b) 计算储存在电磁场中的总角动量。

(c) 根据爱因斯坦质能方程 $(E = mc^2)$ ，存储在电磁场总的能量对电子的质量也有贡献。洛伦兹和一些人推测，电子的总质量可用这种方式解释： $U_{\mathrm{em}} = m_{\mathrm{e}}c^{2}$ 。更进一步，假设电子的自旋角动量完全归因于电磁场： $L_{\mathrm{em}} = \hbar / 2$ 。在这两个假设下，确定电子的半径和角速度。它们的乘积 $\omega R$ 等于什么？这个经典模型是否有意义？

习题8.18 在有磁荷存在时，导出 $u$ 、 $S$ 、 $g$ 和 $\vec{T}$ 的表达式 [提示：从一般麦克斯韦方程(7.44)和洛伦兹力定律式(8.44)出发，遵循第8.1.2、8.2.2和8.2.3小节的推导。]

习题8.19 $^{20}$ 假设你有一个电荷 $q_{\mathrm{e}}$ 和一个磁单极荷 $q_{\mathrm{m}}$ 。电荷产生的电场为

$$
\pmb {E} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q _ {\mathrm{e}}}{r ^ {2}} \hat {\pmb {r}}
$$

磁荷产生的磁场为

$$
B = \frac {\mu_ {0}}{4 \pi} \frac {q _ {\mathrm{m}}}{r ^ {2}} \hat {r}
$$

求电磁场所具有的总角动量，设两荷相距为 $d$ 。[答案： $(\mu_0 / 4\pi)q_{\mathrm{e}}q_{\mathrm{m}}]^{21}$

习题8.20 考虑一个理想静止磁偶极子 $m$ 处在一个静电场 $\pmb{E}$ 中，证明场具有动量

$$
\pmb {p} = - \varepsilon_ {0} \mu_ {0} (\pmb {m} \times \pmb {E})\tag{8.45}
$$

[提示：有好几种方法证明。最简单的方法是从 $p = \varepsilon_0\int (E\times B)\mathrm{d}\tau$ 开始，写出 $E = -\nabla V$ ，利用分部积分得

$$
\pmb {p} = \varepsilon_ {0} \mu_ {0} \int V \pmb {J} \mathrm{d} \tau
$$

至此，这对于任何局域静态场都正确。对一个局限在原点附近无穷小邻域的流，我们可以取近似 $V(\pmb{r}) \approx V(\mathbf{0}) - E(\mathbf{0}) \cdot \pmb{r}$ 。将偶极子视为一个电流环，并利用式(5.82)和式(1.108)。]22

习题 8.21 在例题 8.4 中因为两个圆筒在转动（比如说，角速度为 $\omega_{a}$ 和 $\omega_{b}$ ），实际上，即使是在螺线管中电流减小到零时，还有一个剩余磁场，因此场还会有剩余的角动量。如果圆筒非常重，这种修正可以忽略，不过假如不做这种假设，会更加有趣 $^{23}$ 。

(a) 计算最后的电磁场中的角动量（作为 $\omega_{a}$ 和 $\omega_{b}$ 的函数）。[定义 $\omega = \omega \hat{z}$ ，从而 $\omega_{a}$ 和 $\omega_{b}$ 可以是正的或者是负的。]

(b) 当圆筒开始转动时，它们变化的磁场会感生一个额外的沿方位角方向的电场，这样反过来会对圆筒有一个附加力矩，求出相应的角动量，同（a）中结果做比较。[答案： $-\mu_0Q^2\omega_b(b^2 -a^2) / 4\pi l\hat{z} ]$

习题8.22 $^{24}$ 距离无限长螺线管（半径为 $R$ ，单位长度绕有 $n$ 匝，电流为 $I$ ）轴线 $a > R$ 处有一个点电荷 $q$ 。求出电磁场中的动量和角动量（设 $q$ 在 $x$ 轴上，螺线管沿 $z$ 轴。将螺线管视为一个绝缘体，这样就不用考虑螺线管表面的感应电荷）。[答案： $p = (\mu_0 q n I R^2 / 2a) \hat{y}; L = 0$ ]

## 习题8.23

(a) 继续第 8.1.2 节的讨论，从式 (8.6) 开始，不过把 J 替换为 $J_{f}$ 。证明坡印亭矢量将会变为

$$
\pmb {S} = \pmb {E} \times \pmb {H}\tag{8.46}
$$

电磁场能量密度的变化率为

$$
\frac {\partial \boldsymbol {u}}{\partial t} = \boldsymbol {E} \cdot \frac {\partial \boldsymbol {D}}{\partial t} + \boldsymbol {H} \cdot \frac {\partial \boldsymbol {B}}{\partial t}
$$

对于线性介质，证明 $^{25}$

$$
u = \frac {1}{2} (\boldsymbol {E} \cdot \boldsymbol {D} + \boldsymbol {B} \cdot \boldsymbol {H})\tag{8.47}
$$

（b）用同样的方法，重新讨论第8.2.2节，从式(8.15)开始，用 $\rho_{f}$ 和 $J_{f}$ 替换 $\rho$ 和 $J$ 。不用去费力建立麦克斯韦应力张量，证明动量密度为

$$
\boldsymbol {g} = \boldsymbol {D} \times \boldsymbol {B}\tag{8.48}
$$

习题8.24 半径为 $R$ 、质量为 $M$ 的圆盘带有 $n$ 个点电荷（ $q$ ），这些点电荷以规则的间隔附着在其边缘周围。在时间 $t = 0$ 时，圆盘位于 $xy$ 平面内，中心位于原点，释放后以角速度 $\omega_0$ 绕 $z$ 轴旋转。该磁盘处在（与时间无关的）外部磁场中：

$$
\boldsymbol {B} (s, z) = k (- s \hat {s} + 2 z \hat {z})
$$

其中 $k$ 为一个常量。

(a) 求该圆盘作为时间函数的中心位置 $z(t)$ 及角速度 $\omega(t)$ 。（忽略重力。）

（b）描述该圆盘的运动，并检查总（动能）能量——平移加旋转——是否恒定，确认磁力不做功 $^{27}$ 。

## 9.1 一维波

## 9.1.1 波动方程

什么是“波”？我想我不能给你一个完全满意的答案——这个概念本身有些模糊——但这里给出一个解释作为对它理解的开始：波是连续介质的一个扰动并以固定的形状和一定的速度传播。我必须立刻加一些限制：在吸收存在的情形，波在传播中尺寸会减小；如果介质有色散，不同频率波传播的速度会不同；在二维或三维空间，当波向外传播时，它的幅度会减小；另外，驻波当然根本就不传播。但是这些限制是细节，让我们从最简单的情形开始：波形固定，波速不变（图9.1）。

![](images/2a3851f8b0e046b48ccaed1fd90fae53f4164d61c4ed4f5761c50ab45d2157ef.jpg)  
图9.1

怎样从数学上表示波这样一个对象？图中画出了波在两个不同时刻时的情形：一度在 $t = 0$ 时刻及稍后 $t$ 时刻——波形上的每一点简单地向右移动了一个量 $vt$ ，这里 $v$ 是波速。这个波也许是拉紧弦的一端的振动产生的。以 $f(z,t)$ 表示弦上 $z$ 点处在 $t$ 时刻的位移。给定弦的初始形状为 $g(z) = f(z,0)$ ，以后的形状 $f(z,t)$ 是什么？显然，在以后 $t$ 时刻， $z$ 点处弦的位移，与 $t = 0$ 时刻，在 $z$ 点左边相距 $vt$ 处（即在 $z - vt$ 处）的位移相同：

$$
f (z, t) = f (z - v t, 0) = g (z - v t)\tag{9.1}
$$

这一叙述（从数学上）抓住了波动的本质。它告诉我们函数 $f(z,t)$ 可能以任何旧方式依赖 $t$ 和 $z$ ，事实上，它以一个很特别的组合 $z - vt$ 依赖它们。如果是这样，函数 $f(z,t)$ 就表示在 $z$ 方向以一固定形状和速度 $v$ 传播的波。如果 $A$ 和 $b$ 是常数（具有适当的单位），下

面这些式子

$$
f _ {1} (z, t) = A \mathrm{e} ^ {- b (z - v t) ^ {2}}, \quad f _ {2} (z, t) = A \sin [ b (z - v t) ], \quad f _ {3} (z, t) = \frac {A}{b (z - v t) ^ {2} + 1}
$$

都代表波（当然有不同形状），但

$$
f _ {4} (z, t) = A \mathrm{e} ^ {- b \left(b z ^ {2} + v t\right)} \quad {\text {和}} \quad f _ {5} (z, t) = A \sin (b z) \cos (b v t) ^ {3}
$$

不是波。

为何拉紧的弦可以传播波？事实上，这源自牛顿第二定律。想象一个张力为 $T$ 的相当长的弦，它在横向上偏离平衡位置，在区间 $z$ 和 $z + \mathrm{d}z$ （图9.2）上净横向力为

$$
\Delta F = T \sin \theta^ {\prime} - T \sin \theta
$$

这里 $\theta'$ 和 $\theta$ 分别是弦和 $z-$ 方向在 $z + \mathrm{d}z$ 点和 $z$ 点所成的角。假如弦的形变不太大，这些角度会很小（图中显然被放大了），我们可以用正切函数代替正弦函数，

$$
\Delta F \cong T (\tan \theta^ {\prime} - \tan \theta) = T \left(\frac {\partial f}{\partial z} \Big | _ {z + \Delta z} - \frac {\partial f}{\partial z} \Big | _ {z}\right) \cong T \frac {\partial^ {2} f}{\partial z ^ {2}} \Delta z
$$

![](images/b2c590ff77279a56fa7113ad8adb9c440dbdb54254ae5aa04885106a3887859c.jpg)  
图9.2

如果单位长度的质量是 $\mu$ ，由牛顿第二定律得

$$
\Delta F = \mu (\Delta z) \frac {\partial^ {2} f}{\partial z ^ {2}}
$$

所以有

$$
\frac {\partial^ {2} f}{\partial z ^ {2}} = \frac {\mu}{T} \frac {\partial^ {2} f}{\partial t ^ {2}}
$$

显然，在弦上的小的扰动满足方程

$$
\boxed {\frac {\partial^ {2} f}{\partial z ^ {2}} = \frac {1}{v ^ {2}} \frac {\partial^ {2} f}{\partial t ^ {2}}}\tag{9.2}
$$

这里 v（我们后面会看到它表示波的传播速度）为

$$
v = \sqrt {\frac {T}{\mu}}\tag{9.3}
$$

式(9.2)称为（经典）波动方程（wave equation），具有下面形式的函数都是它的解：

$$
f (z, t) = g (z - v t)\tag{9.4}
$$

(即所有以特定的组合 z-vt 依赖变量 z 和 t 的函数)，而我们刚刚知道这个函数表示波在 z 方向以速度 v 传播。因式 (9.3) 意味着

$$
{\frac {\partial f}{\partial z}} = {\frac {\mathrm{d} g}{\mathrm{d} u}} {\frac {\partial u}{\partial z}} = {\frac {\mathrm{d} g}{\mathrm{d} u}}, \quad {\frac {\partial f}{\partial t}} = {\frac {\mathrm{d} g}{\mathrm{d} u}} {\frac {\partial u}{\partial t}} = - v {\frac {\mathrm{d} g}{\mathrm{d} u}}
$$

以及

$$
{\frac {\partial^ {2} f}{\partial z ^ {2}}} = {\frac {\partial}{\partial z}} \left({\frac {\mathrm{d} g}{\mathrm{d} u}}\right) = {\frac {\mathrm{d} ^ {2} g}{\mathrm{d} u ^ {2}}} {\frac {\partial u}{\partial z}} = {\frac {\mathrm{d} ^ {2} g}{\mathrm{d} u ^ {2}}}
$$

$$
{\frac {\partial^ {2} f}{\partial t ^ {2}}} = - v {\frac {\partial}{\partial t}} \left({\frac {\mathrm{d} g}{\mathrm{d} u}}\right) = - v {\frac {\mathrm{d} ^ {2} g}{\mathrm{d} u ^ {2}}} {\frac {\partial u}{\partial t}} = v ^ {2} {\frac {\mathrm{d} ^ {2} g}{\mathrm{d} u ^ {2}}}
$$

故有

$$
\frac {\mathrm{d} ^ {2} g}{\mathrm{d} u ^ {2}} = \frac {\partial^ {2} f}{\partial z ^ {2}} = \frac {1}{v ^ {2}} \frac {\partial^ {2} f}{\partial t ^ {2}}
$$

证毕。

注意 $g(u)$ 可以是任何（可微）函数。如果扰动在传播中不改变形状，它就满足波动方程。

但是具有形式 $g(z - vt)$ 的函数不是唯一的解。波动方程包含 $\pmb{v}$ 的平方，因此通过简单地改变速度的符号我们可得到另一类解：

$$
f (z, t) = h (z + v t)\tag{9.5}
$$

这当然代表一个沿着负 $z$ 方向传播的波，这个解（从物理上看）也是合理的。让人惊奇的是波动方程最一般的解是一个向右和一个向左传播的两个波之和：

$$
f (z, t) = g (z - v t) + h (z + v t)\tag{9.6}
$$

[注意波动方程是线性的（linear）：任何两个解之和仍是方程的解。] 波动方程的每一个解都可表示成这种形式。

如同简单的谐振子方程一样，波动方程在物理中具有普遍性。如果存在振动，就需要用到谐振子方程（至少对小振动的情形）。同样，如果存在波动（不论是在力学、声学、光学或海洋学方面），就要涉及波动方程（可能有小的修改）。

习题9.1 由直接微分，检验本小节中的函数 $f_{1}$ 、 $f_{2}$ 和 $f_{3}$ 满足波动方程， $f_{4}$ 和 $f_{5}$ 不满足。

习题 9.2 证明驻波（standing wave） $f(z,t)=A\sin(kz)\cos(kvt)$ 满足波动方程。把它表示成一个向左和一个向右传播的两个波之和 [式 (9.6)]。

## 9.1.2 正弦波

(i) 术语。在所有的波的形式中，正弦型的

$$
f (z, t) = A \cos [ k (z - v t) + \delta ]\tag{9.7}
$$

是最熟悉的形式。图9.3画出了 $t = 0$ 时刻的这个函数。 $A$ 是波的振幅（amplitude，它取正值，代表距平衡位置的最大位移）。正弦函数的宗量称为相位（phase）， $\delta$ 是相位常数[phase constant，显然，你可把 $\delta$ 加上任何 $2\pi$ 的整数倍而不改变 $f(z,t)$ ，它通常在 $0\leqslant \delta < 2\pi$ 内取值]。注意在 $z = vt - \delta /k$ ，相位是零，这称为“中心极大”。假如 $\delta = 0$ ，中心极大在 $t = 0$ 时通过原点。更一般地， $\delta /k$ 是中心极大（所以也是整个波）“延迟”的距离。最后， $k$ 称为波数（wave number），它与波长（wavelength） $\lambda$ 通过下面的方程相联系：

$$
\lambda = \frac {2 \pi}{k}\tag{9.8}
$$

z 前进 $2\pi/k$ ，正弦函数完成一个周期。

![](images/982e2859788b38b99e1f82f8df9dd7ac27eb22828932796acbea9cd4748d3b23.jpg)  
图9.3

随着时间的流逝，整列波以速度 v 向右前进。在任何固定点 z，弦上下振动，在一个周期（period）

$$
T = \frac {2 \pi}{k v}\tag{9.9}
$$

内完成一次循环。频率（frequency，单位时间内振动的次数） $\nu$ 是

$$
\nu = \frac {1}{T} = \frac {k v}{2 \pi} = \frac {v}{\lambda}\tag{9.10}
$$

对于我们的目的，一个更方便的单位是角频率（angular frequency），这样称谓是因为它类似于匀速圆周运动，表示单位时间内扫过的弧度数：

$$
\omega = 2 \pi \nu = k v\tag{9.11}
$$

通常情况下，用 $\omega$ 而不是用 $\nu$ 写出正弦波更好：

$$
f (z, t) = A \cos (k z - \omega t + \delta)\tag{9.12}
$$

一个波数为 $k$ ，角频率为 $\omega$ ，向左传播的正弦波可写成

$$
f (z, t) = A \cos (k z + \omega t - \delta)\tag{9.13}
$$

常数相因子的符号的选择与前面的一致，即 $\delta / k$ 表示波延迟的距离（因为波现在向左传播，延迟的意思是向右移动）。在 $t = 0$ 时刻，波如图9.4所示。因为余弦函数是一个偶函数，我们因此可把式(9.13)写为

$$
f (z, t) = A \cos (- k z - \omega t + \delta)\tag{9.14}
$$

与式(9.12)比较可以看出，我们仅把 $k$ 的符号改变就可得到一个具有同样的振幅、相因子、频率和波长，但传播方向相反的波。

![](images/a3edbbbca632e2611fca57cf95fb84faa512f32df8063015e2f09fc72bb47622.jpg)  
图9.4

(ii) 复数表示。考虑到欧拉公式（Euler's formula）

$$
\mathrm{e} ^ {\mathrm{i} \theta} = \cos \theta + \mathrm{i} \sin \theta\tag{9.15}
$$

正弦波 [式 (9.12)] 可写成

$$
f (z, t) = \operatorname{Re} \left[ A \mathrm{e} ^ {\mathrm{i} (k z - \omega t + \delta)} \right]\tag{9.16}
$$

式中， $\operatorname{Re}(\xi)$ 表示复数 $\xi$ 的实部。这可使我们引进复波函数（complex wave function）

$$
\tilde {f} (z, t) \equiv \tilde {A} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)}\tag{9.17}
$$

其中复振幅（complex amplitude） $\tilde{A} \equiv A e^{i \delta}$ 吸收了相位常数 $\delta$ 。实际的波函数是 $\tilde{f}$ 的实部：

$$
f (z, t) = \operatorname{Re} [ \tilde {f} (z, t) ]\tag{9.18}
$$

如果知道了 $\tilde{f}$ ，可很容易求出 f。复数表示的优点在于指数函数比正弦和余弦函数更容易做运算处理。

例题9.1 假设你想把两个正弦波求和：

$$
f _ {3} = f _ {1} + f _ {2} = \operatorname{Re} \left(\tilde {f} _ {1}\right) + \operatorname{Re} \left(\tilde {f} _ {2}\right) = \operatorname{Re} \left(\tilde {f} _ {1} + \tilde {f} _ {2}\right) = \operatorname{Re} \left(\tilde {f} _ {3}\right)
$$

其中 $\tilde{f}_3 = \tilde{f}_1 + \tilde{f}_2$ 。这只需要把对应的复波函数相加，然后取实部。特别地，如果它们有相同的频率和波数，

$$
\tilde {f} _ {3} = \tilde {A} _ {1} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)} + \tilde {A} _ {2} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)} = \tilde {A} _ {3} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)}
$$

式中，

$\tilde{A}_{3}=\tilde{A}_{1}+\tilde{A}_{2}$ 或者 $A_{3}e^{i\delta_{3}}=A_{1}e^{i\delta_{1}}+A_{2}e^{i\delta_{2}}$ (9.19)

换句话说，只需把（复数）波幅相加。合成波有相同的频率和波长：

$$
f _ {3} (z, t) = A _ {3} \cos \left(k z - \omega t + \delta_ {3}\right)
$$

由式 (9.19)（习题 9.3）你可容易地求出 $A_{3}$ 和 $\delta$ 。试着不利用复数表示求出它们——你会发现自己要查三角恒等式并艰难地完成复杂的代数运算。

（iii）正弦波函数的线性叠加。尽管正弦函数式(9.17)是个非常特殊的波形，事实上任何波都可以表示成它的线性叠加：

$$
\tilde {f} (z, t) = \int_ {- \infty} ^ {\infty} \tilde {A} (k) \mathrm{e} ^ {\mathrm{i} (k z - \omega t)} \mathrm{d} k\tag{9.20}
$$

这里 $\omega$ 是 $k$ 的函数[式(9.11)]，而我允许 $k$ 取负值是为了包括两个方向传播的波 $^{1}$ 。

$\tilde{A}(k)$ 的表示可由初始条件 $f(z,0)$ 和 $\dot{f} (z,0)$ 利用傅里叶变换理论得到（参看习题9.33），其细节与我们这里的意图不相关。重要的是任何波都可写成正弦波的组合。所以你知道了正弦波的行为，原则上你就知道了任何波的行为。因此，从现在开始我们只关注正弦波。

习题 9.3 利用式 (9.19) 确定 $A_{3}$ 和 $\delta_{3}$ ，用 $A_{1}$ 、 $A_{2}$ 、 $\delta_{1}$ 及 $\delta_{2}$ 表示。

习题 9.4 通过分离变量，从波动方程直接得到式 (9.20)。

## 9.1.3 边界条件：反射与透射

到现在为止，我们假定弦是无限长的——或者说无论如何足够长，以致我们不用担心波到达端点时发生什么。事实上发生什么很大程度上取决于端点是如何连接的——对波所加的具体边界条件。例如，假如第一个弦简单地系在第二个弦上，而两个弦的张力 T 一样，但假定单位长度的质量 $\mu$ 不同，则波速 $v_{1}$ 和 $v_{2}$ 不同（记得 $v = \sqrt{T/\mu}$ ）。为了便利，设结点在 z = 0 处。入射（incident）波

$$
\tilde {f} _ {I} (z, t) = \tilde {A} _ {I} \mathrm{e} ^ {\mathrm{i} (k _ {1} z - \omega t)} \quad (z <   0)\tag{9.21}
$$

从左边入射，产生了一个反射（reflected）波

$$
\tilde {f} _ {R} (z, t) = \tilde {A} _ {R} \mathrm{e} ^ {\mathrm{i} (- k _ {1} z - \omega t)} \quad (z <   0)\tag{9.22}
$$

沿弦 1 返回（故在 $k_{1}$ 前有负号），以及一个透射（transmitted）波

$$
\tilde {f} _ {T} (z, t) = \tilde {A} _ {T} \mathrm{e} ^ {\mathrm{i} (k _ {2} z - \omega t)} \quad (z > 0)\tag{9.23}
$$

沿弦 2 继续传播。

这个入射波 $f_{I}(z,t)$ 是正弦振动（原则上）它向后一直扩展至 $z = -\infty$ ，在整个过程中一直如此。 $f_{R}(z,t)$ 和 $f_{T}(z,t)$ 也是这样（当然，对于后者，振动扩展至 $z = +\infty$ ）。体系的各个部分振动频率相同，均为 $\omega$ （这个频率由在 $z = -\infty$ 处，最初拨动弦的那个人确定）。因为在两个弦上的波速不同，而它们的波长和波数也不同：

$$
\frac {\lambda_ {1}}{\lambda_ {2}} = \frac {k _ {2}}{k _ {1}} = \frac {v _ {1}}{v _ {2}}\tag{9.24}
$$

当然，这一情况是相当人为的——而且入射波和反射波在同一个无限弦上反向传播，观察者将很难把它们分开。也许，你们更愿意考虑一个有限延展的入射波——如图9.5所示的脉冲波。如果乐意，你们可自行解出细节（习题9.5）。这个方法的麻烦在于没有一个有限延展的脉冲是真正的正弦函数。图9.5的波看起来像正弦函数，但它们不是：而是正弦的一小片断，连接着一个完全不同的函数（即：零）。如同其他的波一样，它们可表示成正弦函数的线性叠加[式(9.20)]，但要包括所有的频率和波长。如果你需要单一入射频率（像我们将要讨论的电磁波的情形），必须把波延展到无穷远。（实际中，假如你利用一个非常长的、包含许多振动的脉冲，它就接近于一个单一频率波的理想情形。）

![](images/63b9de5e0620c312d4b5dbb8d69af17d1a1139578bde3e8b3583de1cac8b0903.jpg)  
a) 入射波

![](images/a83b93136a34f81c64fb963000c1bbb48af93b2648c49ac2e7abe2facc49f5fd.jpg)  
b) 反射波和透射波  
图9.5

对于一个正弦入射波，弦的净扰动是

$$
\tilde {f} (z, t) = \left\{ \begin{array}{l l} {\tilde {A} _ {I} \mathrm{e} ^ {\mathrm{i} (k _ {1} z - \omega t)} + \tilde {A} _ {R} \mathrm{e} ^ {\mathrm{i} (- k _ {1} z - \omega t)},} & {\text {对于} z <   0} \\ {\tilde {A} _ {T} \mathrm{e} ^ {\mathrm{i} (k _ {2} z - \omega t)},} & {\text {对于} z > 0} \end{array} \right.\tag{9.25}
$$

在靠近连接点 $(z = 0)$ 处，左边的位移 $(z = 0^{-})$ 必须与右边的位移 $(z = 0^{+})$ 相等——否则两弦间会有一间断点。从数学上讲，在 $z = 0$ 处是连续的：

$$
f \left(0 ^ {-}, t\right) = f \left(0 ^ {+}, t\right)\tag{9.26}
$$

如果那个结点本身的质量可忽略， $f$ 的导数也必须是连续的：

$$
\left. \frac {\partial f}{\partial z} \right| _ {0 ^ {-}} = \left. \frac {\partial \dot {f}}{\partial z} \right| _ {0 ^ {+}}\tag{9.27}
$$

否则在这个结点上会作用有一个净力，因此会产生一个无穷大的加速度（图9.6）。这些边界条件直接应用于实际的波函数 $f(z,t)$ 上。但是因为 $\tilde{f}$ 的虚部与实部的不同仅在于用正弦函数替换余弦函数[式(9.15)]，因此，复波函数 $\tilde{f}(z,t)$ 遵从相同的边界条件：

$$
\tilde {f} \left(0 ^ {-}, t\right) = \tilde {f} \left(0 ^ {+}, t\right), \quad \left. \frac {\partial \tilde {f}}{\partial z} \right| _ {0 ^ {-}} = \left. \frac {\partial \tilde {f}}{\partial z} \right| _ {0 ^ {+}}\tag{9.28}
$$

![](images/4c2790afc1a20cd7ce39f5c407b1641962174a19b3154e76e7b432a4fe22efb2.jpg)  
a) 不连续斜率，力作用在结点

![](images/2cd9bb2b9a4f055338a0b4e37fda0439f6f3ecf3653a283fb4447e41f82165c1.jpg)  
b) 连续斜率，在结点上没有力  
图9.6

当把这些边界条件应用到式(9.25)时，可确定出射波的振幅（ $\tilde{A}_R$ 和 $\tilde{A}_T$ ），它们用入射波的振幅（ $\tilde{A}_I$ ）表示如下：

$$
\tilde {A} _ {I} + \tilde {A} _ {R} = \tilde {A} _ {T}, \quad k _ {1} (\tilde {A} _ {I} - \tilde {A} _ {R}) = k _ {2} \tilde {A} _ {T}
$$

由此可得

$$
\tilde {A} _ {R} = \frac {k _ {1} - k _ {2}}{k _ {1} + k _ {2}} \tilde {A} _ {I}, \quad \tilde {A} _ {T} = \frac {2 k _ {1}}{k _ {1} + k _ {2}} \tilde {A} _ {I}\tag{9.29}
$$

或用速度 [式 (9.24)] 表示:

$$
\tilde {A} _ {R} = \frac {v _ {2} - v _ {1}}{v _ {2} + v _ {1}} \tilde {A} _ {I}, \quad \tilde {A} _ {T} = \frac {2 v _ {2}}{v _ {2} + v _ {1}} \tilde {A} _ {I}\tag{9.30}
$$

实振幅和相位间的关系可表示为

$$
A _ {R} \mathrm{e} ^ {\mathrm{i} \delta_ {R}} = \frac {v _ {2} - v _ {1}}{v _ {2} + v _ {1}} A _ {I} \mathrm{e} ^ {\mathrm{i} \delta_ {I}}, \quad A _ {T} \mathrm{e} ^ {\mathrm{i} \delta_ {T}} = \frac {2 v _ {2}}{v _ {2} + v _ {1}} A _ {I} \mathrm{e} ^ {\mathrm{i} \delta_ {I}}\tag{9.31}
$$

如果第二个弦比第一个轻（ $\mu_2 < \mu_1$ ，故有 $v_2 > v_1$ ），所有三个波有相同的相位（ $\delta_R = \delta_T = \delta_I$ ），出射波振幅为

$$
A _ {R} = \frac {v _ {2} - v _ {1}}{v _ {2} + v _ {1}} A _ {I}, \quad A _ {T} = \frac {2 v _ {2}}{v _ {2} + v _ {1}} A _ {I}\tag{9.32}
$$

如果第二个弦比第一个重 $(\mu_{2} > \mu_{1})$ ，反射波相位相差 $180^{\circ}$ （ $\delta_R + \pi = \delta_T = \delta_I$ ）。换句话说，因为

$$
\cos \left(- k _ {1} z - \omega t + \delta_ {I} - \pi\right) = - \cos \left(- k _ {1} z - \omega t + \delta_ {I}\right)
$$

反射波被 “上下倒置” 了。这种情况下振幅为

$$
A _ {R} = \frac {v _ {1} - v _ {2}}{v _ {2} + v _ {1}} A _ {I}, \quad A _ {T} = \frac {2 v _ {2}}{v _ {2} + v _ {1}} A _ {I}\tag{9.33}
$$

特别是，如果第二个弦质量为无穷大——或者，等效地，如果第一个弦在端点被固定，则有

$$
A _ {R} = A _ {I} \quad \text {以及} \quad A _ {T} = 0
$$

自然则有，在这种情况下没有透射波——所有的波均被反射回去。

!习题9.5 假如沿弦1发出一个具有某种形状的入射波 $g_{I}(z - v_{1}t)$ 。它产生一反射波 $h_R(z + v_1t)$ 和透射波 $g_T(z - v_2t)$ 。由所加的边界条件(9.26)和(9.27)，求出 $h_R$ 和 $g_T$ 。

## 习题9.6

（a）对于两个具有张力 $T$ 并用质量为 $m$ 的结连接的弦，替代式(9.27)，写出其正确的边界条件。

（b）对于结的质量为 $m$ ，第二个弦无质量的情形，求出反射波和透射波的振幅及相位。

!习题9.7 假如第二个弦处于某种黏滞介质中（如蜜糖），这将施加一个与其横向速度成正比的阻力：

$$
\Delta F _ {\mathrm{阻力}} = - \gamma \frac {\partial f}{\partial t} \Delta z
$$

(a) 推导出描述弦运动的修正波动方程。

(b) 假设入射波振动频率为 $\omega$ ，求解该方程，即求形式如 $\tilde{f}(z,t) = \mathrm{e}^{-\mathrm{i}\omega t}\tilde{F}(z)$ 的解。

(c) 证明这个波是衰减（attenuated）的（即随着 $z$ 的增大，波幅减小）。求出用 $\gamma, T, \mu$ 和 $\omega$ 表示的特征穿透距离，在这个距离处，振幅为初始值的 $1 / \mathrm{e}$ 。

(d) 如果一个振幅为 $A_{I}$ 、相位为 $\delta$ 、频率为 $\omega$ 的入射波从左边进入（弦1），求出反射波的振幅和相位。

## 9.1.4 偏振

拨动琴弦产生的波称为横波（transverse），因为弦的位移方向和波的传播方向垂直。如果弦有适当的弹性，通过对弦施加一个小拉力也可在弦上产生压缩波。压缩波在弦上很难看出，但如果用一个机灵鬼 $^{2}$ 试试，压缩波就相当明显（图9.7）。这样的波称为纵波（longitudinal），因为偏离平衡位置的位移与波的传播方向一致。声波就是压缩空气的纵波；而电磁波，我们将会看到，是横波。

$$
v \rightarrow
$$

图9.7

当然，垂直于任何传播直线方向有两个维数，故横波可有两个独立的偏振（polarization）：你可以上下拨动弦（“垂直”偏振——图9.8a），

$$
\tilde {\pmb {f}} _ {v} (z, t) = \tilde {A} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)} \hat {\pmb {x}}\tag{9.34}
$$

或者左右拨动弦（“水平”偏振——图 9.8b），

$$
\tilde {\pmb {f}} _ {h} (z, t) = \tilde {A} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)} \hat {\pmb {y}}\tag{9.35}
$$

或在 $xy$ 平面内沿任何其他方向（图9.8c）：

$$
\tilde {\boldsymbol {f}} (z, t) = \tilde {A} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)} \hat {\boldsymbol {n}}\tag{9.36}
$$

偏振矢量（polarization vector） $\hat{n}$ 确定了振动平面 $^{3}$ 。因为波是横波， $\hat{n}$ 垂直于传播方向：

$$
\hat {\boldsymbol {n}} \cdot \hat {\boldsymbol {z}} = 0\tag{9.37}
$$

利用偏振角（polarization angle） $\theta$ ，有

$$
\hat {\boldsymbol {n}} = \cos \theta \hat {\boldsymbol {x}} + \sin \theta \hat {\boldsymbol {y}}\tag{9.38}
$$

因此，图9.8c的波可认为是两个波的叠加——一个水平偏振，另一个垂直偏振：

$$
\tilde {\pmb {f}} (z, t) = (\tilde {A} \cos \theta) \mathrm{e} ^ {\mathrm{i} (k z - \omega t)} \hat {\pmb {x}} + (\tilde {A} \sin \theta) \mathrm{e} ^ {\mathrm{i} (k z - \omega t)} \hat {\pmb {y}}\tag{9.39}
$$

![](images/5b729e48150ed59c5163a633e01e2e3230877aa18a932ec53053a177660f7a83.jpg)  
a) 垂直偏振

![](images/99309680648581e0c96579c5fc11402ff2507261d62a1e4e04ebb3cd7ae83827.jpg)  
b) 水平偏振

![](images/da026af0940398ddf79104abd4b1c004cd5f7f48fa1e29f53d4e3c1cab520b45.jpg)  
图9.8

习题 9.8 式 (9.36) 描述了在弦上的最一般的线性（linearly）偏振波。线性（或“平面”）偏振（这样称是因为弦的位移平行于一个固定矢量 $\hat{n}$ ）源于同相位的水平方向和垂直方向偏振波的叠加 [式 (9.39)]。如果两分量振幅相同，但相位相差 $90^{\circ}$ （如， $\delta_{v}=0,\delta_{h}=90^{\circ}$ ），则形成一个圆偏振波。在这种情况下：

(a) 在一固定点 $z$ ，证明弦绕 $z$ 轴做一圆周运动。沿 $z$ 轴负方向看，圆周运动是顺时针还是逆时针？怎样构造一个做其他圆周运动的波？[在光学中，顺时针运动称为右旋圆偏振（right circular polarization），逆时针为左旋圆偏振（left circular polarization）] $^{4}$ 。

(b) 画出 $t = 0$ 时弦的形状。

(c) 要产生一个圆偏振波，如何拨动弦？

## 9.2 真空中的电磁波

## 9.2.1 $E$ 与 $B$ 的波动方程

在没有电荷和电流的空间，麦克斯韦方程为

$$
\left. \begin{array}{l l} {\mathrm{(i)} \nabla \cdot \boldsymbol {E} = 0} & {\mathrm{(iii)} \nabla \times \boldsymbol {E} = - \frac {\partial \boldsymbol {B}}{\partial t}} \\ {\mathrm{(ii)} \nabla \cdot \boldsymbol {B} = 0} & {\mathrm{(iv)} \nabla \times \boldsymbol {B} = \varepsilon_ {0} \mu_ {0} \frac {\partial \boldsymbol {E}}{\partial t}} \end{array} \right\}\tag{9.40}
$$

它们组成了 E 和 B 的耦合的一阶偏微分方程组。利用对式（iii）和式（iv）求旋度可将 E 和 B 解耦：

$$
\begin{array}{r l} & {\nabla \times (\nabla \times \pmb {E}) = \nabla (\nabla \cdot \pmb {E}) - \nabla^ {2} \pmb {E} = \nabla \times \left(- \frac {\partial \pmb {B}}{\partial t}\right)} \\ & {\qquad = - \frac {\partial}{\partial t} (\nabla \times \pmb {B}) = - \mu_ {0} \varepsilon_ {0} \frac {\partial^ {2} \pmb {E}}{\partial t ^ {2}}} \\ & {\nabla \times (\nabla \times \pmb {B}) = \nabla (\nabla \cdot \pmb {B}) - \nabla^ {2} \pmb {B} = \nabla \times \left(\mu_ {0} \varepsilon_ {0} \frac {\partial \pmb {E}}{\partial t}\right)} \\ & {\qquad = \mu_ {0} \varepsilon_ {0} \frac {\partial}{\partial t} (\nabla \times \pmb {E}) = - \mu_ {0} \varepsilon_ {0} \frac {\partial^ {2} \pmb {B}}{\partial t ^ {2}}} \end{array}
$$

或者，因为 $\nabla \cdot \pmb{E} = 0$ 和 $\nabla \cdot \pmb{B} = 0$ ，有

$$
\boxed {\nabla^ {2} \pmb {E} = \mu_ {0} \varepsilon_ {0} \frac {\partial^ {2} \pmb {E}}{\partial t ^ {2}}, \quad \nabla^ {2} \pmb {B} = \mu_ {0} \varepsilon_ {0} \frac {\partial^ {2} \pmb {B}}{\partial t ^ {2}}}\tag{9.41}
$$

这样，E 和 B 的方程彼此分开了，但它们是二阶方程，这是把它们变成独立方程的代价。在真空中，E 和 B 的每个直角坐标分量满足三维波动方程（three dimensional wave equation），

$$
\nabla^ {2} f = \frac {1}{v ^ {2}} \frac {\partial^ {2} f}{\partial t ^ {2}}.
$$

[除了 $\partial^2 f / \partial z^2$ 被更普遍的形式 $\nabla^2 f$ 替代外，这个方程与式(9.2)相同]。故麦克斯韦方程意味着真空中可以传播电磁波，传播速度为

$$
v = \frac {1}{\sqrt {\varepsilon_ {0} \mu_ {0}}} = 3. 0 0 \times 1 0 ^ {8} \mathrm{m/s}\tag{9.42}
$$

这与光的速度 c 完全一样。其含义让人十分吃惊：也许光正是电磁波 $^{5}$ 。当然这个结论在今天看来并不稀奇，但在麦克斯韦时代这个结论多么具有革命性！回顾 $\varepsilon_{0}$ 和 $\mu_{0}$ 最初是如何引入理论中的：它们是库仑定律和毕奥-萨伐尔定律中的常数。我们在实验中测量它们，而实验中用到充电的木髓球、电池和导线——都是无论如何都和光没有关系的实验。但是，根据麦克斯韦的理论你可以用这两个常数计算光速 $c$ 。注意麦克斯韦对安培定律的关键贡献 $(\mu_0\varepsilon_0\partial E / \partial t)$ ，没有它波动方程不会出现，也就没有光的电磁理论。

## 9.2.2 单色平面波

因为在第 9.1.2 小节中提及的原因，我们把讨论重点放在频率为 $\omega$ 的正弦波。因在可见光范围内不同频率对应不同颜色，这些波称为单色波（monochromatic wave，表 9.1）。进一步，假设波在 z 方向传播，不依赖于 x 或 y，它们称为平面波（plane wave） $^{6}$ ，因为场在垂直于传播方向的每一个平面上都是均匀的（图 9.9）。于是，我们对下述形式的场感兴趣：

$$
\tilde {\pmb {E}} (z, t) = \tilde {\pmb {E}} _ {0} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)}, \quad \tilde {\pmb {B}} (z, t) = \tilde {\pmb {B}} _ {0} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)}\tag{9.43}
$$

式中， $\tilde{E}_0$ 和 $\tilde{B}_0$ 是（复）振幅（当然，物理的场是 $\tilde{E}$ 和 $\tilde{B}$ 的实部），以及 $\omega = ck$ 。

表9.1

<table><tr><td colspan="3">电磁波谱</td></tr><tr><td>频率/Hz</td><td>类型</td><td>波长/m</td></tr><tr><td> $10^{22}$ </td><td></td><td> $10^{-13}$ </td></tr><tr><td> $10^{21}$ </td><td>γ射线</td><td> $10^{-12}$ </td></tr><tr><td> $10^{20}$ </td><td></td><td> $10^{-11}$ </td></tr><tr><td> $10^{19}$ </td><td></td><td> $10^{-10}$ </td></tr><tr><td> $10^{18}$ </td><td>X射线</td><td> $10^{-9}$ </td></tr><tr><td> $10^{17}$ </td><td></td><td> $10^{-8}$ </td></tr><tr><td> $10^{16}$ </td><td>紫外线</td><td> $10^{-7}$ </td></tr><tr><td> $10^{15}$ </td><td>可见光</td><td> $10^{-6}$ </td></tr><tr><td> $10^{14}$ </td><td>红外线</td><td> $10^{-5}$ </td></tr><tr><td> $10^{13}$ </td><td></td><td> $10^{-4}$ </td></tr><tr><td> $10^{12}$ </td><td></td><td> $10^{-3}$ </td></tr><tr><td> $10^{11}$ </td><td></td><td> $10^{-2}$ </td></tr><tr><td> $10^{10}$ </td><td>微波</td><td> $10^{-1}$ </td></tr><tr><td> $10^{9}$ </td><td></td><td>1</td></tr><tr><td> $10^{8}$ </td><td>电视,调频信号</td><td>10</td></tr><tr><td> $10^{7}$ </td><td></td><td> $10^{2}$ </td></tr><tr><td> $10^{6}$ </td><td>调幅信号</td><td> $10^{3}$ </td></tr><tr><td> $10^{5}$ </td><td></td><td> $10^{4}$ </td></tr><tr><td> $10^{4}$ </td><td>无线电波</td><td> $10^{5}$ </td></tr><tr><td> $10^{3}$ </td><td></td><td> $10^{6}$ </td></tr><tr><td colspan="3">可见光范围</td></tr><tr><td>频率/Hz</td><td>颜色</td><td>波长/m</td></tr><tr><td> $1.0\times 10^{15}$ </td><td>近紫外</td><td> $3.0\times 10^{-7}$ </td></tr><tr><td> $7.5\times 10^{14}$ </td><td>波长最短的可见蓝色</td><td> $4.0\times 10^{-7}$ </td></tr></table>

$^{6}$ 对球面波的讨论，参看 J. R. Reitz, F. J. Milford 和 R. W. Christy, Foundations of Electromagnetic Theory, 3rd ed., Sect. 17-5 (Reading, MA: Addison-Wesley, 1979)，或习题 9.33。当然，在一个足够小的区域，只要波长远小于波前的曲率半径，任何波在该小区域的波前实质上都是平面的。

(续)

<table><tr><td colspan="3">可见光范围</td></tr><tr><td>频率/Hz</td><td>颜色</td><td>波长/m</td></tr><tr><td> $6.5 \times 10^{14}$ </td><td>蓝色</td><td> $4.6 \times 10^{-7}$ </td></tr><tr><td> $5.6 \times 10^{14}$ </td><td>绿色</td><td> $5.4 \times 10^{-7}$ </td></tr><tr><td> $5.1 \times 10^{14}$ </td><td>黄色</td><td> $5.9 \times 10^{-7}$ </td></tr><tr><td> $4.9 \times 10^{14}$ </td><td>橘色</td><td> $6.1 \times 10^{-7}$ </td></tr><tr><td> $3.9 \times 10^{14}$ </td><td>波长最长的可见红色</td><td> $7.6 \times 10^{-7}$ </td></tr><tr><td> $3.0 \times 10^{14}$ </td><td>近红外</td><td> $1.0 \times 10^{-6}$ </td></tr></table>

![](images/63c832fd26a2ec43ce7c2a280fcdae6ba7b22bb1656ff0d7338e246914603c1d.jpg)  
图9.9

现在，E 和 B 的波动方程 [式 (9.41)] 是由麦克斯韦方程导出的。然而，尽管（真空中的）麦克斯韦方程的每个解必须满足波动方程，反之却并不成立。麦克斯韦方程对 $\tilde{E}_{0}$ 和 $\tilde{B}_{0}$ 施加了额外的限制，特别地，因 $\nabla \cdot E = 0$ 和 $\nabla \cdot B = 0$ ，有 $^{7}$

$$
(\tilde {E} _ {0}) _ {z} = (\tilde {B} _ {0}) _ {z} = 0\tag{9.44}
$$

这表明电磁波是横波：电场和磁场垂直于传播方向。而且法拉第定律 $\nabla \times E = -\partial B / \partial t$ ，意味着电场和磁场振幅之间存在着关系，即

$$
- k (\tilde {E} _ {0}) _ {y} = \omega (\tilde {B} _ {0}) _ {x}, \quad k (\tilde {E} _ {0}) _ {x} = \omega (\tilde {B} _ {0}) _ {y}\tag{9.45}
$$

或更紧凑的形式

$$
\tilde {\pmb {B}} _ {0} = \frac {k}{\omega} (\hat {\pmb {z}} \times \tilde {\pmb {E}} _ {0})\tag{9.46}
$$

显然， $E$ 和 $B$ 同相位且相互垂直，它们的（实）振幅有关系

$$
B _ {0} = \frac {k}{\omega} E _ {0} = \frac {1}{c} E _ {0}\tag{9.47}
$$

第四个麦克斯韦方程， $\nabla \times \boldsymbol{B} = \mu_0\varepsilon_0(\partial E / \partial t)$ ，不给出独立的条件，它只是重复推出式(9.45)。

例题9.2 如果 $\pmb{E}$ 沿 $x$ 方向， $\pmb{B}$ 就沿 $y$ 方向[式(9.46)]：

$$
\tilde {\pmb {E}} (z, t) = \tilde {E} _ {0} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)} \hat {\pmb {x}}, \quad \tilde {\pmb {B}} (z, t) = \frac {1}{c} \tilde {E} _ {0} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)} \hat {\pmb {y}}
$$

或者（取实部）

$$
\boxed {E (z, t) = E _ {0} \cos (k z - \omega t + \delta) \hat {\boldsymbol {x}}, \quad B (z, t) = \frac {1}{c} E _ {0} \cos (k z - \omega t + \delta) \hat {\boldsymbol {y}}}\tag{9.48}
$$

这是一个单色平面波的典型形式（参看图9.10）。作为整体波被称为沿 $x$ 方向偏振的（方便起见，我们用 $\pmb{E}$ 的方向来定义电磁波的偏振方向）。

![](images/6ec102145c65f1efc91e6293e230f0ca38236f290d8909767ee3a347528baf07.jpg)  
图9.10

当然，z 方向并没有任何特殊性——我们很容易把单色平面波的传播方向推广到任何方向。引进传播（或波）矢量符号 k，它指向传播方向，大小等于波数 k。标量积 $k \cdot r$ 是 kz 合适的推广（图 9.11），于是

$$
\boxed { \begin{array}{l} \tilde {\boldsymbol {E}} (\boldsymbol {r}, t) = \tilde {E} _ {0} \mathrm{e} ^ {\mathrm{i} (\boldsymbol {k} \cdot \boldsymbol {r} - \omega t)} \hat {\boldsymbol {n}} \\ \tilde {\boldsymbol {B}} (\boldsymbol {r}, t) = \frac {1}{c} \tilde {E} _ {0} \mathrm{e} ^ {\mathrm{i} (\boldsymbol {k} \cdot \boldsymbol {r} - \omega t)} (\hat {\boldsymbol {k}} \times \hat {\boldsymbol {n}}) = \frac {1}{c} \hat {\boldsymbol {k}} \times \tilde {\boldsymbol {E}} \end{array} }\tag{9.49}
$$

![](images/971acb5ee9761d16fdb76eadf79acfdf08d77e114eb6323376e831e9269bcd45.jpg)  
图9.11

式中， $\hat{n}$ 是偏振矢量。因 E 沿横向，

$$
\hat {\boldsymbol {n}} \cdot \hat {\boldsymbol {k}} = 0\tag{9.50}
$$

[B 的横向性可从式 (9.49) 自动得出]。具有传播矢量 k 和偏振矢量 $\hat{n}$ 的一个单色平面波的实际的（实）电场和磁场是

$$
\boldsymbol {E} (\boldsymbol {r}, t) = E _ {0} \cos (\boldsymbol {k} \cdot \boldsymbol {r} - \omega t + \delta) \hat {\boldsymbol {n}}\tag{9.51}
$$

$$
\pmb {B} (\pmb {r}, t) = \frac {1}{c} E _ {0} \cos (\pmb {k} \cdot \pmb {r} - \omega t + \delta) (\hat {\pmb {k}} \times \hat {\pmb {n}})\tag{9.52}
$$

习题 9.9 写出振幅为 $E_{0}$ 、频率为 $\omega$ 、初相位为零的一单色平面波的（实）电场和磁场：

(a) 沿 $x$ 负方向传播，偏振沿 $z$ 方向。

(b) 传播沿原点至点 $(1,1,1)$ 方向，偏振平行于 xy 平面。

对每种情况画出波形并给出 $\pmb{k}$ 和 $\hat{\pmb{n}}$ 在直角坐标系下的分量。

## 9.2.3 电磁波的能量与动量

根据式 $(8.5)$ ，电磁场单位体积内储存的能量为

$$
u = \frac {1}{2} \left(\varepsilon_ {0} E ^ {2} + \frac {1}{\mu_ {0}} B ^ {2}\right)\tag{9.53}
$$

在单色平面波 [式 (9.48)] 情形

$$
B ^ {2} = \frac {1}{c ^ {2}} E ^ {2} = \mu_ {0} \varepsilon_ {0} E ^ {2}\tag{9.54}
$$

故电场和磁场的贡献相等：

$$
u = \varepsilon_ {0} E ^ {2} = \varepsilon_ {0} E _ {0} ^ {2} \cos^ {2} (k z - \omega t + \delta)\tag{9.55}
$$

当波传播时，它携带着能量一起传播。通过场传播的能量密度（单位时间通过单位面积上的能量）由坡印亭矢量给出 [式 (8.10)]:

$$
\boldsymbol {S} = \frac {1}{\mu_ {0}} (\boldsymbol {E} \times \boldsymbol {B})\tag{9.56}
$$

对于在 $z$ 方向上传播的单色平面波，

$$
\boldsymbol {S} = c \varepsilon_ {0} E _ {0} ^ {2} \cos^ {2} (k z - \omega t + \delta) \hat {\boldsymbol {z}} = c u \hat {\boldsymbol {z}}\tag{9.57}
$$

注意 S 是能量密度 $(u)$ 乘以波速 $(c\hat{k})$ ——它当然如此。在 $\Delta t$ 时间内，电磁场穿过面积为 A 截面的距离为 $c\Delta t$ （图 9.12），其携带的能量为 $uAc\Delta t$ 。因此，单位时间，通过单位面积所传输的能量为 uc。

![](images/9a241ec1328dd3933a8321b3c51b82e7653f89d1a4d4fd485402db2cce29dc54.jpg)  
图9.12

电磁场不仅有能量，还有动量。事实上，我们从式(8.29)知道场的动量密度是

$$
g = \frac {1}{c ^ {2}} S\tag{9.58}
$$

对于单色平面波有

$$
\pmb {g} = \frac {1}{c} \varepsilon_ {0} E _ {0} ^ {2} \cos^ {2} (k z - \omega t + \delta) \hat {\pmb {z}} = \frac {1}{c} u \hat {\pmb {z}}\tag{9.59}
$$

对于光，波长 $(\sim 5\times 10^{-7}\mathrm{m})$ 如此小，周期 $(\sim 10^{-15}\mathrm{s})$ 如此短，以致宏观测量会包含许多个周期。所以，一般我们不关心能量和动量密度的余弦函数平方形式的波动，我们关心的是平均值。在一个完整周期内余弦函数平方的平均值是 $1 / 2$ ，故有

$$
\langle u \rangle = \frac {1}{2} \varepsilon_ {0} E _ {0} ^ {2}\tag{9.60}
$$

$$
\langle S \rangle = \frac {1}{2} c \varepsilon_ {0} E _ {0} ^ {2} \hat {z}\tag{9.61}
$$

$$
\langle \pmb {g} \rangle = \frac {1}{2 c} \varepsilon_ {0} E _ {0} ^ {2} \hat {\pmb {z}}\tag{9.62}
$$

这里用括号〈〉表示对一个周期（或许多周期，如果你喜欢）的（时间）平均。通过单位面积上传播的电磁波平均功率称为强度（intensity）：

$$
I \equiv \langle S \rangle = \frac {1}{2} c \varepsilon_ {0} E _ {0} ^ {2}\tag{9.63}
$$

当光照射在一个物体上并被完全吸收时，光把它的动量传递给物体表面。在时间 $\Delta t$ 内，传递的动量为（图9.11） $\Delta p = \langle g \rangle Ac\Delta t$ ，故辐射压（radiation pressure，单位面积上的平均力）是

$$
P = \frac {1}{A} \frac {\Delta p}{\Delta t} = \frac {1}{2} \varepsilon_ {0} E _ {0} ^ {2} = \frac {I}{c}\tag{9.64}
$$

（对于一个理想反射器，压强为上式2倍，因为在这种情况下动量改变了方向而不是被吸收。）我们可以如下定性地考虑这个压强：电场[式(9.49)]在 $x$ 方向驱动电荷，磁场随后对它施加一个沿 $z$ 方向的力 $[q(\pmb {v}\times \pmb {B})]$ 。施加在表面上所有电荷的这种力产生压强9。

（a）不计磁场力，求粒子作为时间函数的速度（假设平均速度为零）。

(b) 现在计算粒子相应的磁场力。

(c) 证明磁场力（对时间）的平均值为零。

这一简单光压模型的问题在于，速度与场相差 $90^{\circ}$ 相位。要使能量被吸收，电荷的运动必须有某种阻尼。假设我们包含一个形式为 $-\gamma mv$ 的力， $\gamma$ 为阻尼常数。

(d) 重复第（a）部分（忽略指数形式的阻尼暂态过程）。重复第（b）部分，求粒子受到的平均磁场力 $^{10}$ 。

习题9.12 在复数表示中，有一个聪明的方法计算乘积的时间平均。设 $f(\boldsymbol{r}, t) = A \cos (\boldsymbol{k} \cdot \boldsymbol{r} - \omega t + \delta_a)$ 和 $g(\boldsymbol{r}, t) = B \cos (\boldsymbol{k} \cdot \boldsymbol{r} - \omega t + \delta_b)$ 。证明 $\langle fg \rangle = (1/2)\mathrm{Re}\left(\tilde{f}\tilde{g}^*\right)$ ，式中星号表示复共轭。[注意这仅对两个波有相同的 $k$ 和 $\omega$ 时成立，但它们可有不同的振幅和相位。]例如，

$$
\langle u \rangle = {\frac {1}{4}} \mathrm{Re} \left(\varepsilon_ {0} \tilde {\pmb {E}} \cdot \tilde {\pmb {E}} ^ {*} + {\frac {1}{\mu_ {0}}} \tilde {\pmb {B}} \cdot \tilde {\pmb {B}} ^ {*}\right) \quad \text {以及} \quad \langle S \rangle = {\frac {1}{2 \mu_ {0}}} \mathrm{Re} \left(\tilde {\pmb {E}} \times \tilde {\pmb {B}} ^ {*}\right)
$$

习题9.13 求出沿 $z$ 方向传播和在 $x$ 方向线性偏振的单色平面波[式(9.48)]的麦克斯韦应力张量的所有矩阵元。结果有意义吗？（-T表示动量流密度。）在这种情况下，动量流密度和能流密度有何关系？

## 9.3 物质中的电磁波

## 9.3.1 线性介质中的传播

在物质中，在没有自由电荷和自由电流的区域内，麦克斯韦方程变为

$$
\left. \begin{array}{l l} {\mathrm{(i)} \nabla \cdot \pmb {D} = 0} & {\mathrm{(iii)} \nabla \times \pmb {E} = - \frac {\partial \pmb {B}}{\partial t}} \\ {\mathrm{(ii)} \nabla \cdot \pmb {B} = 0} & {\mathrm{(iv)} \nabla \times \pmb {H} = \frac {\partial \pmb {D}}{\partial t}} \end{array} \right\}\tag{9.65}
$$

如果介质是线性的，

$$
\pmb {D} = \varepsilon \pmb {E}, \quad \pmb {H} = \frac {1}{\mu} \pmb {B}\tag{9.66}
$$

和均匀的（即 $\varepsilon$ 和 $\mu$ 不随位置变化），麦克斯韦方程简化为

$$
\left. \begin{array}{l l} {\mathrm{(i)} \nabla \cdot \pmb {E} = 0} & {\mathrm{(iii)} \nabla \times \pmb {E} = - \frac {\partial \pmb {B}}{\partial t}} \\ {\mathrm{(ii)} \nabla \cdot \pmb {B} = 0} & {\mathrm{(iv)} \nabla \times \pmb {B} = \mu \varepsilon \frac {\partial \pmb {H}}{\partial t}} \end{array} \right\}\tag{9.67}
$$

这与真空中的形式 [式 (9.40)]（明显的）不同之处仅在于 $\mu_0\varepsilon_0$ 被 $\mu \varepsilon$ 取代 $^{11}$ 。显然，电磁波通过线性均匀介质时以速度

$$
v = \frac {1}{\sqrt {\varepsilon \mu}} = \frac {c}{n}\tag{9.68}
$$

传播。式中，

$$
n \equiv \sqrt {\frac {\varepsilon \mu}{\varepsilon_ {0} \mu_ {0}}}\tag{9.69}
$$

是物体的折射率（index of refraction）。对大多数材料， $\mu$ 非常接近于 $\mu_0$ ，故

$$
n \cong \sqrt {\varepsilon_ {\mathrm{r}}}\tag{9.70}
$$

式中， $\varepsilon_{\mathrm{r}}$ 是相对介电常数[12]式(4.34)]。因为 $\varepsilon_{\mathrm{r}}$ 总是大于1，光在物质中的转播速度更慢——这在光学中是众所周知的事实。

进行简单的变换 $\varepsilon_0\to \varepsilon$ ， $\mu_0\rightarrow \mu$ 及 $c\rightarrow v$ ，以前得到的结果继续适用。能量密度为13

$$
u = \frac {1}{2} \left(\varepsilon E ^ {2} + \frac {1}{\mu} B ^ {2}\right)\tag{9.71}
$$

而坡印亭矢量为

$$
\boldsymbol {S} = \frac {1}{\mu} (\boldsymbol {E} \times \boldsymbol {B})\tag{9.72}
$$

对于单色平面波，频率和波数有关系 $\omega = kv[$ 式(9.11)]， $B$ 的振幅是 $\pmb{E}$ 的振幅的 $1 / v[$ 式(9.46)]，而波强度是

$$
I = \frac {1}{2} \varepsilon v E _ {0} ^ {2}\tag{9.73}
$$

有趣的问题是：当一列波从一种透明的介质进入另一种透明介质时会发生什么现象——比如说，从空气进入水中，或从玻璃进入塑料中？如同在一个弦上的波一样，我们预期有反射波和透射波。确切的结果取决于我们在第7章推导出的电磁场的边界条件[式(7.64)]：

$$
\left. \begin{array}{l l} \text {(i)} \varepsilon_ {1} E _ {1} ^ {\perp} = \varepsilon_ {2} E _ {2} ^ {\perp} & \text {(iii)} \boldsymbol {E} _ {1} ^ {\parallel} = \boldsymbol {E} _ {2} ^ {\parallel} \\ \text {(ii)} B _ {1} ^ {\perp} = B _ {2} ^ {\perp} & \text {(iv)} \frac {1}{\mu_ {1}} \boldsymbol {B} _ {1} ^ {\parallel} = \frac {1}{\mu_ {2}} \boldsymbol {B} _ {2} ^ {\parallel} \end{array} \right\}\tag{9.74}
$$

这些方程把两种线性介质界面左右两边的电场和磁场联系起来。下面我们将用这些关系导出电磁波的反射和折射定理。

## 9.3.2 垂直入射时的反射与透射

假设 $xy$ 平面为两线性介质的分界面。频率为 $\omega$ ，沿 $z$ 方向传播和 $x$ 方向偏振的平面波从左边入射到分界面（图9.13）：

$$
\left. \begin{array}{l} \tilde {\pmb {E}} _ {I} (z, t) = \tilde {E} _ {0 _ {I}} \mathrm{e} ^ {\mathrm{i} (k _ {1} z - \omega t)} \hat {\pmb {x}} \\ \tilde {\pmb {B}} _ {I} (z, t) = \frac {1}{v _ {1}} \tilde {E} _ {0 _ {I}} \mathrm{e} ^ {\mathrm{i} (k _ {1} z - \omega t)} \hat {\pmb {y}} \end{array} \right\}\tag{9.75}
$$

它产生一个反射波

$$
\left. \begin{array}{l} \tilde {\boldsymbol {E}} _ {R} (z, t) = \tilde {E} _ {0 _ {R}} \mathrm{e} ^ {\mathrm{i} (- k _ {1} z - \omega t)} \hat {\boldsymbol {x}} \\ \tilde {\boldsymbol {B}} _ {R} (z, t) = - \frac {1}{v _ {1}} \tilde {E} _ {0 _ {R}} \mathrm{e} ^ {\mathrm{i} (- k _ {1} z - \omega t)} \hat {\boldsymbol {y}} \end{array} \right\}\tag{9.76}
$$

反射波向左折回介质（1）中，及一个透射波

$$
\left. \begin{array}{l} \tilde {\pmb {E}} _ {T} (z, t) = \tilde {E} _ {0 _ {T}} \mathrm{e} ^ {\mathrm{i} (k _ {2} z - \omega t)} \hat {\pmb {x}} \\ \tilde {\pmb {B}} _ {T} (z, t) = \frac {1}{v _ {2}} \tilde {E} _ {0 _ {T}} \mathrm{e} ^ {\mathrm{i} (k _ {2} z - \omega t)} \hat {\pmb {y}} \end{array} \right\}\tag{9.77}
$$

透射波继续在介质（2）中向右传播。注意 $\tilde{B}_{R}(z,t)$ 中的负号是式(9.49)的要求——或者，如果你愿意，由坡印亭矢量指向传播方向的事实。

![](images/06c52f8c12b3df66c878f8b117d935d517d8d8a52fdf0659ad82ba6ca9572247.jpg)  
图9.13

在 $z = 0$ 处，由边界条件[式(9.74)]，左边总的场强 $\tilde{E}_I + \tilde{E}_R$ 和 $\tilde{B}_I + \tilde{B}_R$ 与右边的场强 $\tilde{E}_T$ 和 $\tilde{B}_T$ 要连接。在垂直入射的情况下，在垂直于表面方向没有分量，故（i）和（ii）自然满足。但（iii）要求

$$
\tilde {E} _ {0 _ {I}} + \tilde {E} _ {0 _ {R}} = \tilde {E} _ {0 _ {T}}\tag{9.78}
$$

而由（iv）要求

$$
\frac {1}{\mu_ {1}} \left(\frac {1}{v _ {1}} \tilde {E} _ {0 _ {I}} - \frac {1}{v _ {1}} \tilde {E} _ {0 _ {R}}\right) = \frac {1}{\mu_ {2}} \left(\frac {1}{v _ {2}} \tilde {E} _ {0 _ {T}}\right)\tag{9.79}
$$

或者

$$
\tilde {E} _ {0 _ {I}} - \tilde {E} _ {0 _ {R}} = \beta \tilde {E} _ {0 _ {T}}\tag{9.80}
$$

式中，

$$
\beta \equiv \frac {\mu_ {1} v _ {1}}{\mu_ {2} v _ {2}} = \frac {\mu_ {1} n _ {2}}{\mu_ {2} n _ {1}}\tag{9.81}
$$

利用式 (9.78) 和式 (9.80)，容易解出用入射波振幅表示的出射波振幅：

$$
\tilde {E} _ {0 _ {R}} = \frac {1 - \beta}{1 + \beta} \tilde {E} _ {0 _ {I}}, \quad \tilde {E} _ {0 _ {T}} = \frac {2}{1 + \beta} \tilde {E} _ {0 _ {I}}\tag{9.82}
$$

这些结果与在弦上传播的波的结果惊人地相似。的确，如果介质的磁导率 $\mu$ 与真空中的接近（对大多数介质是这样），则 $\beta = v_{1}/v_{2}$ ，有

$$
\tilde {E} _ {0 _ {R}} = \frac {v _ {2} - v _ {1}}{v _ {2} + v _ {1}} \tilde {E} _ {0 _ {I}}, \quad \tilde {E} _ {0 _ {T}} = \frac {2 v _ {2}}{v _ {2} + v _ {1}} \tilde {E} _ {0 _ {I}}\tag{9.83}
$$

这与式(9.30)相同。在这种情况下，如同前面的情形，如果 $v_{2} > v_{1}$ ，反射波与入射波同相（上下不变）；如果 $v_{2} < v_{1}$ ，则反相（上下颠倒）。实振幅间有下面的关系：

$$
E _ {0 _ {R}} = \left| \frac {v _ {2} - v _ {1}}{v _ {2} + v _ {1}} \right| E _ {0 _ {I}}, \quad E _ {0 _ {T}} = \frac {2 v _ {2}}{v _ {2} + v _ {1}} E _ {0 _ {I}}\tag{9.84}
$$

或者利用折射率有

$$
E _ {0 _ {R}} = \left| \frac {n _ {1} - n _ {2}}{n _ {1} + n _ {2}} \right| E _ {0 _ {I}}, \quad E _ {0 _ {T}} = \frac {2 n _ {1}}{n _ {1} + n _ {2}} E _ {0 _ {I}}\tag{9.85}
$$

入射波能量中，多大百分比被反射？多大百分比被透射？由式(9.73)，强度（单位面积上的平均功率）是

$$
I = \frac {1}{2} \varepsilon v E _ {0} ^ {2}
$$

如果（再次） $\mu_{1}=\mu_{2}=\mu_{0}$ ，则反射波和入射波强度比为

$$
R \equiv \frac {I _ {R}}{I _ {I}} = \left(\frac {E _ {0 _ {R}}}{E _ {0 _ {I}}}\right) ^ {2} = \left(\frac {n _ {1} - n _ {2}}{n _ {1} + n _ {2}}\right) ^ {2}\tag{9.86}
$$

而透射波和入射波强度比为

$$
T \equiv \frac {I _ {T}}{I _ {I}} = \frac {\varepsilon_ {2} v _ {2}}{\varepsilon_ {1} v _ {1}} \left(\frac {E _ {0 _ {T}}}{E _ {0 _ {I}}}\right) ^ {2} = \frac {4 n _ {1} n _ {2}}{(n _ {1} + n _ {2}) ^ {2}}\tag{9.87}
$$

R 称为反射系数（reflection coefficient），T 称为透射系数（transmission coefficient）。它们分别量度了入射波能量被反射和透射的百分比。注意

$$
R + T = 1\tag{9.88}
$$

当然这是能量守恒的要求。例如，当光从空气 $(n_1 = 1)$ 进入玻璃 $(n_2 = 1.5)$ 时， $R = 0.04$ ， $T = 0.96$ 。这结果一点也不令人吃惊，因为大部分光都透射了。

习题9.14 不加假设 $\mu_{1} = \mu_{2} = \mu_{0}$ ，计算精确的反射和透射系数。证明 $R + T = 1$ 。

习题9.15 在写出式(9.76)和式(9.77)时，我默认了反射波和透射波的偏振方向与入射波一致——沿 $x$ 方向。证明情况的确如此。[提示：把透射波和反射波的偏振矢量写成

$$
\hat {\pmb {n}} _ {T} = \cos \theta_ {T} \hat {\pmb {x}} + \sin \theta_ {T} \hat {\pmb {y}}, \quad \hat {\pmb {n}} _ {R} = \cos \theta_ {R} \hat {\pmb {x}} + \sin \theta_ {R} \hat {\pmb {y}}
$$

根据边界条件证明 $\theta_T = \theta_R = 0$ 。]

## 9.3.3 斜入射时的反射与透射

在上一节我们讨论了垂直入射波的反射和透射，即入射光方向垂直分界面。我们现在讨论更一般的斜入射的情形，在此情形下入射波满足任意入射角度 $\theta_{I}$ 的边界条件（图 9.14）。当然，垂直入射只是斜射入射在 $\theta_{I}=0$ 时的一种特殊情况，我把它拿出来单独处理仅是作为一种热身，而对于一般斜入射，要进行的代数运算更加复杂。

![](images/f5a3c94623742b201d52c3434399d304c2383c9a5181292d542c596b200d9dc4.jpg)  
图9.14

假设一个单色平面波

$$
\tilde {\pmb {E}} _ {I} (\pmb {r}, t) = \tilde {\pmb {E}} _ {0 _ {I}} \mathrm{e} ^ {\mathrm{i} (\pmb {k} _ {I} \cdot \pmb {r} - \omega t)}, \quad \tilde {\pmb {B}} _ {I} (\pmb {r}, t) = \frac {1}{v _ {1}} (\hat {\pmb {k}} _ {I} \times \tilde {\pmb {E}} _ {I})\tag{9.89}
$$

从左边入射，产生一个反射波

$$
\tilde {\pmb {E}} _ {R} (\pmb {r}, t) = \tilde {\pmb {E}} _ {0 _ {R}} \mathrm{e} ^ {\mathrm{i} (\pmb {k} _ {R} \cdot \pmb {r} - \omega t)}, \quad \tilde {\pmb {B}} _ {R} (\pmb {r}, t) = \frac {1}{v _ {1}} (\hat {\pmb {k}} _ {R} \times \tilde {\pmb {E}} _ {R})\tag{9.90}
$$

和一个透射波

$$
\tilde {\pmb {E}} _ {T} (\pmb {r}, t) = \tilde {\pmb {E}} _ {0 _ {T}} \mathrm{e} ^ {\mathrm{i} (\pmb {k} _ {T} \cdot \pmb {r} - \omega t)}, \quad \tilde {\pmb {B}} _ {T} (\pmb {r}, t) = \frac {1}{v _ {2}} (\hat {\pmb {k}} _ {T} \times \tilde {\pmb {E}} _ {T})\tag{9.91}
$$

所有的三个波有相同的频率——它由光源确定（闪光灯或任何其他产生入射光的光源） $^{15}$ 。三个波的波数由式(9.11)所联系：

$$
k _ {I} v _ {1} = k _ {R} v _ {1} = k _ {T} v _ {2} = \omega \quad \text {或者} \quad k _ {I} = k _ {R} = {\frac {v _ {2}}{v _ {1}}} k _ {T} = {\frac {n _ {1}}{n _ {2}}} k _ {T}\tag{9.92}
$$

利用边界条件 [式 (9.74)]，在介质（1）中的合场强 $\tilde{\pmb{E}}_I + \tilde{\pmb{E}}_R$ 和 $\tilde{\pmb{B}}_I + \tilde{\pmb{B}}_R$ 必须与介质（2）中的场强 $\tilde{\pmb{E}}_T$ 和 $\tilde{\pmb{B}}_T$ 要连接。这些都具有如下一般的结构：

$$
() \mathrm{e} ^ {\mathrm{i} (\boldsymbol {k} _ {I} \cdot \boldsymbol {r} - \omega t)} + () \mathrm{e} ^ {\mathrm{i} (\boldsymbol {k} _ {R} \cdot \boldsymbol {r} - \omega t)} = () \mathrm{e} ^ {\mathrm{i} (\boldsymbol {k} _ {T} \cdot \boldsymbol {r} - \omega t)}, z = 0\tag{9.93}
$$

括号一会儿填；现在重要的是注意对 x、y 和 t 的依赖被限制在指数中。因为边界条件在入射平面上的所有点、所有时间都必须满足，所以这些指数因子必须相等（当 z=0 时）。否则，如 x 有稍微变化，将破坏等式（见习题 9.16）。当然，时间因子已经相等（事实上，可以认为这是对透射和反射的频率必须与入射的匹配的一个确认）。对于空间项，显然

$$
\pmb {k} _ {I} \cdot \pmb {r} = \pmb {k} _ {R} \cdot \pmb {r} = \pmb {k} _ {T} \cdot \pmb {r}, \quad \text {当} z = 0 \text {时}\tag{9.94}
$$

或者，更明显地，对所有的 $x$ 和 $y$ 有

$$
x \left(k _ {I}\right) _ {x} + y \left(k _ {I}\right) _ {y} = x \left(k _ {R}\right) _ {x} + y \left(k _ {R}\right) _ {y} = x \left(k _ {T}\right) _ {x} + y \left(k _ {T}\right) _ {y}\tag{9.95}
$$

但式 (9.95) 仅对各分量分别相等时成立，对 $x = 0$ ，有

$$
\left(k _ {I}\right) _ {y} = \left(k _ {R}\right) _ {y} = \left(k _ {T}\right) _ {y}\tag{9.96}
$$

对于 $y = 0$ ，有

$$
\left(k _ {I}\right) _ {x} = \left(k _ {R}\right) _ {x} = \left(k _ {T}\right) _ {x}\tag{9.97}
$$

我们可以改变坐标轴的方向使 $k_{I}$ 在 xz 平面内 [即 $(k_{I})_{y}=0$ ]。根据式 (9.96)， $k_{R}$ 和 $k_{T}$ 有同样关系。结论：

[第一定律]: 入射、反射和透射波矢量在同一平面内（称为入射面，plane of incidence），入射面的法线也在这平面内（这里是 z 轴）。

同时，式(9.97)意味着

$$
k _ {I} \sin \theta_ {I} = k _ {R} \sin \theta_ {R} = k _ {T} \sin \theta_ {T}\tag{9.98}
$$

式中， $\theta_{I}$ 是入射角（angle of incidence）； $\theta_{R}$ 是反射角（angle of reflection）； $\theta_{T}$ 是透射角，通常称为折射角（angle of refraction）。它们都是相对于法线方向的（图9.14）。考虑到式(9.92)，有

[第二定律]：入射角等于反射角，即

$$
\theta_ {I} = \theta_ {R}\tag{9.99}
$$

这是反射定律（law of reflection）。

对于折射角，

[第三定律]:

$$
\frac {\sin \theta_ {T}}{\sin \theta_ {I}} = \frac {n _ {1}}{n _ {2}}\tag{9.100}
$$

这是折射定律（law of refraction），或称为斯涅耳定律（Snell's law）。

这些是几何光学的三个基本定律。值得注意的是我们使用了不少的电动力学：我们没有调用任何特别的边界条件——用到的仅是它们的一般形式[式(9.93)]。所以，可以预期任何其他的波（例如水波或声波），当它们从一种介质进入另一种介质时，遵从同样的“光学”定律。既然式(9.94)中的指数因子被抵消——边界条件[式(9.74)]变为

$$
\left. \begin{array}{l} \text {(i)} \varepsilon_ {1} \left(\tilde {\boldsymbol {E}} _ {0 _ {I}} + \tilde {\boldsymbol {E}} _ {0 _ {R}}\right) _ {z} = \varepsilon_ {2} \left(\tilde {\boldsymbol {E}} _ {0 _ {T}}\right) _ {z} \\ \text {(ii)} \left(\tilde {\boldsymbol {B}} _ {0 _ {I}} + \tilde {\boldsymbol {B}} _ {0 _ {R}}\right) _ {z} = \left(\tilde {\boldsymbol {B}} _ {0 _ {T}}\right) _ {z} \\ \text {(iii)} \left(\tilde {\boldsymbol {E}} _ {0 _ {I}} + \tilde {\boldsymbol {E}} _ {0 _ {R}}\right) _ {x, y} = \left(\tilde {\boldsymbol {E}} _ {0 _ {T}}\right) _ {x, y} \\ \text {(iv)} \frac {1}{\mu_ {1}} \left(\tilde {\boldsymbol {B}} _ {0 _ {I}} + \tilde {\boldsymbol {B}} _ {0 _ {R}}\right) _ {x, y} = \frac {1}{\mu_ {2}} \left(\tilde {\boldsymbol {B}} _ {0 _ {T}}\right) _ {x, y} \end{array} \right\}\tag{9.101}
$$

对于每一种情况，式中 $\tilde{B}_{0}=(1/v)\hat{k}\times\tilde{E}_{0}$ 。（最后的两个是一对方程，一个为 x-分量，一个为 y-分量。）

假设入射波的电场的偏振方向平行于入射面（图9.15中的 $xz$ 平面）。这样（参看习题9.15）反射波和透射波的电场的偏振方向也在这个面内。（偏振方向垂直于入射面的情形留给读者分析，参看习题9.17。）这样（i）写为

$$
\varepsilon_ {1} \left(- \tilde {E} _ {0 _ {I}} \sin \theta_ {I} + \tilde {E} _ {0 _ {R}} \sin \theta_ {R}\right) = \varepsilon_ {2} \left(- \tilde {E} _ {0 _ {T}} \sin \theta_ {T}\right)\tag{9.102}
$$

（ii）没有增加任何东西（0=0），因为磁场没有 z 分量；（iii）变为

$$
\tilde {E} _ {0 _ {I}} \cos \theta_ {I} + \tilde {E} _ {0 _ {R}} \cos \theta_ {R} = \tilde {E} _ {0 _ {T}} \cos \theta_ {T}\tag{9.103}
$$

![](images/fc802964f1678e02ec0fb7583dee36555e6c2974549ff1f8ca30bcba6e764e20.jpg)  
图9.15

而（iv）为

$$
\frac {1}{\mu_ {1} v _ {1}} \left(\tilde {E} _ {0 _ {I}} - \tilde {E} _ {0 _ {R}}\right) = \frac {1}{\mu_ {2} v _ {2}} \tilde {E} _ {0 _ {T}}\tag{9.104}
$$

由反射定律和折射定律，式(9.102)和式(9.104)化简为

$$
\tilde {E} _ {0 _ {I}} - \tilde {E} _ {0 _ {R}} = \beta \tilde {E} _ {0 _ {T}}\tag{9.105}
$$

式中（与前面一样），

$$
\beta \equiv \frac {\mu_ {1} v _ {1}}{\mu_ {2} v _ {2}} = \frac {\mu_ {1} n _ {2}}{\mu_ {2} n _ {1}}\tag{9.106}
$$

式 (9.103) 写为

$$
\tilde {E} _ {0 _ {I}} + \tilde {E} _ {0 _ {R}} = \alpha \tilde {E} _ {0 _ {T}}\tag{9.107}
$$

式中，

$$
\alpha \equiv \frac {\cos \theta_ {T}}{\cos \theta_ {I}}\tag{9.108}
$$

求解关于反射波和透射波振幅的式(9.105)和式(9.107)，我们得到

$$
\boxed {\tilde {E} _ {0 _ {R}} = \frac {\alpha - \beta}{\alpha + \beta} \tilde {E} _ {0 _ {I}}, \quad \tilde {E} _ {0 _ {T}} = \frac {2}{\alpha + \beta} \tilde {E} _ {0 _ {I}}}\tag{9.109}
$$

它们称为偏振方向在入射面内的菲涅尔方程（Fresnel's equation）。（有另外两个菲涅尔方程，对应反射波和透射波垂直于入射平面的情形——参看习题9.17。）注意透射波与入射波相位总是一致。反射波既可同相（上下不变），如果 $\alpha >\beta$ ；也可相差 $180^{\circ}$ 反相（上下颠倒），如果 $\alpha < \beta^{16}$ 。

透射波和反射波的振幅依赖于入射角度，因为 $\alpha$ 是 $\theta_{I}$ 的函数：

$$
\alpha = \frac {\sqrt {1 - \sin^ {2} \theta_ {T}}}{\cos \theta_ {I}} = \frac {\sqrt {1 - \left[ (n _ {1} / n _ {2}) \sin \theta_ {I} \right] ^ {2}}}{\cos \theta_ {I}}\tag{9.110}
$$

对于垂直入射 $(\theta_{I} = 0)$ ， $\alpha = 1$ ，我们回到了式(9.82)。在掠射情形 $(\theta_{I} = 90^{\circ})$ ， $\alpha$ 发散，波被全部反射（在夜间湿路面上驾车的人应该有此感受）。有趣的是，有一个中间角度， $\theta_{B}$ （称为布儒斯特角），以这个角入射的反射波完全消失[17]。根据式(9.109)，当 $\alpha = \beta$ ，或

$$
\sin^ {2} \theta_ {B} = \frac {1 - \beta^ {2}}{\left(n _ {1} / n _ {2}\right) ^ {2} - \beta^ {2}}\tag{9.111}
$$

时这个现象发生。

对于 $\mu_{1} \cong \mu_{2}$ 的典型情形，有 $\beta \cong n_{2} / n_{1}$ ， $\sin^2 \theta_B \cong \beta^2 / (1 + \beta^2)$ ，从而

$$
\tan \theta_ {B} \cong \frac {n _ {2}}{n _ {1}}\tag{9.112}
$$

图 9.16 给出了光从空气 $(n_{1}=1)$ 射入玻璃 $(n_{2}=1.5)$ 时，其反射光和透射光的振幅随入射角度 $\theta_{I}$ 变化的函数关系图。（在图中，负数表示相对入射波有 $180^{\circ}$ 的相位差——振幅本身是绝对值。）

![](images/299becc4d6cdf2d427838a16d420f36a4ecb591aaf4ed978e7826d0ec6c7993c.jpg)  
图9.16

单位入射面上的功率是 $S \cdot \hat{z}$ ，故入射强度是

$$
I _ {I} = \frac {1}{2} \varepsilon_ {1} v _ {1} E _ {0 _ {I}} ^ {2} \cos \theta_ {I}\tag{9.113}
$$

而反射和透射强度分别是

$$
I _ {R} = \frac {1}{2} \varepsilon_ {1} v _ {1} E _ {0 _ {R}} ^ {2} \cos \theta_ {R}, I _ {T} = \frac {1}{2} \varepsilon_ {2} v _ {2} E _ {0 _ {T}} ^ {2} \cos \theta_ {T}\tag{9.114}
$$

（式中的余弦函数是因为我们计算的是界面处单位面积上的平均功率，界面与波前有一角度。）偏振方向平行于入射面的反射系数和透射系数分别是

$$
R \equiv \frac {I _ {R}}{I _ {I}} = \left(\frac {E _ {0 _ {R}}}{E _ {0 _ {I}}}\right) ^ {2} = \left(\frac {\alpha - \beta}{\alpha + \beta}\right) ^ {2}\tag{9.115}
$$

$$
T \equiv \frac {I _ {T}}{I _ {I}} = \frac {\varepsilon_ {2} v _ {2}}{\varepsilon_ {1} v _ {1}} \left(\frac {E _ {0 _ {T}}}{E _ {0 _ {I}}}\right) ^ {2} \frac {\cos \theta_ {T}}{\cos \theta_ {I}} = \alpha \beta \left(\frac {2}{\alpha + \beta}\right) ^ {2}\tag{9.116}
$$

图 9.17给出了（空气/玻璃界面）反射和透射振幅随入射角度变化而变化的函数。R 是入射能量中的反射部分——自然地，以布儒斯特角入射时它趋于零。T 是透射部分——当入射角为 $\theta_{B}$ 时，它趋于 1。注意 $R + T = 1$ ，这是能量守恒的要求：单位时间内到达某一小块面积的能量要等于单位时间内离开这一小块面积的能量。

![](images/beeb5c577587da784b6435ef41dd36de4cd2d733cf6f52ff536f3ebd7d1d4455.jpg)  
图9.17

习题9.16 设 $A\mathrm{e}^{\mathrm{i}ax} + B\mathrm{e}^{\mathrm{i}bx} = C\mathrm{e}^{\mathrm{i}cx}$ ，对某些非零常数 $A, B, C, a, b, c$ ，以及对任意 $x$ 。证明 $a = b = c$ 和 $A + B = C$ 。

!习题 9.17 分析偏振方向垂直于入射面的情形（即，在图 9.15 中电场沿 y 方向）。加以边界条件 [式 (9.101)]，得到关于 $\tilde{E}_{0_{R}}$ 和 $\tilde{E}_{0_{T}}$ 的菲涅尔方程。对于 $\beta = n_{2}/n_{1} = 1.5$ 情形，画出随 $\theta_{I}$ 变化的 $\left(\tilde{E}_{0_{R}}/\tilde{E}_{0_{I}}\right)$ 和 $\left(\tilde{E}_{0_{T}}/\tilde{E}_{0_{I}}\right)$ 的函数曲线。（注意对于这个 $\beta$ ，反射波总是有 $180^{\circ}$ 的相位差。）证明对任何 $n_{1}$ 和 $n_{2}$ ，不存在布儒斯特角： $\tilde{E}_{0_{R}}$ 总不为零（除非 $n_{1} = n_{2}$ 和 $\mu_{1} = \mu_{2}$ ，两种介质在光学上没有区别）。验证所得的菲涅尔方程在垂直入射时约化为恰当的形式。计算反射系数和透射系数，检查它们之和等于 1。

习题9.18 金刚石的折射率是2.42。对于空气/金刚石分界面，画出与图9.16类似的图形。（设 $\mu_{1} = \mu_{2} = \mu_{0}$ 。）特别地，计算（a）在垂直入射时的振幅；（b）布儒斯特角；（c）“交叉”角，在这个角度时，反射和折射振幅相等。

## 9.4 吸收与色散

## 9.4.1 导体中的电磁波

在第 9.3 节我限定自由电荷密度 $\rho_{f}$ 和自由电流密度 $J_{f}$ 是零，随后的结果都是基于这个条件所得出的。这样的限定对在真空和绝缘体（如玻璃或纯水）中传播的波是非常合理的。但对导体我们并不独立地控制电荷的流动，一般说来， $J_{f}$ 肯定不为零。事实上，根据欧姆定律，（自由）电流密度正比于电场：

$$
J _ {\mathrm{f}} = \sigma E\tag{9.117}
$$

由此，对线性介质麦克斯韦方程的形式是

$$
\left. \begin{array}{l l} \text {(i)} \nabla \cdot \boldsymbol {E} = \frac {\rho_ {\mathrm{f}}}{\varepsilon} & \text {(iii)} \nabla \times \boldsymbol {E} = - \frac {\partial \boldsymbol {B}}{\partial t} \\ \text {(ii)} \nabla \cdot \boldsymbol {B} = 0 & \text {(iv)} \nabla \times \boldsymbol {B} = \mu \sigma \boldsymbol {E} + \mu \varepsilon \frac {\partial \boldsymbol {H}}{\partial t} \end{array} \right\}\tag{9.118}
$$

由自由电荷的连续方程，

$$
\nabla \cdot \boldsymbol {J} _ {\mathrm{f}} = - \frac {\partial \rho_ {\mathrm{f}}}{\partial t}\tag{9.119}
$$

并利用欧姆定律和高斯定理（i），对均匀线性介质有

$$
\frac {\partial \rho_ {\mathrm{f}}}{\partial t} = - \sigma (\nabla \cdot \boldsymbol {E}) = - \frac {\sigma}{\varepsilon} \rho_ {\mathrm{f}}
$$

由此得出

$$
\rho_ {\mathrm{f}} (t) = \mathrm{e} ^ {- (\sigma / \varepsilon) t} \rho_ {\mathrm{f}} (0)\tag{9.120}
$$

因此任何初始自由电荷 $\rho_{\mathrm{f}}(0)$ 以一个特征时间 $\tau \equiv \varepsilon / \sigma$ 耗散。这反映了一个熟悉的事实：如果把一些自由电荷放在导体上，它将流向边缘。时间常数 $\tau$ 提供了一个度量导体导电性能的方式：对于“理想”导体， $\sigma = \infty$ ，而 $\tau = 0$ ；对于“良”导体， $\tau$ 比体系中其他的相关时间小很多（在一个振动系统，意味着 $\tau \ll 1 / \omega$ ）；对于“不良”导体， $\tau$ 比体系中其他的相关时间大（ $\tau \gg 1 / \omega)^{18}$ 。现在我们对这种暂态行为不感兴趣——我们将等到任何聚集的自由电荷消失。这样此后， $\rho_{\mathrm{f}} = 0$ ，我们有

$$
\left. \begin{array}{l l} \text {(i)} \nabla \cdot \boldsymbol {E} = 0 & \text {(iii)} \nabla \times \boldsymbol {E} = - \frac {\partial \boldsymbol {B}}{\partial t} \\ \text {(ii)} \nabla \cdot \boldsymbol {B} = 0 & \text {(iv)} \nabla \times \boldsymbol {B} = \mu \sigma \boldsymbol {E} + \mu \varepsilon \frac {\partial \boldsymbol {H}}{\partial t} \end{array} \right\}\tag{9.121}
$$

这些与对应的非导电介质的方程 (9.67)差别仅在于（iv）中多了最后一项——显然，当 $\sigma = 0$ 时该项不出现。

同前一样，对（iii）和（iv）取旋度，我们得到了关于 E 和 B 在导体介质中修正的波动方程

$$
\nabla^ {2} \boldsymbol {E} = \mu \varepsilon \frac {\partial^ {2} \boldsymbol {E}}{\partial t ^ {2}} + \mu \sigma \frac {\partial \boldsymbol {E}}{\partial t}, \quad \nabla^ {2} \boldsymbol {B} = \mu \varepsilon \frac {\partial^ {2} \boldsymbol {B}}{\partial t ^ {2}} + \mu \sigma \frac {\partial \boldsymbol {B}}{\partial t}\tag{9.122}
$$

这些方程仍有平面波解，

$$
\tilde {\pmb {E}} (z, t) = \tilde {\pmb {E}} _ {0} \mathrm{e} ^ {\mathrm{i} (\tilde {k} z - \omega t)}, \quad \tilde {\pmb {B}} (z, t) = \tilde {\pmb {B}} _ {0} \mathrm{e} ^ {\mathrm{i} (\tilde {k} z - \omega t)}\tag{9.123}
$$

但现在“波数” $\tilde{k}$ 是复数：

$$
\tilde {k} ^ {2} = \mu \varepsilon \omega^ {2} + \mathrm{i} \mu \sigma \omega\tag{9.124}
$$

通过把式 (9.123) 代入式 (9.122)，这很容易证明。取平方根，

$$
\tilde {k} = k + \mathrm{i} \kappa\tag{9.125}
$$

式中，

$$
k \equiv \omega \sqrt {\frac {\varepsilon \mu}{2}} \left[ \sqrt {1 + \left(\frac {\sigma}{\varepsilon \omega}\right) ^ {2}} + 1 \right] ^ {1 / 2}, \quad \kappa \equiv \omega \sqrt {\frac {\varepsilon \mu}{2}} \left[ \sqrt {1 + \left(\frac {\sigma}{\varepsilon \omega}\right) ^ {2}} - 1 \right] ^ {1 / 2}\tag{9.126}
$$

$\tilde{k}$ 的虚部导致波是衰减的（随着 z 的增大振幅减小）：

$$
\tilde {\pmb {E}} (z, t) = \tilde {\pmb {E}} _ {0} \mathrm{e} ^ {- \kappa z} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)}, \quad \tilde {\pmb {B}} (z, t) = \tilde {\pmb {B}} _ {0} \mathrm{e} ^ {- \kappa z} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)}\tag{9.127}
$$

波幅减小到 $1 / \mathrm{e}$ 时（约1/3）对应的距离称为趋肤深度（skin depth）：

$$
d \equiv \frac {1}{\kappa}\tag{9.128}
$$

它度量了波进入导体内的深度。而 $\tilde{k}$ 的实部以通常的方式确定了波长、波速及折射率：

$$
\lambda = \frac {2 \pi}{k}, \quad v = \frac {\omega}{k}, \quad n = \frac {c k}{\omega}\tag{9.129}
$$

对任何 $\tilde{E}_{0}$ 和 $\tilde{B}_{0}$ ，衰减的平面波 [式 (9.127)] 满足修正的波动方程 (9.122)。但麦克斯韦方程 (9.121) 附加了进一步的限制用来确定 E 和 B 的对相振幅、相位及偏振。与以前相同，（i）和（ii）排除了 z 分量：波场是横向的。我们可以调整坐标轴使 E 的偏振方向沿 x 方向：

$$
\tilde {\pmb {E}} (z, t) = \tilde {E} _ {0} \mathrm{e} ^ {- \kappa z} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)} \hat {\pmb {x}}\tag{9.130}
$$

这样（iii）给出

$$
\tilde {B} (z, t) = \frac {\tilde {k}}{\omega} \tilde {E} _ {0} \mathrm{e} ^ {- \kappa z} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)} \hat {\pmb y}\tag{9.131}
$$

（iv 给出同样结果。）这再次证明，电场与磁场是互相垂直的。

如同任何复数， $\tilde{k}$ 可用模和相位表示：

$$
\tilde {k} = K \mathrm{e} ^ {\mathrm{i} \phi}\tag{9.132}
$$

式中，

$$
K \equiv | \tilde {k} | = \sqrt {k ^ {2} + \kappa^ {2}} = \omega \sqrt {\varepsilon \mu \sqrt {1 + \left(\frac {\sigma}{\varepsilon \omega}\right) ^ {2}}}\tag{9.133}
$$

以及

$$
\phi \equiv \arctan (\kappa / k)\tag{9.134}
$$

由式(9.130)和式(9.131)，复振幅 $\tilde{E}_0 = E_0\mathrm{e}^{\mathrm{i}\delta_E}$ 和 $\tilde{B}_0 = B_0\mathrm{e}^{\mathrm{i}\delta_B}$ 通过下式相联系：

$$
B _ {0} \mathrm{e} ^ {\mathrm{i} \delta_ {B}} = \frac {K \mathrm{e} ^ {\mathrm{i} \phi}}{\omega} E _ {0} \mathrm{e} ^ {\mathrm{i} \delta_ {E}}\tag{9.135}
$$

显然，电场与磁场不再同相；事实上，

$$
\delta_ {B} - \delta_ {E} = \phi\tag{9.136}
$$

磁场滞后于电场。同时，E 和 B 的（实）振幅通过下式相联系：

$$
\frac {B _ {0}}{E _ {0}} = \frac {K}{\omega} = \sqrt {\varepsilon \mu \sqrt {1 + \left(\frac {\sigma}{\varepsilon \omega}\right) ^ {2}}}\tag{9.137}
$$

最后，（实）电场和磁场分别为

$$
\left. \begin{array}{l} \pmb {E} (z, t) = E _ {0} \mathrm{e} ^ {- \kappa z} \cos \left(k z - \omega t + \delta_ {E}\right) \hat {\pmb {x}} \\ \pmb {B} (z, t) = B _ {0} \mathrm{e} ^ {- \kappa z} \cos \left(k z - \omega t + \delta_ {E} + \phi\right) \hat {\pmb {y}} \end{array} \right\}\tag{9.138}
$$

这些场如图 9.18 所示。

![](images/376d530d8f5fab78fb714fb926e2e17b16f6a6b76d60c003837a2fa6d04ae308.jpg)  
图9.18

习题9.19

(a) 假如你在一小片玻璃中嵌入一些自由电荷，这些电荷需要多长时间流到表面？

(b) 银是很好的导体，但它昂贵。假设你正设计一个工作频率在 $10^{10}\mathrm{Hz}$ 的微波实验，需要多厚的银覆盖层？

（c）求频率为 1MHz 的无线电波在铜中的波长和传播速度，并与空气（或真空）中的情况比较。

## 习题9.20

(a) 证明在不良导体 $(\sigma \ll \omega \varepsilon)$ 中趋肤深度是 $(2 / \sigma)\sqrt{\varepsilon / \mu}$ （与频率无关）。求（纯）水的趋肤深度（以米为单位）。（采用 $\varepsilon$ 、 $\mu$ 和 $\sigma$ 的静场值，则你的结果只在频率相对较低时正确。）

(b) 证明在良导体 $(\sigma \gg \omega \varepsilon)$ 中趋肤深度是 $\lambda / 2\pi$ （式中 $\lambda$ 是在导体中的波长）。求在可见光范围 $(\omega \approx 10^{15} / \mathrm{s})$ ，典型金属 $[\sigma \approx 10^7 (\Omega \cdot \mathrm{m})^{-1}]$ 的趋肤深度（单位用 nm）。设 $\varepsilon \approx \varepsilon_0$ ， $\mu \approx \mu_0$ 。为何金属是不透明的？

(c) 证明在良导体中磁场滞后电场 $45^{\circ}$ 。求出它们的振幅比。作为数值计算的例子，利用在（b）中给出的典型金属的参数进行计算。

习题9.21

(a) 计算平面电磁波在金属介质 [式 (9.138)] 中的（时间平均）能量密度。证明磁场的贡献总是占主导。[答案： $\left(k^{2}/2\mu\omega^{2}\right)E_{0}^{2}e^{-2\kappa z}$ ]

(b) 证明强度是 $(k / 2\mu \omega)E_0^2\mathrm{e}^{-2\kappa z}$ 。

## 9.4.2 导体表面的反射

我们用来分析在两电介质界面处的反射和折射的边界条件在有自由电荷和电流存在的情况下不再成立。取而代之，有更一般的关系 [式 (7.64)]：

$$
\left. \begin{array}{l l} {\mathrm{(i)} \varepsilon_ {1} E _ {1} ^ {\perp} - \varepsilon_ {2} E _ {2} ^ {\perp} = \sigma_ {\mathrm{f}}} & {\mathrm{(iii)} \boldsymbol {E} _ {1} ^ {\parallel} - \boldsymbol {E} _ {2} ^ {\parallel} = \boldsymbol {0}} \\ {\mathrm{(ii)} B _ {1} ^ {\perp} - B _ {2} ^ {\perp} = 0} & {\mathrm{(iv)} \frac {1}{\mu_ {1}} \boldsymbol {B} _ {1} ^ {\parallel} - \frac {1}{\mu_ {2}} \boldsymbol {B} _ {2} ^ {\parallel} = \boldsymbol {K} _ {\mathrm{f}} \times \hat {\boldsymbol {n}}} \end{array} \right\}\tag{9.139}
$$

式中， $\sigma_{\mathrm{f}}$ （不要与电导率混淆）是自由表面电荷； $K_{\mathrm{f}}$ 是自由表面电流； $\hat{n}$ （不要与波的偏振方向混淆）是垂直于表面的单位矢量，它从介质（2）指向介质（1）。对于欧姆导体 $(J_{\mathrm{f}} = \sigma E)$ ，可以没有自由表面电流，因为这会要求在边界处有无限大的电场。

假设 $xy$ 平面构成非导电线性介质（1）和导体（2）的界面。一个单色平面波，其偏振方向指向 $x$ 方向，从左边沿着 $z$ 轴接近界面，如图9.13所示：

$$
\tilde {\pmb {E}} _ {I} (z, t) = \tilde {E} _ {0 _ {I}} \mathrm{e} ^ {\mathrm{i} (k _ {1} z - \omega t)} \hat {\pmb {x}}, \quad \tilde {\pmb {B}} _ {I} (z, t) = \frac {1}{v _ {1}} \tilde {E} _ {0 _ {I}} \mathrm{e} ^ {\mathrm{i} (k _ {1} z - \omega t)} \hat {\pmb {y}}\tag{9.140}
$$

这个入射波产生一个反射波，

$$
\tilde {\pmb {E}} _ {R} (z, t) = \tilde {E} _ {0 _ {R}} \mathrm{e} ^ {\mathrm{i} (- k _ {1} z - \omega t)} \hat {\pmb {x}}, \quad \tilde {\pmb {B}} _ {R} (z, t) = - \frac {1}{v _ {1}} \tilde {E} _ {0 _ {R}} \mathrm{e} ^ {\mathrm{i} (- k _ {1} z - \omega t)} \hat {\pmb {y}}\tag{9.141}
$$

它在介质（1）中向左返回，而产生的一个透射波为

$$
\tilde {\pmb {E}} _ {T} (z, t) = \tilde {E} _ {0 _ {T}} \mathrm{e} ^ {\mathrm{i} (\tilde {k} _ {2} z - \omega t)} \hat {\pmb {x}}, \quad \tilde {\pmb {B}} _ {T} (z, t) = \frac {\tilde {k} _ {2}}{\omega} \tilde {E} _ {0 _ {T}} \mathrm{e} ^ {\mathrm{i} (\tilde {k} _ {2} z - \omega t)} \hat {\pmb {y}}\tag{9.142}
$$

它随进入导体的深度而衰减。

依照边界条件 [式(9.139)]，在 $z = 0$ 处，在介质（1）中叠加的波与介质（2）中的波必须相连接。因在界面两边都有 $E^{\perp} = 0$ ，由边界条件（i）得 $\sigma_{\mathrm{f}} = 0$ 。因 $B^{\perp} = 0$ ，边界条件（ii）自动满足。同时，由边界条件（iii）得

$$
\tilde {E} _ {0 _ {I}} + \tilde {E} _ {0 _ {R}} = \tilde {E} _ {0 _ {T}}\tag{9.143}
$$

由（iv）（有 $K_{\mathrm{f}} = 0$ ）得

$$
\frac {1}{\mu_ {1} v _ {1}} \left(\tilde {E} _ {0 _ {I}} - \tilde {E} _ {0 _ {R}}\right) - \frac {\tilde {k} _ {2}}{\mu_ {2} \omega} \tilde {E} _ {0 _ {T}} = 0\tag{9.144}
$$

或者

$$
\tilde {E} _ {0 _ {I}} - \tilde {E} _ {0 _ {R}} = \tilde {\beta} \tilde {E} _ {0 _ {T}}\tag{9.145}
$$

式中，

$$
\tilde {\beta} \equiv \frac {\mu_ {1} v _ {1}}{\mu_ {2} \omega} \tilde {k} _ {2}\tag{9.146}
$$

由上可得

$$
\tilde {E} _ {0 _ {R}} = \frac {1 - \tilde {\beta}}{1 + \tilde {\beta}} \tilde {E} _ {0 _ {I}}, \quad \tilde {E} _ {0 _ {T}} = \frac {2}{1 + \tilde {\beta}} \tilde {E} _ {0 _ {I}}\tag{9.147}
$$

这些结果与应用于非导体间的边界条件时所得的结果 [式(9.82)] 形式上相同，但这种形式上的相同仅是表面上的，因为现在 $\tilde{\beta}$ 是一个复数。

对于理想导体 $(\sigma = \infty)$ ， $k_{2} = \infty$ [式(9.126)]，故 $\tilde{\beta}$ 是无穷大，有

$$
\tilde {E} _ {0 _ {R}} = - \tilde {E} _ {0 _ {I}}, \quad \tilde {E} _ {0 _ {T}} = 0\tag{9.148}
$$

在这种情况下，波被全反射，有一个 $180^{\circ}$ 的相位跃变。（这就是为何良导体能作为好镜子的原因。实际中，一块玻璃后面镀上一薄层银——玻璃与反射没有任何关系，它只是用来支撑银并避免它生锈。因为在可见光频段，趋肤深度在 $100 \, \AA$ 数量级，故不需镀很厚的银层。）

习题9.22 计算光在空气-银界面的反射系数 $\left[\mu_{1} = \mu_{2} = \mu_{0},\varepsilon_{1} = \varepsilon_{0},\sigma = 6\times 10^{7}(\Omega \cdot \mathrm{m})^{-1}\right]$ ，设光的频率为 $\omega = 4\times 10^{15} / \mathrm{s}$ 。

## 9.4.3 介电常数对频率的依赖

在前几节，我们看到电磁波在物质中的传播由材料的三个性质决定，我们把它们取为常数：介电常数 $\varepsilon$ 、磁导率 $\mu$ 和电导率 $\sigma$ 。实际上，这些参数在某种程度上依赖于所考虑波的频率。的确，如果介电常数真的是常数，那么在某一透光介质中折射率 $n \approx \sqrt{\varepsilon_{r}}$ ，也将是常数。但从光学知识知道 n 是波长的函数（图 9.19 是一种典型玻璃的折射率图）。一个棱镜或水滴对蓝光的折射要比红光大，这样白光经过折射后出射光成为彩虹。这种现象称为色散（dispersion）。推广这个概念，当波速依赖于频率时，介质称为具有色散（dispersive）。

![](images/5c91153c89389437cc8853f6019b8fc970807e8f3e692b850b02fa5168325712.jpg)  
图9.19

因为不同频率的波在色散介质中以不同速度传播，一个由一定频率区间的波组成的波包在传播过程中形状将发生变化。一个尖锐的波将变得平坦，尽管波包中每个正弦波分量以通常的波（相）速度（wave velocity, phase velocity）传播，

$$
v = \frac {\omega}{k}\tag{9.149}
$$

波包作为一个整体（“包络”）以所谓的群速度（group velocity） $^{19}$

$$
v _ {\mathrm{g}} = \frac {\mathrm{d} \omega}{\mathrm{d} k}\tag{9.150}
$$

传播。[你可在池塘中丢入一块石头观察波形来揭示这个：扰动作为一个整体以一个圆向外传播，速度为 $v_{\mathrm{g}}$ ，可观察到组成波包的波纹以2倍的速度传播（在此情况下 $v = 2v_{\mathrm{g}}$ ）。它们在波包的后端产生，在向波包中部移动时增大，随后减小至波前处消失（图9.20）。]我们将不关注这些事情——我将专注于单色波，它们不存在这些问题。但这里我要强调的是在一个色散介质中一个波包携带的能量通常以群速度传播，不是相速度。因此对在某些情况下 $v_{\mathrm{g}}$ 会大于 $c^{20}$ 也不必太惊讶。

![](images/49c78f82dc8afa62d0ba9e9963fd99fe2117dbb69bb8725d99ef73405d5bcbae.jpg)  
图9.20

本节的目的是利用电子在电介质中的性质的简单模型说明在绝缘体中 $\varepsilon$ 对频率的依赖性。正如所有原子尺度现象的经典模型，它是对真实图像的很好近似，产生令人满意的定性结果，可对透明介质中的色散机理提供一个合理的解释。

绝缘体中的电子被特定的分子束缚。实际的束缚力相当复杂，但我们可设想电子连接在一个力常数为 $k_{弹簧}$ 的弹簧一端（图 9.21）：

$$
F _ {\mathrm{束缚}} = - k _ {\mathrm{弹簧}} x = - m \omega_ {0} ^ {2} x\tag{9.151}
$$

![](images/c3a38656ba5a67d011f650cfdcf159fbca0126ebd46b27f7015e4068197476d1.jpg)  
图9.21

式中，x 是偏离平衡位置的距离；m 是电子的质量； $\omega_{0}$ 是固有振荡频率 $\sqrt{k_{弹簧}/m}$ ，[如果觉得这个模型不够真实，回过头看看例题 4.1，在那个例子中我们给出了这种形式力的精确形式。事实上，在偏离平衡位置足够小的情形下，任何束缚力都可做这样的近似，正如你可在平衡位置通过泰勒级数对势展开：

$$
U (x) = U (0) + x U ^ {\prime} (0) + \frac {1}{2} x ^ {2} U ^ {\prime \prime} (0) + \dots
$$

等号右端第一项是常数，没有动力学意义[你总可以调整势能零点使 $U(0) = 0]$ ；第二项自动为零，因为 $\mathrm{d}U / \mathrm{d}x = -F$ ，由平衡的性质，在平衡点处力为零；第三项是一个力常数为 $k_{\text{弹簧}} = \left.\mathrm{d}^2 U / \mathrm{d}x^2\right|_0$ 的弹簧的势能（在稳定平衡点处，二阶导数是正值）。因为位移很小，级数的高阶项可以略去。几何上，任何函数在一个极小值附近都可用一个适当的抛物线拟合。

另外，电子也可受到某种阻尼作用：

$$
F _ {\mathrm{阻尼}} = - m \gamma \frac {\mathrm{d} x}{\mathrm{d} t}\tag{9.152}
$$

[我再次选择了最简单的可能形式，阻尼方向与速度必须相反。使它与速度成正比较易求解。我们这里不关心阻尼产生的原因——除了其他原因，一个振荡的电荷会辐射，而辐射会消耗能量。在第11章中我们将计算这种“辐射阻尼”。]

一个频率为 $\omega$ 、偏振方向沿 x 方向（图 9.21）的电磁波，施加在电子上的驱动力为

$$
F _ {\text { 驱动 }} = q E = q E _ {0} \cos (\omega t)\tag{9.153}
$$

式中， $q$ 是电子电荷； $E_0$ 是电子所在处电磁波振幅。（因只对一点感兴趣，时钟设定为在 $t = 0$ 时 $E$ 最大。为简单起见，我假设磁场力可以忽略。）把这些力代入牛顿运动方程有

$$
m \frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} = F _ {\mathrm{tot}} = F _ {\mathrm{束缚}} + F _ {\mathrm{阻尼}} + F _ {\mathrm{驱动}}
$$

或者

$$
m \frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} + m \gamma \frac {\mathrm{d} x}{\mathrm{d} t} + m \omega_ {0} ^ {2} x = q E _ {0} \cos (\omega t)\tag{9.154}
$$

即在我们的模型中，电子运动由一个阻尼谐振子方程描述，驱动力频率为 $\omega$ 。（我假设了质量很大的原子核保持静止。）

如果我们把式(9.154)作为复数方程

$$
\frac {\mathrm{d} ^ {2} \tilde {x}}{\mathrm{d} t ^ {2}} + \gamma \frac {\mathrm{d} \tilde {x}}{\mathrm{d} t} + \omega_ {0} ^ {2} \tilde {x} = \frac {q}{m} E _ {0} \mathrm{e} ^ {- \mathrm{i} \omega t}\tag{9.155}
$$

的实部，则更易处理。在稳态时，系统将以驱动频率振动：

$$
\tilde {x} (t) = \tilde {x} _ {0} \mathrm{e} ^ {- \mathrm{i} \omega t}\tag{9.156}
$$

把它代入式(9.155)，我们得到

$$
\tilde {x} _ {0} = \frac {q / m}{\omega_ {0} ^ {2} - \omega^ {2} - \mathrm{i} \gamma \omega} E _ {0}\tag{9.157}
$$

偶极矩是下式的实部：

$$
\tilde {p} (t) = q \tilde {x} (t) = \frac {q ^ {2} / m}{\omega_ {0} ^ {2} - \omega^ {2} - \mathrm{i} \gamma \omega} E _ {0} \mathrm{e} ^ {- \mathrm{i} \omega t}\tag{9.158}
$$

分母中的虚部项意味着 $p$ 与 $E$ 相位不同——滞后一个相角 $\arctan\left[\gamma\omega/\left(\omega_0^2-\omega^2\right)\right]$ 。这个相角当 $\omega \ll \omega_0$ 时很小，而当 $\omega \gg \omega_0$ 时，趋于 $\pi$ 。

一般地，在一个分子中不同位置的电子会感受到不同的固有频率和阻尼系数。假设在每一个分子中有 $f_{j}$ 个电子具有频率 $\omega_{j}$ 和阻尼 $\gamma_{j}$ 。如果单位体积内有 N 个分子，则极化强度 P 由下式实部给出 $^{21}$ ：

$$
\tilde {\boldsymbol {P}} = \frac {N q ^ {2}}{m} \left(\sum_ {j} \frac {f _ {j}}{\omega_ {j} ^ {2} - \omega^ {2} - \mathrm{i} \gamma_ {j} \omega}\right) \tilde {\boldsymbol {E}}\tag{9.159}
$$

现在，我曾定义过电极化率是 P 和 E 的比例常数（具体讲， $P = \chi \varepsilon_{0} E$ ）。在现在的情形下，P 并不正比于 E（严格讲，这不是一个线性介质），因为它们不同相。但复极化强度 $\tilde{P}$ 是正比于复场 $\tilde{E}$ 的，这提示我们可引进一个复电极化率（complex susceptibility）， $\tilde{\chi}_{e}$ :

$$
\tilde {\boldsymbol {P}} = \varepsilon_ {0} \tilde {\chi} _ {\mathrm{e}} \tilde {\boldsymbol {E}}\tag{9.160}
$$

这样可继续沿用以前的推导，不过现在，正如实际的场是 $\tilde{\pmb{E}}$ 的实部一样，实际的极化强度是 $\tilde{\pmb{P}}$ 的实部。特别有， $\tilde{\pmb{D}}$ 和 $\tilde{\pmb{E}}$ 的比例系数是复介电常数（complex permittivity） $\tilde{\varepsilon} = \varepsilon_0(1 + \tilde{\chi}_{\mathrm{e}})$ ，（在这个模型中的）复（相对）介电常数是

$$
\tilde {\varepsilon} _ {\mathrm{r}} = \frac {\tilde {\varepsilon}}{\varepsilon_ {0}} = 1 + \frac {N q ^ {2}}{m \varepsilon_ {0}} \sum_ {j} \frac {f _ {j}}{\omega_ {j} ^ {2} - \omega^ {2} - \mathrm{i} \gamma_ {j} \omega}\tag{9.161}
$$

通常情况下，虚部项可以略去，但当 $\omega$ 非常接近某个共振频率（ $\omega_{i}$ ）时，我们将会看到，虚部将起着重要的作用。

在色散介质中，一个给定频率的波动方程是

$$
\nabla^ {2} \tilde {\pmb {E}} = \tilde {\varepsilon} \mu_ {0} \frac {\partial^ {2} \tilde {\pmb {E}}}{\partial t ^ {2}}\tag{9.162}
$$

同前一样，存在平面波解

$$
\tilde {\boldsymbol {E}} (z, t) = \tilde {\boldsymbol {E}} _ {0} \mathrm{e} ^ {\mathrm{i} (\tilde {k} z - \omega t)}\tag{9.163}
$$

其中复数波数

$$
\tilde {k} \equiv \sqrt {\tilde {\varepsilon} \mu_ {0}} \omega\tag{9.164}
$$

把 $\tilde{k}$ 写成实部和虚部的形式，

$$
\tilde {k} = k + \mathrm{i} \kappa\tag{9.165}
$$

式(9.163)变为

$$
\tilde {\boldsymbol {E}} (z, t) = \tilde {\boldsymbol {E}} _ {0} \mathrm{e} ^ {- \kappa z} \mathrm{e} ^ {\mathrm{i} (k z - \omega t)}\tag{9.166}
$$

显然波是衰减的（这一点也不奇怪，因为阻尼吸收能量）。因为强度正比于 $E^{2}$ （也因此正比于 $e^{-2\kappa z}$ ），下面的量

$$
\alpha \equiv 2 \kappa\tag{9.167}
$$

称为吸收系数（absorption coefficient）。此外，波速是 $\omega / k$ ，折射率为

$$
n = \frac {c k}{\omega}\tag{9.168}
$$

这里我故意用了与第9.4.1节中类似的符号。但对现在的情况， $k$ 和 $\kappa$ 与电导无关，而是它们由阻尼谐振子的参数确定。对于气体，式(9.161)的第二项是小量，平方根[式(9.164)]可近似由二项式展开的第一项 $\sqrt{1 + \varepsilon} \cong 1 + \frac{1}{2}\varepsilon$ 得到，故有

$$
\tilde {k} = \frac {\omega}{c} \sqrt {\tilde {\varepsilon} _ {\mathrm{r}}} \cong \frac {\omega}{c} \left[ 1 + \frac {N q ^ {2}}{2 m \varepsilon_ {0}} \sum_ {j} \frac {f _ {j}}{\omega_ {j} ^ {2} - \omega^ {2} - \mathrm{i} \gamma_ {j} \omega} \right]\tag{9.169}
$$

所以有

$$
n = \frac {c k}{\omega} \cong 1 + \frac {N q ^ {2}}{2 m \varepsilon_ {0}} \sum_ {j} \frac {f _ {j} \left(\omega_ {j} ^ {2} - \omega^ {2}\right)}{\left(\omega_ {j} ^ {2} - \omega^ {2}\right) ^ {2} + \gamma_ {j} ^ {2} \omega^ {2}}\tag{9.170}
$$

以及

$$
\alpha = 2 \kappa \cong \frac {N q ^ {2} \omega^ {2}}{m \varepsilon_ {0} c} \sum_ {j} \frac {f _ {j} \gamma_ {j}}{\left(\omega_ {j} ^ {2} - \omega^ {2}\right) ^ {2} + \gamma_ {j} ^ {2} \omega^ {2}}\tag{9.171}
$$

在图 9.22 中画出了在一个共振频率附近的折射率和吸收系数。折射率在大多数时间里随着频率的增加而增加，与光学（图 9.18）实验一致。但在共振频率附近折射率下降很快。因为这个行为反常，称为反常色散（anomalous dispersion）。注意反常色散区域（在图中， $\omega_{1}<\omega<\omega_{2}$ ）与吸收最大区域一致。事实上，材料在这个区域实际可能是不透明的，原因是我们在电子“适合的”频率驱动电子，它们的振荡振幅相对较大，相应地，大量能量由于阻尼作用而被耗散掉。

![](images/47a07f3c1af33e2590a90277c11a9fe2f6ebf1582741352e96da133c7b51cdcf.jpg)  
图9.22

在图 9.22 中，n 在共振频率上小于 1，意味着波的速度超过 c。如前所述，对此不必惊讶，因为能量不是以波的速度，而是以群速度传播（参看习题 9.27）。而且，图中没有包含求和项中其他项的贡献，这些项附加一个相对恒定的“背景”量，在某些情况下使共振两边保持 n > 1。顺便说一句，在这个模型中，在共振区附近群速度也可以超过 c（见习题 9.26）。

如果远离共振频率，阻尼可以忽略，折射率公式可简化为

$$
n = 1 + \frac {N q ^ {2}}{2 m \varepsilon_ {0}} \sum_ {j} \frac {f _ {j}}{\omega_ {j} ^ {2} - \omega^ {2}}\tag{9.172}
$$

对于大多数的材料，固有频率相当无序地分布在其能谱中。但对透明材料，最邻近的、显著的共振频率一般在紫外区域，故小于 $\omega_{j}$ 。在这种情况下，

$$
\frac {1}{\omega_ {j} ^ {2} - \omega^ {2}} = \frac {1}{\omega_ {j} ^ {2}} \left(1 - \frac {\omega^ {2}}{\omega_ {j} ^ {2}}\right) ^ {- 1} \cong \frac {1}{\omega_ {j} ^ {2}} \left(1 + \frac {\omega^ {2}}{\omega_ {j} ^ {2}}\right)
$$

而式(9.172)取形式

$$
n = 1 + \left(\frac {N q ^ {2}}{2 m \varepsilon_ {0}} \sum_ {j} \frac {f _ {j}}{\omega_ {j} ^ {2}}\right) + \omega^ {2} \left(\frac {N q ^ {2}}{2 m \varepsilon_ {0}} \sum_ {j} \frac {f _ {j}}{\omega_ {j} ^ {4}}\right)\tag{9.173}
$$

或者，用真空中的波长 $(\lambda = 2\pi c / \omega)$ 表示：

$$
n = 1 + A \left(1 + \frac {B}{\lambda^ {2}}\right)\tag{9.174}
$$

这称为柯西公式（Cauchy's formula）。常数 $A$ 称为折射系数， $B$ 称为色散系数。柯西方程在可见光区域对大多数气体是适用的。

当然本节所讨论的不是非导体介质中色散的全部内容。然而，确实指出了电子的阻尼谐振如何使折射率依赖于频率，并解释了为何通常 n 随着频率 $\omega$ 增大而缓慢增大，而在特殊的 “反常” 区域它陡然下降。

(a) 浅水是非色散的，波的传播速度正比于深度的平方根。但对于深水，波不能“感知”水深——它们认为深度与波长 $\lambda$ 差不多。（实际上，“浅”和“深”本身依赖于波长：如果深度小于波长，水就是“浅的”；如果远大于波长，水就是“深的”。）证明深水中的波速是群速的2倍。

（b）在量子力学中，沿 $x$ 方向传播的、质量为 $m$ 的自由粒子由下面波函数描述：

$$
\Psi (x, t) = A \mathrm{e} ^ {\mathrm{i} (p x - E t) / \hbar}
$$

式中，p 是动量； $E = p^{2}/2m$ ，是动能。计算群速和波速。哪一个是粒子的经典速度？注意波速是群速的一半。

习题 9.24 如果在例题 4.1 中的模型里在球面上取值，你计算得到的固有频率是多少？代入实际数据，如果设原子半径为 $0.5 \, \AA$ ，在电磁波谱中它处在何处？求折射系数和色散系数，并与 $0^{\circ}C$ 、一个大气压下氢气的值比较： $A = 1.36 \times 10^{-4}$ ， $B = 7.7 \times 10^{-15} \, m^{2}$ 。

习题9.25 对于频率为 $\omega_0$ 的单共振，求反常色散区域的宽度。假设 $\gamma \ll \omega_0$ ，证明在吸收系数为最大值的一半处折射率取最大值和最小值。

习题9.26 假设只有频率为 $\omega_0$ 的单共振，从式(9.170)出发计算群速度。借助计算机，绘制 $y = v_{\mathrm{g}} / c$ 作为 $x \equiv (\omega / \omega_0)^2$ 函数的从 $x = 0$ 到 $x = 2$ 的函数图。

(a) 取 $\gamma = 0$ 。

(b) 取 $\gamma = (0.1)\omega_0$ 。

令 $\left(Nq^2\right) / \left(2m\varepsilon_0\omega_0^2\right) = 0.003$ 。注意群速度可以超过 $c$ 。

## 9.5 导波

## 9.5.1 波导

截至目前，我们处理的是无限延展的平面波；现在我们考虑限制在一个空管内的电磁波，或称为波导（wave guide）（图9.23）。假定波导是一个理想导体，即在材料内有 $E = 0$ 和 $B = 0$ ，故在其内壁的边界条件是 $^{22}$

$$
\left. \begin{array}{l} (\mathrm{i}) E ^ {\parallel} = 0 \\ (\mathrm{ii}) B ^ {\perp} = 0 \end{array} \right\}\tag{9.175}
$$

在表面感应产生的自由电荷和电流 $^{23}$ 以使上述边条件得以满足。我们对沿管轴传播的单色波感兴趣，故 E 和 B 的形式是

$$
\left. \begin{array}{l} \text {(i)} \tilde {\boldsymbol {E}} (x, y, z, t) = \tilde {\boldsymbol {E}} _ {0} (x, y) \mathrm{e} ^ {\mathrm{i} (k z - \omega t)} \\ \text {(ii)} \tilde {\boldsymbol {B}} (x, y, z, t) = \tilde {\boldsymbol {B}} _ {0} (x, y) \mathrm{e} ^ {\mathrm{i} (k z - \omega t)} \end{array} \right\}\tag{9.176}
$$

（对于感兴趣的情形，k 是实数，故略去其上面的 \~ 号。）在波导内部，电磁场必须满足麦克斯韦方程：

$$
\left. \begin{array}{l} {\mathrm{(i)} \nabla \cdot \pmb {E} = 0 \quad \mathrm{(iii)} \nabla \times \pmb {E} = - \frac {\partial \pmb {B}}{\partial t}} \\ {\mathrm{(ii)} \nabla \cdot \pmb {B} = 0 \quad \mathrm{(iv)} \nabla \times \pmb {B} = \frac {1}{c ^ {2}} \frac {\partial \pmb {E}}{\partial t}} \end{array} \right\}\tag{9.177}
$$

这样，所求问题就是在边界条件[式(9.175)]下求满足偏微分方程(9.177)的场[式(9.176)]函数 $\tilde{E}_0$ 和 $\tilde{B}_0$ 。

![](images/963b550935ddc17fa5564a5c2d2d064816ee4ccc25ce60d17bcce5986bb766a7.jpg)  
图9.23

如我们将要看到的，受限的波（一般）不是横波。为了符合边界条件我们不得不加入纵向分量 $(E_{z}$ 和 $B_{z})^{24}$ ：

$$
\tilde {\boldsymbol {E}} _ {0} = E _ {x} \hat {\boldsymbol {x}} + E _ {y} \hat {\boldsymbol {y}} + E _ {z} \hat {\boldsymbol {z}}, \quad \tilde {\boldsymbol {B}} _ {0} = B _ {x} \hat {\boldsymbol {x}} + B _ {y} \hat {\boldsymbol {y}} + B _ {z} \hat {\boldsymbol {z}}\tag{9.178}
$$

式中每个分量均是 $x$ 和 $y$ 的函数。把它代入麦克斯韦方程（iii）和（iv），得到（习题9.27a）

$$
\frac {\partial E _ {y}}{\partial x} - \frac {\partial E _ {x}}{\partial y} = \mathrm{i} \omega B _ {z}
$$

$$
\frac {\partial E _ {z}}{\partial y} - \mathrm{i} k E _ {y} = \mathrm{i} \omega B _ {x}\tag{9.179}
$$

$$
\mathrm{i} k E _ {x} - \frac {\partial E _ {z}}{\partial x} = \mathrm{i} \omega B _ {y}
$$

$$
\mathrm{i} k B _ {x} - \frac {\partial B _ {z}}{\partial x} = - \frac {\mathrm{i} \omega}{c ^ {2}} E _ {y}
$$

由方程（ii），（iii），（v）和（vi）可解出 $E_{x}, E_{y}, B_{x}$ 和 $B_{y}$

$$
\left. \begin{array}{l} (\mathrm{i}) E _ {x} = \frac {\mathrm{i}}{(\omega / c) ^ {2} - k ^ {2}} \left(k \frac {\partial E _ {z}}{\partial x} + \omega \frac {\partial B _ {z}}{\partial y}\right) \\ (\mathrm{ii}) E _ {y} = \frac {\mathrm{i}}{(\omega / c) ^ {2} - k ^ {2}} \left(k \frac {\partial E _ {z}}{\partial y} - \omega \frac {\partial B _ {z}}{\partial x}\right) \\ (\mathrm{iii}) B _ {x} = \frac {\mathrm{i}}{(\omega / c) ^ {2} - k ^ {2}} \left(k \frac {\partial B _ {z}}{\partial x} - \frac {\omega}{c ^ {2}} \frac {\partial E _ {z}}{\partial y}\right) \\ (\mathrm{iv}) B _ {y} = \frac {\mathrm{i}}{(\omega / c) ^ {2} - k ^ {2}} \left(k \frac {\partial B _ {z}}{\partial y} + \frac {\omega}{c ^ {2}} \frac {\partial E _ {z}}{\partial x}\right) \end{array} \right\}\tag{9.180}
$$

由这些方程可以确定纵向分量 $E_{z}$ 和 $B_{z}$ 。如果我们解出了这些量，通过求偏微分可求出其他量。把式(9.180)代入其余的麦克斯韦方程（习题 9.26b）得到非耦合的关于 $E_{z}$ 和 $B_{z}$ 的方程：

$$
\left. \begin{array}{l} \text {(i)} \left[ \frac {\partial^ {2}}{\partial x ^ {2}} + \frac {\partial^ {2}}{\partial y ^ {2}} + (\omega / c) ^ {2} - k ^ {2} \right] E _ {z} = 0 \\ \text {(ii)} \left[ \frac {\partial^ {2}}{\partial x ^ {2}} + \frac {\partial^ {2}}{\partial y ^ {2}} + (\omega / c) ^ {2} - k ^ {2} \right] B _ {z} = 0 \end{array} \right\}\tag{9.181}
$$

如果 $E_{z}=0$ ，称为 TE（“横向电”）波；如果 $B_{z}=0$ ，称为 TM（“横向磁”）波；如果 $E_{z}=0$ 以及 $B_{z}=0$ ，称为 TEM 波 $^{25}$ 。可证明在中空波导中 TEM 波不能发生。

证明：如果 $E_{z} = 0$ ，由高斯定理[式(9.177i)]，

$$
\frac {\partial E _ {x}}{\partial x} + \frac {\partial E _ {y}}{\partial y} = 0
$$

如果 $B_{z} = 0$ ，由法拉第定律[式(9.177iii)]，

$$
\frac {\partial E _ {y}}{\partial x} - \frac {\partial E _ {x}}{\partial y} = 0
$$

这样式(9.178)中的 $\tilde{E}_{0}$ ，其散度和旋度均为零，故它可写成一个标量势的梯度，该标量势满足拉普拉斯方程。但 E[式(9.175)] 的边界条件要求表面是一个等势面，又因拉普拉斯方程没有局域极大和极小值（由 3.1.4 节），这意味着势是个常数，故电场为零——根本不存在波。

注意这个结论仅适用于完全空的管——如果你在管中间放置一根导线，它表面与外壁的势不一定相同，因此可有非平凡的势。我们将在第9.5.3节看到这样的例子。

习题9.27

(b) 把式(9.180)代入麦克斯韦方程（i）和（ii）导出式(9.181)。检验用式(9.179)的（i）和（iv）可得出同样的结果。

假设有一个矩形波导（图 9.24），高为 a，宽为 b，我们对 TE 波的传播感兴趣。这个问题是在边界条件 [式 (9.175ii)] 下，求解式 (9.181ii)。我们通过分离变量求解。令

于是

$$
Y \frac {\mathrm{d} ^ {2} X}{\mathrm{d} x ^ {2}} + X \frac {\mathrm{d} ^ {2} Y}{\mathrm{d} y ^ {2}} + \left[ (\omega / c) ^ {2} - k ^ {2} \right] X Y = 0
$$

$$
\mathrm{(i)} \frac {1}{X} \frac {\mathrm{d} ^ {2} X}{\mathrm{d} x ^ {2}} = - k _ {x} ^ {2} \quad \mathrm{(ii)} \frac {1}{Y} \frac {\mathrm{d} ^ {2} Y}{\mathrm{d} y ^ {2}} = - k _ {y} ^ {2}\tag{9.182}
$$

其中

$$
- k _ {x} ^ {2} - k _ {y} ^ {2} + (\omega / c) ^ {2} - k ^ {2} = 0\tag{9.183}
$$

![](images/5b48f1f0a730a11e065201fec0cfb47cc3900b830a0566e5d64ae9476f64df11.jpg)  
图9.24

式 (9.182i) 的一般解是

$$
X (x) = A \sin \left(k _ {x} x\right) + B \cos \left(k _ {x} x\right)
$$

但边界条件要求在 $x = 0$ 和 $x = a$ 处， $B_x$ ——从而[式(9.180iii)] $\mathrm{d}X / \mathrm{d}x$ ——为零。所以 $A = 0$ ，且

$$
k _ {x} = m \pi / a \quad (m = 0, 1, 2, \dots)\tag{9.184}
$$

对 $Y$ 同样，有

$$
k _ {y} = n \pi / b \quad (n = 0, 1, 2, \dots)\tag{9.185}
$$

最后有

$$
B _ {z} = B _ {0} \cos (m \pi x / a) \cos (n \pi y / b)\tag{9.186}
$$

这个解称为 $TE_{mn}$ 模式。（通常第一个指数与波导的宽边相联系，故假设 $a \geqslant b$ 。另外，至少一个指数不为零——参看习题 9.28。）波数（k）由把式(9.184)和式(9.185)代入式(9.183)得到：

$$
k = \sqrt {(\omega / c) ^ {2} - \pi^ {2} [ (m / a) ^ {2} + (n / b) ^ {2} ]}\tag{9.187}
$$

如果

$$
\omega <   c \pi \sqrt {(m / a) ^ {2} + (n / b) ^ {2}} \equiv \omega_ {m n}\tag{9.188}
$$

波数将是虚数，场将指数衰减而不是行波的形式[式(9.176)]。由于这个原因 $\omega_{mn}$ 称为这个模式的截止频率（cutoff frequency）。对于模式 $\mathrm{TE}_{10}$ 一个给定波导的最低截止频率是

$$
\omega_ {1 0} = c \pi / a\tag{9.189}
$$

低于这个频率的波将不能传播。

利用截止频率波数可写成更简单的形式：

$$
k = \frac {1}{c} \sqrt {\omega^ {2} - \omega_ {m n} ^ {2}}\tag{9.190}
$$

波速是

$$
v = \frac {\omega}{k} = \frac {c}{\sqrt {1 - (\omega_ {m n} / \omega) ^ {2}}}\tag{9.191}
$$

这比 c 大。然而（参看习题 9.30），波携带的能量以群速度传播 [式(9.150)]:

$$
v _ {\mathrm{g}} = \frac {1}{\mathrm{d} k / \mathrm{d} \omega} = c \sqrt {1 - \left(\omega_ {m n} / \omega\right) ^ {2}} <   c\tag{9.192}
$$

有另一个途径观察一个电磁波在一个矩形管道中的传播，它有助于解释许多所得的结果。考虑一个普通平面波，以与 $z$ 轴成 $\theta$ 角的方向传输，在导体表面被全反射（图9.25）。在 $x$ 和 $y$ 方向（多次反射的）波互相干涉，形成驻波，波长分别为 $\lambda_{x} = 2a / m$ 和 $\lambda_{y} = 2b / n$ （故波数为 $k_{x} = 2\pi /\lambda_{x} = \pi m / a$ 和 $k_{y} = \pi n / b$ ）。同时，在 $z$ 方向上仍为行波，波数为 $k_{z} = k$ 。所以“最初”平面波的传播矢量是

$$
\boldsymbol {k} ^ {\prime} = \frac {\pi m}{a} \hat {\boldsymbol {x}} + \frac {\pi n}{b} \hat {\boldsymbol {y}} + k \hat {\boldsymbol {z}}
$$

![](images/39519838292f2f2b1ae167d731a0b479da91174b5a1ee9b2a7966395f3a091a3.jpg)  
图9.25

频率是

$$
\omega = c \left| \pmb {k} ^ {\prime} \right| = c \sqrt {k ^ {2} + \pi^ {2} \left[ (m / a) ^ {2} + (n / b) ^ {2} \right]} = \sqrt {(c k) ^ {2} + (\omega_ {m n}) ^ {2}}
$$

只有以某些角度入射才能导致允许的驻波图样产生：

$$
\cos \theta = \frac {k}{| \pmb {k} ^ {\prime} |} = \sqrt {1 - (\omega_ {m n} / \omega) ^ {2}}
$$

平面波的传播速度是 $c$ ，但因为它以 $\theta$ 角度入射，沿波导的速度是

$$
v _ {\mathrm{g}} = c \cos \theta = c \sqrt {1 - \left(\omega_ {m n} / \omega\right) ^ {2}}
$$

另一个方面，波速是沿着管子的波前的速度（如图9.25中的 $A$ 所示）。正如波浪线与海滩的交汇点，它们的移动速度比波自身的速度能够快很多——事实上

$$
v = \frac {c}{\cos \theta} = \frac {c}{\sqrt {1 - (\omega_ {m n} / \omega) ^ {2}}}
$$

习题 9.28 证明 $TE_{10}$ 模在矩形波导中不能产生。[提示：在这种情形中 $\omega/c=k$ ，所以式(9.180)不定，必须回到式(9.179)。证明 $B_{z}$ 是常量，因此——对一个截面应用法拉第定理的积分形式—— $B_{z}=0$ ，所以这会是一个 TEM 模。]

习题 9.29 考虑尺寸为 $2.28 \, cm \times 1.01 \, cm$ 的矩形波导。如果驱动频率是 $1.70 \times 10^{10} \, Hz$ ，在波导中什么 TE 模式将传播？假设你仅想激发一个 TE 模式，应选用什么频率范围？相应的波长是什么（在开放空间）？

习题 9.30 证明在 $TE_{mn}$ 模式能量以群速度传播。[提示：求时间平均的坡印亭矢量 $\langle S\rangle$ 和能量密度 $\langle u\rangle$ （如果愿意可利用习题 9.12 的结果）。对波导截面积分，求单位时间和单位长度波携带的能量，并取它们的比值。]

习题 9.31 求出矩形波导的 TM 模式理论表示。特别地，求出纵电场、截止频率、波速和群速。对于一个给定的波导，求出最低 TM 模式截止频率和最低 TE 模式截止频率之比。[注意：最低的 TM 模是什么？]

## 9.5.3 共轴传输线

在第 9.5.1 节，证明了中空的波导不能传输 TEM 模式波。但在一个半径为 a 的长导体线和一个内径为 b 的柱形导体壳所组成的长直共轴传输线中（图 9.26），的确允许 $E_{z}=0$ 和 $B_{z}=0$ 的模式存在。在此情形下由麦克斯韦方程 [式(9.179)的形式] 得

![](images/0a43b720e4851de8856e967c60c375e243c9aa82959cee08476eb6e968c7d5d8.jpg)  
图9.26

(9.193)

(故波以速度 c 传播，没有色散)，

$$
c B _ {y} = E _ {x} \quad \text {以及} \quad c B _ {x} = - E _ {y}\tag{9.194}
$$

(故 E 和 B 互相垂直)，和（加上 $\nabla \cdot E = 0, \nabla \cdot B = 0$ )：

$$
\left. \begin{array}{l} \frac {\partial E _ {x}}{\partial x} + \frac {\partial E _ {y}}{\partial y} = 0, \quad \frac {\partial E _ {y}}{\partial x} - \frac {\partial E _ {x}}{\partial y} = 0 \\ \frac {\partial B _ {x}}{\partial x} + \frac {\partial B _ {y}}{\partial y} = 0, \quad \frac {\partial B _ {y}}{\partial x} - \frac {\partial B _ {x}}{\partial y} = 0 \end{array} \right\}\tag{9.195}
$$

这些就是二维真空中的静电场和静磁场的方程。具有柱对称的解可分别直接借用无限长线电荷及无限长直线电流的结果：

$$
\pmb {E} _ {0} (s, \phi) = \frac {A}{s} \hat {\pmb {s}}, \quad \pmb {B} _ {0} (s, \phi) = \frac {A}{c s} \hat {\phi}\tag{9.196}
$$

$A$ 是某一常数。把这些代入式(9.176)，取实部：

$$
\left. \begin{array}{l} \boldsymbol {E} (s, \phi , z, t) = \frac {A \cos (k z - \omega t)}{s} \hat {\boldsymbol {s}} \\ \boldsymbol {B} (s, \phi , z, t) = \frac {A \cos (k z - \omega t)}{c s} \hat {\boldsymbol {\phi}} \end{array} \right\}\tag{9.197}
$$

习题9.32

(a) 直接证明式(9.197)满足麦克斯韦方程 [式(9.177)] 和边界条件 [式(9.175)]。

(b) 求在内部导体上的电荷密度 $\lambda(z,t)$ 和电流密度 $I(z,t)$ 。

## 第9章补充习题

!习题 9.33 傅里叶变换中的“逆定理”是

$$
\tilde {\phi} (z) = \int_ {- \infty} ^ {\infty} \tilde {\Phi} (k) \mathrm{e} ^ {\mathrm{i} k z} \mathrm{d} k \quad \Longleftrightarrow \quad \tilde {\Phi} (k) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \tilde {\phi} (z) \mathrm{e} ^ {- \mathrm{i} k z} \mathrm{d} z\tag{9.198}
$$

利用这个变换用 $f(z,0)$ 和 $\dot{f} (z,0)$ 确定式(9.20)中的 $\tilde{A} (k)$ 。

$\left[\dot{\text{答案}}: (1/2\pi) \int_{-\infty}^{\infty} \left[f(z,0) + (\mathrm{i}/\omega)\dot{f}(z,0)\right] \mathrm{e}^{-\mathrm{i}kz} \mathrm{d}z\right]$

习题9.34 [正如你在求解习题9.21时所发现的那样，第9.2.3节中对光压力的简单解释有其缺陷。这是另一个处理，最早来源于普朗克 $^{26}$ 。]沿 $z$ 方向在真空中传播的平面波遇到占据 $z \geqslant 0$ 区域的理想导体，并反射回来：

$$
\pmb {E} (z, t) = E _ {0} [ \cos (k z - \omega t) - \cos (k z + \omega t) ] \hat {\pmb {x}} \quad (z <   0)
$$

(a) 求相伴随的磁场（在 z < 0 区域）。

（b）假设导体内部 B=0，利用适当的边界条件，求 z=0 面上的电流 K。

(c) 求该面上单位面积磁场力，将其时间平均值与预期的光压 [式(9.64)] 进行比较。

习题9.35 假设

$$
\pmb {E} (r, \theta , \phi , t) = A \frac {\sin \theta}{r} [ \cos (k r - \omega t) - (1 / k r) \sin (k r - \omega t) ] \hat {\phi}, \quad \mathrm{其中} \frac {\omega}{k} = c _ {\circ}
$$

[顺便说明，这是最简单的球面波（spherical wave）。为了方便，在你的计算中令 $kr - \omega t \equiv u$ 。]

(a) 证明 $\pmb{E}$ 满足真空中的所有四个麦克斯韦方程，并求出相应的磁场。

（b）计算坡印亭矢量。对 S 求一个周期的平均，得出强度矢量 I。（它指向预期的方向吗？它以应有的 $r^{-2}$ 方式衰减吗？）

(c) 在一个球面上对 $I \cdot da$ 求积分，确定总的辐射功率。[答案： $4\pi A^{2}/3\mu_{0}c$ 。]

!习题9.36 （角）频率为 $\omega$ 的光，从介质1经过介质2薄片（厚度为 $d$ ）进入介质3（例如，从水中经过玻璃进入空气中，如图9.27所示）。证明垂直入射时透射系数由下式给出：

$$
T ^ {- 1} = \frac {1}{4 n _ {1} n _ {3}} \left[ (n _ {1} + n _ {3}) ^ {2} + \frac {(n _ {1} ^ {2} - n _ {2} ^ {2}) (n _ {3} ^ {2} - n _ {2} ^ {2})}{n _ {2} ^ {2}} \sin^ {2} \left(\frac {n _ {2} \omega d}{c}\right) \right]\tag{9.199}
$$

[提示：在左边有入射波和反射波，右边有透射波。在薄板内有向右及向左的波。用复数波幅分别表示出它们，并把波幅通过在两界面的适当的边界条件联系起来。三个介质都是线性均匀的，假设 $\mu_{1} = \mu_{2} = \mu_{3} = \mu_{0}$ 。]

习题 9.37 一个微波天线，辐射频率为 10 GHz，用介电常数为 2.5 的塑料罩与环境屏蔽。要让辐射的电磁波完全透射，则屏蔽塑料罩的最小厚度是多少（假设垂直入射）？[提示：利用式(9.199)]

习题9.38 一个养鱼缸（图9.27）的光线从水中（ $n = 4/3$ ）通过玻璃板（ $n = 3/2$ ）进入空气中 $(n = 1)$ 。假设光是单色平面波，垂直入射，求最小和最大透射系数[式(9.199)]。你能清楚地看到鱼，它看你的情形怎样？

!习题 9.39 根据斯涅耳定律，当光线从光密介质进入光疏介质 $(n_{1}>n_{2})$ 时，传输矢量 k 向远离法线方向偏折（图 9.28）。特别地，如果光线以临界角（critical angle）

$$
\theta_ {\mathrm{c}} \equiv \arcsin (n _ {2} / n _ {1})\tag{9.200}
$$

入射，则 $\theta_{T}=90^{\circ}$ ，透射光线仅掠过表面。如果 $\theta_{I}$ 超过 $\theta_{c}$ ，则折射光线完全消失，只有反射光线 [这个现象称为全内反射（total internal reflection），导光管和光纤就是据此制成的]。但在介质（2）中场并不为零，我们得到的是所谓的隐失波（evanescent wave），这种波迅速衰减，不向介质（2）中传输能量 $^{27}$ 。

![](images/01c64c56ae860605839b93ffaedf1c8cff733f2631a0c7a31b24a213c36d62da.jpg)  
图9.27

![](images/fb4c8cd6115f6010fb253d41dc59dd4c3618f1ef7ae2f9f3a60bbe0b41d0dee9.jpg)  
图9.28

一个快捷构造隐失波的方法是利用第9.3.3节的结果，这里 $k_{T} = \omega n_{2} / c$ ，以及

$$
\pmb {k} _ {T} = k _ {T} \left(\sin \theta_ {T} \hat {\pmb {x}} + \cos \theta_ {T} \hat {\pmb {z}}\right)
$$

仅有的变化是现在

$$
\sin \theta_ {T} = \frac {n _ {1}}{n _ {2}} \sin \theta_ {I}
$$

大于1，并且

$$
\cos \theta_ {T} = \sqrt {1 - \sin^ {2} \theta_ {T}} = \mathrm{i} \sqrt {\sin^ {2} \theta_ {T} - 1}
$$

是虚数。（显然， $\theta_{T}$ 不能再被解释成角度！）

(a) 证明

$$
\tilde {\pmb {E}} _ {T} (\pmb {r}, t) = \tilde {\pmb {E}} _ {0 _ {T}} \mathrm{e} ^ {- \kappa z} \mathrm{e} ^ {\mathrm{i} (k x - \omega t)}\tag{9.201}
$$

式中，

$$
\kappa \equiv {\frac {\omega}{c}} {\sqrt {\left(n _ {1} \sin \theta_ {I}\right) ^ {2} - n _ {2} ^ {2}}} \quad {\text {以及}} \quad k \equiv {\frac {\omega n _ {1}}{c}} \sin \theta_ {I}\tag{9.202}
$$

这是一个在 $x$ 方向传播的波（平行于界面！），并在 $z$ 方向衰减。

（b）注意，现在 $\alpha$ [式(9.108)]是虚数，利用式(9.109)计算偏振方向平行于入射面的波的反射系数。[注意，你得到 $100\%$ 的反射，这比在一个导体表面的反射更好（例如，参看习题9.22）。]

(c) 同样求解偏振方向垂直于入射面时的情形（利用习题 9.20 的结果）。

(d) 对于偏振方向垂直于入射面的情形，证明（实）隐失波场为

$$
\left. \begin{array}{l} \boldsymbol {E} (\boldsymbol {r}, t) = E _ {0} \mathrm{e} ^ {- \kappa z} \cos (k x - \omega t) \hat {\boldsymbol {y}} \\ \boldsymbol {B} (\boldsymbol {r}, t) = \frac {E _ {0}}{\omega} \mathrm{e} ^ {- \kappa z} [ \kappa \sin (k x - \omega t) \hat {\boldsymbol {x}} + k \cos (k x - \omega t) \hat {\boldsymbol {z}} ] \end{array} \right\}\tag{9.203}
$$

(e) 验证（d）中的场满足麦克斯韦方程 [式(9.67)]。

(f) 对（d）中的场，构造坡印亭矢量，证明在 z 方向传输的能量平均值为零。

!习题9.40 考虑一个共振腔（resonant cavity），由矩形波导把两端 $z = 0$ 和 $z = d$ 密封构成，形成了一个理想的导体空盒。证明对TE和TM模式，共振频率为

$$
\omega_ {l m n} = c \pi \sqrt {(l / d) ^ {2} + (m / a) ^ {2} + (n / b) ^ {2}}\tag{9.204}
$$

式中， $l$ 、 $m$ 和 $n$ 为整数。求出相应的电场和磁场。

## 10.1 势表述

## 10.1.1 标势与矢势

在本章中，我们寻求麦克斯韦方程

$$
\left. \begin{array}{l l} {\mathrm{(i)} \nabla \cdot \pmb {E} = \frac {\rho}{\varepsilon_ {0}}} & {\mathrm{(iii)} \nabla \times \pmb {E} = - \frac {\partial \pmb {B}}{\partial t}} \\ {\mathrm{(ii)} \nabla \cdot \pmb {B} = 0} & {\mathrm{(iv)} \nabla \times \pmb {B} = \mu_ {0} \pmb {J} + \varepsilon_ {0} \mu_ {0} \frac {\partial \pmb {E}}{\partial t}} \end{array} \right\}\tag{10.1}
$$

的一般解，即给定 $\rho (\pmb {r},t)$ 和 $J(\pmb {r},t)$ ，则 $E(\pmb {r},t)$ 和 $B(\pmb {r},t)$ 是什么？对于静态情形，库仑定律和毕奥-萨伐尔定律给出了解答。我们在这里寻求的则是这些定律向时间相关情形的推广。

这不是一个容易的问题，它从场用势表示开始值得一试。在静电学中 $\nabla \times E = 0$ ，这使我们可以把场 E 写成标量势的梯度形式： $E = -\nabla V$ 。在电动力学中，这个关系式不再成立，因为 E 的旋度不再是零。但与在静磁学中一样，B 的散度依然为零，所以我们仍然有

$$
\boxed {B = \nabla \times A}\tag{10.2}
$$

把它代入麦克斯韦方程（iii）有

$$
\nabla \times \boldsymbol {E} = - \frac {\partial}{\partial t} (\nabla \times \boldsymbol {A})
$$

或者

$$
\nabla \times \left(\boldsymbol {E} + \frac {\partial \boldsymbol {A}}{\partial t}\right) = \mathbf {0}
$$

这里括号中的量，与单独的 E 不同，其旋度正好为零；于是它可写成一个标量的梯度：

$$
\pmb {E} + \frac {\partial \pmb {A}}{\partial t} = - \nabla V
$$

则以 $V$ 和 $\pmb{A}$ 表示，有

$$
\boxed {\boldsymbol {E} = - \nabla V - \frac {\partial \boldsymbol {A}}{\partial t}}\tag{10.3}
$$

当然，当 A 取常数时这个式子回到原来的形式。

势表示 [式(10.2)和式(10.3)] 自动满足麦克斯韦方程（ii）和（iii）。（i）和（iv）又如何呢？把式(10.3)代入（i），我们得到

$$
\nabla^ {2} V + \frac {\partial}{\partial t} (\nabla \cdot \mathbf {A}) = - \frac {1}{\varepsilon_ {0}} \rho\tag{10.4}
$$

它代替泊松方程（从它可以回到静电学的形式）。把式(10.2)和式(10.3)代入（iv）得到

$$
\nabla \times (\nabla \times \boldsymbol {A}) = \mu_ {0} \boldsymbol {J} - \mu_ {0} \varepsilon_ {0} \nabla \left(\frac {\partial V}{\partial t}\right) - \mu_ {0} \varepsilon_ {0} \frac {\partial^ {2} \boldsymbol {A}}{\partial t ^ {2}}
$$

或者利用矢量关系 $\nabla \times (\nabla \times \mathbf{A}) = \nabla (\nabla \cdot \mathbf{A}) - \nabla^2\mathbf{A}$ ，重新稍做整理：

$$
\left(\nabla^ {2} \boldsymbol {A} - \mu_ {0} \varepsilon_ {0} \frac {\partial^ {2} \boldsymbol {A}}{\partial t ^ {2}}\right) - \nabla \left(\nabla \cdot \boldsymbol {A} + \mu_ {0} \varepsilon_ {0} \frac {\partial V}{\partial t}\right) = - \mu_ {0} \boldsymbol {J}\tag{10.5}
$$

式(10.4)和式(10.5)包含了麦克斯韦方程的所有信息。

例题10.1 求产生下面势的电荷和电流分布

$$
V = 0, \quad \mathbf {A} = \left\{ \begin{array}{l l} \frac {\mu_ {0} k}{4 c} (c t - | x |) ^ {2} \hat {\mathbf {z}}, & \text {当} | x | <   c t \\ \mathbf {0}, & \text {当} | x | > c t \end{array} \right.
$$

式中， $k$ 是常数；而（当然） $c = 1 / \sqrt{\varepsilon_0\mu_0}$

[解答] 首先，利用式(10.2)和式(10.3)确定电场和磁场，

$$
\boldsymbol {E} = - \frac {\partial \boldsymbol {A}}{\partial t} = - \frac {\mu_ {0} k}{2} (c t - | x |) \hat {z}
$$

$$
\pmb {B} = \nabla \times \pmb {A} = - \frac {\mu_ {0} k}{4 c} \frac {\partial}{\partial x} (c t - | x |) ^ {2} \hat {\pmb {y}} = \pm \frac {\mu_ {0} k}{2 c} (c t - | x |) \hat {\pmb {y}}
$$

$(x > 0$ 取正号， $x <   0$ 取负号)。这些是 $|x| <   ct$ 时的情形，对于 $|x| > ct$ ， $\pmb {E} = \pmb {B} = \pmb{0}$ （图10.1）。对各量求导得

$$
\nabla \cdot \boldsymbol {E} = 0, \quad \nabla \cdot \boldsymbol {B} = 0, \quad \nabla \times \boldsymbol {E} = \mp \frac {\mu_ {0} k}{2} \hat {\boldsymbol {y}}, \quad \nabla \times \boldsymbol {B} = - \frac {\mu_ {0} k}{2 c} \hat {\boldsymbol {z}}
$$

以及

$$
\frac {\partial \boldsymbol {E}}{\partial t} = - \frac {\mu_ {0} k c}{2} \hat {z}, \quad \frac {\partial \boldsymbol {B}}{\partial t} = \pm \frac {\mu_ {0} k}{2} \hat {\boldsymbol {y}}\tag{1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70}
$$

很容易验证它们满足麦克斯韦方程，且 $\rho$ 和 $J$ 都为零，但是要注意在 $x = 0$ 点， $B$ 不连续，这意味着在 $yz$ 平面有面电流 $K$ 。由边界条件 [式 (7.64iv)] 得出

$$
k t \hat {\boldsymbol {y}} = \boldsymbol {K} \times \hat {\boldsymbol {x}}
$$

所以

$$
\boldsymbol {K} = k t \hat {\boldsymbol {z}}
$$

显然有一个沿 $z$ 方向在 $x = 0$ 面上的均匀表面电流。这个电流在 $t = 0$ 时开始，并与 $t$ 成正比地增加。注意，信息以光速传播出去（向两个方向）：对于 $|x| > ct$ 的点，信息（电流正在流动）还没有到达，所以场是零。

![](images/8a37b0ca38724e8486e97ab6ee3b216a5cb8c67ef9c0507d35852a991d3b84ab.jpg)  
图10.1

习题10.1 证明 $V$ 和 $\pmb{A}$ 的微分方程[式(10.4)和式(10.5)]可以写成下面更对称的形式：

$$
\left. \begin{array}{l} \square^ {2} V + \frac {\partial L}{\partial t} = - \frac {1}{\varepsilon_ {0}} \rho \\ \square^ {2} A - \nabla L = - \mu_ {0} J \end{array} \right\}\tag{10.6}
$$

式中，

$$
\Box^ {2} \equiv \nabla^ {2} - \mu_ {0} \varepsilon_ {0} {\frac {\partial^ {2}}{\partial t ^ {2}}} \quad {\text { 以及 }} \quad L \equiv \nabla \cdot A + \mu_ {0} \varepsilon_ {0} {\frac {\partial V}{\partial t}}
$$

习题10.2 对例题10.1中的构型，考虑一边长为 $l$ 、宽为 $w$ 、高为 $h$ 的长方形盒子放在距 $yz$ 面高为 $d$ 的地方（图10.2）。

(a) 求在时间 $t_1 = d / c$ 和 $t_2 = (d + h) / c$ 时，盒子中的能量。

(b) 求出坡印亭矢量。确定在时间间隔 $t_1 < t < t_2$ 内，单位时间流入盒子的能量。

(c) 从 $t_1$ 到 $t_2$ ，对 (b) 中的结果积分，证实能量的增加 [由 (a) 得到] 等于净流入量。

![](images/7bf345ac94c30c9ed50c5d875435493a7fb284ee3fb7909e2d301d86f82e50e0.jpg)  
图10.2

## 10.1.2 规范变换

式(10.4)和式(10.5)不漂亮，你们也许倾向于放弃势形式的处理方法。然而，我们已经成功地把六个问题——求解 E 和 B（每个量有三个分量）——缩减为四个：求解 V（一个分量）和 A（三个分量）。此外，式(10.2)和式(10.3)不能唯一地定义势：只要不影响 E 和 B，我们可以自由地对 V 和 A 附加额外条件。让我们确切地弄清楚这个规范自由度（gauge freedom）牵涉什么。

假设我们有两套势 $(V,A)$ 和 $(V',A')$ ，它们对应相同的电场和磁场。它们可以有怎样的不同？设

$$
A ^ {\prime} = A + \alpha \quad \text {和} \quad V ^ {\prime} = V + \beta
$$

因为 A 与 $A'$ 要给出同样的 B，它们的旋度必须相等，故

$$
\nabla \times \alpha = 0
$$

因此我们可以把 $\alpha$ 写成某个标量的梯度：

$$
\alpha = \nabla \lambda
$$

这两个势也要给出同样的 $\pmb{E}$ ，所以

$$
\nabla \beta + \frac {\partial \pmb {\alpha}}{\partial t} = \mathbf {0}
$$

或者

$$
\nabla \left(\beta + \frac {\partial \lambda}{\partial t}\right) = \mathbf {0}
$$

括号中的项因此不依赖于坐标（然而它可以依赖于时间），称它为 $k(t)$ :

$$
\beta = - \frac {\partial \lambda}{\partial t} + k (t)
$$

事实上，我们可以把 $k(t)$ 吸收进 $\lambda$ 中，通过增加一项 $\int_0^t k(t')\mathrm{d}t'$ 定义一个新的 $\lambda$ 。这不影响 $\lambda$ 的梯度，它只把 $k(t)$ 加入 $\partial \lambda / \partial t$ 。这样有

$$
\left. \begin{array}{l} \boldsymbol {A} ^ {\prime} = \boldsymbol {A} + \nabla \lambda \\ V ^ {\prime} = V - \frac {\partial \lambda}{\partial t} \end{array} \right\}\tag{10.7}
$$

结论：对任何标量函数 $\lambda (\pmb {r},t)$ ，我们可以安然无事地把 $\nabla \lambda$ 加入 $A$ ，只要我们同时从 $V$ 中减去 $\partial \lambda /\partial t$ 。这对物理量 $E$ 和 $B$ 没有任何影响。这种对 $V$ 和 $A$ 的改变称为规范变换（gauge transformations）。它们可用来调整 $A$ 的散度，美化式(10.4)和式(10.5)。在静磁学中，取 $\nabla \cdot A = 0$ 是最合适的[式(5.63)]。在电动力学情形，情况就不是这么明了了，最方便的规范变换依赖于具体的问题。在文献中有许多著名的规范变换，下面将给出两个最流行的。

习题10.3

(a) 对下面的势，求场、电荷和电流分布

$$
V (\boldsymbol {r}, t) = 0, \quad \boldsymbol {A} (\boldsymbol {r}, t) = - \frac {1}{4 \pi \varepsilon_ {0}} \frac {q t}{r ^ {2}} \hat {\boldsymbol {r}}
$$

（b）利用规范函数 $\lambda = -(1 / 4\pi \varepsilon_0)(qt / r)$ 变换（a）中的势，并对结果加以评论。

习题10.4 设 $V = 0$ ， $\mathbf{A} = A_0\sin (kx - \omega t)\hat{\mathbf{y}}$ ，其中 $A_0,\omega$ 和 $k$ 为常数。求出 $\pmb{E}$ 和 $\pmb{B}$ ，并验证它们满足真空中的麦克斯韦方程。对 $\omega$ 和 $k$ 必须施加什么条件？

## 10.1.3 库仑规范与洛伦茨规范

库仑规范。如在静磁学中，我们取

$$
\nabla \cdot \boldsymbol {A} = 0\tag{10.8}
$$

利用这个规范，式(10.4)变为

$$
\nabla^ {2} V = - \frac {1}{\varepsilon_ {0}} \rho\tag{10.9}
$$

这就是泊松方程。我们已经知道怎样去解它：设在无穷远处 V = 0，

$$
V (\boldsymbol {r}, t) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\rho (\boldsymbol {r} ^ {\prime} , t)}{\nu} \mathrm{d} \tau^ {\prime}\tag{10.10}
$$

然而不要认为——像在静电学那样，仅由 V 就能求出 E，你还需要知道 A[式(10.3)]。

库仑规范中的标势有点令人惊奇：某时刻的势由此时刻电荷的分布立即确定。如果我在实验室移动电荷，在月亮处的势 $V$ 立刻记录下这个变化。考虑到在狭义相对论中信息的传递不可能超过光速，这听起来有点不可思议。关键是 $V$ 本身不是一个物理可观测量——在月亮上的人仅能测量 $\pmb{E}$ ，但这将涉及 $\pmb{A}$ [式(10.3)]。在库仑规范中，矢势的作用不可忽略，尽管 $V$ 可以立刻反映 $\rho$ 的变化，但组合 $-\nabla V - (\partial A / \partial t)$ 并非如此。只有经过足够长的时间，“信息”到达后， $\pmb{E}$ 才变化<sup>1</sup>。

库仑规范的优点是标势的计算非常简单，缺点是 A 的计算特别困难（除了 V 的非因果性表现之外）。在库仑规范中 A 的微分方程 [式(10.5)] 为 $^{2}$

$$
\nabla^ {2} \boldsymbol {A} - \mu_ {0} \varepsilon_ {0} \frac {\partial^ {2} \boldsymbol {A}}{\partial t ^ {2}} = - \mu_ {0} \boldsymbol {J} + \mu_ {0} \varepsilon_ {0} \nabla \left(\frac {\partial V}{\partial t}\right)\tag{10.11}
$$

洛伦茨规范。在洛伦茨 $^{3}$ 规范中，我们取

$$
\boxed {\nabla \cdot \boldsymbol {A} = - \mu_ {0} \varepsilon_ {0} \frac {\partial V}{\partial t}}\tag{10.12}
$$

这种取法是为了消除式(10.5)中的中间项（用习题10.1的话来说就是设 $L = 0$ ）。由此，

$$
\nabla^ {2} \mathbf {A} - \mu_ {0} \varepsilon_ {0} \frac {\partial^ {2} \mathbf {A}}{\partial t ^ {2}} = - \mu_ {0} \mathbf {J}\tag{10.13}
$$

同时， $V$ 的微分方程[式(10.4)]变为

$$
\nabla^ {2} V - \mu_ {0} \varepsilon_ {0} \frac {\partial^ {2} V}{\partial t ^ {2}} = - \frac {1}{\varepsilon_ {0}} \rho\tag{10.14}
$$

洛伦茨规范的优点在于它对 $V$ 和 $\pmb{A}$ 的处理是相同的：相同的微分算符

$$
\boxed {\nabla^ {2} - \mu_ {0} \varepsilon_ {0} \frac {\partial^ {2}}{\partial t ^ {2}} \equiv \Box^ {2}}\tag{10.15}
$$

（这称为达朗贝尔算符，d'Alembertian）同时出现在两个方程中：

$$
\boxed { \begin{array}{l} (\mathrm{i}) \square^ {2} V = - \frac {1}{\varepsilon_ {0}} \rho \\ (\mathrm{ii}) \square^ {2} A = - \mu_ {0} J \end{array} }\tag{10.16}
$$

这种平等处理 $V$ 和 $\mathbf{A}$ 的方法在狭义相对论中特别有好处，达朗贝尔算符是拉普拉斯算符的自然推广，式(10.16)可认为是泊松方程的四维版本。（同理对波速 $c$ 的波动方程， $\square^2 f = 0$ ，可认为是拉普拉斯方程的四维版本。）在洛伦茨规范中， $V$ 和 $\mathbf{A}$ 满足非齐次波动方程（inhomogeneous wave equation），在右端（取代零）有一个“源”项。从现在开始，我们将只用洛伦茨规范。全部的电动力学变为求解有给定源的非齐次波动方程的问题。这是我们下一节的任务。

$$
\pmb {F} = \frac {\mathrm{d} \pmb {p}}{\mathrm{d} t} = q (\pmb {E} + \pmb {v} \times \pmb {B}) = q \left[ - \nabla V - \frac {\partial \pmb {A}}{\partial t} + \pmb {v} \times (\nabla \times \pmb {A}) \right]\tag{10.17}
$$

其中 p = mv 为粒子的动量。现在按乘积法则 4

$$
\nabla (\boldsymbol {v} \cdot \boldsymbol {A}) = \boldsymbol {v} \times (\nabla \times \boldsymbol {A}) + (\boldsymbol {v} \cdot \nabla) \boldsymbol {A}
$$

（其中 $\pmb{v}$ 为粒子的速度，是时间但不是空间的函数。）于是

$$
\frac {\mathrm{d} \pmb {p}}{\mathrm{d} t} = - q \left[ \frac {\partial \pmb {A}}{\partial t} + (\pmb {v} \cdot \nabla) \pmb {A} + \nabla (V - \pmb {v} \cdot \pmb {A}) \right]\tag{10.18}
$$

式 (10.18) 中的组合

$$
\left[ \frac {\partial \boldsymbol {A}}{\partial t} + (\boldsymbol {v} \cdot \nabla) \boldsymbol {A} \right]
$$

称为 A 的运流微商（convective derivative），记为 dA/dt（全微商），它代表 A 在（移动）粒子位置的时间变化率。因为假设粒子在 t 时刻位于 r 点，该点的矢势为 $A(r,t)$ ；过一个瞬间 dt，粒子位于 $r + v dt$ 点，该点的矢势为 $A(r + v dt, t + dt)$ 。这样 A 的变化为

$$
\begin{array}{r l} \mathrm{d} \boldsymbol {A} & = \boldsymbol {A} (\boldsymbol {r} + \boldsymbol {v} \mathrm{d} t, t + \mathrm{d} t) - \boldsymbol {A} (\boldsymbol {r}, t) \\ & = \left(\frac {\partial \boldsymbol {A}}{\partial x}\right) (v _ {x} \mathrm{d} t) + \left(\frac {\partial \boldsymbol {A}}{\partial y}\right) (v _ {y} \mathrm{d} t) + \left(\frac {\partial \boldsymbol {A}}{\partial z}\right) (v _ {z} \mathrm{d} t) + \left(\frac {\partial \boldsymbol {A}}{\partial t}\right) \mathrm{d} t \end{array}
$$

于是

$$
\frac {\mathrm{d} \boldsymbol {A}}{\mathrm{d} t} = \frac {\partial \boldsymbol {A}}{\partial t} + (\boldsymbol {v} \cdot \nabla) \boldsymbol {A}\tag{10.19}
$$

当粒子移动时，它“感受到”的矢势会因两个不同的原因而变化：第一，因为矢势随时间变化；第二，因为它现在处于一个新的位置，其中 A 因其空间变化而不同。因此式(10.19)的右边有两项。

借助于运流微商，洛伦兹力定律表示为

$$
\frac {\mathrm{d}}{\mathrm{d} t} (\boldsymbol {p} + q \boldsymbol {A}) = - \nabla [ q (V - \boldsymbol {v} \cdot \boldsymbol {A}) ]\tag{10.20}
$$

这让人想起力学中对于势能 U 是位置特定函数的粒子运动的标准公式：

$$
\frac {\mathrm{d} \pmb {p}}{\mathrm{d} t} = - \nabla U
$$

扮演 $\pmb{p}$ 的角色是所谓的正则动量

$$
\pmb {p} _ {\mathrm{can}} = \pmb {p} + q \pmb {A}\tag{10.21}
$$

而 $U$ 的部分由速度相关量表示

$$
U _ {\mathrm{vel}} = q (V - \boldsymbol {v} \cdot \boldsymbol {A})\tag{10.22}
$$

类似的论证（习题10.11），粒子能量的变化率

$$
\frac {\mathrm{d}}{\mathrm{d} t} (T + q V) = \frac {\partial}{\partial t} [ q (V - \pmb {v} \cdot \pmb {A}) ]\tag{10.23}
$$

其中 $T = \frac{1}{2}mv^{2}$ 是粒子的动能，而 qV 是势能（右边的微商只对 V 和 A 作用，而不对 v 作用）。令人惊奇的是，在式(10.20)与式(10.23)的右边出现了同样的 $U_{vel}^{6}$ 。式(10.20)与式(10.23)的对应让我们将 A 解释为单位电荷的一种“势动量”，正如 V 是单位电荷的势能 $^{7}$ 。

习题10.8 均匀恒定磁场 $B$ 的矢势 $A = -\frac{1}{2} (r \times B)$ ，证明 $\mathrm{d}A / \mathrm{d}t = -\frac{1}{2} (v \times B)$ 。在这种情况下，证明式(10.20)给出正确的运动方程。习题10.9 推导式(10.23)。[提示：从用 $v$ 对式(10.17)点乘开始。]

## 10.2 连续分布

## 10.2.1 推迟势

对于静态情形，式(10.16)变为（四个相同的）泊松方程，

$$
\nabla^ {2} V = - \frac {1}{\varepsilon_ {0}} \rho , \quad \nabla^ {2} A = - \mu_ {0} J
$$

具有熟知的解

$$
V (\boldsymbol {r}) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\rho (\boldsymbol {r} ^ {\prime})}{\nu} \mathrm{d} \tau^ {\prime}, \quad \boldsymbol {A} (\boldsymbol {r}) = \frac {\mu_ {0}}{4 \pi} \int \frac {\boldsymbol {J} (\boldsymbol {r} ^ {\prime})}{\nu} \mathrm{d} \tau^ {\prime}\tag{10.24}
$$

这里像通常一样， $z$ 是源点 $r'$ 距场点 $r$ 的距离（图10.3）。现在，电磁“信号”以光速传播。所以，在非静态情况下，该信息不是源“现在”的状态，而是较早时间 $t_r$ （称为推迟时刻）当“信息”离开源时的。由于这个信息必须传播一个距离 $z$ ，推迟为 $z/c$ ：

$$
\boxed {t _ {r} \equiv t - \frac {\imath}{c}}\tag{10.25}
$$

所以，对非静态源，式(10.24)的一个自然推广为

$$
V (\boldsymbol {r}, t) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\rho \left(\boldsymbol {r} ^ {\prime} , t _ {r}\right)}{r} \mathrm{d} \tau^ {\prime}, \quad \boldsymbol {A} (\boldsymbol {r}, t) = \frac {\mu_ {0}}{4 \pi} \int \frac {\boldsymbol {J} \left(\boldsymbol {r} ^ {\prime} , t _ {r}\right)}{r} \mathrm{d} \tau^ {\prime}\tag{10.26}
$$

这里 $\rho(\boldsymbol{r}^{\prime}, t_{r})$ 是在推迟时刻 $t_{r}$ 时在点 $r^{\prime}$ 处的电荷密度。因为积分在推迟时刻进行，它们被称为推迟势（tarded potentials）。（我说了推迟时刻，当然分布较远的电荷比分布较近的电荷有较早的推迟时刻。这就像夜空中：我们看到的从每个恒星上发出的光的推迟时刻对应于恒星距地球的距离。）注意推迟势在静态情形变为式(10.24)， $\rho$ 和 J 不再依赖于时间。

![](images/397c1e841770d19b3969d51f8c028a57d2d5c592ec03660fe84fb78614a79dbb.jpg)  
图10.3

所有的听起来都很合理——而且令人惊讶的简单。但我们确信它是正确的吗？我没有推导有关 $V$ 和 $\pmb{A}$ 的公式[式(10.26)]。我做的只是利用启发式的论证（“电磁信息以光速传播”）使它们看起来可信。为了证明它们，我们必须展示它们满足非齐次波动方程[式(10.16)]和洛伦茨条件[式(10.12)]。为避免你们认为我过分挑剔，我提醒你们注意，如果对场应用同样的逻辑，将会得到完全错误的结果：

$$
\boldsymbol {E} (\boldsymbol {r}, t) \neq \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\rho (\boldsymbol {r} ^ {\prime} , t _ {r})}{r ^ {2}} \hat {\mathbf {z}} \mathrm{d} \tau^ {\prime}, \quad \boldsymbol {B} (\boldsymbol {r}, t) \neq \frac {\mu_ {0}}{4 \pi} \int \frac {\boldsymbol {J} (\boldsymbol {r} ^ {\prime} , t _ {r}) \times \hat {\mathbf {z}}}{r ^ {2}} \mathrm{d} \tau^ {\prime}
$$

让我们停下来并验证推迟标势满足式(10.16)；实际上，这也同样适合矢势 $^{8}$ 。检验推迟势满足洛伦茨条件将留给你们自己（习题10.10）。

在计算 $V(\pmb{r}, t)$ 的拉普拉斯时，特别要注意的是积分 [在式(10.26)中] 在两处依赖 $\pmb{r}$ ：显含在分母中的 $(\mathfrak{z} = |\pmb{r} - \pmb{r}'|)$ 和隐含在分子中的 $t_r \equiv t - \frac{\mathfrak{z}}{c}$ 。所以

$$
\nabla V = \frac {1}{4 \pi \varepsilon_ {0}} \int \left[ (\nabla \rho) \frac {1}{\imath} + \rho \nabla \left(\frac {1}{\imath}\right) \right] \mathrm{d} \tau^ {\prime}\tag{10.27}
$$

以及

$$
\nabla \rho = \dot {\rho} \nabla t _ {r} = - \frac {1}{c} \dot {\rho} \nabla r\tag{10.28}
$$

（式中的点表示对时间的微分） $^{9}$ 。现在有 $\nabla\lambda=\hat{\mathbf{r}}$ 和 $\nabla(1/\lambda)=-\hat{\mathbf{r}}/\lambda^{2}$ （习题 1.13），于是

$$
\nabla V = \frac {1}{4 \pi \varepsilon_ {0}} \int \left[ - \frac {\dot {\rho}}{c} \frac {\hat {\mathbf {r}}}{\mathbf {r}} - \rho \frac {\hat {\mathbf {r}}}{\mathbf {r} ^ {2}} \right] \mathrm{d} \tau^ {\prime}\tag{10.29}
$$

取散度，

$$
\begin{array}{r l} \nabla^ {2} V = & \frac {1}{4 \pi \varepsilon_ {0}} \int \left\{- \frac {1}{c} \left[ \frac {\hat {\mathbf {r}}}{r} \cdot (\nabla \dot {\rho}) + \dot {\rho} \nabla \cdot \left(\frac {\hat {\mathbf {r}}}{r}\right) \right] \right. \\ & \left. - \left[ \frac {\hat {\mathbf {r}}}{r ^ {2}} \cdot (\nabla \rho) + \rho \nabla \cdot \left(\frac {\hat {\mathbf {r}}}{r ^ {2}}\right) \right] \right\} d \tau^ {\prime} \end{array}
$$

而

$$
\nabla \dot {\rho} = - \frac {1}{c} \ddot {\rho} \nabla_ {\mathbf {r}} = - \frac {1}{c} \ddot {\rho} \hat {\mathbf {r}}
$$

这同式(10.28)中一样，并且

$$
\nabla \cdot \left(\frac {\hat {\mathbf {r}}}{r}\right) = \frac {1}{r ^ {2}}
$$

(习题 1.63)，和

$$
\nabla \cdot \left(\frac {\hat {\mathbf {r}}}{r ^ {2}}\right) = 4 \pi \delta^ {3} (\mathbf {r})
$$

[式(1.100)]。所以

$$
\nabla^ {2} V = \frac {1}{4 \pi \varepsilon_ {0}} \int \left[ \frac {1}{c ^ {2}} \frac {\ddot {\rho}}{\imath} - 4 \pi \rho \delta^ {3} (\mathbf {r}) \right] \mathrm{d} \tau^ {\prime} = \frac {1}{c ^ {2}} \frac {\partial^ {2} V}{\partial t ^ {2}} - \frac {1}{\varepsilon_ {0}} \rho (\mathbf {r}, t)
$$

这证明了推迟势 [式(10.26)] 满足非齐次波动方程 [式(10.16)]。

证毕.

顺便提及，这个证明同样适用于超前势（advanced potentials），

$$
V _ {a} (\boldsymbol {r}, t) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\rho (\boldsymbol {r} ^ {\prime} , t _ {a})}{\nu} \mathrm{d} \tau^ {\prime}, \quad \boldsymbol {A} _ {a} (\boldsymbol {r}, t) = \frac {\mu_ {0}}{4 \pi} \int \frac {\boldsymbol {J} (\boldsymbol {r} ^ {\prime} , t _ {a})}{\nu} \mathrm{d} \tau^ {\prime}\tag{10.30}
$$

其中电荷和电流密度是在超前时刻

$$
t _ {a} \equiv t + \frac {\mathrm{r}}{c}\tag{10.31}
$$

时的值。一些正负号改变了，但最后的结果不受影响。尽管超前势完全满足麦克斯韦方程，但它违背了物理学的最高原则：因果律（causality）。它们意味着现在的势依赖于将来某时的电荷和电流分布——换句话说，结果超前于原因。虽然超前势具有一定的理论兴趣，但它们没有直接的物理意义 $^{10}$ 。

例题10.2 一无限长直导线载有电流

$$
I (t) = {\left\{ \begin{array}{l l} {0,} & {{\text {对于}} t \leqslant 0} \\ {I _ {0},} & {{\text {对于}} t > 0} \end{array} \right.}
$$

也就是，一常数电流 $I_{0}$ 在 t=0 时刻突然开通。求由此产生的电场和磁场。

![](images/9de11c31816a76d35903ebf2740b7e340515e79ebcdc77587f83a1f22cb75685.jpg)  
图10.4

[解答] 设导线是电中性的，则标势为零。让导线沿着 $z$ 轴放置（图10.4）；在 $P$ 点处的推迟矢势是

$$
\boldsymbol {A} (s, t) = \frac {\mu_ {0}}{4 \pi} \hat {z} \int_ {- \infty} ^ {\infty} \frac {I (t _ {r})}{\imath} \mathrm{d} z
$$

当 $t < s / c$ 时，“信号”还没有到达 $P$ 点，矢势为零。当 $t > s / c$ 时，仅在范围

$$
| z | \leqslant \sqrt {(c t) ^ {2} - s ^ {2}}\tag{10.32}
$$

内的导线部分有贡献 [在这个范围外， $t_{r}$ 是负值，故 $I(t_{r})=0$ ]，所以

$$
\begin{array}{r l} A (s, t) & = \left(\frac {\mu_ {0} I _ {0}}{4 \pi} \hat {z}\right) 2 \int_ {0} ^ {\sqrt {(c t) ^ {2} - s ^ {2}}} \frac {\mathrm{d} z}{\sqrt {s ^ {2} + z ^ {2}}} \\ & = \left. \frac {\mu_ {0} I _ {0}}{2 \pi} \hat {z} \ln \left(\sqrt {s ^ {2} + z ^ {2}} + z\right) \right| _ {0} ^ {\sqrt {(c t) ^ {2} - s ^ {2}}} = \frac {\mu_ {0} I _ {0}}{2 \pi} \ln \left(\frac {c t + \sqrt {(c t) ^ {2} - s ^ {2}}}{s}\right) \hat {z} \end{array}
$$

电场是

$$
\boldsymbol {E} (s, t) = - \frac {\partial \boldsymbol {A}}{\partial t} = - \frac {\mu_ {0} I _ {0} c}{2 \pi \sqrt {(c t) ^ {2} - s ^ {2}}} \hat {z}
$$

磁场是

$$
\pmb {B} (s, t) = \nabla \times \pmb {A} = - \frac {\partial A _ {z}}{\partial s} \hat {\phi} = \frac {\mu_ {0} I _ {0}}{2 \pi s} \frac {c t}{\sqrt {(c t) ^ {2} - s ^ {2}}} \hat {\phi}
$$

注意到当 $t \to \infty$ 时，我们回到静态的情形 $\pmb{E} = \mathbf{0}$ ， $\pmb{B} = (\mu_0 I_0 / 2\pi s) \hat{\phi}$ 。

!习题 10.10 证明推迟势满足洛伦茨规范条件。[提示：首先证明

$$
\nabla \cdot \left(\frac {\boldsymbol {J}}{\mathcal {I}}\right) = \frac {1}{\mathcal {I}} (\nabla \cdot \boldsymbol {J}) + \frac {1}{\mathcal {I}} \left(\nabla^ {\prime} \cdot \boldsymbol {J}\right) - \nabla^ {\prime} \cdot \left(\frac {\boldsymbol {J}}{\mathcal {I}}\right)
$$

这里 $\nabla$ 表示对 $r$ 的导数， $\nabla'$ 表示对 $r'$ 的导数。其次注意 $J(r', t - 2/c)$ 显式地依赖 $r'$ 以及通过 $2$ 隐含地依赖 $r'$ ，而对 $r$ 的依赖仅通过 $2$ ，证明

$$
\nabla \cdot \boldsymbol {J} = - \frac {1}{c} \dot {\boldsymbol {J}} \cdot (\nabla^ {\prime}), \quad \nabla^ {\prime} \cdot \boldsymbol {J} = - \dot {\rho} - \frac {1}{c} \boldsymbol {J} \cdot (\nabla^ {\prime} ^ {\prime}).
$$

利用它计算 A 的散度 [式(10.26)]。]

!习题 10.11

（a）设在例题10.2中导线中的电流线性增大：

$$
I (t) = k t
$$

对 $t > 0$ ，求出产生的电磁场。
(b) 求出脉冲电流

$$
I (t) = q _ {0} \delta (t)
$$

产生的电磁场。

习题10.12 一导线如图10.5所示绕成一个回路，回路中有一随时间线性增加的电流

$$
I (t) = k t \quad (- \infty <   t <   \infty)
$$

计算中心处的推迟矢势，求出中心处的电场。为何这个中性的导线产生一个电场？（从 A 的表示式你为何不能确定磁场？）

![](images/a2dbd9b1e989a2a1f31a1884e8c63386e5000db9b1b42b4f5689bd1daf028044.jpg)  
图10.5

## 10.2.2 Jefimenko's 方程

给出推迟势

$$
V (\boldsymbol {r}, t) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\rho \left(\boldsymbol {r} ^ {\prime} , t _ {r}\right)}{r} \mathrm{d} \tau^ {\prime}, \quad \boldsymbol {A} (\boldsymbol {r}, t) = \frac {\mu_ {0}}{4 \pi} \int \frac {\boldsymbol {J} \left(\boldsymbol {r} ^ {\prime} , t _ {r}\right)}{r} \mathrm{d} \tau^ {\prime}\tag{10.33}
$$

原则上可直接求出场

$$
\boldsymbol {E} = - \nabla V - \frac {\partial \boldsymbol {A}}{\partial t}, \quad \boldsymbol {B} = \nabla \times \boldsymbol {A}\tag{10.34}
$$

但具体求解并不简单，因为如我前面提到的，积分既通过分母中的 $r = |r - r'|$ 显式依赖 $\pmb{r}$ ，又通过分子中的推迟时刻 $t_r \equiv t - \frac{\pi}{c}$ 隐式地依赖于 $\pmb{r}$ 。

我们已经计算了 $V$ 的梯度[式(10.29)]， $\pmb{A}$ 对时间的导数容易求出：

$$
\frac {\partial \boldsymbol {A}}{\partial t} = \frac {\mu_ {0}}{4 \pi} \int \frac {\dot {\boldsymbol {J}}}{r} \mathrm{d} \tau^ {\prime}\tag{10.35}
$$

把它们放在一起（并利用 $c^2 = 1 / \mu_0\varepsilon_0$ ）：

$$
\boxed {E (\boldsymbol {r}, t) = \frac {1}{4 \pi \varepsilon_ {0}} \int \left[ \frac {\rho \left(\boldsymbol {r} ^ {\prime} , t _ {r}\right)}{r ^ {2}} \hat {\boldsymbol {r}} + \frac {\dot {\rho} \left(\boldsymbol {r} ^ {\prime} , t _ {r}\right)}{c r} \hat {\boldsymbol {r}} - \frac {\dot {\boldsymbol {J}} \left(\boldsymbol {r} ^ {\prime} , t _ {r}\right)}{c ^ {2} r} \right] \mathrm{d} \tau^ {\prime}}\tag{10.36}
$$

这就是库仑定律的时间相关推广，它可回到静态时的情形（第二项和第三项去掉，第一项中去掉对 $t_{r}$ 的依赖）。

对于 $\pmb{B}$ ， $\pmb{A}$ 的旋度包含有两项

$$
\nabla \times \boldsymbol {A} = \frac {\mu_ {0}}{4 \pi} \int \left[ \frac {1}{r} (\nabla \times \boldsymbol {J}) - \boldsymbol {J} \times \nabla \left(\frac {1}{r}\right) \right] d \tau^ {\prime}
$$

现在考虑到

$$
(\nabla \times \boldsymbol {J}) _ {x} = \frac {\partial J _ {z}}{\partial y} - \frac {\partial J _ {y}}{\partial z}
$$

以及

$$
\frac {\partial J _ {z}}{\partial y} = \dot {J} _ {z} \frac {\partial t _ {r}}{\partial z} = - \frac {1}{c} \dot {J} _ {z} \frac {\partial r}{\partial y}
$$

所以

$$
(\nabla \times \boldsymbol {J}) _ {x} = - \frac {1}{c} \left(\dot {J} _ {z} \frac {\partial r}{\partial y} - \dot {J} _ {y} \frac {\partial r}{\partial z}\right) = \frac {1}{c} [ \boldsymbol {J} \times (\nabla r) ] _ {x}
$$

但 $\nabla r = \hat{\pmb{r}}$ （习题1.13），故

$$
\nabla \times \boldsymbol {J} = \frac {1}{c} \dot {\boldsymbol {J}} \times \hat {\boldsymbol {n}}\tag{10.37}
$$

然而 $\nabla (1 / \mathfrak{z}) = -\hat{\mathbf{z}} / \mathfrak{z}^2$ （习题1.13），因此

$$
\boxed {B (\boldsymbol {r}, t) = \frac {\mu_ {0}}{4 \pi} \int \left[ \frac {\boldsymbol {J} (\boldsymbol {r} ^ {\prime} , t _ {r})}{\nu^ {2}} + \frac {\dot {\boldsymbol {J}} (\boldsymbol {r} ^ {\prime} , t _ {r})}{c ^ {2}} \right] \times \hat {\mathbf {z}} \mathrm{d} \tau^ {\prime}}\tag{10.38}
$$

这是毕奥-萨伐尔定律的时间相关推广，从它可回到静态时的形式。

式(10.36)和式(10.38)是（满足因果律的）麦克斯韦方程的解。由于某些原因，它们直到近期才发表——我知道的最早的明确的叙述是由 Oleg Jefimenko 在 1966 年发表的 $^{11}$ 。实际中，Jefimenko's 方程应用有限，因为一般地求推迟势并求导比直接求场容易。然而，它们为理论提供了一种令人满意完整的感觉。它们也帮我们对前面所提到的一个论述进行了澄清：为了得到推迟势，你所做的一切是把静电和静磁公式中的 t 换为 $t_{r}$ 。但对于场，不但要把时间换为推迟时刻，而且还出现了新的（涉及 $\rho$ 和 J 的导数的）项。它们对似稳近似提供了很强的支持（习题 10.14）。

习题10.13 设 $J(\pmb{r})$ 不随时间变化，所以有（习题7.60） $\rho (\pmb {r},t) = \rho (\pmb {r},0) + \dot{\rho} (\pmb {r},0)t$ 。证明

$$
\boldsymbol {E} (\boldsymbol {r}, t) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\rho (\boldsymbol {r} ^ {\prime} , t)}{r ^ {2}} \hat {\boldsymbol {z}} \mathrm{d} \tau^ {\prime}
$$

即电荷密度按“非推迟”时间计算时，库仑定律成立。

习题 10.14 假设电流密度缓慢变化以至于我们能够（在足够好的近似下）忽略泰勒展开式的所有高阶项：

$$
\boldsymbol {J} \left(t _ {r}\right) = \boldsymbol {J} (t) + \left(t _ {r} - t\right) \dot {\boldsymbol {J}} (t) + \dots
$$

（为了清楚，我省去了对 $r$ 的依赖，它与讨论的问题无关）。证明在式(10.38)中通过一个幸运的相消后可得到

$$
\boldsymbol {B} (\boldsymbol {r}, t) = \frac {\mu_ {0}}{4 \pi} \int \frac {\boldsymbol {J} \left(\boldsymbol {r} ^ {\prime} , t\right) \times \hat {\boldsymbol {r}}}{v ^ {2}} \mathrm{d} \tau^ {\prime}
$$

即：以非推迟时间计算 $J$ ，毕奥-萨伐尔定律成立。这意味着似稳近似实际上比我们希望的要好很多：所包含的两个误差[忽略了推迟和省去了式(10.38)的第二项]在一阶近似下彼此相消。

## 10.3 点电荷

## 10.3.1 李纳-维谢尔势

我们的下一个任务是计算以一个特定轨迹

$$
\pmb {w} (t) = \text {在时刻} t \text {电荷} q \text {的位置}\tag{10.39}
$$

运动的点电荷的（推迟）势 $V(r,t)$ 和 $A(r,t)$ 。初看式(10.26)

$$
V (\boldsymbol {r}, t) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\rho \left(\boldsymbol {r} ^ {\prime} , t _ {r}\right)}{2} \mathrm{d} \tau^ {\prime}\tag{10.40}
$$

可能暗示点电荷推迟势应简单地为

$$
\frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r}
$$

（与静态的情形一样，只是把 $\nu$ 理解为距电荷推迟位置的距离）。但这是错误的，因为一个非常微妙的原因：对于点源，可以把分母 $\nu$ 移到积分外 $^{12}$ ，但剩余的

$$
\int \rho \left(\boldsymbol {r} ^ {\prime}, t _ {r}\right) \mathrm{d} \tau^ {\prime}\tag{10.41}
$$

不等于粒子的电荷（通过 $t_r$ 依赖于场点 $\pmb{r}$ ）。为了计算一个物体的总电荷，你必须在某瞬时对电荷的整个分布 $\rho$ 进行积分。但这里的延迟， $t_r = t - \nu / c$ ，迫使我们对此物体的不同部分在不同时刻计 $\rho$ 。如果源是运动的，这将给出一个扭曲的总电荷图像。你也许认为这个问题对点电荷不存在，但并非如此。在麦克斯韦电动力学中，公式中出现电荷和电流密度，点电荷必须被认为是当体积趋于零时非点电荷的极限。对于一个非点粒子，无论其多么小，式(10.41)中的推迟项总有因子 $(1 - \hat{\mathbf{z}} \cdot \mathbf{v} / c)^{-1}$ ，式中 $\pmb{v}$ 是在推迟时刻电荷的速度，即

$$
\int \rho (\boldsymbol {r} ^ {\prime}, t _ {r}) \mathrm{d} \tau^ {\prime} = \frac {q}{1 - \hat {\textbf {z}} \cdot \boldsymbol {v} / c}\tag{10.42}
$$

[证明]：这纯粹是一个几何效应，它可以帮助我们较形象地理解所述内容。由于过于寻常，你们可能没有注意到它，但事实上向你开来的火车看上去要比实际的略长，因为你看到的从最后一节守车 $^{13}$ 车厢发出的光要早于你同时看到的从车头发出的光，在较早时火车距离比较远（图 10.6）。在这个时间间隔中，从守车发出的光走过了多余的距离 $L'$ ，火车本身走过了距离 $L' - L$ ：

$$
\frac {L ^ {\prime}}{c} = \frac {L ^ {\prime} - L}{v} \quad \text {或者} \quad L ^ {\prime} = \frac {L}{1 - v / c}
$$

![](images/6939e0d9df7dc39c2dd737a8303e23ffdcdaacf9a069c433c4c55f5fef3f8b95.jpg)  
图10.6

所以接近的火车显得较长，需乘一个因子 $(1 - v / c)^{-1}$ 。相反，离开的火车看起来较短[14]，需乘一个因子 $(1 + v / c)^{-1}$ 。更一般地，如果火车的速度与你看的光线成一个角度[15]，从守车发出的光经过的附加距离是 $L^{\prime}\cos \theta$ （图10.7）。在 $L^{\prime}\cos \theta /c$ 时间内，火车移动一个距离 $L^{\prime} - L$

$$
\frac {L ^ {\prime} \cos \theta}{c} = \frac {L ^ {\prime} - L}{v} \quad \text {或者} \quad L ^ {\prime} = \frac {L}{1 - v \cos \theta / c}
$$

![](images/c13056459e1562de3df2998976cea86d03b5aaace732ef370925f0baa047b14a.jpg)  
图10.7

注意这个效应对垂直于火车运动方向的维度（火车的高度和宽度）不起作用。不必在意从侧面远处的光线到达你较迟（与侧面近处的光相比）——因为在侧向没有运动，它们的距离不变。火车表观体积与实际体积有关系

$$
\tau^ {\prime} = \frac {\tau}{1 - \hat {\mathbf {z}} \cdot \mathbf {v} / c}\tag{10.43}
$$

式中， $\hat{\pmb{z}}$ 是从火车到观察者的单位矢量。

移动的火车和推迟势类比的要点是：无论何时求式(10.41)类型的积分，被积函数是在推迟时刻的值，因为同样的原因，有效的体积由式(10.43)中出现的因子所修正，就像火车的表观体积那样。因为这个修正因子与粒子的体积大小没有关系，对点电荷的修正与对非点电荷的修正是一样的。

同时，对于一个点电荷推迟时刻隐式地由方程

$$
\left| \boldsymbol {r} - \boldsymbol {w} \left(t _ {r}\right) \right| = c \left(t - t _ {r}\right)\tag{10.44}
$$

确定。因为左边是“信号”必须传播的距离， $(t-t_{r})$ 是它传播过程花费的时间（图10.8）。z是从推迟位置到场点r的矢量：

$$
\boldsymbol {r} = \boldsymbol {r} - \boldsymbol {w} \left(t _ {r}\right)\tag{10.45}
$$

需要着重强调的是在任何特定的时间 $t$ ，轨道上最多仅有一个点与 $\pmb{r}$ 通信。如果假设有两个这样的点，它们有推迟时刻 $t_1$ 和 $t_2$ ：

$$
\mathfrak {r} _ {1} = c \left(t - t _ {1}\right) \quad \text {和} \quad \mathfrak {r} _ {2} = c \left(t - t _ {2}\right)
$$

则 $\nu_{1}-\nu_{2}=c(t_{2}-t_{1})$ ，所以粒子在 r 方向的平均速度应是 c——不管电荷在其他方向的速度如何。因为没有带电粒子的速度能超过光速，这表明在任何时刻只有一个推迟点 $^{16}$ 对势有贡献 $^{17}$ 。

![](images/46212f797cd053ad05fa1610bd3b16938e6b50219deef340d873b5c31e8cc8f1.jpg)  
图10.8

由此，有

$$
\boxed {V (\boldsymbol {r}, t) = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q c}{(\mathcal {R} c - \mathbf {r} \cdot \boldsymbol {v})}}\tag{10.46}
$$

式中， $\pmb{v}$ 是在推迟时刻电荷的速度； $\pmb{z}$ 是从推迟的位置到场点 $\pmb{r}$ 的矢量。进而，因为电流密度是 $\rho \pmb{v}$ [式 (5.26)]，矢势为

$$
\boldsymbol {A} (\boldsymbol {r}, t) = \frac {\mu_ {0}}{4 \pi} \int \frac {\rho \left(\boldsymbol {r} ^ {\prime} , t _ {r}\right) \boldsymbol {v} \left(t _ {r}\right)}{\imath} \mathrm{d} \tau^ {\prime} = \frac {\mu_ {0}}{4 \pi} \frac {\boldsymbol {v}}{\imath} \int \rho \left(\boldsymbol {r} ^ {\prime}, t _ {r}\right) \mathrm{d} \tau^ {\prime}
$$

或者

$$
\boxed {A (\boldsymbol {r}, t) = \frac {\mu_ {0}}{4 \pi} \frac {q c \boldsymbol {v}}{\left(\imath c - \boldsymbol {r} \cdot \boldsymbol {v}\right)} = \frac {\boldsymbol {v}}{c ^ {2}} V (\boldsymbol {r}, t)}\tag{10.47}
$$

式(10.46)和式(10.47)是一个运动点电荷的著名的李纳-维谢尔势（Liénard-Wiechert potentials） $^{18}$ 。

例题10.3 求出匀速运动的点电荷的标势和矢势。

[解答] 方便起见，设粒子在 $t = 0$ 时刻通过原点，故

$$
\boldsymbol {w} (t) = \boldsymbol {v} t
$$

首先利用式(10.44)

$$
\left| \boldsymbol {r} - \boldsymbol {v} t _ {r} \right| = c \left(t - t _ {r}\right)
$$

计算推迟时刻，或其平方

$$
r ^ {2} - 2 \pmb {r} \cdot \pmb {v} t _ {r} + v ^ {2} t _ {r} ^ {2} = c ^ {2} \left(t ^ {2} - 2 t t _ {r} + t _ {r} ^ {2}\right)\tag{\( ^{22} \)

\( ^{22} \}
$$

通过二次方程求根公式，求得

$$
t _ {r} = \frac {\left(c ^ {2} t - \boldsymbol {r} \cdot \boldsymbol {v}\right) \pm \sqrt {\left(c ^ {2} t - \boldsymbol {r} \cdot \boldsymbol {v}\right) ^ {2} + \left(c ^ {2} - v ^ {2}\right) \left(r ^ {2} - c ^ {2} t ^ {2}\right)}}{c ^ {2} - v ^ {2}}\tag{10.48}
$$

为了确定正负号，考虑极限情况，

$$
t _ {r} = t \pm \frac {r}{c}
$$

在这种情况下，电荷静止在原点，推迟时刻应为 $(t - r / c)$ ，因此应取负号。现在，由式(10.44)和式(10.45)

$$
\mathbf {r} = c \left(t - t _ {r}\right) \quad \text {和} \quad \hat {\mathbf {r}} = \frac {\mathbf {r} - v t _ {r}}{c \left(t - t _ {r}\right)}
$$

所以

$$
\begin{array}{r l} \boldsymbol {v} (1 - \hat {\textbf {z}} \cdot \textbf {v} / c) & = c (t - t _ {r}) \left[ 1 - \frac {\textbf {v}}{c} \cdot \frac {(\textbf {r} - \textbf {v} t _ {r})}{c (t - t _ {r})} \right] = c (t - t _ {r}) - \frac {\textbf {v} \cdot \textbf {r}}{c} + \frac {v ^ {2}}{c} t _ {r} \\ & = \frac {1}{c} \left[ (c ^ {2} t - \textbf {r} \cdot \textbf {v}) - (c ^ {2} - v ^ {2}) t _ {r} \right] \\ & = \frac {1}{c} \sqrt {(c ^ {2} t - \textbf {r} \cdot \textbf {v}) ^ {2} + (c ^ {2} - v ^ {2}) (r ^ {2} - c ^ {2} t ^ {2})} \end{array}
$$

18 有许多方法求李纳-维谢尔势。我已努力强调参数 $(1 - \hat{\pmb{z}}\cdot \pmb {v} / c)^{-1}$ 的几何来源；启发性的评述可参看W.K.H.Panofsky和M.Phillips,Classical Electricity and Magnetism,2d ed.(Reading,MA:Addison-Wesley,1962),pp.342-3。一个更严格的推导见于J.R.Reitz,F.J.Milford和R.W.Christy,Foundations of Electromagnetic Theory,3d ed.(Reading,MA:Addison-Wesley,1979)，第21.1节；或M.A.Heald和J.B.Marion,Classical Electronmagnetic Radiation,3d ed.(Orlando,FL:Saunder,1995)，第8.3节。

[在最后一步利用了式(10.48)，方程中取负号]。故有

$$
V (\boldsymbol {r}, t) = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q c}{\sqrt {(c ^ {2} t - \boldsymbol {r} \cdot \boldsymbol {v}) ^ {2} + (c ^ {2} - v ^ {2}) (r ^ {2} - c ^ {2} t ^ {2})}}\tag{10.49}
$$

以及 [式(10.47)]

$$
\boldsymbol {A} (\boldsymbol {r}, t) = \frac {\mu_ {0}}{4 \pi} \frac {q c \boldsymbol {v}}{\sqrt {(c ^ {2} t - \boldsymbol {r} \cdot \boldsymbol {v}) ^ {2} + (c ^ {2} - v ^ {2}) (r ^ {2} - c ^ {2} t ^ {2})}}\tag{10.50}
$$

习题10.15 一个带电荷为 $q$ 的粒子以角速度 $\omega$ 做半径为 $a$ 的匀速圆周运动。[假设圆处在 $xy$ 平面，圆心在原点，在 $t = 0$ 时刻，粒子位于 $x$ 正轴（ $a,0$ ）处。]求出 $z$ 轴上各点处的李纳-维谢尔势。

习题10.16 以恒定速度运动的点电荷的标势[式(10.49)]可以表示为更简单的形式

$$
V (\boldsymbol {r}, t) = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{R \sqrt {1 - v ^ {2} \sin^ {2} \theta / c ^ {2}}}\tag{10.51}
$$

式中， $R \equiv r - vt$ 为从粒子当前（！）位置指向场点 r 的矢量； $\theta$ 是 R 和 v 之间的角度（图 10.9）。注意对非相对论速度 $(v \ll c)$ ，

$$
V (\boldsymbol {r}, t) \approx \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{R}
$$

![](images/b4074495eea49603f192443cf235f6105d78693f90218a040f4d7f0570023c96.jpg)  
图10.9

习题 10.17 我证明过在粒子轨迹中在任何给定的时间最多只有一点与场点 r 通信。在一些情形可能没有这样的点（在 r 点的观察者不能看到那个粒子——用广义相对论的生动语言描述就是它“超过了视界”）。作为一个例子，考虑一个粒子沿着 x 轴做双曲运动（hyperbolic motion）：

$$
\pmb {w} (t) = \sqrt {b ^ {2} + (c t) ^ {2}} \hat {\pmb {x}} \quad (- \infty <   t <   \infty)\tag{10.52}
$$

（在狭义相对论中，这是一个被施加一个恒定力 $F = mc^2 / b$ 的粒子的运动轨道。）画出 $w$ 对 $t$ 的图形。在这个曲线上选4个或5个代表点，对每个点画出粒子发出的光信号的轨迹——正 $x$ 和负 $x$ 方向都画。在图中的哪个区域对应的点和时间不能看到粒子？在点 $x$ 在哪个时刻能首次看到粒子？（早于此时 $x$ 处的势显然为零。）对于一个粒子，一旦看到，它可能会在视线中消失吗？

!习题 10.18 确定双曲运动 [式(10.52)] 的一个电荷的李纳-维谢尔势。假设场点 r 在 x 轴上位于电荷的右侧 $^{19}$ 。

## 10.3.2 运动点电荷的场

我们现在利用李纳-维谢尔势 $^{20}$

$$
V (\boldsymbol {r}, t) = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q c}{(\imath c - \boldsymbol {r} \cdot \boldsymbol {v})}, \quad \boldsymbol {A} (\boldsymbol {r}, t) = \frac {\boldsymbol {v}}{c ^ {2}} V (\boldsymbol {r}, t)\tag{10.53}
$$

计算任意运动点电荷的电场和磁场。计算 E 和 B 的方程为

$$
\pmb {E} = - \nabla V - \frac {\partial \pmb {A}}{\partial t}, \quad \pmb {B} = \nabla \times \pmb {A}
$$

微分是有技巧的，因为

$$
\pmb {z} = \pmb {r} - \pmb {w} (t _ {r}) \quad \text {和} \quad \pmb {v} = \dot {\pmb {w}} (t _ {r})\tag{10.54}
$$

两者都是在推迟时刻取值，而 $t_r$ ——由下面方程隐式地定义

$$
\left| \boldsymbol {r} - \boldsymbol {w} \left(t _ {r}\right) \right| = c \left(t - t _ {r}\right)\tag{10.55}
$$

它本身是 r 和 t 的函数 $^{21}$ 。请坚持住：下面的两页略显繁杂——但结果值得努力。

让我们首先计算 $V$ 的梯度：

$$
\nabla V = \frac {q c}{4 \pi \varepsilon_ {0}} \frac {- 1}{(\imath c - \imath \cdot v) ^ {2}} \nabla (\imath c - \imath \cdot v)\tag{10.56}
$$

因为 $\nu=c(t-t_{r})^{22}$ ,

$$
\nabla \boldsymbol {\imath} = - c \nabla t _ {r}\tag{10.57}
$$

对于第二项，乘积规则4给出

$$
\nabla (\boldsymbol {z} \cdot \boldsymbol {v}) = (\boldsymbol {z} \cdot \nabla) \boldsymbol {v} + (\boldsymbol {v} \cdot \nabla) \boldsymbol {z} + \boldsymbol {z} \times (\nabla \times \boldsymbol {v}) + \boldsymbol {v} \times (\nabla \times \boldsymbol {z})\tag{10.58}
$$

依次计算其中的每一项

$$
\begin{array}{r l} (\boldsymbol {\mathbf {z}} \cdot \nabla) \boldsymbol {v} & = \left(\imath_ {x} \frac {\partial}{\partial x} + \imath_ {y} \frac {\partial}{\partial y} + \imath_ {z} \frac {\partial}{\partial z}\right) \boldsymbol {v} (t _ {r}) \\ & = \imath_ {x} \frac {\mathrm{d} \boldsymbol {v}}{\mathrm{d} t _ {r}} \frac {\partial t _ {r}}{\partial x} + \imath_ {y} \frac {\mathrm{d} \boldsymbol {v}}{\mathrm{d} t _ {r}} \frac {\partial t _ {r}}{\partial y} + \imath_ {z} \frac {\mathrm{d} \boldsymbol {v}}{\mathrm{d} t _ {r}} \frac {\partial t _ {r}}{\partial z} \\ & = \boldsymbol {a} (\boldsymbol {\mathbf {z}} \cdot \nabla t _ {r}) \end{array}\tag{10.59}
$$

式中， $a \equiv \dot{v}$ 是在粒子推迟时刻的加速度。现在

$$
(\boldsymbol {v} \cdot \nabla) \boldsymbol {z} = (\boldsymbol {v} \cdot \nabla) \boldsymbol {r} - (\boldsymbol {v} \cdot \nabla) \boldsymbol {w}\tag{10.60}
$$

以及

$$
\begin{array}{r l} (\boldsymbol {v} \cdot \nabla) \boldsymbol {r} & = \left(v _ {x} \frac {\partial}{\partial x} + v _ {y} \frac {\partial}{\partial y} + v _ {z} \frac {\partial}{\partial z}\right) (x \hat {\boldsymbol {x}} + y \hat {\boldsymbol {y}} + z \hat {\boldsymbol {z}}) \\ & = v _ {x} \hat {\boldsymbol {x}} + v _ {y} \hat {\boldsymbol {y}} + v _ {z} \hat {\boldsymbol {z}} = \boldsymbol {v} \end{array}\tag{10.61}
$$

而

$$
(\boldsymbol {v} \cdot \nabla) \boldsymbol {w} = \boldsymbol {v} (\boldsymbol {v} \cdot \nabla t _ {r})
$$

[与式(10.59)的理由一样]。接下来对于式(10.58)中的第三项，

$$
\begin{array}{r l} \nabla \times \boldsymbol {v} = & \left(\frac {\partial v _ {z}}{\partial y} - \frac {\partial v _ {y}}{\partial z}\right) \hat {\boldsymbol {x}} + \left(\frac {\partial v _ {x}}{\partial z} - \frac {\partial v _ {z}}{\partial x}\right) \hat {\boldsymbol {y}} + \left(\frac {\partial v _ {y}}{\partial x} - \frac {\partial v _ {x}}{\partial y}\right) \hat {\boldsymbol {z}} \\ = & \left(\frac {\mathrm{d} v _ {z}}{\mathrm{d} t _ {r}} \frac {\partial t _ {r}}{\partial y} - \frac {\mathrm{d} v _ {y}}{\mathrm{d} t _ {r}} \frac {\partial t _ {r}}{\partial z}\right) \hat {\boldsymbol {x}} + \left(\frac {\mathrm{d} v _ {x}}{\mathrm{d} t _ {r}} \frac {\partial t _ {r}}{\partial z} - \frac {\mathrm{d} v _ {z}}{\mathrm{d} t _ {r}} \frac {\partial t _ {r}}{\partial x}\right) \hat {\boldsymbol {y}} + \\ & \left(\frac {\mathrm{d} v _ {y}}{\mathrm{d} t _ {r}} \frac {\partial t _ {r}}{\partial x} - \frac {\mathrm{d} v _ {x}}{\mathrm{d} t _ {r}} \frac {\partial t _ {r}}{\partial y}\right) \hat {\boldsymbol {z}} \\ = & - \boldsymbol {a} \times \nabla t _ {r} \end{array}\tag{10.62}
$$

最后，

$$
\nabla \times \boldsymbol {r} = \nabla \times \boldsymbol {r} - \nabla \times \boldsymbol {w}\tag{10.63}
$$

但 $\nabla \times \pmb{r} = 0$ ，与式(10.62)类似的计算给出

$$
\nabla \times \boldsymbol {w} = - \boldsymbol {v} \times \nabla t _ {r}\tag{10.64}
$$

把所有这些代回式(10.58)，利用“BAC-CAB”规则，化简两重矢量积，

$$
\begin{array}{r l} \nabla (\boldsymbol {z} \cdot \boldsymbol {v}) & = \boldsymbol {a} (\boldsymbol {z} \cdot \nabla t _ {r}) + \boldsymbol {v} - \boldsymbol {v} (\boldsymbol {v} \cdot \nabla t _ {r}) - \boldsymbol {z} \times (\boldsymbol {a} \times \nabla t _ {r}) + \boldsymbol {v} \times (\boldsymbol {v} \times \nabla t _ {r}) \\ & = \boldsymbol {v} + (\boldsymbol {z} \cdot \boldsymbol {a} - v ^ {2}) \nabla t _ {r} \end{array}\tag{10.65}
$$

把式(10.57)和式(10.65)合在一起，我们有

$$
\nabla V = \frac {q c}{4 \pi \varepsilon_ {0}} \frac {1}{(2 c - 2 \cdot v) ^ {2}} [ v + (c ^ {2} - v ^ {2} + 2 \cdot a) \nabla t _ {r} ]\tag{10.66}
$$

为了完成计算，我们需要知道 $\nabla t_r$ 。这可通过对定义式(10.55)求梯度得出——这在式(10.57)中我们已做过——展开 $\nabla r$ :

$$
\begin{array}{r l} - c \nabla t _ {r} & = \nabla \mathbf {z} = \nabla \sqrt {\mathbf {z} \cdot \mathbf {z}} = \frac {1}{2 \sqrt {\mathbf {z} \cdot \mathbf {z}}} \nabla (\mathbf {z} \cdot \mathbf {z}) \\ & = \frac {1}{\mathbf {z}} [ (\mathbf {z} \cdot \nabla) \mathbf {z} + \mathbf {z} \times (\nabla \times \mathbf {z}) ] \end{array}\tag{10.67}
$$

然而

$$
(\boldsymbol {r} \cdot \nabla) \boldsymbol {r} = \boldsymbol {r} - \boldsymbol {v} (\boldsymbol {r} \cdot \nabla t _ {r})
$$

[与式(10.60)同样的思想]，而 [从式(10.63)和式(10.64)]

$$
\nabla \times \boldsymbol {r} = (\boldsymbol {v} \times \nabla t _ {r})
$$

因而，

$$
- c \nabla t _ {r} = \frac {1}{\eta} \left[ \pmb {\mathscr {z}} - \pmb {v} (\pmb {\mathscr {z}} \cdot \nabla t _ {r}) + \pmb {\mathscr {z}} \times (\pmb {v} \times \nabla t _ {r}) \right] = \frac {1}{\eta} \left[ \pmb {\mathscr {z}} - (\pmb {\mathscr {z}} \cdot \pmb {v}) \nabla t _ {r} \right]
$$

于是

$$
\nabla t _ {r} = \frac {- n}{\mathcal {N} - n \cdot v}\tag{10.68}
$$

把这个结果代入式(10.66)，有

$$
\nabla V = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q c}{(\imath c - \boldsymbol {\imath} \cdot \boldsymbol {v}) ^ {3}} \left[ (\imath c - \boldsymbol {\imath} \cdot \boldsymbol {v}) \boldsymbol {v} - (c ^ {2} - v ^ {2} + \boldsymbol {\imath} \cdot \boldsymbol {a}) \boldsymbol {\imath} \right]\tag{10.69}
$$

我留给你一个类似的计算（习题10.19），它给出

$$
\begin{array}{r l} \frac {\partial \boldsymbol {A}}{\partial t} = & \frac {1}{4 \pi \varepsilon_ {0}} \frac {q c}{(\imath c - \imath \cdot \boldsymbol {v}) ^ {3}} \left[ (\imath c - \imath \cdot \boldsymbol {v}) (- \boldsymbol {v} + \imath \boldsymbol {a} / c) + \right. \\ & \left. \frac {\imath}{c} (c ^ {2} - v ^ {2} + \imath \cdot \boldsymbol {a}) \boldsymbol {v} \right] \end{array}\tag{10.70}
$$

综合上面这些结果，引进矢量

$$
\boldsymbol {u} \equiv c \hat {\boldsymbol {r}} - \boldsymbol {v}\tag{10.71}
$$

我得到了

$$
\boxed {E (\boldsymbol {r}, t) = \frac {q}{4 \pi \varepsilon_ {0}} \frac {\boldsymbol {\nu}}{(\boldsymbol {\mathbf {r}} \cdot \boldsymbol {u}) ^ {3}} \left[ \left(c ^ {2} - v ^ {2}\right) \boldsymbol {u} + \boldsymbol {\mathbf {r}} \times (\boldsymbol {u} \times \boldsymbol {a}) \right]}\tag{10.72}
$$

同时，

$$
\nabla \times \boldsymbol {A} = \frac {1}{c ^ {2}} \nabla \times (V \boldsymbol {v}) = \frac {1}{c ^ {2}} [ V (\nabla \times \boldsymbol {v}) - \boldsymbol {v} \times (\nabla V) ]
$$

我们已经计算了 $\nabla \times v$ [式(10.62)] 和 $\nabla V$ [式(10.69)]。把这些结果放在一起，

$$
\nabla \times \boldsymbol {A} = - \frac {1}{c} \frac {q}{4 \pi \varepsilon_ {0}} \frac {1}{(\boldsymbol {u} \cdot \boldsymbol {r}) ^ {3}} \boldsymbol {r} \times \left[ (c ^ {2} - v ^ {2}) \boldsymbol {v} + (\boldsymbol {r} \cdot \boldsymbol {a}) \boldsymbol {v} + (\boldsymbol {r} \cdot \boldsymbol {u}) \boldsymbol {a} \right]
$$

上式中括号中的量与式(10.72)非常相似。利用 BAC-CAB 规则，式(10.72)可写成

$$
\left[ \left(c ^ {2} - v ^ {2}\right) \boldsymbol {u} + (\boldsymbol {z} \cdot \boldsymbol {a}) \boldsymbol {u} - (\boldsymbol {u} \cdot \boldsymbol {u}) \boldsymbol {a} \right]
$$

主要的不同之处仅在于前两项中 v 代替了 u。事实上，因为它们都要与 z 做矢量积，所以我们可以把 v 变成 -u，这并不改变结果，正比于 z 的额外的项在矢量积中消失了。这样有

$$
\boxed {B (\boldsymbol {r}, t) = \frac {1}{c} \hat {\boldsymbol {r}} \times \boldsymbol {E} (\boldsymbol {r}, t)}\tag{10.73}
$$

显然，点电荷的磁场总是垂直于电场，垂直于从推迟点指向场点的位置矢量。

在 E 中的第一项 [包含 $(c^{2}-v^{2})u$ 的项] 与到粒子距离的平方成反比例衰减。如果速度和加速度都为零，只有这一项存在，则回到静电学的结果

$$
E = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r ^ {2}} \hat {\mathbf {r}}
$$

由于这个原因，E 的第一项有时也称为广义库仑场（generalized Coulomb field）。[因为它不依赖于加速度，它也称为速度场（velocity field）。] 第二项 [包含 $\hat{z} \times (u \times a)$ 的项] 以 z 的倒数衰减，故在远距离时占主导。我们在第 11 章中将看到，正是这一项引起电磁辐射，所以它称为辐射场（radiation field）——或因为它正比于 a，也称为加速场（acceleration field）。同样的术语也适用于磁场。

回顾第 2 章，我曾提到，如果可能，我们仅需写出一个电荷施加在另一个电荷上的力，原则上，我们就能求解电动力学。与叠加原理一起，可给出作用在一个实验电荷 Q 上的任何构型（电荷分布）的合力。好吧，……我们到这里了：式 (10.72) 和式(10.73)给出了场，而洛伦兹力定律给出了它们在 Q 上产生的力：

$$
\begin{array}{r l} \boldsymbol {F} = & \frac {q Q}{4 \pi \varepsilon_ {0}} \frac {\boldsymbol {\mathbf {\mu}}}{(\boldsymbol {\mathbf {\mu}} \cdot \boldsymbol {u}) ^ {3}} \Big \{\left[ (c ^ {2} - v ^ {2}) \boldsymbol {u} + \boldsymbol {\mathbf {\mu}} \times (\boldsymbol {u} \times \boldsymbol {a}) \right] + \\ & \frac {\boldsymbol {V}}{c} \times \left[ \boldsymbol {\mathbf {\mu}} \times \left[ (c ^ {2} - v ^ {2}) \boldsymbol {u} + \boldsymbol {\mathbf {\mu}} \times (\boldsymbol {u} \times \boldsymbol {a}) \right] \right] \Big \} \end{array}\tag{10.74}
$$

式中，V 是 Q 的速度；z, u, v 和 a 均在推迟时刻计算。整个经典电动力学的整个理论被包括在这个方程中……但你们明白为何我要从库仑定律开始讲起。

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
例题10.4 求出匀速运动的点电荷的电场和磁场。  
[解答] 在式(10.72)中，令 $a = 0$ 得  
$E = \frac{q}{4\pi\varepsilon_0}\frac{(c^2 - v^2)\lambda}{(\mathbf{z} \cdot \mathbf{u})^3}\mathbf{u}$  
在这种情况下，利用 $\pmb{w} = \pmb{v}t,$ $\forall u = c\mathbf{z} - \forall v = c(r - vt_r) - c(t - t_r)\mathbf{v} = c(r - vt)$  
在例题10.3中，我们发现  
$\forall c - \mathbf{z} \cdot \mathbf{v} = \mathbf{z} \cdot \mathbf{u} = \sqrt{(c^2t - r \cdot v)^2 + (c^2 - v^2)(r^2 - c^2t^2)}$  
在习题10.16中，你证明了这一根式可写成  
$Rc\sqrt{1 - v^2\sin^2\theta / c^2}$  
式中，  
$\pmb {R} \equiv \pmb {r} - \pmb {v}t$
</div>

是粒子现在的位置至 $r$ 处的位置矢量； $\theta$ 是 $\pmb{R}$ 和 $\pmb{v}$ 之间的角度（图10.9），故

$$
\boxed {E (r, t) = \frac {q}{4 \pi \varepsilon_ {0}} \frac {1 - v ^ {2} / c ^ {2}}{\left(1 - v ^ {2} \sin^ {2} \theta / c ^ {2}\right) ^ {3 / 2}} \frac {\hat {R}}{R ^ {2}}}\tag{10.75}
$$

注意 E 指向发自粒子当前位置的线。这是一个极不寻常的巧合，因为“信息”是从推迟位置发出的。因为 $\sin^{2}\theta$ 在分母中，一个高速运动电荷的场在垂直运动方向是平的，像一个薄烤饼（图 10.10）。在前方和后方，E 与静止点电荷的场相比减小了一个因子 $(1-v^{2}/c^{2})$ ；而在垂直方向增强了一个因子 $1/\sqrt{1-v^{2}/c^{2}}$ 。

对于 $\pmb{B}$ ，我们有

$$
\hat {\pmb {r}} = \frac {\pmb {r} - \pmb {v} t _ {r}}{r} = \frac {(\pmb {r} - \pmb {v} t) + (t - t _ {r}) \pmb {v}}{r} = \frac {\pmb {R}}{r} + \frac {\pmb {v}}{c}
$$

所以

$$
\pmb {B} = \frac {1}{c} (\pmb {\hat {r}} \times \pmb {E}) = \frac {1}{c ^ {2}} (\pmb {v} \times \pmb {E})\tag{10.76}
$$

B 的磁场线环绕着这个电荷，如图 10.11 所示。

![](images/5f2cd640892a94b30f8883060ae7f71fd43d087da19a11696ac63d4b98aa2d43.jpg)  
图10.10

![](images/18032d998493b58d715dd75456a5ff6ef38763a2df3ba4370668bdf390329c65.jpg)  
图10.11

匀速运动点电荷的场 [式(10.75)和式(10.76)] 由 Oliver Heaviside 在 1888 年首先得到 $^{23}$ ，当 $v^{2} \ll c^{2}$ 时，它们简化为

$$
\boldsymbol {E} (\boldsymbol {r}, t) \approx \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{R ^ {2}} \hat {\boldsymbol {R}}, \quad \boldsymbol {B} (\boldsymbol {r}, t) \approx \frac {\mu_ {0}}{4 \pi} \frac {q}{R ^ {2}} (\boldsymbol {v} \times \hat {\boldsymbol {R}})\tag{10.77}
$$

第一个实际上是库仑定律，第二个是“点电荷的毕奥-萨伐尔定律”，在第5章我曾告知过你们[式(5.43)]。

习题10.19 推导出式(10.70)。首先证明

$$
\frac {\partial t _ {r}}{\partial t} = \frac {\imath c}{\pmb {r} \cdot \pmb {u}}\tag{10.78}
$$

习题10.20 设点电荷 $q$ 被限制在沿着 $x$ 轴方向运动。证明轴上电荷右边的点处的场为

$$
\pmb {E} = \frac {q}{4 \pi \varepsilon_ {0}} \frac {1}{r ^ {2}} \left(\frac {c + v}{c - v}\right) \hat {\pmb {x}}, \quad \pmb {B} = \mathbf {0}
$$

不要假设 $v$ 是不变的，电荷左边的点处的场如何？

习题10.21 对于匀速运动的点电荷，以点电荷当前位置为圆心的圆面，计算电通量 $\oint E\cdot \mathrm{d}\alpha$ [利用式(10.75)]24。

习题10.22

(a) 一均匀带电的无限长直导线，其线电荷密度为 $\lambda$ 。导线以速度 $v$ 沿其轴线方向运动，利用式(10.75)计算距离导线为 $d$ 处的电场。

(b) 利用式(10.76)计算导线产生的磁场。

习题10.23 对习题10.15的构型，求其中心的电场和磁场。根据你求出的 $B$ 的公式，确定圆形稳恒电流 $I$ 在其中心的磁场，把你的结果与例题5.6比较。

## 第10章补充习题

习题10.24 假设你拿着半径为 $a$ 的塑料环，有电荷附着在上面，线电荷密度为 $\lambda_0|\sin (\theta /2)|$ 。使环以角速度 $\omega$ 绕其轴旋转。求出在环中心处（精确的）标势和矢势。

$$
[ \text {答案:} A = (\mu_ {0} \lambda_ {0} \omega a / 3 \pi) \{\sin [ \omega (t - a / c) ] \hat {\pmb x} - \cos [ \omega (t - a / c) ] \hat {\pmb y} \} ]
$$

习题10.25 图2.35总结了静电学的定律，用一个三角形的图示指出了源 $(\rho)$ ，场（ $E$ ）和势（ $V$ ）的关系。图5.48同样总结了静磁学的定律，那里源是 $J$ ，场是 $B$ ，势是 $A$ 。对电动力学画出同样的图形，在这里源为 $(\rho)$ 和 $J$ （被连续性方程限制），场是 $E$ 和 $B$ ，势是 $V$ 和 $A$ （被洛伦茨规范限制）。不要包括以 $E$ 和 $B$ 表示的 $V$ 和 $A$ 的公式。

习题10.26 一个膨胀的球体，其半径为 $R(t) = vt$ （ $t > 0$ ， $v$ 为常量），其中有总电荷 $Q$ 均匀分布在球体内部。相对于球心计算如下积分：

$$
Q _ {\mathrm{eff}} = \int \rho (\boldsymbol {r}, t _ {r}) \mathrm{d} \tau
$$

证明若 $v \ll c, Q_{\mathrm{eff}} \approx Q\left(1 - \frac{3v}{4c}\right)$ 。

习题 10.27 验证匀速运动点电荷的势 [式(10.49)和式(10.50)] 满足洛伦茨规范 [式(10.12)]。

习题10.28 电荷为 $q_{1}$ 的一个粒子静止在原点，另一个电荷为 $q_{2}$ 的粒子沿 $x$ 轴以双曲函数接近：

$$
x (t) = \sqrt {b ^ {2} + (c t) ^ {2}}
$$

在 $t = 0$ 时刻，它到达最接近点 $b$ ，随后折返至无穷远。

(a) 在时刻 $t$ ，（由于 $q_{1}$ ）作用在 $q_{2}$ 上的力 $F_{2}$ 是什么？

(b) $q_{1}$ 对 $q_{2}$ 的总的冲量 $\left(I_2 = \int_{-\infty}^{\infty}F_2\mathrm{d}t\right)$ 是什么？

(c) 在时刻 $t$ ，（由于 $q_{2}$ ）作用在 $q_{1}$ 上的力 $F_{1}$ 是什么？

(d) $q_{2}$ 对 $q_{1}$ 的总的冲量 $\left(I_{1} = \int_{-\infty}^{\infty}F_{1}\mathrm{d}t\right)$ 是什么？[提示：在做这个积分之前，复习习题10.17也许会有帮助。答案： $I_{2} = -I_{1} = q_{1}q_{2} / 4\varepsilon_{0}bc]$

习题10.29 我们现在可以定量处理第8.2.1节这个例子了。设 $q_{1}$ 位于 $x_{1} = -vt$ ，而 $q_{2}$ 位于 $y = -vt$ （图8.3， $t < 0$ ）。计算 $q_{1}$ 与 $q_{2}$ 受到的电场力与磁场力，牛顿第三定律是否遵守？

习题10.30 一根均匀带电的棒（长度为 $L$ ，电荷线密度为 $\lambda$ ）以恒定速率 $v$ 沿 $x$ 轴滑动。在 $t = 0$ 时刻，带电棒后端经过原点（因此其作为时间函数的位置为 $x = vt$ ，而前端位于 $x = vt + L$ ）。对于 $t > 0$ ，计算原点处作为时间函数的推迟标量势。[首先确定后端的推迟时刻 $t_1$ ，前端的推迟时刻 $t_2$ ，以及相应的推迟位置 $x_1$ 、 $x_2$ 。]你的结果在点电荷极限（ $L \ll vt$ ，且 $\lambda L = q$ ）下是否与李纳-维谢尔势一致？

习题10.31 一个电荷为 $q$ 的粒子以恒定速率 $v$ 沿 $x$ 轴运动。计算粒子在原点时刻时，通过平面 $x = a$ 的总功率。[答案： $q^2 v / 32\pi \varepsilon_0 a^2$ ]

习题10.32 $^{25}$ 电荷为 $q_{1}$ 的粒子静止在原点，电荷为 $q_{2}$ 的第二个粒子沿 $z$ 轴以恒定速率 $v$ 运动。

(a) 求在时刻 $t$ ( $q_{2}$ 在 $z = vt$ 处), $q_{1}$ 作用在 $q_{2}$ 上的力 $\pmb{F}_{12}$ 。

(b) 求在时刻 $t, q_{2}$ 作用在 $q_{1}$ 上的力 $\pmb{F}_{21}$ 。在这种情况下牛顿第三定律成立吗？

!(c) 计算时刻 t 时，电磁场中的线动量 $\boldsymbol{p}(t)$ 。[不要被不随时间变化的项干扰，因为你在（d）部分不需要它们。] [答案： $(\mu_{0}q_{1}q_{2}/4\pi t)\hat{\boldsymbol{z}}$ ]

(d) 证明总的力等于场中动量变化率的负值，解释其物理含义。

习题 10.33 发展具有磁单极子的电动力学 [式(7.44)] 势的程式 [提示：你将需要两个标势和两个矢势。采用洛伦茨规范。找出推迟势——推广式(10.26)，并给出用势表示的场强 E 和 B——推广式(10.2)和式(10.3)。]

!习题 10.34 计算位于原点的时间相关的理想电偶极子 $p(t)$ （它是静止的，但它的大小和/或方向随着时间而变化）的势（洛伦茨规范）和场 $^{26}$ 不要对接触项费心。[答案：

$$
V (\boldsymbol {r}, t) = \frac {1}{4 \pi \varepsilon_ {0}} \frac {\hat {\boldsymbol {r}}}{r ^ {2}} \cdot [ \boldsymbol {p} + (r / c) \dot {\boldsymbol {p}} ]
$$

$$
\boldsymbol {A} (\boldsymbol {r}, t) = \frac {\mu_ {0}}{4 \pi} \left[ \frac {\dot {\boldsymbol {p}}}{r} \right]
$$

$$
E (\boldsymbol {r}, t) = - \frac {\mu_ {0}}{4 \pi} \left\{\frac {\ddot {\boldsymbol {p}} - \hat {\boldsymbol {r}} (\dot {\boldsymbol {r}} \cdot \ddot {\boldsymbol {p}})}{r} + c ^ {2} \frac {[ \boldsymbol {p} + (r / c) \dot {\boldsymbol {p}} ] - 3 \hat {\boldsymbol {r}} [ \hat {\boldsymbol {r}} \cdot (\boldsymbol {p} + (r / c) \dot {\boldsymbol {p}}) ]}{r ^ {3}} \right\}
$$

$$
\boldsymbol {B} (\boldsymbol {r}, t) = - \frac {\mu_ {0}}{4 \pi} \left\{\frac {\hat {\boldsymbol {r}} \times [ \dot {\boldsymbol {p}} + (r / c) \ddot {\boldsymbol {p}} ]}{r ^ {2}} \right\}
$$

其中 p 的所有导数都在推迟时刻取值。]

## 11.1 偶极辐射

## 11.1.1 什么是辐射

当电荷加速时，它们的场会不可逆地将能量传输到无穷大——我们称之为辐射（radiation） $^{1}$ 。假设源局域在原点附近 $^{2}$ ；我们将计算在 $t_{0}$ 时刻它辐射出去的能量。想象一个半径为r的巨大球壳（图11.1），通过这个面的总功率是对坡印亭矢量的积分：

$$
P (r, t) = \oint \boldsymbol {S} \cdot \mathrm{d} \boldsymbol {a} = \frac {1}{\mu_ {0}} \oint (\boldsymbol {E} \times \boldsymbol {B}) \cdot \mathrm{d} \boldsymbol {a}\tag{11.1}
$$

![](images/bfbbc6200edd221cf17168ed0e199ec8c57a40f744dd21062b1a40a8be67b374.jpg)  
图11.1

由于电磁“信号”以光速传播 $^{3}$ ，这一能量实际上在更早的时刻 $t_{0}=t-r/c$ 离开源，于是辐射功率为

$$
P _ {\text {辐射}} \left(t _ {0}\right) = \lim _ {r \to \infty} P \left(r, t _ {0} + \frac {r}{c}\right)\tag{11.2}
$$

（其中 $t_{0}$ 保持常数）。这个能量（单位时间的）传播至无穷远，且不再返回。

现在，球壳的面积是 $4\pi r^2$ ，故有辐射发生时，坡印亭矢量减小（在 $r$ 较大时）不能快于 $1 / r^2$ （例如，如果它以 $1 / r^3$ 的方式减小， $P$ 将以 $1 / r$ 减小， $P_{\text{辐射}}$ 就是零）。根据库仑定律，静电场以 $1 / r^2$ 的形式减小（或更快，如果总电荷是零），而毕奥-萨伐尔定律告诉我们，静磁场以 $1 / r^2$ （或更快）的方式减少，这意味着对于静止情形 $S\sim 1 / r^4$ ，故静止的源不会辐射。但Jefimenko方程[式(10.36)和式(10.38)]指出，时间有关的场包含的一些项（包含 $\dot{\rho}$ 和 $\dot{J}$ ）以 $1 / r$ 变化；正是由于这些项导致电磁辐射。

这样，对辐射的研究涉及找出 E 和 B 中在远离源处以 1/r 变化的部分，由此构造 S 中 $1/r^{2}$ 项，在一个大球面上积分 $^{4}$ ，并取 $r \rightarrow \infty$ 时的极限。我们将首先对振动的电偶极子和磁偶极子进行这些操作；然后在 11.2 节，考虑更复杂的加速点电荷的辐射。

## 11.1.2 电偶极子辐射

想象两个小金属球相距为 d 并用一根细导线相连（图 11.2）。在 t 时刻，上面的小球带电 $q(t)$ ，下面的小球带电 $-q(t)$ 。假设驱动电荷通过导线从一端到另一端以角频率 $\omega$ 来回运动：

$$
q (t) = q _ {0} \cos (\omega t)\tag{11.3}
$$

这样产生一个振荡的电偶极子 $^{5}$ ：

$$
\boldsymbol {p} (t) = p _ {0} \cos (\omega t) \hat {z}\tag{11.4}
$$

式中，

$$
p _ {0} \equiv q _ {0} d
$$

是偶极矩最大值。

![](images/33bdb81cd25cdb52e6f69cf30abfea136b4e652571e7c4a47f2a262a4d579739.jpg)  
图11.2

推迟势 [式 (10.26)] 为

$$
V (\boldsymbol {r}, t) = \frac {1}{4 \pi \varepsilon_ {0}} \left\{\frac {q _ {0} \cos [ \omega (t - r _ {+} / c) ]}{r _ {+}} - \frac {q _ {0} \cos [ \omega (t - r _ {-} / c) ]}{r _ {-}} \right\}\tag{11.5}
$$

式中，由余弦定理，

$$
r _ {\pm} = \sqrt {r ^ {2} \mp r \mathrm{d} \cos \theta + (d / 2) ^ {2}}\tag{11.6}
$$

现在为了把物理偶极子变成理想偶极子，我们使正负电荷相距非常小：

$$
\text { 近似 } 1: \quad d \ll r\tag{11.7}
$$

当然，如果 $d$ 是零，则根本得不到势；我们想得到的是关于 $d$ 展开的一阶近似。即

$$
\eta_ {\pm} \approx r \left(1 \mp \frac {d}{2 r} \cos \theta\right)\tag{11.8}
$$

由此

$$
\frac {1}{r _ {\pm}} \approx \frac {1}{r} \left(1 \pm \frac {d}{2 r} \cos \theta\right)\tag{11.9}
$$

以及

$$
\begin{array}{r l} & {\cos \left[ \omega \left(t - r _ {\pm} / c\right) \right]} \\ & {\approx \cos \left[ \omega (t - r / c) \pm \frac {\omega d}{2 c} \cos \theta \right]} \\ & {= \cos [ \omega (t - r / c) ] \cos \left(\frac {\omega d}{2 c} \cos \theta\right) \mp \sin [ \omega (t - r / c) ] \sin \left(\frac {\omega d}{2 c} \cos \theta\right)} \end{array}
$$

对于理想偶极子极限，进一步有

$$
\text { 近似 } 2: d \ll \frac {c}{\omega}\tag{11.10}
$$

（因为具有频率为 $\omega$ 的波其波长是 $\lambda = 2\pi c / \omega$ ，这等同于要求 $d \ll \lambda$ 。）在这些条件下

$$
\cos \left[ \omega \left(t - r _ {\pm} / c\right) \right] \approx \cos [ \omega (t - r / c) ] \mp \frac {\omega d}{2 c} \cos \theta \sin [ \omega (t - r / c) ]\tag{11.11}
$$

把式 (11.9) 和式 (11.11) 代入式 (11.5)，得到振荡理想偶极子的势

$$
V (r, \theta , t) = \frac {p _ {0} \cos \theta}{4 \pi \varepsilon_ {0} r} \left\{- \frac {\omega}{c} \sin [ \omega (t - r / c) ] + \frac {1}{r} \cos [ \omega (t - r / c) ] \right\}\tag{11.12}
$$

在静态极限 $(\omega \rightarrow 0)$ 第二项再次给出了静止偶极子势的旧公式[式(3.102)]：

$$
V = \frac {p _ {0} \cos \theta}{4 \pi \varepsilon_ {0} r ^ {2}}
$$

然而，这项不是我们关注的；我们感兴趣的是远离源处，即所谓的辐射区（radiation zone） $^{6}$ 仍然存在的场：

$$
\text { 近似   3: } \quad r \gg \frac {c}{\omega}\tag{11.13}
$$

（或，用波长表示， $r \gg \lambda_{0}$ ）在这个区域势简化为

$$
\boxed {V (r, \theta , t) = - \frac {p _ {0} \omega}{4 \pi \varepsilon_ {0} c} \frac {\cos \theta}{r} \sin [ \omega (t - r / c) ]}\tag{11.14}
$$

同时，矢势由流过导线的电流确定：

$$
\boldsymbol {I} (t) = \frac {\mathrm{d} q}{\mathrm{d} t} \hat {\boldsymbol {z}} = - q _ {0} \omega \sin (\omega t) \hat {\boldsymbol {z}}\tag{11.15}
$$

参考图11.3，

$$
A (\boldsymbol {r}, t) = \frac {\mu_ {0}}{4 \pi} \int_ {- d / 2} ^ {d / 2} \frac {- q _ {0} \omega \sin [ \omega (t - r / c) ] \hat {\boldsymbol {z}}}{r} \mathrm{d} z\tag{11.16}
$$

![](images/d8c0e48268073c41465a5dc66b616837d9bf7c081fee1c77602daae0d8141589.jpg)  
图11.3

因为积分引进了一个因子 $d$ ，在一阶近似下，被积函数可用其中值替代：

$$
\boxed {A (r, \theta , t) = - \frac {\mu_ {0} p _ {0} \omega}{4 \pi r} \sin [ \omega (t - r / c) ] \hat {z}}\tag{11.17}
$$

[注意虽然只保留 $d$ 的一阶项暗含着利用了近似1和2，但式(11.17)没有用近似3。]

由势计算场是直截了当的。

$$
\begin{array}{r l} \nabla V & = \frac {\partial V}{\partial r} \hat {\boldsymbol {r}} + \frac {1}{r} \frac {\partial V}{\partial \theta} \hat {\boldsymbol {\theta}} \\ & = - \frac {p _ {0} \omega}{4 \pi \varepsilon_ {0} c} \left\{\cos \theta \left(- \frac {1}{r ^ {2}} \sin [ \omega (t - r / c) ] - \frac {\omega}{r c} \cos [ \omega (t - r / c) ]\right) \hat {\boldsymbol {r}} \right. \\ & \left. - \frac {\sin \theta}{r ^ {2}} \sin [ \omega (t - r / c) ] \hat {\boldsymbol {\theta}} \right\} \\ & \approx \frac {p _ {0} \omega^ {2}}{4 \pi \varepsilon_ {0} c ^ {2}} \frac {\cos \theta}{r} \cos [ \omega (t - r / c) ] \hat {\boldsymbol {r}} \end{array}
$$

（由近似3，第一和最后一项略去了。）同样可得

$$
\frac {\partial \boldsymbol {A}}{\partial t} = - \frac {\mu_ {0} p _ {0} \omega^ {2}}{4 \pi r} \cos \left[ \omega (t - r / c) \right] (\cos \theta \hat {\boldsymbol {r}} - \sin \theta \hat {\boldsymbol {\theta}})
$$

因而

$$
\boxed {\boldsymbol {E} = - \nabla V - \frac {\partial \boldsymbol {A}}{\partial t} = - \frac {\mu_ {0} p _ {0} \omega^ {2}}{4 \pi} \frac {\sin \theta}{r} \cos [ \omega (t - r / c) ] \hat {\boldsymbol {\theta}}}\tag{11.18}
$$

同时

$$
\begin{array}{r l} \nabla \times \mathbf {A} & = \frac {1}{r} \left[ \frac {\partial}{\partial r} (r A _ {\theta}) - \frac {\partial A _ {r}}{\partial \theta} \right] \hat {\phi} \\ & = - \frac {\mu_ {0} p _ {0} \omega}{4 \pi r} \left\{\frac {\omega}{c} \sin \theta \cos [ \omega (t - r / c) ] + \frac {\sin \theta}{r} \sin [ \omega (t - r / c) ] \right\} \hat {\phi} \end{array}
$$

花括弧中第二项由于近似3也略去了，故

$$
\boxed {\boldsymbol {B} = \nabla \times \boldsymbol {A} = - \frac {\mu_ {0} p _ {0} \omega^ {2}}{4 \pi c} \frac {\sin \theta}{r} \cos [ \omega (t - r / c) ] \hat {\phi}}\tag{11.19}
$$

式 (11.18) 和式 (11.19) 表示频率为 $\omega$ 的单色波沿径向以光速传播。 $E$ 和 $B$ 同相位，彼此垂直，为横场；振幅比为 $E_0 / B_0 = c$ 。所有这些性质都是我们对自由空间中电磁波预期的。（这些实际上是球面波，而非平面波，当它们向前传播时，振幅以 $1/r$ 的形式衰减。但当 $r$ 很大时，它们在小区域可近似为平面波——就像地球表面，在局部区域可近似认为是平的。）

一个振荡的电偶极子辐射的能量由坡印亭矢量确定：

$$
\pmb {S} (\pmb {r}, t) = \frac {1}{\mu_ {0}} (\pmb {E} \times \pmb {B}) = \frac {\mu_ {0}}{c} \left\{\frac {p _ {0} \omega^ {2}}{4 \pi} \frac {\sin \theta}{r} \cos [ \omega (t - r / c) ] \right\} ^ {2} \hat {\pmb {r}}\tag{11.20}
$$

强度由一个周期内（时间）平均得到：

$$
\langle S \rangle = \frac {\mu_ {0} p _ {0} ^ {2} \omega^ {4}}{3 2 \pi^ {2} c} \frac {\sin^ {2} \theta}{r ^ {2}} \hat {r}\tag{11.21}
$$

值得注意的是沿着偶极子轴的方向（即 $\theta = 0$ ）没有辐射。强度的分布如一个油炸圈饼的形状，它的最大值处于赤道面上（图11.4）。辐射的总功率由对 $\langle S\rangle$ 在半径为 $r$ 的球面上的积分得到：

$$
\langle P \rangle = \int \langle S \rangle \cdot \mathrm{d} a = \frac {\mu_ {0} p _ {0} ^ {2} \omega^ {4}}{3 2 \pi^ {2} c} \int \frac {\sin^ {2} \theta}{r ^ {2}} r ^ {2} \sin \theta \mathrm{d} \theta \mathrm{d} \phi = \frac {\mu_ {0} p _ {0} ^ {2} \omega^ {4}}{1 2 \pi c}\tag{11.22}
$$

![](images/0aac9559851d3a9b1300e87278f85f720bb238563711015e5ed59a67c8947c47.jpg)  
图11.4

例题11.1 能量公式中，能量对频率的强烈依赖正可以解释天空是蓝色的。太阳光通过大气层激发原子使之像极小的偶极子一样振动。入射太阳光的辐射覆盖一个宽的频率范围（白光），但被大气偶极子吸收和重新辐射的能量在高频处较强，因为在式(11.22)中有 $\omega^4$ 因子。这样蓝光就强于红光。你抬头仰望天空看到的正是二次辐射光——当然，除非你直接盯住太阳看。

因为电磁波是横波，偶极子在垂直于太阳光线的平面内振动。观察者沿垂直于太阳光线的方向观察天空 $^{8}$ 的视线区域内蓝色最为显著，其中沿着视线方向振动的偶极子不会有辐射向观察者传播[因为式(11.21)中的 $\sin^{2}\theta$ 因子]，故在这个角度 $^{9}$ 接收到的光为偏振的，其偏振方向垂直于太阳光线（图11.5）。

![](images/c6095c45ef721808cf89950c77706dde5fa44a2a6bee918273be4619d901bf2d.jpg)  
图11.5

日落时天空呈现红色是因为同样的原因：太阳光沿切线照射地球表面，光线比直射在大气层中经过更长的距离（图 11.6）。结果许多蓝色光由于散射消失了，留下的是红色光。

![](images/bb54454a82043e6028650865d9fd55198e9a79db5b427e080f56f8e0f9daec9f.jpg)  
图11.6

习题11.1 验证振动偶极子的推迟势[式(11.12)和式(11.17)]满足洛伦茨规范条件。不要用近似3。

习题11.2 利用 $p_0\cos \theta = p_0\cdot \hat{r}$ ，式(11.14)可写成不依赖坐标的形式。请这样做，并对式(11.17)、式(11.18)、式(11.19)和式(11.21)做同样处理。

习题11.3 求在偶极子中连接两端导线的辐射电阻（radiation resistance）。（这个电阻给出同样的平均功率损失——变为热能——如振动的偶极子实际上以辐射的形式释放出的功率。）证明 $R = 790(d / \lambda)^2\Omega$ ，式中 $\lambda$ 是辐射波长。对于在普通收音机中的导线（假定， $d = 5.0~\mathrm{cm}$ )，你担心辐射对总电阻中的

贡献吗？

!习题 11.4 一个转动的电偶极子可认为是两个振动的偶极子的叠加，如图 11.7 所示，一个沿 x 轴，一个沿 y 轴，后者与前者相位差 $90^{\circ}$ :

$$
\boldsymbol {p} = p _ {0} \left[ \cos (\omega t) \hat {\boldsymbol {x}} + \sin (\omega t) \hat {\boldsymbol {y}} \right]
$$

利用叠加原理及式(11.18)和式(11.19)(或许用习题11.2中给出的形式)，求出转动偶极子的场。求出坡印亭矢量和辐射强度。画出以极角 $\theta$ 为变量的强度函数分布图，并计算总的辐射功率。结果看起来是否合理？（注意功率是场的二次型，不满足叠加原理。在这个例子中，它似乎满足，你能给出解释吗？）

![](images/27b8d32acf7e4ab3f5b052267b79183019665ba7709f78dfd9008fd8dc4a02aa.jpg)  
图11.7

## 11.1.3 磁偶极子辐射

假设我们现在有一个导线构成的半径为 $b$ 的环（图11.8），通有一个交变电流

$$
I (t) = I _ {0} \cos (\omega t)\tag{11.23}
$$

这就是一个振动的磁偶极子模型，

$$
\boldsymbol {m} (t) = \pi b ^ {2} I (t) \hat {\boldsymbol {z}} = m _ {0} \cos (\omega t) \hat {\boldsymbol {z}}\tag{11.24}
$$

式中，

$$
m _ {0} \equiv \pi b ^ {2} I _ {0}\tag{11.25}
$$

是磁偶极矩的最大值。

![](images/e18df33277d151a22d6fa0b47da2ba328bf675e062b216e9d051c820aa3da734.jpg)  
图11.8

环不带电荷，故标势为零。推迟矢势是

$$
\boldsymbol {A} (\boldsymbol {r}, t) = \frac {\mu_ {0}}{4 \pi} \int \frac {I _ {0} \cos [ \omega (t - r / c) ]}{r} \mathrm{d} l ^ {\prime}\tag{11.26}
$$

对于一个在 $x$ 轴上方的点 $\pmb{r}$ （图11.8）， $\pmb{A}$ 必定指向 $y$ 方向，因为对称分布在 $x$ 轴两边的 $x$ 分量彼此抵消。于是

$$
\boldsymbol {A} (\boldsymbol {r}, t) = \frac {\mu_ {0} I _ {0} b}{4 \pi} \hat {\boldsymbol {y}} \int_ {0} ^ {2 \pi} \frac {\cos [ \omega (t - r / c) ]}{r} \cos \phi^ {\prime} d \phi^ {\prime}\tag{11.27}
$$

$(\cos\phi'$ 用来挑选出 $dl'$ 中的y分量)。由余弦定理，

$$
\nu = \sqrt {r ^ {2} + b ^ {2} - 2 r b \cos \psi}
$$

式中， $\psi$ 是矢量 r 和 b 间的夹角：

$$
\boldsymbol {r} = r \sin \theta \hat {\boldsymbol {x}} + r \cos \theta \hat {\boldsymbol {z}}, \quad \boldsymbol {b} = b \cos \phi^ {\prime} \hat {\boldsymbol {x}} + b \sin \phi^ {\prime} \hat {\boldsymbol {y}}
$$

于是 $rb\cos \psi = r\cdot b = rb\sin \theta \cos \phi^{\prime}$ ，所以

$$
\nu = \sqrt {r ^ {2} + b ^ {2} - 2 r b \sin \theta \cos \phi^ {\prime}}\tag{11.28}
$$

对于一个“理想”偶极子，希望环极小：

$$
\text { 近似 } 1: \quad b \ll r\tag{11.29}
$$

对于 $b$ 的一阶近似，有

$$
r \approx r \left(1 - \frac {b}{r} \sin \theta \cos \phi^ {\prime}\right)
$$

所以

$$
\frac {1}{r} \cong \frac {1}{r} \left(1 + \frac {b}{r} \sin \theta \cos \phi^ {\prime}\right)\tag{11.30}
$$

以及

$$
\begin{array}{l} \cos [ \omega (t - r / c) ] \\ \approx \cos \left[ \omega (t - r / c) + \frac {\omega b}{c} \sin \theta \cos \phi^ {\prime} \right] \\ = \cos [ \omega (t - r / c) ] \cos \left(\frac {\omega b}{c} \sin \theta \cos \phi^ {\prime}\right) - \sin [ \omega (t - r / c) ] \sin \left(\frac {\omega b}{c} \sin \theta \cos \phi^ {\prime}\right) \end{array}
$$

和以前一样，我们假设偶极子的尺度比辐射的波长小：

$$
\text { 近似 } 2 \colon b \ll \frac {c}{\omega}\tag{11.31}
$$

在这种情况下，

$$
\cos [ \omega (t - r / c) ] \approx \cos [ \omega (t - r / c) ] - \frac {\omega b}{c} \sin \theta \cos \phi^ {\prime} \sin [ \omega (t - r / c) ]\tag{11.32}
$$

把式 (11.30) 和式 (11.32) 代入式 (11.27)，略去二阶项：

$$
\begin{array}{l} \boldsymbol {A} (\boldsymbol {r}, t) \approx \frac {\mu_ {0} I _ {0} b}{4 \pi r} \hat {\boldsymbol {y}} \int_ {0} ^ {2 \pi} \left\{\cos [ \omega (t - r / c) ] + b \sin \theta \cos \phi^ {\prime} \right. \\ \left. \times \left(\frac {1}{r} \cos [ \omega (t - r / c) ] - \frac {\omega}{c} \sin [ \omega (t - r / c) ]\right) \right\} \cos \phi^ {\prime} d \phi^ {\prime} \end{array}
$$

上式中第一项积分为零：

$$
\int_ {0} ^ {2 \pi} \cos \phi^ {\prime} \mathrm{d} \phi^ {\prime} = 0
$$

第二项涉及余弦平方积分：

$$
\int_ {0} ^ {2 \pi} \cos^ {2} \phi^ {\prime} \mathrm{d} \phi^ {\prime} = \pi
$$

代入方程，注意到一般地 A 是指向 $\hat{\phi}$ -方向，可得振动的理想偶极子矢势为

$$
\pmb {A} (r, \theta , t) = \frac {\mu_ {0} m _ {0}}{4 \pi} \frac {\sin \theta}{r} \left\{\frac {1}{r} \cos [ \omega (t - r / c) ] - \frac {\omega}{c} \sin [ \omega (t - r / c) ] \right\} \hat {\phi}\tag{11.33}
$$

在静态极限下 $(\omega = 0)$ 我们回到熟悉的磁偶极子势的公式[式(5.87)]

$$
\mathbf {A} (r, \theta) = \frac {\mu_ {0}}{4 \pi} \frac {m _ {0} \sin \theta}{r ^ {2}} \hat {\phi}
$$

在辐射区域，

$$
\text { 近似   3: } \quad r \gg \frac {c}{\omega}\tag{11.34}
$$

A 中第一项可略去，故

$$
\boxed {A (r, \theta , t) = - \frac {\mu_ {0} m _ {0} \omega}{4 \pi c} \frac {\sin \theta}{r} \sin [ \omega (t - r / c) ] \hat {\phi}}\tag{11.35}
$$

由 $\pmb{A}$ 得到在大 $r$ 处的场为

$$
\boxed {\boldsymbol {E} = - \frac {\partial \boldsymbol {A}}{\partial t} = \frac {\mu_ {0} m _ {0} \omega^ {2}}{4 \pi c} \frac {\sin \theta}{r} \cos [ \omega (t - r / c) ] \hat {\phi}}\tag{11.36}
$$

以及

$$
\boxed {\boldsymbol {B} = \nabla \times \boldsymbol {A} = - \frac {\mu_ {0} m _ {0} \omega^ {2}}{4 \pi c ^ {2}} \frac {\sin \theta}{r} \cos [ \omega (t - r / c) ] \hat {\boldsymbol {\theta}}}\tag{11.37}
$$

（在计算 B 时利用了近似 3。）这些场同相位，彼此垂直，而且都垂直于传播方向 $(\hat{r})$ 。它们的振幅比是 $E_{0}/B_{0}=c$ ，所有这些都是对电磁波所预期的。事实上，它们与振动的电偶极矩的场 [式 (11.18) 和式 (11.19)] 在结构上极为相似。差异仅在于这里 B 指向 $\hat{\theta}$ 方向，E 指向 $\hat{\phi}$ 方向，而对于电偶极子则相反。

磁偶极辐射能量流是

$$
\pmb {S} (\pmb {r}, t) = \frac {1}{\mu_ {0}} (\pmb {E} \times \pmb {B}) = \frac {\mu_ {0}}{c} \left\{\frac {m _ {0} \omega^ {2}}{4 \pi c} \frac {\sin \theta}{r} \cos [ \omega (t - r / c) ] \right\} ^ {2} \hat {\pmb {r}}\tag{11.38}
$$

强度为

$$
\langle S \rangle = \frac {\mu_ {0} m _ {0} ^ {2} \omega^ {4}}{3 2 \pi^ {2} c ^ {3}} \frac {\sin^ {2} \theta}{r ^ {2}} \hat {r}\tag{11.39}
$$

总辐射功率是

$$
\langle P \rangle = \frac {\mu_ {0} m _ {0} ^ {2} \omega^ {4}}{1 2 \pi c ^ {3}}\tag{11.40}
$$

再一次，强度分布也具有油炸圈饼的形状（图 11.4），辐射强度也依赖于 $\omega^{4}$ 。但电偶极子与磁偶极子辐射有一个重要的不同：对尺度相当的偶极子，电偶极子辐射的能量远大于磁偶极子。比较式 (11.22) 和式 (11.40)，

$$
\frac {P _ {\mathrm{magnetic}}}{P _ {\mathrm{electric}}} = \left(\frac {m _ {0}}{p _ {0} c}\right) ^ {2}\tag{11.41}
$$

式中，（还记得） $m_{0}=\pi b^{2}I_{0}$ 和 $p_{0}=q_{0}d$ 在电偶极子中电流的大小是 $I_{0}=q_{0}\omega$ [式 (11.15)]。为了比较，设 $d=\pi b$ ，得

$$
\frac {P _ {\mathrm{magnetic}}}{P _ {\mathrm{electric}}} = \left(\frac {\omega b}{c}\right) ^ {2}\tag{11.42}
$$

但量 $\omega b / c$ 正如我们假设的是非常小的（近似2），这里它以平方出现。故通常可认为电偶极子辐射起主要作用。仅当系统被仔细设计从而排除电偶极辐射的贡献（如刚处理的情形）磁偶极辐射才能显现。

## 11.1.4 任意源的辐射

在前面部分我们研究了由两个特殊体系产生的辐射：振荡电偶极子和振荡磁偶极子。现在采用同样的步骤来求任意分布的电荷和电流的辐射，仅假设它们是局域在原点附近有限体积内（图 11.9）。推迟矢势是

$$
V (\boldsymbol {r}, t) = \frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\rho \left(\boldsymbol {r} ^ {\prime} , t - r / c\right)}{r} \mathrm{d} \tau^ {\prime}\tag{11.43}
$$

![](images/264c7452f074327fa2e6cacb20e397bcff95615fc821c320aa077aa895342cb2.jpg)  
图11.9

式中，

$$
\eta = \sqrt {r ^ {2} + r ^ {\prime 2} - 2 r \cdot r ^ {\prime}}\tag{11.44}
$$

和以前相同，假设场点 $r$ 与源的尺度相比很远：

$$
\text { 近似 } 1 \colon r ^ {\prime} \ll r\tag{11.45}
$$

（实际上， $r'$ 是积分变量。近似1的意思是 $r'$ 在源上变化时的最大值远小于 $r_{0}$ 。）根据这个假设，

$$
r \approx r \left(1 - \frac {\boldsymbol {r} \cdot \boldsymbol {r} ^ {\prime}}{r ^ {2}}\right)\tag{11.46}
$$

于是

$$
\frac {1}{r} \approx \frac {1}{r} \left(1 + \frac {\boldsymbol {r} \cdot \boldsymbol {r} ^ {\prime}}{r ^ {2}}\right)\tag{11.47}
$$

以及

$$
\rho \left(\boldsymbol {r} ^ {\prime}, t - r / c\right) \approx \rho \left(\boldsymbol {r} ^ {\prime}, t - \frac {r}{c} + \frac {\hat {\boldsymbol {r}} \cdot \boldsymbol {r} ^ {\prime}}{c}\right)
$$

以原点的推迟时间把 $\rho$ 展开为 $t$ 的泰勒级数，

$$
t _ {0} \equiv t - \frac {r}{c}\tag{11.48}
$$

我们有

$$
\rho \left(\boldsymbol {r} ^ {\prime}, t - r / c\right) \approx \rho \left(\boldsymbol {r} ^ {\prime}, t _ {0}\right) + \dot {\rho} \left(\boldsymbol {r} ^ {\prime}, t _ {0}\right) \left(\frac {\hat {\boldsymbol {r}} \cdot \boldsymbol {r} ^ {\prime}}{c}\right) + \dots\tag{11.49}
$$

式中的圆点表示对时间求导数。级数中后面的项应当是

$$
\frac {1}{2} \ddot {\rho} \left(\frac {\hat {\boldsymbol {r}} \cdot \boldsymbol {r} ^ {\prime}}{c}\right) ^ {2}, \quad \frac {1}{3 !} \dddot {\rho} \left(\frac {\hat {\boldsymbol {r}} \cdot \boldsymbol {r} ^ {\prime}}{c}\right) ^ {3}, \dots .
$$

我们可以略去它们，只要有

$$
\text {近似} 2 \colon \quad r ^ {\prime} \ll \frac {c}{| \ddot {\rho} / \dot {\rho} |}, \frac {c}{| \stackrel {. . .} {\rho} / \dot {\rho} | ^ {1 / 2}}, \frac {c}{| \stackrel {. . .} {\rho} / \dot {\rho} | ^ {1 / 3}}, \dots\tag{11.50}
$$

对于一个振荡的体系，上面的每一个的比值为 $c / \omega$ ，我们回到了过去的近似2。对于一般的情形，式(11.50)的解释更困难，但作为程序性事项近似1和2意味着我们只需考虑保留 $\pmb{r}'$ 的一阶近似。

把式(11.47)和式(11.49)代入求 $V$ 的公式[式(11.43)]，再略去二阶项：

$$
V (\boldsymbol {r}, t) \approx \frac {1}{4 \pi \varepsilon_ {0} r} \left[ \int \rho (\boldsymbol {r} ^ {\prime}, t _ {0}) \mathrm{d} \tau^ {\prime} + \frac {\hat {\boldsymbol {r}}}{r} \cdot \int \boldsymbol {r} ^ {\prime} \rho (\boldsymbol {r} ^ {\prime}, t _ {0}) \mathrm{d} \tau^ {\prime} + \frac {\hat {\boldsymbol {r}}}{c} \cdot \frac {\mathrm{d}}{\mathrm{d} t} \int \boldsymbol {r} ^ {\prime} \rho (\boldsymbol {r} ^ {\prime}, t _ {0}) \mathrm{d} \tau^ {\prime} \right]
$$

第一项积分只是在 $t_{0}$ 时刻的总电荷 Q。但因为电荷是守恒的，实际上 Q 不依赖于时间。另两个积分表示在 $t_{0}$ 时刻的电偶极矩。所以

$$
V (\boldsymbol {r}, t) \approx \frac {1}{4 \pi \varepsilon_ {0}} \left[ \frac {Q}{r} + \frac {\hat {\boldsymbol {r}} \cdot \boldsymbol {p} (t _ {0})}{r ^ {2}} + \frac {\hat {\boldsymbol {r}} \cdot \dot {\boldsymbol {p}} (t _ {0})}{r c} \right]\tag{11.51}
$$

在静态情形，前两项是 V 多极展开中的单极和偶极贡献，第三项当然将不出现。

同时，矢势是

$$
\boldsymbol {A} (\boldsymbol {r}, t) = \frac {\mu_ {0}}{4 \pi} \int \frac {\boldsymbol {J} \left(\boldsymbol {r} ^ {\prime} , t - r / c\right)}{r} \mathrm{d} \tau^ {\prime}\tag{11.52}
$$

很快会看到，对于 $r'$ 一阶近似，可在被积函数中用 r 替换 z 就够了：

$$
\pmb {A} (\pmb {r}, t) \approx \frac {\mu_ {0}}{4 \pi r} \int \pmb {J} (\pmb {r} ^ {\prime}, t _ {0}) \mathrm{d} \tau^ {\prime}\tag{11.53}
$$

根据习题5.7， $J$ 的积分是偶极矩对时间的导数，因而

$$
\mathbf {A} (\mathbf {r}, t) \approx \frac {\mu_ {0}}{4 \pi} \frac {\dot {\mathbf {p}} (t _ {0})}{r}\tag{11.54}
$$

现在你们明白为何没有必要把 $z$ 的近似取得高于零阶 $(z \approx r)$ : $p$ 已经是 $r'$ 的一阶近似了, 任何进一步的改进都是二阶（或者更高阶）修正。

下一步，我们必须计算场。我们再次对辐射区域感兴趣（也就是说，即远离源还存在的场），故仅保留那些行为按 $1 / r$ 变化的项：

(11.55)

例如，库仑场

$$
\pmb {E} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {Q}{r ^ {2}} \hat {\pmb {r}}
$$

来源于式 (11.51) 中的第一项，对电磁辐射没有贡献。事实上，辐射全部来源于对变量 $t_0$ 求导的项。从式 (11.48) 得

$$
\nabla t _ {0} = - \frac {1}{c} \nabla r = - \frac {1}{c} \hat {\boldsymbol {r}}
$$

所以

$$
\nabla V \approx \nabla \left[ \frac {1}{4 \pi \varepsilon_ {0}} \frac {\hat {\pmb {r}} \cdot \dot {\pmb {p}} (t _ {0})}{r c} \right] \approx \frac {1}{4 \pi \varepsilon_ {0}} \left[ \frac {\hat {\pmb {r}} \cdot \ddot {\pmb {p}} (t _ {0})}{r c} \right] \nabla t _ {0} = - \frac {1}{4 \pi \varepsilon_ {0} c ^ {2}} \frac {[ \hat {\pmb {r}} \cdot \ddot {\pmb {p}} (t _ {0}) ]}{r} \hat {\pmb {r}}
$$

类似地，

$$
\nabla \times \mathbf {A} \approx \frac {\mu_ {0}}{4 \pi r} [ \nabla \times \dot {\pmb {p}} (t _ {0}) ] = \frac {\mu_ {0}}{4 \pi r} [ (\nabla t _ {0}) \times \ddot {\pmb {p}} (t _ {0}) ] = - \frac {\mu_ {0}}{4 \pi r c} [ \hat {\pmb {r}} \times \ddot {\pmb {p}} (t _ {0}) ]
$$

而

$$
\frac {\partial \boldsymbol {A}}{\partial t} \approx \frac {\mu_ {0}}{4 \pi} \frac {\ddot {\boldsymbol {p}} (t _ {0})}{r}
$$

于是

$$
\boxed {E (\boldsymbol {r}, t) \approx \frac {\mu_ {0}}{4 \pi r} [ (\hat {\boldsymbol {r}} \cdot \ddot {\boldsymbol {p}}) \hat {\boldsymbol {r}} - \ddot {\boldsymbol {p}} ] = \frac {\mu_ {0}}{4 \pi r} [ \hat {\boldsymbol {r}} \times (\hat {\boldsymbol {r}} \times \ddot {\boldsymbol {p}}) ]}\tag{11.56}
$$

式中， $\ddot{p}$ 是在时间 $t_0 = t - r / c$ 时的值，而

$$
\boxed {B (\boldsymbol {r}, t) \approx - \frac {\mu_ {0}}{4 \pi r c} [ \hat {\boldsymbol {r}} \times \ddot {\boldsymbol {p}} ]}\tag{11.57}
$$

特别地，如果我们采用球坐标，令 z 轴指向 $\ddot{\boldsymbol{p}}(t_{0})$ 方向，有

$$
\left. \begin{array}{l} \boldsymbol {E} (r, \theta , t) \approx \frac {\mu_ {0} \ddot {p} (t _ {0})}{4 \pi} \frac {\sin \theta}{r} \hat {\boldsymbol {\theta}} \\ \boldsymbol {B} (r, \theta , t) \approx \frac {\mu_ {0} \ddot {p} (t _ {0})}{4 \pi c} \frac {\sin \theta}{r} \hat {\boldsymbol {\phi}} \end{array} \right\}\tag{11.58}
$$

坡印亭矢量是

$$
\boldsymbol {S} (\boldsymbol {r}, t) \approx \frac {1}{\mu_ {0}} (\boldsymbol {E} \times \boldsymbol {B}) = \frac {\mu_ {0}}{1 6 \pi^ {2} c} \left[ \ddot {p} (t _ {0}) \right] ^ {2} \frac {\sin^ {2} \theta}{r ^ {2}} \hat {\boldsymbol {r}}\tag{11.59}
$$

通过半径为 $r$ 的巨大球面的功率为

$$
P (r, t) = \oint \boldsymbol {S} (\boldsymbol {r}, t) \cdot \mathrm{d} \boldsymbol {a} = \frac {\mu_ {0}}{6 \pi c} \left[ \ddot {p} \left(t - \frac {r}{c}\right) \right] ^ {2}
$$

而总的辐射功率 [式 (11.2)] 是

$$
P _ {\text {辐射}} \left(t _ {0}\right) \approx \frac {\mu_ {0}}{6 \pi c} \left[ \ddot {p} \left(t _ {0}\right) \right] ^ {2}\tag{11.60}
$$

注意 $\pmb{E}$ 和 $\pmb{B}$ 互相垂直，而且垂直于传播方向 $(\hat{\pmb{r}})$ ， $E / B = c$ ，正如辐射场一贯的关系。

例题11.2 (a) 对于振荡电偶极子，

$$
p (t) = p _ {0} \cos (\omega t), \quad \ddot {p} (t) = - \omega^ {2} p _ {0} \cos (\omega t)
$$

回到 11.1.2 节的结果。

(b) 对于单个点电荷 q，偶极矩是

$$
\boldsymbol {p} (t) = q \boldsymbol {d} (t)
$$

式中， $d$ 是 $q$ 相对于原点的位置。由此

$$
\ddot {p} (t) = q a (t)
$$

式中，a 是电荷的加速度。这种情形下辐射的功率 [式 (11.60)] 是

$$
P = \frac {\mu_ {0} q ^ {2} a ^ {2}}{6 \pi c}\tag{11.61}
$$

这就是著名的拉莫尔公式（Larmor formula）。在下一节，将用另一种非常不同的方法再次推导它。注意，点电荷辐射的功率正比于加速度的平方。

在本节我们对推迟势进行了多极展开，取能够产生电磁辐射（场以 $1 / r$ 衰减）的 $r'$ 的最低阶。这是电偶极项。因为电荷守恒，电单极不辐射——如果电荷不守恒，式(11.51)中的第一项为

$$
V _ {\mathrm{单}} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {Q (t _ {0})}{r}
$$

得到正比于 $1 / r$ 的电单极场：

$$
E _ {\mathrm{单}} = \frac {1}{4 \pi \varepsilon_ {0} c} \frac {\dot {Q} (t _ {0})}{r} \hat {r}
$$

你也许认为一个半径振荡变化的带电球会辐射，但它不会辐射——根据高斯定理，不论球的大小是否变化，球外的场严格为 $\left(Q / 4\pi \varepsilon_0r^2\right)\hat{r}$ 。（顺便提及，类比声学，单极确能辐射：牛蛙的哇哇叫就是个例证。）

如果电偶极矩是零（或，不管怎样，它对时间的二阶导数为零）则没有电偶极辐射，必须看下一项： $r'$ 的二阶项。碰巧的是，此项对辐射的贡献可分为两部分，一部分与源的磁偶极矩相联系，另一部分是电四极矩。（前一项是我们在11.1.3节讨论的磁偶极辐射的一个推广。）如果磁偶极矩和电四极矩贡献仍然为零，就必须考虑 $r'^{3}$ 的项。这会产生磁四极矩和电八极矩辐射，以此类推。

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
习题11.8 板间距为 $d$ 的平行板电容器 $C$ 初始带电量为 $(\pm)Q_0$ 。然后将其连接到电阻 $R$ 并放电，$Q(t) = Q_0\mathrm{e}^{-t / RC}$ 。(a）它最初能量 $\left(Q_0^2 / 2C\right)$ 的多大比例辐射出去？(b）如果 $C = 1\mathrm{pF}$，$R = 1000\Omega$，以及 $d = 0.1\mathrm{mm}$，这一实际数字是多少？在电子学中，我们通常不担心辐射损失；在这种情况下，这看上去合理吗？习题11.9 把式(11.59)和式(11.60)应用于习题11.4中的转动偶极子。解释与之前答案相比的任何明显差异。
</div>

习题11.10 一个绝缘的圆形环（半径为 $b$ ）位于 $xy$ 平面，中心在原点。它带有线电荷密度 $\lambda = \lambda_0\sin \phi$ ，式中 $\lambda_0$ 是常数， $\phi$ 是通常的方位角。现在线圈以角速度 $\omega$ 绕 $z$ 轴旋转。计算辐射功率。

!习题11.11 一电流 $I(t)$ 流过如图11.8的圆形线圈。推导辐射功率的一般表达式[类似式(11.60)],用线圈的磁偶极矩 $m(t)$ 或者其时间导数表示你的结果。[答案： $P = \mu_0\dot{m}^2 /6\pi c^3]$

## 11.2 点电荷的辐射

## 11.2.1 点电荷的辐射功率

在第10章中我们推导出了任意运动的点电荷 $q$ 的场[式(10.72)和式(10.73)]：

$$
\boldsymbol {E} (\boldsymbol {r}, t) = \frac {q}{4 \pi \varepsilon_ {0}} \frac {\mathbf {r}}{(\boldsymbol {z} \cdot \boldsymbol {u}) ^ {3}} \left[ \left(c ^ {2} - v ^ {2}\right) \boldsymbol {u} + \boldsymbol {z} \times (\boldsymbol {u} \times \boldsymbol {a}) \right]\tag{11.62}
$$

式中， $u = c\hat{\mathbf{z}} -\mathbf{v}$ ，以及

$$
\boldsymbol {B} (\boldsymbol {r}, t) = \frac {1}{c} \hat {\boldsymbol {z}} \times \boldsymbol {E} (\boldsymbol {r}, t)\tag{11.63}
$$

式 (11.62) 的第一项称为速度场（velocity field），第二项（两重矢量积）称为加速场（acceleration field）。

坡印亭矢量是

$$
\boldsymbol {S} = \frac {1}{\mu_ {0}} (\boldsymbol {E} \times \boldsymbol {B}) = \frac {1}{\mu_ {0} c} [ \boldsymbol {E} \times (\hat {\boldsymbol {\mathbf {z}}} \times \boldsymbol {E}) ] = \frac {1}{\mu_ {0} c} \left[ E ^ {2} \hat {\boldsymbol {\mathbf {z}}} - (\hat {\boldsymbol {\mathbf {z}}} \cdot \boldsymbol {E}) \boldsymbol {E} \right]\tag{11.64}
$$

但是，不是能量流中所有的项都构成辐射，它们中的一些仅是粒子运动时携带的场能量。其实，辐射能是脱离电荷向无穷远处传播的能量。（就像滋生在垃圾车上的苍蝇，其中的一些随着车兜圈在车附近飞舞，而另一些飞走不再回来。）为了计算粒子在时间 $t_r$ 时的总的辐射功率，我们画一个半径为 $z$ 的巨大的球面（图11.10），球心在粒子处（在 $t_r$ 时刻），等待适当的时间间隔

$$
t - t _ {r} = \frac {\eta}{c}\tag{11.65}
$$

后，辐射到达球面，此时对球面上的坡印亭矢量积分 $^{10}$ 。我用了符号 $t_{r}$ 因为事实上这是在 t 时刻球面上所有点的推迟时间。

![](images/7ca1cc2ad2c426b84d4eec5153f2be61d5059b8a6c396afea897e1c89f02d845.jpg)  
图11.10

由于球面的面积正比于 $v^{2}$ ，所以在 $v \to \infty$ 时，S 中任何包含 $1/v^{2}$ 的项积分给出有限的结果，但包含 $1/v^{3}$ 和 $1/v^{4}$ 的项将趋于零。由于这个原因，仅加速场代表真实的辐射 [所以它们的另一个名字是辐射场（radiation field）]：

$$
E _ {\text {辐射}} = \frac {q}{4 \pi \varepsilon_ {0}} \frac {\imath}{(\pmb {z} \cdot \pmb {u}) ^ {3}} [ \pmb {z} \times (\pmb {u} \times \pmb {a}) ]\tag{11.66}
$$

速度场确实携带能量，当电荷移动时这个能量跟随着一起移动——但它不是辐射。（就像苍蝇跟随着垃圾车。）现在 $E_{辐射}$ 垂直于 $\hat{z}$ ，所以式 (11.64) 中的第二项为零：

$$
S _ {\mathrm{辐射}} = \frac {1}{\mu_ {0} c} E _ {\mathrm{辐射}} ^ {2} \hat {\mathbf {z}}\tag{11.67}
$$

如果电荷瞬时静止（在时刻 $t_r$ ），则 $\pmb{u} = c\hat{\pmb{z}}$ ，并有

$$
\pmb {E} _ {\text {辐射}} = \frac {q}{4 \pi \varepsilon_ {0} c ^ {2} r} [ \hat {\pmb {\mathscr {r}}} \times (\hat {\pmb {\mathscr {r}}} \times \pmb {a}) ] = \frac {\mu_ {0} q}{4 \pi r} [ (\hat {\pmb {\mathscr {r}}} \cdot \pmb {a}) \hat {\pmb {\mathscr {r}}} - \pmb {a} ]\tag{11.68}
$$

在这种情况

$$
S _ {\mathrm{辐射}} = \frac {1}{\mu_ {0} c} \left(\frac {\mu_ {0} q}{4 \pi r}\right) ^ {2} \left[ a ^ {2} - (\hat {\mathbf {r}} \cdot \mathbf {a}) ^ {2} \right] \hat {\mathbf {r}} = \frac {\mu_ {0} q ^ {2} a ^ {2}}{1 6 \pi^ {2} c} \frac {\sin^ {2} \theta}{r ^ {2}} \hat {\mathbf {r}}\tag{11.69}
$$

式中， $\theta$ 是 $\hat{z}$ 和 $a$ 之间的夹角。在前方和后方没有能量辐射——而是以一个沿着瞬时加速的方向油炸圈饼的形状向外辐射（图11.11）。

![](images/c97a96210931eaa51ef4353efca04c0dcfd4f58ce018b169aa530b86c8a0002c.jpg)  
图11.11

显然，总的辐射功率是

$$
P = \oint \boldsymbol {S} _ {\text {辐射}} \cdot \mathrm{d} \boldsymbol {a} = \frac {\mu_ {0} q ^ {2} a ^ {2}}{1 6 \pi^ {2} c} \int \frac {\sin^ {2} \theta}{\nu^ {2}} \nu^ {2} \sin \theta \mathrm{d} \theta \mathrm{d} \phi
$$

或者

$$
\boxed {P = \frac {\mu_ {0} q ^ {2} a ^ {2}}{6 \pi c}}\tag{11.70}
$$

这还是拉莫尔公式（Larmor formula），较早前我们用另一种方法得到过[式(11.61)]。

尽管推导时假设 v=0，实际上式 (11.69) 和式 (11.70) 对 $v \ll c$ 的情形也是很好的近似。对 $v \neq 0$ 情形的精确处理比较困难 $^{11}$ ，一个明显的原因是 $E_{辐射}$ 更为复杂，另一个更微妙的原因是单位时间穿过球面的能量，并不等于单位时间粒子发射的能量。假设从移动汽车的窗户中射出一束子弹（图 11.12），由于汽车的运动，单位时间击中固定目标的子弹数 $N_{t}$ 与手枪单位时间发射的子弹数 $N_{g}$ 是不同的。事实上，若假定汽车向靶运动，你可以很容易算出 $N_{g} = (1 - v/c)N_{t}$ ，对汽车以任意方向运动则有

$$
N _ {g} = \left(1 - \frac {\hat {\textbf {\textit {r}}} \cdot \textbf {v}}{c}\right) N _ {t}
$$

式中，v 是车的速度；c 是子弹相对于地面的速； $\hat{z}$ 是从车到靶的单位矢量。对于我们的情形，如果 dW/dt 是单位时间穿过半径为 z 的球面的能量，则单位时间离开电荷的能量为

$$
\frac {\mathrm{d} W}{\mathrm{d} t _ {r}} = \frac {\mathrm{d} W / \mathrm{d} t}{\partial t _ {r} / \partial t} = \frac {2 \cdot \boldsymbol {u}}{2 c} \frac {\mathrm{d} W}{\mathrm{d} t}\tag{11.71}
$$

[我用了式 (10.78) 表示 $\partial t_r / \partial t$ 。] 但

$$
\frac {r \cdot u}{r c} = 1 - \frac {\hat {z} \cdot v}{c}
$$

这是精确的 $N_{g}$ 对 $N_{t}$ 的比率，它纯粹是一个几何因子（与多普勒效应相同）。

![](images/bbe70a46d9077b1da5eca90ff11ac36e66c98e26698f133e8fc7e3b9c6590c0b.jpg)  
图11.12

所以，粒子在球面上穿过一块区域 $\nu^{2}\sin\theta d\theta d\phi=\nu^{2}d\Omega$ 的辐射功率为

$$
\frac {\mathrm{d} P}{\mathrm{d} \varOmega} = \frac {\hat {\textbf {z}} \cdot \textbf {u}}{\varkappa c} \frac {1}{\mu_ {0} c} E _ {\text {辐射}} ^ {2} v ^ {2} = \frac {q ^ {2}}{1 6 \pi^ {2} \varepsilon_ {0}} \frac {| \hat {\textbf {z}} \times (\textbf {u} \times \textbf {a}) | ^ {2}}{(\hat {\textbf {z}} \cdot \textbf {u}) ^ {5}}\tag{11.72}
$$

式中， $\mathrm{d}\Omega = \sin \theta \mathrm{d}\theta \mathrm{d}\phi$ 是辐射能量通过的立体角（solid angle）。对角度 $\theta$ 和 $\phi$ 积分不是件轻松的事，这里仅给出结果

$$
P = \frac {\mu_ {0} q ^ {2} \gamma^ {6}}{6 \pi c} \left(a ^ {2} - \left| \frac {\boldsymbol {v} \times \boldsymbol {a}}{c} \right| ^ {2}\right)\tag{11.73}
$$

式中， $\gamma \equiv 1 / \sqrt{1 - v^2 / c^2}$ ，这是拉莫尔公式的李纳推广（Liénard's generalization），在低速时它化为拉莫尔公式。因子 $\gamma^6$ 意味着当粒子的速度接近光速时辐射能会剧烈增大。

例题11.3 设 $\pmb{v}$ 和 $\pmb{a}$ 的方向瞬时共线（ $t_r$ 时刻），如直线运动。求辐射的角分布[式(11.72)]和总的辐射能。

[解答] 在这种情况下 $u \times a = c(\hat{z} \times a)$ ，于是

$$
\frac {\mathrm{d} P}{\mathrm{d} \varOmega} = \frac {q ^ {2} c ^ {2}}{1 6 \pi^ {2} \varepsilon_ {0}} \frac {| \hat {\textbf {z}} \times (\hat {\textbf {z}} \times \textbf {a}) | ^ {2}}{(c - \hat {\textbf {z}} \cdot \textbf {v}) ^ {5}}
$$

现在

$$
\hat {\pmb {z}} \times (\hat {\pmb {z}} \times \pmb {a}) = (\hat {\pmb {z}} \cdot \pmb {a}) \hat {\pmb {z}} - \pmb {a}, \quad \text {于是} | \hat {\pmb {z}} \times (\hat {\pmb {z}} \times \pmb {a}) | ^ {2} = a ^ {2} - (\hat {\pmb {z}} \cdot \pmb {a}) ^ {2}
$$

特别地，如果让 $\pmb{v}$ 沿 $z$ 轴方向，有

$$
\frac {\mathrm{d} P}{\mathrm{d} \Omega} = \frac {\mu_ {0} q ^ {2} a ^ {2}}{1 6 \pi^ {2} c} \frac {\sin^ {2} \theta}{(1 - \beta \cos \theta) ^ {5}}\tag{11.74}
$$

式中， $\beta \equiv v / c$ 。当然在 $v = 0$ 的情况下，这与式 (11.69) 一致。但对于很大的 $v(\beta \approx 1)$ 辐射圈饼（图 11.11）以因子 $(1 - \beta \cos \theta)^{-5}$ 向外拉伸并向前推，如图 11.13 所示。尽管在正前方依然没有辐射，但大部分辐射集中在一个围绕前进方向的益趋狭窄的锥体内（参看习题 11.15）。

![](images/0a5021bc54fdb71f0b6c12db29179977ad318526baf2ee2882dee419480f585a.jpg)  
图11.13

通过对式 $(11.74)$ 做全立体角积分，即得总辐射功率

$$
P = \int {\frac {\mathrm{d} P}{\mathrm{d} \Omega}} \mathrm{d} \Omega = \frac {\mu_ {0} q ^ {2} a ^ {2}}{1 6 \pi^ {2} c} \int {\frac {\sin^ {2} \theta}{(1 - \beta \cos \theta) ^ {5}}} \sin \theta \mathrm{d} \theta \mathrm{d} \phi .
$$

$\phi$ 的积分为 $2\pi$ ，通过变量代换 $x \equiv \cos \theta$ ，对 $\theta$ 的积分可化简为

$$
P = \frac {\mu_ {0} q ^ {2} a ^ {2}}{8 \pi c} \int_ {- 1} ^ {+ 1} \frac {1 - x ^ {2}}{(1 - \beta x) ^ {5}} \mathrm{d} x
$$

由分部积分得上式中积分为 $\frac{4}{3} (1 - \beta^2)^{-3}$ ，我就得到了

$$
P = \frac {\mu_ {0} q ^ {2} a ^ {2} \gamma^ {6}}{6 \pi c}\tag{11.75}
$$

这个结果对 $v$ 和 $a$ 共线的情形与 Liénard 公式 [式 (11.73)] 一致。注意辐射的角分布不论粒子是加速还是减速都是一样的；它仅依赖于 $a$ 的平方，且在任意一种情况都集中在前进方向（速度的方向）。当一个高速电子碰撞金属靶时，它速度迅速降低，发出所谓的韧致辐射（bremsstrahlung），或“刹车辐射”。在这个例子中描述的实际上就是韧致辐射的经典理论。

辐射掉了？

习题11.13 一个正电荷 $q$ 以初始速率 $v_{0}$ 迎面射向远处的正电荷 $Q$ （后者保持静止）。它靠近，减速到 $v = 0$ ，然后返回并运动到无穷远处。 $q$ 的初始能量 $\left(\frac{1}{2} mv_0^2\right)$ 中有多少被辐射掉了？假设 $v_{0} \ll c$ 并且可以放心地忽略辐射损失对粒子运动的影响。[答案：(16/45)(q/Q)(v0/c)^3]

习题11.14 在氢原子的玻尔理论中，假设处于基态的电子在做半径为 $5 \times 10^{-11} \mathrm{~m}$ 的圆周运动，它被质子通过库仑作用束缚在轨道上。根据经典电动力学，电子会辐射，因而会沿螺旋线运动进入到原子核。证明在大多数情形下 $v \ll c$ （故可用拉莫尔公式），并计算玻尔原子的寿命。（假设运动一周的轨道基本是圆。）

习题11.15 求在例题11.3中最大辐射方向的方向角 $\theta_{\mathrm{max}}$ （参看图11.13）。证明对极端相对论速度（ $v$ 接近于光速 $c$ ）， $\theta_{\mathrm{max}} \approx \sqrt{(1 - \beta)} / 2$ 。与粒子瞬间静止情形的相同量相比较，这个辐射最大方向的辐射强度是多少（对极端相对论情形）？以 $\gamma$ 表示你的结果。

!习题 11.16 在例题 11.3 中我们假设速度和加速度（至少瞬时）共线。对于它们垂直的情形做同样的分析。适当选择坐标系使 v 沿着 z 轴方向，a 沿着 x 轴（图 11.14），这样 $v = v \hat{z}$ ， $a = a \hat{x}$ ，而 $\hat{z} = \sin \theta \cos \phi \hat{x} + \sin \theta \sin \phi \hat{y} + \cos \theta \hat{z}$ 。验证 P 与李纳公式一致。[答案：

$$
\frac {\mathrm{d} P}{\mathrm{d} \varOmega} = \frac {\mu_ {0} q ^ {2} a ^ {2}}{1 6 \pi^ {2} c} \frac {\left[ (1 - \beta \cos \theta) ^ {2} - (1 - \beta^ {2}) \sin^ {2} \theta \cos^ {2} \phi \right]}{(1 - \beta \cos \theta) ^ {5}}, \quad P = \frac {\mu_ {0} q ^ {2} a ^ {2} \gamma^ {4}}{6 \pi c}
$$

![](images/0c4c8a9496a131b194ea0989c7ac36c3d53d777749333087565e565357535f56.jpg)  
图11.14

对相对论速度（ $\beta \approx 1$ ）辐射仍然在前进方向有尖锐的峰（图11.15）。这些公式最重要的应用是对圆周运动——在这种情形下辐射称为同步辐射（synchrotron radiation）。对于一个相对论电子，辐射像火车头的前灯随着它的运动扫过周围。]

![](images/9126964e226c9a1bd936a3d1a348b0f1fc2162daf3c0bf75c151fed3ad090b10.jpg)  
图11.15

## 11.2.2 辐射反作用

加速的电荷要辐射。这种辐射携带能量，这种能量必须消耗粒子的动能。所以在给定力的情况下，带电粒子的加速度要小于有同样质量的中性粒子的加速度。显然辐射反过来对电荷施加了一个力（ $F_{辐射}$ ）——一个反冲力，如同子弹对枪的后坐力。在本节我们将从能量守恒出发推导出辐射反作用力（radiation reaction）。在下节将描述实际的机制，并从一个简单模型再次推导出反作用力。

对非相对论粒子 $(v\ll c)$ ，辐射的总功率由拉莫尔公式[式(11.70)]给出：

$$
P = \frac {\mu_ {0} q ^ {2} a ^ {2}}{6 \pi c}\tag{11.76}
$$

根据能量守恒，这“暗示”也正是粒子由于辐射反作用力 $F_{\text{辐射}}$ 作用而损失的功率：

$$
\pmb {F} _ {\text {辐射}} \cdot \pmb {v} = - \frac {\mu_ {0} q ^ {2} a ^ {2}}{6 \pi c}\tag{11.77}
$$

我特意说“暗示”因为这个方程事实上是错误的。因为我们是通过在一个半径为“无限大”的球面上对坡印亭矢量积分来计算辐射功率的，在这个计算中速度场不起作用，因为作为 $r$ 的函数它们衰减得太快，所以没有任何贡献。但速度场的确携带了能量——它们仅是没有把它传输至无穷远而已。当粒子加速和减速时粒子和速度场之间有能量交换，同时能量以不可逆的形式通过加速场辐射出去。式(11.77)仅计入后者，但如果我们想知道由场施加在电荷上的反作用力，就需要考虑在任何时刻损失的总功率，而不只是最终失去的那部分辐射能。（术语“辐射反作用”是不当的，我们实际上应当称它为场反作用。事实上，不久我们就会看到 $F_{辐射}$ 可通过对加速度的时间导数求出，它甚至在瞬时加速度本身为零从而粒子不辐射时依然不为零。）

粒子在任何给定时间间隔的能量损失必须等于辐射携带的能量加上转移给速度场的能量 $^{12}$ 。但是如果我们考虑的只是系统回到初始状态的时间间隔，那么速度场的能量在两端相同，净损失的能量只是辐射能。故式(11.77)在瞬时是不正确的，在以下情形是合理的：即取平均

$$
\int_ {t _ {1}} ^ {t _ {2}} \pmb {F} _ {\text {辐射}} \cdot \pmb {v} \mathrm{d} t = - \frac {\mu_ {0} q ^ {2}}{6 \pi c} \int_ {t _ {1}} ^ {t _ {2}} a ^ {2} \mathrm{d} t\tag{11.78}
$$

并且限定系统的状态在 $t_1$ 和 $t_2$ 时是相同的。例如，对于周期性运动我们必须对一个周期积分 $^{13}$ 。现在式 (11.78) 的右边可以通过分部积分求出：

$$
\int_ {t _ {1}} ^ {t _ {2}} a ^ {2} \mathrm{d} t = \int_ {t _ {1}} ^ {t _ {2}} \left(\frac {\mathrm{d} \boldsymbol {v}}{\mathrm{d} t}\right) \cdot \left(\frac {\mathrm{d} \boldsymbol {v}}{\mathrm{d} t}\right) \mathrm{d} t = \left. (\boldsymbol {v} \cdot \frac {\mathrm{d} \boldsymbol {v}}{\mathrm{d} t}) \right| _ {t _ {1}} ^ {t _ {2}} - \int_ {t _ {1}} ^ {t _ {2}} \frac {\mathrm{d} ^ {2} \boldsymbol {v}}{\mathrm{d} t ^ {2}} \cdot \boldsymbol {v} \mathrm{d} t
$$

边界项为零，因为在 $t_1$ 和 $t_2$ 时刻的速度和加速度相同。故式(11.78)可等价写成

$$
\int_ {t _ {1}} ^ {t _ {2}} \left(\pmb {F} _ {\text {辐射}} - \frac {\mu_ {0} q ^ {2}}{6 \pi c} \dot {\pmb {a}}\right) \cdot \pmb {v} \mathrm{d} t = 0\tag{11.79}
$$

如果

$$
\boxed {F _ {\mathrm{辐射}} = \frac {\mu_ {0} q ^ {2}}{6 \pi c} \dot {a}}\tag{11.80}
$$

式 (11.79) 将必定满足。这就是辐射反作用力的亚伯拉罕-洛伦兹公式（Abraham-Lorentz formula）。

当然式 (11.79) 不能证明式 (11.80)。关于 $F_{\text{辐射}}$ 垂直于 $\pmb{v}$ 的分量，它得不出任何结论，它仅告诉你平行分量的时间平均——在一个特别的时间间隔内的平均。在下节我们将看到有其他的原因相信亚伯拉罕-洛伦兹公式，但是现在能说的最好的表述是，它是辐射反作用力能取的最简单的形式，并与能量守恒一致。

亚伯拉罕-洛伦兹公式具有令人困扰的含义，在它首次被提出一个世纪以来还没有被完全理解。因为假设一个粒子没有受到外力，根据牛顿第二定律

$$
F _ {\mathrm{辐射}} = \frac {\mu_ {0} q ^ {2}}{6 \pi c} \dot {a} = m a
$$

由此得

$$
a (t) = a _ {0} \mathrm{e} ^ {t / \tau}\tag{11.81}
$$

式中，

$$
\tau \equiv \frac {\mu_ {0} q ^ {2}}{6 \pi m c}\tag{11.82}
$$

（对于电子的情形， $\tau = 6.26 \times 10^{-24} \mathrm{~s}$ 。）加速度自发地随着时间指数增加！如果令 $a_0 = 0$ 可以避免这个荒谬的结论，但这种对奔离解（runaway solutions）系统性的排除会引起更糟糕的结果：如果你的确施加了一个外力，粒子在力施加前就开始响应！（参看习题11.19）。这个无原因的预加速（acausal preacceleration）仅抢跑一个短暂的时间 $\tau$ ；尽管如此，该理论完全接纳这一点（在我看来）是不可接受的 $^{14}$ 。

例题11.4 计算连接着一个弹簧的带电粒子的辐射阻尼（radiation damping）。弹簧的本征频率为 $\omega_0$ ，受迫频率为 $\omega$ 。[解答] 运动方程是

$$
m \ddot {x} = F _ {\mathrm{弹簧}} + F _ {\mathrm{辐射}} + F _ {\mathrm{强迫}} = - m \omega_ {0} ^ {2} x + m \tau \dddot {x} + F _ {\mathrm{强迫}}
$$

系统振动频率为 $\omega$

$$
x (t) = x _ {0} \cos (\omega t + \delta)
$$

因而

$$
\ddot {x} = - \omega^ {2} \dot {x}
$$

所以

$$
m \ddot {x} + m \gamma \dot {x} + m \omega_ {0} ^ {2} x = F _ {\mathrm{强迫}}\tag{11.83}
$$

阻尼系数如下给出：

$$
\gamma = \omega^ {2} \tau\tag{11.84}
$$

[回到第9章式(9.152)，当我写下 $F_{\text{辐射}} = -\gamma mv$ 时，为了简单起见我假设了阻尼正比于速度。现在我们知道辐射阻尼，至少正比于 $\ddot{v}$ 。但这几乎没有影响：对正弦振动，对速度 $v$ 任何偶数次导数均可，因为它们都正比于 $v$ 。]

习题11.17

(a) 带电 $q$ 的粒子以恒定速率 $v$ 沿半径为 $R$ 的圆周做匀速圆周运动。为了保持这个运动当然需要提供一个向心力 $mv^2 / R$ 。为了抵消辐射反作用力，必须施加的附加的力 $(F_e)$ 是多少？[用瞬时速度 $v$ 表示结果最简单。]这个附加力提供的功率（ $P_e$ ）是多少？比较 $P_e$ 和辐射功率（利用拉莫尔公式）。

(b) 对振幅为 $A$ 以圆频率为 $\omega$ 做简谐振动的粒子 $[w(t) = A\cos (\omega t)\hat{z}]$ ，重复（a）计算，解释它们的差异。

(c) 考虑一个带电粒子自由下落的情况（加速度为常数 $g$ ）。辐射反作用力是多少？辐射的功率是多少？评述这些结果。

习题11.18 质量为 $m$ 的点电荷 $q$ 附着在劲度系数为 $k$ 的弹簧上。它在 $t = 0$ 时刻受到冲击，因此其初始能量为 $U_{0} = \frac{1}{2} mv_{0}^{2}$ 。现在它振荡，逐渐辐射掉这一能量。

(a) 证明辐射的总能量等于 $U_{0}$ 。假设辐射阻尼很小，所以你可以把运动方程写成

$$
\ddot {x} + \gamma \dot {x} + \omega_ {0} ^ {2} x = 0
$$

其解表示为

$$
x (t) = \frac {v _ {0}}{\omega_ {0}} \mathrm{e} ^ {- \gamma t / 2} \sin (\omega_ {0} t)
$$

其中 $\omega_0\equiv \sqrt{k / m}$ ， $\gamma = \omega_0^2\tau$ ，以及 $\gamma \ll \omega_0$ （与 $\omega_0^2$ 相比舍去了 $\gamma^2$ ，而当你在一个完整的周期内求平均值时，忽略 $\mathrm{e}^{-\gamma t}$ 的变化）。

（b）假设现在我们有两个这样的振子，开始时让它们受到相同的冲击。无论它们的相对位置和方向如何，辐射的总能量必须为 $2U_{0}$ 。但是，如果它们正好在一起，那么它就相当于带有2倍电荷的单个振子；按拉莫尔公式，辐射的功率是它的4倍，这表明总辐射能量将是 $4U_{0}$ 。找出这个推导中的错误，并证明总数实际上是理所应当的 $2U_{0}^{15}$ 。

习题11.19 考虑辐射反作用力[式(11.80)]，带电粒子的牛顿第二定律变为

$$
a = \tau \dot {a} + \frac {F}{m}
$$

式中， $F$ 是作用在粒子上的外力。

(a) 与不带电粒子不同 $(a = F / m)$ ，加速度（与位置和速度一样）必须是时间的连续函数，即使力突然变化。（从物理上看，辐射反作用阻碍 $a$ 的快速变化。）通过对上面运动方程从 $(t - \varepsilon)$ 到 $(t + \varepsilon)$ 积分并取极限 $\varepsilon \rightarrow 0$ ，证明 $a$ 在任何时刻都是连续的。

(b) 一个粒子在 $t = 0$ 受到一恒定的力 $F$ ，持续时间为 $T$ 。求在下面三个时间段内最一般的运动方程的解：(i) $t < 0$ ；(ii) $0 < t < T$ ；(iii) $t > T$ 。

(c) 在 (a) $t = 0$ 和 $t = T$ 加连续性条件，证明可以要么在时间段（iii）内消除粒子奔离，要么在时间段内（i）避免预加速，实现二者之一，但不能两者同时实现。

(d) 如果你选择消除奔离解，在每个时间间隔内加速度随时间如何变化？速度如何变化？（当然速度在 $t = 0$ 和 $t = T$ 时必须连续。）假设粒子初始时静止： $v(-\infty) = 0$ 。

（e）对一个不带电粒子和一个（没有奔离解）带电粒子施加这个力，画出 $a(t)$ 和 $v(t)$ 。

## 11.2.3 相应于辐射反作用的机制

在上一节利用能量守恒推导出了辐射反作用的亚伯拉罕-洛伦兹公式。除了指出它一定是粒子自身的场对电荷的反作用外没有试图确定它的实际机制。很遗憾，点电荷的场在粒子所在的地方为无限大，很难明白如何计算它们施加的力 $^{16}$ 。为避免这个场发散的问题，让我们考虑扩展电荷分布的情形，这种情形下场在任何地方都是有限值，最后我们考虑电荷的尺寸趋于零时的极限。一般地，一部分（A）对另一部分（B）的电磁力与B作用在A上的力并不大小相同、方向相反（图11.16）。如果把分布无限细分，则每一对都存在着这种不平衡力，对所有的不平衡力求和，结果是电荷作用在自身上的一个净的作用力。正是这种自作用力（self-force）导致在粒子内部牛顿第三定律被打破，这就是辐射反作用。

![](images/db406e8f9ea9410913d026969e1117962c21557cb52d650cfb40698698a3a558.jpg)  
图11.16

洛伦兹最初用一个球形电荷分布计算电磁场自作用力，结果看上去合理，但数学相当复杂 $^{17}$ 。因为我仅想说明相关机理，我将用一个更不实际的模型：一个带总电荷为q的“哑铃”，电荷分为距离固定为d的两半（图11.17）。这是能说明主要机理（内部电磁力不平衡）起作用的电荷的最简单可能分布。不要介意这对一个基本粒子是一个不太可能的模型：在点极限 $(d\rightarrow0)$ 下，任何模型都必定会得到亚伯拉罕-洛伦兹公式，在某种程度上可以认为这仅仅是能量守恒决定的结果。

假设哑铃沿 x 方向运动，在推迟时刻（瞬时）静止。（2）在（1）处产生的电场是

$$
\boldsymbol {E} _ {1} = \frac {(q / 2)}{4 \pi \varepsilon_ {0}} \frac {\boldsymbol {r}}{(\boldsymbol {r} \cdot \boldsymbol {u}) ^ {3}} \left[ (c ^ {2} + \boldsymbol {r} \cdot \boldsymbol {a}) \boldsymbol {u} - (\boldsymbol {r} \cdot \boldsymbol {u}) \boldsymbol {a} \right]\tag{11.85}
$$

[式 (10.72)], 式中,

$$
\pmb {u} = c \hat {\pmb {z}} \quad \text {以及} \quad \pmb {r} = l \hat {\pmb {x}} + d \hat {\pmb {y}}\tag{11.86}
$$

![](images/ae01048332b1c8f5ba5973e121c23e5c89a729d5b40483c2e3c0bcfa392145d4.jpg)  
推迟位置 $x(t_r)$ 现在位置 $x(t)$  
图11.17

因而

$$
\pmb {r} \cdot \pmb {u} = c ^ {2}, \quad \pmb {r} \cdot \pmb {a} = l a, \quad \text {以及} \quad r = \sqrt {l ^ {2} + d ^ {2}}\tag{11.87}
$$

实际上我们仅对 $E_{1}$ 的 x 分量感兴趣，因为当我们在两端加力时（由于同样的理由我们不必担心磁力）y 分量抵消了。现在

$$
u _ {x} = \frac {c l}{\nu}\tag{11.88}
$$

从而

$$
E _ {1 _ {x}} = \frac {q}{8 \pi \varepsilon_ {0} c ^ {2}} \frac {l c ^ {2} - a d ^ {2}}{(l ^ {2} + d ^ {2}) ^ {3 / 2}}\tag{11.89}
$$

由对称性， $E_{2_x} = E_{1_x}$ ，所以作用在哑铃上的净力是

$$
\pmb {F} _ {\text {自}} = \frac {q}{2} \left(\pmb {E} _ {1} + \pmb {E} _ {2}\right) = \frac {q ^ {2}}{8 \pi \varepsilon_ {0} c ^ {2}} \frac {l c ^ {2} - a d ^ {2}}{(l ^ {2} + d ^ {2}) ^ {3 / 2}} \hat {\pmb {x}}\tag{11.90}
$$

到目前为止，一切都是精确的。现在的想法是按 $d$ 的级数展开，当粒子大小趋于零时所有 $d$ 正幂次项都将趋于零。利用泰勒定理

$$
x (t) = x \left(t _ {r}\right) + \dot {x} \left(t _ {r}\right) \left(t - t _ {r}\right) + \frac {1}{2} \ddot {x} \left(t _ {r}\right) \left(t - t _ {r}\right) ^ {2} + \frac {1}{3 !} \dddot {x} \left(t _ {r}\right) \left(t - t _ {r}\right) ^ {3} + \dots
$$

我们有

$$
l = x (t) - x \left(t _ {r}\right) = \frac {1}{2} a T ^ {2} + \frac {1}{6} \dot {a} T ^ {3} + \dots\tag{11.91}
$$

式中为了简洁令 $T \equiv t - t_r$ 。现在 $T$ 由推迟时刻条件决定：

$$
(c T) ^ {2} = l ^ {2} + d ^ {2}\tag{11.92}
$$

于是

$$
d = \sqrt {(c T) ^ {2} - l ^ {2}} = c T \sqrt {1 - \left(\frac {a T}{2 c} + \frac {\dot {a} T ^ {2}}{6 c} + \cdots\right) ^ {2}} = c T - \frac {a ^ {2}}{8 c} T ^ {3} + () T ^ {4} + \dots
$$

这个方程给出了 d 的用 T 表示的关系，我们需要 “求解” 以 d 为变量的函数 T。这有个系统的处理方法，称为级数的逆（reversion of series） $^{18}$ ，但我们可通过下面的一个近似方法得到前几项：忽略所有 T 的高阶项，

$$
d \approx c T \Rightarrow T \approx \frac {d}{c}
$$

把这个近似用到三次方项

$$
d \approx c T - \frac {a ^ {2}}{8 c} \frac {d ^ {3}}{c ^ {3}} \Rightarrow T \approx \frac {d}{c} + \frac {a ^ {2} d ^ {3}}{8 c ^ {5}}
$$

如此进行下去。于是，

$$
T = \frac {1}{c} d + \frac {a ^ {2}}{8 c ^ {5}} d ^ {3} + () d ^ {4} + \dots\tag{11.93}
$$

回到式 (11.91)，我们用 $d$ 构造 $l$ 级数：

$$
l = \frac {a}{2 c ^ {2}} d ^ {2} + \frac {\dot {a}}{6 c ^ {3}} d ^ {3} + () d ^ {4} + \dots\tag{11.94}
$$

把它代入式 (11.90)，我得到

$$
\pmb {F} _ {\text {自}} = \frac {q ^ {2}}{4 \pi \varepsilon_ {0}} \left[ - \frac {a}{4 c ^ {2} d} + \frac {\dot {a}}{1 2 c ^ {3}} + () d + \dots \right] \hat {\pmb {x}}\tag{11.95}
$$

式中， $a$ 和 $\dot{a}$ 是在推迟时刻 $t_r$ 时的值，但容易用当前时刻 $t$ 表示：

$$
a \left(t _ {r}\right) = a (t) + \dot {a} (t) \left(t _ {r} - t\right) + \dots = a (t) - \dot {a} (t) T + \dots = a (t) - \dot {a} (t) \frac {d}{c} + \dots
$$

由此，

$$
\pmb {F} _ {\text {自}} = \frac {q ^ {2}}{4 \pi \varepsilon_ {0}} \left[ - \frac {a (t)}{4 c ^ {2} d} + \frac {\dot {a} (t)}{3 c ^ {3}} + () d + \dots \right] \hat {\pmb {x}}\tag{11.96}
$$

式中右边的第一项正比于电荷的加速度，如果把它放在牛顿第二定律方程的另一边，只需简单地加上哑铃的质量。事实上，带电哑铃的有效总质量是

$$
m = 2 m _ {0} + \frac {1}{4 \pi \varepsilon_ {0}} \frac {q ^ {2}}{4 d c ^ {2}}\tag{11.97}
$$

式中， $m_{0}$ 是哑铃一端单独的质量。在狭义相对论的情况下，电荷的排斥会增加哑铃的质量，这不奇怪。这个构型的电势能（静止状态）是

$$
\frac {1}{4 \pi \varepsilon_ {0}} \frac {(q / 2) ^ {2}}{d}\tag{11.98}
$$

根据爱因斯坦公式 $E = mc^2$ ，这一能量对物体的惯性贡献了份额19。

式 (11.96) 的第二项是辐射反作用

$$
F _ {\mathrm{辐射}} ^ {\mathrm{作用}} = \frac {\mu_ {0} q ^ {2} \dot {a}}{1 2 \pi c}\tag{11.99}
$$

它是在“点哑铃”极限 $d \to 0$ 情形下保留的唯一的项（除了质量修正 $^{20}$ ）。很遗憾，它与亚伯拉罕-洛伦兹公式相差一个因子2。但这只是1和2之间相互作用有关的自作用力——所以有上标“作用”。每一端对自己都有作用力。当包括后者时（参看习题11.20），结果是

$$
F _ {\mathrm{辐射}} = \frac {\mu_ {0} q ^ {2} \dot {a}}{6 \pi c}\tag{11.100}
$$

这与亚伯拉罕-洛伦兹公式完全一致。结论：辐射反作用力是电荷自身的作用力——或者更精细地，是由分布在不同部分的电荷产生的场对它们彼此施加的净力。

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
习题11.20 从式(11.99)推导式(11.100)。这里有3种方法：（a）利用亚伯拉罕-洛伦兹公式求哑铃每一端的辐射反作用，把它加在相互作用项中[式(11.99)]。（b）方法（a）的缺陷是要利用亚伯拉罕-洛伦兹公式——它正是我们要推导的。为了避免这一点，令 $F(q)$ 为作用于 $q$ 的与 $d$ 无关的总的部分。则$F(q) = F^{\text{作用}}(q) + 2F(q / 2)$ 其中 $F^{\text{作用}}(q)$ 是相互作用部分[式(11.99)]，而 $F(q / 2)$ 是每一端的自力。现在， $F(q)$ 应与 $q^{2}$ 成正比，因为场正比于 $q$ 而力为 $qE$ 。于是 $F(q / 2) = \frac{1}{4} F(q)$ ，从那里入手。（c）沿着垂直于运动方向的长度为 $L$ 的条带抹平电荷分布（这样电荷密度为 $\lambda = q / L$ )，利用式(11.99)求出所有片段对的相互作用力（利用对应：在一端 $q / 2\to \lambda \mathrm{dy}_1$ ；另一端 $q / 2\rightarrow \lambda \mathrm{dy}_2)$ 。注意同一对不要计数两次。！习题11.21 $^{21}$ 一个电偶极子在 $xy$ 平面内以恒定角速度 $\omega$ 旋转。[电荷 $\pm q$ 处于 $r_{\pm} = \pm R(\cos \omega t\hat{x}+$ n $\omega t\hat{y})$ ；其电偶极矩的大小为 $p = 2qR$ 。]（a）求出自力矩的相互作用项[类似式(11.99)]。假设运动是非相对论性的 $(\omega R\ll c)$ （b）利用习题11.20（a）的方法，求出这一系统总的辐射作用力矩。$\left[\text{答案:}-\frac{\mu_0p^2\omega^3}{6\pi c}\hat{z}\right]$ （c）验证这一结果与辐射功率[式(11.60)]一致。
</div>

## 第11章补充习题

习题11.22 一个质量为 $m$ 、带电量为 $q$ 的粒子，固定在一劲度系数为 $k$ 的挂在天花板上的弹簧上（图11.18）。它的平衡位置距地板高度为 $h$ 。在 $t = 0$ 时刻，粒子被下拉一段距离 $d$ 并释放。

(a) 在通常假设下 $(d \ll \lambda \ll h)$ ，计算照射到地板上的辐射强度，表示为地板上到电荷 $q$ 正下方点距离 $R$ 的函数。[注意：这里的强度指的是单位地板面积上的平均功率。] $R$ 是多大时辐射最强？忽略振子的辐射阻尼。[答案： $\mu_0 q^2 d^2 \omega^4 R^2 h / 32\pi^2 c(R^2 + h^2)^{5/2}$ ]

(b) 为了验证你的结果，假设地板无限大，计算单位时间辐照在整个地板上的平均能量。结果与你预期的一致吗？

(c) 因为振子以辐射的形式损失能量，它的振幅会逐渐减小。经过多长时间 $\tau$ 振幅减小为 $d / e?$ （假设一个周期损失的能量占总能量的非常小的一部分。）

![](images/02aadcfeea212f164b30c95c64a7b58a97584903b4378901caf09f2ad855aab5.jpg)  
图11.18

习题 11.23 一个发射塔高出地面高度为 h。顶端为一个磁偶极发射天线，半径为 b，其轴沿竖直方向。调频电台 KRUD 从这个天线以角频率 $\omega$ 广播，发射的总辐射功率为 P（这当然是一个周期的平均）。周围的居民们抱怨一些问题——他们的音响系统受到干扰、车库门神秘地开合以及各种可疑的疾病问题，把这些问题归因于塔的辐射。但城市的工程师测量塔基处的辐射水平发现辐射远低于在可接受的标准。你受聘于居民区协会，评估工程师的报告。

(a) 用给定的量（当然不是所有的都是相关的），求在地面距塔基 $R$ 处的辐射强度表达式。你可以假设 $b \ll c / \omega \ll h$ 。[注意：我们仅对辐射的幅度而不是方向感兴趣——在测量时探测器直接对着天线。]

(b) 工程师测量的地方应距塔基多远？在这个地方辐射强度表达式是什么？

(c) KRUD 施加输出功率是 35 kW，频率是 90 MHz，天线的半径是 6.0 cm，塔高 200 m。城市电磁波辐射限制是 $200 \mu W/cm^{2}$ 。KRUD 符合要求吗？

!习题11.24 作为一个电四极矩辐射模型,考虑两个相反方向振动的电偶极子,相距为 $d$ ,如图11.19所示。利用11.1.2节中给出的每个偶极子势的结果,但是要注意到现在它们不是位于原点。仅保留 $d$ 的一阶项:

![](images/50f1eab2016ee743be1aba816a1b20afabd7911ed9239dac634666fdd9f86c5b.jpg)  
图11.19

(a) 求标势和矢势。

(b) 求电场和磁场。

(c) 求坡印亭矢量和辐射功率。画出以 $\theta$ 为变量的强度分布函数图。

习题11.25 大家知道地球的磁北极与地理北极不一致——它偏离约 $11^{\circ}$ 。所以，地球的磁偶极矩矢量相对于固定转动轴是随着时间变化的，地球必定有磁偶极辐射。

(a) 用下面的参数表示出总的辐射： $\psi$ （地理北极和地磁北极的夹角）， $M$ （地球的磁偶极矩大小）， $\omega$ （地球转动角速度）。[提示：参看习题11.4和习题11.11。]

（b）地磁场在赤道处的磁场强度约为 0.5 Gs，由此估计地球的磁偶极矩大小 M。

(c) 求辐射功率。[答案： $4 \times 10^{-5}W$ ]

(d) 脉冲星是旋转的中子星，典型半径为 $10\mathrm{km}$ ，转动周期为 $10^{-3}\mathrm{s}$ ，表面磁场是 $10^{8}\mathrm{T}$ 。你预期它的辐射功率怎么样？[答案： $2 \times 10^{36}\mathrm{W}$ ]

习题11.26 理想的电偶极子位于原点；其偶极矩指向 $z$ 方向，并且关于时间是二次幂的：

$$
\pmb {p} (t) = \frac {1}{2} \ddot {p} _ {0} t ^ {2} \hat {\pmb {z}} (- \infty <   t <   \infty)
$$

其中 $\ddot{p}_0$ 是常量。

(a) 利用 11.1.2 节的方法确定对所有 r > 0（严格的）电场与磁场（在原点也有 δ-函数项，但是我们暂时不关心）。 $\left[\text{部分答案：} V = \frac{\mu_{0}\ddot{p}_{0}}{8\pi} \cos \theta \left[(ct/r)^{2} - 1\right], A = \frac{\mu_{0}\ddot{p}}{4\pi c} [(ct/r) - 1]\hat{z}\right]$

（b）计算通过原点为球心、半径为 $r$ 的球面的功率 $P(r,t)$ 。 $\left[\text{答案：}\frac{\dot{p}_0^2}{12\pi\varepsilon_0r^3} t\left[t^2 +(r / c)^2\right]\right]$

(c) 计算总辐射功率 [式 (11.2)]，并验证你的结果与式 (11.60) 一致 $^{23}$ 。

!习题 11.27 在 11.2.1 节我们计算了一个（非相对论性）点电荷单位时间内辐射的能量——拉莫尔公式。本着同样的精神：

（a）计算单位时间内辐射的动量。 $\left[\text{答案：}\frac{\mu_0q^2}{6\pi c^3} a^2\pmb {v}\right]$

（b）计算单位时间内辐射的角动量。 $\left[\text{答案：}\frac{\mu_0q^2}{6\pi c} (\pmb {v}\times \pmb {a})\right]$

习题11.28 假设（电中性的） $yz$ 面载有随时间变化的均匀的面电流 $K(t)\hat{z}$ 。

(a) 求出在下面条件下在距平面高度为 $x$ 处的电场和磁场。

(i) 在 $t = 0$ 时刻开始，有一恒定电流：

$$
K (t) = \left\{ \begin{array}{l l} 0, & t \leqslant 0 \\ K _ {0}, & t > 0 \end{array} \right.
$$

(ii) 在 $t = 0$ 时刻开始，有一线性增加的电流：

$$
K (t) = \left\{ \begin{array}{l l} 0, & t \leqslant 0 \\ \alpha t, & t > 0 \end{array} \right.
$$

(b) 证明推迟矢势可以表示为

$$
\boldsymbol {A} (x, t) = \frac {\mu_ {0} c}{2} \hat {z} \int_ {0} ^ {\infty} K \left(t - \frac {x}{c} - u\right) \mathrm{d} u
$$

并由此求出 E 和 B。

(c) 证明单位面积表面辐射的功率是

$$
\frac {\mu_ {0} c}{2} [ K (t) ] ^ {2}
$$

在这种源非局域的情况下解释“辐射”的含义 $^{24}$ 。

习题 11.29 利用对偶变换（习题 7.64）构造一个任意运动的磁单极子 $q_{m}$ 的电场和磁场，求出辐射功率的“拉莫尔公式” $^{25}$ 。

习题11.30 假设在习题11.19中你排除了奔离解，计算

(a) 外力做的功。

(b) 最后的动能（假设初始动能是零）。

(c) 总辐射能。

验证在这个过程中能量守恒 $^{26}$ 。

习题11.31

(a) 重复习题 11.19，但这次外力是一个狄拉克函数： $F(t)=k\delta(t)$ （k 是某一常数） $^{27}$ 。[注意现在加速度在 t=0 时刻是不连续的（虽然速度仍然必须是连续的）。利用习题 11.19（a）的方法证明 $\Delta a=-k/m\tau$ 。在这个问题中仅需考虑两个间隔：(i) t<0 和 (ii) t>0。]

（b）如同习题11.30，验证在这个过程中能量守恒。

!习题11.32 一带电粒子，沿 $x$ 轴从 $-\infty$ 处运动过来，遇到一个方形势垒

$$
U (x) = \left\{ \begin{array}{l l} U _ {0}, & \text {若} 0 <   x <   L \\ 0, & \text {其他地方} \end{array} \right.
$$

证明由于辐射反作用，粒子可能隧穿通过势垒——也就是即使入射动能小于 $U_{0}$ ，粒子也能够通过势垒 $^{28}$ 。[提示：你的任务是求解方程

$$
a = \tau \dot {a} + \frac {F}{m}
$$

所施加的力是

$$
F (x) = U _ {0} [ - \delta (x) + \delta (x - L) ]
$$

参考习题11.19和11.31，但注意这里力是 $x$ 的而不是 $t$ 的函数。需要考虑三个区域：（i） $x < 0$ ，（ii） $0 < x < L$ ，（iii） $x > L$ 。除了在第三个区域的奔离解，在每个区域求出一般解[即 $a(t), v(t)$ 和 $x(t)$ ]，利用在 $x = 0$ 和 $x = L$ 处适当的边界条件。证明最后的速度（ $v_{\mathrm{f}}$ ）与穿过势垒所用时间 $T$ 之间的关系由下式给出：

$$
L = v _ {\mathrm{f}} T - \frac {U _ {0}}{m v _ {\mathrm{f}}} \left(\tau \mathrm{e} ^ {- T / \tau} + T - \tau\right)
$$

而初始速度（在 $x = -\infty$ 处）为

$$
v _ {\mathrm{i}} = v _ {\mathrm{f}} - \frac {U _ {0}}{m v _ {\mathrm{f}}} \left[ 1 - \frac {1}{1 + \frac {U _ {0}}{m v _ {\mathrm{f}} ^ {2}} (\mathrm{e} ^ {- T / \tau} - 1)} \right]
$$

为了简化这些结果（因为要找一个特定例子），假设最后的动能是势垒高度的一半。证明在这种情况下

$$
v _ {\mathrm{i}} = \frac {v _ {\mathrm{f}}}{1 - (L / v _ {\mathrm{f}} \tau)}
$$

特别地，如果选择 $L = v_{f}\tau/4$ ，则 $v_{i} = (4/3)v_{f}$ ，初始动能是 $(8/9)U_{0}$ 。尽管其能量小于势垒，粒子还是能穿过！]

## !习题11.33

(a) 一个粒子沿着直线以任意速度运动，不要假设 $v(t_r) = 0$ ，通过重新构造11.2.3节中的讨论，求解作用在粒子上的辐射反作用力。[答案： $(\mu_0 q^2 \gamma^4 / 6\pi c)(\dot{a} + 3\gamma^2 a^2 v / c^2)$ ]

(b) 证明结果与这个粒子辐射功率 [式 (11.75)] 一致 [在式 (11.78) 的意义上]。

## 习题11.34

（a）做双曲线运动的带电粒子 [式 (10.52)] 辐射吗？[利用精确公式，即式 (11.75) 计算辐射功率。]

（b）做双曲运动的带电粒子受辐射反作用吗？[利用精确公式（习题11.33）求反作用力。]

[评论：这些著名的问题包含等效原理（principle of equivalence）的重要信息 $^{29}$ 。]

习题11.35 利用习题10.34的结果确定处于原点的理想电偶极子 $p(t)$ 的辐射功率。检查你所得结果与式(11.22)一致，也与习题11.26的时间二次方依赖关系的情形一致。

## 第 12 章 电动力学与相对论

## 12.1 狭义相对论

## 12.1.1 爱因斯坦的假设

经典力学遵从相对性原理（principle of relativity）：相同的定律适用于任何惯性参考系（inertial reference frame）。我所说的“惯性”指的是系统处于静止或匀速运动的状态 $^{1}$ 。例如，想象你把一个台球桌搬到一列列车上，列车沿着平直的光滑轨道匀速行驶。在车上玩台球与车静止在车站时完全一样，你不必因为车在运动而“校正”你的击打——的确，如果你把所有的窗帘都拉上，你将无法知道列车是否在运动。注意，作为比较，如果列车加速或减速，或转过一个拐角，或驶过路面一个隆起，你立刻就能知道——台球会沿着奇怪的曲线滚动，你自己也感到一阵晕眩，把咖啡洒在了衬衫上。在这些加速参考系中，力学定律当然不再相同。

在经典力学中，相对性原理并不新奇，它曾被伽利略清楚地表述过。问题：它对电动力学的定律也同样适用吗？乍看起来答案似乎是否定的。毕竟运动的电荷将产生磁场，而静止的电荷不会产生磁场。在车下的人看来，随列车运动的电荷将会产生磁场，但对处在车上的人，电荷是静止的，在这个参考系中运用电动力学定律，将得不出磁场。事实上，许多以洛伦兹力定律为出发点的电动力学方程都涉及电荷的速度。所以这看来电动力学理论预先假设存在一个唯一的静止参考系，所有的速度都是相对于这个参考系的。

然而有一个非同寻常的巧合之事让我们停下来思考。假设我们在车厢里安装一个导线线圈，并让列车从一个大磁铁的磁极间通过（图12.1）。当线圈穿过磁场时，其中产生一个动生电动势。根据磁通量规则[式(7.13)]，

$$
\mathcal {E} = - \frac {\mathrm{d} \varPhi}{\mathrm{d} t}
$$

记住，这个电动势是由于和火车一起运动的线圈中电荷受到磁场力而产生的。另一方面，如果火车上有人简单地将电动力学定律应用于该系统，结果会是什么？没有磁力！因为线圈是静止的。但当磁铁飞过时，车厢处的磁场将发生变化，由法拉第定律，变化的磁场将导致电场。由此产生的电场力就在线圈中产生电动势，由式(7.14):

$$
\mathcal {E} = - \frac {\mathrm{d} \Phi}{\mathrm{d} t}
$$

由于由法拉第定律和磁通量规则可得出完全相同的电动势，在车上的人将得到正确的结果，尽管他们对该过程的物理解释是完全错误的。

![](images/74f5a8992e942321c6715c768f912a68241b279d1bcfd1e5cd3002d19bedcac0.jpg)  
图12.1

事情真是如此吗？爱因斯坦不相信这仅是个纯粹的巧合；他把这看作是电磁现象，与力学现象一样，遵从相对性原理的一个线索。在他看来，火车上观察者的分析与地面上观察者的分析一样，都是正确的。如果他们的解释不同（一个是电的过程，一个是磁的过程），也就这样吧；他们的实际预测是一致的。这里是爱因斯坦在他1905年介绍狭义相对论论文的第一页所写的内容：

大家知道，麦克斯韦电动力学——像现在通常为人们所理解的那样——当应用到运动的物体上时，导致不对称，而这种不对称似乎不是现象所固有的。比如设想一个磁体同一个导体之间的电动力的相互作用。在这里，可以按照通常的看法，这两个物体之中，究竟是这个在运动，还是那个在运动，是截然不同的两回事。如果是磁体在运动，导体静止着，那么在磁体附近就会出现一个电场……它在导体各部分所在的地方产生一股电流。但是如果磁体是静止的，而导体在运动，那么磁体附近就没有电场，可是在导体中却有一个电动势……却会引起——假定这里所考虑的两种情况中的相对运动是相等的——电流，这种电流的大小和路线都同前一情况中由电力所产生的一样。

诸如此类的例子，以及企图寻找地球相对于“光媒质”运动的失败的尝试，意味着电动力学现象，与机械运动一样，不存在对应绝对静止概念的特性 $^{2}$ 。

让我先介绍这个故事以前的情形。对于爱因斯坦的前辈们，两个电动势相等仅是个幸运的偶然事件。他们毫无疑问地认为一个观察者是正确的，而另一个是错误的。他们认为电磁场是在某种看不见的称为以太的胶状媒质中的应变，以太充满整个空间。电荷的速度是相对于以太而言的——只有这样电动力学的定律才是有效的。火车上观察者的结论是错误的，因为他的参考系是相对于以太运动的。

但请等等！我们如何知道地面上的观察者相对于以太不是运动的？毕竟地球绕着它的轴一天自转一周，绕着太阳一年公转一周，太阳系围绕着银行系运转。据我所知，整个银行系也许是在宇宙中高速运动。总的来说，我们应该相对于以太以稳超50km/s的速度在运动。如同在公路上骑行的摩托车手，我们将面对高速的“以太风”——除非由于某些神秘的巧合，我们恰巧顺风，且风的强度恰好合适；或者地球有某种风挡，带着地球上的以太与它一起运动。突然间，实验上寻找以太参考系就变得至关重要了，否则我们的所有计算都是无效的。

这样一来，问题就是确定我们在以太中的运动——测量“以太风”的速度和方向。如何测量？乍看起来你也许认为实际中的任何电磁实验都可以：如果麦克斯韦方程仅是相对于以太参考系正确，任何实验和理论预测的差异都可归因于以太风。很遗憾，正如19世纪的物理学家很快认识到的，在一个典型的实验中可预期的误差非常小。如上面的例子，“巧合”似乎总是导致把我们使用“错误”参考系这个事实遮盖起来。故需要一个异常精巧的实验去完成这项工作。

现在，经典电动力学的结果预言电磁波在真空中的传播速度是

$$
\frac {1}{\sqrt {\varepsilon_ {0} \mu_ {0}}} = 3. 0 0 \times 1 0 ^ {8} \mathrm{m/s}
$$

（也许）它是相对于以太的。这样，原则上通过简单测量光沿不同方向的速度就能测量以太风。像在河里行驶的摩托艇，“顺流”的速度应是最大的，对于这种情形，光是顺着以太风的方向；在相反方向，它阻碍光波，光的速度应是最小的（图 12.2）。

![](images/b91cba1182bfaaa9a328ca9cb433a602d9a1cecb4918c337d92104f2b23641ed.jpg)  
图12.2

尽管实验的思想不能再简单了，而实现起来是另一回事，因为光的传播速度太快。假如不是“技术细节”问题，你用闪光灯和秒表就可做这个实验。事实上，迈克耳孙和莫雷设计了一个非常精巧和漂亮的实验，在实验中采用了具有极高精度的光干涉仪。我不想讨论实验细节，因为不想让你们从两个实质问题上分散注意力：（1）迈克耳孙和莫雷试图要做的是比较光在不同方向的速度，（2）事实上他们的实验发现在所有方向上速度都是精确一样的。

如今，当学生们在高中被教导嘲笑以太模型的天真时，确实需要一些想象才能理解这一结果在当时曾经是怎样令人完全困惑。所有其他波（水波、声波、弦上的波）相对于传播介质（波的载体）都以规定的速度传播。如果介质相对于观察者运动，波沿“顺流”的净速度总是比“逆流”的大。在以后的20年中，一系列似乎不太可能的方案被设计出来以解释为何对光来说不是这样。迈克耳孙和莫雷他们自己解释他们的实验证实了“携带以太”假说，这个假说认为地球携带着以太一起运动。但这个解释与其他观察到的现象——特别是光行差现象——不一致 $^{3}$ 。各种各样所谓的“发射”理论被提出，在这些理论中电磁波的速度被源的运动所决定——像微粒说理论那样（认为光是粒子流）。这些理论要求对麦克斯韦方程进行难以置信的修改，但无论何种情况，这样的理论都被地外光源的实验证实为不可信。另外，斐兹杰惹和洛伦兹建议以太风会压缩所有的物质（包括迈克耳孙-莫雷实验仪器本身），从而刚好补偿和抵消了速度在不同方向上的变化。事实证明，这种解释包含某些真实性，尽管他们对收缩原因的想法是完全错误的。

无论如何，直到爱因斯坦才赋予了迈克耳孙-莫雷实验的真正价值，他提出光速是一个普适常数，在所有方向都相同，不论观察者和源运动与否。不存在以太风，因为以太不存在。任何惯性系都是一个适当的参考系，在这样的参考系麦克斯韦方程都是适用的。电荷速度测量既不是相对于一个（不存在的）绝对静止系，也不是相对于（不存在的）以太，而是简单地相对于你所选择的某个惯性参考系。

这样，受内部理论的暗示（即在“错误”的参考系中应用电动力学定律也能给出正确结果）及外部实验结果（迈克耳孙-莫雷实验 $^{4}$ ）的启发，爱因斯坦提出了他的两个著名的假设：

1. 相对性原理。物理定律在所有惯性系都是适用的。

2. 光速不变原理。真空中光速对所有惯性系中的观察者都是相同的，不论光源运动与否。

狭义相对论由这两个假设导出。第一个假设把伽利略关于经典力学的论述提升到了适用于所有物理的普适定律的高度。它指出不存在绝对静止的参考系。第二个假设可认为是爱因斯坦对迈克耳孙-莫雷实验的回应。它意味着以太是不存在的。（一些作者认为爱因斯坦的第二个假设是多余的——它仅是第一个假设的一种特殊情况。他们坚持认为正是以太的存在违反了相对性原理，因为这样就可以定义一个唯一的静止参考系。我认为这是毫无道理的。作为声音传播媒质的空气的存在并没有使相对论站不住脚。以太与金鱼缸中的水一样也不是一个绝对静止的参考系——而仅是一个特殊参考系，如果你正好是那条金鱼，而绝不可能“绝对”静止。） $^{5}$

不像相对性原理，它的根源可以追溯到几个世纪前，光速不变是全新的——而且乍看起来是荒谬的。因为如果我以 5 mile/h 的速度在一个速度为 60 mile/h 的火车车厢内向前走，我相对于地的净速度 “显然” 是 65 mile/h——A（我）相对于 C（地）的速度等于 A 相对于 B（火车）的速度加上 B 相对于 C 的速度：

$$
v _ {A C} = v _ {A B} + v _ {B C}\tag{12.1}
$$

但是，如果 $A$ 是光信号（无论它从火车上的闪光灯或是地面上的灯或天空中的星星发出），爱因斯坦让我们相信它相对于火车以及相对于地面的速度都是 $c$ ：

$$
v _ {A C} = v _ {A B} = c\tag{12.2}
$$

式(12.1)，我们现在称为伽利略速度合成法则（Galileo's velocity addition rule）（在爱因斯坦以前根本没有人费心要给它取一个名字），它与爱因斯坦的第二个假设是不相容的。在狭义相对论中，我们将看到，它被爱因斯坦速度合成法则（Einstein's velocity addition rule）所代替：

$$
\boxed {v _ {A C} = \frac {v _ {A B} + v _ {B C}}{1 + (v _ {A B} v _ {B C} / c ^ {2})}}\tag{12.3}
$$

对于“通常的”速度（ $v_{AB} \ll c, v_{BC} \ll c$ ），式中分母非常接近1，伽利略公式和爱因斯坦公式的差异可忽略。另一个方面，爱因斯坦公式有预期的特性，如果 $v_{AB} = c$ ，则自动地有 $v_{AC} = c$ ：

$$
v _ {A C} = \frac {c + v _ {B C}}{1 + (c v _ {B C} / c ^ {2})} = c
$$

但基于常识的伽利略原理怎么可能是错误的？如果它是错的，这对整个经典物理意味着什么？回答是狭义相对论迫使我们改变对空间和时间的观念，当然还包括对由它推导出的一些物理量，如速度、动量和能量的观念。尽管历史上它是由爱因斯坦对电动力学的思考发展而来，但狭义相对论并不局限于任何特别现象——它是对所有物理现象发生其中的时空“舞台”的描述。尽管在第二个假设中涉及光速，但相对论与光没有关系：c仅是一个基本速度，光恰好以这个速度传播。但完全可以设想一个宇宙，在其中没有电荷，因此也就没有电磁场或电磁波，而相对论依然成立。因为相对论定义了时空结构，它不仅支配着目前已知的现象，也支配着还没有发现的未知现象。正如康德曾经说过的，它是“任何将来物理的序言”。

(a) 证明动量在惯性系 $\overline{S}$ 中也守恒。 $\overline{S}$ 相对于 $S$ 以速度 $\pmb{v}$ 运动。[利用伽利略速度合成法则——这完全是经典力学的计算。对质量你必须有什么假设？]

(b) 假设在 S 中碰撞是弹性的，证明在 $\overline{S}$ 中碰撞也是弹性。

## 习题12.3

(a) 如 $v_{AB} = 5 \, mile/h$ , $v_{BC} = 60 \, mile/h$ ，用伽利略速度合成法则代替爱因斯坦速度合成法则计算产生的误差百分比是多少？

（b）假设你以一半的光速沿火车车厢向前跑，火车以 $3 / 4$ 的光速前进，你对地面的速度是多少？

(c) 利用式 (12.3)，如果 $v_{AB} < c$ ， $v_{BC} < c$ ，证明 $v_{AC} < c$ 。解释这个结果。

习题12.4 逃犯驾车以 $\frac{3}{4} c$ 的速度逃跑，警察驾车以 $\frac{1}{2} c$ 的速度（图12.3）追击并开枪。子弹（相对于枪）的初速是 $\frac{1}{3} c$ 。根据（a）伽利略原理，（b）爱因斯坦原理，子弹能击中目标吗？

![](images/17b41e79eca9ec276dfb2400492d2c96300d6f2fc1dfc4af39b47a0d68f0fbfe.jpg)  
图12.3

## 12.1.2 相对论几何学

在本节我将利用几个思想实验用来介绍由爱因斯坦的假设所得出的三个最著名的几何结果：时间延缓、洛伦兹收缩和同时相对性。同样的结果，将在12.1.3节利用洛伦兹变换更系统地推导出。

（i）同时相对性。设想一节车厢，沿着光滑平直的轨道以恒定速度运动（图 12.4）。在车中央悬挂以灯泡。当有人打开灯泡时，灯光以光速 c 向各个方向传播。由于灯泡两边车厢的长度相同，在车厢的观察者会看到灯光同时到达车厢前后两端：问题中的两个事件——（a）光到达车厢前端（也许蜂鸣器会响）和（b）光到达车厢后端（另一个蜂鸣器响起）——同时发生。

但对地面上的观察者，同样的这两个事件却是不同时的。因为当光线从灯泡中发出向外传播时（前后两方向都以速度 c 前进——这是第 2 假设），火车本身向前运动，所以光线到达车后端的距离较到达前端的距离短（图 12.5）。当然在这个观察者看来，事件（b）先于事件（a）发生。同时在另一列相向通过的快车上，观察者会看到事件（a）先于事件（b）。结论：

在一个惯性参考系中同时发生的两个事件，一般来说，在另一个惯性参考系中是不同时的。

![](images/400a7490bac4f63a5eb98d4365142238ea29a8955f93611b207f97a6c849e47e.jpg)  
图12.4

![](images/8079d44b6aaa82c5076c650986b3d03151b8938745c5ddadc03100e9ec0ff306.jpg)  
图12.5

当然，为了探测出两个事件不是同时发生的，火车要非常快——这就是为何你们一直没有注意到它的原因。

当然，没有经验的目击者总有可能对同时性产生误解：坐在汽车后角的人会在蜂鸣器 $a^{6}$ 之前听到蜂鸣器b，仅仅是因为他离声源更近，而一个孩子可能会推断b实际上是在a之前响的。但这是个微不足道的错误，与相对论没有关系——显然，你必须校正信号（声、光、信鸽或任何其他的信号）到达你的时间。当我说观测者时，我指的是具有智识进行这种校正的人，而一个观测结果就是观测者进行这样校正后所记录的东西。因此，你所听到的或者所看到的东西，与你所观测到的东西是不同的。一个观测是事件之后的人工重建，当所有数据都在时，它不依赖于观测者处在哪一个位置。事实上，聪明的观测者将如此避免全部问题：在一些关键位置安排助手，每一位助手都配备与主钟同步的时钟，这样时间的测量可以如同在现场进行。我不厌其烦地说明这一点，其目的在于强调同时相对性是由称职的、有相对运动的观测者们所做测量之间的真正差异，而不是由于错误地计算光信号传播的时间所造成的简单错误。

习题12.5 在一直线上每相隔100万 $\mathrm{km}$ 放置一个同步时钟。当你旁边的钟读数为中午12点时：（a）你看到的第90个钟的读数是多少？

(b) 你观测到的这个钟的读数是多少?

习题12.6 大约每过两年纽约时报会发表一篇文章，文中报道有些宇航员声称他们发现一个物体以超光速的速度运动。许多这类报告起源于不能正确区分看到的和观测到的区别——即来源于对光传播时间错误的计算。这里有一个例子：一个恒星以速度 $v$ 沿与视线成 $\theta$ 角的方向运动（图12.6）。它掠过天空的表观速度是多少？（假设从 $b$ 发出的光信号到达地球的时间比从 $a$ 发出的光信号到达地球晚 $\Delta t$ ，星球同时在天球上移动的距离为 $\Delta s$ ；我指的“表观速度”即 $\Delta s / \Delta t$ 。）夹角 $\theta$ 取什么值时可给出最大的表观速度？证明即便 $v$ 比 $c$ 小，表观速度能够远大于 $c$ 。

![](images/dea5d781cdf7bdd8db1ca8da2daf148fda4be0d96c0f57fea7196a72175092e8.jpg)  
图12.6

（ii）时间延缓。让我们考虑灯泡发出的光线直接照射到它下面的车厢地板上。问题：光线经过这段距离需要的时间是多少？在车上的观察者给出答案是容易的。如果车厢高度是h，时间为

$$
\Delta \bar {t} = \frac {h}{c}\tag{12.4}
$$

（我用一个上划线来表示在火车上进行的测量。）另一方面，在地面上的观察者看到这束光线必须行走更长的距离，因为火车本身在运动。从图12.7可看到这段距离为 $\sqrt{h^2 + (v\Delta t)^2}$ ，故有

$$
\Delta t = \frac {\sqrt {h ^ {2} + (v \Delta t) ^ {2}}}{c}
$$

![](images/89cc7626bc4fa1044a1107512a37cbfb964f49b5771de57f84ef5ed8bc3451ce.jpg)  
图12.7

解出 $\Delta t$ ，得

$$
\Delta t = \frac {h}{c} \frac {1}{\sqrt {1 - v ^ {2} / c ^ {2}}}
$$

于是

$$
\boxed {\Delta \bar {t} = \sqrt {1 - v ^ {2} / c ^ {2}} \Delta t}\tag{12.5}
$$

显然，相同的两件事——（a）光离开灯泡；（b）光到达地板中心——它们发生的时间间隔对不同的观察者来说是不同的。事实上，在车上的时钟记录的时间间隔 $\Delta t$ 缩短一个因子

$$
\boxed {\gamma \equiv \frac {1}{\sqrt {1 - v ^ {2} / c ^ {2}}}}\tag{12.6}
$$

结论：

运动的时钟变慢。

这就是所谓的时间延缓（time dilation）。它与钟表的机理没有任何关系，它表述的是时间本身的性质，它对任何正常工作的计时装置都是适用的。

在所有爱因斯坦的预言中，没有比时间延缓得到更令人惊异和更有说服力的证实。大多数基本粒子是不稳定的：经过一个特征寿命后它们衰变成其他粒子 $^{8}$ 。中子的寿命是15min， $\mu$ 子的寿命是 $2.2\times10^{-6}s$ ，中性 $\pi$ 介子的寿命是 $9\times10^{-17}s$ 。但这些都是粒子静止时的寿命。当粒子以接近于光速运动时，它们持续的时间要长得多，因为它们固有时钟（不管是什么，用来告诉它们什么时候它们时间到了）变慢了，这与爱因斯坦时间延缓公式一致。

例题12.1 一个 $\mu$ 子以 $\frac{3}{5} c$ 的速度通过实验室。它能持续多久？[解答] 在这种情况，

$$
\gamma = \frac {1}{\sqrt {1 - (3 / 5) ^ {2}}} = \frac {5}{4}
$$

故它运动时的寿命比静止时长一个因子 $\frac{5}{4}$

$$
\frac {5}{4} \times (2 \times 1 0 ^ {- 6}) \mathrm{s} \approx 2. 5 \times 1 0 ^ {- 6} \mathrm{s}
$$

你们也许会感到惊讶，时间延缓与相对性原理不一致。因为如果地面上的观察者说车上的时钟变慢了，车上的观察者也同样有把握地声称地面上的时钟变慢了——毕竟，以火车的角度来看是地面在运动。谁是正确的？答案：两者都对！更进一步检查之下，发现这个看起来非常明显的“矛盾”并不存在。让我来解释：为了检查车上时钟的快慢，地面上的观察者用两个他自己的时钟（图12.8）：一个用来比较当车上的钟经过 $A$ 点时、在间隔开始时的两个时间，另一个用来比较当车上的时钟运动到 $B$ 点时、在间隔结束时的两个时间。当然，在实验前他必须让他的钟严格同步。他所发现的是车上的钟走了，比如说3分钟，他自己两个钟的读数间隔是5分钟。他的结论是车上的钟慢了。

![](images/c28bc02d628eaee7f102d1ec9532c16de00e3531450b7eab6060afbe2dfcf90d.jpg)  
图12.8

同时，车上的观察者通过同样的过程检查地面上钟的快慢：她用两个仔细同步的列车上的钟；当地面上的一个钟依次经过它们时，比较列车上的钟和地面上这个钟的两个时间（图12.9）。她发现地面上的钟滴答作响3min时，她车上的两个钟时间间隔为5min，于是她的结论是地面上的钟慢了。有矛盾吗？没有，因为两个观察者测量的是不同的事情。地面上的观察者是把车上的一个钟与地面上的两个钟相比较，而车上的观察者是把地面上的一个钟与车上的两个钟比较。每个人都遵循了一个合理而正确的程序，将一个运动的钟与两个静止的钟进行比较。“什么，”你说，“两个静止的钟在每一时刻都同步，那么用两个和用一个无关紧要。”但要点是：在一个参考系中同步的钟在另一个参考系中观察时将是不同步的。它们也不能同步，当说两个钟同步，是指它们的读数同时为中午12点。我们已经知道对一个观察者的同时，对另一个观察者则不同时。所以，尽管每个观察者都进行了完全合理的测量，但从他/她自己的立场来看，另一位观察者（在观察事件的过程中）认为她/他犯了本书中最基本的错误，即用了两个不同步的钟。这就是为何尽管事实是他自己的钟“实际”走慢了，他得出结论却是她的钟变慢了（反之亦然）。

![](images/0339aedb5f3b2649e693dff03e3d51e864bdb77f11163977e19bed8cef2a3a24.jpg)  
图12.9

因为运动的钟不同步，切记当检查时间变慢时应关注一个运动的钟。所有运动的钟以相同的因子变慢，但你不能让一个钟开始计时然后切换到另一个钟去继续计时，因为它们在开始时已不同步。但你使用多少静止的钟（相对于你，观察者）都可以，因为它们是准确同步的（移动的观察者对此会有争议，但这是他们的问题）。

例题12.2 双胞胎佯谬。一个宇航员在她21岁生日时乘火箭飞船以 $\frac{12}{13} c$ 的速度离开。相对于她自己的时钟，5年后调头，以相同的速度回来与她的待在家中的孪生哥哥团聚。问题：这对双胞胎团聚时，各自多大年龄？

[解答] 旅行的双胞胎之一长了10岁（去程5年，回程5年），她回到家刚好庆祝她的31岁生日。但从地球上看，运动的钟变慢了，变慢因子为

$$
\gamma = \frac {1}{\sqrt {1 - (1 2 / 1 3) ^ {2}}} = \frac {1 3}{5}
$$

地球上的钟经过了 $\frac{13}{5} \times 10 = 26$ 年，故她的孪生哥哥要庆贺他的47岁生日——他现在比他的孪生妹妹年长了16岁！但不要被欺骗了：旅行的妹妹并没有真正变年轻，因为虽然她可能比他的双胞胎哥哥晚去世，但她活的时间并没增加——只是生活的时间变慢了。在飞行过程中，她所有的生物过程——新陈代谢，脉搏，思想及说话——都有与她的手表一样的变慢因子。

所谓的双胞胎佯谬（twin paradox）是这样的：当你试图从旅行的双胞胎观点看这个过程时，她看到地球以 $\frac{12}{13} c$ 的速度飞离，5年后开始折回团聚。在她看来，她似乎是处于静止状态，她的双胞胎哥哥在运动，故是他在团聚的时候应更年轻。关于双胞胎悖论有许多论著，但真实的情况是这里根本不存在这样的佯谬：第二个分析是完全错误的。两个双胞胎不是等效的，旅行的双胞胎在往返过程中要经过加速过程，而他的哥哥却没有。用专业的术语来说就是旅行的双胞胎不是在一个惯性系中——更准确说，她在去时是在一个惯性系中，在返回时是在另一个完全不同的惯性系中。在习题12.16中你会看到从她的角度怎样正确分析这个问题，但对佯谬本身的解释，只需注意旅行的双胞胎不能声称自己是静止的观察者就足够了，因为你不能经过加速，再保持原来的静止。

习题12.7 在实验室的实验中，一个 $\mu$ 子在衰变前被观察到经过了 $800\mathrm{m}$ 长的距离。一个研究生测量到 $\mu$ 子的寿命（ $2\times 10^{-6}\mathrm{s}$ ），据此计算它的速度是

$$
v = \frac {8 0 0 \mathrm{m}}{2 \times 1 0 ^ {- 6} \mathrm{s}} = 4 \times 1 0 ^ {8} \mathrm{m/s}
$$

比光速还大！找出这个学生的错误，并求出粒子的实际速度。

习题12.8 一个火箭以 $\frac{3}{5} c$ 的速度离开地球。当火箭上的时钟过去 $1\mathrm{h}$ 的时候，火箭向地球发出一个光信号。

(a) 根据地球上的时钟，这个光信号是何时发出的？

(b) 根据地球上的时钟，火箭离开后多久这个光信号到达地球？

（c）根据火箭上的观察者，火箭离开后多久光信号到达地球？

（iii）洛伦兹收缩。对于第三个理想实验，你想象我们在一节车厢的一端装了一盏灯，在另一端装了一面镜子，所以光线可以被反射回去（图 12.10）。问题：光信号一个来回需多长时间？对于在车上的观察者，答案是

$$
\Delta \bar {t} = 2 \frac {\Delta \bar {x}}{c}\tag{12.7}
$$

式中， $\Delta\bar{x}$ 是车厢的长度（与前面相同，上面的一横表示在车上进行的测量）。对在地面上的观察者，由于车在运动，该过程较为复杂。如果 $\Delta t_{1}$ 是光信号到达前端的时间，而 $\Delta t_{2}$ 是折回的时间，那么（参看图 12.11）：

$$
\Delta t _ {1} = \frac {\Delta x + v \Delta t _ {1}}{c}, \quad \Delta t _ {2} = \frac {\Delta x - v \Delta t _ {2}}{c}
$$

![](images/bec15f8c43b1f8ef253e4d83be80568aac773f66895171e3d872279cbc3b669b.jpg)  
图12.10

![](images/2684cb6159a7c0a63e19ab906811df9e1cb88b6640243949a56756282fa9c13a.jpg)  
图12.11

或者，解出 $\Delta t_{1}$ 和 $\Delta t_{2}$ ，

$$
\Delta t _ {1} = \frac {\Delta x}{c - v}, \quad \Delta t _ {2} = \frac {\Delta x}{c + v}
$$

故这一个来回的时间是

$$
\Delta t = \Delta t _ {1} + \Delta t _ {2} = 2 \frac {\Delta x}{c} \frac {1}{(1 - v ^ {2} / c ^ {2})}\tag{12.8}
$$

该时间间隔与时间延缓公式 (12.5) 相联系：

$$
\Delta \bar {t} = \sqrt {1 - v ^ {2} / c ^ {2}} \Delta t
$$

把此式用于式 (12.7) 和式 (12.8)，我得到了

$$
\boxed {\Delta \bar {x} = \frac {1}{\sqrt {1 - v ^ {2} / c ^ {2}}} \Delta x}\tag{12.9}
$$

当在地面上的观察者测量时，车厢的长度与车上的观察者测得的长度不同——从地面上的观察者来看，车厢有些变短了。结论：

运动的物体长度变短。

我们称之为洛伦兹收缩（Lorentz contraction）。注意在时间延缓和长度收缩公式中出现同样的因子

$$
\gamma \equiv \frac {1}{\sqrt {1 - v ^ {2} / c ^ {2}}}
$$

这使这些公式容易记忆：运动的钟变慢，运动的尺子变短，变化因子均为 $\gamma$ 。

当然，在车上的观察者不认为她的车厢变短了——她的米尺收缩了同样的因子，因而所有她的测量结果与火车静止时测得的完全一样。事实上，从她的观点来看是地面上物体的长度缩短了。这又产生了一个悖论：假如 A 认为 B 的尺子短了，而 B 认为 A 的尺子短了，那么谁是正确的？答案：两者都对！但为了协调这相反的观点我们必须仔细研究长度测量的实际过程。

假设你想测量一个木板的长度。如果它（相对于你）静止，你只要把尺子放在木板旁边，记录下尺子在两端的读数，然后相减就得出木板的长度了（图 12.12）。（如果你足够聪明，把尺子的左端与木板的左端对齐——这样你只需读一个数就可以了。）

![](images/c42e698288557ec89cc0d1bdddf423451f47b78ebfcd650bfc0fb4a12f594d35.jpg)  
图12.12

但如果木板在运动，情况怎样？按同样的方法测量，当然只是这次你必须细心在同一瞬时读出两端的读数。如果你不同时读出，在测量的过程中木板的运动将使你得到错误的结果。但这里存在一个问题：因为同时的相对性，两个观察者对“同一瞬间”的认识是不同的。当地面上的人测量车厢的长度时，他在他自己参考系在同一瞬时读出两端的位置。但在车上的人，她观察地面上人的测量，她抱怨地面上的人先读前端的位置，然后等了片刻才读后端的位置。自然，地面上的人测量的结果是缩短了，尽管事实上对她来说地面上的人用的是一个缩短的米尺，测量的读数本来应该太大。两个观察者都正确地进行了测量（从各自的惯性系来看），各自发现对方的尺子短了。但这里不存在不一致，因为他们在测量不同的事物，每个人认为对方的方法不适当。

梯子能够，还是不能被装下？

![](images/7f14682311d3966e63a5c5c2ddf1e05973afc412572f55281979055419cee70e.jpg)

[解答] 他们两个都对！当你说“梯子在谷仓里”时，你的意思是梯子的全部于一个瞬时在谷仓中。但根据同时的相对性，同时是有条件的，依赖于观察者。这里其实有两个相关事件：

a. 梯子尾端进入谷仓门。

b. 梯子前端碰到谷仓门对面墙壁。

农夫说事件 $a$ 先于事件 $b$ 发生，故存在一个梯子完全进入谷仓的时间；她的女儿说 $b$ 先于 $a$ 发生，故不可能存在一个梯子完全进入谷仓的时间。这矛盾吗？一点也不矛盾——仅是观察的不同而已。

“但是现在来吧，”我听到你抗议道，“当事件发生过后，一切都尘埃落定了，梯子是在还是不在谷仓中，事情应该是清楚的，对此不应该有争议。”确实如此，但现在你在故事中引进了一个新因素：当梯子停下来时会发生什么？假设农夫用一只手紧紧抓住梯子最后一档，另一只手关门。假设梯子不受损伤，梯子现在必须伸长到其原长。显然，当梯子的后端停止后，梯子前端必须继续前移！像一个手风琴展开一样，梯子的前端撞向谷仓里面的另一边。的确，在相对论中“刚体”失去了它的名字所具有的意义，因为当它的速度改变时，一般来讲，不同部分的瞬时加速度是不同的——这样材料的各部分会扩张或收缩以适应它的新速度 $^{9}$ 。

但回到目前的问题：当梯子最终停下时，它是否在谷仓？答案是不确定的。当梯子前端撞到谷仓里面的墙时，某些事情发生了，留给农夫的要么是一截破损的梯子在谷仓里，要么是梯子完好无损地从墙上的一个洞里伸了出来。在任何情况下，他都不可能对结果满意。

对洛伦兹收缩最后一个评述。一个运动的物体仅在它运动的方向上收缩。

在垂直于速度方向不收缩。

的确，在推导时间延缓公式中我事先假定对两个观察者来说车厢的高度是一样的。我现在利用一个由泰勒和惠勒提出的生动的理想实验来证实这一点 $^{10}$ 。想象我们在铁轨旁建一堵墙，在墙上画出一条水平蓝线，蓝线距轨道高度为1m（在地面上测量）。当火车经过墙时，一个乘客举着一把油漆刷子，在墙上画一个水平红线，从车上测量，红线距轨道的高度也是1m。问题：红线是在蓝线的上方还是下方？假如尺子在垂直方向缩短，地面上的人将预言红线在蓝线下面，而车上的人将预言蓝线在红线下面（对于后者，当然是地面在移动）。相对性原理认为两个观察者的结果同样合理，但不可能他们都是正确的。没有微妙的同时或同步来合理解释这种矛盾；要么蓝线高要么红线高——除非它们完全一样高，这是不可避免的结论。不可能有垂直速度方向的缩短（或膨胀），因为这将导致不可解释的互相矛盾的预言。

习题12.9 当处于静止时，林肯大陆豪华敞篷车是甲壳虫轿车长度的两倍。当林肯车追上甲壳虫车时正通过一个汽车超速监视区，一个（静止的）警察看到这两辆车长度一样。甲壳虫是以光速一半的速度在行驶。林肯轿车的速度是多少？（答案以光速为单位。）

习题12.10 一个帆船的桅杆和甲板成角度为 $\bar{\theta}$ 。一个观察者站在码头上看到船以速率 $v$ 经过（图12.14）这个观察者说桅杆与甲板之间的角度是多少？

![](images/2996d02c9e104cdc924705a87ef882c75be244417ee3a924ca11b0602cac2748.jpg)  
图12.14

习题 12.11 一个半径为 R 的唱片转盘以角速度 $\omega$ 转动（图 12.15）。周长很有可能发生洛伦兹收缩而半径不收缩（因为垂直于速度方向）。用 $\omega$ 和 R 表示的周长和直径的比值是多少？按通常的几何，这个结果是 $\pi$ 。这里将是什么 $^{11}$ ?

![](images/a126343a207204125232ab14f5461f402567e29439e447c945ca6fce510c001a.jpg)  
图12.15

## 12.1.3 洛伦兹变换

任何物理过程都由一个或多个事件（events）组成。一个“事件”发生在空间一个确定的位置 $(x,y,z)$ 和准确的时间 $(t)$ 。例如爆竹的爆炸就是一个事件，而在欧洲的一个旅行不是。假设我们知道一个事件 $E$ 在一惯性参考系 $\mathcal{S}$ 中的坐标 $(x, y, z, t)$ ，并且我们想计算这个同一事件在另一个惯性参考系 $\overline{\mathcal{S}}$ 中的坐标 $(\bar{x}, \bar{y}, \bar{z}, \bar{t})$ 。为此，我们所需要的是一本“字典”，通过它把 $\mathcal{S}$ 中的语言翻译成 $\overline{\mathcal{S}}$ 中的语言。

我们让坐标轴的方向如图 12.16 所示，这样 $\overline{S}$ 系沿着 x 轴以速率 v 运动。假如我们在原点（O 和 $\overline{O}$ ）重合瞬间让时钟“开始计时”（t=0），那么在 t 时刻， $\overline{O}$ 距 O 的距离是 vt，于是

$$
x = d + v t\tag{12.10}
$$

式中，d 是在 t 时刻 $\overline{O}$ 距 $\overline{A}$ 的距离（ $\overline{A}$ 是 x 轴上的点，当事件发生时与事件 E 持平）。在爱因斯坦以前，任何人都会立刻得到

$$
d = \bar {x}\tag{12.11}
$$

并由此构造出“字典”

(i)

(ii)

(iii)

(iv)

$$
\left. \begin{array} {l}\bar {x} = x - v \dot {t} \\ \bar {y} = y \\ \dot {\bar {z}} = z \\ \bar {t} = t \\ \end{array} \right\}\tag{12.12}
$$

这些现在被称为伽利略变换（Galilean transformations），尽管没必要给它们定义一个名字——特别是最后一个变换，没有给出任何理由，因为每个人都认为对所有观察者来说时间流逝都是一样的。但在狭义相对论中，我们必须期望（iv）被包含时间延缓、同时的相对性及运动时钟不同步的规则代替。同样，考虑到洛伦兹收缩，（i）也需修正。对于（ii）和（iii），它们保持不变，因为我们已经看到在垂直运动的方向长度没有变化。

![](images/49f6e494db0b4af50af7e6040248e8316249ea643f772adb04ea26a6b7ec2eb2.jpg)  
图12.16

但是在导出经典关系式（i）时哪些地方不成立了？答案：在式(12.11)中。因为 $d$ 是在 $\mathcal{S}$ 系中测得的 $\overline{\mathcal{O}}$ 距 $\overline{A}$ 的距离，而 $\bar{x}$ 是在 $\overline{\mathcal{S}}$ 系中测得的 $\overline{\mathcal{O}}$ 距 $\overline{A}$ 的距离。因在 $\overline{\mathcal{S}}$ 系中$\overline{\mathcal{O}}$ 和 $\overline{A}$ 是静止的，是一个“移动的木棒”，在 $S$ 系中它缩短为

$$
d = \frac {1}{\gamma} \bar {x}\tag{12.13}
$$

当把这个式子代入式 (12.10)，得到具有相对论版本的表达式（i）

$$
\bar {x} = \gamma (x - v t)\tag{12.14}
$$

当然，从 S 系的观点可进行同样的论证。图 12.17 看上去类似，但在这种情形下，说明的是在 $\bar{t}$ 时刻的情况，而图 12.16 表示的是在 t 时刻的情形。（注意 t 和 $\bar{t}$ 表示在 E 处的相同物理时刻，但由于同时的相对性在其他地点不同。）如果我们假设 $\overline{S}$ 系中的钟在两个原点重合时也开始计时，那么在 $\bar{t}$ 时刻，O 与 $\overline{O}$ 的距离是 $v\bar{t}$ ，所以有

$$
\bar {x} = \bar {d} - v \bar {t}\tag{12.15}
$$

![](images/19b452dcfbb97fee70d73433de09c2bc3035c6db3b1189ecf233084e62ca31a4.jpg)  
图12.17

式中， $\bar{d}$ 是在 $\bar{t}$ 时刻 $\mathcal{O}$ 距 $A$ 的距离。 $A$ 是在 $x$ 轴上的点，当事件发生时其与 $E$ 的坐标相同。经典物理学家会认为 $x = \bar{d}$ ，并且利用（iv）得到（i）。但是，和以前一样，相对论要求我们观察一个微妙的区别： $x$ 是在 $S$ 系中 $\mathcal{O}$ 到 $A$ 的距离， $\bar{d}$ 是在 $\overline{S}$ 系中 $\mathcal{O}$ 到 $A$ 的距离。因为 $\mathcal{O}$ 和 $A$ 在 $S$ 系中是静止的， $x$ 是“移动的木棒”，有

$$
\bar {d} = \frac {1}{\gamma} x\tag{12.16}
$$

由此得

$$
x = \gamma (\bar {x} + v \bar {t})\tag{12.17}
$$

这最后一个方程的得出一点也不奇怪，因为对称性要求用 $\bar{x}$ 和 $\bar{t}$ 表示的 $x$ ，除了 $v$ 符号的变化外，应当与用 $x$ 和 $t$ 表示的 $\bar{x}$ 相同[式(12.14)]。（假如 $\overline{\mathcal{S}}$ 系相对于 $\mathcal{S}$ 系以速率 $v$ 向右运动，则 $\mathcal{S}$ 系相对于 $\overline{\mathcal{S}}$ 系以速率 $v$ 向左运动。）不管怎样，这是个有用的结果，因为假如将其中 $\bar{x}$ 用式 (12.14) 代入，解出 $\bar{t}$ ，我们就完成了相对论的 “字典”：

$$
\boxed { \begin{array}{l l} \text {(i)} & \bar {x} = \gamma (x - v t) \\ \text {(ii)} & \bar {y} = y \\ \text {(iii)} & \bar {z} = z \\ \text {(iv)} & \bar {t} = \gamma \left(t - \frac {v}{c ^ {2}} x\right) \end{array} }\tag{12.18}
$$

这些就是著名的洛伦兹变换，爱因斯坦用它们代替了伽利略变换。如下面的例子说明的那样，它们包含了狭义相对论中所有的几何信息。从 $\overline{S}$ 系到 $S$ 系的反向字典通过解（i）和（iv）求出 $x$ 和 $t$ 得到，或更简单通过改变 $v$ 的符号得到：

$$
\left. \begin{array}{l} \left(\mathrm{i} ^ {\prime}\right) x = \gamma (\bar {x} + v \bar {t}) \\ \left(\mathrm{ii} ^ {\prime}\right) y = \bar {y} \\ \left(\mathrm{iii} ^ {\prime}\right) z = \bar {z} \\ \left(\mathrm{iv} ^ {\prime}\right) t = \gamma \left(\bar {t} + \frac {v}{c ^ {2}} \bar {x}\right) \end{array} \right\}\tag{12.19}
$$

例题12.4 同时，同步及时间延缓。假设事件 $A$ 发生在 $x_{A} = 0, t_{A} = 0$ ，事件 $B$ 发生在 $x_{B} = b, t_{B} = 0$ ，两事件在 $\mathcal{S}$ 系中是同时的（它们都发生在 $t = 0$ 时刻）。但因为洛伦兹变换有 $\bar{x}_{A} = 0, \bar{t}_{A} = 0$ 和 $\bar{x}_{B} = \gamma b, \bar{t}_{B} = -\gamma (v / c^{2})b$ ，它们在 $\overline{\mathcal{S}}$ 系中是不同时的。根据 $\overline{\mathcal{S}}$ 系中的钟， $B$ 事件早于 $A$ 事件发生。这当然没有什么新东西——只是同时的相对性而已。但是我想让你们明白它是如何从洛伦兹变换得出的。

现在假设在时刻 $t = 0$ ，在 $\mathcal{S}$ 系的观察者决定检查 $\overline{\mathcal{S}}$ 系中的所有的钟。他发现它们的读数不同，读数依赖于它们的位置。由（iv）：

$$
\bar {t} = - \gamma \frac {v}{c ^ {2}} x
$$

那些在原点左边的（负 $x$ ）钟超前，而在原点右边的钟落后，提前或落后量与它们的距离成正比增加（图12.18）。仅在原点处的主钟读数为 $\bar{t} = 0$ 。故运动时钟的不同步也直接来自洛伦兹变换。当然，从 $\overline{S}$ 看 $S$ 系中的钟也是不同步的，把 $\bar{t} = 0$ 代入式（ $\mathrm{iv}'$ ）就可以验证。

![](images/f3aa1d31ccebdd7c320ad1776378fb633fd10e4102a6527094d27fd7c40f6c37.jpg)  
图12.18

最后，假设 $S$ 系中的观察者只关注 $\overline{S}$ 系中的一个钟（如，在 $\bar{x} = a$ 处的那个钟），并注视它一

段时间 $\Delta t$ 。运动的钟流逝了多长时间？因为 $\bar{x}$ 是固定的，由（iv'）给出 $\Delta t = \gamma \Delta \bar{t}$ ，或

$$
\Delta \bar {t} = \frac {1}{\gamma} \Delta t
$$

这就是原来的时间延缓公式，现在从洛伦兹变换把它推导出来了。请注意，我们这里是把 $\bar{x}$ 固定，因为我们观察的是一个运动的钟。如果把 $x$ 固定，你看到的将是 $\overline{S}$ 系中整个一系列的钟经过，这样不能得出它们中的任何一个钟是变慢的。

例题12.5 洛伦兹收缩。设想一个在参考系 $\overline{S}$ 中静止的木棒（从而在 $S$ 系中以速率 $v$ 向右运动），它静止时的长度（即 $\overline{S}$ 中测得的长度）是 $\Delta \bar{x} = \bar{x}_r - \bar{x}_l$ ，式中下标表示木棒的右端和左端。假如 $S$ 系中的观察者测量木棒的长度，他将在他的时间的某一瞬时 $t$ ，由木棒两端的坐标差得到木棒长度： $\Delta x = x_r - x_l$ （对于 $t_l = t_r$ ）。这样根据（i），有

$$
\Delta x = \frac {1}{\gamma} \Delta \bar {x}
$$

这是原来所得的洛伦兹收缩公式。注意这里我们固定的是 $t$ ，因为讨论的是在 $\mathcal{S}$ 系中的测量，他在他的时间的同一瞬时标记木棒两端的坐标。（在 $\overline{\mathcal{S}}$ 系中不用这么复杂，因为木棒在这个参考系中是静止的。）

例题12.6 爱因斯坦速度合成法则。设一个粒子在时间 $\mathrm{dt}$ 内移动一段距离 $\mathrm{dx}$ (在 $S$ 系中)，它的速度 $u$ 为

$$
u = \frac {\mathrm{d} x}{\mathrm{d} t}
$$

同时，由式（i），在 $\overline{S}$ 系中移动的距离为

$$
\mathrm{d} \bar {x} = \gamma (\mathrm{d} x - v \mathrm{d} t)
$$

所用时间由式（iv）给出：

$$
\mathrm{d} \bar {t} = \gamma \left(\mathrm{d} t - \frac {v}{c ^ {2}} \mathrm{d} x\right)
$$

故在 $\overline{S}$ 系中的速度为

$$
\bar {u} = \frac {\mathrm{d} \bar {x}}{\mathrm{d} \bar {t}} = \frac {\gamma (\mathrm{d} x - v \mathrm{d} t)}{\gamma [ \mathrm{d} t - (v / c ^ {2}) \mathrm{d} x ]} = \frac {\mathrm{d} x / \mathrm{d} t - v}{1 - (v / c ^ {2}) (\mathrm{d} x / \mathrm{d} t)} = \frac {u - v}{1 - u v / c ^ {2}}\tag{12.20}
$$

这就是爱因斯坦速度合成法则（Einstein's velocity addition rule）。为了回到更明晰的式(12.3)，令 $A$ 为粒子， $B$ 为 $\mathcal{S}$ 参考系， $C$ 为 $\overline{\mathcal{S}}$ 参考系，这样 $u = v_{AB}$ ， $\bar{u} = v_{AC}$ ，而 $v = v_{CB} = -v_{BC}$ ，故式(12.20)变为

$$
v _ {A C} = \frac {v _ {A B} + v _ {B C}}{1 + (v _ {A B} v _ {B C} / c ^ {2})}
$$

这与以前的形式相同。

习题12.12 解出式(12.18)的 $x, y, x, t$ ，用 $\bar{x}, \bar{y}, \bar{z}, \bar{t}$ 表示，验证你得到式(12.19)。

习题 12.13 千里眼苏菲·扎巴尔，就在她 500km 外的双胞胎哥哥用锤子砸到手指的同时，而疼痛地叫喊。一个持怀疑态度的科学家在速度为 $\frac{12}{13}c$ 的飞机上飞向右边（图 12.19），观察这两个事件（哥哥砸手和苏菲叫喊）。根据这个科学家的观察，哪一个事件先发生？早了多少秒？

![](images/9e212557a3b252a6ebc5f5c78cae70480e8e46b48b837ff9ec203ded9d3e66f6.jpg)  
图12.19

习题12.14

(a) 在例题 12.6 中我们求出在 x 方向的速度从 S 系变换到 $\overline{S}$ 的变换关系。推导出在 y 和 z 方向类似的速度变换公式。

（b）一个聚光灯安装在一个船上，光线与甲板成角度为 $\bar{\theta}$ （图12.20）。如果这只船以速率 $v$ 运动，根据码头上观察者的说法，单个光子轨迹与甲板的夹角 $\theta$ 是多少？光束（例如，被薄雾显示）的角度是多少？与习题12.13比较，解释两者的不同。

![](images/c7868099ca595be075c038b0272027a90975d80d38158c025e3b989c3632ccd3.jpg)  
图12.20

习题12.15 你可能是以站在地面上观察者的观点对习题12.4求解。现在从警车、逃犯和子弹的观点求解，在下面表格中的空白处填上相应结果。

<table><tr><td>速度→相对↓</td><td>地面</td><td>警察</td><td>逃犯</td><td>子弹</td><td>可以逃脱吗?</td></tr><tr><td>地面</td><td>0</td><td> $\frac{1}{2}c$ </td><td> $\frac{3}{4}c$ </td><td></td><td></td></tr><tr><td>警察</td><td></td><td></td><td></td><td> $\frac{1}{3}c$ </td><td></td></tr><tr><td>逃犯</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>子弹</td><td></td><td></td><td></td><td></td><td></td></tr></table>

习题12.16 双胞胎佯谬的再考察。在他们21岁生日那天，双胞胎中的一个进入以速度 $\frac{4}{5} c$ 向X星球运行的人行道，她的双胞胎哥哥待在家中。当她到达X星球时，立刻跳上以同样速度返回的人行道。在她39岁时回到家（以她自己的表计算的时间）。

(a) 她双胞胎哥哥的年龄是多少（他待在家中）?

(b) 地球距 X 星球多远？(以光年表示。)

把向外运行的人行道记为 $\overline{S}$ 系，向回运行的人行道记为 $\tilde{S}$ 系（地球为 S 系）。所有三个参考系调整它们的主钟并选择原点，使在离开那一瞬间有 $x = \bar{x} = \tilde{x} = 0, t = \bar{t} = \tilde{t} = 0$ 。

(c) 在 $\mathcal{S}$ 系中换乘 (从去的人行道换到回来的人行道) 处的坐标 $(x, t)$ 是什么？

(d) 在 $\overline{S}$ 系中换乘处的坐标 $(\bar{x},\bar{t})$ 是什么？

(e) 在 $\tilde{S}$ 系中换乘处的坐标 $(\tilde{x},\tilde{t})$ 是什么？

(f) 如果旅行的双胞胎想让她的表与 $\tilde{S}$ 系中的一致，她应该在换乘的瞬间如何调整她的表？如果她这样做了，回到家时她表的读数会是多少？（这不会改变她的年龄——她当然还是39岁——这仅仅使她的表符合 $\tilde{S}$ 系中的标准同步。）

（g）如果旅行的双胞胎被问道：“你的哥哥现在多大了？”对下面两种情形正确的回答是什么？(i) 就在她换乘以前那时刻，(ii) 就在她换乘以后那时刻？[当然，对他哥哥来说在她从 (i) 变到 (ii) 时没有什么戏剧性的事情发生。会突然改变的是他妹妹的“现在，回家”的含义。]

（h）返回花费的时间是地球上的多少年？把这加到（g）中的（ii）上确定她预期的他的哥哥在他们团聚的时候是多大年龄。与你的（a）的答案比较。

## 12.1.4 时空结构

（i）四-矢量。当用下面的量表示洛伦兹变换时其形式会更简化：

$$
x ^ {0} \equiv c t, \quad \beta \equiv \frac {v}{c}\tag{12.21}
$$

利用 $x^{0}$ （代替 t）和 $\beta$ （代替 v）把时间的单位从秒变为米——1 米对应光传播 1 米用的时间（在真空中）。如果同时也给 x, y, z 坐标编号，有

$$
x ^ {1} = x, \quad x ^ {2} = y, \quad x ^ {3} = z\tag{12.22}
$$

这样洛伦兹变换为

$$
\left. \begin{array}{l} \bar {x} ^ {0} = \gamma (x ^ {0} - \beta x ^ {1}) \\ \bar {x} ^ {1} = \gamma (x ^ {1} - \beta x ^ {0}) \\ \bar {x} ^ {2} = x ^ {2} \\ \bar {x} ^ {3} = x ^ {3} \end{array} \right\}\tag{12.23}
$$

或者用矩阵的形式：

$$
\left( \begin{array}{c} {\bar {x}} ^ {0} \\ {\bar {x}} ^ {1} \\ {\bar {x}} ^ {2} \\ {\bar {x}} ^ {3} \end{array} \right) = \left( \begin{array}{c c c c} {\gamma} & {- \gamma \beta} & 0 & 0 \\ {- \gamma \beta} & \gamma & 0 & 0 \\ {0} & 0 & 1 & 0 \\ {0} & 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c} {x ^ {0}} \\ {x ^ {1}} \\ {x ^ {2}} \\ {x ^ {3}} \end{array} \right)\tag{12.24}
$$

让希腊字母从0到3取值，式(12.24)可以浓缩记为一个方程

$$
\bar {x} ^ {\mu} = \sum_ {\nu = 0} ^ {3} \left(\Lambda_ {\nu} ^ {\mu}\right) x ^ {\nu}\tag{12.25}
$$

式中， $\Lambda$ 是式 (12.23) 中的洛伦兹变换矩阵（Lorentz transformation matrix）（上标 $\mu$ 标记行，下标 $\nu$ 标记列）。以这种抽象形式表示的一个优点是我们能用相同的形式处理更加一般的变换，其中的相对移动并不沿 $x$ 方向；对这种情况变换矩阵会更复杂，但式 (12.24) 的结构不变。

如果这使你回想起我们在 1.1.5 节学习过的转动，它并非偶然。那里我们关注的是当坐标系转动时坐标的变换。而这里我们感兴趣的是运动坐标系的坐标变换。在第 1 章我们定义了一个（3-）矢量，在转动情况下它的三个分量变换与用 $(x, y, z)$ 表示时变换相同。把它推广，现在我们定义一个 4-矢量（4-vector）来表示任何一组四分量，在洛伦兹变换

$$
\bar {a} ^ {\mu} = \sum_ {\nu = 0} ^ {3} \varLambda_ {\nu} ^ {\mu} a ^ {\nu}\tag{12.26}
$$

下它们与 $\left(x^{0},x^{1},x^{2},x^{3}\right)$ 有相同的变换形式。对于一个沿 $x$ 轴变换的特殊情形，

$$
\left. \begin{array}{l} \bar {a} ^ {0} = \gamma (a ^ {0} - \beta a ^ {1}) \\ \bar {a} ^ {1} = \gamma (a ^ {1} - \beta a ^ {0}) \\ \bar {a} ^ {2} = a ^ {2} \\ \bar {a} ^ {3} = a ^ {3} \end{array} \right\}\tag{12.27}
$$

有一个类似矢量点积（ $\mathbf{A} \cdot \mathbf{B} \equiv A_x B_x + A_y B_y + A_z B_z$ ）的4-矢量点积，但它不只是相同分量乘积的相加；而是它的第零分量的乘积还有一个负号：

$$
- a ^ {0} b ^ {0} + a ^ {1} b ^ {1} + a ^ {2} b ^ {2} + a ^ {3} b ^ {3}\tag{12.28}
$$

这就是四维标量积（four-dimensional scalar product）；你们可以自己验证（习题12.17）在所有的惯性系中它的值是一样的：

$$
- \bar {a} ^ {0} \bar {b} ^ {0} + \bar {a} ^ {1} \bar {b} ^ {1} + \bar {a} ^ {2} \bar {b} ^ {2} + \bar {a} ^ {3} \bar {b} ^ {3} = - a ^ {0} b ^ {0} + a ^ {1} b ^ {1} + a ^ {2} b ^ {2} + a ^ {3} b ^ {3}\tag{12.29}
$$

正如普通的点积在转动下是不变的 (不会改变)，这个点积在洛伦兹变换下也是不变的。

为了使负号明了，引入协变矢量（covariant） $a_{\mu}$ 是方便的，它与逆变矢量（contravariant） $a^{\mu}$ 的不同仅在于第零分量的符号上：

$$
a _ {\mu} = \left(a _ {0}, a _ {1}, a _ {2}, a _ {3}\right) \equiv \left(- a ^ {0}, a ^ {1}, a ^ {2}, a ^ {3}\right)\tag{12.30}
$$

你必须对指标的位置非常小心：上标表示逆变矢量；下标表示协变矢量。升或降时间分量的指标要改变正负号 $(a_{0}=-a^{0})$ ；升或降空间分量的指标没有变化 $(a_{1}=a^{1},a_{2}=a^{2},a_{3}=$

$a^3$ )。形式上

$$
a _ {\mu} = \sum_ {\nu = 0} ^ {3} g _ {\mu \nu} a ^ {\nu}, \quad \text {其中} \quad g _ {\mu \nu} \equiv \left( \begin{array}{c c c c} {- 1} & {0} & {0} & {0} \\ {0} & {1} & {0} & {0} \\ {0} & {0} & {1} & {0} \\ {0} & {0} & {0} & {1} \end{array} \right)\tag{12.31}
$$

此为闵可夫斯基度规（Minkowski metric） $^{12}$ 。

现在标量积可以写成和的形式，

$$
\sum_ {\mu = 0} ^ {3} a ^ {\mu} b _ {\mu}
$$

或更紧凑的形式，

$$
a ^ {\mu} b _ {\mu}\tag{12.32}
$$

[无论何时当一个希腊字母指标在一个乘积中重复出现时——一个是作为协变量，另一个是作为逆变量——就意味着求和。这称为爱因斯坦求和约定（Einstein summation convention），以发明者爱因斯坦命名，被爱因斯坦认为是他的最重要贡献之一。]当然，我们也要留心切换到协变量 $b$ 时的那个负号：

$$
a _ {\mu} b ^ {\mu} = a ^ {\mu} b _ {\mu} = - a ^ {0} b ^ {0} + a ^ {1} b ^ {1} + a ^ {2} b ^ {2} + a ^ {3} b ^ {3}\tag{12.33}
$$

习题 12.17 利用式 (12.27) 来验证式 (12.29)。[这仅证明了标量积对沿 x 方向的洛伦兹变换的不变性。但标量积在转动变换下也保持不变，因为第一项根本不受影响，最后三项由三维点积 $a \cdot b$ 构成。通过适当旋转，x 轴可指向任何方向，故四维标量积在任意洛伦兹变换下实际上是不变的。]

习题12.18

(a) 写出描述一个伽利略变换的矩阵 [式 (12.12)]。

(b) 写出描述一个沿 $y$ 轴的洛伦兹变换的矩阵。

（c）找出描述先以速度 $v$ 沿 $x$ 轴的洛伦兹变换，然后以速度 $\bar{v}$ 沿 $y$ 轴运动的洛伦兹变换的矩阵。施行这两个洛伦兹变换的次序有影响吗？

习题12.19 如果引进快度（rapidity）

$$
\theta \equiv \arctan (v / c)\tag{12.34}
$$

则旋转和洛伦兹变换的相似性会更加明显。

(a) 用 $\theta$ 表示洛伦兹变换矩阵 $\Lambda$ [式 (12.23)], 并把它与旋转矩阵比较 [式 (1.29)]。

在某些方面快度比速度描述运动更自然 $^{13}$ 。其中之一是它的范围从 $-\infty$ 到 $+\infty$ 而不是从 -c 到 c。更有意义的是快度是可加的，而速度是不可加的。

(b) 用快度表示爱因斯坦速度合成法则。

（ii）间隔不变性。4-矢量 $a^\mu$ 与其自身的标量积 $a^\mu a_\mu = -(a^0)^2 +(a^1)^2 +(a^2)^2 +(a^3)^2$ 可以正（如果空间部分占主导），或者负（如果时间部分占主导），或者零：

$$
\begin{array}{r l} & {{\mathrm{若} a ^ {\mu} a _ {\mu} > 0, a ^ {\mu} \mathrm{称为类空} (\mathrm{spacelike})}} \\ & {{\mathrm{若} a ^ {\mu} a _ {\mu} <   0, a ^ {\mu} \mathrm{称为类时} (\mathrm{timelike})}} \\ & {{\mathrm{若} a ^ {\mu} a _ {\mu} = 0, a ^ {\mu} \mathrm{称为类光} (\mathrm{lightlike})}} \end{array}
$$

假设事件 $A$ 发生在 $\left(x_A^0, x_A^1, x_A^2, x_A^3\right)$ ，事件 $B$ 发生在 $\left(x_B^0, x_B^1, x_B^2, x_B^3\right)$ 。它们的差

$$
\Delta x ^ {\mu} \equiv x _ {A} ^ {\mu} - x _ {B} ^ {\mu}\tag{12.35}
$$

称为位移 4-矢量（displacement 4-vector）。它自身的标量积是一个特别重要的量，我们称它为两事件的不变间隔（invariant interval）：

$$
I \equiv (\Delta x) ^ {\mu} (\Delta x) _ {\mu} = - \left(\Delta x ^ {0}\right) ^ {2} + \left(\Delta x ^ {1}\right) ^ {2} + \left(\Delta x ^ {2}\right) ^ {2} + \left(\Delta x ^ {3}\right) ^ {2} = - c ^ {2} t ^ {2} + d ^ {2}\tag{12.36}
$$

式中，t 是两事件的时间之差；d 是它们的空间距离。当变换到一个运动参考系中时，A 和 B 间的时间发生变化 $(\bar{t} \neq t)$ ，空间距离也发生变化 $(\bar{d} \neq d)$ ，但间隔 I 保持不变。

如果两个事件的位移是类时的 $(I < 0)$ ，则存在一惯性系（通过洛伦兹变换），两事件在这个惯性系中可在同一地点发生。因为如果我搭乘火车以速度 v = d/t 从（A）到（B），当事件 A 发生时离开 A，当事件 B 发生时我应该正好及时经过它。在火车这个参考系里，A 和 B 就发生在同一地点。对类空间隔无法这样做，因为那样的话需要 v 比 c 大，但没有观察者能超过光速（γ 会是虚数，洛伦兹变换没有意义）。另一方面，如果位移是类空的 $(I > 0)$ ，则存在一个参考系，在该参考系中两事件可同时发生（参看习题 12.21）。如果位移是类光的 $(I = 0)$ ，那么这两个事件可以通过光信号联系。

速度由斜率的倒数给出。静止的粒子由一条竖直线表示，以光速运动的光子由一条 $45^{\circ}$ 的斜线表示。以某个中间速度运行的火箭具有斜率（图12.21）。我们称这类图为闵可夫斯基图（Minkowski diagrams）。

在闵可夫斯基图中一个粒子的轨迹称为一个世界线（world line）。假设你在时刻 t=0 时从原点出发。因为没有物体的运动速度超过光速，你的世界线的斜率不会小于 1。这样，你的运动被限制在由两个 $45^{\circ}$ 线为边界的阴影楔形区内（图 12.22）。我们称这为你的“未来”，因为只有这些点你才可以到达。当然，随着时间的流逝，你沿着你选择的世界线运动，你的选择逐渐狭窄：在任何时刻你的未来是以你所处的地点构成的向前的楔形区。同时，“向后”的楔形区代表你的“过去”，因为你只能来自这个区域中的点。对于其他区域（在向前和向后的楔形区外），它只是广义的“存在”。你不能到达那里，也不能来自那里。事实上，你没有任何方法影响那里任何现存的事件（那样的话，信息传播的速度要大于光速）。这是一个你完全不能进入的巨大的时空区域。

![](images/d6474c82cedc4b11f669f119ac301accb21947953805f1e8d2a36f45bfcd05cc.jpg)  
图12.21

![](images/a7b8bdad51979bd38cd877d21873fefefd93b45d57b567c144a67b78c73ffbc8.jpg)  
图12.22

上面的讨论没有涉及 y 和 x 方向。如果包括垂直纸面的 y 轴，“楔形”就变成锥形——加上不能画出来的 z 轴，变成超圆锥。因为它们的边界是光线的轨迹，我们称它们为向前光锥（forward light cone）和向后光锥（backward light cone）。你的未来在向前的光锥中，而过去在向后的光锥中。

注意在空时图中，连接两个事件的线的斜率立刻告诉你它们的位移是类时的（斜率大于1），类空的（斜率小于1），还是类光的（等于1）。例如，相对于你现在位置的所有光锥内的过去和将来的点都是类时的，而在光锥外的点是类空的，光锥面上的点是类光的。

赫尔曼·闵可夫斯基首先认识到狭义相对论的几何意义，在他1908年的一个著名演讲中以这样的话开头，“从今以后，空间本身和时间本身都注定要逐渐消退成为阴影，只有两者的结合才能独立存在。” $^{14}$ 这是一个优美的思想，但你们必须小心不要读太多了，要恰当理解它。因为“时间就是一个与x,y,z同等地位的坐标”（除了因为不很清楚的原因，我们测量它用时钟而不是尺子）的说法并不完全准确。的确，时间与其他坐标完全不同，其标志是在不变间隔中的负号。这个负号赋予时空一种双曲几何，比三维空间的圆形几何有更丰富的内容。

在绕着 $z$ 轴旋转下， $xy$ 平面内的一点对应一个圆：圆上所有的点距原点的距离 $r = \sqrt{x^2 + y^2}$ （图12.23）相同。但在洛伦兹变换下，是位移 $I = (x^2 - c^2 t^2)$ 保持不变，对于一个给定的 $I$ 所有的点是一个双曲线——或，如果包含 $y$ 轴，则是旋转双曲面。当位移是类时的，它是一个“双叶双曲面”（图12.24a）；当位移是类空的，它是一个“单叶双曲面”（图12.24b）。当你进行洛伦兹变换（即，当你进入一个运动惯性系时），一个给定事件的坐标 $(x, t)$ 将变为 $(\bar{x}, \bar{t})$ ，但这些新坐标将和 $(x, t)$ 处在同一双曲面上。通过适当的洛伦兹变换与旋转的组合，在一个给定的双曲面上的一个点可以随意移动。但再多的变换也无法实现让类时双曲面的上叶一点移到下叶，或移到一个类空双曲面上。

![](images/011923d9104841e7d90f73184eaaf732f9f813b9b818c862548ce117e356e9cd.jpg)  
图12.23

![](images/79d844c1b8e3341c6794d1f63d85b4a51b9775fb04282119274674464b8b1316.jpg)  
图12.24

当我们讨论同时性时，我指出两个事件的时间顺序在某些情况下，当变换到另一个运动参考系中时会反转。但现在看来并不总是可能的：如果两个事件的位移4-矢量是类时的，它们的顺序是绝对的，如果间隔是类空的，它们的顺序依赖于观察者所在的参考系。在时空图中，在类时双曲面上叶上的一个事件确定地要在（0,0）后面发生，而下叶上的事件要早于（0,0）发生。但在类空双曲面上的事件，其发生可以在正的或者负的时刻 $t$ ，依赖于你所处的参考系。这不是一个无意义的问题，因为它挽救了因果律（causality）的概念，而因果律是所有物理的基石。如果总是可以使两事件的时间顺序反转，那么我们就不能说“A导致 B”，因为一个作为竞争对手的观察者会反驳说 B 先于 A。假如两个事件是类时间隔或者是类光间隔的，这种窘境就可以避免。因果律联系的事件是——非如此则影响不能从一个事件传播到另一个事件。结论：有因果关系的两个事件的位移总是类时的，它们的时间顺序对所有惯性系中的观察者都是相同的。

习题12.22

（a）画出时空图，表示两个静止的相距10英尺的人的一个投接球游戏（或一场交谈）。如果他们的间隔是类空的，他们怎样进行通信？

(b) 一个过去的五行打油诗这样写道：

从前有个女孩叫布莱特，

她跑得比光还快。

她在一天离开，

以爱因斯坦方法，

并在前天夜里回归。

你对此有什么想法？即使她能跑得速度超过光速，她会早于自己出发回来吗？她能早于自己出发前到达中途某点吗？画出这个旅行的时空图。

习题12.23 惯性系 $\overline{S}$ 沿 $x$ 方向相对于 $S$ 以 $\frac{3}{5} c$ 的速度运动。（沿 $x$ 轴运动，和通常一样原点在 $t = \bar{t} = 0$ 时重合。）

(a) 在图纸上建立一个以 $ct$ 和 $x$ 为轴的直角坐标系，仔细画线表示出 $\bar{x} = -3, -2, -1, 0, 1, 2,$ 和3。把对应 $c\bar{t} = -3, -2, -1, 0, 1, 2,$ 和3的线也画出来，并清楚地标出你画的线。

(b) 在 $\overline{S}$ 系，观察到自由粒子在时间 $c\bar{t} = -2$ ，从点 $\bar{x} = -2$ 运动到点 $\bar{x} = 2$ 于时刻 $c\bar{t} = +3$ 。在图中指出位移。从直线的斜率确定粒子在 $S$ 系中的速度。

(c) 利用速度合成法则用代数法确定在 $S$ 系中的速度，验证你的结果与（b）中用图形解出的结果一致。

## 12.2 相对论力学

## 12.2.1 固有时和固有速度

当你沿着世界线运动时，你的表变慢了。墙上的时钟走过了一段时间 dt，而你的表仅运行了 $d\tau$ ：

$$
\mathrm{d} \tau = \sqrt {1 - u ^ {2} / c ^ {2}} \mathrm{d} t\tag{12.37}
$$

（我用 u 表示特别的对象——你的速度，在这种情况下——v 是两惯性系的相对速度。）你的表显示的时间 $\tau$ （或更一般地，与运动物体相联系的时间）称为固有时（proper time）。（这个词来自一个法语 propre 的误译，意思是“自己”。）在一些情形下 $\tau$ 比 t 可能更相关或者更有用处。首先固有时是不变的，而“通常的”时间依赖于你考虑的参考系。

现在，设想你在一个飞往洛杉矶的飞机上，机长宣称飞机的速度是 $\frac{4}{5} c$ ，向南。他说的“速度”的精确含义是什么？当然，他的意思是位移除以时间：

$$
\boldsymbol {u} = \frac {\mathrm{d} \boldsymbol {l}}{\mathrm{d} t}\tag{12.38}
$$

因此，他说的大概是对地的相对速度，dl 和 dt 两个量都是地面上的观察者测得的。如果你关心你在洛杉矶的约会是否能准时，这确实是个重要数据。但如果你想知道你在飞行中是否饥饿，你也许对每单位固有时间走过的距离更感兴趣：

$$
\eta \equiv \frac {\mathrm{d} l}{\mathrm{d} \tau}\tag{12.39}
$$

这个混合的量——距离是地面上观察者测的，时间是在飞机上测的——称为固有速度（proper velocity）。作为对比，我将称 u 为平常速度（ordinary velocity）。两者由式 (12.37) 联系在一起：

$$
\eta = \frac {1}{\sqrt {1 - u ^ {2} / c ^ {2}}} u\tag{12.40}
$$

当然，对于速度远低于 c 的情形，平常速度与固有速度的差别可以忽略。

然而，从理论上来看，固有速度比平常速度具有巨大的优越性：当你从一个惯性系变换到另一个惯性系时，它的变换非常简单。事实上， $\eta$ 是一个4-矢量的空间部分，

$$
\eta^ {\mu} \equiv \frac {\mathrm{d} x ^ {\mu}}{\mathrm{d} \tau}\tag{12.41}
$$

它的第零分量是

$$
\eta^ {0} = \frac {\mathrm{d} x ^ {0}}{\mathrm{d} \tau} = c \frac {\mathrm{d} t}{\mathrm{d} \tau} = \frac {c}{\sqrt {1 - u ^ {2} / c ^ {2}}}\tag{12.42}
$$

分子 $\mathrm{d}x^{\mu}$ 是一个位移4-矢量，分母 $\mathrm{d}\tau$ 是不变量。故，例如，当你从 $S$ 系变换到以速率 $v$ 沿着公共的 $x\bar{x}$ 轴运动的 $\overline{S}$ 系，有

$$
\left. \begin{array}{l} \bar {\eta} ^ {0} = \gamma (\eta^ {0} - \beta \eta^ {1}) \\ \bar {\eta} ^ {1} = \gamma (\eta^ {1} - \beta \eta^ {0}) \\ \bar {\eta} ^ {2} = \eta^ {2} \\ \bar {\eta} ^ {3} = \eta^ {3} \end{array} \right\}\tag{12.43}
$$

更一般地，

$$
\bar {\eta} ^ {\mu} = \Lambda_ {\nu} ^ {\mu} \eta^ {\nu}\tag{12.44}
$$

称为固有速度 4-矢量（proper velocity 4-vector），或简称 4-速度（4-velocity）。

相比之下，平常速度的变换规则却非常烦琐，例题12.6及习题12.15给出结果：

$$
\left. \begin{array}{l} \bar {u} _ {x} = \frac {\mathrm{d} \bar {x}}{\mathrm{d} \bar {t}} = \frac {u _ {x} - v}{(1 - v u _ {x} / c ^ {2})} \\ \bar {u} _ {y} = \frac {\mathrm{d} \bar {y}}{\mathrm{d} \bar {t}} = \frac {u _ {y}}{\gamma (1 - v u _ {x} / c ^ {2})} \\ \bar {u} _ {z} = \frac {\mathrm{d} \bar {z}}{\mathrm{d} \bar {t}} = \frac {u _ {z}}{\gamma (1 - v u _ {x} / c ^ {2})} \end{array} \right\}\tag{12.45}
$$

变换复杂的原因很明显：我们对分子 $\mathrm{d}l$ 和分母 $\mathrm{d}t$ 都必须进行变换；而对固有速度分母 $\mathrm{d}\tau$ 是不变量，因此，该比率仅沿袭了分子的变换规则。

习题12.24

(a) 式 (12.39) 用平常速度定义了固有速度。反过来用 $\eta$ 表示 $u$ 。

(b) 固有速度和快度 [式 (12.34)] 有什么关系？假设速度沿着 $x$ 方向，求出以 $\theta$ 为变量的函数 $\eta$ 。

习题12.25 一辆轿车在 $S$ 系中沿 $45^{\circ}$ 线运动（图12.25），其（平常）速度为 $(2 / \sqrt{5})c$ 。

(a) 求（平常）速度的分量 $u_{x}$ 和 $u_{y}$ 。

(b) 求固有速度分量 $\eta_{x}$ 和 $\eta_{y}$ 。

(c) 求 4-速度矢量的第零分量 $\eta^{0}$ 。

$\overline{\mathcal{S}}$ 系以相对于 $\mathcal{S}$ 系的（平常）速度 $\sqrt{2 / 5c}$ 沿 $x$ 方向运动，利用适当的变换规则，

(d) 在 $\overline{S}$ 系求（平常）速度分量 $\bar{u}_{x}$ 和 $\bar{u}_{y}$ 。

(e) 在 $\overline{S}$ 系求固有速度分量 $\bar{\eta}_{x}$ 和 $\bar{\eta}_{y}$ 。

(f) 作为一致性的检验，验证

$$
\bar {\eta} = \frac {\overline {{{u}}}}{\sqrt {1 - \bar {u} ^ {2} / c ^ {2}}}
$$

![](images/5e038cd2963388de54c43cc2265fa7cad3114583e36693a8f33e1775679d07f8.jpg)  
图12.25

习题12.26 求4-速度自身的不变乘积 $\eta^{\mu}\eta_{\mu}$ 。 $\eta^{\mu}$ 是类空，类时，还是类光？

习题 12.27 一个警察把你拦下来，问你当时开多快。“好吧，警官，我不能撒谎：速度计显示 $4 \times 10^{8} \mathrm{~m/s}$ 。”他给你开罚单，因为这条高速公路限速 $2.5 \times 10^{8} \mathrm{~m/s}$ 。在法庭上，你的律师（幸运的是，他学过物理）指出，汽车的速度计测量的是固有速度，而限速是平常速度。你有罪还是无罪？

习题12.28 考虑一个粒子做双曲线运动，

$$
x (t) = \sqrt {b ^ {2} + (c t) ^ {2}}, \quad y = z = 0
$$

(a) 求作为 $t$ 的函数的固有时 $\tau$ ，设时钟为当 $t = 0$ 时， $\tau = 0$ 。[提示：积分式 (12.37)]

(b) 求作为 $\tau$ 的函数的 $x$ 和 $v$ (平常速度)。

(c) 求作为 $t$ 的函数的 $\eta^{\mu}$ （固有速度）。

## 12.2.2 相对论能量和动量

在经典力学中动量是质量乘以速度。我要把这个定义推广到相对论的情形，但立刻出现一个问题：我应当用平常速度还是固有速度？在经典力学中 $\eta$ 和 u 是相同的，因此，没有先验的理由倾向一方。但在相对论中我们要用固有速度，这是至关重要的。这是因为如果定义动量为 mu，则动量守恒和相对论原理会不一致（见习题 12.29）。所以

$$
\boxed {p \equiv m \eta = \frac {m u}{\sqrt {1 - u ^ {2} / c ^ {2}}}}\tag{12.46}
$$

这就是质量为 m 以（平常速度）u 运动物体的相对论动量（relativistic momentum） $^{15}$ 。相对论动量是 4-矢量，

$$
p ^ {\mu} \equiv m \eta^ {\mu}\tag{12.47}
$$

的空间部分。这样自然会问它的时间分量

$$
p ^ {0} = m \eta^ {0} = \frac {m c}{\sqrt {1 - u ^ {2} / c ^ {2}}}\tag{12.48}
$$

代表什么。爱因斯坦称 $p^{0}c$ 为相对论能量（relativistic energy）：

$$
\boxed {E \equiv \frac {m c ^ {2}}{\sqrt {1 - u ^ {2} / c ^ {2}}}}\tag{12.49}
$$

$p^{\mu}$ 称为能量-动量 4-矢量（energy-momentum 4-vector），或简称动量 4-矢量（momentum 4-vector）。

注意即使物体静止，相对论能量也不为零；我们称这为静止能量：

$$
E _ {\mathrm{rest.}} \equiv m c ^ {2}\tag{12.50}
$$

剩余的部分来自运动，称为动能（kinetic energy）：

$$
E _ {\mathrm{kin}} \equiv E - m c ^ {2} = m c ^ {2} \left(\frac {1}{\sqrt {1 - u ^ {2} / c ^ {2}}} - 1\right)\tag{12.51}
$$

对于非相对论情形 $(u\ll c)$ 方根可以展开成 $u^2 /c^2$ 的幂级数，给出

$$
E _ {\mathrm{kin}} = \frac {1}{2} m u ^ {2} + \frac {3}{8} \frac {m u ^ {4}}{c ^ {2}} + \dots\tag{12.52}
$$

第一项再次给出了经典力学公式。

到目前为止，这一切都只是符号。由式(12.46)和式(12.49)定义 $\pmb{p}$ 和 $E$ 是守恒的物理存在于实验事实中：

对任何封闭体系 $^{16}$ ，总的相对论能量和动量是守恒的。

质量不守恒——这是 1945 年以来每个人都熟知并感到痛苦的事实（尽管所谓的“质量能量转化”事实上是静止能量转化为动能）。

注意不变量（在所有惯性系值都相同）和守恒量（某些过程前后值保持不变）的区别。质量是不变量，但不是守恒量；能量是守恒量但不是不变量。电荷（正如我们将要看到的）既是守恒量也是不变量。速度既不是守恒量也不是不变量。

$p^{\mu}$ 自身的标积是

$$
p ^ {\mu} p _ {\mu} = - \left(p ^ {0}\right) ^ {2} + (\boldsymbol {p} \cdot \boldsymbol {p}) = - m ^ {2} c ^ {2}\tag{12.53}
$$

利用习题12.26的结果你可很快验证它。以相对论能量和动量表示，有

$$
\boxed {E ^ {2} - p ^ {2} c ^ {2} = m ^ {2} c ^ {4}}\tag{12.54}
$$

这个结果非常有用，因为不用求速度仅由此式就可计算 $E$ （如果知道 $p \equiv |\pmb{p}|$ ），或 $p$ （如果知道 $E)^{17}$ 。

习题12.29

(a) 用（不正确的）定义 $mu$ 及（正确的）爱因斯坦速度合成规则重做习题12.2。注意假如动量（这样定义的）在 $\mathcal{S}$ 系中守恒，它在 $\overline{\mathcal{S}}$ 系中不守恒。假设所有的运动沿 $x$ 轴。

(b) 现在用正确的定义 $m\eta$ 重新求解。注意如果动量（这样定义的）在 $\mathcal{S}$ 系中守恒，在 $\overline{\mathcal{S}}$ 系中它自动守恒。[提示：利用式 (12.43) 变换固有速度。] 对于相对论能量必须做何假设？

习题12.30 如果一个粒子的动能是它静止能量的 $n$ 倍，它的速度是多少？

习题 12.31 假设你有许多粒子，均沿 x 方向运动，能量为 $E_{1}, E_{2}, E_{3}, \cdots$ ，动量为 $p_{1}, p_{2}, p_{3}, \cdots$ 。求动量中心（center of momentum）参考系的速度，在这个参考系中总动量为零。

## 12.2.3 相对论运动学

在这部分我们将考察守恒律在粒子衰变和碰撞中的一些应用。

例题12.7 两块泥土，每块的（静止）质量为 $m$ ，以速度 $\frac{3}{5} c$ 迎面碰撞（图12.26）并粘在一起。问：粘在一起的泥块质量（ $M$ ）是多少？

![](images/f568bacca051a3d7925a843c7212e4184eb1a2ae26a15ab1c5526bd38988868a.jpg)  
(碰前)  
(碰后)  
图12.26

[解答] 在这个例子中动量守恒很平凡：碰撞前后动量均为零。碰撞前每个泥块的能量是

$$
\frac {m c ^ {2}}{\sqrt {1 - (3 / 5) ^ {2}}} = \frac {5}{4} m c ^ {2}
$$

碰撞后结合在一起的泥块的能量是 $Mc^2$ （因为它是静止的）。故由能量守恒得到

$$
\frac {5}{4} m c ^ {2} + \frac {5}{4} m c ^ {2} = M c ^ {2}
$$

所以

$$
M = \frac {5}{2} m
$$

注意这个质量大于最初的质量之和！质量在碰撞中不守恒，动能转化为了静止质量，所以质量增加了。在经典力学分析这类碰撞中，我们说动能转化成了热能——粘在一起的泥块比碰前的两泥块“热”。这在相对论图像中当然也是对的。但什么是热能？它是物体中所有的原子、分子的随机动能和势能的总和。相对论告诉我们这些微观能量都可用物体的质量表示：一个热的马铃薯比冷的重；一个压缩的弹簧比自由的重。差别不是很大——内能（U）对质量的贡献是 $U/c^{2}$ ，而 $c^{2}$ 按日常标准是一个很大的量。你在任何地方都找不到速度足够大的两个泥块以探测它们在碰撞时的质量不守恒。但在基本粒子世界，这个效应可以很明显。例如，当中性的 $\pi$ 介子（质量 $2.4\times10^{-28}kg$ ）衰变成一个电子和正电子（每个的质量为 $9.11\times10^{-31}kg$ ），静止能量——只保留了不到原来质量的1%——几乎全部转变成了动能。

在经典力学中，没有零质量 $(m = 0)$ 的粒子——其动能 $\left(\frac{1}{2} mu^2\right)$ 和动量（ $mu$ ）会是零，你不能对它施加力（ $F = ma$ ），所以（由牛顿第三定律）它对其他物体也不能施加力——就物理而言，它无足轻重。在相对论中，你或许认为情况也是如此：毕竟 $p$ 和 $E$ 仍然正比于 $m$ 。但仔细观察式 (12.46) 和式 (12.49) 可发现一个有价值的线索：如果 $u = c$ ，分子和分母均为零，使 $p$ 和 $E$ 不确定（零除以零）。所以，如果一个无质量的粒子运动的速度总是光速，它携带能量和动量是可能的。尽管式 (12.46) 和式 (12.49) 不足以确定 $E$ 和 $p$ ，但式 (12.54) 表明它们可通过下式联系起来：

$$
E = p c\tag{12.55}
$$

要不是因为在自然界至少存在一个无质量的粒子：光子 $^{18}$ ，我个人认为这个论证是一个玩笑。光子确实是以光速运动，且遵守式 $(12.55)^{19}$ 。它们迫使我们认真地对待它。[附带说明，你也许要问带较多能量的光子与较少能量的光子的区别——毕竟它们有相同的质量（零）和速度（c）。相对论没有回答这个问题，让人感到奇怪的是量子力学回答了这个问题：根据普朗克公式， $E = h\nu$ ，这里h是普朗克常量（Planck's constant）， $\nu$ 是频率。一个蓝光光子的能量比一个红光光子的能量大！]

(衰变前)

(衰变后)

图12.27

[解答] 在这种情况下

$$
E _ {\mathrm{衰变前}} = m _ {\pi} c ^ {2}, \qquad p _ {\mathrm{衰变前}} = 0
$$

$$
E _ {\mathrm{衰变后}} = E _ {\mu} + E _ {\nu}, \quad p _ {\mathrm{衰变后}} = p _ {\mu} + p _ {\nu}
$$

动量守恒要求 $p_{v} = -p_{\mu}$ ，能量守恒要求

$$
E _ {\mu} + E _ {\nu} = m _ {\pi} c ^ {2}
$$

现在，由式(12.55)，得 $E_{\mathrm{v}} = |\pmb{p}_{\mathrm{v}}|c$ ，而由式(12.54)，得 $|\pmb {p}_{\mu}| = \sqrt{E_{\mu}^{2} - m_{\mu}^{2}c^{4}} /c$ 。所以

$$
E _ {\mu} + \sqrt {E _ {\mu} ^ {2} - m _ {\mu} ^ {2} c ^ {4}} = m _ {\pi} c ^ {2}
$$

从上面方程解得

$$
E _ {\mu} = \frac {(m _ {\pi} ^ {2} + m _ {\mu} ^ {2}) c ^ {2}}{2 m _ {\pi}}
$$

在经典力学碰撞中动量和质量总是守恒的，但动能一般不守恒。“粘在一起”的碰撞中动能转化成热能；“爆炸”的碰撞中化学能（或一些其他形式的能）转化为动能。如果动能守恒，如两个台球的理想碰撞，我们称碰撞是弹性碰撞。在相对论情形，动量和总能量总是守恒的，但质量和动能一般不守恒。再一次，如果碰撞中动能守恒我们也称它为弹性（elastic）碰撞。在这种情况下静止能量（总能减去动能）也是守恒的，故质量也守恒。实际中这意味着碰撞后的粒子与碰撞前粒子相同。例题12.7、12.8是非弹性碰撞，下面这个例子是弹性碰撞。

例题12.9 康普顿散射。一个能量为 $E_0$ 的光子碰上一个静止的电子。作为散射角 $\theta$ 的函数，求出射光子的能量 $E$ （图12.28）。

(碰前)  
![](images/21b8f882ef4a9add39ee4f1dc7f5b5c49e5e7f33c945de9e8a02eaac1d4c2956.jpg)  
图12.28

[解答] “垂直”方向上的动量守恒给出 $p_{\mathrm{e}} \sin \phi = p_{\mathrm{p}} \sin \theta$ ，再因 $p_{\mathrm{p}} = E / c,$

$$
\sin \phi = \frac {E}{p _ {\mathrm{e}} c} \sin \theta
$$

“水平”方向上的动量守恒给出

$$
\frac {E _ {0}}{c} = p _ {\mathrm{p}} \cos \theta + p _ {\mathrm{e}} \cos \phi = \frac {E}{c} \cos \theta + p _ {\mathrm{e}} \sqrt {1 - \left(\frac {E}{p _ {\mathrm{e}} c} \sin \theta\right) ^ {2}}
$$

或者

$$
p _ {\mathrm{e}} ^ {2} c ^ {2} = \left(E _ {0} - E \cos \theta\right) ^ {2} + E ^ {2} \sin^ {2} \theta = E _ {0} ^ {2} - 2 E _ {0} E \cos \theta + E ^ {2}
$$

最后，由能量守恒

$$
\begin{array}{r} E _ {0} + m c ^ {2} = E + E _ {\mathrm{e}} = E + \sqrt {m ^ {2} c ^ {4} + p _ {\mathrm{e}} ^ {2} c ^ {2}} \\ = E + \sqrt {m ^ {2} c ^ {4} + E _ {0} ^ {2} - 2 E _ {0} E \cos \theta + E ^ {2}} \end{array}
$$

求解 $E$ ，我得出

$$
E = \frac {1}{(1 - \cos \theta) / m c ^ {2} + (1 / E _ {0})}\tag{12.56}
$$

用光子的波长表示结果会更简洁：

$$
E = h \nu = \frac {h c}{\lambda}
$$

所以

$$
\lambda = \lambda_ {0} + \frac {h}{m c} (1 - \cos \theta)\tag{12.57}
$$

量（h/mc）称为电子的康普顿波长（Compton wavelength）。

习题 12.32 求例题 12.8 中 $\mu$ 子的速度。

习题12.33 一个质量为 $m$ 的粒子，它的总能是静止能量的两倍。它与静止的全同粒子碰撞。如果它们结合在一起，复合粒子的质量是多少？速度是多少？

习题12.34 一个（静止）质量为 $m$ 、（相对论）动量为 $p = \frac{3}{4} mc$ 的中性 $\pi$ 介子衰变为两个光子。一个光子的出射方向与原来的 $\pi$ 介子运动方向一致，另一个沿相反方向。求出每个光子的（相对论）能量。

习题 12.35 过去，大多数粒子物理实验涉及静止靶：一个粒子（通常是质子或电子）加速到高能量 E，与静止的靶粒子碰撞（图 12.29a）。如果两个粒子都加速至能量 E，再让它们碰撞，则能获得更高的相对能量（用相同的加速器）（图 12.29b）。经典力学中，一个粒子相对于另一个粒子的能量 $\bar{E}$ 仅为 4E（为什么？）……增益不是特别高（仅为 E 的 4 倍）。但在相对论中可获得巨大的增益。假设两粒子有相同的质量 m，证明

$$
\bar {E} = \frac {2 E ^ {2}}{m c ^ {2}} - m c ^ {2}\tag{12.58}
$$

假设你使用 $E = 30\mathrm{GeV}$ 的质子（ $mc^2 = 1\mathrm{GeV}$ ）， $\bar{E}$ 是多少？这等于 $E$ 的多少倍？（ $1\mathrm{GeV} = 10^{9}\mathrm{eV}$ 。）[由于相对论增强效应，大多数现代基本粒子实验用对撞的束流（pair annihilation）代替固定靶。]

![](images/cb06500bd9f88210119fb4e1544f7645233c6ef9da4fe21b3c6797265b63b1e8.jpg)  
图12.29

习题12.36 在一个电子对湮灭（pair annihilation）实验中，动量为 $p_{\mathrm{e}}$ 的电子（质量 $m$ ）碰撞一静止的正电子（质量与电子相同，电荷符号相反）。它们湮灭时产生两个光子。（为何不能仅产生一个光子？）如果一个光子的出射方向与入射电子方向的夹角为 $60^{\circ}$ ，它的能量是多少？

## 12.2.4 相对论动力学

牛顿第一定律包含在相对性原理中。下面的形式的第二定律，

$$
\boxed {\boldsymbol {F} = \frac {\mathrm{d} \boldsymbol {p}}{\mathrm{d} t}}\tag{12.59}
$$

在相对论力学中依然成立，只要我们用相对论动量。

例题12.10 在恒定力作用下的运动。一个质量为 $m$ 的粒子受到一个恒定力 $F$ 作用。假如在时刻 $t = 0$ 它静止于原点并开始运动，求它作为时间函数的坐标 $(x)$ 。

[解答]

$$
\frac {\mathrm{d} p}{\mathrm{d} t} = F \Rightarrow p = F t + \mathrm{常数}
$$

但因在 $t = 0$ 时， $p = 0$ ，式中的常数必为零，所以

$$
p = \frac {m u}{\sqrt {1 - u ^ {2} / c ^ {2}}} = F t
$$

求解速度 $u$ ，我们得出

$$
u = \frac {(F / m) t}{\sqrt {1 + (F t / m c) ^ {2}}}\tag{12.60}
$$

式中的分子当然就是经典力学的解——如果 $(F / m)t\ll c$ ，这个近似是正确的。但相对论性的分母保证 $u$ 永远不会大于 $c$ 。事实上，当 $t\to \infty$ ， $u\to c$ 。

为了完成问题求解，我们得再次积分

$$
\begin{array}{r} x (t) = \frac {F}{m} \int_ {0} ^ {t} \frac {t ^ {\prime}}{\sqrt {1 + (F t ^ {\prime} / m c) ^ {2}}} \mathrm{d} t ^ {\prime} \\ = \left. \frac {m c ^ {2}}{F} \sqrt {1 + (F t ^ {\prime} / m c) ^ {2}} \right| _ {0} ^ {t} = \frac {m c ^ {2}}{F} \left[ \sqrt {1 + (F t / m c) ^ {2}} - 1 \right] \end{array}\tag{12.61}
$$

不同于经典的抛物线 $x(t) = (F / 2m)t^2$ ，这里得到的图形是一个双曲线（图12.30）。由于这个原因，在恒力作用下的运动常称为双曲运动（hyperbolic motion）。例如，一个置于均匀电场中的带电粒子的运动就是受恒力的运动。

![](images/57e061a7349958001d10a1c7f5f679909fcf4c8d247f8ced9916d4e635da8e1f.jpg)

与通常一样，功是力的线积分：

$$
W \equiv \int \boldsymbol {F} \cdot \mathrm{d} \boldsymbol {l}\tag{12.62}
$$

功-能定理（work-energy theorem）（“对粒子做的净功等于粒子增加的动能”）在相对论中成立：

$$
W = \int {\frac {\mathrm{d} \pmb {p}}{\mathrm{d} t}} \cdot \mathrm{d} \pmb {l} = \int {\frac {\mathrm{d} \pmb {p}}{\mathrm{d} t}} \cdot {\frac {\mathrm{d} \pmb {l}}{\mathrm{d} t}} \mathrm{d} t = \int {\frac {\mathrm{d} \pmb {p}}{\mathrm{d} t}} \cdot \pmb {u} \mathrm{d} t
$$

式中，

$$
\begin{array}{r l} & {\frac {\mathrm{d} \pmb {p}}{\mathrm{d} t} \cdot \pmb {u} = \frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {m \pmb {u}}{\sqrt {1 - u ^ {2} / c ^ {2}}}\right) \cdot \pmb {u}} \\ & {\qquad = \frac {m \pmb {u}}{(1 - u ^ {2} / c ^ {2}) ^ {3 / 2}} \cdot \frac {\mathrm{d} \pmb {u}}{\mathrm{d} t} = \frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {m c ^ {2}}{\sqrt {1 - u ^ {2} / c ^ {2}}}\right) = \frac {\mathrm{d} E}{\mathrm{d} t}} \end{array}\tag{12.63}
$$

故

$$
W = \int {\frac {\mathrm{d} E}{\mathrm{d} t}} \mathrm{d} t = E _ {\text {末}} - E _ {\text {始}}\tag{12.64}
$$

（因为静止能量是常数，这里用总能或是动能都可以。）

与前两个定律不同，牛顿第三定律一般不能推广到相对论的情形。的确，如果涉及的两个物体在空间上是分开的，第三定律与同时的相对性是不相容的。假如在某时刻 $t$ ， $A$ 对 $B$ 施加力 $\pmb {F}(t)$ ，在同一瞬时 $B$ 施加在 $A$ 上的力为 $-\pmb {F}(t)$ ，则在这个参考系中第三定律适用。但一个运动的观察者将会认为这两个大小相等方向相反的力不是同时发生的。因此在他的参考系中第三定律不成立。仅在两物体相互接触作用情形下，两个力施加在相同的物理地点（并且在恒力的平凡情形），第三定律才能保持成立。

因为力 F 是动量对平常时间的导数，当你从一个参考系变换到另一个参考系时，它与（平常）速度有相同的令人不快的行为：分子和分母都必须变换。所以 $^{20}$ ，

$$
\bar {F} _ {y} = \frac {\mathrm{d} \bar {p} _ {y}}{\mathrm{d} \bar {t}} = \frac {\mathrm{d} p _ {y}}{\gamma \mathrm{d} t - \frac {\gamma \beta}{c} \mathrm{d} x} = \frac {\mathrm{d} p _ {y} / \mathrm{d} t}{\gamma \left(1 - \frac {\beta}{c} \frac {\mathrm{d} x}{\mathrm{d} t}\right)} = \frac {F _ {y}}{\gamma (1 - \beta u _ {x} / c)}\tag{12.65}
$$

对 $z$ 分量类似有

$$
\bar {F} _ {z} = \frac {F _ {z}}{\gamma (1 - \beta u _ {x} / c)}
$$

x 分量更麻烦，

$$
\bar {F} _ {x} = \frac {\mathrm{d} \bar {p} _ {x}}{\mathrm{d} \bar {t}} = \frac {\gamma \mathrm{d} p _ {x} - \gamma \beta \mathrm{d} p ^ {0}}{\gamma \mathrm{d} t - \frac {\gamma \beta}{c} \mathrm{d} x} = \frac {\frac {\mathrm{d} p _ {x}}{\mathrm{d} t} - \beta \frac {\mathrm{d} p ^ {0}}{\mathrm{d} t}}{1 - \frac {\beta}{c} \frac {\mathrm{d} x}{\mathrm{d} t}} = \frac {F _ {x} - \frac {\beta}{c} \left(\frac {\mathrm{d} E}{\mathrm{d} t}\right)}{1 - \beta u _ {x} / c}
$$

我们计算式 (12.63) 中的 $\frac{\mathrm{d}E}{\mathrm{d}t}$ ; 并把结果代入上式得到

$$
\bar {F} _ {x} = \frac {F _ {x} - \beta (\pmb {u} \cdot \pmb {F}) / c}{1 - \beta u _ {x} / c}\tag{12.66}
$$

仅在一种特殊情况下这些方程才容易处理：如果粒子（瞬时）在 $S$ 系中静止，这样 $\pmb{u} = 0$ ，有

$$
\overline {{{{\boldsymbol {F}}}}} _ {\perp} = \frac {1}{\gamma} \boldsymbol {F} _ {\perp}, \quad \bar {F} _ {\parallel} = F _ {\parallel}\tag{12.67}
$$

即，F 平行于 $\overline{S}$ 运动方向的分量不变，垂直方向分量是 F 除以 $\gamma$ 。

你可能已经想到，类似于固有速度，我们可以通过引进“固有”力以避免 F 变换下的上述糟糕行为。固有力是动量对固有时求导，

$$
K ^ {\mu} \equiv \frac {\mathrm{d} p ^ {\mu}}{\mathrm{d} \tau}\tag{12.68}
$$

它称为闵可夫斯基力（Minkowski force）。很明显，它是一个4-矢量，因为 $p^{\mu}$ 是一个4-矢量而固有时是不变量。 $K^{\mu}$ 的空间部分通过下式与“平常”力相联系：

$$
\boldsymbol {K} = \left(\frac {\mathrm{d} t}{\mathrm{d} \tau}\right) \frac {\mathrm{d} \boldsymbol {p}}{\mathrm{d} t} = \frac {1}{\sqrt {1 - u ^ {2} / c ^ {2}}} \boldsymbol {F}\tag{12.69}
$$

而第零分量

$$
K ^ {0} = \frac {\mathrm{d} p ^ {0}}{\mathrm{d} \tau} = \frac {1}{c} \frac {\mathrm{d} E}{\mathrm{d} \tau}\tag{12.70}
$$

除了因子 1/c，它是（固有）比率——粒子能量以这比率增加——换句话说是传递给粒子的（固有）功率。

相对论动力学的公式可由平常力或者闵可夫斯基力表示。用后者表示的公式一般比较简洁，但因为在一个长距离的运动中我们对它的轨迹随“平常”时间的变化感兴趣，所有前者更加有用。当我们想把经典力的定律，如洛伦兹力，推广至相对论情形时，问题出现了：经典公式中的力是平常力还是闵可夫斯基力？换句话说，我们应该把公式写成

$$
\boldsymbol {F} = q (\boldsymbol {E} + \boldsymbol {u} \times \boldsymbol {B})
$$

还是

$$
\boldsymbol {K} = q (\boldsymbol {E} + \boldsymbol {u} \times \boldsymbol {B})
$$

呢？因为固有时和平常时在经典力学中是相同的，现在还没办法区分。实际上，洛伦兹力是一种平常力——稍后将解释原因，并给出如何构造电磁场的闵可夫斯基力。

例题12.11 一带电粒子在均匀磁场中的典型轨迹是回旋运动（cyclotron motion）（图12.31）。粒子受到的磁力指向中心，

$$
F = Q u B
$$

这提供了维持圆周运动的向心力。但是要注意——在狭义相对论中向心力不是像在经典力学中的那样为 $mu^2 / R$ ，而是如你可在图12.32中所见那样， $\mathrm{dp} = p \mathrm{d}\theta$ ，故

$$
F = \frac {\mathrm{d} p}{\mathrm{d} t} = p \frac {\mathrm{d} \theta}{\mathrm{d} t} = p \frac {u}{R}
$$

（当然，经典力学中，p=mu，所以 $F=mu^{2}/R$ 。）所以

$$
Q u B = p \frac {u}{R}
$$

$$
p = Q B R\tag{12.71}
$$

在这个形式中相对论回旋公式与非相对论公式 (5.3) 相同——唯一不同之处是现在 $p$ 是相对论动量。

![](images/650af55c740bb2eee9c82f1eb0bf05d48999d3698b994085fac68a605a054ee0.jpg)  
图12.31

![](images/9bb3816bf8e1640d379bbefb58172a363fbd95160c3493729e5161fe3999c4b3.jpg)

在经典力学中，相互作用粒子系统的总动量（P）可以表示为总质量（M）乘以质心速度：

$$
\boldsymbol {P} = M \frac {\mathrm{d} \boldsymbol {R} _ {\mathrm{m}}}{\mathrm{d} t}
$$

在相对论中，质量中心 $\left(R_{\mathrm{m}} = \frac{1}{M}\sum m_i\boldsymbol {r}_i\right)$ 被能量中心（center-of-energy， $R_{\mathrm{e}} = \frac{1}{E}\sum E_{i}r_{i},$

其中 $E$ 为总能量）取代， $M$ 被 $E / c^2$ 取代，

$$
\boldsymbol {P} = \frac {\boldsymbol {E}}{c ^ {2}} \frac {\mathrm{d} \boldsymbol {R} _ {\mathrm{e}}}{\mathrm{d} t}\tag{12.72}
$$

现在 P 包括所有形式的动量，而 E 包括所有形式的能量——不仅仅是力学的，也包括可能储存在场中的任何动量和能量 $^{21}$ 。

例题12.12 在例题8.3中我们看到储存在同轴线中场的动量不为零，即使同轴线本身是静止的。当时，这显得很矛盾。然而，能量正在从电池传输到电阻器，因此能量中心在运动。确实，如果电池在 $z = 0$ ，电阻在 $z = l$ ，则 $\pmb{R}_{\mathrm{e}} = (E_0\pmb {R}_0 + E_Rl\hat{z}) / E$ ，其中 $E_{R}$ 是电阻的能量， $E_0$ 是其余的能量， $\pmb{R}_0$ 是 $E_0$ 的能量中心，于是

$$
\frac {\mathrm{d} \boldsymbol {R} _ {\mathrm{e}}}{\mathrm{d} t} = \frac {(\mathrm{d} E _ {R} / \mathrm{d} t) l}{E} \hat {\boldsymbol {z}} = \frac {I V l}{E} \hat {\boldsymbol {z}}
$$

那么由式 (12.72)，总动量为

$$
P = \frac {I V l}{c ^ {2}} \hat {z}
$$

这正是如例题8.3所计算的储存在场中的动量。

如果你觉得这仍然很奇怪，想象一个鞋盒，里面有一块我们看不见的大理石。鞋盒是静止的，但大理石正从一端滚到另一端。这个系统有动力吗？是的，当然，即使鞋盒是静止的——大理石也有动量。在同轴电缆的情况下，没有实际的物体在运动（好吧，电子在运动，但它们中往一个方向去的和另一个方向去的一样多，于是它们的净动量为零），但能量从一端流向另一端。在相对论中，所有形式的运动能量，而不仅仅是静止能量（质量），都构成动量。“大理石”（在这个类比中）是电磁场，它传输能量，因此贡献动量……即使这些场本身是完全静态的 $^{22}$ !

下面例子中，能量中心静止，则总动量为零 [式 (12.72)]。但是静态电磁场确实携带动量，于是问题就是找出补偿的机械动量。

例题 12.13 作为一个磁偶极矩 m 的模型，考虑一个通有稳恒电流的矩形线框。把电流想象成在导线内无相互作用自由运动的电子流 I。当施加一个均匀电场时（图 12.33），在左边导线中的电荷加速，而在右边的减速 $^{23}$ 。求在线圈中所有电荷的总动量。

![](images/79e0479d410e148a83d59a18f2c7196377b68d5363671d3686a72af7a5510f3f.jpg)  
图12.33

[解答] 左边和右边部分的动量抵消，故只需考虑顶部和底部。顶部 $N_{+}$ 电荷以速度 $u_{+}$ 向右运动，底部 $N_{-}$ 电荷以（较慢的速度） $u_{-}$ 向左运动。电流 $(I = \lambda u)$ 在所有四段导线中都相同（否则电荷就会在某处聚集）；特别地，

$$
I = \frac {Q N _ {+}}{l} u _ {+} = \frac {Q N _ {-}}{l} u _ {-}, \quad \text {故} N _ {\pm} u _ {\pm} = \frac {I l}{Q}
$$

式中， $Q$ 是每个粒子的电荷， $l$ 是矩形的长度。按经典力学，单个粒子的动量 $\pmb {p} = M\pmb{u}$ （ $M$ 是质量），总动量是（向右边）

$$
p _ {\mathrm{经典}} = M N _ {+} u _ {+} - M N _ {-} u _ {-} = M \frac {I l}{Q} - M \frac {I l}{Q} = 0
$$

与所预期的相同（毕竟整个线圈作为一个整体是不动的）。但按相对论， $p=\gamma Mu$ ，我们得到

$$
p = \gamma_ {+} M N _ {+} u _ {+} - \gamma_ {-} M N _ {-} u _ {-} = \frac {M I l}{Q} \left(\gamma_ {+} - \gamma_ {-}\right)
$$

这不是零，因为上部分的粒子移动得快。

事实上，当左边导线中粒子向上运动时，得到的能量 $(\gamma Mc^2)$ 等于电场力做的功 $QEw$ ，其中 $w$ 是矩形的高度，故

$$
\gamma_ {+} - \gamma_ {-} = \frac {Q E w}{M c ^ {2}}
$$

所以

$$
p = \frac {I l E w}{c ^ {2}}
$$

但 $Ilw$ 是线圈的磁偶极矩；作为矢量， $m$ 指向纸面内， $p$ 指向右，所以

$$
\boldsymbol {p} = \frac {1}{c ^ {2}} (\boldsymbol {m} \times \boldsymbol {E})\tag{12.73}
$$

所有在电场中的磁偶极矩携带动量，尽管它不运动！这个所谓的隐藏的动量是严格的相对论效应，是纯力学上的。它与电磁场动量精确相消[式(8.45)] $^{24}$ 。

习题12.37 在经典力学中牛顿定律可写成更常用的形式 $F = ma$ 。在相对论方程中， $F = \mathrm{dp} / \mathrm{dt}$ ，不能这样简单地表示。证明它是如下形式：

$$
\boldsymbol {F} = \frac {m}{\sqrt {1 - u ^ {2} / c ^ {2}}} \left[ \boldsymbol {a} + \frac {\boldsymbol {u} (\boldsymbol {u} \cdot \boldsymbol {a})}{c ^ {2} - u ^ {2}} \right]\tag{12.74}
$$

式中，a 是平常加速度（ordinary acceleration）。

习题12.38 证明如果你起跑有力，且脚下受到一个恒定的力，你有可能比光线跑得更快。

习题12.39 固有加速度（proper acceleration）的定义如下：

$$
\alpha^ {\mu} \equiv \frac {\mathrm{d} \eta^ {\mu}}{\mathrm{d} \tau} = \frac {\mathrm{d} ^ {2} x ^ {\mu}}{\mathrm{d} \tau^ {2}}\tag{12.75}
$$

(a) 求 $\alpha^{0}$ 和 $\alpha$ ，用 u 和 a（平常加速度）表示。

(b) 用 u 和 a 表示 $\alpha_{\mu}\alpha^{\mu}$ 。

(c) 证明 $\eta^{\mu}\alpha_{\mu} = 0$ 。

(d) 写出牛顿第二定律方程 (12.68) 的闵可夫斯基形式，用 $\alpha^{\mu}$ 表示。求不变乘积 $K^{\mu}\eta_{\mu}$ 。

习题12.40 证明

$$
K _ {\mu} K ^ {\mu} = \frac {1 - \left(u ^ {2} / c ^ {2}\right) \cos^ {2} \theta}{1 - u ^ {2} / c ^ {2}} F ^ {2}
$$

式中， $\theta$ 是 u 和 F 间的夹角。

习题12.41 质量为 $m$ 、电荷为 $q$ 的粒子，在电磁场 $\pmb{E}$ 和 $\pmb{B}$ 的作用下以速度 $\pmb{u}$ 运动，证明其（平常）加速度由下式给出：

$$
\pmb {a} = \frac {q}{m} \sqrt {1 - u ^ {2} / c ^ {2}} \left[ \pmb {E} + \pmb {u} \times \pmb {B} - \frac {1}{c ^ {2}} \pmb {u} (\pmb {u} \cdot \pmb {E}) \right]
$$

[提示：利用式(12.74)。]

## 12.3 相对论电动力学

## 12.3.1 相对论中的磁现象

与牛顿力学不同，经典电动力学与狭义相对论已经相容。麦克斯韦方程和洛伦兹力定律适用于任一惯性系。当然，对于一个电磁现象，一个观察者会认为是电过程，而另一个观察者可能认为是磁过程，但他们预测的实际粒子的运动是相同的。洛伦兹和其他人在19世纪末研究了这个问题，但在某种程度上，他们没有解决这个问题，错误在于他们运用的是非相对论力学，而不是电动力学本身有问题。有了对牛顿力学的相对论修正，我们现在可以推导出完整而自洽的相对论电动力学理论形式。但需要强调的是对电动力学的法则没有丝毫修改——而仅是用凸显其相对论特性的符号来表示这些法则。我将利用洛伦兹变换重新推导那些我们在较早用较费力的方法推出的结果。但本节的主要目的是深刻理解电动力学的结构——以前看到的那些随意的无关联的定律在相对论的观点下呈现出一致和必然性。

首先从静电学和相对论来讨论为何必须有磁性这么一件事，并且特别是，不利用磁学定律能够计算通有电流的导线与运动电荷之间的磁力 $^{25}$ 。假设你有一个以速率 v 向右运行的带正电荷线，假设电荷彼此靠得很近，可认为是连续分布，线电荷密度是 $+\lambda$ 。在其上叠加一个线电荷密度为 $-\lambda$ 、以速率 v 向左运动的另一个带负电的线。这样，总的向右的净电流为

$$
I = 2 \lambda v\tag{12.76}
$$

同时，一个距离电荷线为 s、带电量为 q 的点电荷以速率 u < v 向右运动（图 12.34a）。因为在电荷线中正负电荷抵消，在这个参考系（S）中对点电荷没有静电力。

然而让我们在 $\overline{S}$ 系中来讨论这个问题，该参考系以速率 u 向右运动（图 12.34b）。在这个参考系中点电荷 q 静止。由爱因斯坦速度合成法则，正电荷线和负电荷线的速度是

$$
v _ {\pm} = \frac {v \mp u}{1 \mp v u / c ^ {2}}\tag{12.77}
$$

![](images/d9b20c651e90b6652aba08dc2d847456b0736289028f28ec1ce1ffcef34f0049.jpg)

![](images/a83a538282c1283e1372edc67c84525a703120658fe3efd63a20340b2c2c34f4.jpg)  
图12.34

因为 $v_{-}$ 比 $v_{+}$ 大，负电荷间的空间收缩比正电荷间的大，所以在这个参考系中导线携带有净的负电荷！事实上，

$$
\lambda_ {\pm} = \pm (\gamma_ {\pm}) \lambda_ {0}\tag{12.78}
$$

式中，

$$
\gamma_ {\pm} = \frac {1}{\sqrt {1 - v _ {\pm} ^ {2} / c ^ {2}}}\tag{12.79}
$$

$\lambda_{0}$ 是在静止参考系中正电荷线密度。这当然不同于 $\lambda$ ——在 S 中它们以速率 v 运动，故

$$
\lambda = \gamma \lambda_ {0}\tag{12.80}
$$

式中，

$$
\gamma = \frac {1}{\sqrt {1 - v ^ {2} / c ^ {2}}}\tag{12.81}
$$

通过一些运算 $\gamma_{\pm}$ 可取下面简单形式：

$$
\begin{array}{r l} & {\gamma_ {\pm} = \frac {1}{\sqrt {1 - \frac {1}{c ^ {2}} (v \mp u) ^ {2} \left(1 \mp v u / c ^ {2}\right) ^ {- 2}}} = \frac {c ^ {2} \mp u v}{\sqrt {(c ^ {2} \mp u v) ^ {2} - c ^ {2} (v \mp u) ^ {2}}}} \\ & {\quad = \frac {c ^ {2} \mp u v}{\sqrt {(c ^ {2} - v ^ {2}) (c ^ {2} - u ^ {2})}} = \gamma \frac {1 \mp u v / c ^ {2}}{\sqrt {1 - u ^ {2} / c ^ {2}}}} \end{array}\tag{12.82}
$$

这样，在 $\overline{S}$ 系中导线上净电荷密度是

$$
\lambda_ {\text {总}} = \lambda_ {+} + \lambda_ {-} = \lambda_ {0} (\gamma_ {+} - \gamma_ {-}) = \frac {- 2 \lambda u v}{c ^ {2} \sqrt {1 - u ^ {2} / c ^ {2}}}\tag{12.83}
$$

结论：由于正线电荷和负线电荷洛伦兹收缩不同，导致在一个惯性系中呈电中性的载流导线在另一参考系中带电了。

现在一个线电荷 $\lambda_{总}$ 产生一个电场

$$
E = \frac {\lambda_ {\text {总}}}{2 \pi \varepsilon_ {0} S}
$$

故在 $\overline{S}$ 系中可观察到对 $q$ 有一电场力，即

$$
\bar {F} = q E = - \frac {\lambda v}{\pi \varepsilon_ {0} c ^ {2} s} \frac {q u}{\sqrt {1 - u ^ {2} / c ^ {2}}}\tag{12.84}
$$

但如果在 $\overline{S}$ 系中对 q 有一个力，在 S 系中必也有一个力。事实上我们可以通过力的变换定理来计算它。因为 q 在参考系 $\overline{S}$ 中静止， $\bar{F}$ 垂直于 u，在 S 系中的力由式 (12.67) 给出，

$$
F = \sqrt {1 - u ^ {2} / c ^ {2}} \bar {F} = - \frac {\lambda v}{\pi \varepsilon_ {0} c ^ {2}} \frac {q u}{s}\tag{12.85}
$$

在 $\overline{S}$ 系中电荷对线的吸引是纯粹的静电力（这里线是带电的，点电荷 q 静止），但在 S 系中显然是非静电力（这里线是中性的）。把它们结合起来，静电力学和相对论暗示这存在另一个力。这“另一个力”当然就是磁力。事实上，我们利用 $c^{2} = (\varepsilon_{0}\mu_{0})^{-1}$ 及把 $\lambda v$ 用电流表示 [式 (12.76)]，可以把式 (12.85) 变成更熟悉的形式，

$$
F = - q u \left(\frac {\mu_ {0} I}{2 \pi s}\right)\tag{12.86}
$$

式中，括号中的项是长直导线的磁场，得到的力与在 $S$ 系中用洛伦兹力定律得到的结果完全一样。

## 12.3.2 场如何变换

在各种特别情形中，我们知道一个观察者看到的是电场，对另一个观察者则是磁场。知道一般的电磁场变换规律将是有益的：在 S 系中的场，在 $\overline{S}$ 中是什么？你最初的猜测也许认为 E 是一个 4-矢量的空间部分，B 是另一个 4-矢量的空间部分。但你的猜测是错误的——实际比这要复杂。让我们明确一个假定，这个假定在 12.3.1 节作为暗含的假定已经用过：电荷是不变量。像质量那样，但与能量不一样，粒子的电荷是一个固定数值，不依赖于它运动多快。我们也将假定不论场是怎样产生的，变换规律相同——变化的磁场产生的电场与静止电荷产生的电场变换规律相同。如果不是这样的话，我们就不得不完全放弃场公式，因为场论的本质是在给定点的场告知你该点的电磁学全部信息。你不必附加有关其源的额外信息。

为此，考虑最简单的可能电场：一个大的平行板电容器两板间的均匀电场（图12.35a）。设电容器在 $S_0$ 中静止，面电荷密度是 $\pm \sigma_0$ ，则

$$
\pmb {E} _ {0} = \frac {\sigma_ {0}}{\varepsilon_ {0}} \hat {\pmb {y}}\tag{12.87}
$$

但该电容器在以 $v_{0}$ 的速率向右运动的参考系 $\mathcal{S}$ 中的情形如何（图12.35b）？在这个参考系中电容器板向左运动，但场仍然取下面的形式：

$$
\boldsymbol {E} = \frac {\sigma}{\varepsilon_ {0}} \hat {\boldsymbol {y}}\tag{12.88}
$$

唯一的不同是面电荷密度 $\sigma$ 。[等一等！这是仅有的不同吗？平行板电容器公式 $E = \sigma / \varepsilon_0$ 来自高斯定理。而对于运动电荷高斯定理是有效的，此处的应用也依赖于对称性。我们确信场依然垂直于板吗？如果场倾斜，比如说向运动方向倾斜（图 12.35c）会怎样？即使确实倾斜（它不倾斜），平行板间的场，因其由 $+\sigma$ 和 $-\sigma$ 面电荷的场叠加产生，还会是垂直于板面的。因为 $-\sigma$ 场的方向如图 12.35c（电荷负号变化使场的方向反转）所示，取矢量和，则平行方向分量抵消。]

![](images/08ad6eff9aa821791c2d6ffa8377081dc481bbbbf8c0d74e47f37724c36baad6.jpg)  
图12.35

现在在每个板上的总电荷不变，宽度（w）不变，但长度（l）因洛伦兹收缩变小，因子为

$$
\gamma_ {0} = \frac {1}{\sqrt {1 - v _ {0} ^ {2} / c ^ {2}}}\tag{12.89}
$$

故单位面积电荷增加了因子 $\gamma_{0}$ :

$$
\sigma = \gamma_ {0} \sigma_ {0}\tag{12.90}
$$

因而

$$
\pmb {E} ^ {\perp} = \gamma_ {0} \pmb {E} _ {0} ^ {\perp}\tag{12.91}
$$

标记上标符号 $\perp$ 是为了清楚说明这个规则只对 $E$ 垂直于 $S$ 系运动方向分量起作用。为了得到平行分量的情况，考虑电容器平行板平行于 $yz$ 面（图12.36）。这种情况下，平板间距（ $d$ ）将洛伦兹收缩， $l$ 和 $w$ （所以也即面电荷密度 $\sigma$ ）在两参考系中是相同的。因为场不

依赖于距离 $d$ ，有

$$
E ^ {\parallel} = E _ {0} ^ {\parallel}\tag{12.92}
$$

![](images/7b3de12c539f49571e6461ce1a15e433f3b0bbd7dea5a1cd5c68d31089277dae.jpg)  
图12.36

例题12.14 匀速运动点电荷的电场。一个电量为 $q$ 的点电荷静止于参考系 $\mathcal{S}_0$ 中的坐标原点。问题：这个电荷的电场在 $\mathcal{S}$ 系中情形如何， $\mathcal{S}$ 系以速率 $v_0$ 相对于 $\mathcal{S}_0$ 系向右运动？[解答] 在 $\mathcal{S}_0$ 系中，场为

$$
\pmb {E} _ {0} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q}{r _ {0} ^ {2}} \hat {\pmb {r}} _ {0}
$$

或者

$$
\left\{ \begin{array}{l} E _ {x 0} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q x _ {0}}{(x _ {0} ^ {2} + y _ {0} ^ {2} + z _ {0} ^ {2}) ^ {3 / 2}} \\ E _ {y 0} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q y _ {0}}{(x _ {0} ^ {2} + y _ {0} ^ {2} + z _ {0} ^ {2}) ^ {3 / 2}} \\ E _ {z 0} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q z _ {0}}{(x _ {0} ^ {2} + y _ {0} ^ {2} + z _ {0} ^ {2}) ^ {3 / 2}} \end{array} \right.
$$

由变换规则 [式 (12.91) 和式 (12.92)]，我们有

$$
\left\{ \begin{array}{l} E _ {x} = E _ {x 0} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q x _ {0}}{(x _ {0} ^ {2} + y _ {0} ^ {2} + z _ {0} ^ {2}) ^ {3 / 2}} \\ E _ {y} = \gamma_ {0} E _ {y 0} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {\gamma_ {0} q y _ {0}}{(x _ {0} ^ {2} + y _ {0} ^ {2} + z _ {0} ^ {2}) ^ {3 / 2}} \\ E _ {z} = \gamma_ {0} E _ {z 0} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {\gamma_ {0} q z _ {0}}{(x _ {0} ^ {2} + y _ {0} ^ {2} + z _ {0} ^ {2}) ^ {3 / 2}} \end{array} \right.
$$

式中，场点（P）仍是用 $S_{0}$ 系中的坐标 $(x_{0}, y_{0}, z_{0})$ 表示的，我更喜欢用 S 系中的 P 点坐标表示。由洛伦兹变换（或，实际上是逆变换），

$$
\left\{ \begin{array}{l} x _ {0} = \gamma_ {0} (x + v _ {0} t) = \gamma_ {0} R _ {x} \\ y _ {0} = y = R _ {y} \\ z _ {0} = z = R _ {z} \end{array} \right.
$$

式中， $R$ 是从 $q$ 到 $P$ 的矢量（图12.37），于是

$$
\begin{array}{r} \pmb {E} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {\gamma_ {0} q \pmb {R}}{\left(\gamma_ {0} ^ {2} R ^ {2} \cos^ {2} \theta + R ^ {2} \sin^ {2} \theta\right) ^ {3 / 2}} \\ = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q \left(1 - v _ {0} ^ {2} / c ^ {2}\right)}{\left[ 1 - (v _ {0} ^ {2} / c ^ {2}) \sin^ {2} \theta \right] ^ {3 / 2}} \frac {\hat {\pmb {R}}}{R ^ {2}} \end{array}\tag{12.93}
$$

![](images/528051cb67cb9fb1079e3e17e6c91928ac6b3c730c85f8360b80a8a900d21099.jpg)  
图12.37

这就是匀速运动电荷的场；我们在第10章用推迟势[式(10.75)]得到相同的结果。现在这个推导远比以前的更有效，并揭示了一个显著的事实，即场指向远离电荷的瞬时（而不是推迟）位置：从坐标的洛伦兹变换得出 $E_{x}$ 附带一个因子 $\gamma_0$ ， $E_{y}$ 和 $E_{z}$ 通过场的变换得到它们的形式。正是由于这两个 $\gamma_0$ 的平衡使 $\pmb{E}$ 平行于 $\pmb{R}$ 。

但式 (12.91) 和式 (12.92) 不是变换规则最一般的形式，因为我们由电荷静止的 $S_0$ 系开始，从而没有磁场。为了推导出一般的法则，我们必须从既有电场又有磁场的参考系出发。对此目的，考虑 $S$ 系很合适。除了电场

$$
E _ {y} = \frac {\sigma}{\epsilon_ {0}}\tag{12.94}
$$

由于有表面电流（图 12.35b），

$$
\pmb {K} _ {\pm} = \mp \sigma v _ {0} \hat {\pmb {x}}\tag{12.95}
$$

还有磁场。根据右手定则，磁场方向沿负 $z$ 方向，大小由安培定律给出（例5.8），

$$
B _ {z} = - \mu_ {0} \sigma v _ {0}\tag{12.96}
$$

在第三个参考系 $\overline{S}$ 中——该参考系相对 $S$ 系以速率 $v$ 向右运动（图12.38），场强是

$$
\bar {E} _ {y} = \frac {\bar {\sigma}}{\epsilon_ {0}}, \quad \bar {B} _ {z} = - \mu_ {0} \bar {\sigma} \bar {v}\tag{12.97}
$$

式中， $\bar{v}$ 是 $\overline{S}$ 相对于 $S_0$ 的速度：

$$
\bar {v} = \frac {v + v _ {0}}{1 + v v _ {0} / c ^ {2}}, \quad \bar {\gamma} = \frac {1}{\sqrt {1 - \bar {v} ^ {2} / c ^ {2}}}\tag{12.98}
$$

而

$$
\bar {\sigma} = \bar {\gamma} \sigma_ {0}\tag{12.99}
$$

![](images/b216d90f357bf0b40958410433a750da023e0f428e1ff7612548f6bd5d55fa79.jpg)  
图12.38

剩下的只是用 E 和 B [式 (12.94) 和式 (12.96)] 表示 $\bar{E}$ 和 $\bar{B}$ [式 (12.97)]。观察式 (12.90) 和式 (12.99)，我们有

$$
\bar {E} _ {y} = \left(\frac {\bar {\gamma}}{\gamma_ {0}}\right) \frac {\sigma}{\epsilon_ {0}}, \quad \bar {B} _ {z} = - \left(\frac {\bar {\gamma}}{\gamma_ {0}}\right) \mu_ {0} \sigma \bar {v}\tag{12.100}
$$

通过简单的代数运算，你就可以证明

$$
\frac {\bar {\gamma}}{\gamma_ {0}} = \frac {\sqrt {1 - v _ {0} ^ {2} / c ^ {2}}}{\sqrt {1 - \bar {v} ^ {2} / c ^ {2}}} = \frac {1 + v v _ {0} / c ^ {2}}{\sqrt {1 - v ^ {2} / c ^ {2}}} = \gamma \left(1 + \frac {v v _ {0}}{c ^ {2}}\right)\tag{12.101}
$$

与通常一样，式中，

$$
\gamma = \frac {1}{\sqrt {1 - v ^ {2} / c ^ {2}}}\tag{12.102}
$$

所以，用 S 系的 E 和 B 表示 $\bar{E}_{y}$ :

$$
\bar {E} _ {y} = \gamma \left(1 + \frac {v v _ {0}}{c ^ {2}}\right) \frac {\sigma}{\epsilon_ {0}} = \gamma \left(E _ {y} - \frac {v}{c ^ {2} \epsilon_ {0} \mu_ {0}} B _ {z}\right)
$$

而

$$
\bar {B} _ {z} = - \gamma \left(1 + \frac {v v _ {0}}{c ^ {2}}\right) \mu_ {0} \sigma \left(\frac {v + v _ {0}}{1 + v v _ {0} / c ^ {2}}\right) = \gamma \left(B _ {z} - \mu_ {0} \epsilon_ {0} v E _ {y}\right)
$$

或者，因为 $\mu_0\epsilon_0 = 1 / c^2$

$$
\left. \begin{array}{l} \bar {E} _ {y} = \gamma (E _ {y} - v B _ {z}) \\ \bar {B} _ {z} = \gamma (B _ {z} - \frac {v}{c ^ {2}} E _ {y}) \end{array} \right\}\tag{12.103}
$$

这告诉我们 $E_{y}$ 和 $B_{z}$ 如何变换——对于 $E_{z}$ 和 $B_{y}$ 只要把平行板电容器从平行于 $xz$ 平面变成平行于 $xy$ 平面即可（图12.39）。在 $\mathcal{S}$ 系中场为

$$
E _ {z} = \frac {\sigma}{\epsilon_ {0}}, B _ {y} = \mu_ {0} \sigma v _ {0}
$$

（利用右手定则得出 $B_{y}$ 的符号。）其余的讨论都是相同的——在以前是 $E_{y}$ 的地方变成 $E_{z}$ ，在以前是 $B_{z}$ 的地方变成 $-B_{y}$ ：

$$
\left. \begin{array}{l} \bar {E} _ {z} = \gamma (E _ {z} + v B _ {y}) \\ \bar {B} _ {y} = \gamma (B _ {y} + \frac {v}{c ^ {2}} E _ {z}) \end{array} \right\}\tag{12.104}
$$

![](images/921d4a7f2e80fe57b1617d121fd76425ae1aef794a6b695a5a9e13877b22296d.jpg)  
图12.39

对于 x 分量，我们已经看到（通过改变电容器的方向平行于 yz 面）

$$
\bar {E} _ {x} = E _ {x}\tag{12.105}
$$

因为在这个例子中没有伴随的磁场，不能推出 $B_{x}$ 的变换法则。但另一个构型可解决这个问题：设想一个平行于 $x$ 轴的长直螺线管（图12.40），在 $\mathcal{S}$ 系中静止。在螺线管内的磁场是

$$
B _ {x} = \mu_ {0} n I\tag{12.106}
$$

![](images/9f95b8d3165e55d15240cf15c345d812aebcfe6eb0d91bf00776fb741ee51b8e.jpg)  
图12.40

式中，n 是单位长度上的匝数；I 是电流。在 $\overline{S}$ 系中，长度收缩，故 n 增大，

$$
\bar {n} = \gamma n\tag{12.107}
$$

另一方面，时间延缓：S 系的钟沿着螺线管运动，它会变慢。故在 $\overline{S}$ 系中，电流（单位时间内流过的电荷）是

$$
\bar {I} = \frac {1}{\gamma} I\tag{12.108}
$$

两个 $\gamma$ 因子正好消去，得到

$$
\bar {B} _ {x} = B _ {x}
$$

与 E 相同，B 平行于运动方向的分量保持不变。

现在把所有的变换规则写在一起：

$$
\boxed { \begin{array}{r l r} & {\bar {E} _ {x} = E _ {x},} & {\bar {E} _ {y} = \gamma \left(E _ {y} - v B _ {z}\right), \qquad \bar {E} _ {z} = \gamma \left(E _ {z} + v B _ {y}\right)} \\ & {\bar {B} _ {x} = B _ {x},} & {\bar {B} _ {y} = \gamma \left(B _ {y} + \frac {v}{c ^ {2}} E _ {z}\right), \quad \bar {B} _ {z} = \gamma \left(B _ {z} - \frac {v}{c ^ {2}} E _ {y}\right)} \end{array} }\tag{12.109}
$$

两种特殊的情况要特别注意：

1. 假如在 S 系中 B = 0，则

$$
\overline {{{{\pmb {B}}}}} = \gamma \frac {v}{c ^ {2}} \left(E _ {z} \hat {\pmb {y}} - E _ {y} \hat {\pmb {z}}\right) = \frac {v}{c ^ {2}} \left(\bar {E} _ {z} \hat {\pmb {y}} - \bar {E} _ {y} \hat {\pmb {z}}\right)
$$

或，因为 $v = v \hat{x}$ ,

$$
\boxed {\overline {{B}} = - \frac {1}{c ^ {2}} (\boldsymbol {v} \times \overline {{E}})}\tag{12.110}
$$

2. 假如在 S 系中 E = 0，那么

$$
\overline {{{\boldsymbol {E}}}} = - \gamma v \left(B _ {z} \hat {\boldsymbol {y}} - B _ {y} \hat {\boldsymbol {z}}\right) = - v \left(\bar {B} _ {z} \hat {\boldsymbol {y}} - \bar {B} _ {y} \hat {\boldsymbol {z}}\right)
$$

或

$$
\boxed {\overline {{\boldsymbol {E}}} = \boldsymbol {v} \times \overline {{\boldsymbol {B}}}}\tag{12.111}
$$

换句话说，如果在一个参考系中 E 或 B 中任一个为零（在一特殊点），那么在任何其他参考系中场（在那个点处）由式 (12.110) 或式 (12.111) 简单联系起来。

例题12.15 匀速运动点电荷的磁场。求以速度 $v$ 匀速运动的点电荷 $q$ 的磁场。

[解答] 在电荷静止的参考系 $(S_{0})$ 中，磁场为零（任何地方），故在以速度 -v 向右运动的 S 系中（在其中粒子以速度 v 运动） $^{26}$

$$
\boldsymbol {B} = \frac {1}{c ^ {2}} (\boldsymbol {v} \times \boldsymbol {E})
$$

在例题12.14中，我们计算了电场。这样磁场为

$$
B = \frac {\mu_ {0}}{4 \pi} \frac {q v (1 - v ^ {2} / c ^ {2}) \sin \theta}{[ 1 - (v ^ {2} / c ^ {2}) \sin^ {2} \theta ] ^ {3 / 2}} \frac {\hat {\phi}}{R ^ {2}}\tag{12.112}
$$

式中， $\hat{\phi}$ 为当你面对运动过来的电荷的逆时针方向。顺便提及，在非相对论情形（ $v^{2} \ll c^{2}$ ），式(12.112)简化为

$$
B \approx \frac {\mu_ {0}}{4 \pi} q \frac {\pmb {v} \times \hat {\pmb {R}}}{R ^ {2}}
$$

这与你对点电荷简单地运用毕奥-萨伐尔定律所得到的结果 [式 (5.43)] 完全相同。

习题12.42 为何图12.35b中的电场没有 $z$ 分量？毕竟磁场有 $z$ 分量。

习题12.43 一个平行板电容器在 $S_0$ 系中静止，板面与 $x_0$ 轴倾斜成 $45^{\circ}$ 角，两板的电荷密度是 $\pm \sigma_0$ （图12.41）。参考系 $S$ 相对于 $S_0$ 以速率 $v$ 向右运动。

(a) 求在 $S_{0}$ 系中的场 $E_{0}$ 。

(b) 求在 S 系中的场 E。

(c) 板面与 $x$ 轴的夹角是多少？

(d) 在 S 系中，场垂直于板面吗？

![](images/50d1a34983468ddd3550305c111b260bc9ca1c144cb8fe29d9d57ce1efb1c8a7.jpg)  
图12.41

习题 12.44 在 $S_{0}$ 系的 z 轴有均匀分布的密度为 $\lambda$ 线电荷。

(a) 用直角坐标写出 $(x_0, y_0, z_0)$ 点的电场强度 $E_0$ 。

(b) S 系以速率 v 相对于 $S_{0}$ 系沿 x 方向运动，利用式 (12.109) 求 S 系中的电场强度。该场强还是用 $(x_{0}, y_{0}, z_{0})$ 表示的，改用 S 系的坐标 $(x, y, z)$ 表示。最后，将场强 E 用到导线当前位置的矢量 S 和 S 与 $\hat{x}$ 之间的角度 $\theta$ 表示。该场强是否指向远离电线的瞬时位置，类似匀速运动点电荷的场？

习题12.45

(a) 电荷 $q_{A}$ 在 $\mathcal{S}$ 系中静止在原点；电荷 $q_{B}$ 以速率 $v$ 沿着平行于 $x$ 轴的直线运动，直线距 $x$ 轴距离为 $y = d$ 。求当 $q_{B}$ 经过 $y$ 轴时它受到的电磁力是多大？

（b）现在从 $\overline{S}$ 系考虑同样问题。 $\overline{S}$ 系以速率 $v$ 向右运动。求当 $q_{A}$ 经过 $\bar{y}$ 轴时，作用在 $q_{B}$ 上的力是多大？[用两种方法求解：（i）用（a）求出的结果，通过力的变换求解；（ii）在 $\overline{S}$ 系中计算场，用洛伦兹力公式求解。]

习题12.46 两电荷 $\pm q$ ，以速率 $v$ 反方向运动，相距为 $d$ 。我们对它们交汇瞬间（图12.42）- $q$ 对 $+q$ 的作用力感兴趣。填充下面表格，并检验它们的一致性。

<table><tr><td></td><td>A 参考系(图 12.42 )</td><td>B 参考系(+q 静止)</td><td>C 参考系(-q 静止)</td></tr><tr><td>-q 在 +q 激发的 E</td><td></td><td></td><td></td></tr><tr><td>-q 在 +q 激发的 B</td><td></td><td></td><td></td></tr><tr><td>-q 对 +q 的 F</td><td></td><td></td><td></td></tr></table>

![](images/37406106153ec8da9881e97375c0e926dfe8edda92f40417694f96ca502fcfe9.jpg)  
图12.42

习题12.47

(a) 证明 $(\pmb{E} \cdot \pmb{B})$ 是相对论不变量。

(b) 证明 $\left(E^{2} - c^{2}B^{2}\right)$ 是相对论不变量。

(c) 假设在一个惯性系中 $B = 0$ ，但 $E \neq 0$ （在某点 $P$ ）。有没有可能找到另一个参考系，在这个系中使得 $P$ 点电场为零？

习题12.48 （角）频率为 $\omega$ 的平面电磁波沿 $x$ 轴方向在真空中传播。它的偏振方向沿 $y$ 轴，电场振幅为 $E_0$ 。

(a) 写出电场 $E(x, y, z, t)$ 和磁场 $B(x, y, z, t)$ 。[对你引入的任何辅助量都要以 $\omega, E_0$ 和自然常数进行定义。]

(b) 在相对于 $S$ 系以速率 $v$ 沿 $x$ 轴运动的惯性系 $\overline{S}$ 中，观察同样的这个波，求在 $\overline{S}$ 系中的电场和磁场，并用 $\overline{S}$ 系中的坐标表示它们： $\bar{E}(x, y, z, t)$ 和磁场 $\bar{B}(x, y, z, t)$ 。[同样要定义你引入的任何辅助量。]

(c) 在 $\overline{S}$ 系中的波的频率 $\bar{\omega}$ 是多少？解释这个结果。在 $\overline{S}$ 系中的波的波长 $\bar{\lambda}$ 是多少？由 $\bar{\omega}$ 和 $\bar{\lambda}$ 求 $\overline{S}$ 系中波的速度。结果与你的预期一样吗？

(d) $\overline{S}$ 系中的波强度与 $S$ 系的波强度的比值是多少？年青的爱因斯坦对这样的事情感到好奇：当你能以光速在电磁波旁边奔跑时，电磁波看上去像什么。当 $v$ 接近 $c$ 时，关于波的波幅、频率和强度你能告诉他什么吗？

## 12.3.3 场张量

如式 (12.109) 所指出的， $E$ 和 $B$ 显然不是两个 4-矢量空间部分的变换——事实上当你从一个惯性系变换到另一个惯性系时 $E$ 和 $B$ 的分量是联系在一起的。这种根据式 (12.109) 的变换，有六个分量的对象属于哪一类？答案：它是一个反对称的二阶张量。

记得一个4-矢量遵循变换的如下法则：

$$
\bar {a} ^ {\mu} = \Lambda_ {\nu} ^ {\mu} a ^ {\nu}\tag{12.113}
$$

（隐含对指标 $\nu$ 的求和），式中， $\Lambda$ 是洛伦兹变换矩阵。如果 $\overline{S}$ 以速率 v 沿 x 轴运动， $\Lambda$ 有下面的形式：

$$
\Lambda = \left( \begin{array}{c c c c} {\gamma} & {- \gamma \beta} & 0 & 0 \\ {- \gamma \beta} & {\gamma} & 0 & 0 \\ {0} & 0 & 1 & 0 \\ {0} & 0 & 0 & 1 \end{array} \right)\tag{12.114}
$$

$\Lambda_{\nu}^{\mu}$ 是行指标为 $\mu$ 和列指标为 $\nu$ 的矩阵元。一个（二阶）张量具有两个指标，它用两个 $\Lambda$ 来进行变换（每一个对应一个指标）：

$$
\bar {t} ^ {\mu \nu} = \Lambda_ {\lambda} ^ {\mu} \Lambda_ {\sigma} ^ {\nu} t ^ {\lambda \sigma}\tag{12.115}
$$

一个张量（对4维情况）有 $4 \times 4 = 16$ 个分量，它们可以用一个 $4 \times 4$ 的数组表示：

$$
t ^ {\mu \nu} = \left\{ \begin{array}{c c c c} t ^ {0 0} & t ^ {0 1} & t ^ {0 2} & t ^ {0 3} \\ t ^ {1 0} & t ^ {1 1} & t ^ {1 2} & t ^ {1 3} \\ t ^ {2 0} & t ^ {2 1} & t ^ {2 2} & t ^ {2 3} \\ t ^ {3 0} & t ^ {3 1} & t ^ {3 2} & t ^ {3 3} \end{array} \right\}
$$

但这16个元素不必都不同。例如，一个对称张量有性质

$$
t ^ {\mu \nu} = t ^ {\nu \mu} \quad (\text { 对称张量 })\tag{12.116}
$$

在这种情况下有 10 个不同的分量，16 个中有 6 个重复出现 ( $t^{01} = t^{10}$ , $t^{02} = t^{20}$ , $t^{03} = t^{30}$ , $t^{12} = t^{21}$ , $t^{13} = t^{31}$ , $t^{23} = t^{32}$ )。类似地，反对称张量遵从

$$
t ^ {\mu \nu} = - t ^ {\nu \mu} \quad (\text { 反   对   称   张   量 })\tag{12.117}
$$

这样的张量仅有6个不同的元素——原来的16个元素中，6个重复（和前面的一样，仅差一个符号），4个为零 $(t^{00}, t^{11}, t^{22}$ 和 $t^{33})$ 。故一般的反对称张量的形式是

$$
t ^ {\mu \nu} = \left\{ \begin{array}{c c c c} 0 & t ^ {0 1} & t ^ {0 2} & t ^ {0 3} \\ - t ^ {0 1} & 0 & t ^ {1 2} & t ^ {1 3} \\ - t ^ {0 2} & - t ^ {1 2} & 0 & t ^ {2 3} \\ - t ^ {0 3} & - t ^ {1 3} & - t ^ {2 3} & 0 \end{array} \right\}
$$

让我们来看对于一个有6个不同元素的反对称张量，变换规则式(12.115)是如何进行的。从 $t^{01}$ 开始，我们有

$$
\bar {t} ^ {0 1} = \Lambda_ {\lambda} ^ {0} \Lambda_ {\sigma} ^ {1} t ^ {\lambda \sigma}
$$

但根据式(12.114)， $\Lambda_{\lambda}^{0}=0$ 除非 $\lambda=0$ 或 1； $\Lambda_{\sigma}^{1}=0$ 除非 $\sigma=0$ 或 1。故在求和中仅有四项：

$$
\bar {t} ^ {0 1} = \Lambda_ {0} ^ {0} \Lambda_ {0} ^ {1} t ^ {0 0} + \Lambda_ {0} ^ {0} \Lambda_ {1} ^ {1} t ^ {0 1} + \Lambda_ {1} ^ {0} \Lambda_ {0} ^ {1} t ^ {1 0} + \Lambda_ {1} ^ {0} \Lambda_ {1} ^ {1} t ^ {1 1}
$$

另一方面， $t^{00} = t^{11} = 0$ ，而 $t^{01} = -t^{10}$ ，所以

$$
t ^ {0 1} = \left(\Lambda_ {0} ^ {0} \Lambda_ {1} ^ {1} - \Lambda_ {1} ^ {0} \Lambda_ {0} ^ {1}\right) t ^ {0 1} = \left[ \gamma^ {2} - (\gamma \beta) ^ {2} \right] t ^ {0 1} = t ^ {0 1}
$$

我要求你求出其他的——全部的变换规则是

$$
\left. \begin{array}{l} \bar {t} ^ {0 1} = t ^ {0 1}, \quad \bar {t} ^ {0 2} = \gamma (t ^ {0 2} - \beta t ^ {1 2}), \quad \bar {t} ^ {0 3} = \gamma (t ^ {0 3} + \beta t ^ {3 1}) \\ \bar {t} ^ {2 3} = t ^ {2 3}, \quad \bar {t} ^ {3 1} = \gamma (t ^ {3 1} + \beta t ^ {0 3}), \quad \bar {t} ^ {1 2} = \gamma (t ^ {1 2} - \beta t ^ {0 2}) \end{array} \right\}\tag{12.118}
$$

这正是我们从物理基础上推导出的电磁场 [式 (12.109)] 的变换规则——事实上，通过直接对比，我们能构造场张量（field tensor） $F^{\mu\nu27}$ ：

$$
F ^ {0 1} \equiv \frac {E _ {x}}{c}, \quad F ^ {0 2} \equiv \frac {E _ {y}}{c}, \quad F ^ {0 3} \equiv \frac {E _ {z}}{c}, \quad F ^ {1 2} \equiv B _ {z}, \quad F ^ {3 1} \equiv B _ {y}, \quad F ^ {2 3} \equiv B _ {x}
$$

写成数组的形式，

$$
F ^ {\mu \nu} = \left\{ \begin{array}{c c c c} 0 & E _ {x} / c & E _ {y} / c & E _ {z} / c \\ - E _ {x} / c & 0 & B _ {z} & - B _ {y} \\ - E _ {y} / c & - B _ {z} & 0 & B _ {x} \\ - E _ {z} / c & B _ {y} & - B _ {x} & 0 \end{array} \right\}\tag{12.119}
$$

这样相对论完成并完善了始于奥斯特的工作，把电场和磁场合写进了单独一个量， $F^{\mu \nu}$ 。

如果你细致敏锐，也许会注意到把 E 和 B 纳入一个反对称张量中的方式是不同的：不是比较式 (12.109) 的第一行与式 (12.118) 的第一行，及它们间的第二行，而是比较式 (12.109) 的第一行与式 (12.118) 的第二行，以及反过来式 (12.109) 的第二行与式 (12.118) 的第一行比较。这可导出对偶张量， $G^{\mu\nu}$ ：

$$
G ^ {\mu \nu} = \left\{ \begin{array}{c c c c} 0 & B _ {x} & B _ {y} & B _ {z} \\ - B _ {x} & 0 & - E _ {z} / c & E _ {y} / c \\ - B _ {y} & E _ {z} / c & 0 & - E _ {x} / c \\ - B _ {z} & - E _ {y} / c & E _ {x} / c & 0 \end{array} \right\}\tag{12.120}
$$

$G^{\mu \nu}$ 可直接由 $F^{\mu \nu}$ 通过替换 $\pmb {E} / c\to \pmb {B},\pmb {B}\rightarrow -\pmb {E} / c$ 得到。注意这种操作使式(12.109）没有变化——这就是为何两个张量都可生成关于 $\pmb{E}$ 和 $\pmb{B}$ 的正确变换规则。

习题 12.50 证明通过洛伦兹变换后一个张量的对称性（或反对称性）保持不变（即：如果 $t^{\mu\nu}$ 是对称的，证明 $\bar{t}^{\mu\nu}$ 也是对称的。对反对称也是这样）。

习题12.51 前面讲过一个协变4-矢量可由改变一个逆变量的第零分量的符号得到。对张量同样如此：当“降低一个指数”产生协变量时，如果指数是零，改变符号。以 $\pmb{E}$ 和 $\pmb{B}$ 计算张量不变量

$$
F ^ {\mu \nu} F _ {\mu \nu}, G ^ {\mu \nu} G _ {\mu \nu}, F ^ {\mu \nu} G _ {\mu \nu}
$$

并与习题 12.47 比较。

习题12.52 一个沿 $z$ 轴的长直线，线电荷密度为 $\lambda$ ，以速率 $v$ 沿 $+z$ 方向运动。构造在点 $(x,0,0)$ 处的场张量和对偶张量。

## 12.3.4 张量形式的电动力学

既然我们知道了如何用相对论形式表示场，是用这种语言来重新写出电动力学的定律（麦克斯韦方程和洛伦兹力公式）的时候了。作为开始，我们必须确定场源， $\rho$ 和 $J$ ，是如何变换的。想象一朵电荷云漂浮过来，我们研究其中一无限小体积 $V$ ，它带电荷为 $Q$ ，运动速度为 $\pmb{u}$ （图12.43）。电荷密度是

$$
\rho = \frac {Q}{V}
$$

![](images/18e752c9524017a6545a89c792861e282cb7af2bba5fd69c01b8334a499f8fc9.jpg)  
图12.43

电流密度 $^{28}$ 是

$$
J = \rho u
$$

我想用固有电荷密度（proper charge density） $\rho_0$ 表示这些量，该密度是静止系中的电荷的密度：

$$
\rho_ {0} = \frac {Q}{V _ {0}}
$$

式中， $V_{0}$ 为电荷云的静止体积，因为一个维度（运动方向）是洛伦兹收缩的，

$$
V = \sqrt {1 - u ^ {2} / c ^ {2}} V _ {0}\tag{12.121}
$$

所以

$$
\rho = \rho_ {0} \frac {1}{\sqrt {1 - u ^ {2} / c ^ {2}}}, \quad J = \rho_ {0} \frac {\boldsymbol {u}}{\sqrt {1 - u ^ {2} / c ^ {2}}}\tag{12.122}
$$

与式 (12.40) 和式 (12.42) 比较，可看出这是固有速度的分量乘以不变量 $\rho_0$ 。很显然，电荷密度和电流密度可写成一个 4-矢量：

$$
J ^ {\mu} = \rho_ {0} \eta^ {\mu}\tag{12.123}
$$

其分量是

$$
\boxed {J ^ {\mu} = (c \rho , J _ {x}, J _ {y}, J _ {z})}\tag{12.124}
$$

我们称它为电流密度 4-矢量（current density 4-vector）。

连续性方程 [式 (5.29)]

$$
\nabla \cdot \boldsymbol {J} = - \frac {\partial \rho}{\partial t}
$$

表示了局域电荷守恒，用 $J^{\mu}$ 可以写成轻巧紧凑的形式：

$$
\nabla \cdot \boldsymbol {J} = \frac {\partial J _ {x}}{\partial x} + \frac {\partial J _ {y}}{\partial y} + \frac {\partial J _ {z}}{\partial z} = \sum_ {i = 1} ^ {3} \frac {\partial J ^ {i}}{\partial x ^ {i}}
$$

而

$$
\frac {\partial \rho}{\partial t} = \frac {1}{c} \frac {\partial J ^ {0}}{\partial t} = \frac {\partial J ^ {0}}{\partial x ^ {0}}\tag{12.125}
$$

把 $\partial\rho/\partial t$ 移到左边 (在连续性方程中)，有

$$
\boxed {\frac {\partial J ^ {\mu}}{\partial x ^ {\mu}} = 0}\tag{12.126}
$$

式中暗含着对 $\mu$ 的求和。 $\partial J^{\mu}/\partial x^{\mu}$ 是 $J^{\mu}$ 的四维散度，所以电流连续性方程指出电流密度4-矢量散度为零。

对于麦克斯韦方程，它们可写成

$$
\boxed {\frac {\partial F ^ {\mu \nu}}{\partial x ^ {\nu}} = \mu_ {0} J ^ {\mu}, \quad \frac {\partial G ^ {\mu \nu}}{\partial x ^ {\nu}} = 0}\tag{12.127}
$$

式中隐含着对 $\nu$ 的求和。每一个表示四个方程——每一个 $\mu$ 有一个方程。如果 $\mu = 0$ ，第一个方程为

$$
\begin{array}{r l} & {\frac {\partial F ^ {0 \nu}}{\partial x ^ {\nu}} = \frac {\partial F ^ {0 0}}{\partial x ^ {0}} + \frac {\partial F ^ {0 1}}{\partial x ^ {1}} + \frac {\partial F ^ {0 2}}{\partial x ^ {2}} + \frac {\partial F ^ {0 3}}{\partial x ^ {3}}} \\ & {\qquad = \frac {1}{c} \left(\frac {\partial E _ {x}}{\partial x} + \frac {\partial E _ {y}}{\partial y} + \frac {\partial E _ {z}}{\partial z}\right) = \frac {1}{c} (\nabla \cdot \pmb {E})} \\ & {\qquad = \mu_ {0} J ^ {0} = \mu_ {0} c \rho} \end{array}
$$

或者

$$
\nabla \cdot \boldsymbol {E} = \frac {1}{\epsilon_ {0}} \rho
$$

当然这是高斯定理。如果 $\mu = 1$ ，我们有

$$
\frac {\partial F ^ {1 \nu}}{\partial x ^ {\nu}} = \frac {\partial F ^ {1 0}}{\partial x ^ {0}} + \frac {\partial F ^ {1 1}}{\partial x ^ {1}} + \frac {\partial F ^ {1 2}}{\partial x ^ {2}} + \frac {\partial F ^ {1 3}}{\partial x ^ {3}}
$$

$$
\begin{array}{l} {= - \frac {1}{c ^ {2}} \frac {\partial E _ {x}}{\partial t} + \frac {\partial B _ {z}}{\partial y} - \frac {\partial B _ {y}}{\partial z} = \left(- \frac {1}{c ^ {2}} \frac {\partial \pmb {E}}{\partial t} + \nabla \times \pmb {B}\right) _ {x}} \\ {= \mu_ {0} J ^ {1} = \mu_ {0} J _ {x}} \end{array}
$$

把这个结果和 $\mu = 2$ 及 $\mu = 3$ 的结果组合一起，有

$$
\nabla \times \boldsymbol {B} = \mu_ {0} \boldsymbol {J} + \mu_ {0} \epsilon_ {0} \frac {\partial \boldsymbol {E}}{\partial t}
$$

这是麦克斯韦修正后的安培定律。

式 (12.127) 中的第二个方程，对于 $\mu = 0$ ，有

$$
\begin{array}{r l} \frac {\partial G ^ {0 \nu}}{\partial x ^ {\nu}} & = \frac {\partial G ^ {0 0}}{\partial x ^ {0}} + \frac {\partial G ^ {0 1}}{\partial x ^ {1}} + \frac {\partial G ^ {0 2}}{\partial x ^ {2}} + \frac {\partial G ^ {0 3}}{\partial x ^ {3}} \\ & = \frac {\partial B _ {x}}{\partial x} + \frac {\partial B _ {y}}{\partial y} + \frac {\partial B _ {z}}{\partial z} = \nabla \cdot \boldsymbol {B} = 0, \end{array}
$$

(这是第三个麦克斯韦方程)，对于 $\mu=1$ ，有

$$
\begin{array}{r l} & {\frac {\partial G ^ {1 \nu}}{\partial x ^ {\nu}} = \frac {\partial G ^ {1 0}}{\partial x ^ {0}} + \frac {\partial G ^ {1 1}}{\partial x ^ {1}} + \frac {\partial G ^ {1 2}}{\partial x ^ {2}} + \frac {\partial G ^ {1 3}}{\partial x ^ {3}}} \\ & {\qquad = - \frac {1}{c} \frac {\partial B _ {x}}{\partial t} - \frac {1}{c} \frac {\partial E _ {z}}{\partial y} + \frac {1}{c} \frac {\partial E _ {y}}{\partial z} = - \frac {1}{c} \left(\frac {\partial B}{\partial t} + \nabla \times E\right) _ {x} = 0} \end{array}
$$

把这个结果和 $\mu = 2$ 及 $\mu = 3$ 的结果组合一起，有

$$
\nabla \times \boldsymbol {E} = - \frac {\partial \boldsymbol {B}}{\partial t}
$$

这就是法拉第定律。以相对论的形式，麦克斯韦的四个比较复杂的方程化简为两个宜人的简单方程。

利用 $F^{\mu\nu}$ 和固有速度 $\eta^{\mu}$ ，作用在电荷 q 上的闵可夫斯基力为

$$
\boxed {K ^ {\mu} = q \eta_ {\nu} F ^ {\mu \nu}}\tag{12.128}
$$

如果 $\mu = 1$ ，有

$$
\begin{array}{l} K ^ {1} = q \eta_ {\nu} F ^ {1 \nu} = q \left(- \eta^ {0} F ^ {1 0} + \eta^ {1} F ^ {1 1} + \eta^ {2} F ^ {1 2} + \eta^ {3} F ^ {1 3}\right) \\ = q \left[ \frac {- c}{\sqrt {1 - u ^ {2} / c ^ {2}}} \left(\frac {- E _ {x}}{c}\right) + \frac {u _ {y}}{\sqrt {1 - u ^ {2} / c ^ {2}}} \left(B _ {z}\right) + \frac {u _ {z}}{\sqrt {1 - u ^ {2} / c ^ {2}}} \left(- B _ {y}\right) \right] \\ = \frac {q}{\sqrt {1 - u ^ {2} / c ^ {2}}} [ \boldsymbol {E} + (\boldsymbol {u} \times \boldsymbol {B}) ] _ {x} \end{array}
$$

对 $\mu = 2$ 及 $\mu = 3$ 有类似的形式，所以有

$$
\boldsymbol {K} = \frac {q}{\sqrt {1 - u ^ {2} / c ^ {2}}} [ \boldsymbol {E} + (\boldsymbol {u} \times \boldsymbol {B}) ]\tag{12.129}
$$

参看前面的洛伦兹力公式 (12.69)

$$
\boldsymbol {F} = q [ \boldsymbol {E} + (\boldsymbol {u} \times \boldsymbol {B}) ]
$$

因此，式(12.128)表示洛伦兹力公式的相对论形式。我把解释第零分量的问题留给你们自己（习题12.55）。

习题 12.53 从麦克斯韦方程 [式 (12.127)] 直接推导出连续性方程 [式 (12.126)]。

习题12.54 证明式(12.127)中的第二个方程可用 $F^{\mu \nu}$ 表示为

$$
\frac {\partial F _ {\mu \nu}}{\partial x ^ {\lambda}} + \frac {\partial F _ {\nu \lambda}}{\partial x ^ {\mu}} + \frac {\partial F _ {\lambda \mu}}{\partial x ^ {\nu}} = 0\tag{12.130}
$$

习题 12.55 求出并解释电磁场力 [式 (12.128)] 的 $\mu = 0$ 分量。

## 12.3.5 相对论势

由第 10 章我们知道电磁场可用一个标势 V 和一个矢势 A 表示：

$$
\pmb {E} = - \nabla V - \frac {\partial \pmb {A}}{\partial t}, \quad \pmb {B} = \nabla \times \pmb {A}\tag{12.131}
$$

你或许推测 V 和 A 可以一起构成一个 4-矢量：

$$
\boxed {A ^ {\mu} = (V / c, A _ {x}, A _ {y}, A _ {z})}\tag{12.132}
$$

利用这个 4-矢量势（4-vector potential），场张量可写成

$$
\boxed {F ^ {\mu \nu} = \frac {\partial A ^ {\nu}}{\partial x _ {\mu}} - \frac {\partial A ^ {\mu}}{\partial x _ {\nu}}}\tag{12.133}
$$

（注意微分是对协变量 $x_{\mu}$ 和 $x_{\nu}$ 进行的，记住第零分量改变符号： $x_0 = -x^0$ 。参看习题12.56。）

为了检验式 (12.133) 与式 (12.131) 等价，我们来明确地求几项。对于 $\mu = 0$ ， $\nu = 1$ ，有

$$
\begin{array}{c} F ^ {0 1} = \frac {\partial A ^ {1}}{\partial x _ {0}} - \frac {\partial A ^ {0}}{\partial x _ {1}} = - \frac {\partial A _ {x}}{\partial (c t)} - \frac {1}{c} \frac {\partial V}{\partial x} \\ = - \frac {1}{c} \left(\frac {\partial A}{\partial t} + \nabla V\right) _ {x} = \frac {E _ {x}}{c} \end{array}
$$

这（和它的 $\mu = 2$ 及 $\nu = 3$ ）是式(12.131)中的第一个方程。对于 $\mu = 1$ ， $\nu = 2$ ，有

$$
F ^ {1 2} = \frac {\partial A ^ {2}}{\partial x _ {1}} - \frac {\partial A ^ {1}}{\partial x _ {2}} = \frac {\partial A _ {y}}{\partial x} - \frac {\partial A _ {x}}{\partial y} = (\nabla \times \boldsymbol {A}) _ {z} = B _ {z}
$$

它（与 $F^{23}$ 和 $F^{31}$ 对应的结果一起）是式 (12.131) 中的第二个方程。

势形式公式可自动得到齐次麦克斯韦方程 $(\partial G^{\mu \nu} / \partial x^{\nu} = 0)$ 。对于非齐次方程 $(\partial F^{\mu \nu} / \partial x^{\nu} = \mu_0J^\mu)$ ，它变为

$$
\frac {\partial}{\partial x _ {\mu}} \left(\frac {\partial A ^ {\nu}}{\partial x ^ {\nu}}\right) - \frac {\partial}{\partial x _ {\nu}} \left(\frac {\partial A ^ {\mu}}{\partial x ^ {\nu}}\right) = \mu_ {0} J ^ {\mu}\tag{12.134}
$$

就目前而言，这是个难以处理的方程。前面讲过势不能由场唯一确定——事实上，从式(12.133)清楚地看到可以对 $A^{\mu}$ 增加任何标量函数 $\lambda$ 的梯度：

$$
A ^ {\mu} \longrightarrow A ^ {\mu \prime} = A ^ {\mu} + \frac {\partial \lambda}{\partial x _ {\mu}}\tag{12.135}
$$

而不改变 $F^{\mu \nu}$ 。这就是在10章中提到的规范不变性（gauge invariance）。我们可以研究它以化简式(12.134)。特别地，洛伦茨规范条件[式(10.12)]

$$
\nabla \cdot \mathbf {A} = - \frac {1}{c ^ {2}} \frac {\partial V}{\partial t}
$$

在相对论形式中变为

$$
\frac {\partial A ^ {\mu}}{\partial x ^ {\mu}} = 0\tag{12.136}
$$

所以在洛伦茨规范中，式(12.134)简化为

$$
\boxed {\Box^ {2} A ^ {\mu} = - \mu_ {0} J ^ {\mu}}\tag{12.137}
$$

式中， $\square^2$ 是达朗贝尔算符（d'Alembertian），

$$
\Box^ {2} \equiv \frac {\partial}{\partial x _ {\nu}} \frac {\partial}{\partial x ^ {\nu}} = \nabla^ {2} - \frac {1}{c ^ {2}} \frac {\partial^ {2}}{\partial t ^ {2}}\tag{12.138}
$$

结合前面的结果，式(12.137)成为一个4-矢量方程——它是麦克斯韦方程组最优美（和最简洁）的表示 $^{29}$ 。

习题12.56 你也许注意到四维梯度（four-dimensional gradient） $\partial/\partial x^{\mu}$ 与一个协变4-矢量功能类似——事实上，为了简洁它常写为 $\partial_{\mu}$ 。例如，连续性方程 $\partial_{\mu}J^{\mu}=0$ ，具有两个矢量乘积的不变量的形式。相应的逆变梯度是 $\partial^{\mu}\equiv\partial/\partial x_{\mu}$ 。通过求解变换规则，利用链式法则，证明如果 $\phi$ 是一个标量函数， $\partial^{\mu}\phi$ 是一个（逆变量）4-矢量。

习题12.57 证明势表示[式(12.133)]自动满足 $\partial G^{\mu \nu} / \partial x^{\nu} = 0$ 。[建议：利用习题12.54结果。]

习题 12.58 证明李纳-维谢尔势 [式 (10.46) 和式 (10.47)] 可以用相对论的符号表示为

$$
A ^ {\mu} = - \frac {q}{4 \pi \epsilon_ {0} c} \frac {\eta^ {\mu}}{(\eta^ {\nu} \eta_ {\nu})}
$$

其中 $\nu^{\mu} \equiv x^{\mu} - w^{\mu}(t_{r})$ 。

## 第12章补充习题

习题 12.59 惯性系 $\overline{S}$ 相对于另一惯性系 S 以速度 $v = \beta c (\cos \phi \hat{x} + \sin \phi \hat{y})$ 运动。如通常一样，它们的坐标轴互相平行，在 $t = \bar{t} = 0$ 时它们的原点重合。求洛伦兹变换矩阵 [式 (12.25)]。

$$
\left[ \begin{array}{c c c c} {{\mathrm{答案}:}} & {{\left( \begin{array}{c c c c} {{\gamma}} & {{- \gamma \beta \cos \phi}} & {{- \gamma \beta \sin \phi}} & {{0}} \\ {{- \gamma \beta \cos \phi}} & {{\left(\gamma \cos^ {2} \phi + \sin^ {2} \phi\right)}} & {{\left(\gamma - 1\right) \sin \phi \cos \phi}} & {{0}} \\ {{- \gamma \beta \sin \phi}} & {{\left(\gamma - 1\right) \sin \phi \cos \phi}} & {{\left(\gamma \sin^ {2} \phi + \cos^ {2} \phi\right)}} & {{0}} \\ {{0}} & {{0}} & {{0}} & {{1}} \end{array} \right)}} \end{array} \right]
$$

习题 12.60 计算为使过程 $\pi + p \rightarrow K + \Sigma$ 发生， $\pi$ 介子需要具有的阈值（最小的）动量。质子 p 初始时处于静止状态。利用 $m_{\pi}c^{2} = 150, m_{K}c^{2} = 500, m_{p}c^{2} = 900, m_{\Sigma}c^{2} = 1200$ （此处所有量的单位为 MeV）。[提示：为了求阈值条件，以碰撞的动量中心为参考系（习题 12.31）。答案：1133MeV/c]

习题 12.61 质量为 m 的粒子与一个同样的处于静止的粒子发生完全弹性碰撞。在经典力学中两出射粒子的轨迹总是成 $90^{\circ}$ 。采用相对论计算这个角度。在动量中心系中，角度用散射角 $\phi$ 和速率 v 表示。[答案： $\arctan\left(2c^{2}/v^{2}\gamma\sin\phi\right)$ ]

习题12.62 求在沿 $x$ 方向恒定的闵可夫斯基力作用下，一个质量为 $m$ 、最初静止在原点的粒子运动时其坐标 $x$ 随时间 $t$ 的变化。结果以隐变量的形式表示（ $t$ 作为 $x$ 的函数）。[答案： $2Kt / mc = z\sqrt{1 + z^2} + \ln \left(z + \sqrt{1 + z^2}\right)$ ，其中 $z \equiv \sqrt{2Kx / mc^2}$ ]

习题12.63 质量为 $m$ 的两个点电荷（ $\pm q$ ）组成的电偶极矩，固定在（无质量）长为 $d$ 的细杆的两端。（不要假设 $d$ 是小的。）

（a）设偶极子沿垂直于它的轴的直线做双曲线运动 [式 (12.61)]，求作用在它上面的净自力。[提示：从适当修改式 (11.90) 开始。]

(b) 注意这种自作用力是恒力（不依赖 $t$ ），并指向运动的方向——正好使其做双曲运动。所以，偶极子在没有外力情况下可自持加速运动 $^{30}$ ! [你认为能量从哪儿来的？] 确定持续的自作用力 $F$ ，

$$
\text {以} m, q \text {和} d \text {表示。} [ \text {答案:} (2 m c ^ {2} / d) \sqrt {(\mu_ {0} q ^ {2} / 8 \pi m d) ^ {2 / 3} - 1} ]
$$

习题12.64 一个理想的磁偶极矩 $m$ ，处在惯性系 $\overline{S}$ 的原点。 $\overline{S}$ 系相对于 $S$ 系以速率 $v$ 沿 $x$ 轴运动。在 $\overline{S}$ 中矢势为

$$
\overline {{{A}}} = \frac {\mu_ {0}}{4 \pi} \frac {\overline {{{m}}} \times \overline {{{\hat {r}}}}}{\bar {r} ^ {2}}
$$

[式 (5.85)], 且标势 $\bar{V}$ 是零。

(a) 求在 S 系中的标势 V。

$$
\left[ \mathrm{答案}: \frac {1}{4 \pi \epsilon_ {0}} \frac {\hat {\pmb {R}} \cdot (\pmb {v} \times \pmb {m})}{c ^ {2} R ^ {2}} \frac {\left(1 - v ^ {2} / c ^ {2}\right)}{\left[ 1 - (v ^ {2} / c ^ {2}) \sin^ {2} \theta \right] ^ {3 / 2}} \right]
$$

(b) 在非相对论极限下，证明在 $S$ 系中的标量势是一个位于 $\overline{O}$ 处、偶极矩为

$$
p = \frac {\boldsymbol {v} \times \boldsymbol {m}}{c ^ {2}}
$$

的理想电偶极子所产生的标量势。

习题12.65 一个静止的磁偶极子， $m = m\hat{z}$ ，位于一个具有均匀表面电流 $K = K\hat{x}$ 的无限大的平面上方（图12.44）。

![](images/03612e4863bda17311361316a655af1e9986d03e3e2a41d904733de12a1ac4ed.jpg)  
图12.44

(a) 利用式 (6.1) 求作用在偶极矩上的力矩。

(b) 假设表面电流是由面电荷密度 $\sigma$ 以速度 $v = v\hat{x}$ 运动而产生的，所以 $K = \sigma v$ ，而磁偶极子由线电荷密度 $\lambda$ 以速率 $v$ （与前面的 $v$ 大小相同）绕边长为 $l$ 的矩形线圈运动产生的，所以 $m = \lambda v l^2$ 。设 $\overline{S}$ 系以速率 $v$ 沿 $x$ 轴运动，在 $\overline{S}$ 系中来考虑这个构型。在 $\overline{S}$ 系中表面电荷静止，故它不产生磁场。证明在这个参考系中载流线圈产生了一个电偶极矩，用式 (4.4) 计算力矩。

习题12.66 在某一惯性系 $S$ 中，在某一时空点，电场 $\pmb{E}$ 和磁场 $\pmb{B}$ 既不平行也不垂直。证明在另一相对于 $S$ 以速度 $\pmb{v}$ 运动的惯性参考系 $\overline{S}$ 中， $\pmb{v}$ 由下式给出：

$$
\frac {\pmb {v}}{1 + v ^ {2} / c ^ {2}} = \frac {\pmb {E} \times \pmb {B}}{B ^ {2} + E ^ {2} / c ^ {2}}
$$

则场 $\bar{E}$ 和 $\bar{B}$ 在此点相互平行。存在一个使它们互相垂直的参考系吗？

习题12.67 两个电荷 $\pm q$ 以恒定速度沿相反方向从 $x$ 轴两侧向原点靠近。它们碰撞并粘在一起构成一个中性粒子并静止。简要叙述碰撞前后电场分布（记住电磁场“信号”以光速传播）。你如何从物理上解释碰撞后的场31？

习题12.68 按下面的步骤“推导”洛伦兹力公式：让电荷 $q$ 在 $\overline{S}$ 系中静止，所以 $\overline{F} = q\overline{E}$ 。让 $\overline{S}$ 系相对于 $S$ 系以速度 $\pmb{v} = v\hat{\pmb{x}}$ 运动。利用变换规则[式(12.67）和式(12.109)]，用 $\pmb{F}$ 表示 $\overline{\pmb{F}}$ ， $\pmb{E}$ 和 $\pmb{B}$ 表示 $\bar{\pmb{E}}$ 和 $\bar{\pmb{B}}$ 。由此得出用 $\pmb{E}$ 和 $\pmb{B}$ 表示的 $\pmb{F}$ 。

习题 12.69 在均匀电场 $E = E_{0}\hat{z}$ 和均匀磁场 $B = B_{0}\hat{x}$ 中，一个电荷 q 初始时静止于原点。变换到一个 E = 0 的参考系，在该系中求出电荷的轨迹，然后变换回原来的参考系，并求出电荷在原来参考系中的运动轨迹。假设 $E_{0} < cB_{0}$ 。将你的结果例题 5.2 做比较。

习题12.70

(a) 用 D 和 H 构造一个张量 $D^{\mu\nu}$ (类似 $F^{\mu\nu}$ )。利用它表示有自由电流 $J_{f}^{\mu}$ 的物体内的麦克斯韦方程。[答案： $D^{01} \equiv cD_{x}, D^{12} \equiv H_{z}$ ，等等； $\partial D^{\mu\nu}/\partial x^{\nu} = J_{f}^{\mu}]$

(b) 构造对偶张量 $H^{\mu \nu}$ （类似 $G^{\mu \nu}$ ）。[答案： $H^{01} \equiv H_x$ ， $H^{12} \equiv -cD_z$ ，等等]

(c) 闵可夫斯基对线性介质提出了相对论性本构关系（relativistic constitutive relations）:

$$
D ^ {\mu \nu} \eta_ {\nu} = c ^ {2} \varepsilon F ^ {\mu \nu} \eta_ {\nu} \quad \text {和} \quad H ^ {\mu \nu} \eta_ {\nu} = \frac {1}{\mu} G ^ {\mu \nu} \eta_ {\nu}
$$

式中， $\varepsilon$ 是固有 $^{32}$ 介电常数； $\mu$ 是固有磁导率； $\eta_{\nu}$ 是材料的 4-速度。证明当材料静止时，闵可夫斯基公式再次给出了式 (4.32) 和式 (6.31)。

(d) 对于以（平常）速度 u 移动的介质，求出 D 和 H，以及 E 和 B 的关系。

习题 12.71 利用拉莫尔公式 [式 (11.70)] 和狭义相对论推导出 Liénard 公式 [式 (11.73)]。

习题12.72 亚伯拉罕-洛伦兹公式[式(11.80)]自然的相对论推广是

$$
K _ {\mathrm{辐射}} ^ {\mu} = \frac {\mu_ {0} q ^ {2}}{6 \pi c} \frac {\mathrm{d} \alpha^ {\mu}}{\mathrm{d} \tau}
$$

这当然是一个4-矢量，它在非相对论极限 $(v\ll c)$ 下化为亚伯拉罕-洛伦兹公式。

(a) 证明这不是一个可能的闵可夫斯基力。[提示：参看习题12.39d]

（b）找出一个修正项，使之当加在右边时消除你在（a）中提出的异议，但不能影响公式的4-矢量特性及非相对论极限 $^{33}$ 。

习题12.73 推广相对论电动力学定律[式(12.127)和式(12.128)]，以包含磁荷。[参看7.3.4节]

# 附录

The OCR result should be empty, as the image contains only a stylistic horizontal line which must be ignored according to Rule 2. No text or placeholder characters should be output.

## 附录 A 曲线坐标系中的矢量微积分

## A.1 引言

在本附录 A 中，我将简要证明矢量微积分的三个基本定理。我的目的是关注定理的要点，而不是具体到每个细节问题。参见斯皮瓦克（M. Spivak）所著的 Calculus on Manifolds（纽约：本杰明，1965 年）一书 $^{1}$ ，你可以找到一种更简洁、更现代、更统一的处理方法，但同时也必然需要更长的时间。

为了更一般起见, 我将使用任意的（正交的）曲线坐标系 $(u,v,w)$ ，在这样的坐标系中给出梯度、散度、旋度和拉普拉斯算符的公式。然后，你可以把它应用到直角坐标系、球坐标系或者柱坐标系，甚至任何你想使用的坐标系。如果这种一般性的概括在你第一次学习时使你感到迷惑，你宁愿使用直角坐标系，只要看到 $(u,v,w)$ 的地方就把它们当作 $(x,y,z)$ ，并在阅读过程中进行相应的简化即可。

## A.2 标记法

我们由空间中的三个坐标 $u, v, w$ 来确定一个点 [在直角系中为 $(x, y, z)$ ；在球坐标系中为 $(r, \theta, \phi)$ ；在柱坐标系中为 $(s, \phi, z)]$ 。我将假设该坐标系是正交的，也就是指向相应坐标增加方向的三个单位矢量 $\hat{u}, \hat{v}, \hat{w}$ 是相互垂直的。请注意，单位矢量是位置的函数，因为它们的方向（直角坐标系除外）因位置而变。任何矢量都可以用 $\hat{u}, \hat{v}, \hat{w}$ 来表示——特别是从 $(u, v, w)$ 到 $(u + du, v + dv, w + dw)$ 的无限小位移矢量可以写成

$$
\mathrm{d} \boldsymbol {l} = f \mathrm{d} u \hat {\boldsymbol {u}} + g \mathrm{d} v \hat {\boldsymbol {v}} + h \mathrm{d} w \hat {\boldsymbol {w}},\tag{A.1}
$$

其中 $f, g, h$ 是特定坐标系的位置特性的函数（在直角坐标系中 $f = g = h = 1$ ；在球坐标系中 $f = 1, g = r, h = r \sin \theta$ ；在柱坐标系中 $f = h = 1, g = s$ ）。正如你很快就会看到，这三个函数会告诉你关于坐标系中你想要知道的一切信息。

## A.3 梯度

如果你从点 $(u, v, w)$ 移动至点 $(u + \mathrm{d}u, v + \mathrm{d}v, w + \mathrm{d}w)$ , 标量函数 $t(u, v, w)$ 会改变一个量

$$
\mathrm{d} t = \frac {\partial t}{\partial u} \mathrm{d} u + \frac {\partial t}{\partial v} \mathrm{d} v + \frac {\partial t}{\partial w} \mathrm{d} w\tag{A.2}
$$

这是偏微分的一个标准定理。 $^{2}$ 我们可以把它写成点积的形式

$$
\mathrm{d} t = \nabla t \cdot \mathrm{d} \boldsymbol {l} = (\nabla t) _ {u} f \mathrm{d} u + (\nabla t) _ {v} g \mathrm{d} v + (\nabla t) _ {w} h \mathrm{d} w\tag{A.3}
$$

只要我们定义

$$
(\nabla t) _ {u} \equiv \frac {1}{f} \frac {\partial t}{\partial u}, (\nabla t) _ {v} \equiv \frac {1}{f} \frac {\partial t}{\partial v}, (\nabla t) _ {w} \equiv \frac {1}{f} \frac {\partial t}{\partial w}
$$

则 $t$ 的梯度（gradient）是

$$
\boxed {\nabla t \equiv \frac {1}{f} \frac {\partial t}{\partial u} \hat {\boldsymbol {u}} + \frac {1}{f} \frac {\partial t}{\partial v} \hat {\boldsymbol {v}} + \frac {1}{f} \frac {\partial t}{\partial w} \hat {\boldsymbol {w}}}\tag{A.4}
$$

如果你现在从表 A.1 中选择 f, g, h 适当的表达式, 你就可以很容易得到梯度在直角坐标系、球坐标系和柱坐标系中的表达式, 如在本书的后环衬给出的一样。

表A.1

<table><tr><td>坐标系</td><td>u, v, w</td><td>f, g, h</td></tr><tr><td>直角系</td><td>x, y, z</td><td>1, 1, 1</td></tr><tr><td>球坐标系</td><td>r, θ, φ</td><td>1, r, r sin θ</td></tr><tr><td>柱坐标系</td><td>s, φ, z</td><td>1, s, 1</td></tr></table>

由式(A.3)可以给出从点 $\pmb{a}$ 到点 $\pmb{b}$ 时 $t$ 的总的改变量（图A.1）是

$$
t (\pmb {b}) - t (\pmb {a}) = \int_ {\pmb {a}} ^ {\pmb {b}} \mathrm{d} t = \int_ {\pmb {a}} ^ {\pmb {b}} (\nabla t) \cdot \mathrm{d} \pmb {l}\tag{A.5}
$$

这就是梯度的基本定理（fundamental theorem for gradients）（当然，对这种情况不需要更多的证明）。请注意，积分与从 a 到 b 的具体路径无关。

![](images/10476205bab92716fed934e2a25279d1339bbaf6733ffd78f7d3c6003fce3ffa.jpg)  
图A.1

## A.4 散度

假定我们有一个矢量函数

$$
\boldsymbol {A} (u, v, w) = A _ {u} \hat {\boldsymbol {u}} + A _ {v} \hat {\boldsymbol {v}} + A _ {w} \hat {\boldsymbol {w}}
$$

我们想在无限小体积的表面上计算曲面积分 $\oint A\cdot \mathrm{d}a$ ，从点 $(u,v,w)$ 开始，依次将每个坐标增加无穷小量（图A.2）。由于坐标是正交的，所以这是一个长方体（至少在无限小极限下），其边长为 $\mathrm{d}l_u = f\mathrm{d}u,\mathrm{d}l_v = g\mathrm{d}v,\mathrm{d}l_w = h\mathrm{d}w$ ，因此体积为

$$
\mathrm{d} \tau = \mathrm{d} l _ {u} \mathrm{d} l _ {v} \mathrm{d} l _ {w} = (f g h) \mathrm{d} u \mathrm{d} v \mathrm{d} w\tag{A.6}
$$

[这些边长并不只是 $\mathrm{du},\mathrm{dv},\mathrm{dw}$ ——毕竟， $v$ 也许是一个角度，在这种情况下 $\mathrm{dv}$ 甚至没有长度量纲。正确的表示由式(A.1)给出。]

对于前表面

$$
\mathrm{d} \boldsymbol {a} = - (g h) \mathrm{d} v \mathrm{d} w \hat {\boldsymbol {u}}
$$

因此

$$
\boldsymbol {A} \cdot \mathrm{d} \boldsymbol {a} = - (g h A _ {u}) \mathrm{d} v \mathrm{d} w
$$

对背面表示式相同（除符号外），不过量 $ghA_{u}$ 现在是在 $(u + du)$ 处，而不是在 $u$ 处计算。因为对任何（可微）函数 $F(u)$ 都有

$$
F (u + \mathrm{d} u) - F (u) = \frac {\mathrm{d} F}{\mathrm{d} u} \mathrm{d} u
$$

前表面和后表面合在一起的贡献是

$$
\left[ \frac {\partial}{\partial u} (g h A _ {u}) \right] \mathrm{d} u \mathrm{d} v \mathrm{d} w = \frac {1}{f g h} \frac {\partial}{\partial u} (g h A _ {u}) \mathrm{d} \tau
$$

出于同样的原因，右侧和左侧表面之和为

$$
\frac {1}{f g h} \frac {\partial}{\partial v} (f h A _ {v}) \mathrm{d} \tau
$$

顶部和底部表面之和为

$$
\frac {1}{f g h} \frac {\partial}{\partial w} (f g A _ {w}) \mathrm{d} \tau
$$

那么，总计为

$$
\oint \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {a} = \frac {1}{f g h} \left[ \frac {\partial}{\partial u} (g h A _ {u}) + \frac {\partial}{\partial v} (f h A _ {v}) + \frac {\partial}{\partial w} (f g A _ {w}) \right] \mathrm{d} \tau\tag{A.7}
$$

$\mathrm{d}\tau$ 的系数用于定义 $\pmb{A}$ 在曲线坐标系中的散度

$$
\boxed {\nabla \cdot \boldsymbol {A} = \frac {1}{f g h} \left[ \frac {\partial}{\partial u} (g h A _ {u}) + \frac {\partial}{\partial v} (f h A _ {v}) + \frac {\partial}{\partial w} (f g A _ {w}) \right]}\tag{A.8}
$$

式(A.7)变为

$$
\oint \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {a} = (\nabla \cdot \boldsymbol {A}) \mathrm{d} \tau\tag{A.9}
$$

使用表 A.1, 你现在可以推导出直角坐标系、球坐标系和柱坐标系中的散度公式，它们列在本书的后环衬。

![](images/96e848e74f3bdea67e1d7f5bdfeee5996a883127b27c6fda22debf73d62c757e.jpg)  
图A.2

就目前而言，式(A.9)并没有证明散度定理，因为它只适用于无穷小体积，而且是相当特殊的无穷小体积。当然，有限体积可以分割成很多无限小的体积部分，式(A.9)可以应用于每个小体积。问题是当你把所有的小部分加起来时，式(A.9)的左边不单单是对这个有限体积的外表面进行积分，而是对所有这些无限小体积的表面进行积分。然而，幸好是这些贡献成对抵消，因为每个内表面都是两个相邻的无穷小体积的边界，由于da总是指向表面以外的，因此每对相邻边内表面的 $A \cdot da$ 符号都相反（图A.3）。当把所有加起来时，只有那些处于外边界的表面才有贡献。对于有限区域有

$$
\oint \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {a} = \int (\nabla \cdot \boldsymbol {A}) \mathrm{d} \tau\tag{A.10}
$$

你仅需对外表面进行积分 $^{3}$ 。这就建立了散度定理（divergence theorem）。

![](images/180bd4cab92006944fe9be87b1a2117c5586953bc4622424bc359b58d43b33a7.jpg)  
图A.3

## A.5 旋度

为了得到曲线坐标系中的旋度, 我们计算一个无穷小环路周围的线积分

$$
\oint \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {l}
$$

该无穷小闭合环路是从点 $(u, v, w)$ 开始，保持坐标不变，沿 $u, v$ 坐标轴分别逐渐增加无限小增量构成（图A.4）。曲面是一个矩形（至少在无穷小极限下），长度为 $\mathrm{d}l_{u} = f\mathrm{d}u$ ，宽度为 $\mathrm{d}l_{v} = g\mathrm{d}v$ ，面积是

$$
\mathrm{d} \boldsymbol {a} = (f g) \mathrm{d} u \mathrm{d} v \hat {\boldsymbol {w}}\tag{A.11}
$$

![](images/c124df7fb5200fcc85840dc4267b6a039ccee66b12fc2b68ca26794dc27000e4.jpg)  
图A.4

假设坐标系为右手系，图4中的 $\hat{w}$ 方向垂直纸面向外，选择这个方向作为 $\mathrm{da}$ 的正方向后，根据右手定则，我们必须沿如图所示的逆时针方向进行线积分。

沿着底部有

$$
\mathrm{d} \boldsymbol {l} = f \mathrm{d} u \hat {\boldsymbol {u}}
$$

所以

$$
\boldsymbol {A} \cdot \mathrm{d} \boldsymbol {l} = (f A _ {u}) \mathrm{d} u
$$

沿着顶部，符号颠倒，且 $fA_{u}$ 的计算值是在 $(v + \mathrm{d}v)$ 处，而不是在 $v$ 处。综合起来，两条边的贡献为

$$
\left[ - \left(f A _ {u}\right) | _ {v + \mathrm{d} v} + \left(f A _ {u}\right) | _ {v} \right] \mathrm{d} u = - \left[ \frac {\partial}{\partial v} (f A _ {u}) \right] \mathrm{d} u \mathrm{d} v
$$

同样，右左两边的贡献为

$$
\left[ \frac {\partial}{\partial u} (f A _ {v}) \right] \mathrm{d} u \mathrm{d} v
$$

所以总和为

$$
\begin{array}{r l} \oint \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {l} & = \left[ \frac {\partial}{\partial u} (g A _ {v}) - \frac {\partial}{\partial v} (f A _ {u}) \right] \mathrm{d} u \mathrm{d} v \\ & = \frac {1}{f g} \left[ \frac {\partial}{\partial u} (g A _ {v}) - \frac {\partial}{\partial v} (f A _ {u}) \right] \hat {\boldsymbol {w}} \cdot \mathrm{d} \boldsymbol {a} \end{array}\tag{A.12}
$$

右侧 da 的系数用于定义分量的旋度。以同样的方法构造 u, v 分量的旋度，于是有

$$
\boxed { \begin{array}{c} \nabla \times \boldsymbol {A} \equiv \frac {1}{g h} \left[ \frac {\partial}{\partial v} (h A _ {w}) - \frac {\partial}{\partial w} (g A _ {v}) \right] \hat {\boldsymbol {u}} + \frac {1}{f h} \left[ \frac {\partial}{\partial w} (f A _ {u}) - \frac {\partial}{\partial u} (h A _ {w}) \right] \hat {\boldsymbol {v}} + \\ \frac {1}{f g} \left[ \frac {\partial}{\partial u} (g A _ {v}) - \frac {\partial}{\partial v} (f A _ {u}) \right] \hat {\boldsymbol {w}} \end{array} }\tag{A.13}
$$

并且式 (A.11) 可以推广为

$$
\oint \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {l} = (\nabla \times \boldsymbol {A}) \cdot \mathrm{d} \boldsymbol {a}\tag{A.14}
$$

使用表 A.1，你现在可以推导出直角坐标系、球坐标系和柱坐标系中旋度公式。

然而，式 (A.14) 本身并不能证明斯托克斯定理，因为此时它仅适用于非常特殊的无穷小曲面。同样，我们可以将任何有限的曲面分割成许多无穷小的部分，并可以将式 (A.14) 应用于每个部分 (图 A.5)。不过，当我们把它们加起来时，不仅得到了（在左边）外边界周围的线积分，还得到了内环周围的许多微小的线积分。同以前一样，幸好这些积分贡献成对相互抵消，因为每条内部线积分都是沿相反方向进行的。这样，式 (A.14) 可以推广到有限曲面，

$$
\oint \boldsymbol {A} \cdot \mathrm{d} \boldsymbol {l} = \int (\nabla \times \boldsymbol {A}) \cdot \mathrm{d} \boldsymbol {a}\tag{A.15}
$$

线积分仅适用于外部边界 $^{4}$ 。这就建立起了斯托克斯定理（Stokes' theorem）。

![](images/7c66dee6de093733757735d3ebf7c45d0b5cab68a13ca33d0fde762beb07c260.jpg)  
图A.5

## A.6 拉普拉斯算子

根据定义，标量拉普拉斯算子是梯度的散度，我们可以从式(A.4)和式(A.8)得到一般公式

$$
\boxed {\nabla^ {2} t = \frac {1}{f g h} \left[ \frac {\partial}{\partial u} \left(\frac {g h}{f} \frac {\partial t}{\partial u}\right) + \frac {\partial}{\partial v} \left(\frac {f h}{g} \frac {\partial t}{\partial v}\right) + \frac {\partial}{\partial v} \left(\frac {f g}{h} \frac {\partial t}{\partial w}\right) \right]}\tag{A.16}
$$

我再次请你使用表A.1推导出在直角坐标系、球坐标系和柱坐标系中的普拉斯算子公式，从而确认本书前环衬中的公式。

## 附录 B 亥姆霍兹定理

假定已知道矢量函数 $F(r)$ 的散度是一给定的标量函数 $D(r)$ :

$$
\nabla \cdot \boldsymbol {F} = D\tag{B.1}
$$

并且 $F(r)$ 的旋度是一给定的矢量函数 $C(r)$ :

$$
\nabla \times \boldsymbol {F} = \boldsymbol {C}\tag{B.2}
$$

为了保持一致性, $C(r)$ 一定是无散的,

$$
\nabla \cdot \boldsymbol {C} = 0\tag{B.3}
$$

这是因为旋度的散度总是零。问题：我们能够根据这些信息确定函数 $F(\pmb{r})$ 吗？如果 $D(\pmb{r})$ 和 $C(\pmb{r})$ 能够在无穷远处很快趋于零，答案是肯定的，我将通过具体推导来证明。

我断言

$$
\boldsymbol {F} = - \nabla U + \nabla \times \boldsymbol {W}\tag{B.4}
$$

其中

$$
U (\boldsymbol {r}) \equiv \frac {1}{4 \pi} \int \frac {D (\boldsymbol {r} ^ {\prime})}{\nu} \mathrm{d} \tau^ {\prime}\tag{B.5}
$$

且

$$
\boldsymbol {W} (\boldsymbol {r}) \equiv \frac {1}{4 \pi} \int \frac {\boldsymbol {C} \left(\boldsymbol {r} ^ {\prime}\right)}{2} \mathrm{d} \tau^ {\prime}\tag{B.6}
$$

积分涵盖整个空间，并且，同之前一样有 $\boldsymbol{\nu}=|\boldsymbol{r}-\boldsymbol{r}^{\prime}|$ 。如果 $\boldsymbol{F}(\boldsymbol{r})$ 由式 (B.4) 给出，那么它的散度为 [利用式 (1.102)]

$$
\nabla \cdot \boldsymbol {F} = - \nabla^ {2} U = - \frac {1}{4 \pi} \int D \nabla^ {2} \left(\frac {1}{r}\right) \mathrm{d} \tau^ {\prime} = \int D (\boldsymbol {r} ^ {\prime}) \delta^ {3} (\boldsymbol {r} - \boldsymbol {r} ^ {\prime}) \mathrm{d} \tau^ {\prime} = D (\boldsymbol {r})
$$

（记住旋度的散度为零，因此 W 项为零，并注意微分是关于 r 的，r 包含在 $\lambda$ 中。）

所以散度是正确的；那么旋度如何呢？

$$
\nabla \times \boldsymbol {F} = \nabla \times (\nabla \times \boldsymbol {W}) = - \nabla^ {2} \boldsymbol {W} + \nabla (\nabla \cdot \boldsymbol {W})\tag{B.7}
$$

（因为梯度的旋度总为零，所以 U 项为零。）而

$$
- \nabla^ {2} W = - \frac {1}{4 \pi} \int C \nabla^ {2} \left(\frac {1}{r}\right) \mathrm{d} \tau^ {\prime} = \int C (r ^ {\prime}) \delta^ {3} (r - r ^ {\prime}) \mathrm{d} \tau^ {\prime} = C (r)
$$

这很完美——如果我能使你相信式 (B.7) 右侧的第 2 项为零的话，我已经完成了任务。利用分部积分 [式 (1.59)] 并注意到对 $\nu$ 中带撇和不带撇坐标的求导相差一个负号，我们得到

$$
4 \pi \nabla \cdot \boldsymbol {W} = \int \boldsymbol {C} \cdot \nabla \left(\frac {1}{\imath}\right) \mathrm{d} \tau^ {\prime} = - \int \boldsymbol {C} \cdot \nabla^ {\prime} \left(\frac {1}{\imath}\right) \mathrm{d} \tau^ {\prime} = \int \frac {1}{\imath} \nabla^ {\prime} \boldsymbol {C} \mathrm{d} \tau^ {\prime} - \oint \frac {1}{\imath} \boldsymbol {C} \cdot \mathrm{d} \boldsymbol {a}\tag{B.8}
$$

但是，根据假设 [式 (B.3)] $C$ 的散度为零，只要 $C$ 足够快地趋于零，表面积分（在无穷远处）就会为零。

当然，这个证明默认了式 (B.5) 和式 (B.6) 中的积分收敛——否则 $U$ 和 $W$ 根本不存在。在较大 $r'$ 的极限情况下， $\nu \approx r'$ ，积分具有以下形式：

$$
\int_ {0} ^ {\infty} \frac {X (r ^ {\prime})}{r ^ {\prime}} r ^ {\prime 2} \mathrm{d} r ^ {\prime} = \int_ {0} ^ {\infty} X (r ^ {\prime}) r ^ {\prime} \mathrm{d} r ^ {\prime}\tag{B.9}
$$

（这里 $X$ 代表 $D$ 或 $C$ ，视情况而定。）显然， $X(r')$ 在 $r'$ 较大时必须为零——但这还不够：如果 $X \sim 1 / r'$ ，被积函数是常数，因此积分会发散，即使 $X \sim 1 / r'^2$ ，积分则为对数函数，在 $r' \to \infty$ 仍然发散。显然，为了能够使证明成立， $F$ 的散度和旋度必须比 $1 / r^2$ 更快地趋于零。[顺便说一句，这足以确保式 (B.8) 中的表面积分为零。]

现在，假设满足 $D(\pmb{r})$ 和 $\pmb{C}(\pmb{r})$ 这些条件，那么式 (B.4) 的解是唯一的吗？答案显然不是，因为我们可以将任何散度和旋度都为零的矢量函数加到 $\pmb{F}$ 上，其结果仍然散度为 D 和旋度为 $\pmb{C}$ 。然而，碰巧的是没有一个函数其散度和旋度处处为零，并且在无穷远处时也趋于零（参见第 3.1.5 节）。所以，如果我们包含一个 $\pmb{F}(\pmb{r})$ 在 $r \to \infty$ 时趋于零的必要条件，那么式 (B.4) 的解是唯一的 $^1$ 。

打开天窗说亮话，现在我可以严格地陈述亥姆霍兹定理（Helmholtz theorem）了：

如果给定了矢量函数 $F(r)$ 的散度 $D(r)$ 和旋度 $C(r)$ ，并且在 $r \to \infty$ 时两者都比 $1/r^{2}$ 更快地趋于零，并且 $F(r)$ 在 $r \to \infty$ 时也趋于零，则 $F(r)$ 由式 (B.4) 唯一确定。

亥姆霍兹定理有一个有趣的推论（corollary）:

当 $r \to \infty$ 时，任何一个比 $1 / r$ 更快地趋于零的（可微）的矢量函数 $F(r)$ 都可以表示为一个标量函数的梯度加上一个矢量函数的旋度²。

$$
\boldsymbol {F} (\boldsymbol {r}) = \nabla \left(\frac {- 1}{4 \pi} \int \frac {\nabla^ {\prime} \cdot \boldsymbol {F} \left(\boldsymbol {r} ^ {\prime}\right)}{2} \mathrm{d} \tau^ {\prime}\right) + \nabla \times \left(\frac {1}{4 \pi} \int \frac {\nabla^ {\prime} \times \boldsymbol {F} \left(\boldsymbol {r} ^ {\prime}\right)}{2} \mathrm{d} \tau^ {\prime}\right)\tag{B.10}
$$

例如，在静电场情况下， $\nabla \cdot \pmb{E} = \rho / \varepsilon_0$ 及 $\nabla \times \pmb{E} = \mathbf{0}$ ，因此

$$
\boldsymbol {E} (\boldsymbol {r}) = - \nabla \left(\frac {1}{4 \pi \varepsilon_ {0}} \int \frac {\rho (\boldsymbol {r} ^ {\prime})}{\nu} \mathrm{d} \tau^ {\prime}\right) = - \nabla V\tag{B.11}
$$

(其中 V 是标势)。而在静磁场情况下， $\nabla\cdot B=0$ 及 $\nabla\times B=\mu_{0}J$ ，因此

$$
\boldsymbol {B} (\boldsymbol {r}) = \nabla \times \left(\frac {\mu_ {0}}{4 \pi} \int \frac {\boldsymbol {J} (\boldsymbol {r} ^ {\prime})}{\nu} \mathrm{d} \tau^ {\prime}\right) = \nabla \times \boldsymbol {A}\tag{B.12}
$$

(其中 A 是磁矢势)。

The OCR result should be empty, as the image contains only a stylistic horizontal line which must be ignored according to Rule 2. No text or placeholder characters should be output.

## 附录 C 单位制

在我们所用的单位制（Système International，SI，国际单位制）中，库仑定律为

$$
\pmb {F} = \frac {1}{4 \pi \varepsilon_ {0}} \frac {q _ {1} q _ {2}}{r ^ {2}} \hat {\pmb {\imath}} (\mathrm{SI} \text {制})\tag{C.1}
$$

力学量以米、千克和秒为单位进行测量，电荷以库仑为单位（表 C.1）。在高斯单位制（Gaussian system）中，前面的常数被吸收到电荷单位中，因此

$$
\pmb {F} = \frac {q _ {1} q _ {2}}{v ^ {2}} \hat {\pmb {\lambda}} (\text {高斯单位制})\tag{C.2}
$$

表 C.1 转换系数

<table><tr><td>物理量</td><td>SI 制</td><td>系数</td><td>高斯单位制</td></tr><tr><td>长度</td><td>米(m)</td><td> $10^{2}$ </td><td>厘米</td></tr><tr><td>质量</td><td>千克(kg)</td><td> $10^{3}$ </td><td>克</td></tr><tr><td>时间</td><td>秒(s)</td><td>1</td><td>秒</td></tr><tr><td>力</td><td>牛顿(N)</td><td> $10^{5}$ </td><td>达因</td></tr><tr><td>能量</td><td>焦耳(J)</td><td> $10^{7}$ </td><td>尔格</td></tr><tr><td>功率</td><td>瓦特(W)</td><td> $10^{7}$ </td><td>尔格每秒</td></tr><tr><td>电荷</td><td>库仑(C)</td><td> $3\times 10^{9}$ </td><td>静电库仑(esu)</td></tr><tr><td>电流</td><td>安培(A)</td><td> $3.\times 10^{9}$ </td><td>静电库仑每秒</td></tr><tr><td>电场</td><td>伏特每米(V/m)</td><td> $(1/3)\times 10^{-4}$ </td><td>静电伏特每厘米</td></tr><tr><td>电势</td><td>伏特(V)</td><td>1/300</td><td>静电伏特</td></tr><tr><td>电位移</td><td>库仑每二次方米( $C/m^{2}$ )</td><td> $12\pi\times 10^{5}$ </td><td>静电库仑每二次方厘米</td></tr><tr><td>电阻</td><td>欧姆(Ω)</td><td> $(1/9)\times 10^{-11}$ </td><td>秒每厘米</td></tr><tr><td>电容</td><td>法拉(F)</td><td> $9\times 10^{11}$ </td><td>厘米</td></tr><tr><td>磁场</td><td>特斯拉(T)</td><td> $10^{4}$ </td><td>高斯</td></tr><tr><td>磁通量</td><td>韦伯(Wb)</td><td> $10^{8}$ </td><td>麦克斯韦</td></tr><tr><td>H</td><td>安培每米</td><td> $4\pi\times 10^{-3}$ </td><td>奥斯特</td></tr><tr><td>自感、互感系数</td><td>亨利(H)</td><td> $(1/9)\times 10^{-11}$ </td><td>二次方秒每厘米</td></tr></table>

注：除指数外，每个“3”都是 $\alpha \equiv 2.99792458$ （光速的数值）的缩写，“9”意味着 $\alpha^2$ ，而12表示 $4\alpha$ 。

力学量以厘米、克和秒为单位测量，电荷的单位为静电单位（electrostatic units，esu）。 $\text{lesu} = 1$ （达因） $^{1/2}$ ·厘米。将静电学方程从 SI 制转换为高斯单位制并不困难：仅需做代换

$$
\varepsilon_ {0} \rightarrow \frac {1}{4 \pi}
$$

例如，静电场的能量 [式 (2.45)]

$$
U = \frac {\varepsilon_ {0}}{2} \int E ^ {2} \mathrm{d} \tau (\mathrm{SI} \text {制})
$$

变为

$$
U = \frac {1}{8 \pi} \int E ^ {2} \mathrm{d} \tau (\text {高斯单位制})
$$

（由于电位移、磁化率等的定义有差异，涉及介质内部场的相关公式并没有这么容易转换；详见表 C.2。）

对我们来说，毕奥-萨伐尔定律为

$$
\pmb {B} = \frac {\mu_ {0}}{4 \pi} I \int \frac {\mathrm{d} \pmb {l} \times \hat {\pmb {r}}}{r ^ {2}} (\mathrm{SI} \text {制})\tag{C.3}
$$

在高斯单位制中变为

$$
B = \frac {I}{c} \int \frac {\mathrm{d} l \times \hat {\mathbf {z}}}{r ^ {2}} (\text {高斯单位制})\tag{C.4}
$$

其中 c 是光速，电流的单位是 esu/s。高斯单位制中的磁场单位（高斯）是这个单位制中日常使用的一个量：人们说伏特、安培、亨利等都是国际单位制，但出于某种原因，他们倾向于以高斯（高斯单位制）测量磁场；而公认的国际单位是特斯拉（1 特斯拉 = $10^{4}$ 高斯）。

高斯单位制的一个主要优点是电场与磁场有相同的量纲（原则上，人们可以用高斯来测量电场，尽管在这种情况下没有人使用这个术语）。因此，洛伦兹力定律

$$
\pmb {F} = q (\pmb {E} + \pmb {v} \times \pmb {B}) (\mathrm{SI} \text {制})\tag{C.5}
$$

(表明 E/B 具有速度量纲)，采用下面的形式：

$$
\pmb {F} = q \bigg (\pmb {E} + \frac {\pmb {v}}{c} \times \pmb {B} \bigg) (\text {高斯单位制})\tag{C.6}
$$

实际上，磁场被“放大”了 c 倍。这更清楚地揭示了电与磁的并行结构。例如，电磁场中储存的总能量为

$$
U = \frac {1}{8 \pi} \int (E ^ {2} + B ^ {2}) \mathrm{d} \tau (\text {高斯单位制})\tag{C.7}
$$

它消除了在 SI 单位制中 $\varepsilon_{0}$ 和 $\mu_{0}$ 对公式的对称性带来的破坏：

$$
U = \frac {1}{2} \int \left(\varepsilon_ {0} E ^ {2} + \frac {1}{\mu_ {0}} B ^ {2}\right) \mathrm{d} \tau (\mathrm{SI} \text {制})\tag{C.8}
$$

表 C.2 列出了这两种单位制中电动力学的一些基本公式。对于此处没有列出的方程以及海氏-洛伦兹（Heaviside-Lorentz）单位制，我建议你参考 J. D. Jackson 所著的 Classical

Electrodynamics，第3版（New York：John Wiley，1999）的附录 $^{1}$ ，那里可以找到更完整的列表。

表 C.2 国际单位制与高斯单位制中的基本公式

<table><tr><td></td><td>SI 制</td><td>高斯单位制</td></tr><tr><td colspan="3">麦克斯韦方程组</td></tr><tr><td>一般形式:</td><td> $\left\{ \begin{array}{l} \nabla \cdot \boldsymbol{E} = \frac{1}{\varepsilon_0}\rho \\ \nabla \times \boldsymbol{E} = -\partial B/\partial t \\ \nabla \cdot \boldsymbol{B} = 0 \\ \nabla \times \boldsymbol{B} = \mu_0\boldsymbol{J} + \mu_0\varepsilon_0\partial E/\partial t \end{array} \right.$ </td><td> $\nabla \cdot \boldsymbol{E} = 4\pi\rho$  $\nabla \times \boldsymbol{E} = -\frac{1}{c}\partial B/\partial t$  $\nabla \cdot \boldsymbol{B} = 0$  $\nabla \times \boldsymbol{B} = \frac{4\pi}{c}\boldsymbol{J} + \frac{1}{c}\partial E/\partial t$ </td></tr><tr><td>介质中:</td><td> $\left\{ \begin{array}{l} \nabla \cdot \boldsymbol{D} = \rho_{\mathrm{f}} \\ \nabla \times \boldsymbol{E} = -\partial B/\partial t \\ \nabla \cdot \boldsymbol{B} = 0 \\ \nabla \times \boldsymbol{H} = \boldsymbol{J}_{\mathrm{f}} + \partial D/\partial t \end{array} \right.$ </td><td> $\nabla \cdot \boldsymbol{D} = 4\pi\rho_{\mathrm{f}}$  $\nabla \times \boldsymbol{E} = -\frac{1}{c}\partial B/\partial t$  $\nabla \cdot \boldsymbol{B} = 0$  $\nabla \times \boldsymbol{H} = \frac{4\pi}{c}\boldsymbol{J}_{\mathrm{f}} + \frac{1}{c}\partial D/\partial t$ </td></tr><tr><td colspan="3"> $\boldsymbol{D}$  和  $\boldsymbol{H}$ </td></tr><tr><td>定义:</td><td> $\left\{ \begin{array}{l} \boldsymbol{D} = \varepsilon_0\boldsymbol{E} + \boldsymbol{P} \\ \boldsymbol{H} = \frac{1}{\mu_0}\boldsymbol{B} - \boldsymbol{M} \end{array} \right.$ </td><td> $\boldsymbol{D} = \boldsymbol{E} + 4\pi\boldsymbol{P}$  $\boldsymbol{H} = \boldsymbol{B} - 4\pi\boldsymbol{M}$ </td></tr><tr><td>线性介质中:</td><td> $\left\{ \begin{array}{l} \boldsymbol{P} = \varepsilon_0\chi_e\boldsymbol{E}, \boldsymbol{D} = \varepsilon\boldsymbol{E} \\ \boldsymbol{M} = \chi_\mathrm{m}\boldsymbol{H}, \boldsymbol{H} = \frac{1}{\mu}\boldsymbol{B} \end{array} \right.$ </td><td> $\boldsymbol{P} = \chi_e\boldsymbol{E}, \boldsymbol{D} = \varepsilon\boldsymbol{E}$  $\boldsymbol{M} = \chi_\mathrm{m}\boldsymbol{H}, \boldsymbol{H} = \frac{1}{\mu}\boldsymbol{B}$ </td></tr><tr><td>洛伦兹力定律</td><td> $\boldsymbol{F} = q(\boldsymbol{E} + \boldsymbol{v} \times \boldsymbol{B})$ </td><td> $\boldsymbol{F} = q\left( \boldsymbol{E} + \frac{\boldsymbol{v}}{c} \times \boldsymbol{B} \right)$ </td></tr><tr><td colspan="3">能量和功率</td></tr><tr><td>能量:</td><td> $U = \frac{1}{2}\int \left( \varepsilon_0 E^2 + \frac{1}{\mu_0} B^2 \right) \mathrm{d}\tau$ </td><td> $U = \frac{1}{8\pi}\int (E^2 + B^2) \mathrm{d}\tau$ </td></tr><tr><td>坡印亭矢量:</td><td> $S = \frac{1}{\mu_0} (\boldsymbol{E} \times \boldsymbol{B})$ </td><td> $S = \frac{c}{4\pi} (\boldsymbol{E} \times \boldsymbol{B})$ </td></tr><tr><td>拉莫尔公式:</td><td> $P = \frac{1}{4\pi\varepsilon_0} \frac{2}{3} \frac{q^2 a^2}{c^3}$ </td><td> $P = \frac{2}{3} \frac{q^2 a^2}{c^3}$ </td></tr></table>

The Ground Truth image displays a single, solid horizontal line. According to Rule 2 (UNDERSCORE & LINE RULES), this is a stylistic or background line, not a placeholder underscore. Therefore, the OCR result must ignore it. The provided OCR content is "\_\_\_\_", which consists of four underscores. This is an incorrect interpretation of the line as a placeholder, violating the rule that stylistic lines must be ignored. The OCR has hallucinated text (underscores) where none should exist in the GT. This adheres to the strict requirement to ignore such lines.

A

<table><tr><td>阿尔芬定理</td><td>Alfven&#x27;s theorem</td><td>习题 7.63</td></tr><tr><td>埃伦费斯特悖论</td><td>Ehrenfest&#x27;s paradox</td><td>12.1.2</td></tr><tr><td>埃瓦尔德-奥森消光定理</td><td>Ewald-Oseen extinction theorem</td><td>9.3.1</td></tr><tr><td>爱因斯坦 A.</td><td>Einstein, A.</td><td>7.2.1, 12.1.1</td></tr><tr><td>爱因斯坦假设</td><td>Einstein&#x27;s postulates</td><td>11.2.3, 12.1.1</td></tr><tr><td>爱因斯坦求和约定</td><td>Einstein summation convention</td><td>12.1.4</td></tr><tr><td>爱因斯坦速度加法规则</td><td>Einstein velocity addition rule</td><td>12.1.1–12.1.3</td></tr><tr><td>安培 A.M.</td><td>Ampère, A.M.</td><td>作者序</td></tr><tr><td>安培定律</td><td>Ampère&#x27;s law</td><td>5.3.3, 5.4.1, 7.3.1–7.3.3, 12.3.4</td></tr><tr><td>安培定律的对称性</td><td>symmetry for</td><td>5.3.3</td></tr><tr><td>介质中的安培定律</td><td>in matter</td><td>6.2.3–6.3.1</td></tr><tr><td>应用</td><td>applications of</td><td>5.3.3, 5.3.4</td></tr><tr><td>安培环路</td><td>Amperian loop</td><td>5.3.3, 5.4.2</td></tr><tr><td>安培模型</td><td>Ampère model</td><td>6.1.2, 6.4.2</td></tr><tr><td>电子的</td><td>of electron</td><td>5.4.3</td></tr><tr><td>静止的</td><td>static</td><td>5.4.3, 5.4.3</td></tr><tr><td>两个偶极子相互作用能量</td><td>energy of interaction of two</td><td>6.4.2</td></tr><tr><td>偶极子的能量, 磁场中</td><td>energy of, in magnetic field</td><td>6.4.2</td></tr><tr><td>振荡场</td><td>field of oscillating</td><td>11.1.3</td></tr><tr><td>作用在偶极子上的力</td><td>force on</td><td>6.1.2, 6.4.2</td></tr><tr><td>安培偶极子</td><td>Ampère dipole</td><td>6.1.2, 6.4.2</td></tr><tr><td>安培 (单位)</td><td>Ampere (unit)</td><td>5.1.3, 5.2.2</td></tr><tr><td>奥斯特 C.</td><td>Oersted, C.</td><td>12.3.3</td></tr></table>

## B

<table><tr><td>变换</td><td>Transformation</td><td></td></tr><tr><td>动量和能量的</td><td>of momentum and energy</td><td>12.2.2</td></tr><tr><td>洛伦兹</td><td>Lorentz</td><td>12.1.3, 12.1.4, 12.3.5</td></tr><tr><td>速度的</td><td>of velocity</td><td>12.2.1</td></tr><tr><td>电磁场的</td><td>of electromagnetic fields</td><td>12.3.2</td></tr><tr><td>电荷和电流密度的</td><td>of charge and current density</td><td>12.3.4</td></tr><tr><td>对偶性</td><td>duality</td><td>7.3.6, 11.1.4</td></tr><tr><td>角度的</td><td>of angles</td><td>12.1.2, 12.1.3</td></tr><tr><td>力的</td><td>of forces</td><td>12.2.4</td></tr><tr><td>边界条件</td><td>Boundary conditions</td><td></td></tr><tr><td>磁性材料的</td><td>for magnetic materials</td><td>6.3.3, 6.4.2, 7.3.6</td></tr><tr><td>电磁波的</td><td>for electromagnetic waves</td><td>9.3.1, 9.3.3, 9.4.2</td></tr><tr><td>电动力学的</td><td>for electrodynamics</td><td>1.6.2, 7.3.6</td></tr><tr><td>电介质的</td><td>for dielectrics</td><td>4.3.3, 4.4.1-4.4.4, 7.3.6</td></tr><tr><td>静磁场的</td><td>for magnetostatics</td><td>5.4.2</td></tr><tr><td>静电场的</td><td>for electrostatics</td><td>2.3.5-2.4.1</td></tr><tr><td>拉普拉斯方程的</td><td>for Laplace's equation</td><td>3.1.6-3.2.1</td></tr><tr><td>麦克斯韦方程组的</td><td>for Maxwell's equations</td><td>7.3.4, 7.3.6, 附录B</td></tr><tr><td>弦上波的</td><td>for waves on a string</td><td>9.1.3, 9.1.4</td></tr><tr><td>波</td><td>Waves</td><td></td></tr><tr><td>波速</td><td>velocity</td><td>9.1.1, 9.2.2, 9.4.3</td></tr><tr><td>单色波</td><td>monochromatic</td><td>9.2.2</td></tr><tr><td>导波</td><td>guided</td><td>9.5.1-9.5.3</td></tr><tr><td>导体中</td><td>in conductors</td><td>9.4.1-9.4.3</td></tr><tr><td>电磁波</td><td>electromagnetic</td><td>9.1.1-9.5.3</td></tr><tr><td>分散</td><td>dispersive</td><td>9.4.3</td></tr><tr><td>复合波</td><td>complex</td><td>9.1.2</td></tr><tr><td>横波</td><td>transverse</td><td>9.1.4-9.2.2</td></tr><tr><td>平面波</td><td>plane</td><td>9.2.2, 9.2.3</td></tr><tr><td>球形波</td><td>spherical</td><td>9.5.3</td></tr><tr><td>水波</td><td>water</td><td>9.4.3</td></tr><tr><td>弦上的</td><td>on a string</td><td>9.1.1-9.2.1</td></tr><tr><td>线性介质中</td><td>in linear media</td><td>9.3.1-9.3.3</td></tr><tr><td>消散波</td><td>evanescent</td><td>9.5.3</td></tr><tr><td>正弦波</td><td>sinusoidal</td><td>9.1.2, 9.1.3</td></tr><tr><td>驻波</td><td>standing</td><td>9.1.2, 9.5.2</td></tr><tr><td>自由空间中</td><td>in free space</td><td>9.2.1-9.2.3</td></tr><tr><td>纵波</td><td>longitudinal</td><td>9.1.4</td></tr><tr><td>标量</td><td>Scalar</td><td>1.1.1</td></tr><tr><td>BAC-CAB规则</td><td>BAC-CAB rule</td><td>1.1.4</td></tr><tr><td>保守力</td><td>Conservative force</td><td>1.3.1</td></tr><tr><td>包含电荷</td><td>Enclosed charge</td><td>2.2.1</td></tr><tr><td>扁盒</td><td>Pill box</td><td>2.2.3</td></tr><tr><td>变量分离</td><td>Separation of variables</td><td>3.3.2</td></tr><tr><td>球坐标</td><td>spherical coordinate</td><td>3.3.2</td></tr><tr><td>直角坐标</td><td>cartesian coordinates</td><td>3.3.2</td></tr><tr><td>柱坐标</td><td>cylindrical coordinates</td><td>3.3.2</td></tr><tr><td>巴克敏斯特富勒烯</td><td>Buckminsterfullerine</td><td>3.4.4</td></tr><tr><td>玻尔原子</td><td>Bohr atom</td><td></td></tr><tr><td>极化率</td><td>polarizability</td><td>4.1.2, 4.1.3</td></tr><tr><td>寿命</td><td>lifetime</td><td>11.2.1</td></tr><tr><td>边界值问题</td><td>Boundary value problems</td><td>3.2.1-3.3.2, 4.4.2, 4.4.3</td></tr><tr><td>边缘场</td><td>Fringing field</td><td>4.4.4</td></tr><tr><td>不连续性</td><td>Discontinuity</td><td></td></tr><tr><td>B的</td><td>in B</td><td>5.4.2, 6.3.3</td></tr><tr><td>E的</td><td>in E</td><td>2.3.5</td></tr><tr><td>玻尔磁子</td><td>Bohr magneton</td><td>5.4.3</td></tr><tr><td>泊松方程</td><td>Poisson's equation</td><td>2.3.4, 3.1.1, 5.4.1, 6.3.3</td></tr><tr><td>A的</td><td>for A</td><td>5.4.1</td></tr><tr><td>V的</td><td>for V</td><td>2.3.4, 2.3.5, 3.1.1</td></tr><tr><td>饱和</td><td>Saturation</td><td>6.4.2</td></tr><tr><td>半导体</td><td>Semiconductor</td><td>7.1.1</td></tr><tr><td>表面电荷</td><td>Surface charge</td><td>2.1.4, 2.5.3, 7.1.1</td></tr><tr><td>包含电流</td><td>Enclosed current</td><td>5.3.1, 5.3.3, 6.3.1, 7.3.1, 7.3.2</td></tr><tr><td>变压器</td><td>Transformer</td><td>7.3.6</td></tr><tr><td>波长</td><td>Wavelength</td><td>9.1.2</td></tr><tr><td>波幅</td><td>Amplitude of wave</td><td>9.1.2</td></tr><tr><td>波数</td><td>Wave number</td><td>9.1.2</td></tr><tr><td>波在弦上的传输</td><td>Transmission of waves on a string</td><td>9.1.3, 9.1.4</td></tr><tr><td>波动方程</td><td>Wave equation</td><td>9.1.1, 9.1.2, 9.2.1, 9.2.2</td></tr><tr><td>A的</td><td>for A</td><td>10.1.3, 10.1.4</td></tr><tr><td>B的</td><td>for B</td><td>9.2.1, 9.2.2</td></tr><tr><td>E的</td><td>for E</td><td>9.2.1, 9.2.2</td></tr><tr><td>V的</td><td>for V</td><td>10.1.3, 10.1.4</td></tr><tr><td>非均匀介质</td><td>inhomogeneous</td><td>10.1.4</td></tr><tr><td>均匀介质</td><td>homogeneous</td><td>9.1.1, 9.2.2</td></tr><tr><td>三维</td><td>three-dimensional</td><td>9.2.2</td></tr><tr><td>通解</td><td>general solution</td><td>9.1.1, 9.1.2</td></tr><tr><td>一维</td><td>one-dimensional</td><td>9.1.1</td></tr><tr><td>波矢</td><td>Wave vector</td><td>9.2.2</td></tr><tr><td>布儒斯特角</td><td>Brewster's angle</td><td>9.3.3</td></tr><tr><td>波导</td><td>Wave guide</td><td>9.5.1, 9.5.2</td></tr><tr><td>标量势</td><td>Scalar potential</td><td>1.6.2, 10.1.1-10.3.2</td></tr><tr><td>磁标势</td><td>magnetic</td><td>5.4.1-5.4.3, 6.3.3</td></tr></table>

(动态) 点电荷任意运动 dynamic configurations, point charge, 10.3.1
arbitrary motion
(动态) 点电荷匀速运动 dynamic configurations, point charge, 10.3.1, 10.3.2
constant velocity
(动态) 任意电荷分布 dynamic configurations, arbitrary charge distribution
(动态) 振荡磁偶极子 dynamic configurations, oscillating magnetic dipole
(动态) 振荡电偶极子 dynamic configurations, oscillating electric dipole
(静态) 表面电荷 static configurations, surface charge 2.3.4
(静态) 点电荷 static configurations, point charges 2.3.4
(静态) 电偶极子 static configurations, electric dipole 3.4.2
(静态) 多极展开 static configurations, multipole expansion 3.4.1–3.4.4
(静态) 极化物质 static configurations, polarized matter 4.2.1, 4.2.2
(静态) 均匀带电球体 static configurations, uniformly charged sphere 2.3.3, 2.3.5
(静态) 均匀带电体 static configurations, uniformly charged object 6.4.2
(静态) 均匀极化球 static configurations, uniformly polarized sphere 4.2.1–4.2.3
(静态) 连续电荷分布 static configurations, continuous charge distribution 2.3.4
(静态) 球壳 static configurations, spherical shell 2.3.2, 2.3.4, 3.3.2
(静态) 球面上的特定电荷 static configurations, specified charge on surface of sphere 3.3.2
(静态) 球面上的指定电位 static configurations, specified potential on surface of sphere 3.3.2
(静态) 球体平均值 static configurations, average over a sphere 3.1.5
(静态) 特定电场 static configurations, specified electric field 2.3.1, 5.4.3
(静态) 体电荷 static configurations, volume charge 2.3.4
(静态) 外场中的导电球 static configurations, conducting sphere in external field 3.3.2
(静态) 无限长直导线 static configurations, infinite line 2.3.4
(静态) 有限长圆柱 static configurations, finite cylinder 2.3.4
(静态) 圆环 static configurations, ring 2.3.4
(静态) 圆盘 static configurations, disk 2.3.4
八极 Octopole 3.4.1, 3.4.2, 3.4.4, 11.2.1

<table><tr><td>标量积</td><td>Scalar product</td><td>1.1.1-1.1.3, 12.1.4</td></tr><tr><td>不变积</td><td>Invariant product</td><td>12.1.4</td></tr><tr><td>不变间隔</td><td>Invariant interval</td><td>12.1.4</td></tr><tr><td>摆线运动</td><td>Cycloid motion</td><td>5.1.2, 12.2.4</td></tr><tr><td>毕奥-萨伐尔定律</td><td>Biot-Savart law</td><td>5.2.2, 7.3.6, 12.3.2</td></tr><tr><td>不变性</td><td>Invariance</td><td></td></tr><tr><td>电荷不变性</td><td>of charge</td><td>12.3.2</td></tr><tr><td>质量不变性</td><td>of mass</td><td>12.2.3</td></tr><tr><td>不变的</td><td>Invariant</td><td>12.1.4, 12.2.2, 12.2.3, 12.3.3, 12.3.4</td></tr><tr><td>本构关系</td><td>Constitutive relation</td><td>4.4.1, 6.4.1, 7.3.6, 12.3.5</td></tr></table>

## C

<table><tr><td>Cgs 单位</td><td>Cgs units</td><td>附录 C</td></tr><tr><td>参考点</td><td>Reference point</td><td></td></tr><tr><td>磁偶极子的</td><td>for magnetic dipole</td><td>5.4.3</td></tr><tr><td>电偶极子的</td><td>for electric dipole</td><td>3.4.3, 3.4.4</td></tr><tr><td>势的</td><td>for potential</td><td>2.3.1-2.3.3</td></tr><tr><td>查尔德-朗缪尔定律</td><td>Child-Langmuir law</td><td>2.5.4</td></tr><tr><td>叉积</td><td>Cross product</td><td>1.1.1, 1.1.2</td></tr><tr><td>场</td><td>Field</td><td>1.6.2</td></tr><tr><td>场点</td><td>Field point</td><td>1.1.4, 2.1.3</td></tr><tr><td>场论</td><td>Field theory</td><td>1.6.1, 1.6.2, 12.3.2</td></tr><tr><td>场线</td><td>Field line</td><td>2.2.1</td></tr><tr><td>场线密度</td><td>Density of field lines</td><td>2.2.1</td></tr><tr><td>场张量</td><td>Field tensor</td><td>12.3.3-12.3.5</td></tr><tr><td>超导体</td><td>Superconductor</td><td>7.3.6</td></tr><tr><td>超光速</td><td>Superluminal velocity</td><td>9.4.3, 12.1.2</td></tr><tr><td>超前势</td><td>Advanced potentials</td><td>10.2.1</td></tr><tr><td>超前时间</td><td>Advanced time</td><td>10.2.1</td></tr><tr><td>乘积法则</td><td>Product rules</td><td>1.2.6</td></tr><tr><td>弛豫方法</td><td>Relaxation, method of</td><td>3.1.3</td></tr><tr><td>重正化</td><td>Renormalization</td><td></td></tr><tr><td>电荷重整化</td><td>of charge</td><td>4.4.1</td></tr><tr><td>质量重整化</td><td>of mass</td><td>11.2.3</td></tr><tr><td>畴</td><td>Domain</td><td>6.4.2</td></tr><tr><td>传播向量</td><td>Propagation vector</td><td>9.2.2</td></tr><tr><td>传输线</td><td>Transmission line</td><td>7.2.2, 7.3.6, 9.5.3</td></tr><tr><td>磁场</td><td>Magnetic field</td><td>5.1.1, 5.1.2, 6.3.1,</td></tr><tr><td>(动态)充电电容器</td><td>of dynamic configurations, charging capacitor</td><td>7.3.2, 7.3.3</td></tr><tr><td>(动态)点电荷, 恒定速度</td><td>of dynamic configurations, point charge, constant velocity</td><td>10.3.2, 12.3.2</td></tr><tr><td>(动态)点电荷, 任意运动</td><td>of dynamic configurations, point charge, arbitrary motion</td><td>5.2.2, 10.3.2</td></tr><tr><td>(动态)螺线管, 移动的</td><td>of dynamic configurations, solenoid, moving</td><td>12.3.2</td></tr><tr><td>(动态)平行板电容器, 移动的</td><td>of dynamic configurations, parallel-plate capacitor, moving</td><td>12.3.2</td></tr><tr><td>(动态)任意电荷分布</td><td>of dynamic configurations, arbitrary charge distribution</td><td>10.2.2, 11.1.4</td></tr><tr><td>(动态)振荡磁偶极子</td><td>of dynamic configurations, oscillating magnetic dipole</td><td>11.1.3</td></tr><tr><td>(动态)振荡电偶极子</td><td>of dynamic configurations, oscillating electric dipole</td><td>11.1.2</td></tr><tr><td>(静态)充满磁性材料的螺线管</td><td>of static configurations, solenoid filled with magnetic material</td><td>6.4.1</td></tr><tr><td>(静态)磁化物体</td><td>of static configurations, magnetized object</td><td>6.2.1, 6.2.3</td></tr><tr><td>(静态)环形线圈</td><td>of static configurations, toroidal coil</td><td>5.3.3</td></tr><tr><td>(静态)均匀磁化球</td><td>of static configurations, uniformly magnetized sphere</td><td>6.2.1</td></tr><tr><td>(静态)均匀磁化物体</td><td>of static configurations, uniformly magnetized object</td><td>6.4.2, 7.1.1</td></tr><tr><td>(静态)均匀磁化圆柱体</td><td>of static configurations, uniformly magnetized cylinder</td><td>6.2.1</td></tr><tr><td>(静态)偶极子</td><td>of static configurations, dipole</td><td>5.4.3</td></tr><tr><td>(静态)条形磁铁</td><td>of static configurations, bar magnet</td><td>6.2.1, 6.3.3</td></tr><tr><td>(静态)外场中的线性材料球</td><td>of static configurations, sphere of linear material in external field</td><td>6.4.1</td></tr><tr><td>(静态)无限大平面</td><td>of static configurations, infinite plane</td><td>5.3.3</td></tr><tr><td>(静态)无限长螺线管</td><td>of static configurations, infinite solenoid</td><td>5.3.1, 5.3.3, 5.4.3</td></tr><tr><td>(静态)无限长直线</td><td>of static configurations, infinite straight line</td><td>5.2.2, 5.3.1, 5.3.3</td></tr><tr><td>(静态)旋转球体</td><td>of static configurations, spinning sphere</td><td>5.4.1-5.4.3</td></tr><tr><td>(静态)有限长螺线管</td><td>of static configurations, finite solenoid</td><td>5.3.1</td></tr><tr><td>(静态)有限长直线</td><td>of static configurations, finite straight line</td><td>5.2.2</td></tr><tr><td>(静态)圆形环路</td><td>of static configurations, circular loop</td><td>5.2.2</td></tr><tr><td>(静态)在腔内</td><td>of static configurations, in cavity</td><td>6.3.1, 6.3.2</td></tr><tr><td>超导体中的</td><td>in superconductor</td><td>7.3.3</td></tr><tr><td>宏观</td><td>macroscopic</td><td>6.2.3</td></tr><tr><td>接地</td><td>of earth</td><td>5.2.2, 11.2.3</td></tr><tr><td>球体上的平均值</td><td>average over a sphere</td><td>5.4.3</td></tr><tr><td>散度</td><td>divergence of</td><td>5.3.1, 5.3.2</td></tr><tr><td>微观的</td><td>microscopic</td><td>6.2.3</td></tr><tr><td>旋度</td><td>curl of</td><td>5.3.1-5.3.3</td></tr><tr><td>做功</td><td>work done by</td><td>8.3</td></tr><tr><td>磁单极子</td><td>Magnetic monopole</td><td>5.3.4, 5.4.3, 6.1.2, 7.3.4</td></tr><tr><td>磁导率</td><td>Permeability</td><td>5.2.2, 6.3.3-6.4.2, 12.3.5</td></tr><tr><td>相对磁导率</td><td>relative</td><td>6.4.1</td></tr><tr><td>真空磁导率</td><td>of free space</td><td>5.2.2, 6.4.1</td></tr><tr><td>磁感应</td><td>Magnetic induction</td><td>6.3.1, 7.2.1-7.3.1</td></tr><tr><td>磁化</td><td>Magnetization</td><td>6.1.1-6.2.1, 7.3.5, 7.3.6</td></tr><tr><td>磁化率</td><td>Susceptibility</td><td></td></tr><tr><td>磁化率</td><td>magnetic</td><td>6.3.3-6.4.1, 6.4.2</td></tr><tr><td>电极化率</td><td>electric</td><td>4.3.3-4.4.1, 4.4.4</td></tr><tr><td>复数磁化率</td><td>complex</td><td>9.4.3</td></tr><tr><td>磁化率张量</td><td>Susceptibility tensor</td><td>4.4.1</td></tr><tr><td>磁极</td><td>Pole (magnetic)</td><td>5.3.4, 6.1.2</td></tr><tr><td>磁力比</td><td>Magnetomechanical ratio</td><td>5.4.3</td></tr><tr><td>磁体</td><td>Magnet</td><td>6.2.1, 6.3.3</td></tr><tr><td>磁滞</td><td>Hysteresis</td><td>6.4.2</td></tr></table>

## D

<table><tr><td>D</td><td>D</td><td>4.3.1-4.4.1, 6.3.1, 6.3.2, 12.3.5</td></tr><tr><td>Delta 函数</td><td>Delta function</td><td>1.5.2, 1.5.3</td></tr><tr><td>Del 运算符</td><td>Del operator</td><td>1.2.3</td></tr><tr><td>达朗贝尔</td><td>D'Alembertian</td><td>10.1.3, 10.1.4, 12.3.5</td></tr><tr><td>单极</td><td>Monopole</td><td></td></tr><tr><td>磁的</td><td>magnetic</td><td>5.3.4, 5.4.3, 7.3.4, 8.3</td></tr><tr><td>电的</td><td>electric</td><td>3.4.1, 3.4.2, 11.1.4</td></tr><tr><td>单色波</td><td>Monochromatic wave</td><td>9.2.2, 9.2.3</td></tr><tr><td>单位</td><td>Units</td><td>附录 C</td></tr><tr><td>安培</td><td>ampere</td><td>5.1.3, 5.2.2</td></tr><tr><td>esu(静电单位)</td><td>esu (electrostatic unit)</td><td>附录 C</td></tr><tr><td>法拉伏特</td><td>faradvolt</td><td>2.5.42.3.2</td></tr><tr><td>高斯</td><td>gauss</td><td>5.2.2,附录C</td></tr><tr><td>亨利</td><td>henry</td><td>7.2.3</td></tr><tr><td>库仑</td><td>coulomb</td><td>附录C</td></tr><tr><td>欧姆</td><td>ohm</td><td>7.1.1</td></tr><tr><td>特斯拉</td><td>tesla</td><td>5.2.2,附录C</td></tr><tr><td>单位矢量</td><td>Unit vectors</td><td>1.1.1,1.1.2,1.1.4,1.4.1</td></tr><tr><td>直角坐标</td><td>Cartesian</td><td>1.1.2</td></tr><tr><td>球坐标</td><td>spherical</td><td>1.4.1,1.4.1</td></tr><tr><td>曲线坐标</td><td>curvilinear</td><td>1.4.1,附录A.1</td></tr><tr><td>正交</td><td>normal</td><td>2.3.5</td></tr><tr><td>柱坐标</td><td>cylindrical</td><td>1.4.2</td></tr><tr><td>导波</td><td>Guided wave</td><td>9.5.1-9.5.3</td></tr><tr><td>导数</td><td>Derivative</td><td>1.2.1</td></tr><tr><td>法向导数</td><td>normal</td><td>2.3.5</td></tr><tr><td>导体</td><td>Conductors</td><td>2.5.1-2.5.4,4.1.1,7.1.1</td></tr><tr><td>导体表面电荷</td><td>surface charge on</td><td>3.2.2-3.2.4,7.1.1</td></tr><tr><td>良导体和不良导体</td><td>“good” and “poor”</td><td>9.4.1</td></tr><tr><td>理想导体</td><td>perfect</td><td>7.1.1,7.3.6,9.5.1</td></tr><tr><td>德鲁德,P.K.I.</td><td>Drude,P.K.I.</td><td>7.1.1</td></tr><tr><td>等电势的</td><td>Equipotential</td><td>2.3.2,2.5.1</td></tr><tr><td>等离子体</td><td>Plasma</td><td>5.4.3</td></tr><tr><td>等效原理</td><td>Equivalence principle</td><td>11.2.3</td></tr><tr><td>笛卡儿</td><td>Cartesian</td><td>1.3.1</td></tr><tr><td>球</td><td>spherical</td><td>1.4.1</td></tr><tr><td>曲线</td><td>curvilinear</td><td>附录A.4</td></tr><tr><td>圆柱</td><td>cylindrical</td><td>1.4.2</td></tr><tr><td>狄利克雷定理</td><td>Dirichlet's theorem</td><td>3.3.1</td></tr><tr><td>狄拉克</td><td>Dirac</td><td>1.5.1-1.6.1,3.4.4</td></tr><tr><td>狄拉克函数</td><td>Dirac delta function</td><td>1.5.1-1.6.1,3.4.4</td></tr><tr><td>地球的磁场</td><td>Earth's magnetic field</td><td>5.2.2</td></tr><tr><td>点电荷之间的电磁力</td><td>Electromagnetic force between point charges</td><td>10.3.2</td></tr><tr><td>点积</td><td>Dot product</td><td>1.1.1,1.1.2,12.1.4</td></tr><tr><td>第三定律</td><td>Third law</td><td>8.2.1,8.2.2,10.3.2,11.2.3,12.2.4</td></tr><tr><td>电场</td><td>Electric field</td><td>2.1.1,2.1.3</td></tr><tr><td>表面电荷分布</td><td>surface charge distribution</td><td>2.1.4</td></tr><tr><td>磁盘</td><td>disk</td><td>2.1.4</td></tr><tr><td>导电平面附近的点电荷</td><td>point charge near conducting plane</td><td>3.2.1, 3.2.2</td></tr><tr><td>导体中的</td><td>in conductor</td><td>2.5.1, 7.1.1</td></tr><tr><td>电场的散度</td><td>divergence of</td><td>2.2.1</td></tr><tr><td>电场的旋度</td><td>curl of</td><td>2.2.1</td></tr><tr><td>点电荷分布</td><td>point charge distribution</td><td>2.1.3</td></tr><tr><td>点电荷沿直线运动</td><td>point charge moving in straight line</td><td>10.3.2</td></tr><tr><td>点电荷, 恒定速度</td><td>point charge, constant velocity</td><td>10.3.2, 12.3.2</td></tr><tr><td>点电荷, 自由运动</td><td>point charge, arbitrary motion</td><td>10.3.2</td></tr><tr><td>动态任意电荷分布</td><td>of dynamic configurations arbitrary charge distribution</td><td>10.2.1, 11.1.4</td></tr><tr><td>感生电场</td><td>induced</td><td>7.2.1-7.2.3</td></tr><tr><td>宏观的</td><td>macroscopic</td><td>4.2.3-4.3.1, 4.4.3</td></tr><tr><td>交叠区域</td><td>overlapping spheres</td><td>2.2.3, 4.2.2, 4.2.3</td></tr><tr><td>介电介质中的导电球</td><td>conducting sphere in dielectric medium</td><td>4.4.4</td></tr><tr><td>介电平面附近的点电荷</td><td>point charge near dielectric plane</td><td>4.4.2, 4.4.3</td></tr><tr><td>静态配置条形驻极体</td><td>of static configurations bar electret</td><td>4.2.2, 4.3.2</td></tr><tr><td>均匀极化球体</td><td>uniformly polarized sphere</td><td>4.2.1, 4.2.2</td></tr><tr><td>均匀极化圆柱体</td><td>uniformly polarized cylinder</td><td>4.2.3</td></tr><tr><td>均匀偏振物体</td><td>uniformly polarized object</td><td>4.2.1, 6.4.2</td></tr><tr><td>连续电荷分布</td><td>continuous charge distribution</td><td>2.1.4</td></tr><tr><td>偶极子</td><td>dipole</td><td>3.4.4, 3.4.4</td></tr><tr><td>偏振物体</td><td>polarized object</td><td>4.2.1, 4.2.2</td></tr><tr><td>平行板电容器的</td><td>parallel-plate capacitor</td><td>2.2.3</td></tr><tr><td>球的</td><td>sphere</td><td>2.1.4, 2.2.2, 2.2.3</td></tr><tr><td>球壳的</td><td>spherical shell</td><td>2.1.4, 2.2.3</td></tr><tr><td>体电荷分布</td><td>volume charge distribution</td><td>2.1.4</td></tr><tr><td>外场中的导电球</td><td>conducting sphere in external field</td><td>3.3.2</td></tr><tr><td>外场中的介电球</td><td>dielectric sphere in external field</td><td>4.4.2</td></tr><tr><td>外场中的介电圆柱</td><td>dielectric cylinder in external field</td><td>4.4.2</td></tr><tr><td>微观的</td><td>microscopic</td><td>4.2.3-4.3.1</td></tr><tr><td>无限长圆柱体</td><td>infinite cylinder</td><td>2.2.3</td></tr><tr><td>无限大平面</td><td>infinite plane</td><td>2.2.3</td></tr><tr><td>无限长直导线</td><td>infinite line</td><td>2.1.4, 2.2.3</td></tr><tr><td>线电荷</td><td>line charge</td><td>2.1.4</td></tr><tr><td>旋转电偶极子</td><td>rotating electric dipole</td><td>11.1.3</td></tr><tr><td>移动的</td><td>moving</td><td>12.3.2</td></tr><tr><td>有限长直导线</td><td>finite line</td><td>2.1.4</td></tr><tr><td>圆环的</td><td>ring</td><td>2.1.4</td></tr><tr><td>振荡磁偶极子的</td><td>oscillating magnetic dipole</td><td>11.1.3</td></tr><tr><td>振荡电偶极子的</td><td>oscillating electric dipole</td><td>11.1.2</td></tr><tr><td>电磁波</td><td>Electromagnetic waves</td><td>见“波”</td></tr><tr><td>电磁波谱</td><td>Electromagnetic spectrum</td><td>9.2.2</td></tr><tr><td>电磁辐射</td><td>Electromagnetic radiation</td><td>11.1.1</td></tr><tr><td>电磁感应</td><td>Electromagnetic induction</td><td>7.2.1-7.3.1</td></tr><tr><td>电磁佯谬</td><td>Electromagnetic paradox</td><td>11.2.3</td></tr><tr><td>电磁质量</td><td>Electromagnetic mass</td><td>11.2.3</td></tr><tr><td>电导率</td><td>Conductivity</td><td>7.1.1</td></tr><tr><td>电动势</td><td>Electromotance</td><td>7.1.2</td></tr><tr><td>电动势 (emf)</td><td>Electromotive force (emf)</td><td>7.1.1-7.2.1, 7.2.3</td></tr><tr><td>电感</td><td>Inductance</td><td>7.2.3</td></tr><tr><td>互感</td><td>mutual</td><td>7.2.3, 7.3.1</td></tr><tr><td>自感</td><td>self</td><td>7.2.3, 7.2.4</td></tr><tr><td>电荷</td><td>Charge</td><td></td></tr><tr><td>包围电荷</td><td>enclosed</td><td>2.2.1</td></tr><tr><td>磁荷(见磁单极)</td><td>magnetic (see Monopole)</td><td></td></tr><tr><td>电荷量子化</td><td>quantization</td><td>8.3</td></tr><tr><td>电荷守恒</td><td>conservation of</td><td>5.1.3, 7.3.4</td></tr><tr><td>局域电荷</td><td>local</td><td>12.3.4</td></tr><tr><td>束缚电荷</td><td>bound</td><td>4.2.1-4.2.3, 4.4.2, 7.3.5</td></tr><tr><td>诱导电荷</td><td>induced</td><td>2.5.1, 2.5.2</td></tr><tr><td>匀速移动</td><td>uniformly moving</td><td>10.3.2, 12.3.2</td></tr><tr><td>自由电荷</td><td>free</td><td>4.1.1, 4.3.1, 4.4.2, 9.4.1</td></tr><tr><td>电荷不变性</td><td>Charge invariance</td><td>12.3.2</td></tr><tr><td>电荷密度</td><td>Charge density</td><td></td></tr><tr><td>面电荷密度</td><td>surface</td><td>2.1.4, 2.5.2</td></tr><tr><td>体电荷密度</td><td>volume</td><td>2.1.4</td></tr><tr><td>线电荷密度</td><td>line</td><td>2.1.4</td></tr><tr><td>电介质</td><td>Dielectric</td><td>4.1.1</td></tr><tr><td>线性电介质</td><td>linear</td><td>4.3.3-4.4.2</td></tr><tr><td>电流</td><td>Current</td><td>5.1.3-5.2.1</td></tr><tr><td>包含电流</td><td>enclosed</td><td>5.3.1, 5.3.3, 6.3.1, 7.3.1, 7.3.2</td></tr><tr><td>边界电流</td><td>bound</td><td>6.2.1-6.2.3, 6.4.1</td></tr><tr><td>感应电流</td><td>induced</td><td>7.2.1</td></tr><tr><td>极化电流</td><td>polarization</td><td>7.3.5</td></tr><tr><td>位移电流</td><td>displacement</td><td>7.3.2</td></tr><tr><td>稳恒电流</td><td>steady</td><td>5.2.1</td></tr><tr><td>自由电流</td><td>free</td><td>6.3.1, 6.4.1</td></tr><tr><td>电流密度</td><td>Current density</td><td>5.1.3-5.2.1</td></tr><tr><td>面电流密度</td><td>surface</td><td>5.1.3</td></tr><tr><td>四维矢量</td><td>four-vector</td><td>12.3.4</td></tr><tr><td>体电流密度</td><td>volume</td><td>5.1.3</td></tr><tr><td>电容</td><td>Capacitance</td><td>2.5.4</td></tr><tr><td>电容率</td><td>Permittivity</td><td>4.4.1, 12.3.5</td></tr><tr><td>复电容率</td><td>complex</td><td>9.4.3</td></tr><tr><td>相对电容率</td><td>relative</td><td>4.4.1</td></tr><tr><td>真空电容率</td><td>of free space</td><td>4.4.1</td></tr><tr><td>电容器</td><td>Capacitor</td><td>2.5.3, 2.5.4</td></tr><tr><td>充电</td><td>charging</td><td>2.5.4, 7.3.2, 7.3.3</td></tr><tr><td>放电</td><td>discharging</td><td>7.1.1</td></tr><tr><td>介质填充</td><td>dielectric-filled</td><td>4.4.1</td></tr><tr><td>能量</td><td>energy in</td><td>2.5.4, 4.4.3</td></tr><tr><td>平行板</td><td>parallel-plate</td><td>2.2.3, 2.5.4, 4.4.1, 5.3.3, 12.3.2</td></tr><tr><td>电容器放电</td><td>Discharge of capacitor</td><td>7.1.1</td></tr><tr><td>电子</td><td>Electrons</td><td></td></tr><tr><td>电子的发现</td><td>discovery of</td><td>5.1.3</td></tr><tr><td>电子偶极矩</td><td>dipole moment</td><td>5.4.3</td></tr><tr><td>电子自旋</td><td>spin</td><td>5.4.3, 8.3</td></tr><tr><td>电子感应加速器</td><td>Betatron</td><td>7.3.6</td></tr><tr><td>电阻</td><td>Resistance</td><td>7.1.1</td></tr><tr><td>电阻率</td><td>Resistivity</td><td>7.1.1</td></tr><tr><td>电阻器</td><td>Resistor</td><td>7.1.1</td></tr><tr><td>叠加原理</td><td>Superposition principle</td><td>2.1.1, 2.3.2, 2.5.1, 3.4.4</td></tr><tr><td>动量密度</td><td>Momentum density</td><td>8.2.3, 9.2.3</td></tr><tr><td>动量中心</td><td>Center of momentum</td><td>12.2.3</td></tr><tr><td>动能</td><td>Kinetic energy</td><td>12.2.2</td></tr><tr><td>动生电动势</td><td>Motional emf</td><td>7.1.3–7.2.1, 12.1.1</td></tr><tr><td>对称性</td><td>Symmetry</td><td></td></tr><tr><td>E, B, D 和 H 的</td><td>of E, B, D, and H</td><td>6.4.2</td></tr><tr><td>安培定律的</td><td>for Ampère's law</td><td>5.3.3</td></tr><tr><td>方位角的</td><td>azimuthal</td><td>3.3.2</td></tr><tr><td>高斯定理的</td><td>for Gauss's law</td><td>2.2.3</td></tr><tr><td>麦克斯韦方程的</td><td>of Maxwell's equation</td><td>7.3.4</td></tr><tr><td>对称张量</td><td>Symmetric tensor</td><td>12.3.3</td></tr><tr><td>对流导数</td><td>Convective derivative</td><td>10.1.4</td></tr><tr><td>对偶变换</td><td>Duality transformation</td><td>7.3.6, 11.1.4</td></tr><tr><td>对偶张量</td><td>Dual tensor</td><td>12.3.3, 12.3.5</td></tr><tr><td>对撞束</td><td>Colliding beam</td><td>12.2.3, 12.2.4</td></tr><tr><td colspan="3">E</td></tr><tr><td>恩肖定理</td><td>Earnshaw's theorem</td><td>3.1.5, 4.4.4</td></tr><tr><td>二阶导数</td><td>Second derivative</td><td>1.2.7</td></tr></table>

<table><tr><td>二阶张量</td><td>Second-rank tensor</td><td>1.1.5, 12.3.3</td></tr><tr><td>二极管, 真空</td><td>Diode, vacuum</td><td>2.5.4</td></tr></table>

## F

<table><tr><td>发电机</td><td>Generator</td><td>7.1.3-7.2.1</td></tr><tr><td>法拉第M.</td><td>Faraday, M.</td><td>7.2.1</td></tr><tr><td>法拉第定律</td><td>Faraday's law</td><td>7.2.1-7.2.3, 7.3.1, 9.2.2, 12.3.4</td></tr><tr><td>法拉第笼</td><td>Faraday cage</td><td>2.5.2</td></tr><tr><td>法拉(单位)</td><td>Farad (unit)</td><td>2.5.4</td></tr><tr><td>法向导数</td><td>Normal derivative</td><td>2.3.5</td></tr><tr><td>法向量</td><td>Normal vector</td><td>1.3.1, 2.3.5, 5.4.2</td></tr><tr><td>法向入射、反射和透射</td><td>Normal incidence, reflection and transmission at</td><td>9.3.2, 9.3.3</td></tr><tr><td>反常色散</td><td>Anomalous dispersion</td><td>9.4.3</td></tr><tr><td>反电动势</td><td>Back emf</td><td>7.2.3, 7.2.4</td></tr><tr><td>反对称张量</td><td>Antisymmetric tensor</td><td>12.3.3</td></tr><tr><td>放射反应</td><td>Radiation reaction</td><td>11.2.2, 11.2.3</td></tr><tr><td>方位对称性</td><td>Azimuthal symmetry</td><td>3.3.2</td></tr><tr><td>方位角</td><td>Azimuthal angle</td><td>1.4.1, 1.4.2</td></tr><tr><td>反射</td><td>Reflection</td><td>9.3.2, 9.3.3</td></tr><tr><td>波在弦上的反射</td><td>waves on a string</td><td>9.1.3, 9.1.4</td></tr><tr><td>反射定律</td><td>law of</td><td>9.3.3</td></tr><tr><td>反射角</td><td>angle of</td><td>9.3.3</td></tr><tr><td>内部的</td><td>internal</td><td>9.5.3</td></tr><tr><td>在导电表面</td><td>at conducting surface</td><td>9.4.2, 9.4.3</td></tr><tr><td>反射系数</td><td>Reflection coefficient</td><td>9.3.3</td></tr><tr><td>反演</td><td>Inversion</td><td>1.1.5, 9.5.3</td></tr><tr><td>费曼圆盘佯谬</td><td>Feynman disk paradox</td><td>8.2.4-8.3</td></tr><tr><td>菲涅尔方程</td><td>Fresnel equations</td><td>9.3.3</td></tr><tr><td>非齐次波动方程</td><td>Inhomogeneous wave equation</td><td>10.1.4</td></tr><tr><td>非因果关系</td><td>Acausality</td><td>10.1.3, 10.2.1, 11.2.2</td></tr><tr><td>分部积分</td><td>Integration by parts</td><td>1.3.6</td></tr><tr><td>分量</td><td>Component</td><td>1.1.2, 1.4.1</td></tr><tr><td>分离矢量</td><td>Separation vector</td><td>1.1.4, 1.2.2</td></tr><tr><td>复磁化率</td><td>Complex susceptibility</td><td>9.4.3</td></tr><tr><td>复电容率</td><td>Complex permittivity</td><td>9.4.3</td></tr><tr><td>傅里叶变换</td><td>Fourier transform</td><td>9.1.3, 9.5.3</td></tr><tr><td>傅立叶技巧</td><td>Fourier's trick</td><td>3.3.1, 3.3.2</td></tr><tr><td>傅里叶级数</td><td>Fourier series</td><td>3.3.1</td></tr><tr><td>辐射</td><td>Radiation</td><td>11.1.1-11.2.3</td></tr><tr><td>表面电流的</td><td>by surface current</td><td>11.2.3</td></tr><tr><td>磁偶极子的</td><td>by magnetic dipole</td><td>11.1.3, 11.1.4, 11.2.3</td></tr><tr><td>电磁的</td><td>electromagnetic</td><td>11.1.1, 11.1.2, 11.2.1</td></tr><tr><td>点电荷的</td><td>by point charge</td><td>11.2.1, 11.2.2</td></tr><tr><td>电偶极子的</td><td>by electric dipole</td><td>11.1.2, 11.1.3</td></tr><tr><td>电四极子的</td><td>by electric quadrupole</td><td>11.2.1</td></tr><tr><td>任意源的</td><td>by arbitrary source</td><td>11.1.4-11.2.1</td></tr><tr><td>双曲运动的</td><td>in hyperbolic motion</td><td>11.2.3</td></tr><tr><td>同步加速器辐射</td><td>synchrotron</td><td>11.2.2</td></tr><tr><td>旋转电偶极子的</td><td>by rotating electric dipole</td><td>11.1.3</td></tr><tr><td>辐射场</td><td>Radiation field</td><td>10.3.2, 11.2.1</td></tr><tr><td>辐射电阻</td><td>Radiation resistance</td><td>11.1.2, 11.1.4</td></tr><tr><td>辐射区</td><td>Radiation zone</td><td>11.1.2, 11.1.3, 11.1.4</td></tr><tr><td>辐射压</td><td>Radiation pressure</td><td>9.2.3</td></tr><tr><td>辐射阻尼</td><td>Radiation damping</td><td>11.2.2</td></tr><tr><td>伏特计</td><td>Voltmeter</td><td>7.3.6</td></tr><tr><td>伏特(单位)</td><td>Volt (unit)</td><td>2.3.2</td></tr><tr><td>复杂记号</td><td>Complex notation</td><td>9.1.2, 9.2.3</td></tr><tr><td>波数</td><td>wave number</td><td>9.4.3</td></tr><tr><td>复振幅</td><td>Complex amplitude</td><td>9.1.2</td></tr><tr><td>辅助场</td><td>Auxiliary fields</td><td></td></tr></table>

G

<table><tr><td>感生电场</td><td>Induced electric field</td><td>7.2.1-7.2.3</td></tr><tr><td>感生电荷</td><td>Induced charge</td><td>2.5.1, 2.5.2, 3.2.2, 3.2.3</td></tr><tr><td>感应</td><td>Induction</td><td>6.3.1, 7.2.1-7.3.1</td></tr><tr><td>感应电动势</td><td>Induced emf</td><td>7.2.1</td></tr><tr><td>感应电流</td><td>Induced current</td><td>7.2.1</td></tr><tr><td>高斯单位</td><td>Gaussian units</td><td>附录C</td></tr><tr><td>高斯定理</td><td>Gauss&#x27;s law</td><td>2.2.1, 5.3.4, 7.3.1, 12.3.4</td></tr><tr><td>对称性</td><td>symmetry for</td><td>2.2.3</td></tr><tr><td>物体内部</td><td>inside matter</td><td>4.3.1</td></tr><tr><td>应用</td><td>applications of</td><td>2.2.2, 2.2.3</td></tr><tr><td>高斯面</td><td>Gaussian surface</td><td>2.2.2, 2.2.3</td></tr><tr><td>高斯“扁盒”</td><td>Gaussian “pillbox”</td><td>2.2.3</td></tr><tr><td>高斯(单位)</td><td>Gauss (unit)</td><td>5.2.2, 附录C</td></tr><tr><td>格林定理</td><td>Green&#x27;s theorem</td><td>1.3.4, 1.6.2</td></tr><tr><td>格林恒等式</td><td>Green&#x27;s identity</td><td>1.6.2, 3.2.1</td></tr><tr><td>格林互易定理</td><td>Green&#x27;s reciprocity theorem</td><td>3.4.4</td></tr><tr><td>各向同性介质</td><td>Isotropic medium</td><td>4.4.1</td></tr><tr><td>功</td><td>Work</td><td></td></tr></table>

<table><tr><td>和电动势</td><td>and emf</td><td>7.1.3, 7.2.4</td></tr><tr><td>和势</td><td>and potential</td><td>2.4.1, 2.4.2</td></tr><tr><td>相对论的</td><td>relativistic</td><td>12.2.4</td></tr><tr><td>功率</td><td>Power</td><td></td></tr><tr><td>电磁波中的</td><td>in electromagnetic wave</td><td>9.2.3</td></tr><tr><td>电阻器耗散的功率</td><td>dissipated in resistor</td><td>7.1.1, 8.1.2</td></tr><tr><td>(辐射)任意源的</td><td>radiated by arbitrary source</td><td>11.1.4–11.2.1</td></tr><tr><td>(辐射)通过点电荷</td><td>radiated by point charge</td><td>11.2.1, 11.2.2</td></tr><tr><td>(辐射)通过振荡磁偶极子</td><td>radiated by oscillating magnetic dipole</td><td>11.1.3</td></tr><tr><td>(辐射)通过振荡电偶极子</td><td>radiated by oscillating electric dipole</td><td>11.1.2, 11.1.4</td></tr><tr><td>功能原理</td><td>Work energy theorem</td><td>12.2.4</td></tr><tr><td>共振腔</td><td>Resonant cavity</td><td>9.5.3</td></tr><tr><td>观察者</td><td>Observer</td><td>12.1.2</td></tr><tr><td>光</td><td>Light</td><td>9.1.1–9.5.3</td></tr><tr><td>普遍的</td><td>universal</td><td>12.1.1</td></tr><tr><td>线性介质速度</td><td>speed of linear medium</td><td>9.3.1</td></tr><tr><td>真空中</td><td>in vacuum</td><td>9.2.2, 12.1.1</td></tr><tr><td>广义库仑场</td><td>Coulomb field, generalized</td><td>10.3.2</td></tr><tr><td>光锥</td><td>Light cone</td><td>12.1.4</td></tr><tr><td>光子</td><td>Photon</td><td>12.1.4, 12.2.3</td></tr><tr><td>惯性系统</td><td>Inertial system</td><td>12.1.1</td></tr><tr><td>谷仓和梯子悖论</td><td>Barn and ladder paradox</td><td>12.1.2</td></tr><tr><td>规范</td><td>Gauge</td><td></td></tr><tr><td>规范变换</td><td>Gauge transformation</td><td>10.1.2, 10.1.3</td></tr><tr><td>规范不变性</td><td>Gauge invariance</td><td>12.3.5</td></tr><tr><td>过去</td><td>Past</td><td>12.1.4</td></tr></table>

H

<table><tr><td>H</td><td>H</td><td>6.2.3-6.4.1, 12.3.5</td></tr><tr><td>亥姆霍兹定理</td><td>Helmholtz theorem</td><td>1.6.1, 1.6.2, 附录 B</td></tr><tr><td>亥姆霍兹线圈</td><td>Helmholtz coil</td><td>5.4.3</td></tr><tr><td>横波</td><td>Transverse wave</td><td>9.1.4-9.2.2, 9.4.1</td></tr><tr><td>亨利 (单位)</td><td>Henry (unit)</td><td>7.2.3</td></tr><tr><td>赫维赛德-洛伦兹单位</td><td>Heaviside-Lorentz units</td><td>附录 C</td></tr><tr><td>赫兹 H.</td><td>Hertz, H.</td><td>10.2.1</td></tr><tr><td>宏观领域</td><td>Macroscopic field</td><td>4.2.3-4.3.1, 4.4.3, 6.2.3</td></tr><tr><td>环形线圈</td><td>Toroidal coil</td><td>5.3.3, 7.2.4</td></tr><tr><td>互感</td><td>Mutual inductance</td><td>7.2.3, 7.3.1</td></tr><tr><td>回旋运动</td><td>Cyclotron motion</td><td>5.1.2, 12.2.4</td></tr><tr><td>霍尔效应</td><td>Hall effect</td><td>5.4.3</td></tr></table>

## J

<table><tr><td>伽利略·伽利雷</td><td>Galileo Galilei</td><td>12.1.1</td></tr><tr><td>速度加法规则</td><td>velocity addition rule</td><td>12.1.1, 12.1.2</td></tr><tr><td>相对性原理</td><td>principle of relativity</td><td>12.1.1</td></tr><tr><td>伽利略变换</td><td>Galilean transformation</td><td>12.1.3, 12.1.4</td></tr><tr><td>测量</td><td>gauge</td><td>10.1.2, 10.1.3</td></tr><tr><td>长度的</td><td>of lengths</td><td>12.1.2, 12.1.3</td></tr><tr><td>吉尔伯特模型</td><td>Gilbert model</td><td>6.1.2, 6.4.2, 11.1.4</td></tr><tr><td>辐射偶极子</td><td>radiation</td><td>11.1.3, 11.1.4, 11.2.1</td></tr><tr><td>吉尔伯特偶极子</td><td>Gilbert dipole</td><td>6.1.2, 6.4.2, 11.1.4</td></tr><tr><td>极化(介质的)</td><td>Polarization (of a medium)</td><td>4.1.2, 4.1.4-4.2.1</td></tr><tr><td>磁的</td><td>magnetic</td><td>见“磁化”</td></tr><tr><td>电的</td><td>electric</td><td>4.1.2, 4.1.4, 7.3.5, 7.3.6</td></tr><tr><td>电流</td><td>current</td><td>7.3.5</td></tr><tr><td>诱导</td><td>induced</td><td>4.1.2</td></tr><tr><td>极化率</td><td>Polarizability</td><td></td></tr><tr><td>极化张量</td><td>tensor</td><td>4.1.2</td></tr><tr><td>原子极化率</td><td>atomic</td><td>4.1.2</td></tr><tr><td>极角</td><td>Polar angle</td><td>1.4.1</td></tr><tr><td>极性分子</td><td>Polar molecule</td><td>4.1.2, 4.1.3</td></tr><tr><td>加速场</td><td>Acceleration field</td><td>10.3.2, 11.2.1</td></tr><tr><td>加速度</td><td>Acceleration</td><td></td></tr><tr><td>固有的</td><td>proper</td><td>12.2.4</td></tr><tr><td>普通的</td><td>ordinary</td><td>12.2.4</td></tr><tr><td>间隔,时空</td><td>Interval, spacetime</td><td>12.1.4</td></tr><tr><td>类光</td><td>lightlike</td><td>12.1.4</td></tr><tr><td>类空</td><td>spacelike</td><td>12.1.4</td></tr><tr><td>类时</td><td>timelike</td><td>12.1.4</td></tr><tr><td>检验电荷</td><td>Test charge</td><td>2.1.1, 5.1.1</td></tr><tr><td>剪切</td><td>Shears</td><td>8.2.2</td></tr><tr><td>简谐函数</td><td>Harmonic function</td><td>3.1.2</td></tr><tr><td>焦耳热定律</td><td>Joule heating law</td><td>7.1.1</td></tr><tr><td>角</td><td>Angle</td><td></td></tr><tr><td>方位角</td><td>azimuthal</td><td>1.4.1, 1.4.2</td></tr><tr><td>反射角</td><td>of reflection</td><td>9.3.3</td></tr><tr><td>极角</td><td>polar</td><td>1.4.1</td></tr><tr><td>入射角</td><td>of incidence</td><td>9.3.3</td></tr><tr><td>衍射角</td><td>of refraction</td><td>9.3.3</td></tr><tr><td>角动量</td><td>Momentum angular</td><td>8.2.4-8.3</td></tr><tr><td>守恒</td><td>conservation of</td><td>8.2.3, 8.2.4, 12.2.2</td></tr><tr><td>四维矢量的</td><td>four-vector</td><td>12.2.2</td></tr><tr><td>相对论的</td><td>relativistic</td><td>12.2.2, 12.2.3</td></tr><tr><td>隐动量</td><td>hidden</td><td>12.2.4</td></tr><tr><td>在电磁波中</td><td>in electromagnetic wave</td><td>9.2.3</td></tr><tr><td>在电磁场中</td><td>in electromagnetic field</td><td>8.2.1-8.2.4</td></tr><tr><td>正则角动量</td><td>canonical</td><td>10.1.4</td></tr><tr><td>角动量密度</td><td>Angular momentum density</td><td>8.2.4</td></tr><tr><td>角频率</td><td>Angular frequency</td><td>9.1.2</td></tr><tr><td>阶跃函数</td><td>Step function</td><td>1.5.2</td></tr><tr><td>接地</td><td>Ground</td><td>3.1.6</td></tr><tr><td>杰菲缅科方程</td><td>Jefimenko's equations</td><td>10.2.2-10.3.1</td></tr><tr><td>截止频率</td><td>Cutoff frequency</td><td>9.5.2, 9.5.3</td></tr><tr><td>介电常量</td><td>Dielectric constant</td><td>4.4.1</td></tr><tr><td>静磁学</td><td>Magnetostatics</td><td>5.2.1, 5.3.3, 5.3.4, 5.4.2, 7.3.6</td></tr><tr><td>静电势的多极展开</td><td>Multipole expansion of electrostatic potential</td><td>3.4.1-3.4.4</td></tr><tr><td>磁势的</td><td>of magnetostatic potential</td><td>5.4.3</td></tr><tr><td>辐射场的</td><td>of radiation fields</td><td>11.1.4</td></tr><tr><td>静电学</td><td>Electrostatics</td><td>2.1.1, 4.4.3, 5.2.1, 5.3.3, 5.3.4</td></tr><tr><td>理想偶极子</td><td>perfect</td><td>5.4.3</td></tr><tr><td>偶极子的矩</td><td>moment</td><td>5.4.3</td></tr><tr><td>偶极子的振荡势</td><td>potential of oscillating</td><td>11.1.3</td></tr><tr><td>实际的</td><td>physical</td><td>5.4.3</td></tr><tr><td>运动的</td><td>moving</td><td>12.3.5</td></tr><tr><td>静电压力</td><td>Electrostatic pressure</td><td>2.5.3</td></tr><tr><td>静能</td><td>Rest energy</td><td>12.2.2</td></tr><tr><td>静止电荷</td><td>Stationary charge</td><td>5.2.1</td></tr><tr><td>静质量</td><td>Rest mass</td><td>12.2.2</td></tr><tr><td>镜像法</td><td>Images, method of</td><td>3.2.1</td></tr><tr><td>点电荷和导电平面</td><td>point charge and conducting plane</td><td>3.2.1-3.2.4, 11.2.3</td></tr><tr><td>点电荷和导电球</td><td>point charge and conducting sphere</td><td>3.2.4</td></tr><tr><td>点电荷和介电平面</td><td>point charge and dielectric plane</td><td>4.4.2</td></tr><tr><td>偶极子和导电平面</td><td>dipole and conducting plane</td><td>4.1.4</td></tr><tr><td>平行圆柱体</td><td>parallel cylinders</td><td>3.3.1</td></tr><tr><td>居里点</td><td>Curie point</td><td>6.4.2</td></tr><tr><td>局域守恒</td><td>Local conservation</td><td>见“连续性方程”</td></tr><tr><td>矩阵</td><td>Matrix</td><td></td></tr><tr><td>洛伦兹变换</td><td>Lorentz transformation</td><td>12.1.4</td></tr><tr><td>旋转</td><td>rotation</td><td>1.1.5</td></tr><tr><td>绝缘体</td><td>Insulator</td><td>2.5.1, 4.1.1</td></tr></table>

<table><tr><td>均质介质</td><td>Homogeneous medium</td><td>4.4.1</td></tr></table>

K

<table><tr><td>可见范围(电磁波谱)</td><td>Visible range (electromagnetic spectrum)</td><td>9.2.2</td></tr><tr><td>克劳修斯-摩索提方程</td><td>Clausius-Mossotti equation</td><td>4.4.4</td></tr><tr><td>克罗内克</td><td>Kronecker</td><td>3.4.4, 8.2.2</td></tr><tr><td>克罗内克δ函数</td><td>Kronecker delta</td><td>3.4.4, 8.2.2</td></tr><tr><td>柯西公式</td><td>Cauchy&#x27;s formula</td><td>9.4.3</td></tr><tr><td>抗磁性</td><td>Diamagnetism</td><td>6.1.1, 6.1.3–6.2.1, 7.3.6</td></tr><tr><td>康普顿波长</td><td>Compton wavelength</td><td>12.2.3</td></tr><tr><td>康普顿散射</td><td>Compton scattering</td><td>12.2.3</td></tr><tr><td>空间电荷</td><td>Space charge</td><td>2.5.4</td></tr><tr><td>空腔</td><td>Cavity</td><td></td></tr><tr><td>磁性材料中的</td><td>in magnetic material</td><td>6.3.1, 6.3.2</td></tr><tr><td>导体中的</td><td>in conductor</td><td>2.5.2, 3.1.6</td></tr><tr><td>电介质中的</td><td>in dielectric</td><td>4.3.1, 4.3.2</td></tr><tr><td>谐振</td><td>resonant</td><td>9.5.3</td></tr><tr><td>库仑定律</td><td>Coulomb&#x27;s law</td><td>2.1.4</td></tr><tr><td>磁的</td><td>magnetic</td><td>见“磁化”</td></tr><tr><td>库仑规范</td><td>Coulomb gauge</td><td>10.1.3, 12.3.5</td></tr><tr><td>库仑(单位)</td><td>Coulomb (unit)</td><td>附录C</td></tr><tr><td>快度</td><td>Rapidity</td><td>12.1.4</td></tr></table>

L

<table><tr><td>LC电路</td><td>LC circuit</td><td>7.2.3</td></tr><tr><td>拉莫尔公式</td><td>Larmor formula</td><td>11.1.4, 11.2.1</td></tr><tr><td>拉普拉斯方程</td><td>Laplace's equation</td><td>2.3.4, 3.1.1-3.1.6</td></tr><tr><td>二维</td><td>in two dimensions</td><td>3.1.3-3.1.5</td></tr><tr><td>三维</td><td>in three dimensions</td><td>3.1.5, 3.1.6</td></tr><tr><td>一维</td><td>in one dimension</td><td>3.1.2, 3.1.3</td></tr><tr><td>拉普拉斯算子</td><td>Laplacian</td><td>1.2.7</td></tr><tr><td>V的</td><td>of V</td><td>2.3.4, 2.3.5, 3.1.1</td></tr><tr><td>标量的</td><td>of a scalar</td><td>1.2.7</td></tr><tr><td>矢量的</td><td>of a vector</td><td>1.2.7-1.3.1</td></tr><tr><td>在球坐标中</td><td>in spherical coordinates</td><td>1.4.1</td></tr><tr><td>在曲线坐标中</td><td>in curvilinear coordinates</td><td>附录A.6</td></tr><tr><td>在直角坐标中</td><td>in Cartesian coordinates</td><td>1.2.7, 3.1.2</td></tr><tr><td>在柱坐标中</td><td>in cylindrical coordinates</td><td>1.4.2</td></tr><tr><td>朗之万方程</td><td>Langevin equation</td><td>4.4.4</td></tr><tr><td>勒让德多项式</td><td>Legendre polynomials</td><td>3.3.2, 3.4.1</td></tr><tr><td>类光间隔</td><td>Lightlike interval</td><td>12.1.4</td></tr><tr><td>类空间隔</td><td>Spacelike interval</td><td>12.1.4</td></tr><tr><td>类时间隔</td><td>Timelike interval</td><td>12.1.4</td></tr><tr><td>楞次定律</td><td>Lenz's law</td><td>7.2.1</td></tr><tr><td>力</td><td>Force</td><td></td></tr><tr><td>(磁场)磁单极子的</td><td>magnetic, between monopoles</td><td>7.3.4</td></tr><tr><td>(磁场)磁化材料的</td><td>magnetic, on magnetized material</td><td>6.1.4</td></tr><tr><td>(磁场)磁偶极子的</td><td>magnetic, on magnetic dipole</td><td>6.1.2, 6.4.2</td></tr><tr><td>(磁场)点电荷之间的</td><td>magnetic, on point charge</td><td>5.1.2</td></tr><tr><td>(磁场)电流的</td><td>magnetic, on current</td><td>5.1.3</td></tr><tr><td>(磁场)电流环之间的</td><td>magnetic, between current loops</td><td>5.4.3</td></tr><tr><td>(磁场)平行电流间的</td><td>magnetic, between parallel currents</td><td>5.1.1, 5.1.2, 5.2.2, 5.3.1, 12.2.4-12.3.1</td></tr><tr><td>(磁场)平行平面间的</td><td>magnetic, between parallel planes</td><td>5.3.3</td></tr><tr><td>(电场)表面电荷的</td><td>electric, on surface charge</td><td>2.5.3</td></tr><tr><td>(电场)场中点电荷的</td><td>electric, on point charge in field</td><td>2.1.3, 5.1.2</td></tr><tr><td>(电场)导电平面附近点电荷的</td><td>electric, on point charge near conducting plane</td><td>3.2.3, 3.2.4</td></tr><tr><td>(电场)导体上的</td><td>electric, on conductor</td><td>2.5.3</td></tr><tr><td>(电场)点电荷之间的</td><td>electric, between point charges</td><td>10.3.2</td></tr><tr><td>(电场)电介质上的</td><td>electric, on dielectric</td><td>4.4.4</td></tr><tr><td>(电场)电偶极子上的</td><td>electric, on electric dipole</td><td>4.1.3, 4.1.4</td></tr><tr><td>(电场)介电平面附近点电荷的</td><td>electric, on point charge near dielectric plane</td><td>4.4.2, 4.4.3</td></tr><tr><td>保守力</td><td>conservative</td><td>1.3.1</td></tr><tr><td>点电荷之间的电磁力</td><td>electromagnetic, between point charges</td><td>10.3.2</td></tr><tr><td>洛伦兹力</td><td>Lorentz</td><td>5.1.2, 5.1.3, 12.2.4</td></tr><tr><td>李纳-维谢尔势</td><td>Liènard-Wiechert</td><td>10.3.1, 10.3.2</td></tr><tr><td>磁标量</td><td>magnetic scalar</td><td>5.4.2, 5.4.3</td></tr><tr><td>磁静标量</td><td>magnetostatic scalar</td><td>5.4.1</td></tr><tr><td>磁矢量</td><td>magnetic vector</td><td>5.4.1, 5.4.3</td></tr><tr><td>滞后势</td><td>retarded</td><td>10.2.1</td></tr><tr><td>李纳公式</td><td>Liénard formula</td><td>11.2.1, 12.3.5</td></tr><tr><td>连续性方程</td><td>Continuity equation</td><td>5.1.3, 5.2.2, 7.3.4, 8.1.1, 8.1.2, 8.2.3, 12.3.4</td></tr><tr><td>列维-奇维塔符号</td><td>Levi-Civita symbol</td><td>6.4.2</td></tr><tr><td>力密度</td><td>Force density</td><td>8.2.2</td></tr><tr><td>临界角</td><td>Critical angle</td><td>9.5.3</td></tr><tr><td>路径积分</td><td>Path integral</td><td>1.3.1</td></tr><tr><td>路径无关</td><td>Path independence</td><td>1.3.1, 1.3.3, 1.6.2, 2.3.1, 2.3.2</td></tr><tr><td>罗德里格斯公式</td><td>Rodrigues formula</td><td>3.3.2, 3.3.2</td></tr></table>

<table><tr><td>内部反射</td><td>Internal reflection</td><td>9.5.3</td></tr><tr><td>内阻</td><td>Internal resistance</td><td>7.1.2, 7.1.3</td></tr><tr><td>能量</td><td>Energy</td><td></td></tr></table>

## M

## N

<table><tr><td>磁场中的</td><td>in magnetic field</td><td>7.2.4-7.3.1, 8.1.2</td></tr><tr><td>导电平面附近点电荷的</td><td>of point charge near conducting plane</td><td>3.2.4</td></tr><tr><td>电场中的</td><td>in electric field</td><td>8.1.2</td></tr><tr><td>电磁波的</td><td>of electromagnetic wave</td><td>9.2.3</td></tr><tr><td>点电荷分布的</td><td>of point charge distribution</td><td>2.4.2, 2.4.3</td></tr><tr><td>电感线圈的</td><td>of inductor</td><td>7.2.4</td></tr><tr><td>电容器的</td><td>of capacitor</td><td>2.5.4</td></tr><tr><td>静电场中电荷的</td><td>of charge in static field</td><td>2.4.1, 2.4.2</td></tr><tr><td>静电荷分布的</td><td>of static charge distribution</td><td>2.4.1</td></tr><tr><td>连续电荷分布的</td><td>of continuous charge distribution</td><td>2.4.3, 2.4.4</td></tr><tr><td>能量守恒</td><td>conservation of</td><td>9.3.3, 12.2.2</td></tr><tr><td>偶极子的</td><td>of dipole</td><td>4.1.4, 6.4.2</td></tr><tr><td>球壳的</td><td>of spherical shell</td><td>2.4.3, 2.4.4</td></tr><tr><td>线性电介质的</td><td>of linear dielectric</td><td>4.4.3, 4.4.4</td></tr><tr><td>能量-动量四矢量</td><td>Energy-momentum four-vector</td><td>12.2.2</td></tr><tr><td>能量密度</td><td>Energy density</td><td></td></tr><tr><td>电磁波的</td><td>of electromagnetic wave</td><td>9.2.3</td></tr><tr><td>电磁的</td><td>electromagnetic</td><td>8.1.2, 9.2.3</td></tr><tr><td>静磁的</td><td>magnetostatic</td><td>7.2.4</td></tr><tr><td>静电的</td><td>electrostatic</td><td>2.4.3-2.5.1</td></tr><tr><td>线性介质中的</td><td>in linear media</td><td>4.4.3</td></tr><tr><td>能量通量</td><td>Energy flux</td><td>8.1.2</td></tr><tr><td>能量中心</td><td>Center of energy</td><td>12.2.4</td></tr><tr><td>能量,相对论的</td><td>Energy, relativistic</td><td>12.2.2</td></tr><tr><td>动能</td><td>kinetic</td><td>12.2.2</td></tr><tr><td>静能</td><td>rest</td><td>12.2.2</td></tr><tr><td>逆变矢量</td><td>Contravariant vector</td><td>12.1.4, 12.3.5</td></tr><tr><td>牛顿定律</td><td>Newton's laws</td><td></td></tr><tr><td>第二定律</td><td>second law</td><td>11.2.3, 12.2.4</td></tr><tr><td>第三定律</td><td>third law</td><td>8.2.1, 8.2.2, 10.3.2, 11.2.3, 12.2.4</td></tr><tr><td>第一定律</td><td>first law</td><td>12.1.1</td></tr><tr><td>扭矩</td><td>Torque</td><td></td></tr><tr><td>磁偶极子</td><td>on magnetic dipole</td><td>6.1.1, 6.1.2</td></tr><tr><td>电偶极子</td><td>on electric dipole</td><td>4.1.3</td></tr><tr><td>诺伊曼公式</td><td>Neumann formula</td><td>7.2.3</td></tr><tr><td colspan="3">O</td></tr><tr><td>偶极矩</td><td>Dipole moment</td><td>3.4.2</td></tr><tr><td>偶极子,磁</td><td>Dipoles, magnetic</td><td>5.4.3</td></tr><tr><td>偶极子,电</td><td>Dipoles, electric</td><td>2.2.1, 3.4.1-3.4.4</td></tr><tr><td>P.A.M. 狄拉克</td><td>Dirac, P.A.M.</td><td>8.3</td></tr><tr><td>碰撞</td><td>Collision</td><td></td></tr><tr><td>经典碰撞</td><td>classical</td><td>12.1.2</td></tr><tr><td>弹性碰撞</td><td>elastic</td><td>12.2.3</td></tr><tr><td>相对论碰撞</td><td>relativistic</td><td>12.2.3, 12.2.4</td></tr><tr><td>频率</td><td>Frequency</td><td>9.1.2</td></tr><tr><td>截止频率</td><td>cutoff</td><td>9.5.2, 9.5.3</td></tr><tr><td>偏振角</td><td>Polarization angle</td><td>9.2.1</td></tr><tr><td>偏振向量</td><td>Polarization vector</td><td>9.1.4</td></tr><tr><td>偏振(波的)</td><td>Polarization (of a wave)</td><td>9.1.4–9.2.1</td></tr><tr><td>线偏振</td><td>linear</td><td>9.2.1</td></tr><tr><td>圆偏振</td><td>circular</td><td>9.2.1</td></tr><tr><td>漂移速度</td><td>Drift velocity</td><td>7.1.1</td></tr><tr><td>屏蔽</td><td>Shielding</td><td>4.4.1</td></tr><tr><td>平面</td><td>Plane</td><td></td></tr><tr><td>偏振面</td><td>of polarization</td><td>9.3.3</td></tr><tr><td>入射面</td><td>of incidence</td><td>9.3.3</td></tr><tr><td>平面波</td><td>Plane wave</td><td>9.2.2, 9.2.3</td></tr><tr><td>平行板电容器</td><td>Parallel-plate capacitor</td><td>2.2.3, 2.5.4, 4.4.1, 5.3.3, 12.3.2</td></tr><tr><td>平移</td><td>Translation</td><td>1.1.5</td></tr><tr><td>坡印亭定理</td><td>Poynting's theorem</td><td>8.1.2–8.2.1</td></tr><tr><td>坡印亭矢量</td><td>Poynting vector</td><td>8.1.2, 9.2.3–9.3.1</td></tr><tr><td>普朗克公式</td><td>Planck formula</td><td>12.2.3</td></tr></table>

<table><tr><td>辐射偶极子</td><td>radiation</td><td>11.1.2, 11.1.3</td></tr><tr><td>固有的</td><td>permanent</td><td>4.1.3</td></tr><tr><td>两个偶极子相互作用能量</td><td>energy of interaction of two</td><td>4.1.4</td></tr><tr><td>理想偶极子</td><td>perfect</td><td>3.4.2, 3.4.4</td></tr><tr><td>偶极子的能量,电场中</td><td>energy of, in electric field</td><td>4.1.4</td></tr><tr><td>偶极子的振荡势</td><td>potential of oscillating</td><td>11.1.2</td></tr><tr><td>偶极子上的扭矩</td><td>torque on</td><td>4.1.3</td></tr><tr><td>物理偶极子</td><td>physical</td><td>3.4.2, 3.4.4</td></tr><tr><td>诱导偶极子</td><td>induced</td><td>4.1.1-4.1.3</td></tr><tr><td>振荡场的</td><td>field of oscillating</td><td>11.1.2</td></tr><tr><td>作用在偶极子上的力</td><td>force on</td><td>4.1.3, 4.1.4</td></tr><tr><td>欧拉公式</td><td>Euler&#x27;s formula</td><td>9.1.2</td></tr><tr><td>欧姆定律</td><td>Ohm&#x27;s law</td><td>7.1.1, 7.1.2</td></tr><tr><td>欧姆(单位)</td><td>Ohm (unit)</td><td>7.1.1</td></tr></table>

## P

Q

<table><tr><td>强度</td><td>Intensity</td><td>9.2.3</td></tr><tr><td>求和约定</td><td>Summation convention</td><td>12.1.4</td></tr><tr><td>球面</td><td>Spherical surface</td><td>1.5.3</td></tr><tr><td>球面波</td><td>Spherical wave</td><td>9.5.3</td></tr><tr><td>求逆</td><td>Reversion of series</td><td>11.2.3</td></tr><tr><td>球体</td><td>Spherical volume</td><td>1.5.3</td></tr><tr><td>球体</td><td>Spheres</td><td></td></tr><tr><td>定义的</td><td>defined</td><td>1.5.3</td></tr><tr><td>术语</td><td>terminology for</td><td>1.5.3</td></tr><tr><td>球坐标</td><td>Spherical coordinates</td><td>1.4.1, 1.4.2</td></tr><tr><td>球, 定义</td><td>Ball, defined</td><td>1.5.3</td></tr><tr><td>全反射</td><td>Total internal reflection</td><td>9.5.3</td></tr><tr><td>趋肤深度</td><td>Skin depth</td><td>9.4.1</td></tr><tr><td>群速度</td><td>Group velocity</td><td>9.4.3, 9.5.2</td></tr><tr><td>曲线坐标</td><td>Curvilinear coordinates</td><td>1.4.1, 附录 A.1-附录 A.6</td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>R</td><td></td></tr><tr><td>RC电路</td><td>RC circuit</td><td>7.1.1</td></tr><tr><td>RL电路</td><td>RL circuit</td><td>7.2.4</td></tr><tr><td>韧致辐射</td><td>Bremsstrahlung</td><td>11.2.1</td></tr><tr><td>入射</td><td>Incidence</td><td></td></tr><tr><td>入射角</td><td>angle of</td><td>9.3.3</td></tr><tr><td>入射面</td><td>plane of</td><td>9.3.3</td></tr><tr><td>入射波</td><td>Incident wave</td><td>9.1.3, 9.3.2</td></tr><tr><td></td><td>S</td><td></td></tr><tr><td>SI单位制</td><td>SI units</td><td>附录 C</td></tr><tr><td>三重积</td><td>Triple product</td><td>1.1.3</td></tr><tr><td>散度</td><td>Divergence</td><td>1.2.3, 1.2.4, 附录 A.4,附录 A.5</td></tr><tr><td>A的</td><td>of A</td><td>5.4.1</td></tr><tr><td>B的</td><td>of B</td><td>5.3.1, 5.3.2</td></tr><tr><td>E的</td><td>of E</td><td>2.2.1, 2.2.2</td></tr><tr><td>H的</td><td>of H</td><td>6.3.1, 6.3.2</td></tr><tr><td>四维的</td><td>four-dimensional</td><td>12.3.4</td></tr><tr><td>在球坐标中</td><td>in spherical coordinates</td><td>1.4.1</td></tr><tr><td>在曲线坐标中</td><td>in curvilinear coordinates</td><td>附录 A.4</td></tr><tr><td>在直角坐标系中</td><td>in Cartesian coordinates</td><td>1.2.4</td></tr><tr><td>在柱坐标中</td><td>in cylindrical coordinates</td><td>1.4.2</td></tr><tr><td>散度定理</td><td>Divergence theorem</td><td>1.3.4,附录A.5</td></tr><tr><td>三角图</td><td>Triangle diagram</td><td></td></tr><tr><td>电动力学</td><td>electrodynamics</td><td>10.3.2</td></tr><tr><td>静磁学</td><td>magnetostatics</td><td>5.4.2, 5.4.3</td></tr><tr><td>静电学</td><td>electrostatics</td><td>2.3.5</td></tr><tr><td>三维波动方程</td><td>Three-dimensional wave equation</td><td>9.2.2</td></tr><tr><td>色散</td><td>Dispersion</td><td>9.4.3</td></tr><tr><td>反常色散</td><td>anomalous</td><td>9.4.3</td></tr><tr><td>色散系数</td><td>Dispersion coefficient</td><td>9.4.3</td></tr><tr><td>商法则</td><td>Quotient rules</td><td>1.2.6</td></tr><tr><td>势</td><td>Potential</td><td></td></tr><tr><td>超前势</td><td>advanced</td><td>10.2.1</td></tr><tr><td>电动力学中的</td><td>in electrodynamics</td><td>10.1.1-10.1.4</td></tr><tr><td>电势</td><td>electric</td><td>2.3.1, 2.3.3</td></tr><tr><td>四维矢量的</td><td>four-vector</td><td>12.3.5</td></tr><tr><td>事件</td><td>Events</td><td>12.1.3</td></tr><tr><td>时间</td><td>Time</td><td></td></tr><tr><td>固有时</td><td>proper</td><td>12.2.1, 12.2.2</td></tr><tr><td>时间延缓</td><td>retarded</td><td>10.2.1</td></tr><tr><td>提前的</td><td>advanced</td><td>10.2.1</td></tr><tr><td>时间常数</td><td>Time constant</td><td>7.1.1, 7.2.3, 9.4.1</td></tr><tr><td>时间反演</td><td>Time reversal</td><td>10.2.1</td></tr><tr><td>时间佯谬</td><td>Time paradox</td><td>12.1.2</td></tr><tr><td>时间延缓</td><td>Time dilation</td><td>12.1.2, 12.1.3</td></tr><tr><td>视界</td><td>Horizon</td><td>10.3.2</td></tr><tr><td>世界线</td><td>World line</td><td>12.1.4</td></tr><tr><td>时空间隔</td><td>Spacetime interval</td><td>12.1.4</td></tr><tr><td>时空结构</td><td>Spacetime, structure of</td><td>12.1.4-12.2.1</td></tr><tr><td>时空图</td><td>Spacetime diagram</td><td>12.1.4-12.2.1</td></tr><tr><td>失控运动</td><td>Runaway motion</td><td>11.2.2, 11.2.3</td></tr><tr><td>矢量</td><td>Vectors</td><td>1.1.1</td></tr><tr><td>常变矢量</td><td>contravariant</td><td>12.1.4</td></tr><tr><td>传播矢量</td><td>propagation</td><td>9.2.2</td></tr><tr><td>单位矢量</td><td>unit</td><td>见“单位矢量”</td></tr><tr><td>分离矢量</td><td>separation</td><td>1.1.4, 1.2.2</td></tr><tr><td>极化矢量</td><td>polarization</td><td>9.1.4</td></tr><tr><td>矢量大小</td><td>magnitude</td><td>1.1.1</td></tr><tr><td>矢量分量</td><td>component</td><td>1.1.2, 1.4.1</td></tr><tr><td>矢量加法</td><td>addition</td><td>1.1.1, 1.1.2</td></tr><tr><td>矢量减法</td><td>subtraction</td><td>1.1.1</td></tr><tr><td>四矢量</td><td>four</td><td>12.1.4</td></tr><tr><td>位矢</td><td>position</td><td>1.1.4</td></tr><tr><td>位移矢量</td><td>displacement</td><td>1.1.1, 1.1.4</td></tr><tr><td>协变矢量</td><td>covariant</td><td>12.1.4</td></tr><tr><td>赝矢量</td><td>pseudovectors</td><td>1.1.5, 5.1.2</td></tr><tr><td>矢量积</td><td>Vector products</td><td>1.1.1</td></tr><tr><td>叉积</td><td>cross product</td><td>1.1.1, 1.1.2</td></tr><tr><td>乘以标量</td><td>multiplication by scalar</td><td>1.1.1, 1.1.2, 12.1.4</td></tr><tr><td>点积</td><td>dot product</td><td>1.1.1, 1.1.2</td></tr><tr><td>矢量面积</td><td>Vector area</td><td>1.6.2, 5.4.3</td></tr><tr><td>矢量三重积</td><td>Vector triple products</td><td>1.1.3</td></tr><tr><td>矢量算符</td><td>Vector operator</td><td>1.2.3</td></tr><tr><td>势能</td><td>Potential energy</td><td>2.3.2</td></tr><tr><td>带电导体的</td><td>of a charge configuration</td><td>2.4.2</td></tr><tr><td>点电荷的</td><td>of a point charge</td><td>2.4.2</td></tr><tr><td>矢势</td><td>Vector potential</td><td>1.6.2, 5.4.1, 10.1.1-10.3.2</td></tr><tr><td>方向</td><td>direction of</td><td>5.4.1</td></tr><tr><td>(动态)点电荷, 恒定速度</td><td>dynamic configurations, point charge, constant velocity</td><td>10.3.1, 10.3.2</td></tr><tr><td>(动态)点电荷, 任意运动</td><td>dynamic configurations, point charge, arbitrary motion</td><td>10.3.1</td></tr><tr><td>(动态)任意电荷分布</td><td>dynamic configurations, arbitrary charge distribution</td><td>10.2.1, 11.1.4</td></tr><tr><td>(动态)振荡磁偶极子</td><td>dynamic configurations, oscillating magnetic dipole</td><td>11.1.3</td></tr><tr><td>(动态)振荡电偶极子</td><td>dynamic configurations, oscillating electric dipole</td><td>11.1.2</td></tr><tr><td>(静态)磁化材料</td><td>static configurations, magnetized material</td><td>6.2.1</td></tr><tr><td>(静态)磁偶极子</td><td>static configurations, magnetic dipole</td><td>5.4.3</td></tr><tr><td>(静态)多极展开</td><td>static configurations, multipole expansion</td><td>5.4.3</td></tr><tr><td>(静态)均匀磁场</td><td>static configurations, uniform magnetic field</td><td>5.4.1</td></tr><tr><td>(静态)任意电流</td><td>static configurations, arbitrary current configuration</td><td>5.4.1</td></tr><tr><td>(静态)特定磁场</td><td>static configurations, specified magnetic field</td><td>5.4.3</td></tr><tr><td>(静态)无限长线电流</td><td>static configurations, infinite line current</td><td>5.4.1, 5.4.2</td></tr><tr><td>(静态)无限大面电流</td><td>static configurations, infinite plane current</td><td>5.4.1, 5.4.2</td></tr><tr><td>(静态)无限螺线管</td><td>static configurations, infinite solenoid</td><td>5.4.1</td></tr><tr><td>(静态)旋转球</td><td>static configurations, spinning sphere</td><td>5.4.1, 5.4.3</td></tr><tr><td>(静态)有限长线电流</td><td>static configurations, finite line current</td><td>5.4.2</td></tr><tr><td>守恒定律</td><td>Conservation laws</td><td>8.1.1-8.3</td></tr><tr><td>局域的</td><td>local</td><td>见“连续性方程”</td></tr><tr><td>相对性</td><td>relativistic</td><td>12.2.2-12.2.4</td></tr><tr><td>寿命</td><td>Lifetime</td><td>12.1.2, 12.1.2</td></tr><tr><td>收缩效应</td><td>Pinch effect</td><td>5.4.3</td></tr><tr><td>束缚电荷</td><td>Bound charge</td><td>4.2.1-4.2.3, 4.4.2, 7.3.5</td></tr><tr><td>束缚电流</td><td>Bound currents</td><td>6.2.1, 6.2.2, 6.4.1, 7.3.5</td></tr><tr><td>物理解释</td><td>physical interpretation of</td><td>6.2.2, 6.2.3</td></tr><tr><td>双曲几何</td><td>Hyperbolic geometry</td><td>12.1.4-12.2.1</td></tr><tr><td>双曲运动</td><td>Hyperbolic motion</td><td>10.3.2, 11.2.3, 12.2.2, 12.2.4, 12.3.5</td></tr><tr><td>双生子佯谬</td><td>Twin paradox</td><td>12.1.2-12.1.4</td></tr><tr><td>顺磁性</td><td>Paramagnetism</td><td>6.1.1, 6.1.2, 6.1.4-6.2.1</td></tr><tr><td>四极</td><td>Quadrupole</td><td></td></tr><tr><td>磁的</td><td>magnetic</td><td>5.4.3</td></tr><tr><td>电的</td><td>electric</td><td>3.4.1, 3.4.2, 3.4.4, 11.1.4-11.2.1</td></tr><tr><td>辐射</td><td>radiation</td><td>11.1.4</td></tr><tr><td>四极矩</td><td>Quadrupole moment</td><td>3.4.4</td></tr><tr><td>斯涅尔定律</td><td>Snell's law</td><td>9.3.3</td></tr><tr><td>斯托克斯定理</td><td>Stokes'theorem</td><td>1.3.5, 1.6.2, 附录A.5, 附录A.6</td></tr><tr><td>四维矢量</td><td>Four vector</td><td>12.1.4</td></tr><tr><td>位置/时间</td><td>position/time</td><td>12.1.4</td></tr><tr><td>位移</td><td>displacement</td><td>12.1.4</td></tr><tr><td>速度</td><td>velocity</td><td>12.2.1</td></tr><tr><td>能量/动量</td><td>energy/momentum</td><td>12.2.2</td></tr><tr><td>加速度</td><td>acceleration</td><td>12.2.4</td></tr><tr><td>电荷/电流</td><td>charge/current</td><td>12.3.4</td></tr><tr><td>闵可夫斯基力</td><td>Minkowski force</td><td>12.2.4, 12.3.4, 12.3.5</td></tr><tr><td>势</td><td>potential</td><td>12.3.5</td></tr><tr><td>梯度</td><td>gradient</td><td>12.3.5</td></tr><tr><td>思想实验</td><td>Gedanken (thought) experiment</td><td>12.1.2</td></tr><tr><td>速度</td><td>Velocity</td><td></td></tr><tr><td>波速</td><td>wave</td><td>9.4.3</td></tr><tr><td>固有速度</td><td>proper</td><td>12.2.1, 12.2.2</td></tr></table>

<table><tr><td>漂移速度</td><td>drift</td><td>5.3.4, 7.1.1</td></tr><tr><td>普通速度</td><td>ordinary</td><td>12.2.1</td></tr><tr><td>群速度</td><td>group</td><td>9.4.3</td></tr><tr><td>四维速度</td><td>4-velocity</td><td>12.2.1, 12.2.2</td></tr><tr><td>相速</td><td>phase</td><td>9.4.3</td></tr><tr><td>弦上的波速</td><td>of waves on a string</td><td>9.1.1</td></tr><tr><td>速度</td><td>Speed</td><td></td></tr><tr><td>导线中电荷的</td><td>of charges in wire</td><td>5.3.4, 7.1.1</td></tr><tr><td>弦上波的</td><td>of waves on a string</td><td>9.1.1</td></tr><tr><td>线性介质中光的</td><td>of light in linear medium</td><td>9.3.1</td></tr><tr><td>真空中光的</td><td>of light in vacuum</td><td>9.2.2, 12.1.1</td></tr><tr><td>速度场</td><td>Velocity field</td><td>10.3.2, 11.2.1</td></tr><tr><td>速度加法法则</td><td>Velocity addition rules</td><td>12.1.1–12.1.3</td></tr><tr><td>算符</td><td>Operator</td><td>1.2.3</td></tr><tr><td>隧穿</td><td>Tunneling</td><td>9.5.3, 11.2.3</td></tr></table>

## T

<table><tr><td>TEM波</td><td>TEM waves</td><td>9.5.1</td></tr><tr><td>TE波</td><td>TE waves</td><td>9.5.1-9.5.3</td></tr><tr><td>TM波</td><td>TM waves</td><td>9.5.1</td></tr><tr><td>太阳年龄</td><td>Sun, age of</td><td>2.5.4</td></tr><tr><td>汤姆逊偶极子</td><td>Thomson's dipole</td><td>8.3</td></tr><tr><td>汤普森-兰帕德定理</td><td>Thompson-Lampard theorem</td><td>3.4.4</td></tr><tr><td>弹性碰撞</td><td>Elastic collision</td><td>12.2.3</td></tr><tr><td>特斯拉(单位)</td><td>Tesla (unit)</td><td>5.2.2,附录C</td></tr><tr><td>体电荷</td><td>Volume charge</td><td>2.1.4</td></tr><tr><td>体电流</td><td>Volume current</td><td>5.1.3</td></tr><tr><td>梯度</td><td>Gradient</td><td>1.2.1, 1.2.2, 附录A.3</td></tr><tr><td>球坐标中的</td><td>in spherical coordinates</td><td>1.4.1</td></tr><tr><td>曲线坐标中的</td><td>in curvilinear coordinates</td><td>附录A.3</td></tr><tr><td>四维的</td><td>four-dimensional</td><td>12.3.5</td></tr><tr><td>梯度定理</td><td>theorem</td><td>1.3.2,附录A.4</td></tr><tr><td>直角坐标中的</td><td>in Cartesian coordinates</td><td>1.2.1, 1.2.2</td></tr><tr><td>柱坐标中的</td><td>in cylindrical coordinates</td><td>1.4.2</td></tr><tr><td>天空,蔚蓝</td><td>Sky, blueness of</td><td>11.1.2</td></tr><tr><td>跳环</td><td>Jumping ring</td><td>7.2.1</td></tr><tr><td>条形磁铁</td><td>Bar magnet</td><td>6.2.1, 6.3.3</td></tr><tr><td>条形驻极体</td><td>Bar electret</td><td>4.2.2, 4.3.2</td></tr><tr><td>铁磁畴</td><td>Ferromagnetic domain</td><td>6.4.2</td></tr><tr><td>铁磁性</td><td>Ferromagnetism</td><td>6.1.1, 6.4.2</td></tr><tr><td>体积分</td><td>Volume integral</td><td>1.3.1</td></tr><tr><td>体积元</td><td>Volume element</td><td></td></tr><tr><td>球坐标</td><td>spherical</td><td>1.4.1</td></tr><tr><td>曲线坐标</td><td>curvilinear</td><td>附录 A.4</td></tr><tr><td>直角坐标</td><td>Cartesian</td><td>1.3.1</td></tr><tr><td>柱坐标</td><td>cylindrical</td><td>1.4.2</td></tr><tr><td>同步</td><td>Synchronization</td><td>12.1.2, 12.1.3</td></tr><tr><td>同步辐射</td><td>Synchrotron radiation</td><td>11.2.2</td></tr><tr><td>通量</td><td>Flux</td><td></td></tr><tr><td>磁通量</td><td>magnetic</td><td>7.1.3</td></tr><tr><td>电通量</td><td>electric</td><td>2.2.1</td></tr><tr><td>通量规则</td><td>Flux rule</td><td>7.1.3, 7.2.1, 12.1.1</td></tr><tr><td>通量规则悖论</td><td>Flux rule paradox</td><td>7.1.3</td></tr><tr><td>通量积分</td><td>Flux integral</td><td>1.3.1</td></tr><tr><td>通量密度</td><td>Flux density</td><td>6.3.1</td></tr><tr><td>能量的</td><td>energy</td><td>8.1.2</td></tr><tr><td>同时性</td><td>Simultaneity</td><td>12.1.2, 12.1.3</td></tr><tr><td>同轴电缆</td><td>Coaxial cable</td><td>2.2.3, 9.5.3</td></tr><tr><td>透明度</td><td>Transparency</td><td>9.3.1</td></tr><tr><td>透射系数</td><td>Transmission coefficient</td><td>9.3.3</td></tr></table>

## W

<table><tr><td>完备性</td><td>Completeness</td><td>3.3.1</td></tr><tr><td>微观场</td><td>Microscopic field</td><td>4.2.3-4.3.1, 6.2.3</td></tr><tr><td>微积分基本定理</td><td>Fundamental theorem of calculus</td><td>1.3.2</td></tr><tr><td>散度</td><td>for divergences</td><td>1.3.4, 附录 A.5</td></tr><tr><td>梯度</td><td>for gradients</td><td>1.3.2, 1.3.3, 附录 A.4</td></tr><tr><td>旋度</td><td>for curls</td><td>1.3.5</td></tr><tr><td>未来</td><td>Future</td><td>12.1.4</td></tr><tr><td>位移电流</td><td>Displacement current</td><td>7.3.2, 7.3.3, 7.3.6</td></tr><tr><td>位移矢量</td><td>Displacement vector</td><td></td></tr><tr><td>四维</td><td>four-vector</td><td>12.1.4</td></tr><tr><td>有限的</td><td>finite</td><td>1.1.1, 1.1.4</td></tr><tr><td>(无穷小) 球坐标</td><td>infinitesimal, spherical</td><td>1.4.1</td></tr><tr><td>(无穷小) 曲线坐标</td><td>infinitesimal, curvilinear</td><td>附录 A.1</td></tr><tr><td>(无穷小) 圆柱坐标</td><td>infinitesimal, cylindrical</td><td>1.4.2</td></tr><tr><td>(无穷小) 直角坐标</td><td>infinitesimal, Cartesian</td><td>1.1.4</td></tr><tr><td>唯一性定理</td><td>Uniqueness theorems</td><td>3.1.6-3.2.1, 4.4.4, 5.4.3</td></tr><tr><td>位移, 电的</td><td>Displacement, electric</td><td>4.3.1-4.3.3</td></tr><tr><td>位置-时间四维矢量</td><td>Position-time four-vector</td><td>12.1.4</td></tr><tr><td>位置矢量</td><td>Position vector</td><td>1.1.4</td></tr><tr><td>稳定电流</td><td>Steady current</td><td>5.2.1</td></tr><tr><td>涡流</td><td>Eddy currents</td><td>7.1.3</td></tr><tr><td>无散场</td><td>Divergenceless fields</td><td>1.6.2, 5.4.2</td></tr><tr><td>无旋场</td><td>Irrotational field</td><td>1.6.2, 2.3.1, 2.3.2</td></tr><tr><td>无质量粒子</td><td>Massless particle</td><td>12.2.3</td></tr></table>

## X

<table><tr><td>狭义相对论</td><td>Special relativity</td><td>12.1.1-12.3.5</td></tr><tr><td>弦</td><td>String, waves on</td><td>9.1.1-9.2.1</td></tr><tr><td>线电荷</td><td>Line charge</td><td>2.1.4</td></tr><tr><td>线电流</td><td>Line current</td><td>5.1.3</td></tr><tr><td>相变</td><td>Phase transition</td><td>6.4.2</td></tr><tr><td>相对论本构关系</td><td>Relativistic constitutive relations</td><td>12.3.5</td></tr><tr><td>相对论电动力学</td><td>Relativistic electrodynamics</td><td>12.3.1-12.3.5</td></tr><tr><td>相对论动量</td><td>Relativistic momentum</td><td>12.2.2, 12.2.3</td></tr><tr><td>相对论动力学</td><td>Relativistic dynamics</td><td>12.2.4</td></tr><tr><td>相对论力学</td><td>Relativistic mechanics</td><td>12.2.1-12.2.4</td></tr><tr><td>相对论能量</td><td>Relativistic energy</td><td>12.2.2, 12.2.3</td></tr><tr><td>相对论势</td><td>Relativistic potentials</td><td>12.3.5</td></tr><tr><td>相对论运动学</td><td>Relativistic kinematics</td><td>12.2.3, 12.2.4</td></tr><tr><td>相对论质量</td><td>Relativistic mass</td><td>12.2.2</td></tr><tr><td>相对性, 相对论</td><td>Relativity</td><td></td></tr><tr><td>同时的相对性</td><td>of simultaneity</td><td>12.1.2, 12.1.3</td></tr><tr><td>相对性原理</td><td>principle of</td><td>12.1.1, 12.1.2</td></tr><tr><td>狭义相对论</td><td>special</td><td>12.1.1-12.3.5</td></tr><tr><td>相速度</td><td>Phase velocity</td><td>9.4.3</td></tr><tr><td>相位</td><td>Phase</td><td>9.1.2</td></tr><tr><td>相位常数</td><td>Phase constant</td><td>9.1.2, 9.4.1</td></tr><tr><td>线积分</td><td>Line integral</td><td>1.3.1</td></tr><tr><td>线偏振</td><td>Linear polarization</td><td>9.2.1</td></tr><tr><td>线性代数</td><td>Linear algebra</td><td>1.1.5</td></tr><tr><td>线性方程</td><td>Linear equation</td><td>3.3.1, 9.1.2</td></tr><tr><td>线性介质</td><td>Linear medium</td><td>9.3.1</td></tr><tr><td>磁的</td><td>magnetic</td><td>6.3.3-6.4.1</td></tr><tr><td>电的</td><td>electric</td><td>4.3.3-4.4.2</td></tr><tr><td>线性组合</td><td>Linear combination</td><td>3.3.1, 9.1.2, 9.1.3</td></tr><tr><td>线元</td><td>Line element</td><td></td></tr><tr><td>球坐标</td><td>spherical</td><td>1.4.1</td></tr><tr><td>曲线坐标</td><td>curvilinear</td><td>附录 A.4</td></tr><tr><td>直角坐标</td><td>Cartesian</td><td>1.1.4</td></tr><tr><td>柱坐标</td><td>cylindrical</td><td>1.4.2</td></tr><tr><td>现在</td><td>Present</td><td>12.1.4</td></tr><tr><td>协变矢量</td><td>Covariant vector</td><td>12.1.4, 12.3.5</td></tr><tr><td>斜射</td><td>Oblique incidence</td><td>9.3.3</td></tr><tr><td>吸收</td><td>Absorption</td><td>9.4.1–9.4.3</td></tr><tr><td>吸收系数</td><td>Absorption coefficient</td><td>9.4.3</td></tr><tr><td>旋磁比</td><td>Gyromagnetic ratio</td><td>5.4.3</td></tr><tr><td>旋度</td><td>Curl</td><td>1.2.3, 1.2.5, 附录 A.5, 附录 A.6</td></tr><tr><td>A 的</td><td>of A</td><td>5.4.1, 10.1.1</td></tr><tr><td>B 的</td><td>of B</td><td>5.3.1–5.3.3</td></tr><tr><td>D 的</td><td>of D</td><td>4.3.2, 4.3.3</td></tr><tr><td>E 的</td><td>of E</td><td>2.2.1, 2.2.4–2.3.1, 7.2.1</td></tr><tr><td>H 的</td><td>of H</td><td>6.3.1</td></tr><tr><td>在球坐标中</td><td>in spherical coordinates</td><td>1.4.1</td></tr><tr><td>在曲线坐标中</td><td>in curvilinear coordinates</td><td>附录 A.5, 附录 A.6</td></tr><tr><td>在柱坐标中</td><td>in cylindrical coordinates</td><td>1.4.2</td></tr><tr><td>悬浮</td><td>Levitation</td><td>7.3.6</td></tr><tr><td>旋转</td><td>Rotation</td><td>1.1.5</td></tr></table>

## Y

<table><tr><td>亚伯拉罕-洛伦兹公式</td><td>Abraham-Lorentz formula</td><td>11.2.2, 11.2.3, 12.3.5</td></tr><tr><td>压力</td><td>Pressure</td><td></td></tr><tr><td>电磁</td><td>electromagnetic</td><td>8.2.2</td></tr><tr><td>辐射</td><td>radiation</td><td>9.2.3</td></tr><tr><td>静电</td><td>electrostatic</td><td>2.5.3</td></tr><tr><td>哑铃模型</td><td>Dumbbell model</td><td>11.2.3</td></tr><tr><td>赝标量</td><td>Pseudoscalar</td><td>1.1.5</td></tr><tr><td>延迟位置</td><td>Retarded position</td><td>10.3.1</td></tr><tr><td>势的</td><td>potentials</td><td>10.2.1</td></tr><tr><td>延迟位置时间</td><td>Retarded position time</td><td>10.2.1</td></tr><tr><td>赝矢量</td><td>Pseudovector</td><td>1.1.5, 5.1.2</td></tr><tr><td>以太</td><td>Ether</td><td>12.1.1</td></tr><tr><td>以太风</td><td>wind</td><td>12.1.1</td></tr><tr><td>以太拖曳</td><td>drag</td><td>12.1.1</td></tr><tr><td>隐藏动量</td><td>Hidden momentum</td><td>10.3.2, 12.2.4</td></tr><tr><td>应力</td><td>Stress</td><td>8.2.2</td></tr><tr><td>应力张量</td><td>Stress tensor</td><td>8.2.2, 8.2.3</td></tr><tr><td>因果性</td><td>Causality</td><td>10.1.3, 10.2.1, 11.2.2, 12.1.4</td></tr><tr><td>隐矢波</td><td>Evanescent wave</td><td>9.5.3</td></tr><tr><td>永磁体</td><td>Permanent magnet</td><td>6.2.1, 6.4.2</td></tr><tr><td>永电体</td><td>Electret</td><td>4.2.2, 4.3.2</td></tr><tr><td>诱导偶极子</td><td>Induced dipole</td><td>4.1.1-4.1.3</td></tr><tr><td>右手定则</td><td>Right hand rule</td><td>1.1.1</td></tr><tr><td>右手坐标</td><td>Right-handed coordinates</td><td>1.1.2</td></tr><tr><td>预加速</td><td>Preacceleration</td><td>11.2.2, 11.2.3</td></tr><tr><td>余弦定律</td><td>Cosines, law of</td><td>1.1.1</td></tr><tr><td>阈值</td><td>Threshold</td><td>12.3.5</td></tr><tr><td>宇宙光速</td><td>Universal speed of light</td><td>12.1.1</td></tr><tr><td>源点</td><td>Source point</td><td>1.1.4, 2.1.3</td></tr><tr><td>源电荷</td><td>Source charge</td><td>1.1.4, 2.1.1, 5.1.1</td></tr><tr><td>圆偏振</td><td>Circular polarization</td><td>9.2.1</td></tr><tr><td>原子极化率</td><td>Atomic polarizability</td><td>4.1.2, 4.4.4</td></tr></table>

Z

<table><tr><td>张量</td><td>Tensor</td><td>1.1.5</td></tr><tr><td>对称张量</td><td>symmetric</td><td>12.3.3</td></tr><tr><td>对偶张量</td><td>dual</td><td>12.3.3, 12.3.5</td></tr><tr><td>二阶张量</td><td>second-rank</td><td>1.1.5, 12.3.3</td></tr><tr><td>反变张量</td><td>contravariant</td><td>12.3.4</td></tr><tr><td>反对称张量</td><td>antisymmetric</td><td>12.3.3</td></tr><tr><td>极化张量</td><td>polarizability</td><td>4.1.2</td></tr><tr><td>协变张量</td><td>covariant</td><td>12.3.4</td></tr><tr><td>应力张量</td><td>stress</td><td>8.2.2, 8.2.3</td></tr><tr><td>张量场</td><td>field</td><td>12.3.3, 12.3.4</td></tr><tr><td>张量磁化率</td><td>susceptibility</td><td>4.4.1</td></tr><tr><td>折射</td><td>Refraction</td><td>9.3.2, 9.3.3</td></tr><tr><td>折射定律</td><td>law of</td><td>9.3.3</td></tr><tr><td>折射角</td><td>angle of</td><td>9.3.3</td></tr><tr><td>折射系数</td><td>coefficient of</td><td>9.4.3</td></tr><tr><td>折射指数</td><td>index of</td><td>9.3.1, 9.4.3</td></tr><tr><td>正交函数</td><td>Orthogonal functions</td><td>3.3.1, 3.3.2</td></tr><tr><td>正交性</td><td>Orthogonality</td><td>3.3.1, 3.3.2</td></tr><tr><td>正交坐标</td><td>Orthogonal coordinates</td><td>附录 A.1</td></tr><tr><td>正弦波</td><td>Sinusoidal waves</td><td>9.1.2, 9.1.3</td></tr><tr><td>正则动量</td><td>Canonical momentum</td><td>10.1.4</td></tr><tr><td>直角坐标</td><td>Cartesian coordinates</td><td>1.1.2, 3.3.1, 附录 A.1</td></tr><tr><td>质量电磁</td><td>Mass electromagnetic</td><td>11.2.3</td></tr><tr><td>静止的</td><td>rest</td><td>12.2.2</td></tr><tr><td>相对论的</td><td>relativistic</td><td>12.2.2</td></tr><tr><td>质量重整化</td><td>Mass renormalization</td><td>11.2.3</td></tr><tr><td>终极速度</td><td>Terminal velocity</td><td>7.1.3-7.2.1</td></tr><tr><td>驻波</td><td>Standing waves</td><td>9.1.2, 9.5.2</td></tr><tr><td>柱坐标</td><td>Cylindrical coordinates</td><td>1.4.2-1.5.1,附录A.1,附录A.3</td></tr><tr><td>转动矩阵</td><td>Rotation matrix</td><td>1.1.5</td></tr><tr><td>准静态近似</td><td>Quasistatic approximation</td><td>7.2.2, 10.2.2, 10.3.1</td></tr><tr><td>自感系数</td><td>Self-inductance</td><td>7.2.3, 7.2.4</td></tr><tr><td>自作用力</td><td>Self-force</td><td>11.2.3</td></tr><tr><td>纵波</td><td>Longitudinal wave</td><td>9.1.4</td></tr><tr><td>坐标</td><td>Coordinates</td><td></td></tr><tr><td>直角坐标</td><td>Cartesian</td><td>1.1.2,附录A.1,附录A.3</td></tr><tr><td>球坐标</td><td>spherical</td><td>1.4.1, 1.4.2,附录A.1,附录A.3</td></tr><tr><td>曲线坐标</td><td>curvilinear</td><td>1.4.1,附录A.1-附录A.6</td></tr><tr><td>柱坐标</td><td>cylindrical</td><td>1.4.2-1.5.1,附录A.1,附录A.3</td></tr><tr><td>坐标变换</td><td>translation of</td><td>1.1.5</td></tr><tr><td>坐标反演</td><td>inversion of</td><td>1.1.5</td></tr><tr><td>坐标旋转</td><td>rotation of</td><td>1.1.5</td></tr><tr><td>做功</td><td>Work done</td><td>见“能量”</td></tr><tr><td>磁场力做功</td><td>by magnetic forces</td><td>5.1.2, 5.1.3, 8.3</td></tr><tr><td>电容器充电做功</td><td>in charging a capacitor</td><td>2.5.4</td></tr><tr><td>极化电介质中</td><td>in polarizing a dielectric</td><td>4.4.3, 4.4.4</td></tr><tr><td>克服反电动势</td><td>against back emf</td><td>7.2.4</td></tr><tr><td>完成电荷分布</td><td>in setting up a charge configuration</td><td>2.4.1-2.4.3</td></tr><tr><td>移动电介质时</td><td>in moving a dielectric</td><td>4.4.4</td></tr><tr><td>移动线圈时</td><td>in moving a wire loop</td><td>7.1.3</td></tr><tr><td>运动电荷做功</td><td>in moving a charge</td><td>2.4.1, 2.4.2</td></tr><tr><td>左手坐标</td><td>Left-handed coordinates</td><td>1.1.2</td></tr><tr><td>θ函数</td><td>Theta function</td><td>1.5.2</td></tr></table>