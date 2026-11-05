# 数学卷公式显示层修复（\text 包裹）变更清单

口径：只把 $…$ 跨度内裸露的中日韩文字/全角标点包进 \text{}，渲染结果与原卷阅读顺序一致，不改数学内容；被编辑题 content_hash 按各文件构建家族算法重算；data/math2/2009-2021 旧哈希本就不可复现，全文件规范化到 finalize_questions.chash 口径。

- math3-2016-12 block[analysis]: \text 包裹
