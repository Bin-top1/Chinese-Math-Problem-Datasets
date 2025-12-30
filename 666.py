from datasets import load_dataset
import os

# 指定本地缓存路径和保存路径
cache_path = "H:/math_dataset/camel_math"
save_path = "H:/math_dataset/camel_math/jsonl"
os.makedirs(save_path, exist_ok=True)

# 加载数据集
dataset = load_dataset("rvv-karma/Math-QA", cache_dir=cache_path)

# 保存各个子集（如 train/validation/test）为 jsonl 格式
for split in dataset:
    jsonl_file = os.path.join(save_path, f"{split}.jsonl")
    dataset[split].to_json(jsonl_file, orient="records", lines=True, force_ascii=False)
    print(f"已保存：{jsonl_file}")
