# 만화카페 · 방어회 비교

찾아둔 만화카페의 요금, 영업시간, 좌석과 분위기를 카드로 비교하는 웹앱이에요. 방어회 집 8곳을 같은 방식으로 비교한 페이지(`bangeo.html`)도 있어요. 폰 홈 화면에 설치할 수 있고(PWA), 한 번 열어 두면 오프라인에서도 보여요.

## 폰에 설치하기

GitHub Pages를 켠 뒤 `https://totocos-bara.github.io/ToonCafe/` 를 열어요. 방어회 비교는 `https://totocos-bara.github.io/ToonCafe/bangeo.html` 이에요.

- **아이폰**: Safari로 열고 공유 버튼 → "홈 화면에 추가"
- **안드로이드**: Chrome으로 열고 메뉴(⋮) → "앱 설치" 또는 "홈 화면에 추가"

## 내용 고치기

1. `page.html`(만화카페, `CAFES` 목록) 또는 `bangeo-page.html`(방어회, `SHOPS` 목록)을 고쳐요.
2. `python3 build.py` 로 `index.html` 과 `bangeo.html` 을 다시 만들어요.
3. 아이콘을 바꾸려면 `tools/icon.html` 을 고친 뒤 `node tools/make-icons.js` 를 실행해요.

카페 정보와 사진 주소는 네이버 지도 업체 페이지에서 가져왔어요(2026-11-10 확인). 사진 파일은 저장소에 두지 않고 네이버 주소에서 바로 불러와요.

카드에 직접 넣은 사진은 그 기기의 브라우저(앱)에만 저장돼요.
