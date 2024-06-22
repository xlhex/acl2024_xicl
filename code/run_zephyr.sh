SEED=$1
TASK=$2
PROMPT=$3
BASE_DIR=../output/prompt_zephyr/seed${SEED}

declare -A mapping
declare -A task_mapping
declare -A prompt_mapping

mapping["ISCS"]=../data/testset/iscs.json
mapping["NAN"]=../data/testset/nan.json
mapping["ST"]=../data/testset/st.json
mapping["LILI"]=../data/testset/lili.json
mapping["PICD"]=../data/testset/picd.json
mapping["PISP"]=../data/testset/pisp.json
mapping["HANS"]=../data/testset/hans.json
mapping["SNLI"]=../data/testset/snli.json

task_mapping["ISCS"]=ISCS
task_mapping["NAN"]=NAN
task_mapping["ST"]=ISCS
task_mapping["LILI"]=ISCS
task_mapping["PICD"]=ISCS
task_mapping["PISP"]=ISCS
task_mapping["HANS"]=HANS
task_mapping["SNLI"]=ESNLI

prompt_mapping["icl"]="esnli_no.txt"
prompt_mapping["esnli"]="esnli.txt"
prompt_mapping["xiclfs"]="chatgpt_from_esnli.txt"
prompt_mapping["xiclzs"]="chatgpt_from_scratch.txt"

if [ ! -d $BASE_DIR ];then
    mkdir -p $BASE_DIR
fi

PROMPT=${prompt_mapping[$PROMPT]}
traindata="../data/prompt/full_labels/seed${SEED}/${PROMPT}"
testdata=`echo ${mapping[$TASK]}`
task=`echo ${task_mapping[$TASK]}`
filename="$(basename ${testdata})"
promptname="$(basename ${traindata})"
output=${BASE_DIR}/${filename%.*}.${promptname%.*}.jsonl
echo "python run.py --model_name zephyr --train_file ${traindata} --test_file ${testdata} --task ${task} > ${output}"
python run.py --model_name zephyr --train_file ${traindata} --test_file ${testdata} --task ${task} > ${output}
