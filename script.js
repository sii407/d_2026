window.addEventListener('DOMContentLoaded', () => {
    const targetMonth = 5;
    const targetDate = 5;

    //日本時間を取得
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