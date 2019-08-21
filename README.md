# 홈쇼핑 모아 클론 프로젝트
홈쇼핑 모아 어플리케이션 클론 프로젝트

## 사용된 기술/프레임워크

## 기능

## API

### 카테고리 리스트 받아오기
```
/category
```

### 쇼핑몰 리스트 받아오기
```
/mall
```

### 판매 리스트 받아오기
```
/item/start_date/start_time/mall_name/category_name/orderby
```

#### start date 
쇼핑몰 방송 시작 날자입니다. 기입된 날자 이후부터 시작되는 방송을 포함합니다.


#### start time 
판매 리스트의 시작 시간입니다. 기입된 시간 이후부터 시작되는 방송이 포함됩니다.


#### mall name 
쇼핑몰 이름입니다. 

* all: 모든 쇼핑몰의 방송 정보를 포함합니다.
* cjmall: cj홈쇼핑의 방송 정보만 포함합니다.
* gsshop: gs쇼핑몰의 방송 정보만 포함합니다.
* lottemall: 롯데홈쇼핑의 방송 정보만 포함합니다.
* hmall: 현대홈쇼핑의 방송 정보만 포함합니다.

#### category name
카테고리입니다.

#### orderby
asc

#### 예제
cjmall의 2017년 11월 25일 오후 1시 00분부터 5시까지 방영되는 방송 정보를 가져옵니다.

```
/item/20171125/1300/cjmall/all/asc
```