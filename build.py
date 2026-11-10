#!/usr/bin/env python3
"""page.html(본문)을 설치형 웹앱용 index.html로 감싸요. 사용법: python3 build.py"""
from pathlib import Path

root = Path(__file__).parent
page = (root / "page.html").read_text(encoding="utf-8")

HEAD = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#f3f4f7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#12141b" media="(prefers-color-scheme: dark)">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="192x192" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="만화카페">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0}img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style>
"""

TAIL = """
<script>
// 설치한 앱이 오프라인에서도 열리도록 서비스 워커를 등록해요.
if ("serviceWorker" in navigator && window.isSecureContext) {
  window.addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
}
</script>
</html>
"""

(root / "index.html").write_text(HEAD + page + TAIL, encoding="utf-8")
print("index.html 생성 완료")
