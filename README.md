[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/FVjNDCrt)
# Title (Please modify the title)
## Team

| ![박패캠](https://avatars.githubusercontent.com/u/156163982?v=4) | ![이패캠](https://avatars.githubusercontent.com/u/156163982?v=4) | ![최패캠](https://avatars.githubusercontent.com/u/156163982?v=4) | ![김패캠](https://avatars.githubusercontent.com/u/156163982?v=4) | ![오패캠](https://avatars.githubusercontent.com/u/156163982?v=4) |
| :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: |
|            [민경도](https://github.com/UpstageAILab)             |            [전승열](https://github.com/UpstageAILab)             |            [이진영](https://github.com/UpstageAILab)             |            [조진우](https://github.com/UpstageAILab)             |            [오패캠](https://github.com/UpstageAILab)             |
|                            팀장, 모듈화, 자동화, 모델링, 2차 모델                            |                            Deaugmentation, 모델링, 2차 모델                             |                            augmentation, 모델링                             |                            augmentation, 모델링                             |                            담당 역할                             |

## 0. Overview
### Environment
- upstage server를 vscode와 ssh로 연결하여 사용
- RTX 3090 

### Requirements
- _Write Requirements_

## 1. Competiton Info

### Overview

- 문서 타입 이미지 분류 대회
- 실제 현업에서의 데이터를 토대로 진행
  

### Timeline

- 시작일) 2024.08.06 (화)
- 마감일) 2024.08.11 (일)
- 대회 세미나) 2024.08.12 (월)

## 2. Components

### Directory

- _Insert your directory structure_

e.g.
```
├── code
│   ├── jupyter_notebooks
│   │   └── model_train.ipynb
│   └── train.py
├── docs
│   ├── pdf
│   │   └── (Template) [패스트캠퍼스] Upstage AI Lab 1기_그룹 스터디 .pptx
│   └── paper
└── input
    └── data
        ├── eval
        └── train
```

## 3. Data descrption

### Dataset overview

- train set : 1570장의 이미지가 담겨 있는 train 폴더 & train.csv, meta.csv
- test set : 3140장의 이미지가 담겨 있는 test 폴더 & sample_submission.csv
- 총 17개의 문서 타입 클래스를 분류하는 문제

### EDA

- Class imbalance
  
![스크린샷 2024-08-13 121657](https://github.com/user-attachments/assets/1a2cfef2-1a1e-4d31-b95c-b4441ce38abc)

  
- train & test Image size
  
![스크린샷 2024-08-13 121717](https://github.com/user-attachments/assets/3e005827-6384-49ab-abb0-b6fe254e7bc1)
  
- TTA

![스크린샷 2024-08-13 121812](https://github.com/user-attachments/assets/70056204-6262-4cbe-8623-56104c2e5e78)

- Disagreements per class

![스크린샷 2024-08-13 121836](https://github.com/user-attachments/assets/027c7e9e-dc09-4511-964b-376b69ecb261)

### Data Processing

- Data cleaning (오류 라벨링 수정)
- Augmentation (albumenations, augraphy)
- Denoising 

## 4. Modeling point 

### Model descrition

- '컴퓨팅 파워와 시간 한계성'에 중점을 둔 model selection
- 허깅페이스의 모델 리더보드에서 w/GFLops를 산정하고 선택한 'vit_tiny_224(380기준)'

### Modeling Process

- '결정 경계(Decision Boundary)가 모호한 일부 라벨들'을 기준
- Label smoothing + Focal Loss -> Smoothed Focal Loss
- Cutmix & Mixup

## 5. Process point

### Process descrition

- 앞서 말한 시간 효율을 위해 결정한 4가지 포인트
- 모듈화, 자동화, 분업화, 자율화

### Processing Process

 모듈화 : 디버깅 용이, 작업 공유성 증대
- 자동화 : W&B, Fastai 실행 및 분석 자동화
- 분업화 : 전처리, 모델링, 후처리 단계로 나누어 역할 수행
- 자율화 : 조직적 분석체계 자동화 설계 후 자율적 실습 진행 

## 6. Result

### Leader Board

![스크린샷 2024-08-13 115900](https://github.com/user-attachments/assets/92226760-8ae2-47c4-95be-a2939edd3775)

### Presentation

[발표용.pptx](https://github.com/user-attachments/files/16593896/default.pptx)


### Meeting Log

- _Insert your meeting log link like Notion or Google Docs_

### Reference

- _Insert related reference_
