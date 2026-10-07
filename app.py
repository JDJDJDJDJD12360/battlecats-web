from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
import uvicorn
import bcsfe  # 냥코 세이브 변조 라이브러리

app = FastAPI(title="Battle Cats Save Editor Web")


# 1. 메인 웹 커스텀 페이지 (HTML UI)
@app.get("/", response_class=HTMLResponse)
async def index():
  return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>냥코대전쟁 세이브 커스텀 대시보드</title>
        <style>
            body { background-color: #1a1a1a; color: #f0f0f0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; padding: 40px; }
            .container { max-width: 600px; margin: 0 auto; background: #2b2b2b; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
            h2 { color: #ff9900; text-align: center; margin-bottom: 25px; }
            .section { margin-bottom: 20px; padding: 15px; background: #333; border-radius: 8px; }
            label { display: block; margin: 8px 0; cursor: pointer; }
            input[type="text"], input[type="number"] { width: 100%; padding: 8px; margin-top: 5px; background: #222; border: 1px solid #555; color: #fff; border-radius: 4px; box-sizing: border-box; }
            input[type="checkbox"] { margin-right: 8px; transform: scale(1.2); }
            button { width: 100%; padding: 12px; background: #ff6600; color: white; border: none; font-size: 16px; font-weight: bold; border-radius: 6px; cursor: pointer; transition: 0.2s; }
            button:hover { background: #ff8533; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>🐱 냥코대전쟁 종합 세이브 커스텀</h2>
            <form action="/process" method="post">
                
                <div class="section">
                    <h3>1. 계정 인증 정보</h3>
                    <label>이어하기 코드 (Transfer Code)
                        <input type="text" name="transfer_code" placeholder="코드를 입력하세요" required>
                    </label>
                    <label>인증 번호 (Confirmation Code)
                        <input type="text" name="confirmation_code" placeholder="인증 번호를 입력하세요" required>
                    </label>
                </div>

                <div class="section">
                    <h3>2. 재화 설정</h3>
                    <label>통조림 (Catfood)
                        <input type="number" name="catfood" value="49000">
                    </label>
                    <label>경험치 (XP)
                        <input type="number" name="xp" value="99999999">
                    </label>
                </div>

                <div class="section">
                    <h3>3. 종합 기능 옵션</h3>
                    <label><input type="checkbox" name="unlock_all_cats" checked> 모든 캐릭터 해금 및 강화</label>
                    <label><input type="checkbox" name="clear_all_stages" checked> 모든 스테이지 및 보물 100% 올클리어</label>
                    <label><input type="checkbox" name="max_talents" checked> 모든 본능(Talents) 최대 개방</label>
                </div>

                <button type="submit">세이브 변조 및 새 이어하기 코드 발급</button>
            </form>
        </div>
    </body>
    </html>
    """


# 2. 폼 데이터를 받아 실제 냥코 세이브를 조작하고 새 코드를 발급하는 로직
@app.post("/process", response_class=HTMLResponse)
async def process_save(
    transfer_code: str = Form(...),
    confirmation_code: str = Form(...),
    catfood: int = Form(...),
    xp: int = Form(...),
    unlock_all_cats: bool = Form(False),
    clear_all_stages: bool = Form(False),
    max_talents: bool = Form(False),
):
  try:
    country_code = "kr"  # 한국 서버 기준

    # 1. 서버에서 이어하기 코드로 세이브 데이터 다운로드 및 복호화
    # save_file, _ = bcsfe.core.FileDialog.download_save_aes(transfer_code, confirmation_code, country_code)

    # 2. 유저가 웹에서 선택/입력한 값 적용
    # save_file.set_catfood(catfood)
    # save_file.set_xp(xp)
    # if unlock_all_cats:
    #     save_file.unlock_all_characters()
    # if clear_all_stages:
    #     save_file.clear_all_stages_and_treasures()
    # if max_talents:
    #     save_file.max_talents()

    # 3. 무결성 체크섬 재계산 후 포노스 서버에 업로드하고 새 코드 발급
    # new_transfer_code, new_confirmation_code = bcsfe.core.FileDialog.upload_save_aes(save_file, country_code)

    # (시뮬레이션용 예시 값 - 실제 라이브러리 연동 시 위 주석의 코드를 활성화하세요)
    new_transfer_code = "ABC123XYZ (새로 발급된 코드 예시)"
    new_confirmation_code = "5678"

    return f"""
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <title>변조 완료</title>
            <style>
                body {{ background-color: #1a1a1a; color: #f0f0f0; font-family: sans-serif; padding: 40px; text-align: center; }}
                .box {{ max-width: 500px; margin: 0 auto; background: #2b2b2b; padding: 30px; border-radius: 12px; border: 2px solid #00cc66; }}
                h2 {{ color: #00cc66; }}
                .code-box {{ background: #111; padding: 15px; margin: 15px 0; border-radius: 6px; font-family: monospace; font-size: 18px; color: #ffcc00; }}
            </style>
        </head>
        <body>
            <div class="box">
                <h2>✅ 세이브 데이터 변조 성공!</h2>
                <p>아래의 새로운 이어하기 코드를 복사하여 게임 내에서 로그인하세요.</p>
                <div class="code-box">
                    이어하기 코드: {new_transfer_code}<br>
                    인증 번호: {new_confirmation_code}
                </div>
                <p style="color: #aaa; font-size: 13px;">※ 기존의 이어하기 코드는 폐기되었으니 반드시 이 새 코드를 사용하세요.</p>
                <br>
                <a href="/" style="color: #ff9900; text-decoration: none; font-weight: bold;">← 메인으로 돌아가기</a>
            </div>
        </body>
        </html>
        """

  except Exception as e:
    return f"""
        <body style="background-color: #1a1a1a; color: #ff5555; font-family: sans-serif; padding: 40px; text-align: center;">
            <h2>❌ 처리 중 오류가 발생했습니다</h2>
            <p>입력하신 이어하기 코드나 인증 번호가 올바르지 않거나, 서버 통신에 실패했습니다.</p>
            <p><b>에러 내용:</b> {str(e)}</p>
            <br><a href="/" style="color: #fff;">돌아가기</a>
        </body>
        """


if __name__ == "__main__":
  uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
