#!/bin/bash
set -ex

# 获取并格式化开始时间
start_time=$(date +%s) # 时间戳格式
formatted_start_time=$(date "+%Y-%m-%d %H:%M:%S") # 格式化显示

echo "[$(basename "${0}")] Start time: $formatted_start_time"

# 这里执行您的代码或命令
model_name=${1}
model_path=${2}
gpu_ids=${3}
request_count=${4}
result_file=${5}
output_dir=./output/${model_name}

rm -rf ${output_dir}
rm -rf ${output_dir}/result

tasks=("Insertion" "Completion")

source /root/anaconda3/bin/activate activate ds1000

for task in "${tasks[@]}"; do
#  python run_inference-nt.py --mode ${task} --model_name 34b --url http://10.99.211.107:25250/v1/completions --request_count 50
   CUDA_VISIBLE_DEVICES=${gpu_ids} python run_inference-model-nt.py --mode ${task} --output_dir ${output_dir} --model_name ${model_name} --model_path ${model_path} --request_count ${request_count}

   python run_test.py --mode ${task} --model_name ${model_name} --output_dir ${output_dir} --result_file ${result_file}
done

# 获取并格式化结束时间
end_time=$(date +%s) # 时间戳格式
formatted_end_time=$(date "+%Y-%m-%d %H:%M:%S") # 格式化显示

echo "End time: $formatted_end_time"

# 计算总耗时（秒）
total_time=$((end_time - start_time))

# 计算天、小时、分钟和秒
days=$((total_time / 86400))
hours=$(( (total_time % 86400) / 3600 ))
minutes=$(( (total_time % 3600) / 60 ))
seconds=$((total_time % 60))

# 打印耗时
echo "[$(basename "${0}")] Total time taken: $days days, $hours hours, $minutes minutes, $seconds seconds."
