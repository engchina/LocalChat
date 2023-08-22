# LocalChat
Chat with your local document

# 部署说明

创建虚拟环境：

```
conda create -n localchat python==3.10 -y
conda activate localchat
```

通过 PyPI 安装 LangChain、Milvus 和 Xinference：

```
pip install langchain milvus "xinference[all]"
```

在本地 19530 端口启动 Milvus 向量检索服务：

```
milvus-server
```

在本地 9997 端口启动 (Xinference](https://github.com/xorbitsai/inference) 模型推理服务：

```
xinference
```

启动 chatglm2 模型：


```
xinference launch --model-name "chatglm2" \
   --model-format pytorch \
   --size-in-billions 6 \
   --endpoint "http://127.0.0.1:9997"
```

上述命令会返回 model_uid，可以利用它在 LangChain 中与它们交互。

```
Model uid: 364f1906-407b-11ee-b0c3-00155d24d368
```

运行以下命令查看内置模型：

```
xinference list
```

安装 pip install pymilvus:

```
pip install pymilvus
```