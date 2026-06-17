window.addEventListener('DOMContentLoaded', () => {
    const targetMonth = 5;
    const targetDate = 5;

    // 💡 日本時間（Asia/Tokyo）の「月」と「日」を確実に取得する
    const now = new Date();
    const japanTimeStr = now.toLocaleString("ja-JP", { timeZone: "Asia/Tokyo" });
    const today = new Date(japanTimeStr);

    if (
        today.getMonth() === targetMonth &&
        today.getDate() === targetDate
    ) {
        const messageElement = document.getElementById("celebration-message");
        if (messageElement) {
            messageElement.style.display = "block";
        }
    }
});