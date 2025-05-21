import os
import json
import numpy as np
import pickle
from minilongbench_metrics import *

dataset2metric = {
    "MiniLongBench_narrativeqa": qa_f1_score,
    "MiniLongBench_qasper": qa_f1_score,
    "MiniLongBench_multifieldqa_en": qa_f1_score,
    "MiniLongBench_multifieldqa_zh": qa_f1_zh_score,
    "MiniLongBench_hotpotqa": qa_f1_score,
    "MiniLongBench_2wikimqa": qa_f1_score,
    "MiniLongBench_musique": qa_f1_score,
    "MiniLongBench_dureader": rouge_zh_score,
    "MiniLongBench_gov_report": rouge_score,
    "MiniLongBench_qmsum": rouge_score,
    "MiniLongBench_multi_news": rouge_score,
    "MiniLongBench_vcsum": rouge_zh_score,
    "MiniLongBench_trec": classification_score,
    "MiniLongBench_triviaqa": qa_f1_score,
    "MiniLongBench_samsum": rouge_score,
    "MiniLongBench_lsht": classification_score,
    "MiniLongBench_passage_retrieval_en": retrieval_score,
    "MiniLongBench_passage_count": count_score,
    "MiniLongBench_passage_retrieval_zh": retrieval_zh_score,
    "MiniLongBench_lcc": code_sim_score,
    "MiniLongBench_repobench-p": code_sim_score,
}


def scorer(dataset, predictions, answers, all_classes):
    total_score = 0.
    for (prediction, ground_truths) in zip(predictions, answers):
        score = 0.
        for ground_truth in ground_truths:
            score = max(score, dataset2metric[dataset](prediction, ground_truth, all_classes=all_classes))
        total_score += score
    # print(len(predictions))
    return total_score / len(predictions)


def fun(arr, idx):
    arr = np.array(arr)
    res = np.empty_like(arr)
    for i in range(len(arr)):
        res[idx[i]] = arr[i]
    return res


if __name__ == '__main__':
    all_sc = []
    path1 = r"pred_data/"
    all_model = os.listdir(path1)
    for model in all_model:
        summm = 0
        tmp2 = []
        tmp = 0
        all_scores = []
        file_scores = []
        scen_scores = [0 for i in range(6)]
        print("'", model, "',", sep="" )
        # os.makedirs(f'E:\\testset\\longbench\\longbench_res\\' + model)
        path = path1 + f"\\" + model + f"\\"
        all_files = os.listdir(path)
        # print("Evaluating on:", all_files)
        for filename in all_files:
            if not filename.endswith("json"):
                continue
            predictions, answers, time, scores = [], [], [], []
            dataset = filename.split('.')[0]
            with open(f"{path}{filename}", "r", encoding="utf-8") as f:
                data = json.load(f)  
                # print(data["0"])
                for item in data:
                    item = data[item]
                    predictions.append(item["prediction"])
                    if "all_classes" in item["gold"]:
                        answers.append(item["gold"]["answers"])
                        all_classes = item["gold"]["all_classes"]
                    else:
                        answers.append(item["gold"])
                        all_classes = None
                    # print(predictions[-1], answers[-1])
                    scores.append(scorer(dataset, [predictions[-1]], [answers[-1]], all_classes))
                    # print(scores[-1])
                    if "time" in item:
                        time.append(item["time"])

            # print(dataset, ":", np.mean(scores))
            all_scores += scores

        with open(f"eval_data/{model}_minilongbench_scores.pkl", "wb") as f:
            pickle.dump(all_scores, f)