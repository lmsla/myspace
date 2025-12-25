# 網站部署指南 (Website Deployment Guide)

這個 Repo 現在包含了一個可以直接發布為靜態網站的結構。請按照以下步驟開啟 GitHub Pages 功能。

## 步驟 1: 開啟 Repository Settings

1. 進入此 GitHub Repository 的頁面。
2. 點擊上方的 **Settings** (設定) 分頁。

## 步驟 2: 設定 Pages

1. 在左側選單中找到 **Pages** 選項。
2. 在 **Build and deployment** 區塊下：
    *   **Source**: 選擇 `Deploy from a branch`。
    *   **Branch**: 選擇 `main` (或您當前的分支名稱)。
    *   **Folder**: 選擇 `/docs`。
3. 點擊 **Save** (儲存)。

## 步驟 3: 查看網站

設定完成後，GitHub 會開始建置您的網站。約 1-2 分鐘後，您會在 Pages 設定頁面上方看到網址，格式通常為：

`https://[您的帳號].github.io/[Repo名稱]/`

點擊該連結即可看到您的個人履歷網站！

---

## 如何更新網站內容？

1. **文字內容**：編輯 `docs/index.html`。這是一個標準的 HTML 檔案，您可以直接修改文字。
2. **樣式顏色**：編輯 `docs/styles.css`。您可以調整 `:root` 區塊中的顏色變數。
3. **圖片**：將新圖片放入 `docs/images/` 並更新 HTML 中的 `src` 路徑。
