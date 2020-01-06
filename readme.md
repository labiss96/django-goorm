# Goorm Project

국민대학교 멋쟁이사자처럼 교내 해커톤
구름과자 프로젝트



## Index

1. **개요 및 기능**
2. **App 구조**
3. **사이트맵 구조**
4. **DB 구성도**
5. **배포**
6. **개인 임무분담**
7. **기타**



## 개요

- **프로젝트 개요**
  - 쏼라쏼라
- **주 기능**
  - 구름 브랜드
    - 브랜드별 구름리스트 / CRUD
  - 구름과자
    - 검색 / 리스트 / CRUD / 베스트 구름 / 신상 구름
  - 리뷰
  - 개인별 구름다이어리
  - etc..
- **보조/추가 기능**
  - 금연 클리닉
  - etc..



## App 구조

- Goorm Project

- main
- goorm
- accounts



## 사이트맵 구조



## DB 구성도

- **Brand**
  - brdName
- **Tobacco**
  - tobacco_brand(브랜드관계)
  - 제품명
  - 가격
  - 출시일
  - 니코틴 함량
  - 타르 함량
  - 타격감
  - 맨솔 유무
  - 별점(점수)
  - 좋아요 수
  - like_user
- **User**
  - username
  - password
  - email
  - myGoorm?
- **Review**
  - writer(유저관계)
  - pub_date
  - contents



## 배포

- ngrok?
- pythonanywhere
- heroku
- AWS.....



## 개인임무분담

