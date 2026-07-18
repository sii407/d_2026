window.addEventListener('load', () => {
    const targetMonth = 5;
    const targetDate = 5;

    const formatter = new Intl.DateTimeFormat("ja-JP", {
        timeZone: "Asia/Tokyo",
        month: "numeric",
        day: "numeric"
    });
    
    const parts = formatter.formatToParts(new Date());
    const currentMonth = parseInt(parts.find(p => p.type === 'month').value, 10) - 1;
    const currentDate = parseInt(parts.find(p => p.type === 'day').value, 10);

    if (currentMonth === targetMonth && currentDate === targetDate) {
        const messageElement = document.getElementById("celebration-message");
        if (messageElement) {
            messageElement.style.display = "block";
        }
    }

    const btnSearch = document.getElementById('btn-search');
    const selectYear = document.getElementById('select-year');
    const selectMonth = document.getElementById('select-month');
    const resultContainer = document.getElementById('result-container');

    if (btnSearch && selectYear && selectMonth && resultContainer) {
        btnSearch.addEventListener('click', () => {
            const year = selectYear.value;
            const month = selectMonth.value;

            if (!month) {
                resultContainer.innerHTML = '<p class="attention">月を選択してください</p>';
                return;
            }

            const fileName = `d_${year}_quiz_${month}.pdf`;
            const buttonText = `${year}年 ${parseInt(month, 10)}月クイズPDFを開く`;

            resultContainer.innerHTML = `
                <a href="${fileName}" class="button" target="_blank" rel="noopener">${buttonText}</a>
            `;
        });
    }
});