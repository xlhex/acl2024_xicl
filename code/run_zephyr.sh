#for data in ../data/st_chat_ensli_200.txt  ../data/st_chat_scratch_200.txt  ../data/st_ensli_200.txt  ../data/st_ensli_no_200.txt
#do
#    output="${data%.*}.output13B.json"
#    echo "python fewshot.py ${data} > ${output}"
#    python fewshot.py ${data} > ${output}
#    output="${data%.*}.output13B.json"
#    python llama.py 13B ../data/prompt/full_labels/esnli_no.txt ../data/testset/iscs.json ISCS 0
#done
source activate /home/xuanli/backdoor/envs
export CUDA_VISIBLE_DEVICES=$2

SEED=$1
BASE_DIR=../output/prompt_zephyr/seed${SEED}
declare -A mapping
declare -A task_mapping

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

if [ ! -d $BASE_DIR ];then
    mkdir -p $BASE_DIR
fi

#for testdata in ../data/testset/iscs.json #../data/testset/nan.json ../data/testset/st.json 
#for key in ST PICD LILI PISP
for key in ISCS NAN ST #SNLI PISP PICD HANS
#for key in NAN
do
    #for data in ../data/prompt/full_labels/seed${SEED}/esnli.txt  ../data/prompt/full_labels/seed${SEED}/esnli_no.txt ../data/prompt/full_labels/seed${SEED}/chatgpt_from_esnli.txt  #../data/prompt/full_labels/seed${SEED}/chatgpt_from_scratch.txt
    #for data in ../data/prompt/full_labels/seed${SEED}/chatgpt_from_scratch_logical.txt
    #for data in ../data/prompt/full_labels/seed${SEED}/esnli.txt ../data/prompt/full_labels/seed${SEED}/chatgpt_from_esnli.txt  ../data/prompt/full_labels/seed${SEED}/chatgpt_from_scratch.txt
    for data in ../data/prompt/full_labels/seed${SEED}/mix_from_esnli.txt
    #for data in ../data/prompt/full_labels/seed${SEED}/chatgpt_from_esnli.txt #../data/prompt/full_labels/seed${SEED}/chatgpt_from_scratch.txt
    do
        
        testdata=`echo ${mapping[$key]}`
        task=`echo ${task_mapping[$key]}`
        filename="$(basename ${testdata})"
        promptname="$(basename ${data})"

        #output=${BASE_DIR}/${filename%.*}.${promptname%.*}.output7B.json
        #echo "python llama.py 7B  ${data} ${testdata} ${task} > ${output}"
        #python llama.py 7B  ${data} ${testdata} ${task} > ${output}

        #output=${BASE_DIR}/${filename%.*}.${promptname%.*}.output13B.json
        #echo "python llama.py 13B  ${data} ${testdata} ${task} > ${output}"
        #python llama.py 13B  ${data} ${testdata} ${task} > ${output}

        #output=${BASE_DIR}/${filename%.*}.${promptname%.*}.output30B.json
        #echo "python llama.py 30B  ${data} ${testdata} ${task} > ${output}"
        #python llama.py 30B  ${data} ${testdata} ${task} > ${output}

        #output=${BASE_DIR}/${filename%.*}.${promptname%.*}.output13B.json
        #echo "python llama2.py 13B  ${data} ${testdata} ${task} > ${output}"
        #python llama2.py 13B  ${data} ${testdata} ${task} > ${output}

        output=${BASE_DIR}/${filename%.*}.${promptname%.*}.output7B.json
        echo "python zephyr.py 7B  ${data} ${testdata} ${task} > ${output}"
        python zephyr.py 7B  ${data} ${testdata} ${task} > ${output}

        #output=${BASE_DIR}/${filename%.*}.${promptname%.*}.output65B.json
        #echo "python llama.py 65B  ${data} ${testdata} ${task} > ${output}"
        #python llama.py 65B  ${data} ${testdata} ${task} > ${output}

        #python fewshot.py ${data} > ${output}
        #output="${data%.*}.output13B.json"
        #python llama.py 13B ../data/prompt/full_labels/esnli_no.txt ../data/testset/iscs.json ISCS 0
    done
done
