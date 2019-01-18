# 执行步骤
1. 安装依赖： `npm i`
2. 启动： `npm run dev`

# 感悟
没什么说的，但是最后debug的时候，有个错误： `property filter can't find in undefine`, 从头到尾调了一个下午，原来是JSON多个一个逗号，导致获取不了数据. **F off JSON**
