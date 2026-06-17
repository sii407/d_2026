const targetMonth = 5;
const targetDate = 5;

const today = new Date();

if (
    today.getMonth() === targetMonth &&
    today.getDate() === targetDate
) {
    document.getElementById("celebration-message").style.display = "block";
}