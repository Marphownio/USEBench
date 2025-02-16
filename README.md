# USEBench


This is the official repository of ACM WWW'25 [paper](https://marphownio.github.io/pdfs/www25_usebench.pdf):
>  Wuyuao Mai, Geng Hong, Pei Chen, Xudong Pan, Baojun Liu, Yuan Zhang, Haixin Duan, and Min Yang. 2025. You Can’t Eat Your Cake and Have It Too: The Performance Degradation of LLMs with Jailbreak Defense. In *Proceedings of the ACM Web Conference 2025 (WWW ’25), April 28–May 2, 2025, Sydney, NSW, Australia.* ACM, New York, NY, USA, 12 pages. https://doi.org/10.1145/3696410.3714632

To comprehensively evaluate the impact of jailbreak defense strategies of LLMs from an end-to-end perspective, we propose **USEBench**, which consists of **U**-Bench for Utility, **S**-Bench for Safety and
**E**-Bench for Exaggerated-safety


## Introduction

**U-Bench** aims to effectively measure the utility of LLMs in practice, containing 570 seed prompts that better reflect real user scenarios while ensuring diversity. U-Bench covers 57 tasks across various fields, using multiple-choice questions to query LLMs.

**S-Bench** evaluates LLMs' performance in handling potential malicious threats. After combining the six jailbreak attack strategies with the 520 seed harmful prompts, we ultimately generated 3,000 adversarial prompts that are ready for direct evaluation. The above six jailbreak attack strategies include *RP*, *PS*, *AE*, *ICA*, *AutoDAN-HGA*, *Cold-Attack*.


**E-Bench** examines the false refusal behavior of LLMs that may limit normal functionality, containing 500 pseudo-harmful prompts such as *how to kill a mosquito*


By combining data from these three sub-benches, our research can evaluate the performance of LLMs in the Utility, Safety, and Usability, both before and after the introduction of jailbreak defense strategies in a comprehensive, objective, and accurate way.


## Project Structure

```
.
├── E-Bench
│   └── usability_test_prompt.csv
├── README.md
├── S-Bench
│   ├── AS.csv
│   ├── AutoDAN-HGA
│   │   ├── GPT-3.5-turbo.csv
│   │   ├── GPT-4-turbo.csv
│   │   ├── Llama-2-7b-chat-hf.csv
│   │   ├── Meta-Llama-3-8B-Instruct.csv
│   │   ├── Mistral-7B-Instruct-v0.2.csv
│   │   ├── Mistral-7B-Instruct-v0.3.csv
│   │   └── Vicuna-7b-v1.5.csv
│   ├── Cold-Attack
│   │   ├── GPT-3.5-Turbo.csv
│   │   ├── GPT-4-Turbo.csv
│   │   ├── Llama-2-7b-chat-hf.csv
│   │   ├── Meta-Llama-3-8B-Instruct.csv
│   │   ├── Mistral-7B-Instruct-v0.2.csv
│   │   ├── Mistral-7B-Instruct-v0.3.csv
│   │   └── Vicuna-7b-v1.5.csv
│   ├── get.py
│   ├── ICA.csv
│   ├── PE.csv
│   └── RP.csv
└── U-Bench
    └── utility_test_prompt.csv
```

## Citation
If you find our work helpful, we would greatly appreciate it if you could cite our paper using the following BibTeX format.

```
@inproceedings{mai2025usebench,
     author = {Wuyuao Mai and Geng Hong and Pei Chen and Xudong Pan and Baojun Liu and Yuan Zhang and Haixin Duan and Min Yang},
     title = {You Can’t Eat Your Cake and Have It Too: The Performance Degradation of LLMs with Jailbreak Defense},
     booktitle = {Proceedings of the ACM Web Conference 2025 (WWW '25)},
     year = {2025},
     month = {April 28--May 2},
     location = {Sydney, NSW, Australia},
     publisher = {ACM},
     address = {New York, NY, USA},
     pages = {12},
     doi = {10.1145/3696410.3714632}
}
```



