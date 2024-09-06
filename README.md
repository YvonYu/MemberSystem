# Member System

這是一個基於 Flask 和 MongoDB 的簡易會員登入系統，包含用戶登入、註冊和登出功能。此系統使用 `bcrypt` 來加密用戶密碼，以提高安全性。

- 網站框架：Flask
- 資料庫系統：MongoDB
- 雲端服務：AWS

<br>

## 功能

- **會員登入**: 用戶可以使用電子郵件和密碼登入系統。
- **會員註冊**: 用戶可以註冊新帳戶，註冊時會檢查電子郵件是否已被使用。
- **會員登出**: 用戶可以登出，並清除會話中的用戶信息。
- **響應式設計**: 網站設計適合各種設備顯示，包括手機和桌面設備。
- **錯誤處理**: 提供錯誤頁面以顯示註冊和登入過程中的錯誤信息。

<br>

## 專案結構
- `app.py`： 主應用程序檔案，包含 Flask 應用程式及路由。
- `static/`
  - `css/`
    - `index.css`： 會員登入樣式。
    - `signup.css`： 會員註冊樣式。
- `templates/`
  - `error.html`： 錯誤頁面模板。
  - `index.html`： 會員登入模板。
  - `member.html`： 會員頁面模板。
  - `signup.html`： 會員註冊模板。
- `requirements.txt`： 此專案使用的Python套件列表。
- `README.md`： 專案說明文件。

<br>

## 安裝與運行

### 1. 環境配置

 - 確保您的系統上已安裝 Python。
 - 如果尚未安裝，請從 [Python 官方網站](https://www.python.org/downloads/) 下載並安裝。

 - 安裝完成後，您可以使用以下命令來檢查 Python 是否已安裝：
    ```
    python --version
    ```

### 2. Python 套件

 - 確保您已經安裝了所需的 Python 套件。使用以下命令安裝：

    ```
    pip install -r requirements.txt
    ```

### 3. 運行

 - 啟動 Flask 應用程式：
    ```
    python app.py
    ```
 - 打開瀏覽器，訪問 `http://127.0.0.1:3000/` 。
 
 - 首頁（`/`）：會員登入頁面，若非會員，可點擊「Create an account」前往會員註冊頁面。
 - 會員註冊（`/signup`）：會員註冊頁面，若已有帳號，可點擊「SIGN IN」前往登入頁面。
 - 會員頁面（`/member`）：會員頁面，可點擊「Sign Out」登出帳號，會自動前往會員登入頁面。

<br>

## 聯繫我

- Email: Yvonneyuo@gmail.com
- GitHub: [YvonYu](https://github.com/YvonYu)